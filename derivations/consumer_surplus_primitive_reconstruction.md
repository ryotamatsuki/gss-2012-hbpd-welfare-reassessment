# Consumer surplus: direct integration and branch qualifications

**Status:** Exact symbolic identities and rational regressions reproduce locally; publication-level certification and VOR comparison remain open.

## 1. Primitive utility integration

Let (t_A=(p_B-p_A+\tau+\sigma)/(2\tau)) and (t_B=(p_B-p_A+\tau-\sigma)/(2\tau)). For uniform prices, direct utility integration uses the clipped cutoffs

\[
k_A=\min\{x_0,\max\{0,t_A\}\},\qquad
k_B=\min\{1,\max\{x_0,t_B\}\}.
\]

The four integrands, in location order, are

\[
\begin{array}{ll}
\beta-p_A-\tau z,&z\in[0,k_A],\\
\beta-p_B-\tau(1-z)-\sigma,&z\in[k_A,x_0],\\
\beta-p_A-\tau z-\sigma,&z\in[x_0,k_B],\\
\beta-p_B-\tau(1-z),&z\in[k_B,1].
\end{array}
\]

The cutoffs are clipped to their own history segments before integration. The code `uniform_cs_direct` implements these primitive integrals and does not substitute a paper formula.

For weak HBP, the independent history-specific cutoffs are

\[
x_1^A=\frac12+\frac{q_B-p_A+\sigma}{2\tau},\qquad
x_1^B=\frac12+\frac{p_B-q_A-\sigma}{2\tau},
\]

also clipped to ([0,x_0]) and ([x_0,1]). `hbp_cs_direct` integrates the four resulting utility segments directly.

## 2. Uniform candidate's two allocation branches

At the source uniform-price profile, (t_A=x_u=1/2+\sigma/(6\tau)). The relevant cutoff for B-history consumers is (t_B=1/2-5\sigma/(6\tau)<x_0). Hence:

* If (x_0\ge x_u), only A-history consumers in ((x_u,x_0]) switch to B.
* If (x_0<x_u), neither history segment switches; the inherited allocation remains (x_0) and (1-x_0).

The HECER 2010 text's Eq. (13) writes the first two integrals over ([0,x_u]) and ([x_u,x_0]), respectively. For (x_0<x_u), the second interval is reversed. The displayed expression cannot be used as the actual allocation's consumer surplus in that region without redoing the clipped primitive integral.

## 3. Direct weak-branch difference

For the source weak-HBP price profile and the source uniform-price profile, direct primitive integration gives

\[
CS^d-CS^u=
\begin{cases}
\displaystyle
\frac{-\tau^2(52x_0^2-52x_0-1)+2\sigma\tau(18x_0-17)+\sigma^2}{36\tau},
&x_0\ge x_u,\\[1.2em]
\displaystyle
\frac{\sigma^2+12\sigma\tau x_0-14\sigma\tau-8\tau^2x_0^2+8\tau^2x_0+5\tau^2}{18\tau},
&x_0<x_u.
\end{cases}
\]

The two expressions agree at (x_0=x_u). The first expression applies on the actual one-way-switch branch. Its σ-dependent terms differ in sign from those displayed in HECER Eq. (15). The second expression is required on the no-switch branch.

In dimensionless units τ=1, the direct regression point ((s,x_0)=(99/100,501/1000)) satisfies (x_0<x_u). Exact direct integration yields

\[
CS^d-CS^u=\frac{17993}{4500000}>0.
\]

The printed HECER Eq. (15), evaluated algebraically at the same values, is (1801513/2250000>0). The upstream negative value (-103039/4500000) equals neither actual direct integration nor the printed expression; it results from extending the one-way-switch correction outside its branch. This point also lies below the provisional pure-uniform-equilibrium threshold (x_H(s)), so it is not an equilibrium welfare comparison.

An exact point inside both the weak-HBP branch and the provisional pure-uniform-equilibrium domain is ((s,x_0)=(1/10,7/10)), where (x_u=31/60<x_0<29/40=\bar x_0) and (x_0>x_H(1/10)). Direct integration yields (221/720>0), while printed Eq. (15) yields (1279/3600>0). Thus the formula is numerically false even on a valid one-way-switch branch, but this certified point does not reverse the consumer-surplus ranking.

## 4. Scope

These calculations concern the two source price profiles as primitives. They are equilibrium welfare comparisons only where both profiles are equilibria. Where uniform pure equilibrium fails to exist, the uniform-profile surplus is a profile comparison, not equilibrium welfare. No mixed-equilibrium welfare claim is made.
