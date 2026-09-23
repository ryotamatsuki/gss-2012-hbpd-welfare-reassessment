# Stage 4 — Pure uniform-price equilibrium theorem certificate

**Claim ID:** UPE-2012-1  
**Stage verdict:** GO  
**Evidence state:** analytic proof + independent exact-arithmetic regression; proof-assistant core is handed to the mandatory Stage-7.5A Formal Verification Gate.  
**Source scope:** post-referee accepted manuscript, with an explicit VOR wording qualification.

## Theorem

Let
\[
x=x_0\in(1/2,1],\qquad s=\sigma/\tau\in[0,1),
\]
with \(\tau>0\), common marginal cost \(c\), full market coverage, and uniform-price strategies containing all real prices or, equivalently for pure equilibrium, all prices weakly above \(c\).

Define normalized margins
\[
a=(p_A-c)/\tau,\qquad b=(p_B-c)/\tau.
\]

For \(s=0\), the unique pure-strategy Nash equilibrium is
\[
(a,b)=(1,1).
\]

For \(0<s<1\), define
\[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]
Then the complete pure-strategy uniform-price Nash correspondence is
\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,\,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&1/2<x<x_H(s).
\end{cases}
\]

In dimensional prices, when a pure equilibrium exists,
\[
p_A^u=c+\tau+\frac{\sigma}{3},\qquad
p_B^u=c+\tau-\frac{\sigma}{3}.
\]

At \(x=x_H(s)\), firm B has two payoff-maximizing actions against \(p_A^u\), but only the accepted-manuscript Eq. (12) action is part of a Nash profile. The equilibrium correspondence therefore remains a singleton at equality.

The theorem concerns **pure strategies only**. It makes no claim that a mixed equilibrium fails to exist when \(x<x_H(s)\).

## 1. Primitive demand and exhaustive regime partition

Let
\[
d=b-a.
\]
The two history-specific primitive thresholds are
\[
t_A=\frac{d+1+s}{2},\qquad
t_B=\frac{d+1-s}{2}.
\]
Direct clipping to the inherited segments gives
\[
q_A(d)=\operatorname{clip}(t_A,0,x)+
       \operatorname{clip}(t_B-x,0,1-x),
\qquad q_B=1-q_A.
\]

For \(0<s<1\), set
\[
L=-1-s,\quad
\alpha=2x-1-s,\quad
\beta=2x-1+s,\quad
U=1+s.
\]
Because \(t_A-t_B=s>0\), simultaneous switching in both directions cannot occur. The five exhaustive regimes are
\[
q_A(d)=
\begin{cases}
0,&d\le L,\\
(d+1+s)/2,&L<d<\alpha,\\
x,&\alpha\le d\le\beta,\\
(d+1-s)/2,&\beta<d<U,\\
1,&d\ge U.
\end{cases}
\]
All equality points are retained.

## 2. Strategy-domain reduction

The accepted manuscript does not state a formal lower price bound in the inspected model passage. The pure-equilibrium set is nevertheless identical on unrestricted real prices and on (p_ige c).

A joint margin--demand elimination is required.

* If a firm has positive demand at a negative margin, moving to zero margin strictly improves its payoff to zero.
* If a firm has positive demand at zero margin, a sufficiently small positive price increase preserves positive demand and yields strictly positive profit.
* If a firm has zero demand and its full-demand rival has a negative margin, the rival strictly improves by moving to zero margin.
* If a firm has zero demand and its full-demand rival has zero margin, the rival has a sufficiently small profitable positive price increase.
* If a firm has zero demand and its full-demand rival has a strictly positive margin, the excluded firm can choose the same positive normalized margin as the rival. This sets (d=0), gives the excluded firm strictly positive demand, and yields strictly positive profit.

Hence no pure equilibrium can contain a zero-demand firm, a nonpositive margin with positive demand, or a full-capture tail. Every pure equilibrium has strictly positive margins and strictly positive demand for both firms.

This argument does not assume that an excluded firm can always enter at a positive margin against an arbitrary rival price; instead it first uses the capturing firm's own margin when necessary.

