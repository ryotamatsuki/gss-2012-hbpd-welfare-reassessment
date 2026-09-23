# Stage 7.5 — Full-Theory Freeze Decision

**Verdict:** GO  
**Decision:** full correction/reassessment, not a minimal erratum and not an extended mixed-strategy paper.  
**Working scale:** approximately 15–20 manuscript pages excluding appendices/supplement.  
**Source scope:** post-referee accepted manuscript; exact Springer VOR equation text remains an explicit qualification.

## 1. Research object frozen

The project is a source-specific mathematical reassessment of the uniform-pricing benchmark and downstream welfare analysis in Gehrig, Shy, and Stenbacka (2012).

The paper will make no claim of a general theorem for switching-cost Bertrand games. It will characterize the complete **pure-strategy** price correspondence in the original inherited-history Hotelling model and trace the consequences for the accepted manuscript's Results 1–7.

## 2. Core strategic mechanism

The accepted-manuscript Eq. (12) solves the smooth A-history-to-B switching branch locally. The global price game has a no-switch plateau and a no-poaching kink. Firm B can profitably cross that kink when inherited asymmetry is insufficiently large.

The exact boundary is
\[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6,\qquad s=\sigma/\tau.
\]

For \(0<s<1\), the source price vector is the unique pure Nash equilibrium iff
\[
x_0\ge x_H(s).
\]
Below that boundary the uniform-price game has no pure-strategy equilibrium.

This is the headline theorem. Mixed pricing is outside scope.

## 3. Why this warrants a full reassessment

A minimal counterexample note is too narrow because the correction changes more than one displayed price vector:

1. it supplies a necessary-and-sufficient pure-equilibrium domain rather than only a counterexample;
2. the weak-HBP / pure-uniform equilibrium overlap collapses to a narrow region \(0<s<s_c\);
3. accepted Result 3's weak consumer-surplus reversal disappears under primitive branch-correct integration;
4. accepted Result 4's high-switching-cost small-firm benefit region disappears as a comparison of two pure equilibria;
5. accepted welfare Results 5 and 7 survive, but only under corrected domain/branch qualifications;
6. accepted Result 6 survives on the corrected pure domain under the source/nonnegative-margin strong-HBP selection;
7. a separate strong-HBP below-cost zero-sales equilibrium family requires explicit price-domain/selection language.

That combination is materially more than a typo correction while remaining a bounded source-specific reassessment.

## 4. Scope choices frozen

### Included

- full primitive uniform demand correspondence;
- complete pure-strategy uniform-price equilibrium theorem;
- equality/multiplicity audit;
- strategy-domain reduction for the uniform game;
- accepted-manuscript Eq. (12) exact counterexample;
- primitive CS integration and Eq. (15) correction;
- branch-correct profit/welfare accounting;
- accepted-manuscript Results 1–7 impact ledger;
- strong-HBP below-cost selection qualification;
- exact source/version provenance;
- formal-verification supplement for proof-critical algebra.

### Excluded

- mixed-strategy pricing below \(x_H\);
- general asymmetric installed-base extensions;
- alternative outside-option models;
- new heterogeneity/timing/information structures;
- claims of generic nonexistence in switching-cost Bertrand games;
- welfare claims in the no-pure region;
- any unqualified assertion about exact Springer VOR equations until directly inspected.

## 5. Essential versus normalization assumptions

Essential/model-defining:

- Hotelling line with firms at 0 and 1;
- inherited history split at \(x_0>1/2\);
- linear transport cost \(\tau>0\);
- common switching cost \(0\le\sigma<\tau\);
- full market coverage and one unit per consumer;
- common marginal cost \(c\);
- uniform-pricing benchmark uses one price per firm;
- pure-strategy equilibrium concept for the headline theorem.

Normalization/invariance devices:

- \(s=\sigma/\tau\);
- normalized margins \((p_i-c)/\tau\);
- price-difference coordinate \(d=(p_B-p_A)/\tau\);
- measure-zero consumer tie convention.

The latter do not carry the substantive theorem; Stage 7.5A tests this explicitly.

## 6. Contribution classification before portability red-team

**MODEL-SPECIFIC source correction/reassessment with an exact equilibrium-domain theorem.**

This is intentional. No manuscript sentence will market the result as a general theorem over alternative demand systems or switching-cost models.

## 7. Manuscript architecture frozen

Working title:

**Uniform-Price Equilibria and Welfare with Switching Costs: A Reassessment of Gehrig, Shy, and Stenbacka (2012)**

Sections:

1. Introduction
2. Original Model and Source Claims
3. Global Uniform-Price Demand and Best Responses
4. Pure-Strategy Equilibrium Correspondence
5. Consumer-Surplus and Profit Corrections
6. Implications for the Original Welfare Results
7. Conclusion

Appendix/supplement:

- full piecewise demand and boundary proof;
- exact counterexamples/regressions;
- strong-HBP strategy-domain note;
- formal-verification statement map and build provenance.

## 8. Mixed-equilibrium decision

Route B remains frozen.

Permitted wording:

> We characterize the complete pure-strategy price correspondence. In the region below \(x_H(s)\), no pure-strategy price equilibrium exists; mixed pricing is outside the scope of this reassessment.

Prohibited wording:

- “there is no equilibrium”;
- “Nash equilibrium does not exist” without the pure-strategy qualifier;
- equilibrium welfare outside the pure-existence domain.

## 9. Stage 7.5 gate

**GO → Stage 7.5A.**

The paper contains a nontrivial, exact, source-specific global-equilibrium correction with material downstream welfare implications. The correct research-strength target is a full reassessment with deliberately model-specific claims, not a forced cross-model generalization.
