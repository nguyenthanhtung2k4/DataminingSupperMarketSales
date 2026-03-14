# Experiment Policy

## Muc tieu

He thong log duoc giu de:

- so sanh cac phien ban mo hinh
- viet bao cao de dang
- ghi lai tham so da dung
- biet phuong phap nao tot, phuong phap nao kem

## Cac file log chinh

- `outputs/reports/RESULTS_LOG.md`
  - dang doc tay, mo ta `Ket qua 01`, `Ket qua 02`, ...
- `outputs/reports/results_registry.csv`
  - dang bang, moi dong la mot run
- `outputs/logs/run_<timestamp>.json`
  - log chi tiet cho tung run
- `outputs/logs/best_runs_summary.md`
  - tong hop run tot nhat theo task

## Moi run phai co

- `run_id`
- `run_time`
- `task`
- `dataset_version`
- `code_version` hoac `git_commit`
- `key_params`
- `split_strategy`
- `metrics`
- `output_paths`
- `notes`
- `conclusion`

## Quy uoc dat ten

- pipeline run: `pipeline-YYYYMMDD-HHMMSS`
- notebook executed: `executed_01_eda.ipynb`, ...
- log json: `run_YYYYMMDD_HHMMSS_<task>.json`

## Cach so sanh version

1. Xem `results_registry.csv` de loc task va metric.
2. Xem `RESULTS_LOG.md` de doc nhan xet bang ngon ngu.
3. Xem `best_runs_summary.md` de biet run nao dang dan dau.
4. Neu can chi tiet, mo `run_<timestamp>.json`.

## Ghi chu

- `conclusion` chi nhan mot trong 3 nhan:
  - `tot hon`
  - `kem hon`
  - `chua on`
- Neu thay doi tham so, phai ghi ro trong `notes`.
- Neu doi schema dataset, phai ghi ro `dataset_version`.
