# Stage 11 — Robustness / Referee Attack Gate

**Verdict:** RE-CERTIFIED GO / CLOSED after independent submission-audit remediation  
**Attack date:** 2026-09-23  
**Input:** Stage-10 full manuscript, Stage-8 frozen theory, and independent submission audit `gss2012_independent_submission_audit_20260923.md`  
**Certification regression:** FOUND AND REPAIRED  
**Theory rollback:** LIMITED rollback/re-certification through Stages 1, 4/4A, 7, 7.5A, and 8; the headline `x_H(s)` pure-equilibrium theorem was unchanged.

## Executive adversarial verdict

The first Stage-11 pass did not detect several submission-blocking defects later found by an independent clean-room audit. The later audit identified one FATAL source-fidelity failure and multiple MAJOR scope/proof/formal-verification issues. Those findings triggered change control rather than being treated as prose-only edits.

The repaired state preserves the central pure-equilibrium threshold theorem but changes downstream certification in five material ways: accepted Eq. (15) is recognized as source-faithful on its switching branch and the source error is relocated to the Eq. (15)→Eq. (16) sign transformation; Result 4 profile profits are evaluated on realized allocation branches; the smaller-firm loss claim is explicitly weak-domain only; `x_0=1` is separated as an empty-history-market endpoint for strong HBP; and the unrestricted-price capture proof plus Lean statement-fidelity/CI guards are repaired. Related-literature positioning was also strengthened with the Umezawa corrigendum and explicit non-nesting caution.

## Mandatory attack matrix

| Attack | Classification | Result |
|---|---|---|
| classic-result / relabeling | PASS | The paper does not claim novelty for kinks, switching-cost nonexistence, or BBPD generally. The source-specific contribution is the exact GSS threshold and downstream correction. |
| known-model-in-disguise / theorem absorption | PASS | Recentered price-difference form is a one-dimensional piecewise game, but no located parent theorem yields the GSS (x_H(s)) condition or Results 1–7 correction as a direct specialization. |
| whole-game novelty redundancy | PASS | Fresh exact-title/correction/threshold searches found no prior correction stating the same source-specific theorem. |
| closest-literature completeness | MINOR → FIXED | Added Umezawa (2022), Shrivastav (2023), and Umezawa–Yamakawa (2025). |
| ad hoc assumptions | PASS | Endpoint Hotelling geometry, full coverage, linear transport, inherited split, common switching cost, and common marginal cost are inherited source primitives, not assumptions added to rescue the correction. |
| alternative demand / information structures | PASS AS SCOPE | The manuscript explicitly classifies the result MODEL-SPECIFIC and does not claim portability to outside options, heterogeneous switching costs, imperfect recognition, or alternative spatial demand. |
| participation / capture / kink / regime switching | PASS | Appendix A and Stage-4A certificate enumerate capture tails, plateau interior, both kinks, both switching branches, zero/negative margins, and equality. |
| welfare mechanicality | PASS | Welfare is separately reconstructed from real transport and switching costs; price-transfer cancellation is explicit. |
| institutional / external-validity inflation | PASS | No empirical, calibrated, causal, or policy-generalization claim is made. |
| numerical-not-proof | PASS | Exact examples and generated figures are supplementary to analytic propositions; no proposition rests on sampling. |
| proof / notation inconsistency | PASS | Main theorem, appendix branch proof, exact counterexample, and scope statements agree with frozen theorem registry. |
| theorem quantifier inflation | PASS | Pure-strategy qualifier and maintained (0le s<1), (x_0>1/2) domain are explicit. |
| portability inflation | PASS | The manuscript repeatedly labels the result model-specific and lists non-tested alternative microfoundations. |
| benchmark terminology drift | PASS | No first-best/planner terminology is used; welfare is (CS+pi_A+pi_B) under full coverage. |
| global-equilibrium overclaim | PASS | Below (x_H), wording is only “no pure-strategy equilibrium”; mixed pricing remains unresolved. |
| formal-verification inflation | PASS | Lean is described as checking selected proof-critical algebra, not the full economic model or Nash definition. |
| stale formal theorem | REPAIRED / PASS | The previous Eq. (15) formal target was invalidated, replaced by source-fidelity Eq. (15)/Eq. (16) targets, and rebuilt under the repaired sentinel guard. |
| source/VOR inflation | PASS | Disputed equations/results are attributed to the accepted manuscript; exact Springer VOR body remains unverified. |
| journal-fit/contribution-level risk | MINOR | A model-specific correction needs a field/general-theory outlet receptive to focused rigorous reassessments; handled at Stage 12 rather than by inflating theory. |

