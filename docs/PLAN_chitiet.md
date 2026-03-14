# Đề Tài 1: Phân Tích Doanh Số Siêu Thị

## Summary
- Repo sẽ được thiết kế đúng yêu cầu PDF: có cấu trúc chuẩn, chạy lại được, notebook đi theo pipeline `01 -> 05`, code chính nằm trong `src`, kết quả sinh ra trong `outputs`.
- Bản plan này bổ sung đầy đủ 3 phần còn thiếu theo yêu cầu mới của bạn:
  1. một hệ thống `logs / experiment tracking` để ghi lịch sử chạy, version, tham số, metric và kết luận;
  2. tài liệu hướng dẫn chạy và tài liệu tinh chỉnh để biết nên sửa gì khi muốn kết quả tốt hơn;
  3. mô tả rõ đề tài đang tập trung vào đâu và output cuối cùng của project là gì.
- Trọng tâm học thuật của đề tài sẽ là: `khai phá giỏ hàng`, `phân cụm khách hàng`, và `dự báo doanh số theo thời gian`, vì đây là 3 nhánh phù hợp nhất với rubric và dữ liệu Superstore.

## Topic Focus Và Final Output
- Đề tài không chỉ dừng ở việc “dự đoán sales”, mà tập trung vào 3 câu hỏi phân tích có giá trị báo cáo:
  1. Những mặt hàng hoặc nhóm sản phẩm nào thường đi cùng nhau để hỗ trợ cross-sell/up-sell.
  2. Có thể chia khách hàng thành các nhóm hành vi nào để hiểu chân dung mua sắm.
  3. Doanh số theo tuần/tháng được dự báo tốt nhất bằng phương pháp nào.
- Output cuối cùng của project sẽ gồm:
  - một repo hoàn chỉnh, chạy lại được;
  - bộ notebook phân tích theo đúng thứ tự;
  - dữ liệu đã xử lý trong `data/processed`;
  - bảng luật kết hợp, profile cụm khách hàng, bảng so sánh mô hình forecast;
  - biểu đồ, bảng số liệu, artifact cho báo cáo;
  - file log kết quả để so sánh các lần chạy;
  - tài liệu README/docs đủ để viết báo cáo lớn.
- Output cuối cùng về mặt học thuật phải trả lời được:
  - nhóm sản phẩm nào nên bán kèm;
  - nhóm khách hàng nào có giá trị cao hoặc hành vi khác biệt;
  - mô hình forecast nào tốt nhất theo `MAE`, `RMSE`, `sMAPE`;
  - ít nhất 5 insight có thể hành động được.

## Implementation Changes
- Tạo cấu trúc repo chuẩn:
  - `configs/`
  - `data/raw/`, `data/processed/`
  - `docs/`
  - `notebooks/`
  - `src/`
  - `scripts/`
  - `outputs/figures`, `outputs/tables`, `outputs/models`, `outputs/reports`, `outputs/logs`
- `README.md` ở root sẽ ngắn gọn, tập trung vào:
  - project là gì;
  - output cuối cùng là gì;
  - cách cài đặt;
  - cách chạy đúng thứ tự;
  - các file quan trọng cần sửa trước khi chạy.
- Bổ sung tài liệu chi tiết trong `docs/`:
  - `docs/project_focus.md`: giải thích rõ đề tài tập trung vào 3 nhánh nào, vì sao chọn, nhánh nào là core, nhánh nào là baseline.
  - `docs/data_dictionary.md`: mô tả đầy đủ cột dữ liệu, kiểu dữ liệu, ý nghĩa business, target sử dụng ở từng nhánh.
  - `docs/report_outline.md`: khung nội dung báo cáo đúng thứ tự PDF.
  - `docs/run_guide.md`: hướng dẫn chạy từ đầu đến cuối.
  - `docs/tuning_guide.md`: hướng dẫn nên chỉnh tham số nào để cải thiện kết quả.
  - `docs/experiment_policy.md`: quy tắc ghi log, đặt tên run, cách đọc log và cách so sánh các version.
