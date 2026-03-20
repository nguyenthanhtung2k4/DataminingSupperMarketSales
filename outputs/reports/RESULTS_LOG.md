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

## Ket qua 19

- run_id: `association-20260315-122129`
- run_time: `2026-03-15 12:21:29`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.193768, "avg_lift_top5": 1.134976}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 20

- run_id: `clustering-20260315-122130`
- run_time: `2026-03-15 12:21:30`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 21

- run_id: `forecasting-20260315-122131`
- run_time: `2026-03-15 12:21:31`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789571, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "weekly_sales_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 22

- run_id: `association-20260315-122202`
- run_time: `2026-03-15 12:22:02`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.193768, "avg_lift_top5": 1.134976}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 23

- run_id: `clustering-20260315-122204`
- run_time: `2026-03-15 12:22:04`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 24

- run_id: `forecasting-20260315-122204`
- run_time: `2026-03-15 12:22:04`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789571, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "weekly_sales_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 25

- run_id: `association-20260315-122233`
- run_time: `2026-03-15 12:22:33`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.193768, "avg_lift_top5": 1.134976}`
- key_params: `{"min_support": 0.02, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 26

- run_id: `clustering-20260315-122234`
- run_time: `2026-03-15 12:22:34`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3559298191397193, "davies_bouldin": 1.2056361544083543, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "avg_order_value", "unique_subcategories", "avg_discount", "profit_margin"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 27

- run_id: `forecasting-20260315-122235`
- run_time: `2026-03-15 12:22:35`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `time-based split with holdout horizon=12`
- metrics: `{"MAE": 3371.718325, "RMSE": 3861.789571, "sMAPE": 115.989002}`
- key_params: `{"frequency": "W-MON", "horizon": 12, "moving_average_window": 4, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 4}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 4]}, "best_model": "sarimax"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "weekly_sales_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 28

- run_id: `association-20260315-162149`
- run_time: `2026-03-15 16:21:49`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 20, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **tot hon**

## Ket qua 29

- run_id: `clustering-20260315-162151`
- run_time: `2026-03-15 16:21:51`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3554244951504289, "davies_bouldin": 1.067923078846253, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "unique_subcategories", "total_quantity"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 30

- run_id: `forecasting-20260315-162151`
- run_time: `2026-03-15 16:21:51`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "weekly_sales_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **tot hon**

## Ket qua 31

- run_id: `association-20260315-162304`
- run_time: `2026-03-15 16:23:04`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 20, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 20}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 32

- run_id: `clustering-20260315-162306`
- run_time: `2026-03-15 16:23:06`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3554244951504289, "davies_bouldin": 1.067923078846253, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "unique_subcategories", "total_quantity"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 33

- run_id: `forecasting-20260315-162306`
- run_time: `2026-03-15 16:23:06`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "weekly_sales_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Ket qua 34

- run_id: `association-20260315-163924`
- run_time: `2026-03-15 16:39:24`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 10, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 10}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Association rules over basket transactions using configured item level.
- conclusion: **kem hon**

## Ket qua 35

- run_id: `clustering-20260315-163925`
- run_time: `2026-03-15 16:39:25`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `customer-level aggregation from cleaned transactional data`
- metrics: `{"silhouette": 0.3554244951504289, "davies_bouldin": 1.067923078846253, "best_k": 2}`
- key_params: `{"features": ["recency_days", "order_count", "total_sales", "unique_subcategories", "total_quantity"], "algorithms": ["kmeans", "agglomerative"], "candidate_k": [2, 3, 4, 5, 6], "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: Customer clustering benchmark across KMeans and Agglomerative.
- conclusion: **kem hon**

## Ket qua 36

- run_id: `forecasting-20260315-163926`
- run_time: `2026-03-15 16:39:26`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `6808127`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "weekly_sales_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: Forecasting comparison across naive, moving average, Holt-Winters, and SARIMAX.
- conclusion: **kem hon**

## Kết quả 01

- run_id: `association-20260315-223158`
- run_time: `2026-03-15 22:31:58`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 02

- run_id: `clustering-20260315-223200`
- run_time: `2026-03-15 22:32:00`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **tốt hơn**

## Kết quả 03

- run_id: `classification-20260315-223201`
- run_time: `2026-03-15 22:32:01`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa có mốc so sánh**

## Kết quả 04

- run_id: `forecasting-20260315-223201`
- run_time: `2026-03-15 22:32:01`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 05

- run_id: `association-20260315-223237`
- run_time: `2026-03-15 22:32:37`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 06

- run_id: `clustering-20260315-223239`
- run_time: `2026-03-15 22:32:39`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 07

- run_id: `classification-20260315-223239`
- run_time: `2026-03-15 22:32:39`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 08

- run_id: `forecasting-20260315-223240`
- run_time: `2026-03-15 22:32:40`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 09

- run_id: `association-20260315-225830`
- run_time: `2026-03-15 22:58:30`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 10

- run_id: `clustering-20260315-225831`
- run_time: `2026-03-15 22:58:31`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 11

- run_id: `classification-20260315-225832`
- run_time: `2026-03-15 22:58:32`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 12

- run_id: `forecasting-20260315-225833`
- run_time: `2026-03-15 22:58:33`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 13

- run_id: `association-20260315-231707`
- run_time: `2026-03-15 23:17:07`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 14

- run_id: `clustering-20260315-231709`
- run_time: `2026-03-15 23:17:09`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 15

- run_id: `classification-20260315-231710`
- run_time: `2026-03-15 23:17:10`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 16

- run_id: `forecasting-20260315-231711`
- run_time: `2026-03-15 23:17:11`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13078.476779, "RMSE": 16385.602283, "sMAPE": 18.219553}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **tốt hơn**

## Kết quả 17

- run_id: `association-20260315-231906`
- run_time: `2026-03-15 23:19:06`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 18

- run_id: `clustering-20260315-231907`
- run_time: `2026-03-15 23:19:07`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 19

- run_id: `classification-20260315-231908`
- run_time: `2026-03-15 23:19:08`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 20

- run_id: `forecasting-20260315-231909`
- run_time: `2026-03-15 23:19:09`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13078.476779, "RMSE": 16385.602283, "sMAPE": 18.219553}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 21

