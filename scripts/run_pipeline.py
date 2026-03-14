from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import ensure_output_directories, load_params, resolve_path
from src.data import clean_sales_data, load_raw_data, schema_snapshot
from src.evaluation import export_tracking_summary, log_experiment, write_dataframe
from src.features import build_basket_transactions, build_customer_features, build_weekly_sales
from src.mining import mine_association_rules, run_customer_clustering
from src.models import run_forecasting_experiment
from src.visualization import plot_cluster_profile, plot_forecast, plot_sales_over_time, plot_top_categories


def _write_json(data: dict, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def run_pipeline(config_path: str | None = None, check_only: bool = False) -> None:
    config = load_params(config_path)
    ensure_output_directories(config, PROJECT_ROOT)

    raw_data_path = resolve_path(config["paths"]["raw_data"], PROJECT_ROOT)
    processed_dir = resolve_path(config["paths"]["processed_dir"], PROJECT_ROOT)
    tables_dir = resolve_path(config["paths"]["tables_dir"], PROJECT_ROOT)
    figures_dir = resolve_path(config["paths"]["figures_dir"], PROJECT_ROOT)

    raw_df = load_raw_data(config, PROJECT_ROOT)
    schema_df = schema_snapshot(raw_df)
    write_dataframe(schema_df, tables_dir / "schema_snapshot.csv")

    if check_only:
        print(f"Schema check passed. Raw rows: {len(raw_df)}")
        return

    cleaned_df, cleaning_report = clean_sales_data(raw_df, config)
    write_dataframe(cleaned_df, processed_dir / "cleaned_sales.csv")
    _write_json(cleaning_report, tables_dir / "cleaning_report.json")

    customer_features = build_customer_features(cleaned_df)
    weekly_sales = build_weekly_sales(
        cleaned_df,
        frequency=config["forecasting"]["frequency"],
        target_column=config["forecasting"]["target_column"],
    )
    transactions_df = build_basket_transactions(
        cleaned_df,
        item_level=config["preprocessing"]["basket_item_level"],
    )

    write_dataframe(customer_features, processed_dir / "customer_features.csv")
    write_dataframe(weekly_sales, processed_dir / "weekly_sales.csv")
    write_dataframe(transactions_df, processed_dir / "transactions.csv")

    top_categories_fig = plot_top_categories(cleaned_df, figures_dir / "top_subcategories.png")
    sales_timeline_fig = plot_sales_over_time(weekly_sales, figures_dir / "weekly_sales.png")

    itemsets_df, rules_df = mine_association_rules(transactions_df, config)
    itemsets_path = write_dataframe(itemsets_df, tables_dir / "association_itemsets.csv")
    rules_path = write_dataframe(rules_df, tables_dir / "association_rules.csv")
    association_metrics = {
        "rule_count": int(len(rules_df)),
        "max_lift": float(rules_df["lift"].max()) if not rules_df.empty else 0.0,
        "avg_lift_top5": float(rules_df["lift"].head(5).mean()) if not rules_df.empty else 0.0,
    }
    log_experiment(
        config=config,
        task="association",
        metrics=association_metrics,
        key_params=config["association"],
        output_paths={
            "itemsets": str(itemsets_path),
            "rules": str(rules_path),
            "top_categories_figure": str(top_categories_fig),
        },
        split_strategy="basket grouped by Order ID",
        notes="Association rules over basket transactions using configured item level.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    cluster_comparison_df, cluster_assignment_df, cluster_profile_df = run_customer_clustering(
        customer_features, config
    )
    cluster_comparison_path = write_dataframe(cluster_comparison_df, tables_dir / "clustering_comparison.csv")
    cluster_assignment_path = write_dataframe(cluster_assignment_df, tables_dir / "cluster_assignments.csv")
    cluster_profile_path = write_dataframe(cluster_profile_df, tables_dir / "cluster_profile.csv")
    cluster_figure_path = plot_cluster_profile(cluster_profile_df, figures_dir / "cluster_profile.png")
    best_cluster = cluster_comparison_df.iloc[0]
    log_experiment(
        config=config,
        task="clustering",
        metrics={
            "silhouette": float(best_cluster["silhouette"]),
            "davies_bouldin": float(best_cluster["davies_bouldin"]),
            "best_k": int(best_cluster["k"]),
        },
        key_params={
            "features": config["clustering"]["features"],
            "algorithms": config["clustering"]["algorithms"],
            "candidate_k": config["clustering"]["candidate_k"],
            "best_algorithm": best_cluster["algorithm"],
        },
        output_paths={
            "comparison": str(cluster_comparison_path),
            "assignments": str(cluster_assignment_path),
            "profile": str(cluster_profile_path),
            "profile_figure": str(cluster_figure_path),
        },
        split_strategy="customer-level aggregation from cleaned transactional data",
        notes="Customer clustering benchmark across KMeans and Agglomerative.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    forecast_comparison_df, forecast_predictions_df, forecast_residual_df = run_forecasting_experiment(
        weekly_sales, config
    )
    forecast_comparison_path = write_dataframe(forecast_comparison_df, tables_dir / "forecast_comparison.csv")
    forecast_predictions_path = write_dataframe(forecast_predictions_df, tables_dir / "forecast_predictions.csv")
    forecast_residual_path = write_dataframe(forecast_residual_df, tables_dir / "forecast_residuals.csv")
    forecast_figure_path = plot_forecast(forecast_predictions_df, figures_dir / "forecast_vs_actual.png")
    best_forecast = forecast_comparison_df.dropna(subset=["sMAPE"]).iloc[0]
    log_experiment(
        config=config,
        task="forecasting",
        metrics={
            "MAE": float(best_forecast["MAE"]),
            "RMSE": float(best_forecast["RMSE"]),
            "sMAPE": float(best_forecast["sMAPE"]),
        },
        key_params={
            "frequency": config["forecasting"]["frequency"],
            "horizon": config["forecasting"]["horizon"],
            "moving_average_window": config["forecasting"]["moving_average_window"],
            "holt_winters": config["forecasting"]["holt_winters"],
            "sarimax": config["forecasting"]["sarimax"],
            "best_model": best_forecast["model"],
        },
        output_paths={
            "comparison": str(forecast_comparison_path),
            "predictions": str(forecast_predictions_path),
            "residuals": str(forecast_residual_path),
            "forecast_figure": str(forecast_figure_path),
            "weekly_sales_figure": str(sales_timeline_fig),
        },
        split_strategy=f"time-based split with holdout horizon={config['forecasting']['horizon']}",
        notes="Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    export_tracking_summary(config, PROJECT_ROOT)
    print("Pipeline completed successfully.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the supermarket sales data mining pipeline.")
    parser.add_argument("--config", dest="config_path", default=None, help="Optional path to params.yaml")
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate config and schema without running the full pipeline.",
    )
    args = parser.parse_args()
    run_pipeline(config_path=args.config_path, check_only=args.check_only)


if __name__ == "__main__":
    main()
