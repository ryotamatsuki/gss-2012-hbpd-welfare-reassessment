# Stage 11 — Robustness / Referee Attack Gate

**Verdict:** GO / CLOSED  
**Attack date:** 2026-09-23  
**Input:** Stage-10 full manuscript and Stage-8 frozen theory  
**Certification regression:** NONE  
**Theory rollback:** NOT REQUIRED.

## Executive adversarial verdict

No FATAL or MAJOR mathematical/scope defect was found in the full manuscript. The manuscript remains inside the Stage-8 theorem freeze and Stage-7.5A MODEL-SPECIFIC claim classification.

Three close literature items omitted from the Stage-10 related-literature section were classified MINOR and added: Umezawa (2022), Shrivastav (2023), and Umezawa–Yamakawa (2025). This is an exposition/literature-completeness repair only.

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
| stale formal theorem | PASS | No Stage-10/11 theory change alters formalized definitions or theorem signatures. |
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

## Repairs authorized and completed

Only literature-positioning repairs were made. No equation, proposition, quantifier, domain, benchmark, selection convention, welfare identity, or formal theorem changed.

## Stage-11 gate

**GO / CLOSED.**

Route to Stage 12 — Journal Positioning.
