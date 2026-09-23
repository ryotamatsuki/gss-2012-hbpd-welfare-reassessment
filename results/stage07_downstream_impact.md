# Stage 7 — Downstream welfare and source-result impact

**Verdict:** GO  
**Source:** post-referee accepted manuscript; exact VOR equation text remains unverified.  
**Equilibrium scope:** pure uniform-price equilibrium only. Mixed pricing is outside scope.  
**HBP price-domain convention for CS/profit:** source member \(q_A=c\), equivalently nonnegative net margins on the strong-HBP poaching price; unrestricted below-cost selection is reported separately.

## 1. Corrected uniform pure-existence domain

For
\[
s=\sigma/\tau\in(0,1),
\]
the uniform-price pure equilibrium exists iff
\[
x_0\ge x_H(s)
=\frac12-\frac{s}{3}
+\frac{\sqrt{3s(s+6)}}6.
\]

The accepted manuscript's weak-HBP domain is
\[
\frac12<x_0<\bar x(s),\qquad
\bar x(s)=\frac{3-s}{4}.
\]

These domains overlap iff
\[
0\le s<s_c,\qquad
s_c=-3+\frac{6\sqrt{33}}{11}
\approx0.1333978072.
\]
For \(0<s<s_c\), the weak-HBP / pure-uniform equilibrium comparisons are restricted to
\[
x_H(s)\le x_0<\bar x(s).
\]
At \(s=s_c\), \(x_H=\bar x\) and the weak-domain inequality is strict, so the overlap is empty.

The exact boundary follows from
\[
x_H(s)=\bar x(s)
\iff 11s^2+66s-9=0
\]
on \(s\in[0,1)\).

This narrow overlap is a central downstream consequence of the global price-game correction.

## 2. Consumer-surplus accounting from primitives

For the accepted-version uniform price profile define
\[
x_u=\frac12+\frac{s}{6}.
\]
Its actual allocation is piecewise:

* \(x_0\ge x_u\): A-history consumers on \((x_u,x_0]\) switch to B;
* \(x_0<x_u\): no consumer switches.

The accepted-manuscript Eq. (13) writes the first allocation and therefore cannot be used unchanged when \(x_0<x_u\).

### Weak HBP

Direct primitive integration gives, in dimensional form,

\[
CS^d-CS^u=
\frac{-\tau^2(52x_0^2-52x_0-1)
+2\sigma\tau(18x_0-17)+\sigma^2}{36\tau}
\]
when \(x_0\ge x_u\), and

\[
CS^d-CS^u=
\frac{\sigma^2+12\sigma\tau x_0-14\sigma\tau
-8\tau^2x_0^2+8\tau^2x_0+5\tau^2}{18\tau}
\]
when \(x_0<x_u\).

Both are strictly positive throughout the accepted manuscript's weak-dominance profile domain.

#### Analytic sign proof: switching branch

Normalize \(\tau=1\). The numerator is
\[
N_1=-52x^2+52x+1+36sx-34s+s^2,
\]
a concave quadratic in \(x\). A switching subinterval inside weak dominance exists only for \(s\le3/5\). Its endpoint values satisfy
\[
N_1(x_u)=\frac{2(25s^2-72s+63)}9>0
\]
because the quadratic in \(s\) has negative discriminant, and
\[
N_1(\bar x)=\frac{(1+s)(43-45s)}4>0
\]
for \(s\le3/5\). Concavity implies positivity throughout the interval.

#### Analytic sign proof: no-switch branch

The numerator is
\[
N_0=s^2+12sx-14s-8x^2+8x+5,
\]
also concave in \(x\). At the lower endpoint,
\[
N_0(1/2)=(1-s)(7-s)>0.
\]
If \(s\le3/5\), the upper endpoint is \(x_u\), where
\[
N_0(x_u)=\frac{25s^2-72s+63}{9}>0.
\]
If \(s>3/5\), the weak upper endpoint is \(\bar x<x_u\), where
\[
N_0(\bar x)=\frac{(1-s)(5s+13)}2>0.
\]
Hence the accepted manuscript's weak-dominance CS sign-reversal region does not survive direct integration.

The previous upstream regression at \(s=.99,x_0=.501\) is permanently rejected as a branch-extension error.

## 3. Profit accounting under weak dominance

