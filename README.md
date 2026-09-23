# Gehrig–Shy–Stenbacka (2012) HBP Welfare Reassessment

## Target paper

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI `10.1007/s10842-011-0111-8`.

## Project purpose

Reconstruct the global uniform-price game, characterize its pure-strategy equilibrium correspondence, and recompute consumer-surplus and welfare comparisons only on certified equilibrium domains.

## Current status

**Stage 8 is CLOSED/GO — CANONICAL THEORY FROZEN.** Stages 1–4, 4A, 6, 7, 7.5, 7.5A, and 8 have passed; the next canonical gate is Stage 9 — Repository / Reproducibility Setup. A lawful post-referee accepted manuscript is the controlling equation-level source. Exact Springer VOR equation text remains unavailable, so source-facing discrepancy claims remain accepted-manuscript-qualified.

No publication-facing VOR correction theorem is frozen. The historical audit in `ryotamatsuki/ozshypapers` is treated only as a hypothesis and regression source; the derivations in this repository are independent.

## Certified pure-strategy equilibrium result

The clean-room derivation and independent Stage-4A audit certify the pure-equilibrium boundary

\[
x_0\ge x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6,
\qquad s=\sigma/\tau\in(0,1).
\]

The accepted-manuscript source profile is the unique pure equilibrium on and above this boundary; below it there is no pure-strategy equilibrium. Mixed equilibrium is not characterized, so no claim of general equilibrium nonexistence is made.

The upstream negative consumer-surplus regression at (s=0.99,x_0=0.501) fails direct primitive reproduction because it uses the one-way-switch formula outside its domain. Direct integration gives positive CS gaps throughout the weak-HBP profile domain; the printed Result 2 sign reversal does not survive. An analogous strong-HBP branch error affects Result 4 outside the uniform pure-equilibrium region. See `derivations/consumer_surplus_primitive_reconstruction.md` and `derivations/welfare_and_result_impact.md`.

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
* `derivations/uniform_price_game_full_demand.md` — full clipped demand and certified pure-theorem derivation.
* `derivations/uniform_price_global_best_responses.md` — global piecewise best-response proof.
* `derivations/consumer_surplus_primitive_reconstruction.md` — direct CS integrals and branch formulas.
* `derivations/welfare_and_result_impact.md` — primitive welfare branches; accepted-manuscript Results 1–7 are canonically mapped in `results/stage07_downstream_impact.md`.
* `code/uniform_game_cleanroom.py` — exact-rational clean-room regressions and primitive evaluators.
* `code/symbolic_reconstruction.py` — SymPy integration and welfare identity checks.
* `results/stage04_global_uniform_game_progress.md` — Stage 4 GO/CLOSED record.
* `results/stage04a_independent_certificate.md` — closed independent adversarial certificate.
* `results/stage04a_formal_verification_target_map.md` — mandatory Stage-7.5A Lean handoff map.
* `results/mixed_equilibrium_scope_decision.md` — frozen Route-B scope decision.

The canonical stage route and completion status are tracked in `PROJECT_STATUS.md`.


## Stage 7.5A closure

The final contribution is certified as **MODEL-SPECIFIC** rather than generic. Lean 4.19.0 with mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` formally verifies the selected proof-critical algebraic/inequality core. The full continuum demand/Nash model remains analytically certified rather than fully encoded in Lean.


## Stage 8 freeze

The canonical theorem set, accepted-manuscript Results 1–7 impact, mixed-strategy exclusion, strong-HBP selection condition, MODEL-SPECIFIC contribution classification, formal-verification scope, benchmark definitions, and permanent counterexample regressions are frozen in `results/stage08_canonical_theory_freeze.md`. Post-freeze substantive changes are governed by `docs/THEORY_CHANGE_CONTROL.md`.
