from __future__ import annotations

import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]

TABLE_LAYOUT = {
    "core": [
        "association_rules.csv",
        "classification_class_report.csv",
        "classification_comparison.csv",
        "classification_confusion_matrix.csv",
        "cluster_profile.csv",
        "clustering_comparison.csv",
        "forecast_comparison.csv",
        "forecast_residuals.csv",
    ],
    "diagnostics": [
        "association_itemsets.csv",
        "classification_predictions.csv",
        "cleaning_report.json",
        "cluster_assignments.csv",
        "forecast_predictions.csv",
        "schema_snapshot.csv",
    ],
    "experiments": [
        "experiment_association_report.csv",
        "experiment_classification_report.csv",
        "experiment_clustering_report.csv",
        "experiment_forecasting_report.csv",
    ],
}

RETIRED_TABLE_FILES = [
    "report_association_top.csv",
    "report_classification_best.csv",
    "report_classification_by_class.csv",
    "report_cluster_profile_top.csv",
    "report_clustering_best.csv",
    "report_dataset_summary.csv",
    "report_forecast_best.csv",
    "report_selected_params.csv",
]


def get_project_root() -> Path:
    return PROJECT_ROOT


def load_params(config_path: str | Path | None = None) -> dict[str, Any]:
    path = Path(config_path) if config_path else PROJECT_ROOT / "configs" / "params.yaml"
    return json.loads(path.read_text(encoding="utf-8"))


def save_params(config: dict[str, Any], config_path: str | Path | None = None) -> Path:
    path = Path(config_path) if config_path else PROJECT_ROOT / "configs" / "params.yaml"
    path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def resolve_path(path_value: str | Path, project_root: str | Path | None = None) -> Path:
    base = Path(project_root) if project_root else PROJECT_ROOT
    path = Path(path_value)
    return path if path.is_absolute() else base / path


def ensure_output_directories(config: dict[str, Any], project_root: str | Path | None = None) -> None:
    for key, value in config["paths"].items():
        if key.endswith("_dir"):
            resolve_path(value, project_root).mkdir(parents=True, exist_ok=True)
    tables_root = resolve_path(config["paths"]["tables_dir"], project_root)
    for group in TABLE_LAYOUT:
        (tables_root / group).mkdir(parents=True, exist_ok=True)


def resolve_table_directory(
    config: dict[str, Any],
    group: str,
    project_root: str | Path | None = None,
) -> Path:
    tables_root = resolve_path(config["paths"]["tables_dir"], project_root)
    return tables_root / group


def resolve_table_path(
    config: dict[str, Any],
    group: str,
    filename: str,
    project_root: str | Path | None = None,
) -> Path:
    return resolve_table_directory(config, group, project_root) / filename


def cleanup_legacy_table_files(
    config: dict[str, Any],
    project_root: str | Path | None = None,
) -> list[Path]:
    tables_root = resolve_path(config["paths"]["tables_dir"], project_root)
    removed: list[Path] = []
    for filenames in [*TABLE_LAYOUT.values(), RETIRED_TABLE_FILES]:
        for filename in filenames:
            legacy_path = tables_root / filename
            if legacy_path.exists():
                legacy_path.unlink()
                removed.append(legacy_path)
    retired_report_dir = tables_root / "report"
    if retired_report_dir.exists():
        for path in retired_report_dir.iterdir():
            if path.is_file():
                path.unlink()
                removed.append(path)
        if not any(retired_report_dir.iterdir()):
            retired_report_dir.rmdir()
    return removed


def get_git_commit(project_root: str | Path | None = None) -> str:
    base = Path(project_root) if project_root else PROJECT_ROOT
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=base,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def detect_dataset_version(data_path: str | Path) -> str:
    path = Path(data_path)
    if not path.exists():
        return "missing-dataset"
    stat = path.stat()
    modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    return f"{path.name}|{stat.st_size}B|{modified}"