The weak-HBP minus uniform-candidate normalized profit differences are

\[
\frac{\pi_A^d-\pi_A^u}{\tau}
=
\frac{s^2+12sx_0-10s+20x_0^2-20x_0+1}{18},
\]

\[
\frac{\pi_B^d-\pi_B^u}{\tau}
=
\frac{s^2-12sx_0+14s+20x_0^2-20x_0+1}{18},
\]

and

\[
\frac{(\pi_A^d+\pi_B^d)-(\pi_A^u+\pi_B^u)}{\tau}
=
\frac{s^2+2s+20x_0^2-20x_0+1}{9}.
\]

The accepted manuscript's Result 4 identifies a high-\(s\) profile region where B's HBP profit exceeds its uniform-candidate profit. That region is disjoint from the corrected weak-HBP / pure-uniform equilibrium overlap.

Indeed, for all \(0\le s<s_c\), the numerator of B's gap is a convex quadratic in \(x\). On the larger interval \([1/2,\bar x]\) its endpoint values are
\[
s^2+8s-4<0
\]
and
\[
\frac{(1+s)(21s-11)}4<0.
\]
Therefore it is negative throughout the interval, and in particular on
\[
x_H(s)\le x_0<\bar x(s).
\]

Thus, whenever both regimes admit the pure equilibria being compared under weak dominance,
\[
\boxed{\pi_B^d<\pi_B^u}.
\]

The accepted manuscript's high-switching-cost Result-4 region remains interpretable only as a comparison with the Eq. (12) **counterfactual price profile**, not as a comparison of two pure equilibria.

## 4. Social welfare from real resource costs

With full coverage and one unit purchased by every consumer,
\[
W=CS+\pi_A+\pi_B
=\beta-c
-\tau\int_0^1|z-y(z)|\,dz
-\sigma N_{\rm sw}.
\]
Prices are transfers. This identity is checked independently against direct CS and profit functions.

### Weak dominance

On the only uniform-allocation branch relevant to a weak-domain pure equilibrium,
\[
W^d-W^u
=
\frac{\tau\left[
28x_0^2-28x_0+5
+2s(18x_0-13)+5s^2
\right]}{36}.
\]
It is increasing in \(x_0>1/2\). At the weak upper boundary,
\[
(W^d-W^u)\big|_{\bar x}
=
-\frac{\tau(1+s)(1+9s)}{144}<0.
\]
Therefore
\[
\boxed{W^d<W^u}
\]
throughout the corrected weak-HBP / pure-uniform overlap.

The accepted manuscript's endpoint expression differs algebraically from the direct substitution, but the qualitative welfare sign survives.

Outside the uniform pure-existence domain, the branch-correct profile welfare can still be evaluated, but it is not called equilibrium welfare.

## 5. Strong dominance

The strong-HBP domain is
\[
x_0\ge\bar x(s).
\]
A pure uniform equilibrium and strong HBP can be compared whenever
\[
x_0\ge\max\{\bar x(s),x_H(s)\}.
\]

For every \(s>0\), \(x_H>x_u\). Hence every nondegenerate strong-domain **pure-equilibrium** comparison lies on the accepted manuscript's one-way-switch uniform branch.

### Consumer surplus — source member \(q_A=c\)

For the source strong-HBP equilibrium member,
\[
CS^d-CS^u
=
\frac{\tau(1-x_0)(16-7x_0-13s)}9.
\]
Thus the accepted manuscript's Result-6 threshold
\[
s>\frac{16-7x_0}{13}
\]
survives **within the corrected pure-uniform domain**, provided the nonnegative-margin/no-loss HBP selection \(q_A=c\) is used.

If below-cost poaching prices are admitted, strong HBP has a zero-sales equilibrium family. Consumer surplus and firm profits vary across that family even though allocation is fixed. Result 6 is therefore selection-dependent on the unrestricted price domain.

### Profits — source member

The normalized strong-HBP minus uniform profit gaps are
\[
\frac{\pi_A^d-\pi_A^u}{\tau}
=
-\frac{2(1-x_0)(s+x_0+2)}9<0,
\]
and
\[
\frac{\pi_B^d-\pi_B^u}{\tau}
=
\frac{(1-x_0)(13s+10x_0-13)}9.
\]
The latter may change sign for sufficiently high switching costs; unlike the weak Result-4 region, such points can coexist with the corrected pure-uniform domain.