- run_id: `association-20260315-232159`
- run_time: `2026-03-15 23:21:59`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 22

- run_id: `clustering-20260315-232201`
- run_time: `2026-03-15 23:22:01`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 23

- run_id: `classification-20260315-232202`
- run_time: `2026-03-15 23:22:02`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 24

- run_id: `forecasting-20260315-232202`
- run_time: `2026-03-15 23:22:02`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 25

- run_id: `association-20260315-233655`
- run_time: `2026-03-15 23:36:55`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 26

- run_id: `clustering-20260315-233657`
- run_time: `2026-03-15 23:36:57`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 27

- run_id: `classification-20260315-233658`
- run_time: `2026-03-15 23:36:58`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 28

- run_id: `forecasting-20260315-233658`
- run_time: `2026-03-15 23:36:58`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 29

- run_id: `association-20260315-235740`
- run_time: `2026-03-15 23:57:40`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 30

- run_id: `clustering-20260315-235741`
- run_time: `2026-03-15 23:57:41`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 31

- run_id: `association-20260315-235742`
- run_time: `2026-03-15 23:57:42`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 32

- run_id: `classification-20260315-235742`
- run_time: `2026-03-15 23:57:42`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 33

- run_id: `forecasting-20260315-235743`
- run_time: `2026-03-15 23:57:43`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 34

- run_id: `clustering-20260315-235743`
- run_time: `2026-03-15 23:57:43`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 35

- run_id: `classification-20260315-235744`
- run_time: `2026-03-15 23:57:44`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 36

- run_id: `forecasting-20260315-235745`
- run_time: `2026-03-15 23:57:45`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 37

- run_id: `association-20260316-102102`
- run_time: `2026-03-16 10:21:02`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 38

- run_id: `clustering-20260316-102103`
- run_time: `2026-03-16 10:21:03`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 39

- run_id: `classification-20260316-102104`
- run_time: `2026-03-16 10:21:04`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 40

