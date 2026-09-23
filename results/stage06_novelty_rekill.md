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

### Later HBP/BBPD models

Later work on growing/declining markets, imperfect customer recognition, multiple consumer types, and asymmetric information uses materially different primitives. Recent work explicitly acknowledges pure-price nonexistence in some uniform-price subgames, but does not derive the GSS threshold.

**Absorption result:** NO.

### General kinked-demand / Edgeworth / asymmetric Bertrand literature

This literature establishes that non-smooth demand, captive consumers, capacity, or segmentation can generate missing pure equilibria or mixed pricing. Those theorems do not specialize directly to the GSS demand correspondence in a way that yields the accepted-version Eq. (12) validity domain without solving the model-specific kink comparison.

The 2025 Review of Industrial Organization article “Random Pricing: Bertrand Competition with Uncontested Consumers,” for example, studies homogeneous Bertrand competition with uncontested consumer bases and derives a mixed equilibrium after pure nonexistence. Its primitives are not a parent theorem for the Hotelling-history game here.

Likewise, 2026 work on spatial price-policy subgames emphasizes mixed strategies when an asymmetric pricing subgame lacks a pure equilibrium, but it does not contain this inherited-history switching-cost game or the \(x_H\) theorem.

**Absorption result:** NO.

## 4. What is and is not novel

### Defensible novelty

* first located correction of the accepted manuscript's global Eq. (12) claim;
* complete pure-strategy price correspondence for that benchmark;
* exact necessary-and-sufficient source-profile validity domain;
* exact identification of the pure-nonexistence region;
* branch-correct downstream source-result map;
* independent correction of the accepted-version CS and welfare algebra.

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

**GO.** No exact prior correction or parent theorem was found that absorbs UPE-2012-1. The contribution survives as a source-specific global-equilibrium correction. Stage 7 should now propagate only the certified pure-existence domain through market shares, profits, consumer surplus, and social welfare.
