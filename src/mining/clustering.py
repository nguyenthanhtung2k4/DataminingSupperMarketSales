from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score
from sklearn.preprocessing import StandardScaler


def _fit_partition_model(algorithm: str, X: np.ndarray, seed: int, **kwargs: Any) -> np.ndarray:
    if algorithm == "kmeans":
        model = KMeans(n_clusters=int(kwargs["k"]), random_state=seed, n_init=20)
        return model.fit_predict(X)
    if algorithm == "agglomerative":
        model = AgglomerativeClustering(n_clusters=int(kwargs["k"]))
        return model.fit_predict(X)
    if algorithm == "dbscan":
        model = DBSCAN(eps=float(kwargs["eps"]), min_samples=int(kwargs["min_samples"]))
        return model.fit_predict(X)
    raise ValueError(f"Unsupported clustering algorithm: {algorithm}")


def _evaluate_labels(labels: np.ndarray, X_scaled: np.ndarray) -> dict[str, float] | None:
    unique_labels = set(labels.tolist())
    cluster_labels = sorted(label for label in unique_labels if label != -1)
    if len(cluster_labels) < 2:
        return None

    mask = labels != -1
    evaluation_labels = labels[mask] if -1 in unique_labels else labels
    evaluation_X = X_scaled[mask] if -1 in unique_labels else X_scaled
    if len(np.unique(evaluation_labels)) < 2:
        return None

    cluster_shares = pd.Series(evaluation_labels).value_counts(normalize=True)
    return {
        "cluster_count": float(len(cluster_labels)),
        "silhouette": float(silhouette_score(evaluation_X, evaluation_labels)),
        "davies_bouldin": float(davies_bouldin_score(evaluation_X, evaluation_labels)),
        "min_cluster_share": float(cluster_shares.min()),
        "max_cluster_share": float(cluster_shares.max()),
        "noise_share": float(np.mean(labels == -1)),
    }


def _build_profile_df(assignment_df: pd.DataFrame) -> pd.DataFrame:
    profile_map = {
        "Customer Key": ("customer_count", "count"),
        "total_sales": ("avg_sales", "mean"),
        "avg_order_value": ("avg_order_value", "mean"),
        "recency_days": ("recency_days", "mean"),
        "order_count": ("order_count", "mean"),
        "unique_categories": ("unique_categories", "mean"),
        "unique_subcategories": ("unique_subcategories", "mean"),
        "active_days": ("active_days", "mean"),
        "active_months": ("active_months", "mean"),
        "sales_per_active_month": ("sales_per_active_month", "mean"),
    }
    aggregations = {
        column: agg for column, agg in profile_map.items() if column in assignment_df.columns
    }
    renamed_columns = {
        agg[0]: agg[0] for agg in aggregations.values()
    }

    profile_df = assignment_df.groupby("cluster").agg(**{
        value[0]: (key, value[1]) for key, value in aggregations.items()
    })
    profile_df = profile_df.reset_index().round(3)
    return profile_df.sort_values("customer_count", ascending=False).reset_index(drop=True)


def run_customer_clustering(
    customer_features: pd.DataFrame,
    config: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    clustering_cfg = config["clustering"]
    feature_columns = [column for column in clustering_cfg["features"] if column in customer_features.columns]
    if len(feature_columns) < 2:
        raise ValueError("Not enough clustering features available to run clustering.")

    modeling_frame = customer_features[feature_columns].fillna(0.0)
    feature_columns = [
        column for column in feature_columns if modeling_frame[column].nunique(dropna=False) > 1
    ]
    if len(feature_columns) < 2:
        raise ValueError("Not enough non-constant clustering features available to run clustering.")

    modeling_frame = modeling_frame[feature_columns]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(modeling_frame)

    results: list[dict[str, Any]] = []
    label_cache: dict[str, np.ndarray] = {}
    seed = int(config["project"]["seed"])

    for algorithm in clustering_cfg["algorithms"]:
        if algorithm in {"kmeans", "agglomerative"}:
            for k in clustering_cfg["candidate_k"]:
                if len(customer_features) <= int(k):
                    continue
                cache_key = f"{algorithm}|k={k}"
                labels = _fit_partition_model(algorithm, X_scaled, seed, k=k)
                metrics = _evaluate_labels(labels, X_scaled)
                if not metrics:
                    continue
                label_cache[cache_key] = labels
                results.append(
                    {
                        "algorithm": algorithm,
                        "k": int(metrics["cluster_count"]),
                        "eps": np.nan,
                        "min_samples": np.nan,
                        "silhouette": metrics["silhouette"],
                        "davies_bouldin": metrics["davies_bouldin"],
                        "min_cluster_share": metrics["min_cluster_share"],
                        "max_cluster_share": metrics["max_cluster_share"],
                        "noise_share": metrics["noise_share"],
                        "accepted_for_report": bool(
                            metrics["min_cluster_share"] >= 0.05
                            and metrics["max_cluster_share"] <= 0.75
                        ),
                        "feature_count": int(len(feature_columns)),
                        "features": ", ".join(feature_columns),
                        "cache_key": cache_key,
                    }
                )
        elif algorithm == "dbscan":
            dbscan_cfg = clustering_cfg.get("dbscan", {})
            for eps in dbscan_cfg.get("eps_values", []):
                for min_samples in dbscan_cfg.get("min_samples_values", []):
                    cache_key = f"dbscan|eps={eps}|min_samples={min_samples}"
                    labels = _fit_partition_model(
                        algorithm,
                        X_scaled,
                        seed,
                        eps=eps,
                        min_samples=min_samples,
                    )
                    metrics = _evaluate_labels(labels, X_scaled)
                    if not metrics:
                        continue
                    label_cache[cache_key] = labels
                    results.append(
                        {
                            "algorithm": algorithm,
                            "k": int(metrics["cluster_count"]),
                            "eps": float(eps),
                            "min_samples": int(min_samples),
                            "silhouette": metrics["silhouette"],
                            "davies_bouldin": metrics["davies_bouldin"],
                            "min_cluster_share": metrics["min_cluster_share"],
                            "max_cluster_share": metrics["max_cluster_share"],
                            "noise_share": metrics["noise_share"],
                            "accepted_for_report": bool(
                                metrics["min_cluster_share"] >= 0.05
                                and metrics["max_cluster_share"] <= 0.75
                                and metrics["noise_share"] <= 0.35
                            ),
                            "feature_count": int(len(feature_columns)),
                            "features": ", ".join(feature_columns),
                            "cache_key": cache_key,
                        }
                    )
        else:
            raise ValueError(f"Unsupported clustering algorithm: {algorithm}")

    comparison_df = pd.DataFrame(results)
    if comparison_df.empty:
        raise ValueError("No valid clustering result was produced.")

    comparison_df = comparison_df.sort_values(
        ["accepted_for_report", "silhouette", "davies_bouldin", "max_cluster_share", "noise_share"],
        ascending=[False, False, True, True, True],
    ).reset_index(drop=True)
    best = comparison_df.iloc[0]

    assignment_df = customer_features.copy()
    assignment_df["cluster"] = label_cache[str(best["cache_key"])]
    profile_df = _build_profile_df(assignment_df)

    return comparison_df.drop(columns=["cache_key"]), assignment_df, profile_df
