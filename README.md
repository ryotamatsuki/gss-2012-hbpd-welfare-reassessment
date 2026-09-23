# Gehrig–Shy–Stenbacka (2012) HBP Welfare Reassessment

## Target paper

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI `10.1007/s10842-011-0111-8`.

## Project purpose

Reconstruct the global uniform-price game, characterize its pure-strategy equilibrium correspondence, and recompute consumer-surplus and welfare comparisons only on certified equilibrium domains.

## Current status

**Canonical Stage 0 — HOLD.** The complete HECER 2010 author version is directly available and equation-level work is underway. The full Version of Record body has not been compared, and the prior-disclosure search is preliminary. Provisional Stage 4 mathematics is explicitly exploratory and does not bypass Stages 1–3.

No publication-facing VOR correction theorem is frozen. The historical audit in `ryotamatsuki/ozshypapers` is treated only as a hypothesis and regression source; the derivations in this repository are independent.

## Current mathematical lead (not yet certified)

The clean-room full-demand derivation yields the provisional pure-equilibrium boundary

\[
x_0\ge x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6,
\qquad s=\sigma/\tau\in(0,1).
\]

The candidate source profile is a pure equilibrium above this boundary, including equality; below it the current candidate result is no pure-strategy equilibrium. This remains subject to independent Stage 4A certification. Mixed equilibrium is not characterized, so no claim of general equilibrium nonexistence is made.

The upstream negative consumer-surplus regression at (s=0.99,x_0=0.501) fails direct primitive reproduction because it uses the one-way-switch formula outside its domain. The HECER Eq. (15) display is nevertheless false on a valid switching branch. See `derivations/consumer_surplus_primitive_reconstruction.md`.

## Repository policy

1. Re-derive publication-facing claims from primitive utilities and source text.
2. Separate source transcription, derivation, counterexample, theorem, and downstream implications.
3. Treat local FOCs as insufficient when clipping, regime changes, or boundary actions are feasible.
4. Preserve exact equality and boundary cases.
5. Treat symbolic and numerical checks as supporting evidence, not as global proofs.
6. Keep the VOR and prepublication source claims version-qualified until compared.
7. Do not extrapolate pure-equilibrium welfare into a pure-nonexistence region.
8. Do not submit, perform Stage 15, merge into `main`, or alter the separate 2011 project.

## Current artifacts

* `docs/WORKFLOW.md` — canonical v2.4 workflow mapping.
* `docs/STAGE_00_EVIDENCE_FREEZE.md` — current Stage 0 gate and source boundary.
* `sources/gss_2012_version_boundary.md` — source lineage and version limitations.
* `derivations/uniform_price_game_full_demand.md` — full clipped demand and provisional pure theorem.
* `derivations/consumer_surplus_primitive_reconstruction.md` — direct CS integrals and branch formulas.
* `code/uniform_game_cleanroom.py` — exact-rational clean-room regressions and primitive evaluators.
* `results/stage04_global_uniform_game_progress.md` — work completed, checks, and open gates.

The canonical stage route and completion status are tracked in `PROJECT_STATUS.md`.
