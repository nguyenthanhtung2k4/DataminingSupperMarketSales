# Run Guide

## 1. Chuan bi dataset

- Tai dataset tu Kaggle.
- Dat file vao:

```text
data/raw/train.csv
```

- Neu ten file khac, sua `paths.raw_data` trong `configs/params.yaml`.

## 2. Kiem tra schema

Mo `configs/params.yaml` va xem cac muc:

- `data.required_columns`
- `data.column_aliases`
- `data.preferred_customer_columns`

Neu version dataset khac ten cot, sua lai alias truoc khi chay.

## 3. Cai package

```bash
pip install -r requirements.txt
```

## 4. Cach chay

### Chay pipeline bang code

```bash
python scripts/run_pipeline.py
```

Dung khi muon sinh nhanh:

- data processed
- bang metric
- hinh
- log ket qua

### Chay notebook bang papermill

```bash
python scripts/run_papermill.py
```

Dung khi muon:

- co notebook executed de dua vao bao cao
- tai tao toan bo ket qua theo thu tu `01 -> 05`

## 5. Thu tu notebook

1. `01_eda.ipynb`
2. `02_preprocess_feature.ipynb`
3. `03_mining.ipynb`
4. `04_modeling_forecasting.ipynb`
5. `05_evaluation_report.ipynb`

## 6. File nao can sua neu muon ket qua tot hon

- `configs/params.yaml`
  - `association`
  - `clustering`
  - `forecasting`
- `docs/tuning_guide.md`
  - xem tung nhom tham so va dau hieu tot / xau

## 7. Ket qua duoc sinh ra o dau

- `data/processed/`: du lieu da lam sach va features
- `outputs/tables/`: bang ket qua
- `outputs/figures/`: hinh ve
- `outputs/reports/`: log dang doc tay va notebook executed
- `outputs/logs/`: json logs va tong hop best run
