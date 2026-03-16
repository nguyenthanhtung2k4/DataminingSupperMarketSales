from __future__ import annotations

from itertools import product
from typing import Any

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, label_binarize
from sklearn.tree import DecisionTreeClassifier


def _parameter_grid(grid_config: dict[str, list[Any]]) -> list[dict[str, Any]]:
    if not grid_config:
        return [{}]
    keys = list(grid_config.keys())
    combinations = product(*(grid_config[key] for key in keys))
    return [dict(zip(keys, values)) for values in combinations]


def prepare_classification_data(
    customer_features: pd.DataFrame,
    config: dict[str, Any],
) -> dict[str, Any]:
    classification_cfg = config["classification"]
    target_column = classification_cfg["target_column"]
    if target_column not in customer_features.columns:
        raise KeyError(f"Classification target column '{target_column}' is missing from customer features.")

    feature_columns = [column for column in classification_cfg["features"] if column in customer_features.columns]
    categorical_features = [
        column for column in classification_cfg.get("categorical_features", []) if column in feature_columns
    ]
    numeric_features = [column for column in feature_columns if column not in categorical_features]

    prepared = customer_features[["Customer Key", target_column, *feature_columns]].copy()
    prepared = prepared.dropna(subset=[target_column]).reset_index(drop=True)
    if prepared[target_column].nunique() < 2:
        raise ValueError("Classification target must contain at least two classes.")

    X = prepared[feature_columns].copy()
    y = prepared[target_column].astype(str)
    customer_keys = prepared["Customer Key"].astype(str)

    split = train_test_split(
        X,
        y,
        customer_keys,
        test_size=float(classification_cfg["test_size"]),
        random_state=int(config["project"]["seed"]),
        stratify=y,
    )
    X_train, X_test, y_train, y_test, key_train, key_test = split

    return {
        "X_train": X_train.reset_index(drop=True),
        "X_test": X_test.reset_index(drop=True),
        "y_train": y_train.reset_index(drop=True),
        "y_test": y_test.reset_index(drop=True),
        "key_train": key_train.reset_index(drop=True),
        "key_test": key_test.reset_index(drop=True),
        "numeric_features": numeric_features,
        "categorical_features": categorical_features,
        "labels": sorted(y.unique().tolist()),
    }


def _build_model(model_name: str, params: dict[str, Any], seed: int) -> Any:
    if model_name == "logistic_regression":
        return LogisticRegression(
            max_iter=2000,
            solver="lbfgs",
            C=float(params.get("C", 1.0)),
            class_weight=params.get("class_weight"),
        )
    if model_name == "decision_tree":
        return DecisionTreeClassifier(
            random_state=seed,
            max_depth=params.get("max_depth"),
            min_samples_leaf=int(params.get("min_samples_leaf", 1)),
            class_weight=params.get("class_weight"),
        )
    if model_name == "random_forest":
        return RandomForestClassifier(
            random_state=seed,
            n_estimators=int(params.get("n_estimators", 200)),
            max_depth=params.get("max_depth"),
            min_samples_leaf=int(params.get("min_samples_leaf", 1)),
            class_weight=params.get("class_weight"),
        )
    raise ValueError(f"Unsupported classification model: {model_name}")


def _build_pipeline(
    model_name: str,
    params: dict[str, Any],
    numeric_features: list[str],
    categorical_features: list[str],
    seed: int,
) -> Pipeline:
    transformers: list[tuple[str, Any, list[str]]] = []
    if numeric_features:
        transformers.append(("num", StandardScaler(), numeric_features))
    if categorical_features:
        transformers.append(
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            )
        )
    preprocessor = ColumnTransformer(transformers=transformers, remainder="drop")
    model = _build_model(model_name, params, seed)
    return Pipeline([("preprocessor", preprocessor), ("model", model)])


