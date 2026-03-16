# Data Dictionary

Tài liệu này mô tả schema thực tế của `data/raw/train.csv` đang được repo sử dụng.

## Cột chính đang có trong raw data

| Cột | Vai trò |
| --- | --- |
| `Order ID` | Khóa hóa đơn để nhóm giỏ hàng |
| `Order Date` | Mốc thời gian giao dịch |
| `Ship Date` | Thời gian giao hàng |
| `Customer ID` | Khóa khách hàng |
| `Customer Name` | Tên khách hàng |
| `Segment` | Nhãn phân khúc khách hàng, target của classification |
| `Region` | Khu vực, dùng như feature phân loại bổ sung |
| `Category` | Nhóm sản phẩm cấp cao |
| `Sub-Category` | Nhóm sản phẩm con, item mặc định cho association |
| `Product Name` | Tên sản phẩm |
| `Sales` | Doanh thu |

## Đặc trưng được sinh thêm trong pipeline

### Customer-level features

- `recency_days`
- `order_count`
- `total_sales`
- `avg_order_value`
- `unique_categories`
- `unique_subcategories`
- `active_days`
- `active_months`
- `sales_per_active_month`
- `dominant_region`

### Time-series features

- `ds`
- `y`
- `year`
- `month`
- `quarter`
- `lag_1`
- `lag_2`
- `lag_4`
- `rolling_mean_4`

## Các cột không có trong dataset hiện tại

- `Profit`
- `Discount`
- `Quantity`

Các cột này chỉ được giữ ở mức optional trong config để tương thích schema, nhưng pipeline chính thức của đề tài không dựa vào chúng nếu raw data không có thật.
