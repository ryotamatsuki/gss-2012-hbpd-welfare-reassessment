# Primitive welfare accounting and provisional impact on Results 1–5

**Status:** Clean-room algebra / exact regressions; not frozen. Every statement about the 2012 publication remains conditional on VOR comparison.

## 1. Accounting identity

With full coverage and one unit purchased by every consumer,

\[
W=CS+\pi_A+\pi_B=\beta-c-\tau\int_0^1 |z-y(z)|\,dz-\sigma N_{sw},
\]

where (y(z)\in\{0,1}) is the chosen firm and (N_{sw}) is the mass of consumers switching from their inherited firm. Prices are transfers; transportation and switching costs are real social costs. This identity is checked against the direct CS and profit functions in the clean-room code.

## 2. Uniform candidate allocation branches

For the source price candidate, define (s=\sigma/\tau) and (x_u=1/2+s/6).

* If (x_0\ge x_u), A-history consumers in ((x_u,x_0]) switch to B; B-history consumers stay with B. Then A's actual share is (x_u).
* If (x_0<x_u), neither history segment switches. The actual shares are (x_0) and (1-x_0), not (x_u) and (1-x_u).

The pure-equilibrium theorem candidate requires (x_0\ge x_H(s)>x_u) for every (0<s<1), so all uniform **equilibrium** comparisons use the first branch. Formula comparisons outside that region are only counterfactual source-profile comparisons.

On the no-switch branch the source price profile's actual profits are

\[
\pi_A^u=\tau(1+s/3)x_0,\qquad
\pi_B^u=\tau(1-s/3)(1-x_0),
\]

and (W^u=\beta-c-\tau[x_0^2+(1-x_0)^2]/2). The source switching-branch formulas for uniform profits and welfare do not apply there.

## 3. Result 1 — dominant-firm share

The weak-HBP share from Eq. (7) is (m_A^d=(2-x_0)/3). On the uniform switching branch the actual uniform share is (x_u), so

\[
x_u-m_A^d=\frac{2x_0+s-1}{6}>0\qquad(x_0>1/2).
\]

This differs from the HECER text's displayed ((1-x_0)/3), which is the difference between (x_u) and the strong-HBP share (x_1^A=(2x_0+1+s)/6). The qualitative ordering remains positive in the weak and strong profile comparisons. Where the uniform pure equilibrium fails, this is only a profile comparison, not an equilibrium comparison.

## 4. Result 2 — weak-branch consumer surplus

The direct CS differences are in `consumer_surplus_primitive_reconstruction.md`. On (x_0<x_u),

\[
CS^d-CS^u=\frac{\tau[(1-s)(7-s)+\text{a strictly positive increase in }x_0]}{18}>0.
\]

More explicitly the numerator is (s^2+12sx_0-14s-8x_0^2+8x_0+5), with derivative (12s+8-16x_0>0) for (1/2<x_0<x_u), and at (x_0=1/2) it equals ((1-s)(7-s)>0).

On (x_0\ge x_u), the corrected switching-branch difference is concave in (x_0), agrees with the no-switch branch at (x_u), and at the weak endpoint ̅(x_0=(3-s)/4) equals ((1+s)(43-45s)/144>0) whenever that branch reaches the endpoint ((s\le3/5)). Hence direct profile integration gives (CS^d>CS^u) throughout the weak-dominance parameter domain. The HECER Eq. (15)/Result 2 sign reversal does not survive the primitive branch-correct calculation.

This is equilibrium CS ordering only where (x_0\ge x_H(s)); outside it the uniform candidate is not a pure equilibrium. The upstream claimed negative exact value at ((s,x_0)=(.99,.501)) is a branch extension error. A valid-branch exact point ((.1,.7)) confirms that the printed Eq. (15) also has an independent sign/algebra error, although the gap remains positive there.

## 5. Result 3 — weak-branch social welfare

Primitive welfare accounting gives

\[
W^d-W^u=
\begin{cases}
\displaystyle \frac{\tau[28x_0^2-28x_0+5+2s(18x_0-13)+5s^2]}{36},&x_0\ge x_u,\\[.7em]
\displaystyle \frac{\tau[5s^2-4s+32x_0^2-32x_0+7]}{18},&x_0<x_u.
\end{cases}
\]

Both branches increase with (x_0>1/2) and agree at (x_u). If (s\le3/5), the weak endpoint ̅(x_0) is on the switching branch and its value is (-\tau(1+s)(1+9s)/144<0). If (s>3/5), the weak endpoint lies on the no-switch branch and its value is (\tau(s-1)(7s-1)/18<0). Thus Result 3's sign survives in profile accounting. The HECER endpoint substitution (-\tau(9s^2+10s-1)/144) is false; its sign argument is not reliable for small (s). On the pure-equilibrium overlap, (s\le -3+6\sqrt{33}/11<3/5), so the corrected switching-branch formula applies and uniform equilibrium welfare is higher.

## 6. Result 4 — strong-branch consumer surplus

For the source strong-HBP profile (q_A=c), direct integration gives

\[
CS^d-CS^u=
\begin{cases}
\displaystyle \frac{\tau(1-x_0)(16-7x_0-13s)}9,&x_0\ge x_u,\\[.7em]
\displaystyle \frac{\tau[s^2+40sx_0-46s+64x_0^2-128x_0+73]}{36},&x_0<x_u.
\end{cases}
\]

The first branch is Eq. (25) and is the only branch relevant to a uniform pure equilibrium, because (x_0\ge x_H(s)>x_u). On the strong-dominance domain with (s>3/5), however, there are parameters ̅(x_0\le x_0<x_u) where the second branch applies. At the exact profile ((s,x_0)=(99/100,51/100)), the direct gap is (1/14400>0), whereas Eq. (25) gives (-539/22500). This is a profile-level sign reversal; it is not an equilibrium welfare comparison because (x_0<x_H(s)). Therefore Result 4 must be restricted to the corrected uniform pure-equilibrium domain for an equilibrium interpretation.

## 7. Result 5 — strong-branch social welfare

Direct resource-cost accounting yields

\[
W^d-W^u=
\begin{cases}
-\displaystyle\frac{\tau(1-x_0)(1-x_0+2s)}9,&x_0\ge x_u,\\[.7em]
-\displaystyle\frac{\tau[5(1+s)-8x_0](4x_0-1-s)}{36},&x_0<x_u.
\end{cases}
\]

The no-switch branch occurs in strong dominance only when (s>3/5) and ̅(x_0\le x_0<x_u); both bracketed factors are positive there, so Result 5's sign survives. Eq. (28) is not the correct profile formula in that no-switch region. As an equilibrium welfare claim, the comparison is again restricted to (x_0\ge x_H(s)>x_u), where Eq. (28) applies.

## 8. Mixed equilibrium and HBP selection

No pure-uniform-equilibrium region is assigned an equilibrium CS, profit, or welfare value. Mixed pricing remains uncharacterized. The strong HBP (q_A=c) source profile survives under (p_i\ge c); if below-cost prices are admissible, a separate zero-sales price-selection family affects CS and firm profits while leaving (W) unchanged. See code regressions and the Stage 4 progress report.
