from __future__ import annotations

import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


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