## Independent closest-model re-check

Fresh 2026 searches again found nearby models but not theorem absorption:

- Umezawa (2022), Information Economics and Policy 61, 101004: two-period asymmetric BBPD with horizontal/vertical differentiation and switching costs; equilibrium configurations differ materially from the fixed inherited-share GSS one-period uniform subgame.
- Shrivastav (2023), Information Economics and Policy 65, 101059: imperfect/misinformation consumer recognition with switching costs; different information structure.
- Colombo, Graziano & Pignataro (2024), Information Economics and Policy 67, 101092: imperfect recognition with asymmetric inherited shares; perfect information is a special case but the paper studies information completeness and does not state the GSS global pure-price threshold.
- Umezawa & Yamakawa (2025), Journal of Economics 145, 147–187: two-period BBPD with multiple consumer types and firm-paid switching compensation; different timing, payer, and demand heterogeneity.
- general kinked-demand / Bertrand nonexistence results establish broader possibilities but do not deliver the source-specific payoff factorization (2(x-x_L)(x-x_H)).

A noteworthy methodological analogue is Umezawa's author-hosted 2023 corrigendum to the 2022 IEP paper, which corrects a regime-classification implication in the uniform-pricing benchmark. That note is not a parent theorem for the present model and does not absorb the GSS correction.

## High-stakes reconstruction repeated

The referee audit rechecked the decisive finite deviation conceptually from primitives:

1. the source Eq. (12) candidate is the unique lower-switching smooth FOC intersection;
2. against (a^*), B can move to the no-poaching plateau kink without losing its inherited B-history consumers;
3. the exact source-minus-kink payoff factorization is (2(x_0-x_L)(x_0-x_H));
4. because (x_L<1/2<x_0), the sign is controlled exactly by (x_0-x_H);
5. at equality the kink action is B-optimal but not Nash-compatible because A gains (2sx_0>0).

This reproduces the economic mechanism without relying on numerical sampling.

## Independent submission-audit remediation

The later independent audit findings are closed as follows:

1. **Source fidelity (FATAL):** Eqs. (13)–(17) were re-read from the accepted-manuscript image. The false claim that Eq. (15) was misprinted was removed from manuscript, Python, Lean, regression records, and certificates. Eq. (16)'s sign inversion and the allocation-branch issue are now separated.
2. **Result 4 profit scope (MAJOR):** weak-HBP versus uniform-source-profile profits are piecewise in the realized uniform allocation. The exact no-switch witness `(s,x_0)=(1/2,51/100)` is permanent regression evidence.
3. **Submission claim scope (MAJOR):** abstract, highlights, cover letter, conclusion, and claim ledgers restrict the smaller-firm loss to the weak pure-equilibrium overlap.
4. **Strong endpoint (MAJOR):** `x_0=1` is treated separately; unused HBP quotes are nonunique while realized allocation/payoffs/CS/W are invariant, with zero share/CS gap.
5. **Proof completeness (MAJOR):** Appendix A and Stage-4/4A records use a joint margin–demand capture exclusion, isolate `s=0` and `x_0=1`, and state reverse-branch monotonicity explicitly.
6. **Formal verification (MAJOR):** stale Eq. (15) definitions were replaced, the over-escaped grep guard was repaired with sentinels, and Lean 4.19.0/pinned-mathlib builds pass.
7. **Literature/non-absorption (MAJOR/MINOR):** the Umezawa corrigendum is cited as a methodological analogue; nearby models are distinguished by primitives/timing/information and no formal non-nesting theorem is claimed.

## Repairs authorized and completed

The above mathematical/scope repairs were authorized under theory change control and re-certified at their earliest affected stages. The headline `x_H(s)` theorem, exact Eq. (12) counterexample, mixed-strategy exclusion, and welfare resource-accounting mechanism remain unchanged.

## Stage-11 gate

**RE-CERTIFIED GO / CLOSED.**

Route to Stage 12 — Journal Positioning.
