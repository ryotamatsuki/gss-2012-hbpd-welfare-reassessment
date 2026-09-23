# Stage 7.5A — Quantifier, Portability, and Scope Red-Team

**Status:** IN PROGRESS pending Formal Verification Gate.  
**Economic scope verdict:** PASS.  
**Portability classification:** MODEL-SPECIFIC.  
**Formal-verification state:** APPLICABLE; build certificate required before this Stage can close.

## 1. Headline quantifier ledger

### UPE-2012-1 — complete pure uniform-price correspondence

For every
\[
\tau>0,\quad c\in\mathbb R,\quad x_0\in(1/2,1],\quad 0\le \sigma<\tau,
\]
under the original full-coverage inherited-history Hotelling model and price strategy spaces containing all \(p_i\ge c\) (or all real prices), define \(s=\sigma/\tau\).

- if \(s=0\): unique pure equilibrium in normalized margins is \((1,1)\);
- if \(0<s<1\): unique pure equilibrium exists iff \(x_0\ge x_H(s)\), and equals \((1+s/3,1-s/3)\);
- if \(1/2<x_0<x_H(s)\): the **pure-strategy** equilibrium set is empty.

No mixed-strategy quantifier is asserted.

### CS-2012-W — weak-HBP consumer surplus

The branch-correct primitive profile comparison is defined throughout the accepted weak-HBP profile domain. It is an **equilibrium comparison** only where the uniform pure equilibrium exists.

Maximum defensible statement:

> Under weak HBP, direct primitive integration yields higher consumer surplus than the accepted uniform-price profile throughout the source weak-dominance profile domain; as an equilibrium comparison, this statement is restricted to the corrected pure-overlap domain.

### W-2012-W — weak social welfare

On the weak-HBP / pure-uniform overlap,
\[
W^d<W^u.
\]
Outside the uniform pure-existence domain, only counterfactual profile accounting is permitted.

### CS-2012-S — strong-HBP consumer surplus

Result depends on the strong-HBP price selection if below-cost poaching prices are admissible. Under the source/nonnegative-margin member \(q_A=c\), the accepted threshold survives on the corrected pure-uniform domain.

### W-2012-S — strong social welfare

On the corrected pure domain,
\[
W^d-W^u=-\frac{\tau(1-x_0)(1-x_0+2s)}9\le0,
\]
strict for \(x_0<1\). This welfare result is invariant across the documented strong-HBP zero-sales price family.

## 2. Assumption classification

| Assumption | Type | Role |
|---|---|---|
| Hotelling line, firms at endpoints | model-defining | generates linear location utility differences and five-piece demand |
| inherited history split \(x_0\) | model-defining | creates asymmetric captive/poachable segments |
| linear transport cost \(\tau>0\) | functional-form | carries exact closed form \(x_H\) |
| switching cost \(\sigma\) | economic | creates gap between history-specific thresholds |
| \(0\le\sigma<\tau\) | parameter/source restriction | maintained source domain |
| full coverage | economic/model-defining | removes outside-option participation margins |
| common marginal cost \(c\) | economic but translation-invariant | shifts both prices without changing normalized game |
| pure-strategy equilibrium | scope restriction | headline correspondence only |
| nonnegative margin for strong-HBP source selection | selection convention | needed for selection-free CS/profit statement on strong HBP; not needed for uniform UPE theorem |

## 3. Pre-specified portability/falsification tests

These tests were specified by the project brief before Stage 7.5A.

### P1 — common marginal-cost translation

Replace \(c=0\) normalization by arbitrary common \(c\).

Success criterion: equilibrium margins, demand regimes, \(x_H\), and all real-resource welfare statements are unchanged after adding \(c\) back to both firms' prices.

Result: **SURVIVES.**

Reason: consumer choice depends on price differences; profits use net margins; normalization \(a=(p_A-c)/\tau,b=(p_B-c)/\tau\) is bijective for fixed \(\tau>0\).

### P2 — transport-scale normalization

Do not normalize \(\tau\) to one.

