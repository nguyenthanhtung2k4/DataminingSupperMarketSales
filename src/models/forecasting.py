from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX

from src.evaluation.metrics import mae, rmse, smape


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
    seasonal_periods = config["seasonal_periods"]
    trend = config["trend"]
    seasonal = config["seasonal"] if len(train) >= seasonal_periods * 2 else None
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
    train, test = _split_time_series(ts_df, forecasting_cfg["horizon"])
    y_train = train["y"]
    y_test = test["y"].to_numpy()

    models: list[tuple[str, Any]] = [
        ("naive", lambda: _naive_forecast(y_train, len(test))),
        (
            "moving_average",
            lambda: _moving_average_forecast(
                y_train,
                len(test),
                forecasting_cfg["moving_average_window"],
            ),
        ),
        (
            "holt_winters",
            lambda: _holt_winters_forecast(
                y_train,
                len(test),
                forecasting_cfg["holt_winters"],
            ),
        ),
        (
            "sarimax",
            lambda: _sarimax_forecast(
                y_train,
                len(test),
                forecasting_cfg["sarimax"],
            ),
        ),
    ]

    prediction_df = test.copy()
    comparison_rows: list[dict[str, Any]] = []
    for model_name, runner in models:
        try:
            predicted = runner()
            prediction_df[model_name] = predicted
            comparison_rows.append(
                {"model": model_name, "status": "ok", **_evaluate_forecast(y_test, np.asarray(predicted))}
            )
        except Exception as exc:
            prediction_df[model_name] = np.nan
            comparison_rows.append(
                {
                    "model": model_name,
                    "status": f"failed: {exc}",
                    "MAE": np.nan,
                    "RMSE": np.nan,
                    "sMAPE": np.nan,
                }
            )

    comparison_df = pd.DataFrame(comparison_rows).sort_values(
        ["sMAPE", "RMSE", "MAE"], ascending=[True, True, True], na_position="last"
    )

    best_row = comparison_df.dropna(subset=["sMAPE"]).iloc[0]
    best_model = best_row["model"]
    residual_df = prediction_df[["ds", "y", best_model]].copy()
    residual_df["residual"] = residual_df["y"] - residual_df[best_model]
    residual_df = residual_df.rename(columns={"y": "actual", best_model: "predicted"})

    return comparison_df.reset_index(drop=True), prediction_df, residual_df

