# Tables

Thu muc nay chua bang ket qua duoc sinh ra tu code.

## Co can `run_papermill.py` de co bang CSV khong?

- Khong.
- `run_pipeline.py` sinh bang trong `core/` va `diagnostics/`.
- `run_experiments.py` sinh bang trong `experiments/`.
- `run_papermill.py` chi execute notebook, khong phai nguon sinh bang CSV chinh.

## `core/`

Cac bang ket qua chinh can dung de doc ket qua:

- `association_rules.csv`: tap luat ket hop cuoi cung
- `clustering_comparison.csv`: bang so sanh cac mo hinh phan cum
- `cluster_profile.csv`: ho so tung cum khach hang
- `classification_comparison.csv`: bang so sanh model classification
- `classification_confusion_matrix.csv`: ma tran nham lan cua model tot nhat
- `classification_class_report.csv`: precision, recall, f1 theo tung lop
- `forecast_comparison.csv`: bang so sanh model du bao
- `forecast_residuals.csv`: residual cua model forecast tot nhat

## `diagnostics/`

Cac bang nay phuc vu kiem tra noi bo:

- `schema_snapshot.csv`: schema raw data
- `cleaning_report.json`: thong tin cleaning
- `association_itemsets.csv`: itemset truoc khi sinh rules
- `cluster_assignments.csv`: nhan cum cua tung customer
- `classification_predictions.csv`: du doan tren tap test
- `forecast_predictions.csv`: actual va prediction tren holdout

## `experiments/`

Cac bang nay phuc vu tune tham so:

- `experiment_association_report.csv`
- `experiment_clustering_report.csv`
- `experiment_classification_report.csv`
- `experiment_forecasting_report.csv`

## Ghi chu

- Thu muc `report/` da bi loai bo khoi luong chay chinh.
- Pipeline khong con sinh bang phuc vu LaTeX nua.
