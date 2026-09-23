# Stage 2 — Literature frontier / novelty kill gate

**Verdict:** GO for a source-specific corrected pure-equilibrium reassessment.  
**Scope:** no claim of a general new theorem for all switching-cost Bertrand games.  
**Search date:** 2026-09-23.

## 1. Prior correction search

Searches were run for the exact article title together with:

* erratum
* correction
* corrigendum
* comment
* reply
* DOI `10.1007/s10842-011-0111-8` + correction/erratum/corrigendum
* forward citations and author publication lists.

No substantive correction, corrigendum, comment, or reply addressing Eq. (12), Eq. (15), or the global uniform-price best response was found.

Important false positive: RePEc's “Corrections” section on the article record is the generic RePEc metadata-correction facility and is **not** a correction article.

## 2. Forward-citation / later-literature audit

The search reviewed, at minimum:

* RePEc/CitEc forward-citation records for the 2012 article;
* Stefano Colombo (2015), pricing-policy choice against a price-discriminating rival;
* Shy, Stenbacka and Zhang (2016), history-based versus uniform pricing in growing/declining markets;
* Colombo, Graziano and Pignataro (2024), imperfect HBP with asymmetric market shares;
* Umezawa and Yamakawa (2025), switching costs and BBPD with multiple consumer types;
* Jeong and Maruyama (2008, 2009), strategic commitment to discrimination/uniform pricing with switching costs;
* classic switching-cost / mixed-pricing references and general kinked-demand / nonexistence literature.

Later papers continue to cite GSS (2012) as part of the HBP/switching-cost literature. The searched records do not identify the exact `x_H(s)` restriction or an erratum to the GSS (2012) uniform benchmark.

## 3. Theorem-absorption test

The project theorem is deliberately source-specific:

> In the one-period GSS (2012) inherited-history Hotelling benchmark with uniform pricing, `x_0>1/2`, `0<s=σ/τ<1`, full coverage, and the stated price strategy convention, characterize the complete **pure-strategy** Nash price correspondence.

The closest general literatures do not absorb this theorem in the searched evidence:

### Jeong–Maruyama line

Jeong and Maruyama study commitment to pricing **policies** in two-period switching-cost models. Their equilibrium objects include adoption of discriminatory versus uniform policies. That is a different game and does not provide the GSS one-period five-regime price-difference correspondence or the exact `x_H(s)` threshold.

### Dynamic switching-cost price competition

Beggs–Klemperer/Fabra–García and related dynamic models study Markov pricing and installed-base dynamics. Their equilibrium conditions are not the static inherited-history GSS price game.

### Kinked-demand / Edgeworth nonexistence

General kinked-demand and Edgeworth-cycle work establishes that non-smooth demand can produce nonexistence or cycling in other price games. It does not imply the GSS threshold
[
x_H(s)=rac12-rac{s}{3}+rac{sqrt{3s(s+6)}}6
]
or its exact necessary-and-sufficient role in this model.

### Recent BBPD model with uniform-price nonexistence

Umezawa and Yamakawa (2025) explicitly report that their own multi-consumer-type BBPD model has no pure-strategy equilibrium under uniform pricing and leave mixed uniform pricing for future work. This is useful context: pure nonexistence in a switching-cost uniform benchmark is economically plausible and not an anomalous concept. Their primitives and equilibrium system differ materially from GSS (2012), so the result does not absorb the GSS threshold theorem.

### Imperfect-information asymmetric-share model

Colombo, Graziano and Pignataro (2024) characterize pure equilibria with asymmetric inherited shares and imperfect customer recognition. Their baseline uses a different information structure and (in the published treatment) different timing/recognition primitives. It cites GSS (2012), but the searched material does not state or derive the present correction.

## 4. 2011 GSS separation

Gehrig, Shy and Stenbacka (2011), *European Economic Review*, studies an incumbent/entrant environment in which the entrant does not have the same purchase-history information. Its uniform-price benchmark is a different model.

The separate production repository `ryotamatsuki/gehrig-shy-stenbacka-correction` is not used as evidence of novelty here and has not been modified.

## 5. Novelty classification

The project does **not** claim that “piecewise Bertrand games may lack pure equilibrium” is novel.

The surviving contribution is narrower and stronger:

1. identify that the accepted-manuscript Eq. (12) is only the smooth one-way-switch branch candidate;
2. derive the full primitive demand correspondence including the no-switch plateau and reverse-switch/capture regimes;
3. characterize the exact parameter set on which that candidate is globally Nash;
4. prove complete pure-strategy nonexistence outside that set;
5. propagate the corrected equilibrium domain through the accepted manuscript's CS/profit/welfare comparisons;
6. independently repair branch-sensitive consumer-surplus and welfare algebra.

The exact source-specific domain theorem and its consequence for the accepted manuscript's “unique Nash–Bertrand equilibrium” statement were not found in the prior literature search.

## 6. Architecture kill gate

Three architectures were compared.

### A — minimal correction
Counterexample to Eq. (12) + Eq. (15) algebra correction.

**Rejected as underpowered.** It leaves the economically relevant question—what the correct pure-equilibrium domain is—unanswered.

### B — corrected pure-equilibrium reassessment
Full piecewise demand, complete pure-price correspondence, branch-correct welfare accounting, and exact source-result impact map.

**Selected.** This matches the certified contribution and avoids research creep.

### C — extended mixed-strategy/general-asymmetry paper
Solve mixed pricing on the no-pure region and/or generalize the inherited-share structure.

**Not selected.** Mixed pricing is not required to correct the source's pure “unique Nash–Bertrand equilibrium” claim, and a full mixed solution would materially change project scope. It remains an explicit extension, not an implied result.

## 7. Stage-2 gate

**GO.** No prior correction or theorem absorption was located that removes the source-specific contribution. The manuscript must market the contribution as a mathematically complete reassessment of the GSS (2012) benchmark, not as a generic theorem about all switching-cost price games.

Stage 6 must rerun the search against the frozen theorem wording and any formalized threshold result.
