from __future__ import annotations

import argparse
import copy
import itertools
import sys
from pathlib import Path
from typing import Any

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import ensure_output_directories, load_params, resolve_path, save_params
from src.data import clean_sales_data, load_raw_data
from src.evaluation import rank_metrics_for_task, write_dataframe
from src.features import build_basket_transactions, build_customer_features, build_weekly_sales
from src.mining import mine_association_rules, run_customer_clustering
from src.models import run_forecasting_experiment


def _prepare_context(config: dict[str, Any]) -> tuple[pd.DataFrame, pd.DataFrame]:
    raw_df = load_raw_data(config, PROJECT_ROOT)
    cleaned_df, _ = clean_sales_data(raw_df, config)
    customer_features = build_customer_features(cleaned_df)
    return cleaned_df, customer_features


def _select_best(task: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        raise ValueError(f"No experiment results were produced for task: {task}")
    return max(rows, key=lambda row: rank_metrics_for_task(task, row))


def _association_priority(row: dict[str, Any]) -> tuple[int, tuple[float, ...]]:
    readable = 1 if 8 <= int(row["rule_count"]) <= 20 else 0
    return (readable, rank_metrics_for_task("association", row))


def run_association_experiments(config: dict[str, Any]) -> tuple[dict[str, Any], Path]:
    cleaned_df, _ = _prepare_context(config)
    transactions_df = build_basket_transactions(
        cleaned_df,
        item_level=config["preprocessing"]["basket_item_level"],
    )

    summary_rows: list[dict[str, Any]] = []
    base_cfg = copy.deepcopy(config["association"])
    level2_candidates: list[dict[str, Any]] = []

    for min_support, min_confidence, min_lift in itertools.product(
        [0.01, 0.015, 0.02],
        [0.02, 0.05, 0.10],
        [1.00, 1.05],
    ):
        trial_cfg = copy.deepcopy(config)
        trial_cfg["association"] = {
            **base_cfg,
            "min_support": min_support,
            "min_confidence": min_confidence,
            "min_lift": min_lift,
            "max_length": 2,
        }
        _, rules_df = mine_association_rules(transactions_df, trial_cfg)
        metrics = {
            "min_support": min_support,
            "min_confidence": min_confidence,
            "min_lift": min_lift,
            "max_length": 2,
            "rule_count": int(len(rules_df)),
            "max_lift": float(rules_df["lift"].max()) if not rules_df.empty else 0.0,
            "avg_lift_top5": float(rules_df["lift"].head(5).mean()) if not rules_df.empty else 0.0,
        }
        summary_rows.append(metrics)
        level2_candidates.append(metrics)

    top_two = sorted(level2_candidates, key=_association_priority, reverse=True)[:2]
    for candidate in top_two:
        trial_cfg = copy.deepcopy(config)
        trial_cfg["association"] = {
            **base_cfg,
            "min_support": candidate["min_support"],
            "min_confidence": candidate["min_confidence"],
            "min_lift": candidate["min_lift"],
            "max_length": 3,
        }
        _, rules_df = mine_association_rules(transactions_df, trial_cfg)
        summary_rows.append(
            {
                "min_support": candidate["min_support"],
                "min_confidence": candidate["min_confidence"],
                "min_lift": candidate["min_lift"],
                "max_length": 3,
                "rule_count": int(len(rules_df)),
                "max_lift": float(rules_df["lift"].max()) if not rules_df.empty else 0.0,
                "avg_lift_top5": float(rules_df["lift"].head(5).mean()) if not rules_df.empty else 0.0,
            }
        )

    best_result = max(summary_rows, key=_association_priority)
    summary_df = pd.DataFrame(summary_rows).sort_values(
        ["avg_lift_top5", "rule_count", "max_lift"],
        ascending=[False, False, False],
    )
    output_path = write_dataframe(
        summary_df.round(6),
        resolve_path(config["paths"]["tables_dir"], PROJECT_ROOT) / "experiment_association_report.csv",
    )

    best_config = {
        **base_cfg,
        "min_support": best_result["min_support"],
        "min_confidence": best_result["min_confidence"],
        "min_lift": best_result["min_lift"],
        "max_length": int(best_result["max_length"]),
    }
    return best_config, output_path


def run_clustering_experiments(config: dict[str, Any]) -> tuple[dict[str, Any], Path]:
    _, customer_features = _prepare_context(config)

    feature_sets = {
        "F1": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories"],
        "F2": [
            "recency_days",
            "order_count",
            "total_sales",
            "avg_order_value",
            "unique_subcategories",
            "active_days",
        ],
        "F3": ["recency_days", "order_count", "total_sales", "unique_subcategories", "total_quantity"],
        "F4": ["recency_days", "total_sales", "avg_order_value", "active_days", "total_quantity"],
    }

    summary_rows: list[dict[str, Any]] = []
    base_cfg = copy.deepcopy(config["clustering"])
    for feature_set_name, features in feature_sets.items():
        trial_cfg = copy.deepcopy(config)
        trial_cfg["clustering"] = {
            **base_cfg,
            "features": features,
            "candidate_k": [2, 3, 4, 5, 6],
        }
        comparison_df, _, _ = run_customer_clustering(customer_features, trial_cfg)
        current_rows = comparison_df.copy()
        current_rows["feature_set"] = feature_set_name
        current_rows["feature_list"] = ", ".join(features)
        summary_rows.extend(current_rows.to_dict("records"))

    best_result = _select_best("clustering", summary_rows)
    summary_df = pd.DataFrame(summary_rows).sort_values(
        ["silhouette", "davies_bouldin", "max_cluster_share"],
        ascending=[False, True, True],
    )
    output_path = write_dataframe(
        summary_df.round(6),
        resolve_path(config["paths"]["tables_dir"], PROJECT_ROOT) / "experiment_clustering_report.csv",
    )

    best_config = {
        **base_cfg,
        "features": feature_sets[best_result["feature_set"]],
        "candidate_k": [2, 3, 4, 5, 6],
    }
    return best_config, output_path


def _forecast_trial(
    cleaned_df: pd.DataFrame,
    config: dict[str, Any],
    frequency: str,
    horizon: int,
    moving_average_window: int,
    seasonal_periods: int,
    sarimax_order: tuple[int, int, int],
    sarimax_seasonal_order: tuple[int, int, int, int],
) -> dict[str, Any]:
    trial_cfg = copy.deepcopy(config)
    trial_cfg["forecasting"] = {
        **trial_cfg["forecasting"],
        "frequency": frequency,
        "horizon": horizon,
        "moving_average_window": moving_average_window,
        "holt_winters": {
            **trial_cfg["forecasting"]["holt_winters"],
            "seasonal_periods": seasonal_periods,
        },
        "sarimax": {
            "order": list(sarimax_order),
            "seasonal_order": list(sarimax_seasonal_order),
        },
    }
    ts_df = build_weekly_sales(
        cleaned_df,
        frequency=frequency,
        target_column=trial_cfg["forecasting"]["target_column"],
    )
    comparison_df, _, _ = run_forecasting_experiment(ts_df, trial_cfg)
    best_model_row = comparison_df.dropna(subset=["sMAPE"]).iloc[0].to_dict()
    return {
        "frequency": frequency,
        "horizon": horizon,
        "moving_average_window": moving_average_window,
        "holt_winters_period": seasonal_periods,
        "sarimax_order": str(sarimax_order),
        "sarimax_seasonal_order": str(sarimax_seasonal_order),
        "best_model": best_model_row["model"],
        "MAE": float(best_model_row["MAE"]),
        "RMSE": float(best_model_row["RMSE"]),
        "sMAPE": float(best_model_row["sMAPE"]),
    }


def run_forecasting_experiments(config: dict[str, Any]) -> tuple[dict[str, Any], Path]:
    cleaned_df, _ = _prepare_context(config)
    summary_rows: list[dict[str, Any]] = []

    weekly_model_grid = [
        ((1, 1, 1), (1, 0, 0, 13), 13),
        ((1, 1, 1), (1, 0, 0, 52), 52),
        ((1, 0, 1), (1, 0, 0, 13), 13),
        ((2, 1, 1), (1, 0, 0, 13), 13),
    ]
    for moving_average_window, (order, seasonal_order, seasonal_periods) in itertools.product(
        [2, 4, 8],
        weekly_model_grid,
    ):
        summary_rows.append(
            _forecast_trial(
                cleaned_df=cleaned_df,
                config=config,
                frequency="W-MON",
                horizon=12,
                moving_average_window=moving_average_window,
                seasonal_periods=seasonal_periods,
                sarimax_order=order,
                sarimax_seasonal_order=seasonal_order,
            )
        )

    best_weekly = _select_best("forecasting", summary_rows)
    if best_weekly["sMAPE"] > 35:
        monthly_trials = list(
            itertools.product(
                [3],
                [(1, 1, 1), (1, 0, 1), (2, 1, 1)],
            )
        )
        for moving_average_window, order in monthly_trials:
            summary_rows.append(
                _forecast_trial(
                    cleaned_df=cleaned_df,
                    config=config,
                    frequency="MS",
                    horizon=6,
                    moving_average_window=moving_average_window,
                    seasonal_periods=12,
                    sarimax_order=order,
                    sarimax_seasonal_order=(1, 0, 0, 12),
                )
            )

    best_result = _select_best("forecasting", summary_rows)
    summary_df = pd.DataFrame(summary_rows).sort_values(
        ["sMAPE", "RMSE", "MAE"],
        ascending=[True, True, True],
    )
    output_path = write_dataframe(
        summary_df.round(6),
        resolve_path(config["paths"]["tables_dir"], PROJECT_ROOT) / "experiment_forecasting_report.csv",
    )

    sarimax_order = [int(value.strip()) for value in best_result["sarimax_order"].strip("()").split(",")]
    sarimax_seasonal_order = [
        int(value.strip()) for value in best_result["sarimax_seasonal_order"].strip("()").split(",")
    ]
    best_config = {
        **config["forecasting"],
        "frequency": best_result["frequency"],
        "horizon": int(best_result["horizon"]),
        "moving_average_window": int(best_result["moving_average_window"]),
        "holt_winters": {
            **config["forecasting"]["holt_winters"],
            "seasonal_periods": int(best_result["holt_winters_period"]),
        },
        "sarimax": {
            "order": sarimax_order,
            "seasonal_order": sarimax_seasonal_order,
        },
    }
    return best_config, output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run controlled parameter sweeps for the final report.")
    parser.add_argument(
        "--task",
        choices=["association", "clustering", "forecasting", "all"],
        default="all",
        help="Which task to tune.",
    )
    parser.add_argument(
        "--preset",
        choices=["report"],
        default="report",
        help="Experiment preset. Only 'report' is currently supported.",
    )
    parser.add_argument("--config", dest="config_path", default=None, help="Optional path to params.yaml")
    parser.add_argument(
        "--apply-best",
        action="store_true",
        help="Write the selected best parameters back to the config file.",
    )
    args = parser.parse_args()

    config = load_params(args.config_path)
    ensure_output_directories(config, PROJECT_ROOT)

    selected_tasks = [args.task] if args.task != "all" else ["association", "clustering", "forecasting"]
    updated_config = copy.deepcopy(config)
    results: list[tuple[str, Path]] = []

    if "association" in selected_tasks:
        best_association, output_path = run_association_experiments(updated_config)
        updated_config["association"] = best_association
        results.append(("association", output_path))

    if "clustering" in selected_tasks:
        best_clustering, output_path = run_clustering_experiments(updated_config)
        updated_config["clustering"] = best_clustering
        results.append(("clustering", output_path))

    if "forecasting" in selected_tasks:
        best_forecasting, output_path = run_forecasting_experiments(updated_config)
        updated_config["forecasting"] = best_forecasting
        results.append(("forecasting", output_path))

    if args.apply_best:
        config_path = save_params(updated_config, args.config_path)
        print(f"Updated config: {config_path}")

    for task, output_path in results:
        print(f"{task}: {output_path}")


if __name__ == "__main__":
    main()
