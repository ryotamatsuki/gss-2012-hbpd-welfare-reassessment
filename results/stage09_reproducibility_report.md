# Stage 9 — Repository / Reproducibility Setup

**Verdict:** GO / CLOSED  
**Theory input:** Stage-8 freeze commit b5bb95f083d4c855647314f90ba735eabf2476d3  
**Production branch:** research/stage-09-reproducibility  
**Reproducibility code head certified by CI:** ff695a6722bc7e17c7b8325db4eb947198a0e5ca  
**Theory change:** NONE.

## 1. Objective

Make the Stage-8 frozen theory reproducible from a fresh checkout without changing the mathematical object.

## 2. Environment pins

### Python

- CPython 3.12 in CI; certified run resolved 3.12.14.
- SymPy 1.14.0 pinned in requirements.txt.
- exact arithmetic uses Python standard-library fractions.Fraction.

### Formal verification

- Lean 4.19.0.
- mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b.

### LaTeX

The Stage-9 build scaffold compiles with pdfLaTeX from standard TeX Live packages installed by CI.

## 3. Reproducibility orchestration

Added:

- Makefile
- requirements.txt
- pyproject.toml
- docs/REPRODUCIBILITY.md
- .github/workflows/reproducibility.yml

Primary targets:

- make python-checks
- make generate
- make verify-generated
- make lean
- make manuscript
- make all

## 4. Mathematical regression layers

### Exact primitive / adversarial layer

code/uniform_game_cleanroom.py

Certified output: all exact clean-room checks passed.

This covers primitive clipping, price-regime boundaries, exact Eq. (12) counterexample, x_H sides/equality, best-response attacks, Eq. (15) regressions, welfare identities, and strong-HBP selection regressions.

### Symbolic primitive layer

code/symbolic_reconstruction.py

Certified output: all symbolic primitive welfare identities passed.

### Stage-7 downstream symbolic layer

code/downstream_impact_symbolic.py

Certified output: all Stage-7 symbolic impact identities passed.

Stage 9 exposed a SymPy representation-sensitivity bug in the prior auxiliary script: algebraically identical expressions were compared using structural equality. The script was repaired to assert that the symbolic difference simplifies/factors to exactly zero. Frozen formulas and expected values were unchanged.

### Compact unittest layer

tests/test_frozen_regressions.py

CI result: 4 tests run; all pass.

## 5. Deterministic generated artifacts

Generator: code/generate_stage09_artifacts.py  
Verifier: code/verify_generated_artifacts.py

Committed outputs:

- generated/parameter_domains.csv
- generated/frozen_regressions.csv
- generated/figure_parameter_domains.svg
- generated/figure_uniform_demand_regimes.svg
- generated/manifest.json

The verifier regenerates into a clean temporary directory and compares every committed artifact byte-for-byte.

Certified output: generated artifacts reproduce byte-for-byte.

Stage 9 also exposed one rendering-only portability issue: Python and JavaScript-style two-decimal rounding can diverge at floating tie boundaries. The SVG generator now uses an explicit deterministic positive-coordinate half-up rule. No theory/data value changed.

## 6. Source / provenance reproducibility

Added sources/SOURCE_MANIFEST.md.

The repository stores provenance and equation/result mappings, not copyrighted source PDFs.

CI includes a source redistribution audit that fails if a PDF is committed under sources/.

Certified result: PASS.

## 7. Theorem-certificate routing

Added theorem_certificates/INDEX.md linking downstream work to the canonical Stage-4A, Stage-7, Stage-7.5A, formal-verification, and Stage-8 freeze artifacts.

No duplicate theorem source of truth was created.

## 8. Formal verification fresh-clone regression

Existing .github/workflows/lean-formal.yml was rerun on the Stage-9 PR head.

GitHub Actions:

- run: 35820175432
- job: 107050137903
- conclusion: SUCCESS

The run confirms:

- exact mathlib revision checkout;
- placeholder/project-axiom audit PASS;
- all ten formal targets build;
- #print axioms reports only propext, Classical.choice, and Quot.sound;
- Build completed successfully.

Formal coverage remains **PROOF-CRITICAL CORE**, exactly as frozen at Stage 8.

## 9. Python / generated-artifact fresh-clone regression

GitHub Actions Stage-9 reproducibility run:

- run: 35820175443
- Python job: 107050137762
- conclusion: SUCCESS

Observed outputs:

- exact clean-room checks PASS;
- symbolic primitive welfare identities PASS;
- Stage-7 symbolic identities PASS;
- 4 unittests PASS;
- generated artifacts reproduce byte-for-byte;
- source redistribution audit PASS.

## 10. LaTeX build

A non-substantive Stage-9 production scaffold was added:

- manuscript/main.tex
- manuscript/sections/00_reproducibility_scaffold.tex

This is build infrastructure, not Stage-10 paper drafting.

CI:

- run: 35820175443
- LaTeX job: 107050138087
- conclusion: SUCCESS
- output: build/manuscript/main.pdf
- observed size: 121253 bytes, one page.

## 11. CI failure/recovery ledger

Two failures were found and repaired during Stage 9:

1. **SymPy structural equality:** mathematically identical expressions had different internal forms under SymPy 1.14.0. Repair: compare the symbolic difference to zero. Theory unchanged.
2. **SVG decimal rounding:** one diagnostic SVG differed byte-for-byte across generation paths. Repair: explicit deterministic rounding rule. Underlying frozen parameter data unchanged.

Neither event is a Stage-8 theory regression.

## 12. Fresh-clone coverage

| Requirement | State |
|---|---|
| deterministic Python exact checks | PASS |
| independent primitive demand/payoff evaluator | PASS |
| symbolic verification | PASS |
| permanent counterexample regressions | PASS |
| parameter/boundary regressions | PASS |
| generated table/data regeneration | PASS |
| generated diagnostic figure regeneration | PASS |
| byte-for-byte generated artifact check | PASS |
| source provenance manifest | PASS |
| source PDF redistribution guard | PASS |
| Lean project / pinned mathlib | PASS |
| formal placeholder/axiom audit | PASS |
| LaTeX build infrastructure | PASS |
| theorem certificate index | PASS |
| CI from clean checkout | PASS |

## 13. Stage-9 gate

**GO / CLOSED.**

The repository is reproducible at the frozen-theory level. No mathematical result was changed.

## 14. Next-stage contract

Proceed to **Stage 10 — Section-by-Section Paper Construction**.

Stage 10 may construct manuscript sections in dependency order, design the final Figure/Table Architecture, reformat Stage-9 diagnostic figures using frozen data, and add bibliography/exposition.

Stage 10 may not alter the Stage-8 theorem set or scope without invoking docs/THEORY_CHANGE_CONTROL.md.