## 3. Exclude capture, plateau, and kink profiles

For (0<s<1), on the no-switch plateau (alphale dle\beta),
[
Pi_A=x(b-d),qquad
Pi_B=(1-x)(a+d).
]

At any plateau interior with (x<1), A strictly prefers a lower (d) and B strictly prefers a higher (d), so the profile cannot be Nash.

At (d=alpha) with (x<1), B can move to (d=\beta), keep share (1-x), raise its margin by (2s), and gain
[
2s(1-x)>0.
]
At the endpoint (x=1), B has zero demand at (d=alpha), so the Stage-4 margin--demand elimination excludes the profile instead; the strict-gain formula is not used there.

At (d=\beta), A can move to (d=alpha), keep share (x), raise its margin by (2s), and gain
[
2sx>0.
]
Hence neither plateau interiors nor either plateau kink can be Nash.

The case (s=0) is handled separately rather than by these kink arguments because (alpha=\beta) and the plateau collapses. Then inherited history has no effect on demand,
[
q_A(d)=operatorname{clip}!left(\frac{d+1}{2},0,1\right),
]
and after capture/nonpositive-margin profiles are excluded, the two interior Hotelling first-order conditions intersect uniquely at ((a,b)=(1,1)).

## 4. Smooth switching-branch intersections

### A-history consumers switch to B

On \(L<d<\alpha\),
\[
\Pi_A=\frac{(b-d)(d+1+s)}2,\qquad
\Pi_B=\frac{(a+d)(1-s-d)}2.
\]
Local optimality in this strict branch gives
\[
a=d+1+s,\qquad b=1-s-d.
\]
Together with \(d=b-a\), the unique intersection is
\[
d^*=-\frac{2s}{3},\qquad
a^*=1+\frac{s}{3},\qquad
b^*=1-\frac{s}{3}.
\]
Its strict branch condition is
\[
x>x_u(s):=\frac12+\frac{s}{6}.
\]

### B-history consumers switch to A

On \(\beta<d<U\), the analogous conditions give
\[
d=\frac{2s}{3},\qquad
a=1-\frac{s}{3},\qquad
b=1+\frac{s}{3}.
\]
The branch requirement would imply
\[
x<\frac12-\frac{s}{6}<\frac12,
\]
contradicting \(x>1/2\). This branch contains no pure equilibrium.

With capture, plateau, kinks, and zero margins excluded, the accepted-version Eq. (12) profile is the only remaining pure candidate.

## 5. Global best-response certification

At \((a^*,b^*)\), A's lower-switching payoff has the unique vertex \(a^*\). Its best no-switch boundary alternative has payoff shortfall
\[
\Pi_A(a^*,b^*)-\Pi_A(d=\alpha)
=2(x-x_u)^2>0
\]
for \(x>x_u\). The upper-switching quadratic is decreasing from its plateau boundary because its vertex lies below \(\beta\). Capture cannot improve on the source action. Hence A's source action is its unique global best response whenever the candidate lies in the strict lower-switching branch.

For B, the best plateau/no-poaching action against \(a^*\) is
\[
b_k=a^*+\beta=2x+\frac{4s}{3}.
\]
Define
\[
x_L(s)=\frac12-\frac{s}{3}
       -\frac{\sqrt{3s(s+6)}}6.
\]
Exact factorization gives
\[
\Pi_B(a^*,b^*)-\Pi_B(a^*,b_k)
=2(x-x_L)(x-x_H).
\]
For \(0<s<1\),
\[
x_L<\frac12<x,\qquad x_u<x_H<1.
\]
The key orderings follow by squaring positive sides:
\[
x_H>x_u
\iff \sqrt{3s(s+6)}>3s
\iff s<3,
\]
and
\[
x_H<1
\iff \sqrt{3s(s+6)}<3+2s
\iff (3-s)^2>0.
\]
Therefore B's accepted-version action is a global best response iff \(x\ge x_H(s)\).

This proves both sufficiency and necessity because all other pure branches have already been eliminated.

## 6. Equality / multiplicity trigger

