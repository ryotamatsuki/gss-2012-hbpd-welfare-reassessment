# Stage 4A — Independent mathematical adversarial certificate (in progress)

**Verdict:** OPEN / CONDITIONAL. This file records an independent attack path; it does not claim canonical Stage 4A PASS.

## Headline proposition under review

For (0<s=\sigma/\tau<1), (1/2<x=x_0<1), and price strategies containing (p_i=c) and every (p_i>c), the provisional pure-strategy correspondence is

\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&x<x_H(s),
\end{cases}
\quad x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

The claim concerns pure strategies only. Mixed equilibrium is not characterized.

## Production analytic path

`derivations/uniform_price_game_full_demand.md` derives the clipped demand from the two history-specific primitive thresholds. It enumerates full capture, A-to-B-only switching, no-switch plateau, B-to-A-only switching, and the threshold equalities.

`derivations/uniform_price_global_best_responses.md` uses price difference (d=b-a) as a separate proof path. It writes each firm's payoff on every demand piece, locates the concave-quadratic vertices, excludes capture/plateau/kink cases, derives both smooth-branch intersections, and checks the remaining global deviation to the no-poaching kink. The candidate boundary follows from an exact factorization, not from a numerical plot.

## Independent computational path

`code/uniform_game_cleanroom.py` contains:

* `share_a_direct`: computes market shares by clipping the two primitive utility thresholds to their own history intervals;
* `share_a_piecewise`: a separately coded five-regime expression used only for cross-checks;
* `direct_best_response_candidates`: forms unilateral price breakpoints from primitive threshold/end-point equalities, reconstructs direct clipped demand on each interval, and evaluates every feasible interval vertex and endpoint with exact rational arithmetic.

The direct maximizer does not call `share_a_piecewise`. Its finite candidate set follows because demand is affine between adjacent primitive clipping boundaries, so profit is quadratic there; after the final boundary the deviator's demand is zero. This argument, rather than any grid search, underlies the best-response candidate enumeration.

## Adversarial cases already exercised

* exact regime-crossing counterexample ((s,x)=(1/2,3/5)), including exact gain (719/1800);
* exact equality point (s=6/47, x=67/94=x_H(s)), with source-price and no-poaching-kink B best responses, and a strict A deviation from the kink profile;
* rational points immediately below the same equality boundary;
* deterministic rational parameter sweep over (s\in\{1/20,1/10,1/2,9/10\}) and (x\in\{51/100,3/5,7/10,9/10,99/100\}), checking source best responses in the candidate domain and a profitable kink/plateau deviation outside it;
* clipping boundaries and ε-neighborhoods at full capture, switching, and plateau thresholds;
* (x\downarrow1/2), (x\uparrow1), (s\downarrow0), (s\uparrow1), equality plateaus, zero margins, and disappearing history segments in direct-demand checks.
* strong-dominance CS regression at (s=99/100,x=51/100\), where the no-switch profile gap is (1/14400), while Eq. (25) gives (-539/22500); the same point is explicitly rejected as an equilibrium comparison because (x<x_H(s)).

The wider provisional Results 1–5 impact map, including corrected no-switch welfare branches for Results 3 and 5, is recorded in `derivations/welfare_and_result_impact.md`. These branch formulas do not change the pure-equilibrium theorem candidate because its domain satisfies (x\ge x_H(s)>x_u).

All arithmetic regressions pass under `python code/uniform_game_cleanroom.py` (Python 3.12.14). These checks are adversarial regression evidence only; they do not replace the analytic correspondence proof.

## Strategy-domain attack

The negative-margin reduction is recorded in the full-demand derivation. A firm with positive demand and a below-cost price can set (p_i=c) for zero profit. Full capture cannot be an equilibrium: if the winning firm has a nonnegative margin, the excluded firm can choose a positive margin just inside its demand threshold; if the winning margin is negative, it can instead move to cost. This reduction still needs a line-by-line independent review for all capture-boundary equalities.

## Remaining certification obligations

1. Have the exhaustive price-difference proof checked line by line against every boundary and feasible-set endpoint.
2. Prove the negative-margin reduction under the exact source strategy space, including the source's unspecified price constraints.
3. Add a Lean 4/mathlib certificate for (x_H), the payoff factorization, equality logic, and exact counterexample. The current environment has neither `lean` nor `lake`; no formal verification pass is claimed.
4. Reconcile the theorem and every notation/quantifier with the version-qualified source text after VOR comparison.

Until these are closed, the candidate theorem must remain “provisional pure-strategy characterization under independent review,” not a certified complete equilibrium claim.
