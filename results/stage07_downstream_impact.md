# Stage 7 — Downstream Welfare and Source-Result Impact

**Verdict:** GO / RECERTIFIED AFTER ASTRA AUDIT  
**Source:** post-referee accepted manuscript; exact Springer VOR equation text remains unverified.  
**Equilibrium scope:** pure uniform-price equilibrium only; mixed pricing remains outside scope.  
**Strong-HBP convention:** nondegenerate source member for CS/profit unless unrestricted-price selection is stated explicitly.

## 1. Corrected uniform pure-existence domain

For
[
s=sigma/\tauin(0,1),
]
the uniform-price pure equilibrium exists iff
[
x_0ge x_H(s)
=
\frac12-\frac{s}{3}
+\frac{sqrt{3s(s+6)}}6.
]

The accepted weak-HBP domain is
[
\frac12<x_0<\bar x(s),
qquad
\bar x(s)=\frac{3-s}{4}.
]

The domains overlap iff
[
0le s<s_c,
qquad
s_c=-3+\frac{6sqrt{33}}{11}
approx0.1333978072.
]

For (0<s<s_c), equilibrium comparisons are restricted to
[
x_H(s)le x_0<\bar x(s).
]

At (s=s_c), (x_H=\bar x) and the weak-domain inequality is strict, so the overlap is empty.

## 2. Consumer surplus from primitives

Define
[
x_u=\frac12+\frac{s}{6}.
]

At the accepted uniform price vector:

- if (x_0ge x_u), A-history consumers on ((x_u,x_0]) switch to B;
- if (x_0<x_u), no consumer switches.

The accepted Eq. (13) is therefore an actual-allocation integral only on the first branch.

### 2.1 Weak HBP: switching branch

Direct primitive integration gives
[
CS^d-CS^u
=
\frac{
-\tau^2(52x_0^2-52x_0-1)
+2sigma\tau(18x_0-17)
+sigma^2
}{36\tau}.
]

This is exactly the accepted-manuscript Eq. (15) after its outer minus sign is distributed. Thus the previous project claim that Eq. (15) itself was algebraically wrong is retired.

At
[
s=1/10,qquad x_0=7/10,
]
both primitive integration and accepted Eq. (15) equal
[
221/720.
]

After substituting (sigma=s\tau), however, the accepted printed Eq. (16) places a further global minus sign in front of the same normalized bracket. At the same exact point Eq. (16) equals
[
-221/720.
]

Hence the source algebraic inconsistency is **Eq. (15) → Eq. (16)**, not the Eq. (15) display itself.

### 2.2 Weak HBP: no-switch branch

When (x_0<x_u), actual primitive integration instead gives
[
CS^d-CS^u
=
\frac{
sigma^2+12sigma\tau x_0-14sigma\tau
-8\tau^2x_0^2+8\tau^2x_0+5\tau^2
}{18\tau}.
]

At
[
s=99/100,qquad x_0=501/1000,
]
the actual no-switch value is
[
17993/4500000>0.
]

Thus accepted Result 3 fails for two separate reasons:

1. the printed Eq. (16) reverses the sign of the correctly normalized Eq. (15);
2. the one-way-switch allocation used in Eq. (13) does not apply when (x_0<x_u).

Direct branch-correct integration yields
[
CS^d>CS^u
]
throughout the accepted weak-HBP profile domain. As an equilibrium statement, this comparison is restricted to the corrected pure overlap.

## 3. Profit accounting under weak dominance

The weak-HBP source-profile profits are
[
\frac{pi_A^d}{\tau}
=
\frac{s^2+6sx_0-2s+10x_0^2-10x_0+5}{9},
]
[
\frac{pi_B^d}{\tau}
=
\frac{s^2-6sx_0+4s+10x_0^2-10x_0+5}{9}.
]

At the accepted uniform price vector the realized profit formulas are branch dependent.

### 3.1 Switching branch (x_0ge x_u)

[
\frac{pi_A^d-pi_A^u}{\tau}
=
\frac{s^2+12sx_0-10s+20x_0^2-20x_0+1}{18},
]
[
\frac{pi_B^d-pi_B^u}{\tau}
=
\frac{s^2-12sx_0+14s+20x_0^2-20x_0+1}{18}.
]

Accepted Eq. (22) corresponds to the B-profit expression on this branch.

### 3.2 No-switch branch (x_0<x_u)

The same accepted uniform prices imply shares (x_0) and (1-x_0). Hence
[
\frac{pi_A^d-pi_A^u}{\tau}
=
\frac{s^2+3sx_0-2s+10x_0^2-19x_0+5}{9},
]
[
\frac{pi_B^d-pi_B^u}{\tau}
=
\frac{s^2-9sx_0+7s+10x_0^2-x_0-4}{9}.
]

Both profit branches join continuously at (x_0=x_u).

Exact regression:
[
s=1/2,qquad x_0=51/100.
]
Primitive demand gives
[
pi_B^d=\frac{3221}{9000},
qquad
pi_B^u=\frac{49}{120},
qquad
pi_B^d-pi_B^u=-\frac{227}{4500}<0.
]

Extending the switching-branch Eq. (22) formula to this no-switch point would instead give
[
4/375>0.
]

Therefore accepted Result 4 cannot be retained over the full weak profile domain merely by relabelling it a profile comparison.

### 3.3 Certified weak pure-overlap profit result

