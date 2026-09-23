# Stage 4 — Global uniform-price game (progress report)

**Canonical status:** IN PROGRESS — provisional result; no Stage 4 GO and no Stage 4A PASS claimed.

## Input and scope

* Production repository: `ryotamatsuki/gss-2012-hbpd-welfare-reassessment`.
* Source branch: `research/stage-00-evidence-freeze` at `7c10043ad91f67505c68bf0f99f3b51263a041fb`.
* Work branch: `research/stage-04-uniform-price-game`, branched from the source branch above.
* Initial input commit: `7c10043ad91f67505c68bf0f99f3b51263a041fb`.
* Workflow repository: `ryotamatsuki/research-paper-workflow`, `main` at `63f11a50a13d9328213498a5a6576d00b9bceef7` (pipeline v2.4). `GOVERNANCE.md` still labels v2.3; follow the v2.4 pipeline and preserve this inconsistency in the workflow record.
* Mathematical source for this pass: HECER Discussion Paper No. 299 (July 2010), not yet the VOR body. See `sources/gss_2012_version_boundary.md`.

## Work completed in this block

1. Reconstructed uniform-price consumer choice directly from each history-specific primitive utility difference.
2. Derived the clipped demand correspondence with full capture, one-way switching, no-switch plateau, history-segment disappearance limits, and exact threshold equalities.
3. Wrote a provisional necessary-and-sufficient pure-equilibrium theorem for nonnegative net margins, with a price-domain reduction argument for unrestricted real prices.
4. Implemented separate primitive-clipping and piecewise-regime evaluators plus exact global unilateral best-response candidate enumeration on nonnegative margins.
5. Reproduced the Eq. (12) exact profitable kink deviation at ((\tau,\sigma,x_0,c)=(1,1/2,3/5,0)): gain (719/1800).
6. Integrated consumer surplus from primitive utility under clipped, history-specific thresholds and corrected the Eq. (15) audit's branch assignment.
7. Reproduced exact rational boundary, kink, welfare-endpoint, and HBP selection regressions in `code/uniform_game_cleanroom.py`.
8. Added a SymPy primitive-integration script that verifies weak/strong CS and welfare formulas on both sides of the uniform allocation cutoff.

## Provisional headline result

For (0<s=\sigma/\tau<1) and (x=x_0\in(1/2,1)), the candidate complete pure correspondence is

\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\}, &x\ge x_H(s),\\
\varnothing, & x<x_H(s),
\end{cases}
\quad
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

At equality B has a second best-response price at the no-poaching kink, but that price is not an equilibrium intersection. The Nash set remains a singleton. No mixed-strategy characterization or general-equilibrium nonexistence claim is made.

The primitive-threshold proof map is in `derivations/uniform_price_game_full_demand.md`; a second price-difference proof is in `derivations/uniform_price_global_best_responses.md`. The independent adversarial review and its exact-rational evaluator are documented in `results/stage04a_independent_certificate.md`. The key remaining gate is a line-by-line hostile check of all boundary and feasible-set endpoints.

## Consumer-surplus correction and regression audit

The source candidate's actual uniform allocation changes at (x_u=1/2+s/6). For (x_0<x_u), the actual allocation has no switching; the HECER Eq. (13) integral writes the switching cutoff above (x_0), so it cannot be integrated as though (x_u\le x_0). The direct actual-profile CS gap is therefore piecewise. On (x_0\ge x_u), the direct gap has the Eq. (15) switching-branch form with the σ-dependent terms reversed relative to the HECER display. On (x_0<x_u), a different no-switch formula applies.

The upstream “exact B” value ((s,x_0)=(99/100,501/1000)) is below (x_u) and below (x_H). Direct integration gives (17993/4500000>0), not the upstream claimed negative value. The displayed Eq. (15) is still false on the proper switching branch: at ((s,x_0)=(1/10,7/10)), direct integration gives (221/720), versus (1279/3600) from the printed formula. Both are positive, so this point does not establish a ranking reversal.

Further source-result audit found: (i) the weak-HBP Result 1 share difference implied by Eq. (7) is ((2x_0+s-1)/6), not the printed ((1-x_0)/3); the latter is the strong-HBP difference, while the qualitative sign survives; (ii) correct direct integration gives (CS^d>CS^u) throughout the weak-HBP profile domain, so the printed Result 2 sign reversal disappears; (iii) Eq. (25) and Result 4 require the switching branch (x_0\ge x_u). At the exact strong-branch profile ((s,x_0)=(99/100,51/100)), direct CS gives (1/14400), while Eq. (25) gives (-539/22500). This profile is outside the uniform pure-equilibrium domain, so it is not an equilibrium welfare reversal. Results 3 and 5 retain their welfare signs under the corrected no-switch branches; their printed profile formulas still need branch qualification.

## HBP branch note

The weak-HBP interior prices and strong-HBP (q_A=c) candidate have been reconstructed from history-segment demand. If prices below marginal cost are allowed, the strong-HBP game appears to have an additional bounded zero-sales price family; if (p_i\ge c), that family collapses to the source member. A positive markup at (q_A) is not an equilibrium because A can undercut and profitably poach. This issue is documented in the code regressions and must be reviewed before welfare selection statements are frozen.

## Commands and results

* `python code/uniform_game_cleanroom.py` — passed; output: `all exact clean-room checks passed`.
* `python code/symbolic_reconstruction.py` — passed; output: `all symbolic primitive welfare identities passed`.
* Arithmetic uses Python 3.12.14 standard-library `fractions.Fraction`; exact regression assertions avoid floating-point equality.
* The current environment has no `lean` or `lake` executable. Formal verification is applicable and remains open; these Python identities are not Lean certification.

## Not completed / blockers

* Stage 4A independent certification and hostile branch-enumeration proof remain open; a separate direct-clipping evaluator and d-coordinate proof are now in the branch.
* Direct VOR full-text comparison; all publication-facing discrepancy language remains version-qualified to HECER 2010.
* Full Eq. (1)–(28), Results 1–5, figures, assumptions, and version-difference ledgers as finalized Stage 1 artifacts; a provisional impact ledger is in `derivations/welfare_and_result_impact.md`.
* Literature correction/absorption search closure; the search to date is preliminary only.
* Mixed equilibrium; excluded from the current pure-strategy scope. No welfare result is extrapolated into the no-pure region.
* Lean formal verification and toolchain/audit certificate.

## Verdict and next-stage contract

Stage 4 remains **OPEN / CONDITIONAL**. Do not call the result a certified complete equilibrium correspondence yet. Next: complete the global branch proof independently, compare all price domains, formalize the algebraic core, then rerun the Stage 4A hostile audit. Only after these gates can the source-specific welfare-impact map be finalized.
