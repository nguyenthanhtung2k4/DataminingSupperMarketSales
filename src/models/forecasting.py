from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX

from src.evaluation.metrics import mae, rmse, smape

try:
    from prophet import Prophet
except ImportError:  # pragma: no cover - optional dependency
    Prophet = None


def _split_time_series(ts_df: pd.DataFrame, horizon: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    clean = ts_df[["ds", "y"]].dropna().reset_index(drop=True)
    if len(clean) <= horizon + 8:
        raise ValueError(
            "Time series is too short for forecasting. Increase data size or reduce horizon."
        )
    train = clean.iloc[:-horizon].reset_index(drop=True)
    test = clean.iloc[-horizon:].reset_index(drop=True)
    return train, test


def _naive_forecast(train: pd.Series, horizon: int) -> np.ndarray:
    return np.repeat(train.iloc[-1], horizon)


def _moving_average_forecast(train: pd.Series, horizon: int, window: int) -> np.ndarray:
    return np.repeat(train.tail(window).mean(), horizon)


def _holt_winters_forecast(train: pd.Series, horizon: int, config: dict[str, Any]) -> np.ndarray:
    seasonal_periods = int(config["seasonal_periods"])
    trend = config.get("trend")
    seasonal = config.get("seasonal") if len(train) >= seasonal_periods * 2 else None
    model = ExponentialSmoothing(
        train,
        trend=trend,
        seasonal=seasonal,
        seasonal_periods=seasonal_periods if seasonal else None,
    )
    fitted = model.fit(optimized=True)
    return fitted.forecast(horizon).to_numpy()


def _sarimax_forecast(train: pd.Series, horizon: int, config: dict[str, Any]) -> np.ndarray:
    model = SARIMAX(
        train,
        order=tuple(config["order"]),
        seasonal_order=tuple(config["seasonal_order"]),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    fitted = model.fit(disp=False)
    return fitted.forecast(horizon).to_numpy()


def _prophet_forecast(train_df: pd.DataFrame, horizon: int, frequency: str, config: dict[str, Any]) -> np.ndarray:
    if Prophet is None:
        raise ImportError("prophet is not installed in the current environment.")
    model = Prophet(
        seasonality_mode=config.get("seasonality_mode", "additive"),
        yearly_seasonality=config.get("yearly_seasonality", True),
        weekly_seasonality=config.get("weekly_seasonality", False),
        daily_seasonality=config.get("daily_seasonality", False),
    )
    model.fit(train_df.rename(columns={"ds": "ds", "y": "y"}))
    future = model.make_future_dataframe(periods=horizon, freq=frequency, include_history=False)
    forecast = model.predict(future)
    return forecast["yhat"].to_numpy()


def _evaluate_forecast(actual: np.ndarray, predicted: np.ndarray) -> dict[str, float]:
    return {
        "MAE": round(mae(actual, predicted), 6),
        "RMSE": round(rmse(actual, predicted), 6),
        "sMAPE": round(smape(actual, predicted), 6),
    }


def run_forecasting_experiment(
    ts_df: pd.DataFrame,
    config: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    forecasting_cfg = config["forecasting"]
    train, test = _split_time_series(ts_df, int(forecasting_cfg["horizon"]))
    y_train = train["y"]
    y_test = test["y"].to_numpy()
    frequency = forecasting_cfg["frequency"]

    models: list[tuple[str, Any]] = []
    for model_name in forecasting_cfg.get("enabled_models", []):
        if model_name == "naive":
            models.append(("naive", lambda: _naive_forecast(y_train, len(test))))
        elif model_name == "moving_average":
            models.append(
                (
                    "moving_average",
                    lambda: _moving_average_forecast(
                        y_train,
                        len(test),
                        int(forecasting_cfg["moving_average_window"]),
                    ),
                )
            )
        elif model_name == "holt_winters":
            models.append(
                (
                    "holt_winters",
                    lambda: _holt_winters_forecast(
                        y_train,
                        len(test),
                        forecasting_cfg["holt_winters"],
                    ),
                )
            )
        elif model_name == "sarimax":
            models.append(
                (
                    "sarimax",
                    lambda: _sarimax_forecast(
                        y_train,
                        len(test),
                        forecasting_cfg["sarimax"],
                    ),
                )
            )
        elif model_name == "prophet":
            models.append(
                (
                    "prophet",
                    lambda: _prophet_forecast(
                        train[["ds", "y"]],
                        len(test),
                        frequency,
                        forecasting_cfg.get("prophet", {}),
                    ),
                )
            )

    prediction_df = test.copy()
    comparison_rows: list[dict[str, Any]] = []
    for model_name, runner in models:
        try:
            predicted = np.asarray(runner(), dtype=float)
            prediction_df[model_name] = predicted
            comparison_rows.append(
                {"model": model_name, "status": "ok", **_evaluate_forecast(y_test, predicted)}
            )
        except Exception as exc:
            prediction_df[model_name] = np.nan
            comparison_rows.append(
                {
                    "model": model_name,
                    "status": f"unavailable: {exc}",
                    "MAE": np.nan,
                    "RMSE": np.nan,
                    "sMAPE": np.nan,
                }
            )

    comparison_df = pd.DataFrame(comparison_rows).sort_values(
        ["sMAPE", "RMSE", "MAE"], ascending=[True, True, True], na_position="last"
    )

    valid_rows = comparison_df.dropna(subset=["sMAPE"])
    if valid_rows.empty:
        raise ValueError("No forecasting model produced valid metrics.")

    best_row = valid_rows.iloc[0]
    best_model = str(best_row["model"])
    residual_df = prediction_df[["ds", "y", best_model]].copy()
    residual_df["residual"] = residual_df["y"] - residual_df[best_model]
    residual_df = residual_df.rename(columns={"y": "actual", best_model: "predicted"})

    return comparison_df.reset_index(drop=True), prediction_df, residual_df
