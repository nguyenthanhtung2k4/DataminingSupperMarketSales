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
    "classification": "f1_macro",
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


def _safe_float(value: Any, default: float | None) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if math.isnan(number):
        return default
    return number


def rank_metrics_for_task(task: str, metrics: dict[str, Any]) -> tuple[float, ...]:
    if task == "association":
        return (
            _safe_float(metrics.get("avg_lift_top5"), float("-inf")) or float("-inf"),
            _safe_float(metrics.get("rule_count"), float("-inf")) or float("-inf"),
            _safe_float(metrics.get("max_lift"), float("-inf")) or float("-inf"),
        )
    if task == "clustering":
        accepted = 1.0 if metrics.get("accepted_for_report", True) else 0.0
        return (
            accepted,
            _safe_float(metrics.get("silhouette"), float("-inf")) or float("-inf"),
            -(_safe_float(metrics.get("davies_bouldin"), float("inf")) or float("inf")),
            -(_safe_float(metrics.get("noise_share"), 0.0) or 0.0),
        )
    if task == "classification":
        return (
            _safe_float(metrics.get("f1_macro"), float("-inf")) or float("-inf"),
            _safe_float(metrics.get("roc_auc_ovr"), float("-inf")) or float("-inf"),
            _safe_float(metrics.get("accuracy"), float("-inf")) or float("-inf"),
        )
    if task == "forecasting":
        return (
            -(_safe_float(metrics.get("sMAPE"), float("inf")) or float("inf")),
            -(_safe_float(metrics.get("RMSE"), float("inf")) or float("inf")),
            -(_safe_float(metrics.get("MAE"), float("inf")) or float("inf")),
        )
    return tuple()


def _row_rank(task: str, row: dict[str, str]) -> tuple[float, ...]:
    metrics = json.loads(row["metrics_json"])
    return rank_metrics_for_task(task, metrics)


def write_dataframe(df: pd.DataFrame, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def _next_result_index(results_log_path: Path) -> int:
    if not results_log_path.exists():
        return 1
    text = results_log_path.read_text(encoding="utf-8")
    return text.count("## Kết quả") + 1


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
        return "chưa có mốc so sánh"
    return (
        "tốt hơn"
        if rank_metrics_for_task(task, current_metrics) > rank_metrics_for_task(task, previous_metrics)
        else "chưa tốt hơn"
    )


def _resolve_primary_metric(task: str, metrics: dict[str, Any]) -> tuple[str | None, float | None]:
    metric_name = TASK_PRIMARY_METRICS.get(task)
    if not metric_name or metric_name not in metrics:
        return None, None
    return metric_name, _safe_float(metrics.get(metric_name), None)


def _append_results_log(entry: dict[str, Any], results_log_path: Path) -> None:
    result_index = _next_result_index(results_log_path)
    header = "# RESULTS LOG\n\nFile này ghi lịch sử chạy để phục vụ viết báo cáo.\n"
    block = [
        f"## Kết quả {result_index:02d}",
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
    if not results_log_path.exists():
        results_log_path.write_text(header + "\n".join(block), encoding="utf-8")
        return
    with results_log_path.open("a", encoding="utf-8") as file:
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
        summary_path.write_text("# Best Runs Summary\n\nChưa có dữ liệu run để tổng hợp.\n", encoding="utf-8")
        return summary_path

    lines = ["# Best Runs Summary", ""]
    for task in ["association", "clustering", "classification", "forecasting"]:
        task_rows = _latest_task_rows(task, rows)
        best_row = _best_registry_row(task, rows, latest_only=True)
        if not best_row:
            continue
        metrics = json.loads(best_row["metrics_json"])
        metric_name, metric_value = _resolve_primary_metric(task, metrics)
        if not metric_name:
            continue
        ranked_rows = sorted(task_rows, key=lambda row: _row_rank(task, row), reverse=True)
        conclusion = "chưa có đối chứng"
        if len(ranked_rows) > 1 and _row_rank(task, ranked_rows[0]) > _row_rank(task, ranked_rows[1]):
            conclusion = "tốt hơn các run cùng phiên bản dữ liệu"
        lines.extend(
            [
                f"## {task}",
                f"- run_id: `{best_row['run_id']}`",
                f"- run_time: `{best_row['run_time']}`",
                f"- metric_chinh: `{metric_name}` = `{metric_value}`",
                f"- conclusion: **{conclusion}**",
                "",
            ]
        )

    summary_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return summary_path


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