- Hệ thống `logs / experiment tracking` sẽ gồm cả bản dễ đọc và bản máy đọc được:
  - `outputs/reports/RESULTS_LOG.md`: file log dạng đọc tay, ghi `Kết quả 01`, `Kết quả 02`, `Kết quả 03`... để phục vụ viết báo cáo và so sánh phương pháp.
  - `outputs/reports/results_registry.csv`: bảng tổng hợp chuẩn hóa, mỗi dòng là một lần chạy.
  - `outputs/logs/run_<timestamp>.json`: log chi tiết cho từng run, gồm config, tham số, metric, thời gian chạy, ghi chú.
  - `outputs/logs/best_runs_summary.md`: tóm tắt run tốt nhất theo từng tác vụ.
- Mỗi log run phải ghi tối thiểu:
  - `run_id`
  - `run_time`
  - `task` (`association`, `clustering`, `forecasting`)
  - `dataset_version`
  - `code_version` hoặc `git_commit` nếu có
  - `key_params`
  - `split_strategy`
  - `metrics`
  - `output_paths`
  - `notes`
  - `conclusion` (`tốt hơn`, `kém hơn`, `chưa ổn`)
- `configs/params.yaml` sẽ là nơi điều chỉnh chính:
  - đường dẫn dữ liệu;
  - seed;
  - cấu hình preprocessing;
  - ngưỡng support/confidence/lift;
  - danh sách feature cho clustering;
  - loại split thời gian;
  - horizon forecast;
  - tham số baseline và model nâng cao.
- `src/data/`
  - `loader.py`: đọc file CSV, parse ngày, kiểm tra schema.
  - `cleaner.py`: xử lý missing, duplicate, dữ liệu bất thường, chuẩn hóa text/categorical.
- `src/features/`
  - `builder.py`: tạo basket transactions, RFM, customer-level features, lag/rolling/calendar features cho forecast.
- `src/mining/`
  - `association_rules.py`: Apriori hoặc FP-Growth, tính support/confidence/lift, lưu top rules.
  - `clustering.py`: KMeans và Agglomerative, đánh giá bằng silhouette/DBI, sinh profile cụm.
- `src/models/`
  - `forecasting.py`: `naive`, `moving average`, `Holt-Winters`, `SARIMAX`.
- `src/evaluation/`
  - `metrics.py`: metric cho clustering và forecast.
  - `report.py`: gom bảng so sánh, chọn best run, ghi log.
- `src/visualization/plots.py`
  - các hàm vẽ dùng chung cho notebook và report.
- Notebook pipeline:
  - `01_eda.ipynb`: chất lượng dữ liệu, data dictionary sơ bộ, biểu đồ chính, seasonality sơ bộ.
  - `02_preprocess_feature.ipynb`: cleaning, feature engineering, lưu processed data.
  - `03_mining.ipynb`: association rules + clustering + profiling.
  - `04_modeling_forecasting.ipynb`: so sánh baseline và model forecast.
  - `05_evaluation_report.ipynb`: tổng hợp kết quả cuối, insight, bảng dùng cho báo cáo.
- Script chạy:
  - `scripts/run_pipeline.py`: chạy pipeline bằng code.
  - `scripts/run_papermill.py`: chạy lại toàn bộ notebook và sinh artifact.
  - `scripts/export_results.py`: gom metric và cập nhật `RESULTS_LOG.md`, `results_registry.csv`, `run_<timestamp>.json`.

## Run Guide Và Tuning Guide
- `docs/run_guide.md` phải chỉ rõ người dùng cần sửa những gì trước khi chạy:
  - đặt dataset vào `data/raw/train.csv`;
  - kiểm tra đúng tên cột nếu version Kaggle khác;
  - cập nhật `configs/params.yaml`;
  - cài package từ `requirements.txt`;
  - chạy `python scripts/run_papermill.py` hoặc `python scripts/run_pipeline.py`.
- `docs/run_guide.md` cũng phải giải thích thứ tự chạy và khi nào dùng notebook, khi nào dùng script.
- `docs/tuning_guide.md` phải ghi rõ “muốn kết quả tốt hơn thì chỉnh gì”:
  - với association rules: chỉnh `min_support`, `min_confidence`, mức item theo `Sub-Category` hay `Product Name`;
  - với clustering: chọn feature set, scaling, số cụm `k`, cách đánh đổi giữa metric và khả năng diễn giải;
  - với forecasting: đổi tần suất `week/month`, số lag, rolling window, seasonal period, train/test split;
  - với preprocessing: cách xử lý outlier, discount bất thường, missing dates, duplicate orders.
