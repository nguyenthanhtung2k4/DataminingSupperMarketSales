from __future__ import annotations

from typing import Any

import pandas as pd


STRING_COLUMNS = [
    "Order ID",
    "Customer ID",
    "Customer Name",
    "Category",
    "Sub-Category",
    "Product Name",
    "Region",
    "State",
    "City",
    "Segment",
]


def _clean_string_columns(df: pd.DataFrame) -> pd.DataFrame:
    for column in STRING_COLUMNS:
        if column in df.columns:
            df[column] = df[column].astype(str).str.strip()
    return df


def clean_sales_data(df: pd.DataFrame, config: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, int]]:
    working = df.copy()
    raw_rows = len(working)

    if config["preprocessing"]["drop_duplicate_rows"]:
        working = working.drop_duplicates()
    duplicate_rows_removed = raw_rows - len(working)

    working = _clean_string_columns(working)

    working["Order Date"] = pd.to_datetime(working["Order Date"], errors="coerce")
    invalid_date_rows = int(working["Order Date"].isna().sum())

    if "Ship Date" in working.columns:
        working["Ship Date"] = pd.to_datetime(working["Ship Date"], errors="coerce")

    numeric_defaults = {"Sales": 0.0, "Quantity": 1.0, "Discount": 0.0, "Profit": 0.0}
    for column in ["Sales", "Quantity", "Discount", "Profit"]:
        if column not in working.columns:
            working[column] = numeric_defaults[column]
        working[column] = pd.to_numeric(working[column], errors="coerce")

    if config["preprocessing"]["fill_numeric_missing_with_zero"]:
        working["Sales"] = working["Sales"].fillna(0.0)
        working["Discount"] = working["Discount"].fillna(0.0)
        working["Profit"] = working["Profit"].fillna(0.0)
        working["Quantity"] = working["Quantity"].fillna(1.0)

    required_columns = config["data"]["required_columns"]
    missing_core_mask = working[required_columns].isna().any(axis=1)
    missing_core_rows = int(missing_core_mask.sum())

    working = working.dropna(subset=["Order Date"])
    working = working.dropna(subset=required_columns)

    if config["preprocessing"]["clip_negative_sales"]:
        working = working[working["Sales"] >= 0]

    if "Customer ID" not in working.columns and "Customer Name" in working.columns:
        working["Customer ID"] = working["Customer Name"]
    if "Customer Name" not in working.columns and "Customer ID" in working.columns:
        working["Customer Name"] = working["Customer ID"]

    working["Customer Key"] = (
        working["Customer ID"].fillna(working["Customer Name"]).astype(str).str.strip()
    )
    working["Order Year"] = working["Order Date"].dt.year
    working["Order Month"] = working["Order Date"].dt.to_period("M").astype(str)
    working["Order Week"] = working["Order Date"].dt.to_period("W-MON").astype(str)

    report = {
        "raw_rows": raw_rows,
        "duplicate_rows_removed": duplicate_rows_removed,
        "invalid_date_rows": invalid_date_rows,
        "missing_core_rows": missing_core_rows,
        "final_rows": len(working),
    }

    return working.reset_index(drop=True), report
