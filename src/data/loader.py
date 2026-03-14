from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from src.config import resolve_path


def _normalize_name(name: str) -> str:
    return "".join(char.lower() for char in name if char.isalnum())


def _build_alias_lookup(alias_config: dict[str, list[str]]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for canonical, aliases in alias_config.items():
        for value in [canonical, *aliases]:
            lookup[_normalize_name(value)] = canonical
    return lookup


def standardize_columns(df: pd.DataFrame, alias_config: dict[str, list[str]]) -> pd.DataFrame:
    lookup = _build_alias_lookup(alias_config)
    renamed = {}
    for column in df.columns:
        key = _normalize_name(str(column))
        if key in lookup:
            renamed[column] = lookup[key]
    return df.rename(columns=renamed)


def _ensure_customer_identifier(df: pd.DataFrame) -> pd.DataFrame:
    if "Customer ID" not in df.columns and "Customer Name" in df.columns:
        df["Customer ID"] = df["Customer Name"].astype(str)
    if "Customer Name" not in df.columns and "Customer ID" in df.columns:
        df["Customer Name"] = df["Customer ID"].astype(str)
    return df


def validate_required_columns(df: pd.DataFrame, config: dict[str, Any]) -> None:
    missing = [column for column in config["data"]["required_columns"] if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    preferred = config["data"]["preferred_customer_columns"]
    if not any(column in df.columns for column in preferred):
        raise ValueError(
            "At least one customer identifier column is required. "
            f"Expected one of: {preferred}"
        )


def load_raw_data(config: dict[str, Any], project_root: str | Path | None = None) -> pd.DataFrame:
    raw_path = resolve_path(config["paths"]["raw_data"], project_root)
    if not raw_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {raw_path}. Place train.csv there or update configs/params.yaml."
        )

    df = pd.read_csv(raw_path)
    df = standardize_columns(df, config["data"]["column_aliases"])
    df = _ensure_customer_identifier(df)
    validate_required_columns(df, config)
    return df


def schema_snapshot(df: pd.DataFrame) -> pd.DataFrame:
    return (
        pd.DataFrame(
            {
                "column": df.columns,
                "dtype": [str(dtype) for dtype in df.dtypes],
                "missing_count": df.isna().sum().values,
                "missing_pct": (df.isna().mean().values * 100).round(2),
            }
        )
        .sort_values("missing_pct", ascending=False)
        .reset_index(drop=True)
    )

