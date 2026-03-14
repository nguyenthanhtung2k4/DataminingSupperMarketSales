from __future__ import annotations

import csv
import json
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

TASK_SCORE_RULES = {
    "association": ("max_lift", "max"),
    "clustering": ("silhouette", "max"),
    "forecasting": ("sMAPE", "min"),
}


def _make_json_ready(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _make_json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_make_json_ready(item) for item in value]
    if hasattr(value, "item"):
        return value.item()
    return value


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


def _comparison(metric_name: str, direction: str, current: float, previous: float | None) -> str:
    if previous is None:
        return "chua on"
    if direction == "min":
        return "tot hon" if current < previous else "kem hon"
    return "tot hon" if current > previous else "kem hon"


def _resolve_primary_metric(task: str, metrics: dict[str, Any]) -> tuple[str | None, float | None, str]:
    metric_name, direction = TASK_SCORE_RULES.get(task, (None, "max"))
    if not metric_name or metric_name not in metrics:
        return None, None, direction
    return metric_name, float(metrics[metric_name]), direction


def _previous_best(task: str, metric_name: str, direction: str, registry_path: Path) -> float | None:
    rows = _load_registry_rows(registry_path)
    values: list[float] = []
    for row in rows:
        if row.get("task") != task:
            continue
        metrics = json.loads(row["metrics_json"])
        if metric_name in metrics:
            values.append(float(metrics[metric_name]))
    if not values:
        return None
    return min(values) if direction == "min" else max(values)


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

    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["task"], []).append(row)

    lines = ["# Best Runs Summary", ""]
    for task, task_rows in grouped.items():
        metric_name, _, direction = _resolve_primary_metric(task, json.loads(task_rows[0]["metrics_json"]))
        if not metric_name:
            continue

        def metric_value(row: dict[str, str]) -> float:
            metrics = json.loads(row["metrics_json"])
            return float(metrics[metric_name])

        best_row = min(task_rows, key=metric_value) if direction == "min" else max(task_rows, key=metric_value)
        lines.extend(
            [
                f"## {task}",
                f"- run_id: `{best_row['run_id']}`",
                f"- run_time: `{best_row['run_time']}`",
                f"- metric_chinh: `{metric_name}` = `{metric_value(best_row)}`",
                f"- conclusion: **{best_row['conclusion']}**",
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

    metric_name, metric_value, direction = _resolve_primary_metric(task, metrics)
    previous_best = (
        _previous_best(task, metric_name, direction, registry_path)
        if metric_name and metric_value is not None
        else None
    )
    conclusion = (
        _comparison(metric_name, direction, metric_value, previous_best)
        if metric_name and metric_value is not None
        else "chua on"
    )

    run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_id = f"{task}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    dataset_version = detect_dataset_version(data_path) if data_path else "unknown"

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
