# Gehrig–Shy–Stenbacka (2012) HBP Welfare Reassessment

## Target paper

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination.”

## Project purpose

Reconstruct the full piecewise uniform-price game, characterize the global pure-strategy equilibrium correspondence, and recompute consumer-surplus and welfare comparisons under corrected equilibria.

## Current status

**Stage 0 — Evidence Freeze / independent re-verification.**

No publication-facing correction theorem is frozen yet. The master audit findings are transferred only as hypotheses/evidence to be independently reconstructed in this repository.

## Starting evidence

- Master audit provenance: `ryotamatsuki/ozshypapers — audits/welfare_history_based_price_discrimination_2012_final.md`
- Source status: Complete author-working-paper lineage inspected; VOR body still requires direct equation-level verification.
- Initial signal: The transferred audit found a profitable regime-crossing deviation from the published uniform-price profile and a separate sign/formula error in the consumer-surplus comparison.

## Repository policy

1. Re-derive all publication-facing claims from the original model rather than copying the master-audit conclusion.
2. Separate source transcription, derivation, counterexample, corrected theorem, and downstream implications.
3. Treat local FOCs as insufficient when regime changes, clipping, entry/exit, or boundary actions are feasible.
4. Preserve exact equality and boundary cases in the equilibrium correspondence.
5. Numerical and symbolic checks support but do not replace analytical proof.
6. Do not draft a submission claim until the Version-of-Record lineage and prior-disclosure search are frozen.
7. Keep the master audit repository as provenance; this repository becomes canonical only for publication-facing development after Stage 0 passes.

## Planned structure

```text
README.md
PROJECT_STATUS.md
PROVENANCE.md
CLAIM_BOUNDARY.md
EVIDENCE_MAP.md
docs/
  STAGE_00_EVIDENCE_FREEZE.md
derivations/
code/
results/
sources/
manuscript/
submission/
```

## Immediate next step

Complete `docs/STAGE_00_EVIDENCE_FREEZE.md`: freeze the exact source/version, independently reproduce the transferred discrepancy, run a fresh prior-disclosure search, and decide whether the project passes into theorem/proposition development.

