# Tuning Guide

Tai lieu nay tra loi cau hoi: "can sua cai nao de ket qua tot hon?"

## 1. Association Rules

Can tinh chinh trong `configs/params.yaml`:

- `association.min_support`
- `association.min_confidence`
- `association.min_lift`
- `preprocessing.basket_item_level`

### Khi nao can sua

- rules qua nhieu, nhieu rule vo nghia:
  - tang `min_support`
  - tang `min_confidence`
- rules qua it:
  - giam `min_support`
- rules chung chung:
  - chuyen item level tu `Category` sang `Sub-Category` hoac `Product Name`

### Dau hieu tuning tot

- top rules de giai thich hon
- lift cao hon
- it rule trung lap hoac rule nhieu noise

## 2. Clustering

Can tinh chinh:

- `clustering.candidate_k`
- `clustering.features`

### Khi nao can sua

- silhouette thap:
  - bo cac feature it y nghia
  - them feature co suc phan biet hanh vi
- profile cum kho giai thich:
  - giam so feature
  - thu `k` nho hon
- mot cum qua lon:
  - bo sung feature hanh vi
  - thu `k` lon hon

### Dau hieu tuning tot

- silhouette tang
- Davies-Bouldin giam
- profile tung cum ro rang hon ve business

### Loi pho bien

- chay theo metric dep nhung cum khong co y nghia ve business
- dua vao qua nhieu feature co scale khac nhau

## 3. Forecasting

Can tinh chinh:

- `forecasting.frequency`
- `forecasting.horizon`
- `forecasting.moving_average_window`
- `forecasting.holt_winters`
- `forecasting.sarimax`

### Khi nao can sua

- chuoi qua nhieu noise:
  - thu tong hop theo thang thay vi tuan
- moving average qua tre:
  - giam window
- Holt-Winters khong on dinh:
  - kiem tra `seasonal_periods`
- SARIMAX qua phuc tap:
  - giam order / seasonal_order

### Dau hieu tuning tot

- `MAE`, `RMSE`, `sMAPE` giam
- residual it co pattern hon
- duong forecast bam xu huong nhung khong overfit

### Loi pho bien

- leakage do split sai thoi gian
- overfit do lag / seasonality qua manh
- horizon qua dai so voi do dai chuoi

## 4. Preprocessing

Can tinh chinh:

- xu ly duplicate
- xu ly missing
- cot customer fallback
- cot numeric optional bi thieu

### Khi nao can sua

- dataset co nhieu duplicate order line
- `Discount` / `Profit` co gia tri bat thuong
- dataset thieu `Customer ID`

### Dau hieu tuning tot

- feature customer on dinh hon
- profile cum hop ly hon
- ket qua mining va forecast nhat quan hon
