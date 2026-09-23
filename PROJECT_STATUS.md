# Project Status

## Target

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI `10.1007/s10842-011-0111-8`.

## Current canonical stage

**Stage 0 — Evidence Freeze: HOLD.** Provisional Stage 4 derivations are exploratory work only; they do not bypass the source and novelty gates.

## Current research branch

`research/stage-04-uniform-price-game` (to be branched from `research/stage-00-evidence-freeze` at input commit `7c10043ad91f67505c68bf0f99f3b51263a041fb`). Main is unchanged.

## Gate state

| Gate | Status | Notes |
|---|---|---|
| Stage 0 evidence freeze | HOLD | HECER 2010 full text inspected; VOR body unresolved; prior-disclosure search preliminary. |
| Stage 1 source audit | IN PROGRESS | Bibliographic identity and HECER source version mapped; complete VOR comparison and full claim ledger remain. |
| Stage 2 literature / novelty kill | IN PROGRESS | No correction surfaced in preliminary exact-title searches; no clearance claim. |
| Stage 4 global uniform-price game | EXPLORATORY | Full clipped demand and candidate pure correspondence derived; not yet closed. |
| Stage 4A independent certification | NOT STARTED | Separate branch-exhaustiveness proof / hostile review still required. |
| Eq. (15) primitive CS audit | PROVISIONAL PASS | Direct formulas and exact regressions pass; branch extension in upstream audit rejected. VOR not compared. |
| Formal verification | OPEN | Applicable; no Lean/Lake executable available in current environment. |
| Mixed equilibrium | OUT OF SCOPE (PROVISIONAL) | No claim of general equilibrium nonexistence; no welfare extrapolation into pure-nonexistence domain. |
| Manuscript / journal / Stage 14 | NOT STARTED | No submission package or submission actions. |
| Stage 15 / actual submission | PROHIBITED | Do not submit, freeze, pay, or perform legal finalization. |

## Current mathematical candidate

For (s=\sigma/\tau\in(0,1)), the provisional nonnegative-margin pure equilibrium is the source profile ((a^*,b^*)=(1+s/3,1-s/3)) iff

\[
x_0\ge x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

Below that boundary, the provisional result is no pure-strategy price equilibrium. The equilibrium set is a singleton at the equality boundary even though B has a second best response there. This has not passed Stage 4A and must not be described as certified or as general Nash nonexistence.

## Immediate blockers

1. VOR/accepted-manuscript equation-level comparison.
2. Prior correction and theorem-absorption search closure.
3. Independent proof of complete pure correspondence and strategy-domain reduction.
4. Formal verification core and environment/toolchain certificate.
5. Stage 7 Results 1–5 welfare audit and later canonical gates.

See `docs/STAGE_00_EVIDENCE_FREEZE.md`, `docs/WORKFLOW.md`, and `results/stage04_global_uniform_game_progress.md` for current evidence and boundaries.
