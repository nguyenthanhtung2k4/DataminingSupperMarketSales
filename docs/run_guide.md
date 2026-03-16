# Run Guide

Huong dan nay chi tap trung vao phan chay code va sinh ket qua.

## 1. Kich hoat moi truong

```bash
source .venv/bin/activate
```

## 2. Kiem tra du lieu dau vao

Dam bao file raw ton tai:

```text
data/raw/train.csv
```

## 3. Kiem tra nhanh schema

```bash
python scripts/run_pipeline.py --check-only
```

## 4. Chay full pipeline

```bash
python scripts/run_pipeline.py
```

Sau lenh nay, repo se co:

- `data/processed/*.csv`
- `outputs/tables/core/*`
- `outputs/tables/diagnostics/*`
- `outputs/figures/*.png`
- `outputs/logs/*`
- `outputs/reports/RESULTS_LOG.md`
- `outputs/reports/results_registry.csv`

## 5. Neu muon tune tham so truoc

```bash
python scripts/run_experiments.py --task all --preset report --apply-best
python scripts/run_pipeline.py
```

## 6. Neu muon execute tat ca notebook

```bash
python scripts/run_papermill.py
```

Lenh nay se:

- goi `run_pipeline.py` truoc
- execute 5 notebook
- ghi output truc tiep vao 5 file trong `notebooks/`

## 7. Artifact can kiem tra sau khi chay

- `outputs/tables/core/association_rules.csv`
- `outputs/tables/core/clustering_comparison.csv`
- `outputs/tables/core/classification_comparison.csv`
- `outputs/tables/core/forecast_comparison.csv`
- `outputs/figures/classification_confusion_matrix.png`
- `outputs/figures/forecast_vs_actual.png`
- `outputs/figures/forecast_residuals.png`

## 8. Ghi chu ve bao cao

- Code khong con sinh LaTeX report tu dong.
- Neu viet bao cao, hay viet thu cong trong `docs/Latext/`.
