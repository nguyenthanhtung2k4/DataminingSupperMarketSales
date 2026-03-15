# RESULTS LOG

File nay ghi theo dang doc tay de phuc vu viet bao cao.

## Ket qua 01

- run_id: `association-20260314-194445`
- run_time: `2026-03-14 19:44:45`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `a728db5`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 2, "max_lift": 1.193768, "avg_lift_top5": 1.1208985}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.2, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **chua on**

## Ket qua 02

- run_id: `clustering-20260314-194449`
- run_time: `2026-03-14 19:44:49`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `a728db5`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **chua on**

## Ket qua 03

- run_id: `forecasting-20260314-194451`
- run_time: `2026-03-14 19:44:51`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `a728db5`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789572, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "weekly_sales_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **chua on**

## Ket qua 04

- run_id: `association-20260314-194821`
- run_time: `2026-03-14 19:48:21`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `a728db5`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 2, "max_lift": 1.193768, "avg_lift_top5": 1.1208985}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.2, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 05

- run_id: `clustering-20260314-194823`
- run_time: `2026-03-14 19:48:23`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `a728db5`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 06

- run_id: `forecasting-20260314-194824`
- run_time: `2026-03-14 19:48:24`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `a728db5`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789572, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "weekly_sales_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 07

- run_id: `association-20260315-002011`
- run_time: `2026-03-15 00:20:11`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 2, "max_lift": 1.193768, "avg_lift_top5": 1.1208985}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.2, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 08

- run_id: `clustering-20260315-002013`
- run_time: `2026-03-15 00:20:13`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 09

- run_id: `forecasting-20260315-002014`
- run_time: `2026-03-15 00:20:14`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789572, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "weekly_sales_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 10

- run_id: `association-20260315-005513`
- run_time: `2026-03-15 00:55:13`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 2, "max_lift": 1.193768, "avg_lift_top5": 1.1208985}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.2, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 11

- run_id: `clustering-20260315-005523`
- run_time: `2026-03-15 00:55:23`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 12

- run_id: `forecasting-20260315-005524`
- run_time: `2026-03-15 00:55:24`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789571, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "weekly_sales_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 13

- run_id: `association-20260315-005606`
- run_time: `2026-03-15 00:56:06`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 2, "max_lift": 1.193768, "avg_lift_top5": 1.1208985}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.2, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 14

- run_id: `clustering-20260315-005615`
- run_time: `2026-03-15 00:56:15`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 15

- run_id: `forecasting-20260315-005616`
- run_time: `2026-03-15 00:56:16`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `6ceb2be`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789571, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "weekly_sales_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 16

- run_id: `association-20260315-120027`
- run_time: `2026-03-15 12:00:27`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `7bbf7b8`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.193768, "avg_lift_top5": 1.134976}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 17

- run_id: `clustering-20260315-120036`
- run_time: `2026-03-15 12:00:36`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `7bbf7b8`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 18

- run_id: `forecasting-20260315-120037`
- run_time: `2026-03-15 12:00:37`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `7bbf7b8`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789571, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "weekly_sales_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**