On the corrected weak pure-equilibrium overlap,
[
0le s<s_c,
qquad
x_H(s)le x_0<\bar x(s),
]
the realized uniform branch is the switching branch and
[
\boxed{pi_B^d<pi_B^u}.
]

This is the manuscript's only smaller-firm profit theorem.

## 4. Weak social welfare

With full coverage,
[
W=CS+pi_A+pi_B
=
\beta-c
-\tauint_0^1 |z-y(z)|,dz
-sigma N_{\rm sw}.
]

On the only uniform allocation branch compatible with a weak-domain pure equilibrium,
[
W^d-W^u
=
\frac{\tau}{36}
left[
28x_0^2-28x_0+5
+2s(18x_0-13)+5s^2
\right].
]

At the weak upper boundary,
[
(W^d-W^u)|_{\bar x}
=
-\frac{\tau(1+s)(1+9s)}{144}<0.
]

Hence throughout the corrected weak pure overlap,
[
\boxed{W^d<W^u}.
]

The accepted endpoint-substitution expression is algebraically wrong, but the qualitative Result-5 welfare ranking survives on the restricted pure-equilibrium domain.

## 5. Strong dominance and endpoint separation

For nondegenerate strong dominance,
[
\bar x(s)le x_0<1,
]
the source-selected HBP member has (q_A=c). Under this selection and where the uniform pure equilibrium exists,
[
CS^d-CS^u
=
\frac{\tau(1-x_0)(16-7x_0-13s)}9.
]

Thus accepted Result 6 survives on the corrected pure domain under the source/nonnegative-margin selection.

If below-cost poaching prices are admitted, the nondegenerate strong branch contains a zero-sales family. Consumer surplus and the distribution of profits vary with the selected price member, while allocation and social welfare do not.

The smaller-firm profit ranking from the weak overlap does **not** extend to strong dominance. At
[
s=9/10,qquad x_0=19/20>x_H(s),
]
the source-selected strong-HBP profile and uniform pure equilibrium coexist, yet
[
pi_B^d-pi_B^u=\frac{41}{900}\tau>0.
]

Strong social welfare satisfies
[
W^d-W^u
=
-\frac{\tau(1-x_0)(1-x_0+2s)}9.
]
It is strictly negative for (x_0<1) and equals zero at (x_0=1).

### 5.1 Degenerate endpoint (x_0=1)

At (x_0=1), the inherited B-history segment is empty. The prices directed only to that segment, (q_A) and (p_B), are payoff-irrelevant and are not uniquely determined even under nonnegative-margin restrictions.

Therefore at (x_0=1):

- the full four-price strong-HBP vector is not unique;
- active-segment allocation and active outcomes remain well defined;
- the Result-2 share difference is zero rather than strict;
- the Result-6 CS difference is zero;
- the Result-7 welfare difference is zero;
- unused-price multiplicity does not alter welfare.

## 6. Accepted Results 1–7 recertified impact ledger

| Result | Recertified status |
|---|---|
| Result 1 | **OUTSIDE MAINTAINED DOMAIN.** The (sigma>\tau) result lies outside the maintained (sigma<\tau) reassessment domain and is not altered by the uniform-price correction. |
| Result 2 | **SURVIVES WITH RESTRICTED DOMAIN.** The dominant-firm share ranking survives on the corrected pure domain; it is strict for nondegenerate comparisons and becomes equality at (x_0=1). The accepted weak displayed difference is not the difference implied by its own shares. |
| Result 3 | **INVALID AS STATED.** Eq. (15) itself is correct on its switching branch; printed Eq. (16) reverses its sign, and the no-switch region requires a separate realized-allocation expression. |
| Result 4 | **INVALID AS STATED OVER THE FULL WEAK DOMAIN.** Eq. (22) is a switching-branch formula. On the corrected weak pure overlap, (pi_B^d<pi_B^u); outside it, profile profits must be evaluated on the realized branch. |
| Result 5 | **SURVIVES ON THE RESTRICTED PURE DOMAIN.** Uniform pricing yields higher weak-dominance welfare on the corrected pure overlap. |
| Result 6 | **SELECTION-CONDITIONAL / RESTRICTED.** It survives for nondegenerate (x_0<1) on the corrected pure domain under the source/nonnegative-margin selection; at (x_0=1) the CS gap is zero and unused prices are indeterminate. |
| Result 7 | **SURVIVES / SELECTION-INVARIANT.** Uniform pricing has higher welfare for (x_0<1); equality holds at (x_0=1), including under unused-price multiplicity. |

## 7. No extrapolation into the no-pure region

For
[
1/2<x_0<x_H(s),
]
the project assigns no pure-equilibrium uniform profit, consumer surplus, welfare, or market-share comparison.

The accepted Eq. (12) vector may still be evaluated as a counterfactual price profile, but every such profile calculation must use the actual clipped demand branch. Mixed pricing remains unsolved.

## 8. Stage-7 verdict

**GO / RECERTIFIED.**

Post-Astra recertification changes the downstream diagnosis but not the headline (x_H) theorem:

1. accepted Eq. (15) is restored as source-correct on its switching branch;
2. the CS source error is localized to Eq. (16) plus the no-switch allocation extrapolation;
3. weak profit profile comparisons are branch-corrected;
4. the weak pure-overlap smaller-firm result survives;
5. that profit result is explicitly not generalized to strong dominance;
6. the (x_0=1) strong-HBP endpoint is separated from nondegenerate price-selection claims;
7. weak and strong welfare conclusions survive with the stated domain qualifications.