Success criterion: the game reduces exactly to normalized variables \(a,b,s=\sigma/\tau\), with equilibrium prices
\[
p_A=c+\tau+\sigma/3,\qquad p_B=c+\tau-\sigma/3
\]
and the same dimensionless \(x_H(\sigma/\tau)\).

Result: **SURVIVES.**

### P3 — price-level versus price-difference representation

Solve allocation in \(d=(p_B-p_A)/\tau\) rather than separate price levels.

Success criterion: the direct primitive clipped share and five-piece demand partition agree identically.

Result: **SURVIVES.** This is already cross-checked by separate direct-clipping and piecewise evaluators.

### P4 — consumer tie convention

Alter allocation of consumers exactly indifferent at history-specific thresholds.

Success criterion: market shares, profits, equilibrium conditions, and welfare are unchanged because the indifferent set has Lebesgue measure zero.

Result: **SURVIVES** on the continuum model.

### P5 — equality boundary

Retain exact \(x_0=x_H(s)\) rather than treating it numerically.

Success criterion: B's second payoff-equal kink action does not generate a second Nash profile.

Result: **SURVIVES.** A strictly profitable A deviation of size \(2sx_0\) eliminates the kink profile.

## 4. Why no alternative demand microfoundation is introduced here

The headline theorem is not presented as more than model-specific. Under v2.4, a new quadratic-transport, outside-option, heterogeneous-switching-cost, or altered-timing model would be a substantive model change rather than a required portability test for the claim actually made.

Introducing such a model solely to seek broader generality would violate the Stage-7.5 stop rule against research creep.

Therefore the correct classification is not “portable because five normalization tests survived.” It is:

**MODEL-SPECIFIC, with verified invariance to cost/scale/coordinate/tie conventions.**

## 5. Contribution Robustness Certificate

| Claim | Mechanism invariant | Tests | Result | Classification | Maximum defensible wording |
|---|---|---|---|---|---|
| UPE-2012-1 | global best response must compare the smooth switching optimum with the no-poaching kink | P1–P5 | survives all representation/boundary tests | MODEL-SPECIFIC | complete pure-strategy correspondence in the GSS inherited-history Hotelling benchmark |
| weak CS correction | primitive utility must be integrated on the actual clipped allocation branch | branch/cutoff audit + P1/P2/P4 | survives | MODEL-SPECIFIC | accepted weak-CS formula/result requires correction in this model |
| weak welfare | real transport/switching cost comparison on certified pure overlap | P1/P2/P4 | survives | MODEL-SPECIFIC | uniform pricing yields higher welfare on the corrected weak pure-overlap domain |
| strong CS | source strong-HBP price selection plus corrected uniform pure domain | strategy-domain selection attack | selection-dependent if below-cost prices allowed | CONDITIONALLY PORTABLE WITHIN MODEL / manuscript label: MODEL-SPECIFIC WITH SELECTION CONDITION | Result 6 survives under source/nonnegative-margin HBP selection |
| strong welfare | allocation/resource-cost comparison | below-cost HBP family attack + P1/P2/P4 | selection-invariant | MODEL-SPECIFIC | Result 7 survives on corrected pure domain; equality only at \(x_0=1\) |

For the workflow's required single classification, the paper's headline contribution is **MODEL-SPECIFIC**.

## 6. Prohibited stronger claims

Do not write:

- “switching-cost Bertrand games have no pure equilibrium below this threshold”;
- “the threshold is generic”;
- “the result is robust to alternative spatial demand systems”;
- “no Nash equilibrium exists below \(x_H\)”;
- “welfare is corrected for the entire parameter space”;
- “Lean formally verifies the whole economic model” unless demand, strategy space, and Nash definition are actually encoded.

## 7. Formal-verification handoff

The Stage-4A target map remains current. Stage 7.5A can close only after a reproducible Lean 4/mathlib build certifies the selected algebraic/inequality core, with statement-fidelity and placeholder/axiom audits.

Until then:

**Stage 7.5A verdict = CONDITIONAL / FORMAL VERIFICATION BLOCKER ONLY.**
