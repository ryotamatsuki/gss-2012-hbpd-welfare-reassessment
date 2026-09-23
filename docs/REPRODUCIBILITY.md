# Reproducibility Guide

## Frozen theory

Stage 8 is the theory source of truth. Stage 9 adds infrastructure only.

## Required environments

### Python

- Python 3.12
- SymPy 1.14.0

Install with: python -m pip install -r requirements.txt

### Lean

- Lean 4.19.0
- mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b

See formal/README.md.

### LaTeX

A standard pdfLaTeX installation is sufficient for the Stage-9 build scaffold.

## One-command targets

- make python-checks
- make generate
- make verify-generated
- make lean
- make manuscript

make all runs all targets when Python, Lean, and pdfLaTeX are installed.

## Python verification layers

1. code/uniform_game_cleanroom.py — direct primitive threshold/clipping evaluator, exact rational global best responses, permanent regressions.
2. code/symbolic_reconstruction.py — independent SymPy primitive integration and welfare identities.
3. code/downstream_impact_symbolic.py — Stage-7 exact endpoint/factor identities.
4. tests/test_frozen_regressions.py — compact unittest regression layer.
5. code/generate_stage09_artifacts.py — deterministic CSV/SVG generation.
6. code/verify_generated_artifacts.py — fresh regeneration and byte-for-byte comparison.

## Generated artifacts

Committed under generated/:

- parameter_domains.csv
- frozen_regressions.csv
- figure_parameter_domains.svg
- figure_uniform_demand_regimes.svg
- manifest.json

These are Stage-9 reproducibility/diagnostic outputs. Stage 10 may alter publication formatting, but the frozen formulas/data may not change without theory-change control.

## CI

.github/workflows/reproducibility.yml runs from a clean checkout and verifies:

- Python 3.12;
- pinned SymPy installation;
- exact clean-room regressions;
- symbolic identities;
- unittest regressions;
- deterministic generated artifacts;
- absence of committed source PDFs;
- pdfLaTeX build scaffold.

Lean CI remains separately enforced by .github/workflows/lean-formal.yml.

## Failure policy

A failed exact/symbolic/formal regression is a potential theory regression and must not be patched by updating expected values. Consult docs/THEORY_CHANGE_CONTROL.md and reopen the earliest affected stage if the frozen mathematics changed.
