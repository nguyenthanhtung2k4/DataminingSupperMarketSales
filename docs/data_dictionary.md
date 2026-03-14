# Data Dictionary

Tai lieu nay duoc viet theo schema Superstore pho bien cua dataset `rohitsahoo/sales-forecasting`. Neu file `train.csv` thuc te khac schema nay, hay cap nhat `configs/params.yaml`.

## Cot su dung truc tiep trong project

| Cot | Kieu du lieu | Vai tro |
| --- | --- | --- |
| `Order ID` | string | Khoa don hang, dung de tao basket transactions |
| `Order Date` | date | Moc thoi gian de forecast va tinh recency |
| `Sales` | float | Gia tri doanh thu, target chinh cua forecasting |
| `Category` | string | Nhom san pham cap cao |
| `Sub-Category` | string | Nhom san pham chi tiet, item mac dinh cho association rules |
| `Product Name` | string | Item chi tiet hon, co the dung khi tuning |
| `Customer ID` | string | Khoa khach hang, uu tien dung cho clustering |
| `Customer Name` | string | Du phong khi dataset khong co `Customer ID` |
| `Quantity` | int / float | Thuoc tinh bo sung cho customer profiling |
| `Discount` | float | Thuoc tinh bo sung cho customer profiling |
| `Profit` | float | Thuoc tinh bo sung de tinh profit margin |

## Cot bo sung thuong gap

| Cot | Y nghia |
| --- | --- |
| `Ship Date` | Ho tro phan tich lead time neu can mo rong |
| `Ship Mode` | Thuoc tinh van chuyen |
| `Segment` | Nhom khach hang |
| `Country`, `City`, `State`, `Region` | Thuoc tinh dia ly |
| `Product ID` | Ma san pham |
| `Postal Code` | Thong tin dia ly chi tiet |
| `Row ID` | Khoa dong du lieu, khong phai khoa business |

## Target theo tung nhanh

- `Association rules`:
  - khong co target supervised
  - dau vao la basket theo `Order ID`
  - item mac dinh la `Sub-Category`
- `Clustering`:
  - khong co target supervised
  - dau vao la feature tong hop theo khach hang
- `Forecasting`:
  - target la tong `Sales` sau khi tong hop theo tan suat `W-MON`

## Rui ro can luu y

- thieu cot customer:
  - fallback sang `Customer Name`
- thieu `Profit`, `Discount`, `Quantity`:
  - pipeline van chay, nhung mot so feature profile se it thong tin hon
- leakage:
  - tuyet doi khong shuffle khi danh gia forecasting
- duplicate rows:
  - can kiem tra truoc khi tao basket va tong hop doanh so
- version schema khac:
  - cap nhat `data.column_aliases` trong `configs/params.yaml`
