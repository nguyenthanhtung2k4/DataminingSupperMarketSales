from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import papermill as pm

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import ensure_output_directories, load_params
from src.data import load_raw_data


NOTEBOOKS = [
    "01_eda.ipynb",
    "02_preprocess_feature.ipynb",
    "03_mining.ipynb",
    "04_modeling_forecasting.ipynb",
    "05_evaluation_report.ipynb",
]


def main() -> None:
    config = load_params()
    ensure_output_directories(config, PROJECT_ROOT)
    load_raw_data(config, PROJECT_ROOT)
    subprocess.run([sys.executable, str(PROJECT_ROOT / "scripts" / "run_pipeline.py")], check=True)

    notebooks_dir = PROJECT_ROOT / "notebooks"
    reports_dir = PROJECT_ROOT / "outputs" / "reports"

    for old_executed in reports_dir.glob("executed_*.ipynb"):
        old_executed.unlink()

    for notebook_name in NOTEBOOKS:
        input_path = notebooks_dir / notebook_name
        temp_path = notebooks_dir / f".papermill_tmp_{notebook_name}"
        pm.execute_notebook(str(input_path), str(temp_path), cwd=str(PROJECT_ROOT))
        temp_path.replace(input_path)
        print(f"Executed {notebook_name} -> {input_path}")


if __name__ == "__main__":
    main()
