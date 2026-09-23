# Stage 7.5A — Formal Verification Certificate

**Final state:** FORMAL VERIFICATION PASS — RE-CERTIFIED AFTER SOURCE-FIDELITY REPAIR  
**Project:** GSS (2012) HBP Welfare Reassessment  
**Certified formal source head:** `c53244905973516d097746061f6bc4df4251bec5`  
**CI run:** GitHub Actions run `35855403333`  
**CI job:** `107162564383`  
**Build result:** SUCCESS

## 1. Toolchain and dependency provenance

- Lean: **4.19.0**
- lean-toolchain: `leanprover/lean4:v4.19.0`
- mathlib revision: **`c44e0c8ee63ca166450922a373c7409c5d26b00b`**
- runner: Ubuntu 24.04 GitHub-hosted runner
- build commands:
  - `lake update`
  - `lake exe cache get`
  - `lake build`

The exact mathlib commit remains pinned in `formal/lakefile.lean`.

## 2. Why re-certification was required

The independent submission audit found that the previous formal artifact encoded a locally mis-transcribed object as “printed Eq. (15).” Image-level source reinspection established that accepted Eq. (15) is in fact identical to the primitive one-way-switch CS expression. The source-facing inconsistency is the displayed Eq. (15)→Eq. (16) sign change, while a separate allocation-domain error arises when the one-way-switch formula is extended to (x_0<x_u).

The previous Stage-7.5A certificate was therefore invalidated rather than grandfathered. The repaired Lean definitions and theorem statements were rebuilt from a clean CI checkout.

## 3. Paper-claim to formal-theorem map

| Claim/component | Lean theorem | Certified component |
|---|---|---|
| UPE-2012-1B | `GSS2012.payoff_factorization` | exact source-vs-kink B-payoff factorization (2(x-x_L)(x-x_H)) |
| UPE-2012-1A | `GSS2012.xU_lt_xH` | (x_u<x_H) for (0<s<1) |
| UPE-2012-1A | `GSS2012.xH_lt_one` | (x_H<1) for (0le s<1) |
| UPE-2012-1C | `GSS2012.exact_counterexample_gain` | exact (719/1800>0) counterexample gain |
| UPE-2012-1D | `GSS2012.equality_kink_A_gain` | strict positive A gain (2sx>0) at the equality-kink deviation calculation |
| CS-2012-1A | `GSS2012.eq15_source_fidelity_exact` | primitive one-way-switch gap and accepted Eq. (15) both equal (221/720) at the exact valid point |
| CS-2012-1B | `GSS2012.eq16_is_negative_eq15` | encoded accepted Eq. (16) lhs is the negative of the accepted Eq. (15) normalized expression |
| CS-2012-1B | `GSS2012.eq16_sign_flip_exact` | exact Eq. (16) lhs value (-221/720) at the source-fidelity point |
| CS-2012-2 | `GSS2012.rejected_upstream_cs_regression` | branch-correct no-switch value (17993/4500000>0) at the rejected branch-extension point |
| W-2012-1 | `GSS2012.weak_welfare_endpoint_identity` | exact weak-welfare endpoint identity |
| UPE-2012-OVERLAP | `GSS2012.overlap_equality_implies_polynomial` | (x_H=ar x) implies (11s^2+66s-9=0) |
| UPE-2012-OVERLAP | `GSS2012.overlap_closed_form_root` | (s_c=-3+6sqrt{33}/11) solves the overlap polynomial |

## 4. Statement-fidelity boundary

The Lean artifact certifies the algebraic/inequality core **conditional on the definitions encoded in the formal file**. Source fidelity for Eq. (15) was independently re-established from the accepted-manuscript image before the repaired definition was frozen.

Lean does not encode or certify from primitives:

- the continuum consumer population;
- the complete clipped demand correspondence;
- the economic derivation of the five price-difference regimes;
- the full price strategy space;
- the Nash equilibrium definition or complete best-response correspondence;
- the proof that no other pure equilibrium branch exists;
- the (x_0=1) unused-HBP-price interpretation;
- mixed-strategy equilibrium;
- source/VOR provenance as a document-authentication fact.

Those objects remain analytically certified at Stages 1, 4, 4A, and 7.

Licensed manuscript wording remains:

> Selected proof-critical algebra and inequality results underlying the pure-equilibrium characterization were independently checked in Lean 4/mathlib.

The full economic model is not claimed to be formally proved in Lean.

## 5. Placeholder / project-axiom guard repair

The prior CI grep pattern was over-escaped and did not constitute a reliable fail-closed guard. The repaired workflow now:

1. creates a sentinel Lean file containing `by sorry`;
2. creates a sentinel Lean file containing `axiom bad : False`;
3. requires both sentinels to be detected;
4. scans only project Lean sources `Gss2012/` and `Gss2012.lean`, not downloaded mathlib sources;
5. fails on any project `sorry`, `admit`, or explicit `axiom`.

Run `35855403333` passed the sentinel checks and found no placeholder or project-specific axiom in the project sources.

## 6. Axiom report

Each of the twelve certified theorem targets was queried with `#print axioms`. The CI log reports only:

- `propext`;
- `Classical.choice`;
- `Quot.sound`.

No project-specific axiom appears.

## 7. Build evidence

The repaired run checked out the pinned mathlib revision `c44e0c8ee63ca166450922a373c7409c5d26b00b`, built `Gss2012.Core` and `Gss2012`, printed the axiom dependencies for all twelve selected targets, and ended with:

> Build completed successfully.

## 8. Interaction with Stage 4A

This formal PASS does not replace Stage 4A. The independent Stage-4A path reconstructs primitive clipped demand and globally maximizes unilateral deviations without calling the production piecewise formula.

The two layers remain complementary:

- Stage 4A certifies economic cases, strategy-domain handling, boundaries, and pure-equilibrium scope;
- Lean certifies selected algebraic identities and inequalities from explicit encoded assumptions.

## 9. Rollback rule

This certificate becomes stale if any of the following changes materially:

- definition of (x_H), source/kink payoff, or equilibrium-domain threshold;
- accepted Eq. (15)/(16) source-fidelity definitions;
- branch-correct no-switch CS formula;
- weak-welfare endpoint formula;
- weak/pure overlap boundary;
- formal theorem quantifiers.

## 10. Gate result

**FORMAL VERIFICATION PASS — RE-CERTIFIED.**

The selected formal core is again eligible for the Stage-8 theory freeze. The full-model formalization remains intentionally out of scope.
