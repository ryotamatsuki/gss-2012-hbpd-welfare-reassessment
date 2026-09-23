# Stage 8 — Canonical Theory Freeze

**Verdict:** REOPENED / POST-ASTRA REFREEZE IN PROGRESS  
**Freeze branch:** \`research/stage-08-theory-freeze\`  
**Stage-8 input branch:** \`research/stage-075a-freeze-gate\`  
**Stage-7.5A input head:** \`d159a6d286d5547873decceb4cc26e6d3e0871ef\`  
**Workflow:** research-paper-workflow v2.4, main \`63f11a50a13d9328213498a5a6576d00b9bceef7\`  
**Source scope:** lawful post-referee accepted manuscript; exact Springer VOR equation text remains uninspected.

## 1. Frozen research question

What is the complete pure-strategy uniform-price equilibrium correspondence in the inherited-history switching-cost Hotelling model used by Gehrig, Shy, and Stenbacka (2012), and how does the corrected equilibrium domain alter the accepted manuscript's market-share, profit, consumer-surplus, and social-welfare comparisons?

## 2. Frozen contribution statement

The paper is a **model-specific mathematical correction/reassessment** of GSS (2012).

Its contribution is:

1. reconstruct the complete uniform-price demand correspondence from primitive consumer choice;
2. show that accepted-manuscript Eq. (12) is a smooth one-way-switch branch solution whose global pure-Nash validity requires an additional exact parameter restriction;
3. characterize the complete pure-strategy price correspondence;
4. correct the accepted-manuscript consumer-surplus diagnosis source-faithfully: Eq. (15) is correct on its switching branch, Eq. (16) reverses its sign, and the no-switch branch requires separate accounting;
5. correct weak-profit profile accounting across the uniform switching/no-switch branches and propagate the corrected equilibrium domain through accepted-manuscript Results 1–7;
6. identify which qualitative welfare conclusions survive and which equilibrium comparisons do not.

No generic theorem about all switching-cost Bertrand games is claimed.

## 3. Frozen model

### Players

Two firms, A and B.

### Locations

Hotelling line \([0,1]\), with A at 0 and B at 1.

### Consumers

Unit mass of consumers indexed by \(x\in[0,1]\), each buying exactly one unit under full market coverage.

### Inherited history

\[
h(x)=A\quad\text{for }x\le x_0,\qquad
h(x)=B\quad\text{for }x>x_0,
\]
with
\[
x_0\in(1/2,1].
\]

### Costs

Common marginal cost \(c\in\mathbb R\). Transport cost parameter \(\tau>0\). Switching cost \(\sigma\ge0\), with maintained source restriction
\[
0\le\sigma<\tau.
\]

### Information

Firms know the inherited history partition. Consumers know prices, locations, their inherited supplier, transport costs, and switching cost.

### Pricing regimes

- **Uniform pricing:** each firm chooses one price \(p_A,p_B\).
- **History-based pricing:** each firm may choose loyalty and poaching prices as in the accepted manuscript.

### Equilibrium concept

The headline theorem concerns **pure-strategy Nash equilibrium in uniform prices**.

Mixed-strategy pricing is outside scope.

## 4. Frozen normalization

Define
\[
s=\frac{\sigma}{\tau},\qquad
a=\frac{p_A-c}{\tau},\qquad
b=\frac{p_B-c}{\tau},\qquad
d=b-a.
\]

This normalization is bijective for fixed \(\tau>0\) and does not alter the pure-equilibrium set.

## 5. Frozen primitive uniform demand

The two history-specific switching thresholds are
\[
t_A=\frac{d+1+s}{2},\qquad
t_B=\frac{d+1-s}{2}.
\]

The exact clipped share of A is
\[
q_A(d)
=
\operatorname{clip}(t_A,0,x_0)
+
\operatorname{clip}(t_B-x_0,0,1-x_0),
\qquad
q_B=1-q_A.
\]

For \(0<s<1\), define
\[
L=-1-s,\qquad
\alpha=2x_0-1-s,\qquad
\beta=2x_0-1+s,\qquad
U=1+s.
\]

Then
\[
q_A(d)=
\begin{cases}
0,& d\le L,\\
(d+1+s)/2,& L<d<\alpha,\\
x_0,& \alpha\le d\le\beta,\\
(d+1-s)/2,& \beta<d<U,\\
1,& d\ge U.
\end{cases}
\]

This five-piece demand correspondence is canonical and frozen.

## 6. Frozen headline theorem — UPE-2012-1

Define
\[
x_H(s)
=
\frac12-\frac{s}{3}
+\frac{\sqrt{3s(s+6)}}6.
\]

For \(s=0\), the unique pure uniform-price equilibrium has normalized margins
\[
(a,b)=(1,1).
\]

For \(0<s<1\),
\[
\mathcal E^u(x_0,s)=
\begin{cases}
\{(1+s/3,\,1-s/3)\},&x_0\ge x_H(s),\\
\varnothing,&1/2<x_0<x_H(s).
\end{cases}
\]

Equivalently, where a pure equilibrium exists,
\[
p_A^u=c+\tau+\frac{\sigma}{3},\qquad
p_B^u=c+\tau-\frac{\sigma}{3}.
\]

At \(x_0=x_H(s)\), firm B has a second payoff-equal no-poaching kink best response against A's source price, but the resulting kink profile is not Nash because A has a strict profitable deviation. The equilibrium remains singleton at equality.

This is a **complete pure-strategy correspondence**, not a statement about mixed equilibrium.

## 7. Refrozen strategy-domain result

For the **uniform-price game**, the pure-equilibrium set is unchanged whether prices are allowed over all real numbers or restricted to (p_ige c).

The proof uses a joint margin--demand elimination:

- negative margin with positive demand is strictly improved by moving to zero margin;
- zero margin with positive demand admits a small profitable increase;
- if one firm has zero demand and the full-demand rival has nonpositive margin, that rival can improve;
- if one firm has zero demand and the full-demand rival has positive margin, the excluded firm can match that positive margin, set (d=0), obtain positive demand, and earn positive profit.

Hence every uniform pure equilibrium has strictly positive margins and strictly positive demand.

This invariance does **not** automatically extend to the strong-HBP price vector.

## 8. Frozen exact counterexample

At
\[
(\tau,\sigma,x_0,c)=(1,1/2,3/5,0),
\]
the accepted-manuscript Eq. (12) profile is
\[
(p_A,p_B)=(7/6,5/6).
\]

Firm B earns
\[
\pi_B=\frac{25}{72}.
\]

The no-poaching kink deviation
\[
p_B'=\frac{28}{15}
\]
yields
\[
\pi_B'=\frac{56}{75},
\]
so
\[
\pi_B'-\pi_B=\frac{719}{1800}>0.
\]

This regression is permanent.

## 9. Frozen mixed-equilibrium scope

For
\[
1/2<x_0<x_H(s),
\]
the project proves only:

> there is no pure-strategy price equilibrium.

It does not prove:

- no Nash equilibrium;
- no mixed equilibrium;
- uniqueness/nonuniqueness of a mixed equilibrium;
- equilibrium welfare in that region.

The accepted Eq. (12) vector may be evaluated there only as a counterfactual profile.

## 10. Frozen weak-HBP / uniform overlap

The accepted weak-HBP domain is
\[
\frac12<x_0<\bar x(s),\qquad
\bar x(s)=\frac{3-s}{4}.
\]

The pure-uniform and weak-HBP domains overlap iff
\[
0\le s<s_c,
\]
where
\[
s_c=-3+\frac{6\sqrt{33}}{11}.
\]

For \(0<s<s_c\), equilibrium comparisons are restricted to
\[
x_H(s)\le x_0<\bar x(s).
\]

At \(s=s_c\), \(x_H=\bar x\) and the weak-domain inequality is strict, so the overlap is empty.

## 11. Refrozen weak consumer-surplus correction

Let
[
x_u=rac12+rac{s}{6}.
]

The accepted uniform-price vector induces:

- one-way A-to-B switching when (x_0ge x_u);
- no switching when (x_0<x_u).

On the switching branch,
[
CS^d-CS^u
=
rac{
-	au^2(52x_0^2-52x_0-1)
+2sigma	au(18x_0-17)
+sigma^2
}{
36	au
}.
]

This expression is exactly accepted-manuscript Eq. (15) after distributing its outer minus sign. The previous project claim that Eq. (15) itself was algebraically wrong is withdrawn.

After substituting (sigma=s	au), accepted printed Eq. (16) adds a further global minus sign to the same bracket. At (s=1/10,x_0=7/10), primitive integration and Eq. (15) both equal (221/720), whereas printed Eq. (16) equals (-221/720).

On the no-switch branch,
[
CS^d-CS^u
=
rac{
sigma^2+12sigma	au x_0-14sigma	au
-8	au^2x_0^2+8	au^2x_0+5	au^2
}{
18	au
}.
]

Direct primitive integration gives (CS^d>CS^u) throughout the accepted weak-HBP profile domain. As an **equilibrium** comparison, this statement is restricted to the certified pure overlap.

The exact no-switch regression (s=99/100,x_0=501/1000) remains (17993/4500000>0).

## 12. Refrozen weak profit result

At the accepted uniform price vector, realized profit is branch dependent.

For (x_0ge x_u),
[
rac{pi_B^d-pi_B^u}{	au}
=
rac{s^2-12sx_0+14s+20x_0^2-20x_0+1}{18}.
]

For (x_0<x_u),
[
rac{pi_B^d-pi_B^u}{	au}
=
rac{s^2-9sx_0+7s+10x_0^2-x_0-4}{9}.
]

The formulas agree at (x_0=x_u). Accepted Eq. (22) is the switching-branch expression and cannot be extrapolated into the no-switch region.

At (s=1/2,x_0=51/100), the actual gap is (-227/4500), while the invalid switching-branch extension gives (4/375>0).

On every weak-HBP / pure-uniform equilibrium comparison,
[
pi_B^d<pi_B^u.
]

This sign is not generalized to strong dominance. At (s=9/10,x_0=19/20), the source-selected strong-HBP gap is (41/900>0).

## 13. Frozen weak welfare result

With full coverage,
\[
W=CS+\pi_A+\pi_B
=
\text{gross utility}
-\text{transport cost}
-\text{switching cost}.
\]

Prices are transfers.

On the corrected weak equilibrium overlap,
\[
W^d<W^u.
\]

The accepted endpoint-substitution expression is algebraically incorrect, but the qualitative welfare ranking survives on the corrected pure domain.

## 14. Refrozen strong-HBP selection qualification

For nondegenerate strong dominance (ar x(s)le x_0<1), unrestricted real prices generate a zero-sales poaching-price family.

In normalized notation
[
u=rac{q_A-c}{	au},
]
the family satisfies
[
3-s-4x_0le ule0,
]
with corresponding B loyalty price
[
rac{p_B-c}{	au}=u+2x_0-1+s.
]

Across this nondegenerate family:

- allocation is unchanged;
- social welfare is unchanged;
- consumer surplus and firm-profit distribution can change.

Under the source/nonnegative-margin convention (q_Age c), the nondegenerate family selects the source member (u=0), i.e. (q_A=c).

At (x_0=1), the inherited B-history segment is empty. The prices (q_A) and (p_B), directed only to that segment, remain indeterminate even under nonnegative-margin restrictions. Active allocation, active profits, consumer surplus, and welfare are invariant to those unused prices.

Therefore strong-HBP CS/profit statements for (x_0<1) are selection-conditional unless the source/nonnegative-margin member is imposed, and full price-vector uniqueness is never asserted at (x_0=1).

## 15. Refrozen strong consumer-surplus result

For nondegenerate (x_0<1), under the source/nonnegative-margin strong-HBP selection,
[
CS^d-CS^u
=
rac{	au(1-x_0)(16-7x_0-13s)}9.
]

The accepted strong-HBP CS threshold survives on the corrected pure-uniform domain under this selection.

At (x_0=1), the CS gap is zero and the full strong-HBP price vector is not unique because the B-history segment is empty.

## 16. Frozen strong welfare result

For every selected member of the strong-HBP zero-sales family,
\[
W^d-W^u
=
-\frac{\tau(1-x_0)(1-x_0+2s)}9.
\]

Hence
\[
W^d<W^u
\]
for \(x_0<1\), with equality only at the degenerate limit \(x_0=1\).

This result is selection-invariant.

## 17. Refrozen accepted-manuscript Results 1–7 impact

| Result | Refrozen corrected status |
|---|---|
| Result 1 | outside maintained (sigma<	au) reassessment domain; not affected by UPE correction |
| Result 2 | survives on the corrected pure domain; strict share ranking applies only to nondegenerate comparisons and becomes equality at (x_0=1); displayed weak-branch difference is wrong |
| Result 3 | invalidated as stated; Eq. (15) itself is correct on the switching branch, Eq. (16) reverses its sign, and no-switch branch accounting differs |
| Result 4 | invalidated as stated over the full weak domain because Eq. (22) is a switching-branch formula; on the weak pure overlap (pi_B^d<pi_B^u) |
| Result 5 | survives on corrected weak pure-equilibrium domain |
| Result 6 | survives for nondegenerate (x_0<1) on corrected pure domain under source/nonnegative-margin selection; at (x_0=1) CS gap is zero and full price vector is nonunique |
| Result 7 | survives on corrected pure domain; welfare is selection-invariant and equals uniform at (x_0=1) |

## 18. Proposition maturity classification

| Claim | State |
|---|---|
| UPE-2012-1 complete pure correspondence | PROVED |
| Eq. (12) exact failure witness | PROVED |
| equality singleton result | PROVED |
| uniform strategy-domain invariance | PROVED after joint margin--demand recertification |
| weak CS branch/source correction and sign | PROVED |
| weak profile B-profit branch correction | PROVED |
| weak smaller-firm profit ranking on pure overlap | PROVED |
| strong-domain counterexample to overbroad weak profit wording | PROVED |
| weak welfare ranking on pure overlap | PROVED |
| strong CS ranking | CONDITIONAL on source/nonnegative-margin HBP selection for nondegenerate (x_0<1); zero gap at (x_0=1) |
| strong welfare ranking | PROVED on corrected pure domain; equality at (x_0=1) |
| mixed equilibrium below (x_H) | OUT OF SCOPE / UNRESOLVED |

## 19. Frozen portability classification

Project-level classification:

**MODEL-SPECIFIC.**

Certified invariances:

- common marginal-cost translation;
- transport-scale normalization;
- price-level versus price-difference representation;
- measure-zero tie convention;
- exact equality handling.

Not certified:

- alternative spatial demand systems;
- outside options;
- heterogeneous switching costs;
- alternative timing/information structures;
- general asymmetric installed-base models.

No Stage-7.5A rescue/generalization program is authorized.

## 20. Formal-verification state after Astra rollback

**REOPENED — fresh post-Astra CI required before refreeze.**

Toolchain remains Lean 4.19.0 with mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

Formal coverage classification remains **PROOF-CRITICAL CORE**, not full economic model.

The revised formal target set includes:

- B source-vs-kink payoff factorization;
- (x_u<x_H<1);
- exact (719/1800) counterexample;
- equality-kink A gain;
- accepted Eq. (15) identity with the primitive switching-branch CS formula;
- accepted Eq. (16) sign inversion;
- exact weak no-switch and strong-domain profit regressions;
- no-switch CS regression exact positive value;
- weak-welfare endpoint identity;
- weak/pure overlap polynomial and closed-form root.

The CI guard itself is part of the recertification: sentinel inputs containing `by sorry` and `axiom bad : False` must be detected before the project-source scan is accepted.

Not formalized: continuum demand derivation, full clipping partition from primitives, Nash definition, complete alternative-equilibrium search, mixed equilibrium, or source provenance.

## 21. Refrozen closest-paper / novelty distinction

The contribution is not “kinked Bertrand games may lack pure equilibrium.”

The contribution is the exact source-specific reassessment of the GSS (2012) benchmark: accepted Eq. (12) requires an additional global-best-response restriction, the restriction is characterized exactly by (x_H(s)), the complete pure correspondence is derived, and downstream accepted-manuscript welfare/profit/CS results are reclassified accordingly.

The author-posted Umezawa (2023) corrigendum is a close methodological correction precedent and is explicitly cited. It corrects a nearby uniform-pricing regime inference, but the accessible corrigendum does not state the GSS-specific (x_H(s)) threshold.

In the accessible versions inspected at Stage 6, no prior source was located that supplies the GSS-specific (x_H(s)) theorem. The project does not claim universal non-absorption across uninspected proprietary versions, appendices, or every possible specialization.

## 22. Frozen interpretation

The result concerns the theoretical consequences of inherited customer histories and switching costs for global price competition.

No empirical causal claim, policy calibration, or external-validity claim is frozen.

Any policy discussion in the manuscript must be phrased as a consequence **within the source model**.

## 23. Explicit claims not made

The paper does not claim:

- that the exact Springer VOR necessarily contains identical equations until direct VOR comparison;
- that all switching-cost Bertrand games have the same threshold;
- that no Nash equilibrium exists below \(x_H\);
- that mixed pricing has been solved;
- that the result is portable to alternative demand systems;
- that Lean formalizes the full economic model;
- that any welfare comparison outside the certified pure-equilibrium domain is an equilibrium comparison;
- that strong-HBP consumer surplus is selection-free under unrestricted below-cost prices;
- any first-best or planner-optimality result.

## 24. Frozen evidence set

Mathematical:

- \`results/stage04_theorem_certificate.md\`
- \`results/stage04a_independent_certificate.md\`
- \`derivations/uniform_price_game_full_demand.md\`
- \`derivations/uniform_price_global_best_responses.md\`
- \`derivations/consumer_surplus_primitive_reconstruction.md\`
- \`derivations/welfare_and_result_impact.md\`

Scope / novelty:

- \`results/stage06_novelty_rekill.md\`
- \`results/stage07_downstream_impact.md\`
- \`results/stage075_full_theory_freeze_decision.md\`
- \`results/stage075a_scope_portability_redteam.md\`
- \`results/contribution_robustness_certificate.md\`
- \`results/claim_scope_ledger.md\`

Formal:

- \`results/stage075a_formal_verification_certificate.md\`
- \`formal/Gss2012/Core.lean\`
- \`formal/lakefile.lean\`
- \`formal/lean-toolchain\`
- \`.github/workflows/lean-formal.yml\`

Source:

- \`sources/gss_2012_accepted_manuscript_comparison.md\`
- \`sources/gss_2012_version_boundary.md\`

## 25. Stage-8 freeze rule

Any post-freeze change to:

- primitives;
- strategy domains;
- equilibrium concept;
- \(x_H\);
- theorem quantifiers;
- pure-existence/nonexistence result;
- mixed-equilibrium scope;
- HBP selection rule;
- CS/profit/welfare formulas;
- accepted Result 1–7 classifications;
- portability classification;
- formal theorem statements or encoded assumptions;

requires explicit change control and rollback to the earliest affected stage.

Stage 9–14 may improve reproducibility, exposition, journal fit, formatting, figures, references, and submission compliance, but may not silently change the frozen theory.

## 26. Stage-8 post-Astra refreeze status

The headline UPE theorem, mixed-strategy scope, weak/strong welfare rankings, and MODEL-SPECIFIC classification survive. The source-fidelity, profit-branch, endpoint, proof-completeness, literature, and formal-target records have been rewritten.

**REFREEZE PENDING ONLY THE FRESH POST-ASTRA FORMAL / REPRODUCIBILITY CI.**

Once those gates pass, this document is to be marked **GO — CANONICAL THEORY REFROZEN AFTER ASTRA AUDIT** without any further mathematical change.
