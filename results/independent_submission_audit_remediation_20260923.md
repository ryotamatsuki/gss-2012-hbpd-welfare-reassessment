# Independent submission-audit remediation — 2026-09-23

**Audit baseline:** branch `research/stage-14-submission-qa`, commit `038d0c12bb88125418a660a00a1493f08b3ad9c3`  
**Purpose:** close findings B1–B7 from the independent pre-submission audit without changing the validated central (x_H(s)) pure-equilibrium theorem.

## Closure ledger

| Finding | Status | Repair |
|---|---|---|
| B1 source Eq. (15) misattribution | CLOSED | Image-level re-transcription restores Eq. (15); source error moved to Eq. (15)→Eq. (16) sign inversion; branch-extension issue kept separate. |
| B2 Result 4 profit scope | CLOSED | Weak profit comparisons made piecewise in realized uniform demand; exact no-switch witness added to Python/tests/manuscript. |
| B3 highlight/summary overclaim | CLOSED | Smaller-firm loss restricted everywhere to weak pure-equilibrium overlap; strong-domain positive-gap witness retained. |
| B4 (x_0=1) strong-HBP uniqueness | CLOSED | Empty B-history market treated separately; unused prices nonunique, realized outcomes unique; strict CS/share comparisons become equality. |
| B5 Appendix A proof gaps | CLOSED | Joint margin–demand capture exclusion, separate (s=0) and (x_0=1) cases, and reverse-switch monotonicity added. |
| B6 Lean/source fidelity + guard | CLOSED | Stale Eq. (15) target invalidated/replaced; sentinel-based placeholder/axiom guard added; repaired Lean core builds with pinned toolchain. |
| B7 literature/non-absorption | CLOSED | Umezawa corrigendum integrated; nearby models compared by primitives/timing/information; formal non-nesting is not claimed. |

## Re-certification route

The repair reopened and re-certified the affected source/theory/formal/submission layers: Stage 1; Stage 4/4A proof completeness; Stage 7 downstream impact; Stage 7.5A formal verification; Stage 8 theory freeze; Stage 9 reproducibility; Stage 10/11 claim/proof audit; and Stage 13/14 submission synchronization.

The central uniform-price theorem, exact threshold (x_H(s)), equality-case Nash conclusion, and exact (719/1800) counterexample remain unchanged.

Stage 14 may be re-closed only after the repaired head passes the Stage-14 package QA, submission preflight, reproducibility regression, and Lean verification. Stage 15 / actual submission remains outside this repair.
