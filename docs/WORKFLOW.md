# Canonical research workflow routing

This repository follows `ryotamatsuki/research-paper-workflow` on `main`, pipeline v2.4, checked at commit `63f11a50a13d9328213498a5a6576d00b9bceef7` on 2026-09-23. The canonical pipeline and its checklists control all gates. This file maps the original short correction-reassessment scaffold onto the current canonical stages; the short scaffold does not waive inherited obligations.

| Canonical stage | Application to this project |
|---|---|
| 0 — Idea / Motivation Intake | Define the published-model question and classify correction vs reassessment vs theorem. |
| 1 — Source & Mathematical Audit | Freeze VOR/version lineage, inventory Eqs. (1)–(28), Results 1–5, assumptions, figures, and source-specific claims. |
| 2 — Literature Frontier / Novelty Kill Gate | Search corrections, later literature, and theorem absorption. |
| 3 — Candidate Mechanism Search | Compare minimal correction, pure-equilibrium reassessment, and extended-game routes. |
| 4 — Minimal Model Gate | Rebuild the clipped uniform-price demand game from primitive utilities. |
| 4A — Independent Mathematical Adversarial Certification | Independently certify strategy domains, global deviations, kinks, equality branches, and the pure correspondence. |
| 5 — Mechanism Hardening | Repair a single clearly repairable defect without changing the original model. |
| 6 — Novelty Re-Kill | Test the final theorem against exact and general prior results. |
| 7 — Welfare / Generality / Institutional Validation | Recompute surplus and welfare only on certified equilibrium domains. |
| 7.5 — Full-Theory Freeze Decision | Decide short note vs full reassessment and freeze scope. |
| 7.5A — Generality / Quantifier / Portability Red-Team + Formal Verification Gate | Audit claim scope, portability, theorem quantifiers, and Lean applicability. |
| 8 — Canonical Theory Freeze | Freeze only after source, math, novelty, welfare, and formal gates close. |
| 9 — Repository / Reproducibility Setup | Fresh-clone code, tests, Lean project, CI, figures, and manuscript build. |
| 10 — Section-by-Section Paper Construction | Draft from frozen results. |
| 11 — Robustness / Hostile Referee Attack | Attack theorem completeness, source scope, mixed-equilibrium wording, and welfare claims. |
| 12 — Journal Positioning | Build the venue universe from the surviving contribution. |
| 13 — Full-Paper Integration | Apply current journal requirements without changing theory. |
| 14 — Submission QA | Refresh live requirements and run reproducible package checks; stop before submission. |
| 15 — Submission Freeze | Prohibited in this project run. |

The earlier local scaffold's “Stage 1 — Model Canonicalization” maps primarily to canonical Stage 1, its “Stage 2 — Independent Clean-Room Derivation” maps to Stages 3–4, its “Stage 3 — Boundary and Global-Deviation Audit” maps to Stages 4A–5, its “Stage 4 — Corrected Result Freeze” maps to Stage 8, and its remaining stages map across Stages 7–14. No local short-stage label overrides the canonical v2.4 gate.

## Workflow source discrepancy

The canonical repository's `GOVERNANCE.md` labels v2.3 while its current pipeline/readme and latest main commit identify v2.4. This project follows the v2.4 pipeline and records the governance-file inconsistency rather than silently choosing an older route.

## Current route status

Stage 0 remains on HOLD pending prior-disclosure search closure and a version-qualified publication claim. Exploratory uniform-game work is recorded separately as provisional Stage 4 work and does not constitute a pass through the earlier gates. Stage 14 and Stage 15 have not been reached.
