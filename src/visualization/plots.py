from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


def _save_current_figure(output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    return path


def plot_sales_over_time(ts_df: pd.DataFrame, output_path: str | Path) -> Path:
    plt.figure(figsize=(12, 5))
    plt.plot(ts_df["ds"], ts_df["y"], color="#1f77b4", linewidth=2)
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    return _save_current_figure(output_path)


def plot_top_categories(df: pd.DataFrame, output_path: str | Path, top_n: int = 10) -> Path:
    summary = (
        df.groupby("Sub-Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(top_n)
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=summary,
        x="Sales",
        y="Sub-Category",
        hue="Sub-Category",
        palette="Blues_r",
        legend=False,
    )
    plt.title(f"Top {top_n} Sub-Categories by Sales")
    plt.xlabel("Sales")
    plt.ylabel("Sub-Category")
    return _save_current_figure(output_path)


def plot_cluster_profile(profile_df: pd.DataFrame, output_path: str | Path) -> Path:
    metric_columns = [column for column in profile_df.columns if column != "cluster"]
    melted = profile_df.melt(id_vars=["cluster"], value_vars=metric_columns, var_name="metric", value_name="value")
    plt.figure(figsize=(12, 6))
    sns.barplot(data=melted, x="metric", y="value", hue="cluster")
    plt.title("Cluster Profile Summary")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Metric")
    plt.ylabel("Value")
    return _save_current_figure(output_path)


def plot_confusion_matrix(confusion_df: pd.DataFrame, output_path: str | Path) -> Path:
    plt.figure(figsize=(7, 5))
    sns.heatmap(confusion_df, annot=True, fmt="d", cmap="Blues")
    plt.title("Classification Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    return _save_current_figure(output_path)


def plot_forecast(prediction_df: pd.DataFrame, output_path: str | Path) -> Path:
    plt.figure(figsize=(12, 5))
    plt.plot(prediction_df["ds"], prediction_df["y"], label="Actual", linewidth=2, color="#222222")
    for column in prediction_df.columns:
        if column in {"ds", "y"}:
            continue
        plt.plot(prediction_df["ds"], prediction_df[column], label=column, linewidth=1.5)
    plt.title("Forecast vs Actual")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    return _save_current_figure(output_path)


def plot_forecast_residuals(residual_df: pd.DataFrame, output_path: str | Path) -> Path:
    plt.figure(figsize=(12, 4))
    plt.axhline(0.0, color="#222222", linewidth=1, linestyle="--")
    plt.plot(residual_df["ds"], residual_df["residual"], color="#d62728", linewidth=2)
    plt.title("Forecast Residuals")
    plt.xlabel("Date")
    plt.ylabel("Residual")
    return _save_current_figure(output_path)
