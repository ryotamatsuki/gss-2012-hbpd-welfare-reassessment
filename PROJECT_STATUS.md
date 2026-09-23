# Project Status

## Target

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI `10.1007/s10842-011-0111-8`.

## Current canonical position

**Stage 7 — GO completed. Next gate: Stage 7.5 / 7.5A.**

Stage 4 and Stage 4A are now closed. The complete **pure-strategy** uniform-price correspondence has passed independent adversarial certification. This does not authorize any claim about mixed-strategy nonexistence.

## Current research branch

`research/stage-04a-certification`, created from `research/stage-04-uniform-price-game`. `main`, `research/stage-00-evidence-freeze`, and the separate 2011 correction repository remain unchanged.

## Gate state

| Gate | Status | Notes |
|---|---|---|
| Stage 0 evidence/source freeze | GO for accepted-manuscript-qualified research | Lawful post-referee accepted manuscript obtained; exact Springer VOR equation text still unavailable. |
| Stage 1 source & mathematical audit | GO | Seven accepted-manuscript Results mapped; critical equations independently reconstructed. |
| Stage 2 literature / novelty kill | GO | No prior correction or theorem absorption found for the source-specific `x_H` result. |
| Stage 3 architecture | GO | Route B: corrected complete pure-equilibrium reassessment. |
| Stage 4 global uniform-price game | GO / CLOSED | Five-piece clipped demand and complete pure correspondence proved. |
| Stage 4A independent certification | PASS / CLOSED | Candidate-deviation, alternative-equilibrium, indifference, strategy-domain, and boundary attacks pass. |
| Mixed-equilibrium scope | FROZEN — Route B | Not solved; no claim of general equilibrium nonexistence and no equilibrium welfare in the no-pure region. |
| Stage 6 novelty re-kill | GO | Frozen UPE-2012-1 theorem survives source-specific absorption search. |
| Stage 7 downstream impact | GO | Accepted-manuscript Results 1–7 impact mapped on certified equilibrium domains. |
| Formal verification | APPLICABLE / OPEN FOR STAGE 7.5A | Target map committed; compiled Lean 4/mathlib certificate is mandatory before Stage 8. |
| Stage 7.5 / 7.5A | NEXT | Freeze manuscript scale/scope, portability/quantifiers, and complete formal-verification gate. |
| Stage 8 theory freeze | BLOCKED UNTIL 7.5A | No theory freeze yet. |
| Stage 14 / submission | NOT REACHED | No submission package or portal action. |
| Stage 15 / actual submission | PROHIBITED | Do not submit, freeze, pay, or finalize legal declarations. |

## Certified pure-equilibrium theorem

Let (s=\sigma/\tau\in[0,1)), (x=x_0\in(1/2,1]), (	au>0), and define

[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
]

For (s=0), the unique pure uniform-price equilibrium has normalized margins ((1,1)). For (0<s<1),

[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&1/2<x<x_H(s).
\end{cases}
]

At (x=x_H(s)), B has a second payoff-equal kink best response, but it does not form another Nash profile. Hence the pure equilibrium remains unique where it exists.

## Stage-4A evidence

* `results/stage04_theorem_certificate.md`
* `results/stage04a_independent_certificate.md`
* `results/stage04a_formal_verification_target_map.md`
* `derivations/uniform_price_game_full_demand.md`
* `derivations/uniform_price_global_best_responses.md`
* `code/uniform_game_cleanroom.py`
* `code/symbolic_reconstruction.py`
* `results/mixed_equilibrium_scope_decision.md`

## Remaining blockers before Stage 8

1. Stage 7.5 final theory/paper-scope decision.
2. Stage 7.5A portability/quantifier red-team.
3. Lean 4/mathlib formal-verification PASS with statement-fidelity and no-placeholder audit.
4. Preserve accepted-manuscript/VOR wording qualification unless exact VOR text becomes lawfully available.
