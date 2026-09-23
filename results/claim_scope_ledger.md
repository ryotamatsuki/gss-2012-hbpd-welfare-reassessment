# Claim-Scope Ledger

| Claim ID | Exact scope | Evidence | Classification | Maximum wording | Prohibited wording |
|---|---|---|---|---|---|
| UPE-2012-1 | all \(\tau>0\), common \(c\), \(x_0\in(1/2,1]\), \(0\le\sigma<\tau\), original full-coverage Hotelling model; pure prices | Stage 4 theorem certificate; Stage 4A adversarial certificate; exact evaluator; Lean core when gate closes | MODEL-SPECIFIC | complete pure-strategy correspondence in GSS benchmark | no Nash equilibrium; generic switching-cost theorem |
| EQ12-FAIL | accepted-manuscript Eq. (12) profile fails global pure Nash below \(x_H\) | exact \(719/1800\) counterexample + global theorem | MODEL-SPECIFIC correction | accepted Eq. (12) needs an additional pure-Nash domain restriction | published VOR is wrong unless VOR body verified |
| CS-WEAK | branch-correct weak-HBP profile CS; equilibrium only on pure overlap | primitive integral, symbolic reconstruction, exact regressions | MODEL-SPECIFIC | weak source CS reversal does not survive direct branch-correct integration | corrected equilibrium CS over no-pure region |
| PROFIT-B-WEAK | small-firm HBP profit comparison on weak pure overlap | Stage 7 analytic sign proof | MODEL-SPECIFIC | on every weak-domain pure-equilibrium comparison, \(\pi_B^d<\pi_B^u\) | statement about mixed-equilibrium region |
| W-WEAK | weak HBP vs uniform on corrected pure overlap | resource-cost accounting + endpoint identity | MODEL-SPECIFIC | uniform pricing has higher welfare on certified weak pure overlap | global welfare ranking over entire source parameter space |
| CS-STRONG | source/nonnegative-margin strong-HBP selection and corrected pure-uniform domain | Stage 7 + strong-HBP selection audit | MODEL-SPECIFIC / SELECTION-CONDITIONAL | Result 6 survives under source selection | selection-free CS ranking with unrestricted below-cost prices |
| W-STRONG | corrected pure-uniform domain; all members of strong zero-sales HBP family | direct resource-cost accounting | MODEL-SPECIFIC | Result 7 survives and is selection-invariant; equality at \(x_0=1\) | strict inequality at degenerate \(x_0=1\) |
| MIXED-SCOPE | \(1/2<x_0<x_H(s)\) | mixed-scope memo | OUT OF SCOPE | no pure-strategy equilibrium; mixed pricing outside scope | no equilibrium / no Nash equilibrium |

## Formal-verification wording rule

Until the Lean gate closes, manuscript text may say the algebraic core is **targeted for formal verification**, not formally verified.

After a PASS, manuscript text may say only that the selected algebraic/inequality core has been machine-checked. It may not say the full economic model or complete Nash correspondence is formally verified unless the primitive demand correspondence and equilibrium definition are themselves encoded.
