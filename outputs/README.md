# Outputs

Thu muc nay chua toan bo artifact sinh ra tu code.

## Script nao tao ra file nao?

- `python scripts/run_pipeline.py`
  - tao du lieu trong `data/processed/`
  - tao bang trong `outputs/tables/core/`
  - tao bang debug trong `outputs/tables/diagnostics/`
  - tao hinh trong `outputs/figures/`
  - cap nhat `outputs/logs/` va `outputs/reports/`
- `python scripts/run_experiments.py --task all --preset report --apply-best`
  - tao bang trong `outputs/tables/experiments/`
  - co the cap nhat `configs/params.yaml`
- `python scripts/run_papermill.py`
  - goi `run_pipeline.py` truoc
  - sau do execute notebook
  - ghi output truc tiep vao notebook trong `notebooks/`

## Co can `run_papermill.py` de co csv va png khong?

- Khong.
- `run_pipeline.py` da sinh ra csv va png chinh.
- `run_papermill.py` chi can khi ban muon notebook goc co san output.

## Cac nhom output

- `figures/`: cac hinh phuc vu phan tich va notebook
- `tables/core/`: bang ket qua chinh
- `tables/diagnostics/`: bang kiem tra va prediction chi tiet
- `tables/experiments/`: bang sweep tham so
- `reports/`: notebook da execute va bang tong hop run
- `logs/`: json log tung lan chay va best-run summary

## Ghi chu

- Repo khong con sinh bao cao LaTeX tu dong.
- Neu viet bao cao, hay viet thu cong trong `docs/Latext/`.
