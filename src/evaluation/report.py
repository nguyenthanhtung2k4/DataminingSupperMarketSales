from __future__ import annotations

import csv
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from src.config import detect_dataset_version, get_git_commit, resolve_path


TRACKING_HEADER = [
    "run_id",
    "run_time",
    "task",
    "dataset_version",
    "code_version",
    "split_strategy",
    "metrics_json",
    "key_params_json",
    "output_paths_json",
    "notes",
    "conclusion",
]

TASK_PRIMARY_METRICS = {
    "association": "avg_lift_top5",
    "clustering": "silhouette",
    "forecasting": "sMAPE",
}


def _make_json_ready(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _make_json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_make_json_ready(item) for item in value]
    if hasattr(value, "item"):
        return value.item()
    return value


def _safe_float(value: Any, default: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return default if math.isnan(number) else number


def rank_metrics_for_task(task: str, metrics: dict[str, Any]) -> tuple[float, ...]:
    if task == "association":
        return (
            _safe_float(metrics.get("avg_lift_top5"), float("-inf")),
            _safe_float(metrics.get("rule_count"), float("-inf")),
            _safe_float(metrics.get("max_lift"), float("-inf")),
        )
    if task == "clustering":
        return (
            _safe_float(metrics.get("silhouette"), float("-inf")),
            -_safe_float(metrics.get("davies_bouldin"), float("inf")),
            _safe_float(metrics.get("best_k"), float("-inf")),
        )
    if task == "forecasting":
        return (
            -_safe_float(metrics.get("sMAPE"), float("inf")),
            -_safe_float(metrics.get("RMSE"), float("inf")),
            -_safe_float(metrics.get("MAE"), float("inf")),
        )
    return tuple()


def _row_rank(task: str, row: dict[str, str]) -> tuple[float, ...]:
    metrics = json.loads(row["metrics_json"])
    if task != "clustering":
        return rank_metrics_for_task(task, metrics)

    key_params = json.loads(row["key_params_json"])
    features = key_params.get("features", [])
    feature_quality = 0.0 if {"avg_discount", "profit_margin"} & set(features) else 1.0
    return (feature_quality, *rank_metrics_for_task(task, metrics))


def write_dataframe(df: pd.DataFrame, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def _next_result_index(results_log_path: Path) -> int:
    if not results_log_path.exists():
        return 1
    text = results_log_path.read_text(encoding="utf-8")
    return text.count("## Ket qua") + 1


def _load_registry_rows(registry_path: Path) -> list[dict[str, str]]:
    if not registry_path.exists():
        return []
    with registry_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def _parse_run_time(row: dict[str, str]) -> datetime:
    return datetime.strptime(row["run_time"], "%Y-%m-%d %H:%M:%S")


def _latest_task_rows(task: str, rows: list[dict[str, str]]) -> list[dict[str, str]]:
    task_rows = [row for row in rows if row.get("task") == task]
    if not task_rows:
        return []
    latest_row = max(task_rows, key=_parse_run_time)
    latest_dataset_version = latest_row.get("dataset_version")
    return [row for row in task_rows if row.get("dataset_version") == latest_dataset_version]


def _best_registry_row(task: str, rows: list[dict[str, str]], latest_only: bool = True) -> dict[str, str] | None:
    task_rows = _latest_task_rows(task, rows) if latest_only else [row for row in rows if row.get("task") == task]
    if not task_rows:
        return None
    return max(task_rows, key=lambda row: _row_rank(task, row))


def _comparison(task: str, current_metrics: dict[str, Any], previous_metrics: dict[str, Any] | None) -> str:
    if previous_metrics is None:
        return "chua on"
    return "tot hon" if rank_metrics_for_task(task, current_metrics) > rank_metrics_for_task(task, previous_metrics) else "kem hon"


def _resolve_primary_metric(task: str, metrics: dict[str, Any]) -> tuple[str | None, float | None]:
    metric_name = TASK_PRIMARY_METRICS.get(task)
    if not metric_name or metric_name not in metrics:
        return None, None
    return metric_name, _safe_float(metrics.get(metric_name), None)


def _append_results_log(entry: dict[str, Any], results_log_path: Path) -> None:
    result_index = _next_result_index(results_log_path)
    header = "# RESULTS LOG\n\nFile nay ghi theo dang doc tay de phuc vu viet bao cao.\n"
    block = [
        f"## Ket qua {result_index:02d}",
        "",
        f"- run_id: `{entry['run_id']}`",
        f"- run_time: `{entry['run_time']}`",
        f"- task: `{entry['task']}`",
        f"- dataset_version: `{entry['dataset_version']}`",
        f"- code_version: `{entry['code_version']}`",
        f"- split_strategy: `{entry['split_strategy']}`",
        f"- metrics: `{json.dumps(entry['metrics'], ensure_ascii=False)}`",
        f"- key_params: `{json.dumps(entry['key_params'], ensure_ascii=False)}`",
        f"- output_paths: `{json.dumps(entry['output_paths'], ensure_ascii=False)}`",
        f"- notes: {entry['notes']}",
        f"- conclusion: **{entry['conclusion']}**",
        "",
    ]
    existing_text = results_log_path.read_text(encoding="utf-8") if results_log_path.exists() else ""
    placeholder = "Chua co run nao duoc ghi."
    if not existing_text.strip() or "## Ket qua" not in existing_text:
        results_log_path.write_text(f"{header}\n" + "\n".join(block), encoding="utf-8")
        return

    if placeholder in existing_text:
        existing_text = existing_text.replace(f"\n{placeholder}\n", "\n").replace(placeholder, "")
        results_log_path.write_text(existing_text.rstrip() + "\n\n" + "\n".join(block), encoding="utf-8")
        return

    with results_log_path.open("a", encoding="utf-8") as file:
        if results_log_path.stat().st_size > 0:
            file.write("\n")
        file.write("\n".join(block))


def _append_registry(entry: dict[str, Any], registry_path: Path) -> None:
    registry_exists = registry_path.exists()
    with registry_path.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=TRACKING_HEADER)
        if not registry_exists:
            writer.writeheader()
        writer.writerow(
            {
                "run_id": entry["run_id"],
                "run_time": entry["run_time"],
                "task": entry["task"],
                "dataset_version": entry["dataset_version"],
                "code_version": entry["code_version"],
                "split_strategy": entry["split_strategy"],
                "metrics_json": json.dumps(entry["metrics"], ensure_ascii=False),
                "key_params_json": json.dumps(entry["key_params"], ensure_ascii=False),
                "output_paths_json": json.dumps(entry["output_paths"], ensure_ascii=False),
                "notes": entry["notes"],
                "conclusion": entry["conclusion"],
            }
        )


def _write_run_json(entry: dict[str, Any], logs_dir: Path) -> Path:
    stamp = entry["run_time"].replace(":", "").replace("-", "").replace(" ", "_")
    path = logs_dir / f"run_{stamp}_{entry['task']}.json"
    path.write_text(json.dumps(entry, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def export_tracking_summary(config: dict[str, Any], project_root: str | Path | None = None) -> Path:
    reports_dir = resolve_path(config["paths"]["reports_dir"], project_root)
    logs_dir = resolve_path(config["paths"]["logs_dir"], project_root)
    registry_path = reports_dir / "results_registry.csv"
    summary_path = logs_dir / "best_runs_summary.md"

    rows = _load_registry_rows(registry_path)
    if not rows:
        summary_path.write_text("# Best Runs Summary\n\nChua co du lieu run de tong hop.\n", encoding="utf-8")
        return summary_path

    lines = ["# Best Runs Summary", ""]
    for task in ["association", "clustering", "forecasting"]:
        task_rows = _latest_task_rows(task, rows)
        best_row = _best_registry_row(task, rows, latest_only=True)
        if not best_row:
            continue
        metrics = json.loads(best_row["metrics_json"])
        metric_name, metric_value = _resolve_primary_metric(task, metrics)
        if not metric_name:
            continue
        ranked_rows = sorted(
            task_rows,
            key=lambda row: _row_rank(task, row),
            reverse=True,
        )
        summary_conclusion = "chua on"
        if len(ranked_rows) > 1:
            top_metrics = json.loads(ranked_rows[0]["metrics_json"])
            second_metrics = json.loads(ranked_rows[1]["metrics_json"])
            if _row_rank(task, ranked_rows[0]) > _row_rank(task, ranked_rows[1]):
                summary_conclusion = "tot hon"
        lines.extend(
            [
                f"## {task}",
                f"- run_id: `{best_row['run_id']}`",
                f"- run_time: `{best_row['run_time']}`",
                f"- metric_chinh: `{metric_name}` = `{metric_value}`",
                f"- conclusion: **{summary_conclusion}**",
                "",
            ]
        )

    summary_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return summary_path


def _format_table(df: pd.DataFrame) -> pd.DataFrame:
    formatted = df.copy()
    for column in formatted.columns:
        if pd.api.types.is_float_dtype(formatted[column]):
            formatted[column] = formatted[column].map(
                lambda value: f"{value:.4f}" if abs(value) < 100 else f"{value:.2f}"
            )
        elif pd.api.types.is_integer_dtype(formatted[column]):
            formatted[column] = formatted[column].map(lambda value: f"{int(value)}")
    return formatted


def export_report_tables(config: dict[str, Any], project_root: str | Path | None = None) -> dict[str, Path]:
    raw_path = resolve_path(config["paths"]["raw_data"], project_root)
    processed_dir = resolve_path(config["paths"]["processed_dir"], project_root)
    tables_dir = resolve_path(config["paths"]["tables_dir"], project_root)
    tables_dir.mkdir(parents=True, exist_ok=True)

    cleaned_path = processed_dir / "cleaned_sales.csv"
    if not cleaned_path.exists():
        raise FileNotFoundError(
            f"Processed data not found at {cleaned_path}. Run the pipeline before exporting report tables."
        )

    raw_df = pd.read_csv(raw_path)
    cleaned_df = pd.read_csv(cleaned_path, parse_dates=["Order Date"])

    dataset_summary = pd.DataFrame(
        [
            {
                "Rows": int(len(raw_df)),
                "Columns": int(len(raw_df.columns)),
                "Cleaned Rows": int(len(cleaned_df)),
                "Orders": int(cleaned_df["Order ID"].nunique()),
                "Customers": int(cleaned_df["Customer Key"].nunique()),
                "Date Start": cleaned_df["Order Date"].min().strftime("%Y-%m-%d"),
                "Date End": cleaned_df["Order Date"].max().strftime("%Y-%m-%d"),
                "Total Sales (USD)": round(float(cleaned_df["Sales"].sum()), 2),
            }
        ]
    )

    association_rules = pd.read_csv(tables_dir / "association_rules.csv")
    association_top = association_rules.loc[
        :, ["antecedent", "consequent", "support", "confidence", "lift"]
    ].head(8)
    association_top = association_top.rename(
        columns={
            "antecedent": "Antecedent",
            "consequent": "Consequent",
            "support": "Support",
            "confidence": "Confidence",
            "lift": "Lift",
        }
    ).round(4)

    clustering_comparison = pd.read_csv(tables_dir / "clustering_comparison.csv")
    clustering_best = clustering_comparison.loc[:, ["algorithm", "k", "silhouette", "davies_bouldin"]].head(5)
    clustering_best = clustering_best.rename(
        columns={
            "algorithm": "Algorithm",
            "k": "k",
            "silhouette": "Silhouette",
            "davies_bouldin": "Davies-Bouldin",
        }
    ).round(4)

    cluster_profile = pd.read_csv(tables_dir / "cluster_profile.csv")
    cluster_profile_top = cluster_profile.loc[
        :, ["cluster", "customer_count", "total_sales", "avg_order_value", "recency_days", "unique_subcategories"]
    ]
    cluster_profile_top = cluster_profile_top.rename(
        columns={
            "cluster": "Cluster",
            "customer_count": "Customer Count",
            "total_sales": "Average Sales",
            "avg_order_value": "Average Order Value",
            "recency_days": "Recency (Days)",
            "unique_subcategories": "Category Diversity",
        }
    ).round(3)

    forecast_comparison = pd.read_csv(tables_dir / "forecast_comparison.csv")
    forecast_best = forecast_comparison.loc[:, ["model", "status", "MAE", "RMSE", "sMAPE"]].head(4)
    forecast_best = forecast_best.rename(
        columns={
            "model": "Model",
            "status": "Status",
            "MAE": "MAE",
            "RMSE": "RMSE",
            "sMAPE": "sMAPE",
        }
    ).round(3)

    selected_params = pd.DataFrame(
        [
            {
                "Task": "Association",
                "Selected Parameters": json.dumps(config["association"], ensure_ascii=False),
            },
            {
                "Task": "Clustering",
                "Selected Parameters": json.dumps(
                    {
                        "features": config["clustering"]["features"],
                        "algorithms": config["clustering"]["algorithms"],
                        "candidate_k": config["clustering"]["candidate_k"],
                    },
                    ensure_ascii=False,
                ),
            },
            {
                "Task": "Forecasting",
                "Selected Parameters": json.dumps(config["forecasting"], ensure_ascii=False),
            },
        ]
    )

    output_paths = {
        "dataset_summary": write_dataframe(dataset_summary, tables_dir / "report_dataset_summary.csv"),
        "association_top": write_dataframe(association_top, tables_dir / "report_association_top.csv"),
        "clustering_best": write_dataframe(clustering_best, tables_dir / "report_clustering_best.csv"),
        "cluster_profile_top": write_dataframe(cluster_profile_top, tables_dir / "report_cluster_profile_top.csv"),
        "forecast_best": write_dataframe(forecast_best, tables_dir / "report_forecast_best.csv"),
        "selected_params": write_dataframe(selected_params, tables_dir / "report_selected_params.csv"),
    }
    return output_paths


def _latex_escape(value: Any) -> str:
    text = str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _render_latex_table(df: pd.DataFrame, caption: str, label: str) -> str:
    if df.empty:
        return f"\\paragraph{{Note}} No data was available for {caption.lower()}.\n"
    table_body = _format_table(df).to_latex(index=False, escape=True)
    return "\n".join(
        [
            "\\begin{table}[H]",
            "\\centering",
            "\\small",
            f"\\caption{{{_latex_escape(caption)}}}",
            f"\\label{{{label}}}",
            "\\resizebox{\\textwidth}{!}{%",
            table_body.rstrip(),
            "}",
            "\\end{table}",
            "",
        ]
    )


def _render_figure(relative_path: str, caption: str, label: str) -> str:
    return "\n".join(
        [
            "\\begin{figure}[H]",
            "\\centering",
            f"\\includegraphics[width=0.92\\textwidth]{{{relative_path}}}",
            f"\\caption{{{_latex_escape(caption)}}}",
            f"\\label{{{label}}}",
            "\\end{figure}",
            "",
        ]
    )


def generate_report_tex(config: dict[str, Any], project_root: str | Path | None = None) -> Path:
    project_base = Path(project_root) if project_root else Path.cwd()
    docs_dir = project_base / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    export_report_tables(config, project_root)

    tables_dir = resolve_path(config["paths"]["tables_dir"], project_root)
    cleaned_df = pd.read_csv(resolve_path(config["paths"]["processed_dir"], project_root) / "cleaned_sales.csv", parse_dates=["Order Date"])

    dataset_summary = pd.read_csv(tables_dir / "report_dataset_summary.csv")
    association_top = pd.read_csv(tables_dir / "report_association_top.csv")
    clustering_best = pd.read_csv(tables_dir / "report_clustering_best.csv")
    cluster_profile_top = pd.read_csv(tables_dir / "report_cluster_profile_top.csv")
    forecast_best = pd.read_csv(tables_dir / "report_forecast_best.csv")
    selected_params = pd.read_csv(tables_dir / "report_selected_params.csv")

    dataset_summary_vi = dataset_summary.rename(
        columns={
            "Rows": "Số dòng",
            "Columns": "Số cột",
            "Cleaned Rows": "Dòng sau làm sạch",
            "Orders": "Số đơn hàng",
            "Customers": "Số khách hàng",
            "Date Start": "Ngày bắt đầu",
            "Date End": "Ngày kết thúc",
            "Total Sales (USD)": "Tổng doanh thu (USD)",
        }
    )
    association_top_vi = association_top.rename(
        columns={
            "Antecedent": "Vế trái",
            "Consequent": "Vế phải",
        }
    )
    clustering_best_vi = clustering_best.rename(
        columns={
            "Algorithm": "Thuật toán",
        }
    )
    cluster_profile_top_vi = cluster_profile_top.rename(
        columns={
            "Cluster": "Cụm",
            "Customer Count": "Số khách hàng",
            "Average Sales": "Doanh thu TB",
            "Average Order Value": "Giá trị đơn TB",
            "Recency (Days)": "Độ mới (ngày)",
            "Category Diversity": "Độ đa dạng danh mục",
        }
    )
    forecast_best_vi = forecast_best.rename(
        columns={
            "Model": "Mô hình",
            "Status": "Trạng thái",
        }
    )
    selected_params_vi = selected_params.rename(
        columns={
            "Task": "Nhánh",
            "Selected Parameters": "Tham số đã chọn",
        }
    )

    dataset_row = dataset_summary.iloc[0].to_dict()
    top_rule = association_top.iloc[0].to_dict() if not association_top.empty else {}
    best_cluster = clustering_best.iloc[0].to_dict() if not clustering_best.empty else {}
    top_cluster = cluster_profile_top.sort_values("Average Sales", ascending=False).iloc[0].to_dict()
    best_forecast = forecast_best.iloc[0].to_dict() if not forecast_best.empty else {}

    top_subcategories = (
        cleaned_df.groupby("Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
        .index.tolist()
    )
    top_subcategories_text = ", ".join(top_subcategories)

    report_text = f"""\\documentclass[12pt]{{article}}
\\usepackage[T5]{{fontenc}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[vietnamese]{{babel}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{float}}
\\usepackage{{caption}}
\\usepackage{{array}}
\\usepackage{{hyperref}}

\\hypersetup{{
  colorlinks=true,
  linkcolor=black,
  urlcolor=blue
}}

\\title{{Báo cáo dự án khai phá dữ liệu doanh số siêu thị}}
\\author{{Thành viên nhóm: [Điền họ tên và mã sinh viên]}}
\\date{{Ngày nộp: [Điền ngày]}}

\\begin{{document}}

\\begin{{titlepage}}
\\centering
{{\\Large Bài tập lớn Khai phá dữ liệu\\par}}
\\vspace{{1cm}}
{{\\huge \\textbf{{Phân tích doanh số siêu thị bằng khai phá dữ liệu}}\\par}}
\\vspace{{1.5cm}}
{{\\large Học phần: Dữ liệu lớn và Khai phá dữ liệu\\par}}
\\vspace{{0.5cm}}
{{\\large Đề tài: Phân tích doanh thu từ bộ dữ liệu bán hàng siêu thị\\par}}
\\vspace{{1.5cm}}
{{\\large Thành viên nhóm: [Điền họ tên và mã sinh viên]\\par}}
\\vspace{{0.5cm}}
{{\\large Giảng viên: ThS. Lê Thị Thùy Trang\\par}}
\\vfill
{{\\large Ngày nộp: [Điền ngày]\\par}}
\\end{{titlepage}}

\\begin{{abstract}}
Báo cáo này trình bày một dự án khai phá dữ liệu doanh số siêu thị theo hướng có thể tái lập toàn bộ bằng mã nguồn và cấu hình. Pipeline cuối cùng đã sửa lỗi phân tích ngày tháng theo định dạng ngày-tháng-năm để giữ lại đầy đủ {dataset_row["Rows"]} dòng dữ liệu, sau đó triển khai ba nhánh chính gồm luật kết hợp, phân cụm khách hàng và dự báo chuỗi thời gian. Toàn bộ bảng và hình trong báo cáo được sinh trực tiếp từ thư mục \\texttt{{outputs/}} để bảo đảm báo cáo luôn khớp với kết quả thực nghiệm gần nhất của repo.
\\end{{abstract}}

\\section{{Đặt vấn đề và phân tích yêu cầu}}
Đề tài tập trung vào bài toán doanh thu siêu thị dưới góc nhìn khai phá dữ liệu và phân tích kinh doanh. Mục tiêu không chỉ dừng ở dự báo doanh số, mà còn bao gồm khám phá các mẫu mua kèm giữa các nhóm sản phẩm, phân tách khách hàng theo hành vi mua sắm và so sánh các mô hình dự báo trên chuỗi thời gian doanh thu. Một nghiệm thu được xem là đạt khi repo chạy lại được, kết quả có khả năng diễn giải rõ ràng và báo cáo ưu tiên hình, bảng cùng các insight thay vì chèn mã nguồn dài.

Sau khi sửa lỗi ngày tháng, bộ dữ liệu cuối cùng có {dataset_row["Rows"]} dòng, {dataset_row["Columns"]} cột, {dataset_row["Orders"]} đơn hàng và {dataset_row["Customers"]} khách hàng phân biệt. Khoảng thời gian giao dịch trải dài từ {dataset_row["Date Start"]} đến {dataset_row["Date End"]} với tổng doanh thu {dataset_row["Total Sales (USD)"]} USD. Toàn bộ {dataset_row["Cleaned Rows"]} bản ghi đều được giữ lại sau bước làm sạch, thay vì bị mất hơn một nửa như trước khi sửa lỗi parse ngày.

{_render_latex_table(dataset_summary_vi, "Tóm tắt dữ liệu sau tiền xử lý", "tab:dataset-summary")}

Phân tích mô tả ban đầu cho thấy các nhóm hàng đóng góp doanh thu cao nhất là {top_subcategories_text}. Điều này cho thấy doanh thu tập trung vào một số nhóm sản phẩm quan trọng, từ đó phù hợp để khai thác thêm các luật kết hợp và đề xuất hành động kinh doanh.

{_render_figure("../outputs/figures/top_subcategories.png", "Các nhóm sản phẩm con đóng góp doanh thu cao nhất.", "fig:top-subcategories")}
{_render_figure("../outputs/figures/weekly_sales.png", "Chuỗi doanh thu tổng hợp sau khi sửa tiền xử lý ngày tháng.", "fig:weekly-sales")}

\\section{{Thiết kế giải pháp và quy trình khai phá dữ liệu}}
Pipeline của dự án tuân theo đúng logic tổng quát từ dữ liệu thô đến tiền xử lý, tạo đặc trưng, mô hình hóa, đánh giá và xuất báo cáo. Dữ liệu gốc được đọc từ file CSV, kiểm tra schema, chuẩn hóa tên cột và làm sạch thông qua cấu hình trong \\texttt{{configs/params.yaml}}. Thay đổi quan trọng nhất trong phiên bản cuối là parse \\texttt{{Order Date}} và \\texttt{{Ship Date}} theo chuẩn ngày-tháng-năm, nhờ đó tránh làm mất các dòng hợp lệ khi gặp ngày lớn hơn 12.

Sau bước tiền xử lý, pipeline được chia thành ba nhánh. Thứ nhất, dữ liệu giao dịch theo đơn hàng được chuyển thành giỏ hàng ở mức \\texttt{{Sub-Category}} để khai phá luật kết hợp. Thứ hai, dữ liệu được tổng hợp theo khách hàng để tạo các đặc trưng như độ mới giao dịch, số đơn hàng, tổng doanh thu, giá trị đơn hàng trung bình và độ đa dạng nhóm hàng phục vụ phân cụm. Thứ ba, doanh thu được resample thành chuỗi thời gian đều để so sánh các baseline với Holt-Winters và SARIMAX. Cách tổ chức này bám sát yêu cầu của rubric: có tri thức khai phá, có nhánh phân tích khách hàng và có nhánh dự báo.

\\section{{Phân tích mã nguồn và chức năng}}
Repo được tổ chức theo hướng module hóa để notebook chỉ đóng vai trò trình bày, còn toàn bộ logic chính nằm trong \\texttt{{src/}}. Gói \\texttt{{src/data}} phụ trách đọc dữ liệu, xác thực schema và làm sạch dữ liệu. Gói \\texttt{{src/features}} chịu trách nhiệm tạo basket transaction, tạo đặc trưng khách hàng và tạo chuỗi thời gian doanh số. Gói \\texttt{{src/mining}} hiện thực luật kết hợp và phân cụm khách hàng, trong khi \\texttt{{src/models}} cài đặt các baseline dự báo, Holt-Winters và SARIMAX. Cuối cùng, \\texttt{{src/evaluation}} đảm nhiệm tính metric, ghi log thí nghiệm, xuất bảng tóm tắt và sinh file LaTeX.

Khả năng tái lập được bảo đảm bằng cấu hình và script. Script \\texttt{{scripts/run\\_pipeline.py}} chạy toàn bộ pipeline từ đầu đến cuối. Script \\texttt{{scripts/run\\_experiments.py}} dùng để sweep tham số có kiểm soát theo tiêu chí báo cáo. Script \\texttt{{scripts/export\\_results.py}} cập nhật các bảng, log tóm tắt và file \\texttt{{docs/report.tex}}. Tất cả artifact cuối cùng đều nằm trong \\texttt{{outputs/figures}}, \\texttt{{outputs/tables}}, \\texttt{{outputs/reports}} và \\texttt{{outputs/logs}}.

\\section{{Thử nghiệm và kết quả}}
\\subsection{{Luật kết hợp}}
Nhánh luật kết hợp được chạy trên giỏ hàng theo đơn hàng, sử dụng \\texttt{{Sub-Category}} làm mức item chính. Cấu hình cuối được chọn để cân bằng giữa chất lượng luật và khả năng trình bày trong báo cáo. Luật mạnh nhất trong bảng kết quả là \\emph{{{_latex_escape(top_rule.get("Antecedent", "N/A"))} $\\rightarrow$ {_latex_escape(top_rule.get("Consequent", "N/A"))}}} với support {top_rule.get("Support", "N/A")}, confidence {top_rule.get("Confidence", "N/A")} và lift {top_rule.get("Lift", "N/A")}.

{_render_latex_table(association_top_vi, "Các luật kết hợp tiêu biểu được dùng trong báo cáo", "tab:association-rules")}

\\subsection{{Phân cụm khách hàng}}
Nhánh phân cụm khách hàng được tinh chỉnh theo hướng loại bỏ các đặc trưng không mang tín hiệu thực, đặc biệt là \\texttt{{avg\\_discount}} và \\texttt{{profit\\_margin}} vì dữ liệu gốc không có \\texttt{{Discount}} và \\texttt{{Profit}}. Kết quả tốt nhất cho mục tiêu báo cáo dùng {best_cluster.get("Algorithm", "N/A")} với $k={best_cluster.get("k", "N/A")}$, đạt silhouette {best_cluster.get("Silhouette", "N/A")} và Davies--Bouldin {best_cluster.get("Davies-Bouldin", "N/A")}. Cụm có giá trị cao hơn có doanh thu trung bình {top_cluster.get("Average Sales", "N/A")} và giá trị đơn hàng trung bình {top_cluster.get("Average Order Value", "N/A")}.

{_render_latex_table(clustering_best_vi, "Các phương án phân cụm tốt nhất sau khi tinh chỉnh", "tab:clustering-best")}
{_render_latex_table(cluster_profile_top_vi, "Hồ sơ các cụm khách hàng cuối cùng", "tab:cluster-profile")}
{_render_figure("../outputs/figures/cluster_profile.png", "Biểu đồ hồ sơ trung bình của các cụm khách hàng.", "fig:cluster-profile")}

\\subsection{{Dự báo doanh số}}
Nhánh dự báo được chạy lại sau khi sửa lỗi ngày tháng để chuỗi thời gian phản ánh đúng toàn bộ lịch sử bán hàng. Kết quả cuối cùng cho thấy mô hình tốt nhất là {best_forecast.get("Model", "N/A")} với MAE {best_forecast.get("MAE", "N/A")}, RMSE {best_forecast.get("RMSE", "N/A")} và sMAPE {best_forecast.get("sMAPE", "N/A")}. So với các baseline và SARIMAX, mô hình này bám xu hướng tốt hơn trên tập holdout và cho sai số tương đối thấp nhất.

{_render_latex_table(forecast_best_vi, "So sánh các mô hình dự báo trên tập holdout", "tab:forecast-best")}
{_render_figure("../outputs/figures/forecast_vs_actual.png", "So sánh mô hình dự báo tốt nhất với doanh số thực tế trên tập kiểm tra.", "fig:forecast-vs-actual")}

{_render_latex_table(selected_params_vi, "Bảng tóm tắt tham số cuối cùng của ba nhánh", "tab:selected-params")}

\\section{{Thảo luận và so sánh}}
Kết quả thực nghiệm cho thấy chất lượng dữ liệu đầu vào ảnh hưởng trực tiếp đến toàn bộ pipeline. Việc sửa parse ngày tháng giúp giữ lại đầy đủ dữ liệu và loại bỏ tình trạng chuỗi thời gian có các điểm bằng 0 giả tạo, vốn từng làm giảm mạnh chất lượng dự báo. Ở nhánh luật kết hợp, việc hạ ngưỡng phù hợp giúp thu được tập luật vừa đủ nhiều để phân tích mà không bị quá nhiễu. Ở nhánh phân cụm, tiêu chí diễn giải được đặt ngang hàng với metric, vì một mô hình có silhouette cao hơn rất ít nhưng dùng đặc trưng không thực chất sẽ không phù hợp để đưa vào báo cáo cuối.

Dự án vẫn còn một số giới hạn. Bộ dữ liệu hiện tại không có \\texttt{{Profit}} và \\texttt{{Discount}}, nên không thể phân tích lợi nhuận hoặc chính sách chiết khấu một cách thực chất. Ngoài ra, nhánh dự báo mới dừng ở mức doanh thu tổng hợp, chưa khai thác thêm seasonality theo vùng, theo danh mục hoặc theo từng nhóm sản phẩm chi tiết. Những giới hạn này cần được nêu rõ để giữ tính học thuật và tính trung thực của phần thảo luận.

\\section{{Tổng kết và hướng phát triển}}
Dự án đã xây dựng được một pipeline khai phá dữ liệu doanh số siêu thị có thể tái lập, phù hợp với yêu cầu repo chuẩn và báo cáo khoa học. Kết quả cuối cùng kết hợp được ba góc nhìn: luật kết hợp để phát hiện mẫu mua kèm, phân cụm để nhận diện hành vi khách hàng và dự báo để hỗ trợ lập kế hoạch doanh số ngắn hạn.

Từ góc độ ứng dụng, có thể rút ra ba nhóm hành động chính. Thứ nhất, các luật lift cao hỗ trợ đề xuất bán kèm hoặc thiết kế bundle sản phẩm. Thứ hai, kết quả phân cụm cho phép tách nhóm khách hàng giá trị cao với nhóm mua ít để phục vụ chiến dịch marketing phù hợp. Thứ ba, mô hình dự báo tốt nhất tạo ra một baseline khả dụng cho bài toán dự báo doanh thu trong giai đoạn hiện tại.

Trong các bước tiếp theo, dự án có thể mở rộng theo ba hướng: bổ sung dữ liệu lợi nhuận và chiết khấu để phân tích sâu hơn, xây dựng mô hình dự báo theo từng nhóm sản phẩm hoặc khu vực, và thử mức khai phá luật kết hợp chi tiết hơn ở cấp sản phẩm nếu cấu trúc giỏ hàng đủ dày.

\\end{{document}}
"""

    report_path = docs_dir / "report.tex"
    report_path.write_text(report_text, encoding="utf-8")
    return report_path


def log_experiment(
    *,
    config: dict[str, Any],
    task: str,
    metrics: dict[str, Any],
    key_params: dict[str, Any],
    output_paths: dict[str, str],
    split_strategy: str,
    notes: str,
    project_root: str | Path | None = None,
    data_path: str | Path | None = None,
) -> dict[str, Any]:
    reports_dir = resolve_path(config["paths"]["reports_dir"], project_root)
    logs_dir = resolve_path(config["paths"]["logs_dir"], project_root)
    reports_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    registry_path = reports_dir / "results_registry.csv"
    results_log_path = reports_dir / "RESULTS_LOG.md"
    dataset_version = detect_dataset_version(data_path) if data_path else "unknown"

    previous_best_row = _best_registry_row(task, _load_registry_rows(registry_path), latest_only=False)
    if previous_best_row and previous_best_row.get("dataset_version") != dataset_version:
        same_version_rows = [
            row
            for row in _load_registry_rows(registry_path)
            if row.get("task") == task and row.get("dataset_version") == dataset_version
        ]
        previous_best_row = (
            max(same_version_rows, key=lambda row: _row_rank(task, row))
            if same_version_rows
            else None
        )
    previous_best_metrics = json.loads(previous_best_row["metrics_json"]) if previous_best_row else None
    conclusion = _comparison(task, metrics, previous_best_metrics)

    run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_id = f"{task}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    entry = {
        "run_id": run_id,
        "run_time": run_time,
        "task": task,
        "dataset_version": dataset_version,
        "code_version": get_git_commit(project_root),
        "split_strategy": split_strategy,
        "metrics": _make_json_ready(metrics),
        "key_params": _make_json_ready(key_params),
        "output_paths": _make_json_ready(output_paths),
        "notes": notes,
        "conclusion": conclusion,
    }

    run_json_path = _write_run_json(entry, logs_dir)
    _append_registry(entry, registry_path)
    _append_results_log(entry, results_log_path)
    export_tracking_summary(config, project_root)
    entry["run_json_path"] = str(run_json_path)
    return entry
