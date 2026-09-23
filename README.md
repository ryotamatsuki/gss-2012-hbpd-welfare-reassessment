# Gehrig–Shy–Stenbacka (2012) HBP Welfare Reassessment

## Target paper

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI `10.1007/s10842-011-0111-8`.

## Project purpose

Reconstruct the global uniform-price game, characterize its pure-strategy equilibrium correspondence, and recompute consumer-surplus and welfare comparisons only on certified equilibrium domains.

## Current status

**Stage 14 is CLOSED with CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.** Stages 1–14 of the research/manuscript pipeline have been completed through local submission QA. The sole remaining pre-submission dependency is reconciliation against the authenticated Information Economics and Policy Editorial Manager record and its generated review PDF. A lawful post-referee accepted manuscript is the controlling equation-level source. Exact Springer VOR equation text remains unavailable, so source-facing discrepancy claims remain accepted-manuscript-qualified.

No publication-facing VOR correction theorem is frozen. The historical audit in `ryotamatsuki/ozshypapers` is treated only as a hypothesis and regression source; the derivations in this repository are independent.

## Certified pure-strategy equilibrium result

The clean-room derivation and independent Stage-4A audit certify the pure-equilibrium boundary

\[
x_0\ge x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6,
\qquad s=\sigma/\tau\in(0,1).
\]

The accepted-manuscript source profile is the unique pure equilibrium on and above this boundary; below it there is no pure-strategy equilibrium. Mixed equilibrium is not characterized, so no claim of general equilibrium nonexistence is made.

The upstream negative consumer-surplus regression at (s=0.99,x_0=0.501) fails direct primitive reproduction because it uses the one-way-switch formula outside its domain. Image-level reinspection confirms that accepted Eq. (15) itself is correct on its switching branch; the source sign inconsistency occurs in Eq. (16). Direct integration gives positive CS gaps throughout the weak-HBP profile domain. Result 4 is also branch-specific outside the pure overlap; on the corrected weak pure-equilibrium overlap the smaller firm loses from HBP. See `derivations/consumer_surplus_primitive_reconstruction.md` and `derivations/welfare_and_result_impact.md`.

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


## Stage 9 reproducibility

The frozen theory now reproduces from clean CI checkout with Python 3.12/SymPy 1.14.0 exact and symbolic checks, permanent unittests, deterministic CSV/SVG regeneration, source-PDF guard, Lean 4.19.0/mathlib pinned build, and a pdfLaTeX manuscript scaffold. See `results/stage09_reproducibility_report.md` and `docs/REPRODUCIBILITY.md`.


## Stage 10 manuscript construction

A complete publication-facing manuscript now builds reproducibly from `manuscript/main.tex`. It contains the complete pure-equilibrium theorem, exact counterexample, corrected consumer-surplus and profit comparisons, welfare results, accepted Results 1–7 impact table, explicit strategy/selection/formal-verification scope, related literature, discussion, conclusion, and three appendices. The final repaired IEP-integrated CI build is 22 pages. The independent audit invoked Stage-8 change control for downstream/source-scope repairs; the central `x_H(s)` theorem was unchanged and the repaired theory is refrozen.


## Stage 11–14 completion

A later independent submission audit superseded the initial Stage-11 pass and identified B1–B7, including source-fidelity, profit-branch, endpoint/proof, and formal-CI defects. Change control was invoked, the affected stages were repaired/re-certified, and the Umezawa corrigendum/non-absorption discussion was integrated. Stage 12 continues to select **Information Economics and Policy** as the primary target; Stage 13 is re-certified with synchronized manuscript, title page, one-page cover letter, highlights, and declarations.

On repaired content head `5908ae87ee6f00691ec304ccee134d708afc4a7e`, Stage 14 passed clean-package extraction/rebuild, full manuscript/title/cover compilation, the repaired exact/symbolic/7-test/generated-artifact suite, Lean regression, embedded-font checks, 22-page visual inspection, figure/table artwork QA, and final checksum/provenance recording.

The canonical Stage-14 state is **CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED** because the live IEP Guide body is not retrievable in the automated environment and current portal-only fields/file designations must be checked in the authenticated Editorial Manager record before any submit action.

No Stage 15 freeze or actual submission has occurred. See `results/stage14_submission_qa.md`, `results/stage14_visual_qa.md`, `results/stage14_closure.md`, and `submission/journal_requirements_ledger.md`.
