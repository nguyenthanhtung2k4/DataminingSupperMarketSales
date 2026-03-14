# DataminingSupperMarketSales

Phan tich doanh so sieu thi theo huong Data Mining voi 3 nhanh chinh:

- khai pha gio hang de tim co-hoi cross-sell / up-sell
- phan cum khach hang de xay dung chan dung mua sam
- du bao doanh so theo thoi gian de so sanh cac mo hinh forecast

Dataset du kien: `train.csv` tu Kaggle `rohitsahoo/sales-forecasting`.

## Final Output

Repo sau khi chay xong se sinh ra:

- du lieu da xu ly trong `data/processed/`
- bang top association rules, bang so sanh clustering, bang so sanh forecasting
- hinh ve, bang metric va artifact trong `outputs/`
- file log ket qua de so sanh cac lan chay:
  - `outputs/reports/RESULTS_LOG.md`
  - `outputs/reports/results_registry.csv`
  - `outputs/logs/run_<timestamp>.json`
  - `outputs/logs/best_runs_summary.md`
- bo notebook `01 -> 05` de trinh bay pipeline va viet bao cao

## Cau Truc Chinh

- `configs/params.yaml`: tham so va duong dan can chinh truoc khi chay
- `docs/`: huong dan chi tiet, data dictionary, tuning guide, experiment policy
- `notebooks/`: notebook bao cao theo dung thu tu pipeline
- `src/`: code chinh cua du an
- `scripts/`: script chay pipeline, notebook va xuat ket qua
- `outputs/`: artifacts, log, bang metric, bao cao

## Cach Chay Nhanh

1. Tai dataset va dat file vao `data/raw/train.csv`.
2. Mo `configs/params.yaml` va kiem tra lai ten cot neu version dataset khac.
3. Tao virtual environment de tranh xung dot moi truong:

```bash
python -m venv .venv
```

Neu may cua ban dung `python3` thay vi `python`, hay dung:

```bash
python3 -m venv .venv
```

4. Kich hoat virtual environment tuy theo he dieu hanh:

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS / WSL / Git Bash:

```bash
source .venv/bin/activate
```

Sau khi kich hoat thanh cong, ban se thay `(.venv)` o dau dong lenh.

5. Cai thu vien:

```bash
python -m pip install -r requirements.txt
```

Neu dang dung `python3`, co the dung:

```bash
python3 -m pip install -r requirements.txt
```

6. Chay pipeline bang code:

```bash
python scripts/run_pipeline.py
```

Hoac neu may ban dung `python3`:

```bash
python3 scripts/run_pipeline.py
```

7. Hoac chay lai toan bo notebook:

```bash
python scripts/run_papermill.py
```

Hoac:

```bash
python3 scripts/run_papermill.py
```

8. Khi muon thoat khoi virtual environment:

```bash
deactivate
```

## Truoc Khi Chay Can Sua Gi

- `configs/params.yaml`
  - `paths.raw_data`
  - `data.required_columns`
  - `data.column_aliases`
  - `association`
  - `clustering`
  - `forecasting`

Tai lieu chi tiet:

- [project_focus.md](docs/project_focus.md)
- [data_dictionary.md](docs/data_dictionary.md)
- [run_guide.md](docs/run_guide.md)
- [tuning_guide.md](docs/tuning_guide.md)
- [experiment_policy.md](docs/experiment_policy.md)

## Ghi Chu

- Code chinh nam trong `src/`, notebook chi goi ham va trinh bay ket qua.
- Repo uu tien reproducible va so sanh phuong phap de phuc vu cham diem va viet bao cao.
- Neu schema dataset khac voi phien ban mac dinh, hay cap nhat `configs/params.yaml` truoc khi chay.
