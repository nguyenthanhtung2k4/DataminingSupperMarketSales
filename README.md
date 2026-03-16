# DataminingSupperMarketSales

Repo nay tap trung vao phan code va ket qua chay cho De tai 1: phan tich doanh so sieu thi.

Pipeline gom 4 nhanh bat buoc:

- `Association Rules`
- `Clustering`
- `Classification`
- `Forecasting`

Nhanh `Ban giam sat` khong ap dung cho de tai nay.

## Du lieu dau vao

Du lieu dang duoc doc tu:

- `data/raw/train.csv`

Schema thuc te co cac cot chinh:

- `Order ID`, `Order Date`, `Ship Date`
- `Customer ID`, `Customer Name`, `Segment`, `Region`
- `Category`, `Sub-Category`, `Product Name`
- `Sales`

Luu y: raw data hien tai khong co san `Profit`, `Discount`, `Quantity`, nen pipeline chinh khong dua vao cac cot nay.

## Script chinh

- `python scripts/run_pipeline.py`
  - chay toan bo pipeline
  - sinh `csv`, `png`, `log`
- `python scripts/run_experiments.py --task all --preset report --apply-best`
  - sweep tham so
  - co the ghi cau hinh tot nhat vao `configs/params.yaml`
- `python scripts/run_papermill.py`
  - goi `run_pipeline.py` truoc
  - sau do execute toan bo notebook
  - ghi output truc tiep vao notebook trong `notebooks/`

## Co can chay `run_papermill.py` de co ket qua khong?

- Khong.
- `run_pipeline.py` da tao ra bang va hinh ket qua chinh.
- `run_papermill.py` chi can khi ban muon notebook goc trong `notebooks/` duoc cap nhat output.

## Cach chay nhanh nhat

Kich hoat `.venv` truoc:

```bash
source .venv/bin/activate
```

Chay pipeline:

```bash
python scripts/run_pipeline.py
```

Neu muon tune tham so truoc:

```bash
python scripts/run_experiments.py --task all --preset report --apply-best
python scripts/run_pipeline.py
```

Neu muon chay het notebook:

```bash
python scripts/run_papermill.py
```

## Thu muc output

- `data/processed/`: du lieu sau khi lam sach va tao dac trung
- `outputs/tables/core/`: bang ket qua chinh
- `outputs/tables/diagnostics/`: bang kiem tra chi tiet
- `outputs/tables/experiments/`: bang sweep tham so
- `outputs/figures/`: cac hinh sinh ra tu pipeline
- `outputs/reports/`: notebook da execute va bang tong hop run
- `outputs/logs/`: log moi lan chay

## Bao cao LaTeX

Bao cao khong con duoc sinh tu dong tu code.

- Thu muc viet bao cao thu cong: `docs/Latext/`
- Thu muc nay duoc tach khoi luong chay code
- Pipeline khong tao `report.tex` nua

## Tai lieu nen doc

- `docs/run_guide.md`
- `docs/project_focus.md`
- `docs/data_dictionary.md`
- `outputs/README.md`