def evaluate_classification_candidate(
    prepared_data: dict[str, Any],
    model_name: str,
    params: dict[str, Any],
    seed: int,
) -> dict[str, Any]:
    pipeline = _build_pipeline(
        model_name=model_name,
        params=params,
        numeric_features=prepared_data["numeric_features"],
        categorical_features=prepared_data["categorical_features"],
        seed=seed,
    )
    pipeline.fit(prepared_data["X_train"], prepared_data["y_train"])

    predictions = pd.Series(pipeline.predict(prepared_data["X_test"]), name="predicted_segment")
    actual = prepared_data["y_test"]
    accuracy = accuracy_score(actual, predictions)
    f1_macro = f1_score(actual, predictions, average="macro")
    f1_weighted = f1_score(actual, predictions, average="weighted")

    roc_auc_ovr = np.nan
    if hasattr(pipeline, "predict_proba"):
        probabilities = pipeline.predict_proba(prepared_data["X_test"])
        classes = list(pipeline.named_steps["model"].classes_)
        actual_binarized = label_binarize(actual, classes=classes)
        if actual_binarized.shape[1] == len(classes):
            roc_auc_ovr = roc_auc_score(
                actual_binarized,
                probabilities,
                average="macro",
                multi_class="ovr",
            )

    confusion = confusion_matrix(actual, predictions, labels=prepared_data["labels"])
    confusion_df = pd.DataFrame(
        confusion,
        index=prepared_data["labels"],
        columns=prepared_data["labels"],
    )

    class_report = classification_report(
        actual,
        predictions,
        labels=prepared_data["labels"],
        output_dict=True,
        zero_division=0,
    )
    class_report_df = (
        pd.DataFrame(class_report)
        .transpose()
        .reset_index()
        .rename(columns={"index": "label"})
    )

    prediction_df = pd.DataFrame(
        {
            "Customer Key": prepared_data["key_test"],
            "actual_segment": actual,
            "predicted_segment": predictions,
        }
    )
    prediction_df["correct"] = prediction_df["actual_segment"] == prediction_df["predicted_segment"]

    return {
        "model": model_name,
        "params": params,
        "accuracy": float(accuracy),
        "f1_macro": float(f1_macro),
        "f1_weighted": float(f1_weighted),
        "roc_auc_ovr": float(roc_auc_ovr) if not np.isnan(roc_auc_ovr) else np.nan,
        "prediction_df": prediction_df,
        "confusion_df": confusion_df,
        "class_report_df": class_report_df,
    }


def run_customer_classification(
    customer_features: pd.DataFrame,
    config: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    classification_cfg = config["classification"]
    prepared_data = prepare_classification_data(customer_features, config)
    seed = int(config["project"]["seed"])

    results: list[dict[str, Any]] = []
    artifacts: dict[str, dict[str, Any]] = {}
    for model_name, params in classification_cfg["model_params"].items():
        candidate = evaluate_classification_candidate(prepared_data, model_name, params, seed)
        artifacts[model_name] = candidate
        results.append(
            {
                "model": model_name,
                "accuracy": round(candidate["accuracy"], 6),
                "f1_macro": round(candidate["f1_macro"], 6),
                "f1_weighted": round(candidate["f1_weighted"], 6),
                "roc_auc_ovr": round(candidate["roc_auc_ovr"], 6)
                if not np.isnan(candidate["roc_auc_ovr"])
                else np.nan,
                "params": str(params),
            }
        )

    comparison_df = pd.DataFrame(results).sort_values(
        ["f1_macro", "roc_auc_ovr", "accuracy"],
        ascending=[False, False, False],
        na_position="last",
    ).reset_index(drop=True)
    best_model = comparison_df.iloc[0]["model"]
    best_artifact = artifacts[str(best_model)]
    return (
        comparison_df,
        best_artifact["prediction_df"],
        best_artifact["confusion_df"],
        best_artifact["class_report_df"],
    )


def tune_classification_models(
    customer_features: pd.DataFrame,
    config: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], pd.DataFrame]:
    prepared_data = prepare_classification_data(customer_features, config)
    seed = int(config["project"]["seed"])
    classification_cfg = config["classification"]

    summary_rows: list[dict[str, Any]] = []
    best_params_by_model: dict[str, dict[str, Any]] = {}

    for model_name, grid in classification_cfg["model_grid"].items():
        best_row: dict[str, Any] | None = None
        for params in _parameter_grid(grid):
            candidate = evaluate_classification_candidate(prepared_data, model_name, params, seed)
            row = {
                "model": model_name,
                "accuracy": round(candidate["accuracy"], 6),
                "f1_macro": round(candidate["f1_macro"], 6),
                "f1_weighted": round(candidate["f1_weighted"], 6),
                "roc_auc_ovr": round(candidate["roc_auc_ovr"], 6)
                if not np.isnan(candidate["roc_auc_ovr"])
                else np.nan,
                "params": str(params),
                "_raw_params": params,
            }
            summary_rows.append(row)
            if best_row is None:
                best_row = row
                continue
            current_rank = (
                row["f1_macro"],
                row["roc_auc_ovr"] if not np.isnan(row["roc_auc_ovr"]) else float("-inf"),
                row["accuracy"],
            )
            best_rank = (
                best_row["f1_macro"],
                best_row["roc_auc_ovr"] if not np.isnan(best_row["roc_auc_ovr"]) else float("-inf"),
                best_row["accuracy"],
            )
            if current_rank > best_rank:
                best_row = row
        if best_row is not None:
            best_params_by_model[model_name] = best_row["_raw_params"]

    summary_df = pd.DataFrame(summary_rows).drop(columns=["_raw_params"]).sort_values(
        ["f1_macro", "roc_auc_ovr", "accuracy"],
        ascending=[False, False, False],
        na_position="last",
    ).reset_index(drop=True)
    return best_params_by_model, summary_df
