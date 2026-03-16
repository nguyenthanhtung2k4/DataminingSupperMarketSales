from __future__ import annotations

import numpy as np
import pandas as pd


def _mode_or_first(series: pd.Series) -> str:
    clean = series.dropna().astype(str).str.strip()
    if clean.empty:
        return ""
    mode = clean.mode()
    return mode.iloc[0] if not mode.empty else clean.iloc[0]


def build_basket_transactions(df: pd.DataFrame, item_level: str = "Sub-Category") -> pd.DataFrame:
    if item_level not in df.columns:
        raise KeyError(f"Basket item level '{item_level}' was not found in the dataset.")

    transactions = (
        df.groupby("Order ID")[item_level]
        .apply(lambda series: sorted(set(series.dropna().astype(str).str.strip())))
        .reset_index(name="items")
    )
    transactions["item_count"] = transactions["items"].apply(len)
    transactions["item_level"] = item_level
    return transactions[transactions["item_count"] > 0].reset_index(drop=True)


def build_customer_features(df: pd.DataFrame) -> pd.DataFrame:
    reference_date = df["Order Date"].max() + pd.Timedelta(days=1)

    order_value = (
        df.groupby(["Customer Key", "Order ID"], as_index=False)["Sales"]
        .sum()
        .groupby("Customer Key")["Sales"]
        .mean()
        .rename("avg_order_value")
    )

    monthly_activity = (
        df.groupby(["Customer Key", "Order Month"])
        .size()
        .groupby("Customer Key")
        .size()
        .rename("active_months")
    )

    features = (
        df.groupby("Customer Key")
        .agg(
            customer_name=("Customer Name", _mode_or_first),
            segment=("Segment", _mode_or_first),
            dominant_region=("Region", _mode_or_first),
            order_count=("Order ID", "nunique"),
            total_sales=("Sales", "sum"),
            unique_categories=("Category", "nunique"),
            unique_subcategories=("Sub-Category", "nunique"),
            last_order_date=("Order Date", "max"),
            first_order_date=("Order Date", "min"),
        )
        .reset_index()
    )
    features = features.merge(order_value, on="Customer Key", how="left")
    features = features.merge(monthly_activity, on="Customer Key", how="left")

    features["recency_days"] = (reference_date - features["last_order_date"]).dt.days
    features["active_days"] = (
        features["last_order_date"] - features["first_order_date"]
    ).dt.days.clip(lower=0)
    features["sales_per_active_month"] = np.where(
        features["active_months"].fillna(0) > 0,
        features["total_sales"] / features["active_months"].clip(lower=1),
        features["total_sales"],
    )
    features["avg_order_value"] = features["avg_order_value"].fillna(features["total_sales"])
    features["active_months"] = features["active_months"].fillna(1).astype(int)

    return features.sort_values("total_sales", ascending=False).reset_index(drop=True)


def build_sales_time_series(
    df: pd.DataFrame,
    frequency: str = "W-MON",
    target_column: str = "Sales",
) -> pd.DataFrame:
    aggregated = df.set_index("Order Date").sort_index()[target_column].resample(frequency).sum()
    aggregated = aggregated.rename("y").reset_index().rename(columns={"Order Date": "ds"})
    if aggregated.empty:
        return aggregated

    full_range = pd.date_range(aggregated["ds"].min(), aggregated["ds"].max(), freq=frequency)
    aggregated = (
        aggregated.set_index("ds")
        .reindex(full_range)
        .rename_axis("ds")
        .fillna({"y": 0.0})
        .reset_index()
    )
    return add_time_features(aggregated)


def build_weekly_sales(
    df: pd.DataFrame,
    frequency: str = "W-MON",
    target_column: str = "Sales",
) -> pd.DataFrame:
    return build_sales_time_series(df, frequency=frequency, target_column=target_column)


def add_time_features(ts_df: pd.DataFrame) -> pd.DataFrame:
    working = ts_df.copy()
    working["year"] = working["ds"].dt.year
    working["month"] = working["ds"].dt.month
    working["quarter"] = working["ds"].dt.quarter
    working["lag_1"] = working["y"].shift(1)
    working["lag_2"] = working["y"].shift(2)
    working["lag_4"] = working["y"].shift(4)
    working["rolling_mean_4"] = working["y"].shift(1).rolling(4).mean()
    return working
