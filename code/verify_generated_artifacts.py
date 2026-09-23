"""Regenerate Stage-9 outputs and compare them byte-for-byte."""

from __future__ import annotations

import filecmp
import shutil
import subprocess
import sys
from pathlib import Path


EXPECTED = [
    "parameter_domains.csv",
    "frozen_regressions.csv",
    "figure_parameter_domains.svg",
    "figure_uniform_demand_regimes.svg",
    "manifest.json",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    committed = root / "generated"
    temp = root / ".stage09-regenerate"
    if temp.exists():
        shutil.rmtree(temp)
    try:
        subprocess.run(
            [sys.executable, str(root / "code/generate_stage09_artifacts.py"), "--output", str(temp)],
            check=True,
            cwd=root,
        )
        failures = []
        for name in EXPECTED:
            a, b = committed / name, temp / name
            if not a.exists() or not b.exists() or not filecmp.cmp(a, b, shallow=False):
                failures.append(name)
        extra_committed = sorted(p.name for p in committed.iterdir() if p.is_file() and p.name not in EXPECTED)
        extra_temp = sorted(p.name for p in temp.iterdir() if p.is_file() and p.name not in EXPECTED)
        if extra_committed or extra_temp:
            failures.append(f"unexpected files committed={extra_committed} regenerated={extra_temp}")
        if failures:
            raise SystemExit("generated artifact mismatch: " + ", ".join(failures))
        print("generated artifacts reproduce byte-for-byte")
    finally:
        if temp.exists():
            shutil.rmtree(temp)


if __name__ == "__main__":
    main()