### Social welfare

For every selected member of the strong-HBP zero-sales family,
\[
W^d-W^u
=
-\frac{\tau(1-x_0)(1-x_0+2s)}9.
\]
For the economically nondegenerate domain \(x_0<1\), this is strictly negative. At the degenerate limit \(x_0=1\), it is zero.

Thus Result 7 survives on the corrected pure-equilibrium domain and is robust to the strong-HBP below-cost price-selection family.

## 6. Accepted-manuscript Results 1–7 impact ledger

| Accepted-manuscript result | Depends on Eq. (12)? | Other issue | Corrected status |
|---|---:|---|---|
| **Result 1** — if \(\sigma>\tau\), history-based poaching ceases | No | lies outside the maintained Assumption-1 domain \(\sigma<\tau\) used for the reassessment | **OUTSIDE MAINTAINED DOMAIN / NOT AFFECTED BY UPE CORRECTION** |
| **Result 2** — dominant firm's share is larger under uniform pricing | Yes | displayed weak-branch difference is wrong; correct weak difference is \((2x_0+s-1)/6\) | **QUALITATIVE SIGN SURVIVES; EQUILIBRIUM CLAIM RESTRICTED TO \(x_0\ge x_H\)** |
| **Result 3** — weak-HBP CS is higher iff condition (17) | Yes | Eq. (13) branch ordering + Eq. (15) algebra | **INVALIDATED AS STATED**; primitive CS gives \(CS^d>CS^u\) throughout weak profile domain; equilibrium comparison only on pure overlap |
| **Result 4** — smaller firm benefits from HBP iff switching cost is high enough | Yes | high-\(s\) benefit region is outside the corrected weak pure-equilibrium overlap | **INVALIDATED AS AN EQUILIBRIUM CLAIM**; on every weak-domain pure-equilibrium comparison, \(\pi_B^d<\pi_B^u\) |
| **Result 5** — weak-dominance social welfare is higher under uniform pricing | Yes | accepted endpoint substitution is algebraically wrong and branch qualification is needed | **SURVIVES ON RESTRICTED PURE-EQUILIBRIUM DOMAIN** |
| **Result 6** — strong-dominance CS can be lower under HBP above a threshold | Yes | depends on strong-HBP price selection if below-cost prices are allowed | **SURVIVES ON CORRECTED PURE DOMAIN UNDER SOURCE/NONNEGATIVE-MARGIN HBP SELECTION** |
| **Result 7** — strong-dominance social welfare is higher under uniform pricing | Yes | strictness fails only at degenerate \(x_0=1\); HBP price selection changes transfers but not W | **SURVIVES ON CORRECTED PURE DOMAIN; SELECTION-INVARIANT WELFARE** |

## 7. Market-share correction corresponding to Result 2

The weak-HBP share is
\[
m_{1A}=\frac{2-x_0}{3}.
\]
On the uniform switching branch,
\[
x_1^u=\frac12+\frac{s}{6}.
\]
Therefore
\[
x_1^u-m_{1A}
=
\frac{2x_0+s-1}{6}>0.
\]

The accepted manuscript instead displays \((1-x_0)/3\) in the weak comparison. That expression is the difference between the uniform share and the **strong-HBP** source share. The qualitative ordering survives; the displayed weak formula does not.

## 8. No welfare extrapolation into the no-pure region

For
\[
1/2<x_0<x_H(s),
\]
this project assigns no pure-equilibrium uniform:

* profit,
* consumer surplus,
* social welfare,
* market-share comparison.

The accepted Eq. (12) vector may be evaluated there only as a counterfactual profile. Mixed pricing is not solved.

## 9. Stage-7 verdict

**GO.** The downstream impact is now source-faithful and equilibrium-domain-correct.

The most material changes are:

1. the weak-dominance pure-equilibrium comparison exists only for \(s<s_c\approx0.1334\);
2. the accepted Result-3 weak CS reversal disappears;
3. the accepted Result-4 small-firm HBP-profit region disappears as a pure-equilibrium comparison;
4. weak and strong social-welfare signs survive on the corrected pure domains;
5. strong CS Result 6 survives only with its equilibrium-domain and HBP-selection qualifications.

All subsequent manuscript language must use these corrected classifications.
