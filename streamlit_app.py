from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
OUTPUTS_DIR = ROOT / "outputs"
TABLES_DIR = OUTPUTS_DIR / "tables"
FIGURES_DIR = OUTPUTS_DIR / "figures"
REPORTS_DIR = OUTPUTS_DIR / "reports"
LOGS_DIR = OUTPUTS_DIR / "logs"
DOCS_DIR = ROOT / "docs"


st.set_page_config(
    page_title="Kết quả Data Mining",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at top right, rgba(47, 96, 124, 0.10), transparent 26%),
            linear-gradient(180deg, #f8f3e8 0%, #efe5d3 100%);
        color: #17212b;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
    [data-testid="stSidebar"] {
        background: #1f2430;
    }
    [data-testid="stSidebar"] * {
        color: #f8fafc;
    }
    .hero {
        padding: 1.5rem 1.6rem;
        border-radius: 22px;
        background: linear-gradient(135deg, #18324c 0%, #2f607c 100%);
        margin-bottom: 1.1rem;
        box-shadow: 0 18px 34px rgba(24, 50, 76, 0.18);
    }
    .hero h1 {
        margin: 0 0 0.4rem 0;
        font-size: 2.15rem;
        color: #fffaf2 !important;
    }
    .hero p {
        margin: 0;
        line-height: 1.7;
        font-size: 1rem;
        color: #edf6fb !important;
    }
    .section-caption {
        color: #556274;
        margin-top: -0.25rem;
        margin-bottom: 0.85rem;
    }
    div[data-testid="stMetric"] {
        background: rgba(255, 251, 245, 0.82);
        border: 1px solid rgba(24, 50, 76, 0.08);
        padding: 0.95rem 1rem;
        border-radius: 16px;
        box-shadow: 0 10px 20px rgba(24, 50, 76, 0.06);
    }
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricValue"] {
        color: #13263b !important;
    }
    div[data-testid="stDataFrame"] {
        background: rgba(255, 252, 247, 0.94);
        border: 1px solid rgba(24, 50, 76, 0.10);
        border-radius: 18px;
        overflow: hidden;
    }
    div[data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #18324c 0%, #275873 100%);
        color: #f8fbff !important;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        min-height: 2.8rem;
    }
    div[data-testid="stDownloadButton"] > button:hover {
        background: linear-gradient(135deg, #214563 0%, #2f6a88 100%);
        color: #ffffff !important;
    }
    div[data-testid="stAlert"] {
        border-radius: 14px;
    }
    .pdf-meta {
        color: #5c6675;
        font-size: 0.92rem;
        line-height: 1.55;
    }
    .soft-note {
        padding: 0.95rem 1rem;
        border-radius: 14px;
        background: rgba(217, 230, 239, 0.92);
        border: 1px solid rgba(47, 96, 124, 0.10);
        color: #1b3042;
    }
    .stMarkdown, .stText, p, li, label, h1, h2, h3, h4, h5 {
        color: #17212b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


PAGE_OPTIONS = {
    "Tổng quan": "overview",
    "Luật kết hợp": "association",
    "Phân cụm": "clustering",
    "Phân loại": "classification",
    "Dự báo": "forecasting",
    "Thử nghiệm": "experiments",
    "Nhật ký & Tệp": "logs",
}

TASK_LABELS = {
    "association": "Luật kết hợp",
    "clustering": "Phân cụm",
    "classification": "Phân loại",
    "forecasting": "Dự báo",
}


@st.cache_data(show_spinner=False)
def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


@st.cache_data(show_spinner=False)
def load_registry() -> pd.DataFrame:
    registry_path = REPORTS_DIR / "results_registry.csv"
    df = load_csv(registry_path)
    if df.empty:
        return df

    for column in ["metrics_json", "key_params_json", "output_paths_json"]:
        if column in df.columns:
            df[column] = df[column].apply(
                lambda value: json.loads(value) if isinstance(value, str) and value else {}
            )

    if "run_time" in df.columns:
        df["run_time"] = pd.to_datetime(df["run_time"], errors="coerce")

    return df.sort_values("run_time", ascending=False).reset_index(drop=True)


def latest_output_time() -> str:
    candidates = [
        *OUTPUTS_DIR.glob("**/*.csv"),
        *OUTPUTS_DIR.glob("**/*.json"),
        *OUTPUTS_DIR.glob("**/*.md"),
        *OUTPUTS_DIR.glob("**/*.png"),
    ]
    if not candidates:
        return "Chưa có output"
    latest = max(candidates, key=lambda path: path.stat().st_mtime)
    return pd.Timestamp(latest.stat().st_mtime, unit="s").strftime("%Y-%m-%d %H:%M:%S")


def human_file_size(size_in_bytes: int) -> str:
    size = float(size_in_bytes)
    units = ["B", "KB", "MB", "GB"]
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size_in_bytes} B"


def format_task_name(value: Any) -> str:
    if not isinstance(value, str):
        return str(value)
    return TASK_LABELS.get(value, value.replace("_", " ").title())


def show_pdf_downloads() -> None:
    pdf_paths = sorted(DOCS_DIR.glob("*.pdf"))
    if not pdf_paths:
        st.info("Không tìm thấy file PDF trong thư mục `docs/`.")
        return

    for path in pdf_paths:
        modified = pd.Timestamp(path.stat().st_mtime, unit="s").strftime("%Y-%m-%d %H:%M")
        size_label = human_file_size(path.stat().st_size)
        title = path.stem.replace("_", " ")

        with st.container(border=True):
            info_col, action_col = st.columns([3.0, 1.1], vertical_alignment="center")
            with info_col:
                st.markdown(f"#### {title}")
                st.markdown(
                    (
                        "<div class='pdf-meta'>"
                        f"Tệp gốc: <code>{path.name}</code><br>"
                        f"Dung lượng: <strong>{size_label}</strong><br>"
                        f"Cập nhật: <strong>{modified}</strong>"
                        "</div>"
                    ),
                    unsafe_allow_html=True,
                )
            with action_col:
                with path.open("rb") as file:
                    st.download_button(
                        label="Tải PDF",
                        data=file.read(),
                        file_name=path.name,
                        mime="application/pdf",
                        width="stretch",
                    )


def safe_dataframe(path: Path, empty_message: str) -> pd.DataFrame:
    df = load_csv(path)
    if df.empty:
        st.warning(empty_message)
    return df


def render_image_if_exists(path: Path, caption: str | None = None) -> None:
    if path.exists():
        st.image(str(path), caption=caption, width="stretch")
    else:
        st.info(f"Chưa có hình: `{path.name}`")


def render_history_table(registry_df: pd.DataFrame) -> None:
    if registry_df.empty:
        st.warning("Chưa có `results_registry.csv`.")
        return

    display_df = registry_df[["run_time", "task", "dataset_version", "conclusion"]].copy()
    display_df["run_time"] = pd.to_datetime(display_df["run_time"], errors="coerce").dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    display_df["task"] = display_df["task"].apply(format_task_name)
    display_df = display_df.rename(
        columns={
            "run_time": "Thời gian chạy",
            "task": "Tác vụ",
            "dataset_version": "Phiên bản dữ liệu",
            "conclusion": "Kết luận",
        }
    )

    st.caption("Hiển thị 12 lần chạy gần nhất để bạn dễ theo dõi việc tinh chỉnh mô hình.")
    st.dataframe(display_df.head(12), width="stretch", hide_index=True, height=420)


def render_overview() -> None:
    association_df = load_csv(TABLES_DIR / "core" / "association_rules.csv")
    clustering_df = load_csv(TABLES_DIR / "core" / "clustering_comparison.csv")
    classification_df = load_csv(TABLES_DIR / "core" / "classification_comparison.csv")
    forecasting_df = load_csv(TABLES_DIR / "core" / "forecast_comparison.csv")
    registry_df = load_registry()

    st.markdown(
        """
        <div class="hero">
            <h1>Bảng điều khiển Kết quả khai thác dữ liệu</h1>
            <p>
                Giao diện này tổng hợp toàn bộ kết quả đã chạy từ pipeline và notebook:
                luật kết hợp, phân cụm, phân loại, dự báo, lịch sử thực nghiệm và tài liệu phục vụ báo cáo.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if not association_df.empty:
            top_rule = association_df.sort_values("lift", ascending=False).iloc[0]
            st.metric("Hiệp hội tốt nhất", f"{top_rule['lift']:.4f}", top_rule["antecedent"])
        else:
            st.metric("Hiệp hội tốt nhất", "Chưa có")
    with col2:
        if not clustering_df.empty:
            best_cluster = clustering_df.sort_values("silhouette", ascending=False).iloc[0]
            st.metric(
                "Phân cụm tốt nhất",
                f"{best_cluster['silhouette']:.4f}",
                f"{best_cluster['algorithm']} | k={best_cluster['k']}",
            )
        else:
            st.metric("Phân cụm tốt nhất", "Chưa có")
    with col3:
        if not classification_df.empty:
            best_cls = classification_df.sort_values("f1_macro", ascending=False).iloc[0]
            st.metric("Phân loại tốt nhất", f"{best_cls['f1_macro']:.4f}", best_cls["model"])
        else:
            st.metric("Phân loại tốt nhất", "Chưa có")
    with col4:
        if not forecasting_df.empty:
            best_forecast = forecasting_df.sort_values("sMAPE", ascending=True).iloc[0]
            st.metric("Dự báo tốt nhất", f"{best_forecast['sMAPE']:.4f}", best_forecast["model"])
        else:
            st.metric("Dự báo tốt nhất", "Chưa có")

    left, right = st.columns([1.35, 1], gap="large")
    with left:
        st.markdown("### Trạng thái hiện tại")
        st.caption("Tóm tắt nhanh dữ liệu đầu ra mà dashboard đang đọc.")
        with st.container(border=True):
            st.markdown(
                f"""
                - Bản cập nhật đầu ra mới nhất: `{latest_output_time()}`
                - Số lần chạy đã ghi nhật ký: `{len(registry_df)}`
                - Dashboard đọc trực tiếp từ `outputs/`, không tự chạy lại phân tích
                - Muốn cập nhật dữ liệu mới, hãy chạy lại `python scripts/run_pipeline.py`
                """
            )
            if not registry_df.empty:
                latest_row = registry_df.iloc[0]
                latest_task = format_task_name(latest_row["task"])
                st.markdown(
                    (
                        "<div class='soft-note'>"
                        f"Chạy mới nhất: <strong>{latest_task}</strong> | "
                        f"{latest_row['run_time']} | "
                        f"Kết luận: <strong>{latest_row['conclusion']}</strong>"
                        "</div>"
                    ),
                    unsafe_allow_html=True,
                )
    with right:
        st.markdown("### Tài liệu PDF")
        st.caption("Tải nhanh báo cáo nhóm và file hướng dẫn chính thức.")
        show_pdf_downloads()

    st.markdown("### Lịch sử chạy gần nhất")
    render_history_table(registry_df)


def render_association() -> None:
    st.markdown("### Luật kết hợp")
    st.markdown(
        "<div class='section-caption'>Hiển thị luật kết hợp có support, confidence và lift cao nhất.</div>",
        unsafe_allow_html=True,
    )
    render_image_if_exists(FIGURES_DIR / "top_subcategories.png", "Nhóm sản phẩm theo doanh số")
    rules_df = safe_dataframe(
        TABLES_DIR / "core" / "association_rules.csv",
        "Chưa có bảng `association_rules.csv`.",
    )
    if not rules_df.empty:
        st.dataframe(rules_df, width="stretch", hide_index=True, height=440)


def render_clustering() -> None:
    st.markdown("### Phân cụm")
    st.markdown(
        "<div class='section-caption'>So sánh thuật toán phân cụm và hồ sơ từng cụm khách hàng.</div>",
        unsafe_allow_html=True,
    )
    comparison_df = safe_dataframe(
        TABLES_DIR / "core" / "clustering_comparison.csv",
        "Chưa có bảng `clustering_comparison.csv`.",
    )
    profile_df = safe_dataframe(
        TABLES_DIR / "core" / "cluster_profile.csv",
        "Chưa có bảng `cluster_profile.csv`.",
    )

    col1, col2 = st.columns([1.15, 1], gap="large")
    with col1:
        if not comparison_df.empty:
            st.markdown("#### So sánh mô hình phân cụm")
            st.dataframe(comparison_df, width="stretch", hide_index=True)
    with col2:
        render_image_if_exists(FIGURES_DIR / "cluster_profile.png", "Tóm tắt hồ sơ cụm")

    if not profile_df.empty:
        st.markdown("#### Hồ sơ cụm")
        st.dataframe(profile_df, width="stretch", hide_index=True, height=440)


def render_classification() -> None:
    st.markdown("### Phân loại")
    st.markdown(
        "<div class='section-caption'>Theo dõi kết quả các mô hình phân loại và ma trận nhầm lẫn.</div>",
        unsafe_allow_html=True,
    )
    comparison_df = safe_dataframe(
        TABLES_DIR / "core" / "classification_comparison.csv",
        "Chưa có bảng `classification_comparison.csv`.",
    )
    class_report_df = safe_dataframe(
        TABLES_DIR / "core" / "classification_class_report.csv",
        "Chưa có bảng `classification_class_report.csv`.",
    )
    confusion_df = safe_dataframe(
        TABLES_DIR / "core" / "classification_confusion_matrix.csv",
        "Chưa có bảng `classification_confusion_matrix.csv`.",
    )

    if comparison_df.empty:
        return

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### So sánh mô hình")
        st.dataframe(comparison_df, width="stretch", hide_index=True)
    with col2:
        if not class_report_df.empty:
            st.markdown("#### Báo cáo theo lớp")
            st.dataframe(class_report_df, width="stretch", hide_index=True)

    if not confusion_df.empty:
        st.markdown("#### Ma trận nhầm lẫn")
        st.dataframe(confusion_df, width="stretch", hide_index=True)

    render_image_if_exists(
        FIGURES_DIR / "classification_confusion_matrix.png",
        "Biểu đồ confusion matrix",
    )


def render_forecasting() -> None:
    st.markdown("### Dự báo")
    st.markdown(
        "<div class='section-caption'>Theo dõi chuỗi thời gian, kết quả dự báo và residuals.</div>",
        unsafe_allow_html=True,
    )
    comparison_df = safe_dataframe(
        TABLES_DIR / "core" / "forecast_comparison.csv",
        "Chưa có bảng `forecast_comparison.csv`.",
    )
    residual_df = load_csv(TABLES_DIR / "core" / "forecast_residuals.csv")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        render_image_if_exists(FIGURES_DIR / "weekly_sales.png", "Doanh số theo thời gian")
    with col2:
        render_image_if_exists(FIGURES_DIR / "forecast_vs_actual.png", "Dự báo và thực tế")

    if not comparison_df.empty:
        st.markdown("#### So sánh mô hình dự báo")
        st.dataframe(comparison_df, width="stretch", hide_index=True)

    residual_figure = FIGURES_DIR / "forecast_residuals.png"
    if residual_figure.exists():
        render_image_if_exists(residual_figure, "Residuals")
    elif not residual_df.empty:
        st.markdown("#### Bảng residuals")
        st.dataframe(residual_df, width="stretch", hide_index=True, height=380)


def render_experiments() -> None:
    st.markdown("### Thử nghiệm")
    st.markdown(
        "<div class='section-caption'>Xem các bảng thử nghiệm sinh ra từ `scripts/run_experiments.py`.</div>",
        unsafe_allow_html=True,
    )
    experiment_dir = TABLES_DIR / "experiments"
    files = sorted(experiment_dir.glob("*.csv")) if experiment_dir.exists() else []
    if not files:
        st.info(
            "Hiện chưa có file trong `outputs/tables/experiments/`. "
            "Nếu muốn xem phần này, hãy chạy `python scripts/run_experiments.py`."
        )
        return

    selected = st.selectbox("Chọn file thử nghiệm", files, format_func=lambda path: path.name)
    st.dataframe(load_csv(selected), width="stretch", hide_index=True, height=460)


def render_logs() -> None:
    st.markdown("### Nhật ký & Tệp")
    st.markdown(
        "<div class='section-caption'>Tổng hợp các file Markdown, JSON log và notebook đã execute.</div>",
        unsafe_allow_html=True,
    )
    summary_md = load_text(LOGS_DIR / "best_runs_summary.md")
    results_log_md = load_text(REPORTS_DIR / "RESULTS_LOG.md")
    latest_logs = sorted(LOGS_DIR.glob("run_*.json"), reverse=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### Best Runs Summary")
        with st.container(border=True):
            st.markdown(summary_md or "Chưa có summary.")
    with col2:
        st.markdown("#### RESULTS_LOG")
        with st.container(border=True):
            st.markdown(results_log_md or "Chưa có file log.")

    if latest_logs:
        selected_log = st.selectbox(
            "Chọn log JSON chi tiết",
            latest_logs,
            format_func=lambda path: path.name,
        )
        st.json(load_json_file(selected_log))
    else:
        st.info("Chưa có file `run_*.json`.")

    executed_notebooks = sorted(REPORTS_DIR.glob("executed_*.ipynb"))
    if executed_notebooks:
        st.markdown("#### Notebook đã execute")
        st.write([path.name for path in executed_notebooks])
    else:
        st.info("Chưa có notebook executed trong `outputs/reports/`.")


def main() -> None:
    st.sidebar.title("Điều hướng")
    st.sidebar.caption("Dashboard này chỉ hiển thị kết quả đã được chạy sẵn.")
    label = st.sidebar.radio("Chọn phần xem", list(PAGE_OPTIONS.keys()))
    page = PAGE_OPTIONS[label]

    st.sidebar.markdown("---")
    st.sidebar.write(f"Xuất cập nhật: `{latest_output_time()}`")
    st.sidebar.write(f"Số log JSON: `{len(list(LOGS_DIR.glob('run_*.json')))}`")

    if page == "overview":
        render_overview()
    elif page == "association":
        render_association()
    elif page == "clustering":
        render_clustering()
    elif page == "classification":
        render_classification()
    elif page == "forecasting":
        render_forecasting()
    elif page == "experiments":
        render_experiments()
    else:
        render_logs()


if __name__ == "__main__":
    main()
