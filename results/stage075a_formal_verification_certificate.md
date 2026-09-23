# Stage 7.5A — Formal Verification Certificate

**Final state:** FORMAL VERIFICATION PASS  
**Project:** GSS (2012) HBP Welfare Reassessment  
**Formal source commit:** \`7c48c20b8b15a6198cbdf0e780ec3e7dcb221401\`  
**CI run:** GitHub Actions run \`35817736362\`  
**CI job:** \`107042790562\`  
**Build result:** SUCCESS

## 1. Toolchain and dependency provenance

- Lean: **4.19.0**
- lean-toolchain: \`leanprover/lean4:v4.19.0\`
- mathlib revision: **\`c44e0c8ee63ca166450922a373c7409c5d26b00b\`**
- runner: Ubuntu 24.04 GitHub-hosted runner
- build commands:
  - \`lake update\`
  - \`lake exe cache get\`
  - \`lake build\`

The exact mathlib commit is pinned in \`formal/lakefile.lean\`.

## 2. Formal source

- \`formal/Gss2012/Core.lean\`
- \`formal/Gss2012.lean\`
- \`formal/lakefile.lean\`
- \`formal/lean-toolchain\`
- \`formal/README.md\`
- CI: \`.github/workflows/lean-formal.yml\`

## 3. Paper-claim to formal-theorem map

| Claim/component | Lean theorem | Certified component |
|---|---|---|
| UPE-2012-1B | \`GSS2012.payoff_factorization\` | exact source-vs-kink B-payoff factorization \(2(x-x_L)(x-x_H)\) |
| UPE-2012-1A | \`GSS2012.xU_lt_xH\` | \(x_u<x_H\) for \(0<s<1\) |
| UPE-2012-1A | \`GSS2012.xH_lt_one\` | \(x_H<1\) for \(0\le s<1\) |
| UPE-2012-1C | \`GSS2012.exact_counterexample_gain\` | exact \(719/1800>0\) counterexample gain |
| UPE-2012-1D | \`GSS2012.equality_kink_A_gain\` | strict positive A gain \(2sx>0\) at the equality-kink deviation calculation |
| CS-2012-1 | \`GSS2012.eq15_valid_branch_exact\` | exact corrected-vs-printed Eq. (15) discrepancy on a valid one-way-switch point |
| CS-2012-2 | \`GSS2012.rejected_upstream_cs_regression\` | branch-correct positive exact value \(17993/4500000\) at the rejected upstream regression point |
| W-2012-1 | \`GSS2012.weak_welfare_endpoint_identity\` | exact weak-welfare endpoint identity |
| UPE-2012-OVERLAP | \`GSS2012.overlap_equality_implies_polynomial\` | \(x_H=\bar x\) implies \(11s^2+66s-9=0\) |
| UPE-2012-OVERLAP | \`GSS2012.overlap_closed_form_root\` | the Stage-7 closed form \(s_c=-3+6\sqrt{33}/11\) solves the overlap polynomial |

## 4. Statement-fidelity audit

The Lean artifact certifies the algebraic/inequality core **conditional on the definitions encoded in the formal file**.

It does not encode or certify from primitives:

- the continuum consumer population;
- the complete clipped demand correspondence;
- the economic derivation of the five price-difference regimes;
- the full price strategy space;
- the Nash equilibrium definition or complete best-response correspondence;
- the proof that no other pure equilibrium branch exists;
- mixed-strategy equilibrium;
- source/VOR provenance.

Those objects are certified analytically and independently at Stages 4 and 4A.

Therefore the licensed manuscript wording is:

> Selected proof-critical algebra and inequality results underlying the pure-equilibrium characterization were independently checked in Lean 4/mathlib.

Prohibited wording:

> The complete economic model / Nash equilibrium theorem was formally proved in Lean.

unless those omitted economic objects are later formalized.

## 5. Assumptions supplied versus proved

The formal file defines \(x_H,x_L,x_u,\bar x\), payoff expressions, and the relevant CS/welfare expressions. It proves algebraic identities and inequalities from explicit real-number hypotheses such as \(s\ge0\), \(s>0\), and \(s<1\).

The file does **not** assume the final Nash conclusion as an axiom or definition.

## 6. Placeholder / axiom audit

CI explicitly scans project Lean source for:

- \`sorry\`;
- \`admit\`;
- explicit project \`axiom\` declarations.

Result: **none found**.

Each certified theorem was also queried with \`#print axioms\`. The reported dependencies are only:

- \`propext\`;
- \`Classical.choice\`;
- \`Quot.sound\`.

No project-specific axiom appears.

## 7. Build evidence

GitHub Actions run \`35817736362\` completed successfully.

All required steps passed:

1. checkout;
2. elan install;
3. exact pinned dependency resolution;
4. mathlib cache retrieval;
5. placeholder/project-axiom audit;
6. \`lake build\`.

The build log records:

- Lean 4.19.0 download;
- mathlib checkout at \`c44e0c8ee63ca166450922a373c7409c5d26b00b\`;
- successful construction of \`Gss2012.Core\` and \`Gss2012\`;
- \`Build completed successfully.\`

## 8. Interaction with Stage 4A

This formal PASS does not replace Stage 4A. The independent Stage-4A path reconstructs primitive clipped demand and globally maximizes unilateral deviations without calling the production piecewise formula.

The two layers answer different questions:

- Stage 4A: the economic cases, strategy domain, boundaries, and equilibrium scope are correct;
- Lean: the selected proof-critical algebra follows from its encoded assumptions.

## 9. Rollback rule

The formal certificate becomes stale if any of the following changes materially:

- definition of \(x_H\), source/kink payoff, or equilibrium-domain threshold;
- accepted Eq. (15) correction formula;
- weak-welfare endpoint formula;
- weak/pure overlap boundary;
- theorem quantifiers that change the algebraic domain.

A stale certificate blocks Stage 8 until rebuilt and re-audited.

## 10. Gate result

**FORMAL VERIFICATION PASS.**

The Stage-7.5A Formal Verification Gate is closed.
