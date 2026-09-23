# Accepted-manuscript source comparison — GSS (2012)

**Record date:** 2026-09-23  
**Status:** authoritative post-referee source obtained; Version of Record body still not directly inspected.

## Source

A lawful institutional-repository copy hosted by Hanken/DHANKEN identifies itself on its first page as a **“personal version (author's manuscript as accepted for publishing after the review process but prior to final layout and copyediting)”** of:

Thomas Gehrig, Oz Shy, and Rune Stenbacka, “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393 (2012), DOI `10.1007/s10842-011-0111-8`.

Public bitstream:

`https://helda.helsinki.fi/server/api/core/bitstreams/6484e4b9-eeb4-4b72-ad79-99e2a817e16d/content`

No copyrighted PDF is committed to this repository. No local hash is recorded because the repository stores only provenance and equation/result mappings.

## Why this changes the source gate

The earlier source boundary relied on HECER Discussion Paper No. 299 (July 2010) for the complete mathematical body. The Hanken file is materially stronger provenance because it is explicitly post-referee and accepted for publication. It confirms that the disputed uniform-pricing and welfare statements survived peer review into the accepted manuscript.

It is still not the Springer typeset Version of Record. Accordingly, manuscript claims must use wording such as “the accepted manuscript states …” unless a VOR body is later inspected. Springer metadata, abstract, bibliographic data, and publication history have been verified separately.

## Key accepted-manuscript mappings

PDF page numbers below are the 35-page institutional PDF, zero ambiguity aside from the cover/front matter.

| Item | Accepted-manuscript location | Comparison / audit consequence |
|---|---:|---|
| Model / price definitions | PDF pp. 10–11 | Firms set loyalty prices `p_A,p_B` and poaching prices `q_A,q_B`; unit cost `c`; full coverage; no explicit price-floor statement is made in the inspected model passage. |
| Definition 1 | PDF p. 11 | Weak dominance: `1/2 < x_0 < (3τ-σ)/(4τ)`; strong dominance above that boundary. |
| Assumption 1 | PDF p. 14 | `σ<τ`. |
| Strong-HBP construction | PDF pp. 14–15 | Sets `q_A=c`; checks firm B's loyalty-price increase. This does not by itself specify a global price strategy domain. |
| Eq. (11) | PDF p. 16 | Uniform-pricing primitive utility. |
| Eq. (12) | PDF p. 16 | States `p_A^u=c+τ+σ/3`, `p_B^u=c+τ-σ/3`, `x_1^u=1/2+σ/(6τ)`, introduced as **the unique Nash–Bertrand equilibrium in prices**. This is the central global-equilibrium claim audited here. |
| Uniform/HBP share comparison | PDF p. 17 | Accepted manuscript prints `x_1^u-m_{1A}=(1-x_0)/3` immediately before Result 2; primitive reconstruction shows this is not the weak-HBP share difference. |
| Eqs. (13)–(15) | PDF pp. 19–20 | Eq. (13) integrates uniform CS over the one-way-switch allocation. Eq. (15) is algebraically correct on that branch and matches primitive integration. |
| Eqs. (16)–(17), Figure 5 | PDF p. 20 | Eq. (16) adds a global minus sign relative to the correctly normalized Eq. (15); the resulting condition (17)/Figure 5 reversal also extends the one-way-switch setup into a no-switch region. |
| Eqs. (23)–(25) | PDF pp. 24–25 | Weak-dominance welfare formulas and endpoint substitution; the displayed endpoint identity is algebraically inconsistent with direct substitution, while the welfare sign can survive on the correct branch. |
| Strong-dominance CS | PDF p. 26 | Result 6 gives the strong-HBP CS threshold. The formula is branch-sensitive because the source uniform profile can be on the no-switch plateau. |
| Strong-dominance welfare | PDF p. 28 | Result 7 states uniform pricing raises social welfare; branch-correct resource-cost accounting preserves the sign on the relevant branches, but equilibrium interpretation requires the corrected uniform pure-equilibrium domain. |
| Conclusion | PDF pp. 29–30 | Repeats the consumer-surplus and welfare policy conclusions; these require qualification wherever the uniform pure equilibrium does not exist. |

## Result numbering correction

The accepted manuscript contains **seven** numbered Results, not five. The source-facing impact ledger must therefore use the accepted-manuscript numbering:

1. **Result 1:** sufficiently high switching costs (`σ>τ`) eliminate profitable history-based poaching.
2. **Result 2:** the inherited dominant firm's equilibrium market share is larger under uniform pricing.
3. **Result 3:** weak-dominance consumer-surplus comparison based on condition (17).
4. **Result 4:** weak-dominance smaller-firm profit comparison.
5. **Result 5:** weak-dominance social welfare is higher under uniform pricing.
6. **Result 6:** strong-dominance consumer-surplus threshold.
7. **Result 7:** strong-dominance social welfare is higher under uniform pricing.

Earlier local notes that label the share/CS/welfare statements as “Results 1–5” are bookkeeping shorthand inherited from the upstream audit and must not be used in the manuscript.

## Surviving source discrepancies after accepted-manuscript comparison

The following issues are present in the accepted manuscript and therefore are **not** artifacts of the 2010 working-paper draft:

1. Eq. (12) is explicitly asserted to be the unique Nash–Bertrand equilibrium in prices, while the clean-room global best-response analysis finds an additional necessary restriction `x_0≥x_H(σ/τ)`.
2. The weak-HBP share-difference display before Result 2 does not equal the difference implied by the accepted manuscript's own equilibrium shares.
3. Eq. (15) is correct on its switching branch. The source inconsistency enters at Eq. (16), which is the sign-reversed normalization of Eq. (15), while the Result-3/Figure-5 analysis also fails to respect the no-switch branch when `x_0<x_u`.
4. The weak-welfare endpoint substitution following Eq. (25) retains the disputed algebraic identity.
5. Strong-dominance profile comparisons continue to use the uniform switching allocation without an explicit branch qualification.

These statements remain **accepted-manuscript claims** until the Springer VOR body is directly compared.

## VOR search outcome

Current Springer access exposes metadata, abstract, notes, references, and purchase/subscription routes but not the complete equation-level body in the present environment. RePEc likewise reports subscriber-restricted publisher full text. A direct VOR equation-by-equation comparison therefore remains unavailable.

Under the project’s fail-closed rule, the accepted manuscript is the controlling mathematical source for publication development, and all source-facing assertions are version-qualified. A later lawful VOR copy must be compared before any sentence is upgraded to “the published equation/result states …”.

## Gate consequence

The previous “working paper only” blocker is closed. Stage 1 can proceed on an accepted-manuscript-qualified basis. Direct VOR verification remains an explicit residual limitation, not an unstated assumption.


## Post-Astra source recertification

An independent post-Stage-14 audit identified that the project had mis-transcribed Eq. (15). The accepted-manuscript image was re-opened and the sequence Eqs. (13)–(17) was transcribed again from the PDF.

Canonical result:

- Eq. (15) matches the primitive switching-branch CS gap;
- at (s=1/10,x_0=7/10), both equal (221/720);
- printed Eq. (16) is the negative of the normalized Eq. (15);
- Result 3 remains invalid as stated because of that sign reversal and because the one-way-switch integral is not the realized allocation for (x_0<x_u).

The obsolete project value (1279/3600) is not a source value and must not appear as an accepted-manuscript formula.
