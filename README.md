# DataminingSupperMarketSales

Phân tích doanh số siêu thị theo hướng Data Mining với 3 nhánh chính:

- khai phá giỏ hàng để tìm cơ hội `cross-sell / up-sell`
- phân cụm khách hàng để xây dựng chân dung mua sắm
- dự báo doanh số theo thời gian để so sánh các mô hình forecast

Dataset dự kiến: `train.csv` từ Kaggle `rohitsahoo/sales-forecasting`.

## Kết Quả Cuối Cùng

Sau khi chạy xong, repo sẽ sinh ra:

- dữ liệu đã xử lý trong `data/processed/`
- bảng top `association rules`, bảng so sánh `clustering`, bảng so sánh `forecasting`
- hình vẽ, bảng metric và các artifact trong `outputs/`
- file log kết quả để so sánh các lần chạy:
  - `outputs/reports/RESULTS_LOG.md`
  - `outputs/reports/results_registry.csv`
  - `outputs/logs/run_<timestamp>.json`
  - `outputs/logs/best_runs_summary.md`
- bộ notebook `01 -> 05` để trình bày pipeline và viết báo cáo

## Cấu Trúc Chính

- `configs/params.yaml`: tham số và đường dẫn cần chỉnh trước khi chạy
- `docs/`: hướng dẫn chi tiết, data dictionary, tuning guide, experiment policy
- `notebooks/`: notebook báo cáo theo đúng thứ tự pipeline
- `src/`: code chính của dự án
- `scripts/`: script chạy pipeline, notebook và xuất kết quả
- `outputs/`: artifacts, log, bảng metric, báo cáo

## Cách Chạy Nhanh

1. Tải dataset và đặt file vào `data/raw/train.csv`.
2. Mở `configs/params.yaml` và kiểm tra lại tên cột nếu version dataset khác.
3. Tạo virtual environment để tránh xung đột môi trường:

```bash
python -m venv .venv
```

Nếu máy của bạn dùng `python3` thay vì `python`, hãy dùng:

```bash
python3 -m venv .venv
```

4. Kích hoạt virtual environment tùy theo hệ điều hành:

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

Sau khi kích hoạt thành công, bạn sẽ thấy `(.venv)` ở đầu dòng lệnh.

5. Cài thư viện:

```bash
python -m pip install -r requirements.txt
```

Nếu đang dùng `python3`, có thể dùng:

```bash
python3 -m pip install -r requirements.txt
```

6. Chạy pipeline bằng code:

```bash
python scripts/run_pipeline.py
```

Hoặc nếu máy bạn dùng `python3`:

```bash
python3 scripts/run_pipeline.py
```

7. Hoặc chạy lại toàn bộ notebook:

```bash
python scripts/run_papermill.py
```

Hoặc:

```bash
python3 scripts/run_papermill.py
```

8. Khi muốn thoát khỏi virtual environment:

```bash
deactivate
```

## Trước Khi Chạy Cần Sửa Gì

- `configs/params.yaml`
  - `paths.raw_data`
  - `data.required_columns`
  - `data.column_aliases`
  - `association`
  - `clustering`
  - `forecasting`

Tài liệu chi tiết:

- [project_focus.md](docs/project_focus.md)
- [data_dictionary.md](docs/data_dictionary.md)
- [run_guide.md](docs/run_guide.md)
- [tuning_guide.md](docs/tuning_guide.md)
- [experiment_policy.md](docs/experiment_policy.md)

## Ghi Chú

- Code chính nằm trong `src/`, notebook chỉ gọi hàm và trình bày kết quả.
- Repo ưu tiên `reproducible` và so sánh phương pháp để phục vụ chấm điểm và viết báo cáo.
- Nếu schema dataset khác với phiên bản mặc định, hãy cập nhật `configs/params.yaml` trước khi chạy.
