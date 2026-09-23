# Stage 4A — Formal-verification applicability and target map

**Decision:** FORMAL VERIFICATION APPLICABLE  
**Stage-4A role:** target selection only. Under research-paper-workflow v2.4, the compiled proof-assistant certificate is a mandatory Stage-7.5A pre-freeze gate, not a prerequisite for independent Stage-4A adversarial PASS.

## Target map

| Claim ID | Paper claim/component | Proof-critical component | Lean 4/mathlib target | Explicitly outside this target | Assurance gain |
|---|---|---|---|---|---|
| UPE-2012-1A | threshold ordering | `x_H(s)>x_u(s)` and `x_H(s)<1` for `0<s<1` | exact square-root inequality lemmas | economic derivation of the thresholds | closes boundary/order algebra |
| UPE-2012-1B | B global-deviation threshold | source-vs-kink payoff difference factors as `2(x-x_L)(x-x_H)` | polynomial/radical identity + sign implication | primitive consumer-choice derivation | certifies the necessary/sufficient algebra once demand pieces are independently certified |
| UPE-2012-1C | exact failure witness | at `tau=1, sigma=1/2, x=3/5, c=0`, gain is `719/1800>0` | exact rational arithmetic theorem | source-version provenance | mechanically certifies the counterexample arithmetic |
| UPE-2012-1D | equality knife edge | at `x=x_H`, B's source and kink actions tie, but A gains `2sx>0` at the kink profile | equality substitutions + positive-gain lemma | complete best-response correspondence as an economic object | protects uniqueness at the knife edge |
| CS-2012-1 | accepted-manuscript Eq. (15)/(16) source-fidelity audit | Eq. (15) equals the primitive switching-branch expression and printed Eq. (16) is its negative | polynomial identity lemmas + exact point | continuum integration primitives unless separately encoded | prevents source-transcription and sign-transformation error |
| CS-2012-2 | no-switch CS regression | `s=99/100,x=501/1000` gives positive direct gap `17993/4500000` | exact rational identity/sign theorem | justification that the point is on the no-switch branch unless encoded separately | freezes branch-correct sign |
| PROF-2012-1 | weak Result-4 branch audit | `s=1/2,x=51/100` gives actual no-switch B-profit gap `-227/4500` | exact rational theorem | derivation of HBP prices from primitives | prevents Eq. (22) extrapolation |
| PROF-2012-2 | weak-profit overclaim guard | `s=9/10,x=19/20` gives strong-domain source-selected B-profit gap `41/900>0` | exact rational theorem | full strong-HBP equilibrium derivation | prevents weak-domain claim leakage |
| W-2012-1 | weak-welfare endpoint | correct endpoint substitution identity | exact symbolic identity/sign theorem | welfare accounting primitives | protects the source-result impact map |
| UPE-2012-OVERLAP | pure-equilibrium/weak-HBP overlap | `x_H(s) <= (3-s)/4` iff the derived exact parameter bound | radical inequality equivalence | journal-facing economic interpretation | certifies later domain intersections |

## Statement-fidelity contract for Stage 7.5A

The formal artifact may certify only the algebraic/inequality core unless the primitive demand correspondence and Nash definition are themselves encoded. A theorem of the form “if the certified demand-piece and payoff formulas hold, then the threshold inequality follows” must not be described as a formal proof of the complete economic equilibrium theorem.

The Stage-7.5A certificate must record:

- Lean and mathlib versions/commit;
- exact theorem signatures and paper-claim mapping;
- assumptions supplied versus proved;
- whether demand/clipping and Nash equilibrium are formalized or remain analytic inputs;
- clean build command and output;
- `#print axioms` or equivalent;
- repository-wide `sorry` / `admit` / placeholder audit;
- no conclusion-smuggling through definitions or assumptions.

## Stage-4A consequence

Formal verification is **not** counted as the independent certification path. Stage 4A relies on the clean-room primitive evaluator plus a separate exhaustive analytic branch proof. This target map is the handoff contract that prevents formal verification from being forgotten before Stage 8.