At \(x=x_H(s)\), B is indifferent between \(b^*\) and \(b_k\). The lower switching quadratic has the unique maximizer \(b^*\); the plateau is affine and maximized at \(b_k\); the upper branch decreases away from \(b_k\).

The kink profile \((a^*,b_k)\) is not Nash. Holding \(b_k\) fixed, A moves from \(d=\beta\) to \(d=\alpha\), raises its margin by \(2s\), keeps share \(x\), and gains
\[
2sx>0.
\]
Hence the Nash set remains the singleton \((a^*,b^*)\) at the knife edge.

## 7. Exact regression counterexample

At
\[
(\tau,\sigma,x,c)=(1,1/2,3/5,0),
\]
the accepted-version Eq. (12) candidate is
\[
(p_A,p_B)=(7/6,5/6).
\]
B earns \(25/72\). The no-poaching kink deviation \(p_B'=28/15\) yields \(56/75\), so
\[
\Delta\pi_B=\frac{719}{1800}>0.
\]
All prices are above cost and the point is inside the accepted manuscript's weak-dominance domain.

## 8. Boundary / hostile checks

The proof and the independent exact evaluator cover:

* \(x\downarrow1/2\): for every \(s>0\), \(x_H(s)>1/2\), so sufficiently weak inherited asymmetry is in the no-pure region.
* \(x\uparrow1\): \(x_H(s)<1\), so the accepted profile remains the unique pure equilibrium, including the zero-measure B-history limit.
* \(s\downarrow0\): \(x_H(s)\downarrow1/2\), joining the standard Hotelling equilibrium.
* \(s\uparrow1\): excluded by the strict maintained source assumption \(s<1\); one-sided limits are tested.
* \(x=x_u\): the candidate is on the no-switch kink and is not Nash.
* \(x=x_H\): the B-indifference trigger is audited and Nash remains unique.
* \(x=\bar x=(3-s)/4\): this changes HBP classification, not the uniform demand partition.
* \(d=L,\alpha,\beta,U\): every clipping equality is treated explicitly.
* zero margins, negative margins, large positive prices, full capture, and zero-demand tails: excluded by the strategy-domain/capture arguments.
* measure-zero consumer ties: do not change market shares or profits.
* disappearing inherited B-history segment at \(x=1\): the direct clipped demand remains well-defined and the theorem continues.

## 9. Evidence map

| Claim | Attack | Evidence |
|---|---|---|
| primitive demand exhaustive | derive both history thresholds and clip independently | \`derivations/uniform_price_game_full_demand.md\`; \`code/uniform_game_cleanroom.py\` |
| candidate globality | maximize every unilateral quadratic/affine piece | \`derivations/uniform_price_global_best_responses.md\` |
| no alternative pure equilibrium | enumerate capture, plateau, both smooth branches, kinks, and zero-margin boundaries | this certificate |
| exact \(x_H\) condition | factor source-vs-kink payoff difference | symbolic reconstruction + analytic proof |
| equality multiplicity | vary B within its indifference set and recompute A's response | this certificate; exact equality regression |
| strategy domain | attack negative/zero margins and capture | this certificate |
| exact failure point | rational regime-crossing counterexample | \`code/uniform_game_cleanroom.py\` |

## 10. Formal-verification handoff

Formal verification is **APPLICABLE**. Stage 7.5A must include at least:

1. the \(x_L/x_H\) payoff factorization and threshold orderings;
2. the exact rational counterexample;
3. equality-boundary best-response algebra;
4. accepted Eq. (15) source-fidelity identity and the Eq. (16) sign inversion;
5. branch-correct weak/no-switch and strong-profit exact regressions;
6. the weak-welfare endpoint identity;
7. the pure-overlap boundary \(x_H\le\bar x\) iff \(s\le -3+6\sqrt{33}/11\).

## Final Stage-4 state

**GO.** The complete pure-strategy uniform-price correspondence is analytically characterized. Stage 4A must now independently certify that this production proof has not omitted a branch, boundary, strategy-domain case, or indifference-trigger equilibrium.
