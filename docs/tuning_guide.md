# Tuning Guide

## Association Rules

Các tham số nên thử:

- `association.min_support`
- `association.min_confidence`
- `association.min_lift`
- `association.max_length`
- `preprocessing.basket_item_level`

Dấu hiệu tuning tốt:

- số luật đủ để đọc trong báo cáo
- lift cao hơn
- luật dễ diễn giải hơn

## Clustering

Các tham số nên thử:

- `clustering.features`
- `clustering.candidate_k`
- `clustering.dbscan.eps_values`
- `clustering.dbscan.min_samples_values`

Dấu hiệu tuning tốt:

- silhouette cao hơn
- Davies-Bouldin thấp hơn
- cụm không quá lệch về kích thước
- profile cụm có ý nghĩa business

## Classification

Các tham số nên thử:

- `classification.model_grid.logistic_regression`
- `classification.model_grid.decision_tree`
- `classification.model_grid.random_forest`

Dấu hiệu tuning tốt:

- `F1 Macro` tăng
- `ROC-AUC OvR` tăng
- confusion matrix bớt lệch

## Forecasting

Các tham số nên thử:

- `forecasting.frequency`
- `forecasting.horizon`
- `forecasting.moving_average_window`
- `forecasting.holt_winters.seasonal_periods`
- `forecasting.sarimax.order`
- `forecasting.sarimax.seasonal_order`

Dấu hiệu tuning tốt:

- `sMAPE` giảm
- `RMSE` giảm
- residual dao động quanh 0
- đường forecast bám đúng turning point

## Lỗi phổ biến cần tránh

- split sai thời gian trong forecasting
- dùng cột không có thật trong raw data
- để `support` quá thấp làm association rules quá nhiễu
- chọn clustering chỉ theo metric mà bỏ qua khả năng diễn giải
