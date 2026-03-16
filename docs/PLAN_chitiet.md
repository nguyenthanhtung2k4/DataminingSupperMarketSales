# Kế hoạch chi tiết cho Đề tài 1: Phân tích doanh số siêu thị

## 1. Mục tiêu chính thức của đề tài

Pipeline phải bám đúng form:

`Data Source -> Preprocessing -> Feature Engineering -> Modeling -> Evaluation`

Với Đề tài 1, repo phải có đủ 4 nhánh bắt buộc:

1. `Association Rules`
2. `Clustering`
3. `Classification`
4. `Forecasting`

`Bán giám sát` không nằm trong phạm vi của đề tài này.

## 2. Phạm vi triển khai hiện tại trong repo

### 2.1 Luật kết hợp

- Nhóm giỏ hàng theo `Order ID`
- Dùng `Sub-Category` làm mức item chính
- Có fallback sang `Category` nếu luật quá yếu
- Đánh giá bằng `support`, `confidence`, `lift`
- Xuất top rules để phân tích `combo/cross-sell`

### 2.2 Phân cụm

- Tạo đặc trưng khách hàng ở mức `Customer Key`
- Dùng các đặc trưng có thật trong raw data:
  - `recency_days`
  - `order_count`
  - `total_sales`
  - `avg_order_value`
  - `unique_categories`
  - `unique_subcategories`
  - `active_days`
- So sánh:
  - `KMeans`
  - `Agglomerative`
  - `DBSCAN`
- Đánh giá bằng:
  - `Silhouette`
  - `Davies-Bouldin`
  - kích thước cụm
  - khả năng diễn giải business

### 2.3 Phân lớp

- Target là `Segment`
- Mỗi khách hàng tạo ra một dòng dữ liệu huấn luyện
- So sánh:
  - `Logistic Regression`
  - `Decision Tree`
  - `Random Forest`
- Đánh giá bằng:
  - `Accuracy`
  - `F1 Macro`
  - `ROC-AUC OvR`
  - `Confusion Matrix`

### 2.4 Dự báo chuỗi thời gian

- Tổng hợp doanh số theo thời gian
- Split theo thời gian, không shuffle
- Baseline:
  - `Naive`
  - `Moving Average`
- Mô hình nâng cao:
  - `Holt-Winters`
  - `SARIMAX`
  - `Prophet` nếu môi trường hỗ trợ
- Metric:
  - `MAE`
  - `RMSE`
  - `sMAPE`

## 3. Ràng buộc theo dữ liệu thật

Raw dataset hiện tại có:

- `Sales`
- `Segment`
- `Region`
- `Category`
- `Sub-Category`
- `Product Name`

Raw dataset hiện tại không có sẵn:

- `Profit`
- `Discount`
- `Quantity`

Vì vậy:

- Không hứa phân tích lợi nhuận nếu raw data không có `Profit`
- Không dùng các cột giả hoặc cột hằng làm feature chính thức
- Báo cáo phải ghi rõ giới hạn dữ liệu này

## 4. Cấu trúc mã nguồn cần giữ

- `src/data`: đọc dữ liệu, validate schema, làm sạch
- `src/features`: basket features, customer features, time-series features
- `src/mining`: association rules, clustering
- `src/models`: supervised classification, forecasting
- `src/evaluation`: metric va tracking ket qua
- `src/visualization`: figure cho báo cáo
- `scripts/run_pipeline.py`: chạy full pipeline
- `scripts/run_experiments.py`: tune tham số
- `scripts/run_papermill.py`: chay toan bo notebook va ghi output truc tiep vao notebook goc

## 5. Kế hoạch chạy thực nghiệm

### 5.1 Association

- Sweep:
  - `min_support`
  - `min_confidence`
  - `min_lift`
  - `max_length`
- Chọn cấu hình theo:
  - `avg_lift_top5`
  - số luật đủ đọc trong báo cáo
  - độ ổn định của support/confidence

### 5.2 Clustering

- Thử nhiều feature set chỉ gồm các cột có thật
- Chạy `KMeans`, `Agglomerative`, `DBSCAN`
- Chọn cấu hình theo:
  - `Silhouette`
  - `Davies-Bouldin`
  - tỷ lệ cụm quá nhỏ / quá lớn
  - business profile rõ ràng

### 5.3 Classification

- Tune tham số riêng cho:
  - `Logistic Regression`
  - `Decision Tree`
  - `Random Forest`
- Chọn best config theo:
  - `F1 Macro`
  - `ROC-AUC OvR`
  - `Accuracy`

### 5.4 Forecasting

- Test các tổ hợp:
  - moving average window
  - seasonal period cho Holt-Winters
  - order/seasonal order cho SARIMAX
- Nếu weekly chưa ổn thì so sánh thêm monthly
- Prophet là nhánh tùy chọn theo môi trường cài đặt

## 6. Artifact đầu ra bắt buộc

- `outputs/tables/core/association_rules.csv`
- `outputs/tables/core/clustering_comparison.csv`
- `outputs/tables/core/cluster_profile.csv`
- `outputs/tables/core/classification_comparison.csv`
- `outputs/tables/core/classification_confusion_matrix.csv`
- `outputs/tables/core/classification_class_report.csv`
- `outputs/tables/core/forecast_comparison.csv`
- `outputs/tables/core/forecast_residuals.csv`
- `classification_confusion_matrix.png`
- `forecast_vs_actual.png`
- `forecast_residuals.png`
- 5 notebook trong `notebooks/` neu chay `run_papermill.py`

## 7. Tiêu chí nghiệm thu

- Parse ngày đúng, không còn mất dữ liệu do sai định dạng ngày
- Pipeline chạy đủ 4 nhánh
- Có bảng so sánh cho association, clustering, classification, forecasting
- Có figure cho cluster profile, confusion matrix, forecast và residual
- `README.md`, `PLAN_chitiet.md`, `run_guide.md` thong nhat cung mot scope
- Phan code khong tu sinh LaTeX report
