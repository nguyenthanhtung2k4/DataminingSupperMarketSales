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
from src.config import cleanup_legacy_table_files, resolve_table_path
from src.data import clean_sales_data, load_raw_data, schema_snapshot
from src.evaluation import (
    export_tracking_summary,
    log_experiment,
    write_dataframe,
)
from src.features import build_basket_transactions, build_customer_features, build_sales_time_series
from src.mining import mine_association_rules, run_customer_clustering
from src.models import run_customer_classification, run_forecasting_experiment
from src.visualization import (
    plot_cluster_profile,
    plot_confusion_matrix,
    plot_forecast,
    plot_forecast_residuals,
    plot_sales_over_time,
    plot_top_categories,
)


def _write_json(data: dict, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def run_pipeline(config_path: str | None = None, check_only: bool = False) -> None:
    config = load_params(config_path)
    ensure_output_directories(config, PROJECT_ROOT)

    raw_data_path = resolve_path(config["paths"]["raw_data"], PROJECT_ROOT)
    processed_dir = resolve_path(config["paths"]["processed_dir"], PROJECT_ROOT)
    figures_dir = resolve_path(config["paths"]["figures_dir"], PROJECT_ROOT)

    raw_df = load_raw_data(config, PROJECT_ROOT)
    schema_df = schema_snapshot(raw_df)
    write_dataframe(schema_df, resolve_table_path(config, "diagnostics", "schema_snapshot.csv", PROJECT_ROOT))

    if check_only:
        print(f"Schema check passed. Raw rows: {len(raw_df)}")
        return

    cleaned_df, cleaning_report = clean_sales_data(raw_df, config)
    write_dataframe(cleaned_df, processed_dir / "cleaned_sales.csv")
    _write_json(cleaning_report, resolve_table_path(config, "diagnostics", "cleaning_report.json", PROJECT_ROOT))

    customer_features = build_customer_features(cleaned_df)
    sales_ts = build_sales_time_series(
        cleaned_df,
        frequency=config["forecasting"]["frequency"],
        target_column=config["forecasting"]["target_column"],
    )
    transactions_df = build_basket_transactions(
        cleaned_df,
        item_level=config["preprocessing"]["basket_item_level"],
    )

    write_dataframe(customer_features, processed_dir / "customer_features.csv")
    write_dataframe(sales_ts, processed_dir / "weekly_sales.csv")
    write_dataframe(transactions_df, processed_dir / "transactions.csv")

    top_categories_fig = plot_top_categories(cleaned_df, figures_dir / "top_subcategories.png")
    sales_timeline_fig = plot_sales_over_time(sales_ts, figures_dir / "weekly_sales.png")

    itemsets_df, rules_df = mine_association_rules(transactions_df, config)
    itemsets_path = write_dataframe(
        itemsets_df, resolve_table_path(config, "diagnostics", "association_itemsets.csv", PROJECT_ROOT)
    )
    rules_path = write_dataframe(rules_df, resolve_table_path(config, "core", "association_rules.csv", PROJECT_ROOT))
    association_metrics = {
        "rule_count": int(len(rules_df)),
        "max_lift": float(rules_df["lift"].max()) if not rules_df.empty else 0.0,
        "avg_lift_top5": float(rules_df["lift"].head(5).mean()) if not rules_df.empty else 0.0,
    }
    log_experiment(
        config=config,
        task="association",
        metrics=association_metrics,
        key_params={
            **config["association"],
            "item_level": config["preprocessing"]["basket_item_level"],
        },
        output_paths={
            "itemsets": str(itemsets_path),
            "rules": str(rules_path),
            "top_categories_figure": str(top_categories_fig),
        },
        split_strategy="basket grouped by Order ID",
        notes="Luật kết hợp trên giỏ hàng theo hóa đơn.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    cluster_comparison_df, cluster_assignment_df, cluster_profile_df = run_customer_clustering(
        customer_features, config
    )
    cluster_comparison_path = write_dataframe(
        cluster_comparison_df, resolve_table_path(config, "core", "clustering_comparison.csv", PROJECT_ROOT)
    )
    cluster_assignment_path = write_dataframe(
        cluster_assignment_df, resolve_table_path(config, "diagnostics", "cluster_assignments.csv", PROJECT_ROOT)
    )
    cluster_profile_path = write_dataframe(
        cluster_profile_df, resolve_table_path(config, "core", "cluster_profile.csv", PROJECT_ROOT)
    )
    cluster_figure_path = plot_cluster_profile(cluster_profile_df, figures_dir / "cluster_profile.png")
    best_cluster = cluster_comparison_df.iloc[0]
    log_experiment(
        config=config,
        task="clustering",
        metrics={
            "silhouette": float(best_cluster["silhouette"]),
            "davies_bouldin": float(best_cluster["davies_bouldin"]),
            "best_k": int(best_cluster["k"]),
            "accepted_for_report": bool(best_cluster["accepted_for_report"]),
            "noise_share": float(best_cluster["noise_share"]),
        },
        key_params={
            "features": config["clustering"]["features"],
            "algorithms": config["clustering"]["algorithms"],
            "candidate_k": config["clustering"]["candidate_k"],
            "dbscan": config["clustering"].get("dbscan", {}),
            "best_algorithm": best_cluster["algorithm"],
        },
        output_paths={
            "comparison": str(cluster_comparison_path),
            "assignments": str(cluster_assignment_path),
            "profile": str(cluster_profile_path),
            "profile_figure": str(cluster_figure_path),
        },
        split_strategy="customer-level aggregation from transactional data",
        notes="So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    (
        classification_comparison_df,
        classification_predictions_df,
        classification_confusion_df,
        classification_class_report_df,
    ) = run_customer_classification(customer_features, config)
    classification_comparison_path = write_dataframe(
        classification_comparison_df,
        resolve_table_path(config, "core", "classification_comparison.csv", PROJECT_ROOT),
    )
    classification_predictions_path = write_dataframe(
        classification_predictions_df,
        resolve_table_path(config, "diagnostics", "classification_predictions.csv", PROJECT_ROOT),
    )
    classification_confusion_export_df = classification_confusion_df.reset_index().rename(
        columns={"index": "actual_segment"}
    )
    classification_confusion_path = write_dataframe(
        classification_confusion_export_df,
        resolve_table_path(config, "core", "classification_confusion_matrix.csv", PROJECT_ROOT),
    )
    classification_class_report_path = write_dataframe(
        classification_class_report_df,
        resolve_table_path(config, "core", "classification_class_report.csv", PROJECT_ROOT),
    )
    confusion_figure_path = plot_confusion_matrix(
        classification_confusion_df, figures_dir / "classification_confusion_matrix.png"
    )
    best_classifier = classification_comparison_df.iloc[0]
    log_experiment(
        config=config,
        task="classification",
        metrics={
            "accuracy": float(best_classifier["accuracy"]),
            "f1_macro": float(best_classifier["f1_macro"]),
            "roc_auc_ovr": float(best_classifier["roc_auc_ovr"]),
        },
        key_params=config["classification"]["model_params"][best_classifier["model"]],
        output_paths={
            "comparison": str(classification_comparison_path),
            "predictions": str(classification_predictions_path),
            "confusion": str(classification_confusion_path),
            "class_report": str(classification_class_report_path),
            "confusion_figure": str(confusion_figure_path),
        },
        split_strategy="stratified train/test split at customer level",
        notes="Phân lớp phân khúc khách hàng với target Segment.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    forecast_comparison_df, forecast_predictions_df, forecast_residual_df = run_forecasting_experiment(
        sales_ts, config
    )
    forecast_comparison_path = write_dataframe(
        forecast_comparison_df, resolve_table_path(config, "core", "forecast_comparison.csv", PROJECT_ROOT)
    )
    forecast_predictions_path = write_dataframe(
        forecast_predictions_df, resolve_table_path(config, "diagnostics", "forecast_predictions.csv", PROJECT_ROOT)
    )
    forecast_residual_path = write_dataframe(
        forecast_residual_df, resolve_table_path(config, "core", "forecast_residuals.csv", PROJECT_ROOT)
    )
    forecast_figure_path = plot_forecast(forecast_predictions_df, figures_dir / "forecast_vs_actual.png")
    forecast_residual_figure_path = plot_forecast_residuals(
        forecast_residual_df, figures_dir / "forecast_residuals.png"
    )
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
            "enabled_models": config["forecasting"]["enabled_models"],
            "best_model": best_forecast["model"],
        },
        output_paths={
            "comparison": str(forecast_comparison_path),
            "predictions": str(forecast_predictions_path),
            "residuals": str(forecast_residual_path),
            "forecast_figure": str(forecast_figure_path),
            "forecast_residual_figure": str(forecast_residual_figure_path),
            "sales_time_figure": str(sales_timeline_fig),
        },
        split_strategy=f"time-based split with holdout horizon={config['forecasting']['horizon']}",
        notes="So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.",
        project_root=PROJECT_ROOT,
        data_path=raw_data_path,
    )

    export_tracking_summary(config, PROJECT_ROOT)
    cleanup_legacy_table_files(config, PROJECT_ROOT)
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
