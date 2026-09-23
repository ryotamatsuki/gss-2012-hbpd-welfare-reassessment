# Stage 6 — Novelty re-kill and theorem-absorption audit

**Verdict:** GO  
**Frozen theorem tested:** UPE-2012-1  
**Search date:** 2026-09-23

## 1. Final theorem subjected to the kill test

The contribution tested here is not the generic statement that kinked Bertrand games can lack pure equilibria. It is the source-specific theorem:

\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&x<x_H(s),
\end{cases}
\]
for the GSS (2012) uniform-price subgame, with
\[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

The search also tests the associated correction that the accepted manuscript's Eq. (12) is a local one-way-switch branch solution whose global Nash interpretation requires the additional \(x_H\) restriction.

## 2. Direct correction / disclosure re-search

Fresh searches were run for:

* exact article title + correction / erratum / corrigendum / comment / reply;
* DOI \`10.1007/s10842-011-0111-8\` + correction terms;
* authors + uniform pricing + pure equilibrium / no pure equilibrium;
* fragments of the exact \(x_H\) expression;
* forward-citation records and later papers citing the GSS benchmark.

No prior correction or paper stating the \(x_H\) threshold was found.

The RePEc article record's generic “Corrections” facility is not a corrigendum.

## 3. Strongest plausible absorption candidates

### General switching-cost dynamics

Dynamic switching-cost models, including the Beggs–Klemperer tradition and later continuous-time work, derive dynamic/Markov price equilibria with evolving installed bases. They do not supply the static inherited-history GSS five-regime best-response correspondence or the exact \(x_H\) condition.

**Absorption result:** NO.

### Policy-choice models with switching costs

Jeong and Maruyama study firms' strategic commitment to uniform versus discriminatory pricing in two-period games. Their equilibrium objects are pricing-policy choices plus downstream prices, not the GSS one-period uniform subgame with the same inherited-history partition.

**Absorption result:** NO.

### Closest BBPD / switching-cost neighborhood

The post-Astra recertification treats later papers as potential parent/subgame candidates rather than dismissing them because they are dynamic.

**Umezawa (2022) and author-posted corrigendum (2023).** Umezawa studies a two-period horizontally and vertically differentiated duopoly with switching costs and uses uniform pricing as a benchmark. The 2023 corrigendum is methodologically close: it corrects an inference from the ordering of second-period uniform prices to the ordering of switching cutoffs, and modifies affected parameter regions and propositions. This is a genuine prior example of a regime-consistency correction in a nearby BBPD model. The accessible corrigendum does not state the GSS inherited-share threshold (x_H(s)), and its uniform benchmark depends on first-period states, vertical differentiation/service parameters, and second-period switching conditions not present in the fixed inherited-share GSS one-period game.

**Shrivastav (2023).** The model uses discrete brand preferences, imperfect consumer recognition, and idiosyncratic switching costs. The information structure and strategy object are therefore different from the GSS perfect-history uniform-price subgame.

**Colombo, Graziano & Pignataro (2024).** This is especially close because firms inherit asymmetric market shares and perfect information appears as a limiting case of information completeness. The accessible publisher material nevertheless studies a recognition parameter and pricing menus under partial information; no exact GSS (x_H(s)) global-best-response threshold is located in the accessible article materials inspected here.

**Umezawa & Yamakawa (2025).** This is a two-period model with multiple demand types in which firms accepting switchers bear the common switching cost. The payer of switching costs, consumer heterogeneity, timing, and equilibrium object differ materially from GSS.

**Absorption result:** no absorption identified in the accessible versions inspected. The project does **not** claim universal non-absorption across proprietary versions, uninspected appendices, or every possible specialization.

### General kinked-demand / Edgeworth / asymmetric Bertrand literature

This literature establishes that non-smooth demand, captive consumers, capacity, or segmentation can generate missing pure equilibria or mixed pricing. Those theorems do not specialize directly to the GSS demand correspondence in a way that yields the accepted-version Eq. (12) validity domain without solving the model-specific kink comparison.

The 2025 Review of Industrial Organization article “Random Pricing: Bertrand Competition with Uncontested Consumers,” for example, studies homogeneous Bertrand competition with uncontested consumer bases and derives a mixed equilibrium after pure nonexistence. Its primitives are not a parent theorem for the Hotelling-history game here.

Likewise, 2026 work on spatial price-policy subgames emphasizes mixed strategies when an asymmetric pricing subgame lacks a pure equilibrium, but it does not contain this inherited-history switching-cost game or the \(x_H\) theorem.

**Absorption result:** NO.

## 4. What is and is not novel

### Defensible novelty

* no prior located correction of the accepted manuscript's global Eq. (12) claim in the accessible sources searched;
* complete pure-strategy price correspondence for that benchmark;
* exact necessary-and-sufficient source-profile validity domain;
* exact identification of the pure-nonexistence region;
* branch-correct downstream source-result map;
* source-fidelity correction of the Eq. (15)–(17) chain: Eq. (15) itself is correct on its switching branch, while Eq. (16) reverses its sign and the no-switch branch requires separate accounting;
* corrected Result-4 profit accounting across the uniform allocation branches.

### Not claimed as novel

* existence of kinks in price competition;
* generic pure-strategy nonexistence in Bertrand games;
* generic use of mixed pricing after pure nonexistence;
* general welfare theory of switching costs;
* a cross-model theorem about all asymmetric installed-base games.

## 5. 2011-paper separation

The 2011 Gehrig–Shy–Stenbacka entry paper is a distinct incumbent/entrant model in which access to purchase-history information differs. It neither absorbs nor supplies the current theorem. The separate 2011 correction repository remains untouched.

## 6. Novelty classification

**Source-specific mathematical correction / reassessment with a nontrivial exact equilibrium-domain theorem.**

The theorem is currently classified **MODEL-SPECIFIC**, not generic. That classification is sufficient for this correction project and avoids overstating cross-model generality.

## Stage-6 gate

**GO / RECERTIFIED AFTER ASTRA AUDIT.** No exact prior correction or parent theorem was located in the accessible sources searched that supplies the GSS-specific (x_H(s)) theorem. The Umezawa corrigendum is now treated as a close methodological correction precedent rather than ignored. Non-absorption wording is explicitly limited to inspected accessible versions. The contribution survives as a source-specific global-equilibrium correction.


## 7. Post-Astra closest-model correspondence table

| Work | Timing / state | Consumer / information structure | Switching-cost incidence | Uniform benchmark relation | Absorption assessment |
|---|---|---|---|---|---|
| Umezawa (2022) + 2023 corrigendum | two periods; first-period purchases determine second-period history | horizontal + vertical differentiation; supporting-service asymmetry | consumer switching cost in the 2022 model | second-period uniform benchmark has multiple switching configurations; corrigendum corrects price-order ⇒ cutoff-order inference | methodologically close correction precedent; accessible corrigendum does not contain GSS (x_H) |
| Shrivastav (2023) | dynamic/history based | discrete brand preferences; imperfect correct/incorrect recognition | idiosyncratic switching costs | uniform/history-based comparison embedded in imperfect recognition | different information and demand primitives |
| Colombo, Graziano & Pignataro (2024) | inherited asymmetric shares | partial customer recognition; perfect information as special case | history-based pricing with information completeness parameter | close inherited-share neighborhood | accessible material does not state GSS (x_H); universal non-absorption not claimed |
| Umezawa & Yamakawa (2025) | two periods | multiple demand types | firms accepting switchers bear common switching cost | separate BBPD/uniform dynamics | different payer, heterogeneity, and timing |

Evidence rechecked on 2026-09-23 against publisher/author-hosted records. The project records the author-posted Umezawa corrigendum explicitly in the manuscript bibliography.