- `docs/tuning_guide.md` phải nêu dấu hiệu nhận biết chỉnh tốt:
  - rules bớt nhiễu, lift cao hơn, dễ diễn giải hơn;
  - cụm có silhouette tốt hơn và profile rõ hơn;
  - forecast có `MAE/RMSE/sMAPE` thấp hơn và residual ổn hơn.
- `docs/tuning_guide.md` cũng phải nêu các lỗi phổ biến:
  - leakage do split sai thời gian;
  - rules quá nhiều vì support quá thấp;
  - clustering đẹp về metric nhưng vô nghĩa về business;
  - forecast overfit do lag/seasonality quá phức tạp.

## Test Plan
- Kiểm tra repo có thể chạy lại từ môi trường mới chỉ bằng:
  - cài package;
  - cập nhật `configs/params.yaml`;
  - chạy script chính.
- Kiểm tra validator dừng sớm nếu thiếu cột hoặc parse ngày thất bại.
- Kiểm tra `01 -> 05` notebook chạy theo đúng thứ tự và sinh ra file trong `outputs/`.
- Kiểm tra `RESULTS_LOG.md`, `results_registry.csv`, `run_<timestamp>.json` đều được cập nhật sau mỗi lần chạy.
- Kiểm tra ít nhất:
  - 1 bảng top association rules;
  - 1 bảng so sánh ít nhất 2 thuật toán clustering;
  - 1 bảng forecast với ít nhất 2 baseline và 2 model nâng cao;
  - 1 file tổng hợp best run.
- Kiểm tra notebook không chứa logic lớn; logic chính phải nằm ở `src`.
- Kiểm tra có đủ material để viết báo cáo theo PDF: data dictionary, EDA, mining core, baseline, metric, insight, reproducibility.

## Assumptions
- Root README sẽ ngắn gọn; phân tích sâu và hướng dẫn chi tiết nằm trong `docs/`.
- Dataset chính là file Kaggle `train.csv`; nếu schema thực tế khác, validator và docs sẽ cập nhật theo file thật.
- V1 không làm GUI/demo và không thêm semi-supervised.
- Hệ thống log được thiết kế để dùng tiếp cho các version sau, không chỉ cho một lần chạy.
- Final outputs ưu tiên phục vụ chấm điểm, viết báo cáo và so sánh phương pháp hơn là triển khai production.


####################################################################
# Thực thi xong các file như sau: 

Đã triển khai xong repo theo plan và chạy được trên dữ liệu thật `data/raw/train.csv`. Khung dự án, docs, notebooks, pipeline, forecasting, mining, clustering và hệ `logs` đều đã có. Điểm bắt đầu chính là [README.md](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/README.md), [params.yaml](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/configs/params.yaml), [run_guide.md](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/docs/run_guide.md), [run_pipeline.py](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/scripts/run_pipeline.py) và [run_papermill.py](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/scripts/run_papermill.py).

Tôi đã sinh ra artifact và log thực tế trong [outputs/reports/RESULTS_LOG.md](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/outputs/reports/RESULTS_LOG.md), [results_registry.csv](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/outputs/reports/results_registry.csv) và [best_runs_summary.md](/d:/CODE/DNU_Data_Mining/DataminingSupperMarketSales/outputs/logs/best_runs_summary.md). Kết quả hiện tại từ lần chạy thật:
- Association rules: `2` rule, `max_lift = 1.193768`
- Clustering: tốt nhất là `kmeans`, `k=2`, `silhouette = 0.35593`
- Forecasting: tốt nhất là `sarimax`, `MAE = 3371.72`, `RMSE = 3861.79`, `sMAPE = 115.99`

Tôi đã xác minh:
- `python -m compileall src scripts`
- `python scripts/run_pipeline.py --check-only`
- `python scripts/run_pipeline.py`
- `python scripts/run_papermill.py`
- `python scripts/export_results.py`

Có vài warning runtime từ `sklearn` trên Windows MKL và `statsmodels` khi fit Holt-Winters, nhưng pipeline và notebook vẫn chạy thành công. Nếu muốn, bước tiếp theo hợp lý là tôi tinh chỉnh `configs/params.yaml` để tăng số luật kết hợp, thử lại `k` cho clustering, và cải thiện forecast rồi ghi thêm các `Kết quả 04, 05, 06...` vào log.