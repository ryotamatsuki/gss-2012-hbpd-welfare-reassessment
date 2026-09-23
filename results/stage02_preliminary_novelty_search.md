# Stage 2 — Preliminary novelty-search log (2026-09-23)

**Status: IN PROGRESS — no novelty clearance or kill-gate verdict.** This records a first targeted web-search block only. A search result list is not proof that no correction, reply, prior theorem, or unindexed working paper exists.

## Search boundary

Target work: Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI [10.1007/s10842-011-0111-8](https://doi.org/10.1007/s10842-011-0111-8).

The separate 2011 *European Economic Review* article, “History-based Price Discrimination and Entry in Markets with Switching Costs: A Welfare Analysis,” DOI [10.1016/j.euroecorev.2010.09.001](https://doi.org/10.1016/j.euroecorev.2010.09.001), is treated only as a distinct related paper. Its entrant does not observe consumers’ histories; its results have not been transferred to the 2012 model.

## Search block

Access date: 2026-09-23. Search engines: web search system 2 and system 1. Queries below are recorded as submitted; system 1 indicated that it normalized some queries, so its results are discovery leads rather than exact-query coverage.

### Exact-title / DOI correction searches

- System 2: `"A Welfare Evaluation of History-Based Price Discrimination" correction OR erratum OR corrigendum OR comment OR reply`
- System 2: `"10.1007/s10842-011-0111-8" correction OR erratum OR corrigendum OR comment`
- System 2: `"A Welfare Evaluation of History-Based Price Discrimination" "Eq. (12)" OR "Result 2"`
- System 1: `"A Welfare Evaluation of History-Based Price Discrimination" correction OR erratum OR corrigendum OR comment OR reply`
- System 1: `"10.1007/s10842-011-0111-8" "erratum" OR "correction"`

No result in this search block identified a correction, corrigendum, comment, or author reply to the 2012 article. This is a preliminary negative search, not a claim that none exists. The results did rediscover the distinct 2011 GSS paper, the 2010 HECER author paper underlying the 2012 publication, and bibliographic records for the target.

### Related model / theorem-absorption searches

- System 2: `Gehrig Shy Stenbacka 2012 history based price discrimination later papers switching costs uniform prices`
- System 2: `switching costs Hotelling Bertrand pure strategy equilibrium nonexistence history based price discrimination asymmetric installed base`
- System 1: `Gehrig Shy Stenbacka 2012 history based price discrimination later papers switching costs uniform prices`
- System 1: `switching cost Hotelling asymmetric installed base pure strategy Bertrand equilibrium price discrimination paper`

## Discovery leads and initial model comparison

| Work surfaced | Primary record | Initial relation to the target | Status |
|---|---|---|---|
| Gehrig, Shy & Stenbacka (2011), “History-based Price Discrimination and Entry in Markets with Switching Costs: A Welfare Analysis” | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S001429211000084X) | Related HBP/switching-cost welfare paper, but the information structure has an entrant without access to purchase histories; it is not the 2012 uniform-pricing subgame. | Distinct project/model; compare claims, do not import results. |
| Gehrig, Shy & Stenbacka (2012), target | [Springer DOI page](https://link.springer.com/article/10.1007/s10842-011-0111-8); [HECER 2010 author-version record](https://helda.helsinki.fi/items/fed9830d-40bc-4521-b730-9ff7e36a39cb) | The HECER record exposes the July 2010 Discussion Paper No. 299. The Springer version-of-record body has not been obtained for equation-level comparison. | Source gate remains open. |
| “History-based versus uniform pricing in growing and declining markets” (2016) | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167718716300753) | Later GSS-related dynamic/overlapping-generations setting with Markov-perfect pricing; it cites the target but does not appear to be the same static inherited-segment price game. | Read the full source and references in Stage 2. |
| Colombo et al., “Imperfect history-based price discrimination with asymmetric market shares” (2024) | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167624524000143) | Later HBP work studies incomplete history information and asymmetric inherited shares; current abstract does not establish absorption of the target’s switching-cost, full-coverage uniform-price correspondence. | Obtain and compare full model/results. |
| Umezawa & Yamakawa, “The impact of switching costs on behavior-based price discrimination with multiple consumer types” (2025) | [Springer](https://link.springer.com/article/10.1007/s00712-025-00900-6) | Relevant switching-cost / behavior-based pricing paper. It uses a two-period Hotelling setup with multiple consumer types. Its price game and information/segment structure differ from the target; its equilibrium discussion is a lead for comparison, not an equivalent theorem. | Full theorem-by-theorem absorption check still required. |
| Klemperer, “Markets with Consumer Switching Costs” (1987) | [Article PDF copy](https://www.czaj.org/pub/teaching/IO/Markets%20with%20Consumer%20Switching%20Costs.pdf) | Foundational switching-cost analysis, but not a direct result for the target’s static Hotelling geometry and inherited A/B history intervals. | Check original publication and exact assumptions before relying on it. |
| Lambertini, “On Hotelling’s ‘stability in competition’ with network externalities and switching costs” (2013) | [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1435-5957.2012.00469.x) | Same broad ingredients, but introduces network externalities and studies a different Hotelling game. | Not an evident absorption result; retain as a boundary comparison. |

These first leads do not establish novelty. A shared label (“Hotelling,” “switching costs,” “history-based pricing”) is not enough either to absorb or distinguish the candidate theorem.

## Preliminary conclusion

- Exact-title/DOI searches did not surface a correction or reply in this block.
- The surfaced later HBP/switching-cost papers differ in at least one central element (dynamic entry/exit, multiple types, imperfect history information, or network effects). No theorem with the candidate threshold
  \[
  x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6
  \]
  was identified by these queries.
- This is not a “no prior result” conclusion. Stage 2 remains open pending citation-chain searches, reference-level searches, database checks, complete reading of closest papers, and a theorem-by-theorem comparison using the finalized Stage 4 statement.
- The current pure-equilibrium characterization is provisional. It must not be used to declare novelty until Stage 4/4A close.

## Next search tasks

1. Search publisher, Crossref, RePEc, Google Scholar/OpenAlex, SSRN, IDEAS, author pages, and journal contents for exact-title correction/comment/reply records and citations after 2012.
2. Build backward and forward citation lists for the target and HECER No. 299; classify each as same model, adjacent model, or unrelated.
3. Read the complete primary texts of the 2016, 2024, and 2025 closest leads and inspect their cited switching-cost / piecewise-price-game theorems.
4. Search exact theorem ingredients and algebraic threshold variants after the pure theorem is certified; record rejected candidates and reasons.
5. Re-run the novelty kill gate after any change in the headline theorem or paper scope.
