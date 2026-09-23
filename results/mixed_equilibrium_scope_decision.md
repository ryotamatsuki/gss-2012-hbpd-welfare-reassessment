# Mixed-equilibrium scope decision

**Decision:** Route B — do not solve the mixed-strategy price equilibrium in this correction/reassessment.  
**Date:** 2026-09-23  
**Prerequisite:** Stage 4/4A pure correspondence PASS.

## Question 1 — Does a mixed equilibrium exist below \(x_H(s)\)?

Not established in this project. The pure-strategy theorem proves only that the pure correspondence is empty for
\[
1/2<x_0<x_H(s).
\]
The price strategy set is naturally unbounded unless an explicit bound is imposed, so a generic mixed-existence theorem is not invoked without checking its hypotheses.

## Question 2 — Is a mixed solution necessary to correct the source claim?

No. The accepted manuscript explicitly calls Eq. (12) the “unique Nash–Bertrand equilibrium in prices.” The correction can establish, without solving mixed pricing, that:

1. the displayed profile is a smooth-branch candidate;
2. it is globally pure Nash iff \(x_0\ge x_H(s)\);
3. below that threshold it is not Nash;
4. no other pure-price equilibrium exists.

This is sufficient to qualify the source's pure-price benchmark.

## Question 3 — Is mixed pricing necessary for the paper's welfare statements?

Only if the paper attempted to state an equilibrium welfare comparison over the entire parameter space. It will not.

All corrected equilibrium CS/profit/welfare claims are restricted to the parameter region in which the uniform pure equilibrium exists. Outside that region, the source price vector may be evaluated only as a **counterfactual profile**, never as equilibrium welfare.

## Question 4 — Is a complete mixed solution tractable and contribution-critical?

Potentially interesting, but not required for the selected architecture. A full mixed-price characterization in a five-regime kinked Bertrand game would materially enlarge the project and would need its own support, distributional equilibrium definition, existence proof, computation/analytic certification, and welfare selection analysis.

That is research extension, not a minimal repair of the accepted manuscript.

## Question 5 — Would adding it now constitute research creep?

Yes. Stage 3 selected the complete pure-correspondence reassessment precisely because it resolves the source claim while keeping the model unchanged.

## Frozen manuscript wording

Permitted:

> We characterize the complete pure-strategy price correspondence. Below \(x_H(s)\) the uniform-price game has no pure-strategy equilibrium. Characterization of mixed pricing in that region is outside the scope of this reassessment.

Prohibited:

* “there is no equilibrium” below \(x_H\);
* “the game has no Nash equilibrium” below \(x_H\);
* equilibrium CS/profit/welfare values in the no-pure region;
* treating a failure of a pure optimizer or numerical solver as evidence against mixed equilibrium.

## Reopen rule

Reopen mixed pricing only if:

1. a later source or prior theorem shows that mixed equilibrium is indispensable to the source-specific correction; or
2. the manuscript makes a welfare statement that cannot be truthfully restricted to the certified pure-existence domain.

Otherwise the mixed problem remains an explicitly identified extension.