- run_id: `forecasting-20260316-102104`
- run_time: `2026-03-16 10:21:04`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 41

- run_id: `association-20260316-103959`
- run_time: `2026-03-16 10:39:59`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 42

- run_id: `clustering-20260316-104001`
- run_time: `2026-03-16 10:40:01`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 43

- run_id: `classification-20260316-104002`
- run_time: `2026-03-16 10:40:02`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 44

- run_id: `forecasting-20260316-104002`
- run_time: `2026-03-16 10:40:02`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 45

- run_id: `association-20260316-104015`
- run_time: `2026-03-16 10:40:15`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 46

- run_id: `clustering-20260316-104017`
- run_time: `2026-03-16 10:40:17`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 47

- run_id: `classification-20260316-104018`
- run_time: `2026-03-16 10:40:18`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 48

- run_id: `forecasting-20260316-104018`
- run_time: `2026-03-16 10:40:18`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 49

- run_id: `association-20260316-104421`
- run_time: `2026-03-16 10:44:21`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 50

- run_id: `clustering-20260316-104423`
- run_time: `2026-03-16 10:44:23`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 51

- run_id: `classification-20260316-104423`
- run_time: `2026-03-16 10:44:23`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 52

- run_id: `forecasting-20260316-104424`
- run_time: `2026-03-16 10:44:24`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 53

- run_id: `association-20260316-104432`
- run_time: `2026-03-16 10:44:32`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 54

- run_id: `clustering-20260316-104433`
- run_time: `2026-03-16 10:44:33`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 55

- run_id: `classification-20260316-104434`
- run_time: `2026-03-16 10:44:34`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 56

- run_id: `forecasting-20260316-104435`
- run_time: `2026-03-16 10:44:35`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 57

- run_id: `association-20260316-105119`
- run_time: `2026-03-16 10:51:19`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 58

- run_id: `clustering-20260316-105120`
- run_time: `2026-03-16 10:51:20`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 59

- run_id: `classification-20260316-105121`
- run_time: `2026-03-16 10:51:21`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 60

- run_id: `forecasting-20260316-105122`
- run_time: `2026-03-16 10:51:22`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 61

- run_id: `association-20260316-105651`
- run_time: `2026-03-16 10:56:51`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 62

- run_id: `clustering-20260316-105652`
- run_time: `2026-03-16 10:56:52`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 63

- run_id: `classification-20260316-105653`
- run_time: `2026-03-16 10:56:53`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 64

- run_id: `forecasting-20260316-105654`
- run_time: `2026-03-16 10:56:54`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 65

- run_id: `association-20260316-110216`
- run_time: `2026-03-16 11:02:16`
- task: `association`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/association_itemsets.csv", "rules": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/association_rules.csv", "top_categories_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **chưa tốt hơn**

## Kết quả 66

- run_id: `clustering-20260316-110217`
- run_time: `2026-03-16 11:02:17`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/clustering_comparison.csv", "assignments": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/cluster_assignments.csv", "profile": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/cluster_profile.csv", "profile_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **chưa tốt hơn**

## Kết quả 67

- run_id: `classification-20260316-110218`
- run_time: `2026-03-16 11:02:18`
- task: `classification`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/classification_predictions.csv", "confusion": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_confusion_matrix.csv", "class_report": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/classification_class_report.csv", "confusion_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa tốt hơn**

## Kết quả 68

