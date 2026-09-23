# Stage 4A — Independent mathematical adversarial certificate

**Verdict:** PASS  
**Certified claim:** complete **pure-strategy** uniform-price Nash correspondence UPE-2012-1  
**Not certified here:** mixed-strategy equilibrium; full proof-assistant core (mandatory at Stage 7.5A); exact Springer VOR equation text.  
**Source scope:** accepted manuscript / post-referee version.

## 1. Independence architecture

The certification deliberately uses two paths.

### Production analytic path

\`derivations/uniform_price_game_full_demand.md\` and
\`derivations/uniform_price_global_best_responses.md\` derive the five demand regimes in price-difference space and solve each firm's piecewise global maximization.

### Independent clean-room path

\`code/uniform_game_cleanroom.py\` reconstructs each history group's consumer choice directly from primitive utility thresholds and clipping. Its unilateral best-response evaluator does **not** call the production five-piece share formula. For a deviating firm's price, it obtains candidate breakpoints by making primitive thresholds hit history-segment endpoints, reconstructs the direct clipped demand between those knots, and evaluates every feasible endpoint and quadratic vertex using exact rational arithmetic.

The independent path therefore does not inherit the production branch labels or its best-response algebra.

## 2. Claim certified

For
\[
x_0\in(1/2,1],\qquad s=\sigma/\tau\in[0,1),
\]
the complete pure uniform-price correspondence is

\[
\mathcal E^u(x_0,s)=
\begin{cases}
\{(1,1)\},&s=0,\\[.4em]
\{(1+s/3,1-s/3)\},&0<s<1,\ x_0\ge x_H(s),\\[.4em]
\varnothing,&0<s<1,\ 1/2<x_0<x_H(s),
\end{cases}
\]
in normalized margins, with
\[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

For \(0<s<1\), the equilibrium set is a singleton at \(x_0=x_H(s)\), although firm B has a second payoff-equal action against A's equilibrium price.

The claim is **not** “there is no Nash equilibrium” below \(x_H\); only pure-strategy nonexistence is certified.

## 3. Candidate-deviation audit (D1)

Against the source candidate, the independent evaluator enumerates every unilateral clipping interval and its exact quadratic/affine maximum.

### Firm A

For \(x>x_u=1/2+s/6\), A's source action is its unique lower-switching optimum. Its best plateau boundary is strictly worse by
\[
2(x-x_u)^2.
\]
The reverse-switch branch is decreasing over its feasible interval because its vertex lies below that interval. Capture/zero-demand alternatives give no improvement.

### Firm B

The only globally competitive alternative to B's source action is the no-poaching plateau kink. Exact subtraction factors as
\[
2(x-x_L)(x-x_H),
\]
with \(x_L<1/2\). Hence the source action survives all unilateral deviations iff \(x\ge x_H\).

At the exact counterexample
\[
(s,x)=(1/2,3/5),
\]
the independent primitive evaluator reproduces the source profit \(25/72\), the kink-deviation profit \(56/75\), and the strict gain \(719/1800\).

**D1 state: PASS.**

## 4. Alternative-equilibrium / multiplicity audit (D2)

Every pure profile must fall into one of the five primitive demand pieces or their four boundaries.

* full B capture: excluded by profitable entry or by the capturing firm's escape from a negative margin;
* lower switching interior: local optimality uniquely gives the source profile;
* lower plateau kink \(d=\alpha\): B has a strict same-share price increase;
* plateau interior: a firm has a strict same-share price increase;
* upper plateau kink \(d=\beta\): A has a strict same-share price increase;
* upper switching interior: FOC intersection requires \(x<1/2-s/6\), incompatible with \(x>1/2\);
* full A capture: symmetric exclusion argument;
* zero margin: a sufficiently small positive price increase is profitable when demand is positive; zero demand reduces to capture;
* negative margin with positive demand: charging cost is strictly better.

This is an exhaustive pure-strategy partition. No additional pure branch remains below \(x_H\).

**D2 state: PASS — UNIQUE where a pure equilibrium exists; EMPTY below \(x_H\).**

## 5. Indifference / zero-payoff trigger audit (D3)

### Equality \(x=x_H\)

B is indifferent between its source action and the no-poaching kink. The audit changes B's action to that payoff-equal kink and recomputes A's best response. A can raise its margin by \(2s\), keep share \(x\), and gain \(2sx>0\). Therefore the payoff-equal B action does not generate a second Nash profile.

### Capture / zero demand

Zero-demand actions were varied rather than dismissed. They either admit positive-margin entry by the excluded firm or force the capturing firm to improve away from a negative margin.

### Strong-HBP zero-sale family

The separate HBP game has a genuine indifference trigger if below-cost poaching prices are permitted. On the strong branch,
\[
3-s-4x\le u=(q_A-c)/\tau\le0
\]
supports a payoff-equivalent zero-sales family with
\[
(p_B-c)/\tau=u+2x-1+s.
\]
Changing \(u\) changes prices, consumer surplus, and profit distribution but not allocation or social welfare. Under a nonnegative-margin/no-loss restriction the family collapses to the source member \(u=0\).

This HBP selection issue is retained explicitly; it is not used to manufacture a uniform-price equilibrium.

**D3 state: PASS.**

## 6. Strategy-domain audit

The accepted manuscript does not explicitly state a lower price bound in the inspected model text. The uniform pure-equilibrium theorem is invariant between unrestricted real prices and \(p_i\ge c\) because every pure equilibrium is endogenously forced to have positive margins and positive demand.

This robustness does **not** automatically extend to the strong-HBP price vector: below-cost poaching prices generate the zero-sales family described above. Therefore all source-specific HBP consumer-surplus/profit claims must either use a documented nonnegative-margin convention or state the selection dependence. Strong-HBP social welfare is invariant across that family.

**Strategy-domain state: PASS with an explicit HBP selection qualification.**

## 7. Boundary-targeted attacks

The production proof and independent evaluator have attacked:

* \(x\downarrow1/2\);
* \(x\uparrow1\) and the zero-measure B-history limit;
* \(s\downarrow0\);
* \(s\uparrow1\) from below;
* \(x=x_u\);
* \(x=x_H\);
* \(x=\bar x=(3-s)/4\);
* each price-difference boundary \(L,\alpha,\beta,U\);
* both sides of every clipping boundary;
* full capture by either firm;
* zero margin;
* negative margins;
* large positive prices and zero-demand tails;
* consumer ties;
* history segment disappearance;
* exact rational points above and below \(x_H\).

The exact evaluator uses \`Fraction\` arithmetic; floating-point grid evidence is not used as a proof.

## 8. Exact-regression inventory

Permanent regressions in \`code/uniform_game_cleanroom.py\` include:

1. demand-piece vs direct-clipping equality at all regime boundaries;
2. accepted-version Eq. (12) counterexample \((1,1/2,3/5,0)\);
3. rational points on both sides of the \(x_H\) inequality;
4. exact equality witness \(s=6/47,\ x=67/94=x_H(s)\);
5. B's two best responses at equality and A's strict deviation from the kink profile;
6. rejected upstream CS-sign regression at \(s=99/100,x=501/1000\);
7. a valid one-way-switch Eq. (15) discrepancy point;
8. weak-welfare endpoint identities;
9. strong-HBP below-cost selection family;
10. strong-branch CS/welfare profile regressions.

## 9. Formal-verification applicability

**APPLICABLE.** The project is a published-result correction involving a square-root threshold, exact inequalities, piecewise demand, equality logic, and welfare identities.

Stage 4A records the target map; Stage 7.5A must close it with a compiled Lean 4/mathlib certificate, statement-fidelity audit, no-\`sorry\`/\`admit\` audit, and toolchain provenance.

Formal verification is deliberately not counted as the independent Stage-4A path.

## 10. Surviving limitations

1. The theorem is pure-strategy only; mixed pricing below \(x_H\) is unresolved and outside the selected paper architecture.
2. Exact typeset VOR mathematics is not directly inspected; source-facing language remains accepted-manuscript-qualified.
3. Strong-HBP CS/profit comparisons depend on the price-domain/selection convention if below-cost poaching prices are allowed.
4. Formal proof-assistant certification remains a mandatory downstream gate.

None of these limitations invalidates the certified pure correspondence.

## Stage-4A gate

**PASS / GO to Stage 6 after the mixed-scope decision is frozen.**

Evidence chain:

\`UPE-2012-1 -> exhaustive global-deviation + alternative-equilibrium + indifference attacks -> production derivations + independently coded primitive evaluator + exact regressions -> pure-only / accepted-manuscript / HBP-selection limitations explicit\`.
