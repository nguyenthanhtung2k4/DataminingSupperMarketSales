from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score
from sklearn.preprocessing import StandardScaler


def _fit_model(algorithm: str, n_clusters: int, X: np.ndarray, seed: int) -> np.ndarray:
    if algorithm == "kmeans":
        model = KMeans(n_clusters=n_clusters, random_state=seed, n_init=20)
        return model.fit_predict(X)
    if algorithm == "agglomerative":
        model = AgglomerativeClustering(n_clusters=n_clusters)
        return model.fit_predict(X)
    raise ValueError(f"Unsupported clustering algorithm: {algorithm}")


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
    seed = config["project"]["seed"]
    for algorithm in clustering_cfg["algorithms"]:
        for k in clustering_cfg["candidate_k"]:
            if len(customer_features) <= k:
                continue
            labels = _fit_model(algorithm, k, X_scaled, seed)
            if len(np.unique(labels)) < 2:
                continue
            cluster_shares = pd.Series(labels).value_counts(normalize=True)
            results.append(
                {
                    "algorithm": algorithm,
                    "k": int(k),
                    "silhouette": float(silhouette_score(X_scaled, labels)),
                    "davies_bouldin": float(davies_bouldin_score(X_scaled, labels)),
                    "min_cluster_share": float(cluster_shares.min()),
                    "max_cluster_share": float(cluster_shares.max()),
                    "accepted_for_report": bool(
                        cluster_shares.min() >= 0.05 and cluster_shares.max() <= 0.75
                    ),
                    "feature_count": int(len(feature_columns)),
                    "features": ", ".join(feature_columns),
                }
            )

    comparison_df = pd.DataFrame(results)
    if comparison_df.empty:
        raise ValueError("No valid clustering result was produced.")

    accepted_df = comparison_df[comparison_df["accepted_for_report"]].copy()
    ranking_source = accepted_df if not accepted_df.empty else comparison_df
    comparison_df = ranking_source.sort_values(
        ["silhouette", "davies_bouldin", "max_cluster_share"],
        ascending=[False, True, True],
    ).reset_index(drop=True)
    best = comparison_df.iloc[0]

    best_labels = _fit_model(best["algorithm"], int(best["k"]), X_scaled, seed)
    assignment_df = customer_features.copy()
    assignment_df["cluster"] = best_labels

    profile_df = (
        assignment_df.groupby("cluster")
        .agg(
            customer_count=("Customer Key", "count"),
            total_sales=("total_sales", "mean"),
            avg_order_value=("avg_order_value", "mean"),
            recency_days=("recency_days", "mean"),
            order_count=("order_count", "mean"),
            unique_subcategories=("unique_subcategories", "mean"),
            total_quantity=("total_quantity", "mean"),
            active_days=("active_days", "mean"),
            avg_discount=("avg_discount", "mean"),
            profit_margin=("profit_margin", "mean"),
        )
        .round(3)
        .reset_index()
        .sort_values("customer_count", ascending=False)
    )

    return comparison_df, assignment_df, profile_df