- run_id: `forecasting-20260316-110219`
- run_time: `2026-03-16 11:02:19`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2026-03-15 12:07:33`
- code_version: `d979766`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.564803, "RMSE": 18419.983394, "sMAPE": 18.725375}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_comparison.csv", "predictions": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/diagnostics/forecast_predictions.csv", "residuals": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/tables/core/forecast_residuals.csv", "forecast_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_vs_actual.png", "forecast_residual_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/forecast_residuals.png", "sales_time_figure": "/hdd3/nckh-AIAgent/tungtt/Datamining/DataminingSupperMarketSales/outputs/figures/weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **chưa tốt hơn**

## Kết quả 69

- run_id: `association-20260320-224153`
- run_time: `2026-03-20 22:41:53`
- task: `association`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `d4b120e`
- split_strategy: `basket grouped by Order ID`
- metrics: `{"rule_count": 12, "max_lift": 1.254701, "avg_lift_top5": 1.2276986}`
- key_params: `{"algorithm": "apriori", "min_support": 0.01, "min_confidence": 0.02, "min_lift": 1.0, "max_length": 3, "top_n_rules": 12, "item_level": "Sub-Category"}`
- output_paths: `{"itemsets": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\diagnostics\\association_itemsets.csv", "rules": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\association_rules.csv", "top_categories_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\top_subcategories.png"}`
- notes: Luật kết hợp trên giỏ hàng theo hóa đơn.
- conclusion: **tốt hơn**

## Kết quả 70

- run_id: `clustering-20260320-224203`
- run_time: `2026-03-20 22:42:03`
- task: `clustering`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `d4b120e`
- split_strategy: `customer-level aggregation from transactional data`
- metrics: `{"silhouette": 0.38952090303089726, "davies_bouldin": 1.011043135413477, "best_k": 4, "accepted_for_report": true, "noise_share": 0.0}`
- key_params: `{"features": ["recency_days", "total_sales", "avg_order_value", "active_days", "unique_categories"], "algorithms": ["kmeans", "agglomerative", "dbscan"], "candidate_k": [2, 3, 4, 5, 6], "dbscan": {"eps_values": [0.6, 0.8, 1.0, 1.2], "min_samples_values": [5, 8, 12]}, "best_algorithm": "kmeans"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\clustering_comparison.csv", "assignments": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\diagnostics\\cluster_assignments.csv", "profile": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\cluster_profile.csv", "profile_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\cluster_profile.png"}`
- notes: So sánh KMeans, Agglomerative và DBSCAN trên đặc trưng khách hàng.
- conclusion: **tốt hơn**

## Kết quả 71

- run_id: `classification-20260320-224204`
- run_time: `2026-03-20 22:42:04`
- task: `classification`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `d4b120e`
- split_strategy: `stratified train/test split at customer level`
- metrics: `{"accuracy": 0.386935, "f1_macro": 0.369547, "roc_auc_ovr": 0.548107}`
- key_params: `{"C": 10.0, "class_weight": "balanced"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\classification_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\diagnostics\\classification_predictions.csv", "confusion": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\classification_confusion_matrix.csv", "class_report": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\classification_class_report.csv", "confusion_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\classification_confusion_matrix.png"}`
- notes: Phân lớp phân khúc khách hàng với target Segment.
- conclusion: **chưa có mốc so sánh**

## Kết quả 72

- run_id: `forecasting-20260320-224205`
- run_time: `2026-03-20 22:42:05`
- task: `forecasting`
- dataset_version: `train.csv|2129689B|2020-09-11 15:40:16`
- code_version: `d4b120e`
- split_strategy: `time-based split with holdout horizon=6`
- metrics: `{"MAE": 13133.389642, "RMSE": 18419.610063, "sMAPE": 18.72501}`
- key_params: `{"frequency": "MS", "horizon": 6, "moving_average_window": 3, "holt_winters": {"trend": "add", "seasonal": "add", "seasonal_periods": 12}, "sarimax": {"order": [1, 1, 1], "seasonal_order": [1, 0, 0, 12]}, "enabled_models": ["naive", "moving_average", "holt_winters", "sarimax", "prophet"], "best_model": "holt_winters"}`
- output_paths: `{"comparison": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\forecast_comparison.csv", "predictions": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\diagnostics\\forecast_predictions.csv", "residuals": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\tables\\core\\forecast_residuals.csv", "forecast_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_vs_actual.png", "forecast_residual_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\forecast_residuals.png", "sales_time_figure": "D:\\CODE\\DNU_Data_Mining\\DataminingSupperMarketSales\\outputs\\figures\\weekly_sales.png"}`
- notes: So sánh baseline và mô hình forecast nâng cao theo đúng split thời gian.
- conclusion: **tốt hơn**
