# Project Status

## Target

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI \`10.1007/s10842-011-0111-8\`.

## Current canonical position

**Stage 7.5A — GO / CLOSED. Next gate: Stage 8 — Canonical Theory Freeze.**

Stage 4 and Stage 4A are now closed. The complete **pure-strategy** uniform-price correspondence has passed independent adversarial certification. This does not authorize any claim about mixed-strategy nonexistence.

## Current research branch

\`research/stage-04a-certification\`, created from \`research/stage-04-uniform-price-game\`. \`main\`, \`research/stage-00-evidence-freeze\`, and the separate 2011 correction repository remain unchanged.

## Gate state

| Gate | Status | Notes |
|---|---|---|
| Stage 0 evidence/source freeze | GO for accepted-manuscript-qualified research | Lawful post-referee accepted manuscript obtained; exact Springer VOR equation text still unavailable. |
| Stage 1 source & mathematical audit | GO | Seven accepted-manuscript Results mapped; critical equations independently reconstructed. |
| Stage 2 literature / novelty kill | GO | No prior correction or theorem absorption found for the source-specific \`x_H\` result. |
| Stage 3 architecture | GO | Route B: corrected complete pure-equilibrium reassessment. |
| Stage 4 global uniform-price game | GO / CLOSED | Five-piece clipped demand and complete pure correspondence proved. |
| Stage 4A independent certification | PASS / CLOSED | Candidate-deviation, alternative-equilibrium, indifference, strategy-domain, and boundary attacks pass. |
| Mixed-equilibrium scope | FROZEN — Route B | Not solved; no claim of general equilibrium nonexistence and no equilibrium welfare in the no-pure region. |
| Stage 6 novelty re-kill | GO | Frozen UPE-2012-1 theorem survives source-specific absorption search. |
| Stage 7 downstream impact | GO | Accepted-manuscript Results 1–7 impact mapped on certified equilibrium domains. |
| Formal verification | PASS | Lean 4.19.0 / mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`; clean CI build, no project placeholders/axioms. |
| Stage 7.5 | GO / CLOSED | Full 15–20 page correction/reassessment architecture frozen; mixed pricing excluded. |
| Stage 7.5A | GO / CLOSED | MODEL-SPECIFIC scope certified; Contribution Robustness Certificate and Formal Verification PASS completed. |
| Stage 8 theory freeze | NEXT | All pre-freeze mathematical/scope/formal gates are now closed. |
| Stage 14 / submission | NOT REACHED | No submission package or portal action. |
| Stage 15 / actual submission | PROHIBITED | Do not submit, freeze, pay, or finalize legal declarations. |

## Certified pure-equilibrium theorem

Let
\[
s=\frac{\sigma}{\tau}\in[0,1),\qquad
x=x_0\in(1/2,1],\qquad \tau>0,
\]
and define
\[
x_H(s)=\frac12-\frac{s}{3}+\frac{\sqrt{3s(s+6)}}6.
\]

For \(s=0\), the unique pure uniform-price equilibrium has normalized margins \((1,1)\). For \(0<s<1\),
\[
\mathcal E^u(x,s)=
\begin{cases}
\{(1+s/3,1-s/3)\},&x\ge x_H(s),\\
\varnothing,&1/2<x<x_H(s).
\end{cases}
\]

At \(x=x_H(s)\), B has a second payoff-equal kink best response, but it does not form another Nash profile. Hence the pure equilibrium remains unique where it exists.

## Stage-4A evidence

* \`results/stage04_theorem_certificate.md\`
* \`results/stage04a_independent_certificate.md\`
* \`results/stage04a_formal_verification_target_map.md\`
* \`derivations/uniform_price_game_full_demand.md\`
* \`derivations/uniform_price_global_best_responses.md\`
* \`code/uniform_game_cleanroom.py\`
* \`code/symbolic_reconstruction.py\`
* \`results/mixed_equilibrium_scope_decision.md\`

## Remaining qualification before Stage 8

No mathematical gate remains open. Stage 8 must freeze the certified theorem set, the MODEL-SPECIFIC contribution scope, mixed-strategy exclusion, strong-HBP selection qualification, and accepted-manuscript/VOR wording boundary without changing theory.


## Stage 7.5A evidence

* `results/stage075_full_theory_freeze_decision.md`
* `results/stage075a_scope_portability_redteam.md`
* `results/contribution_robustness_certificate.md`
* `results/claim_scope_ledger.md`
* `results/stage075a_formal_verification_certificate.md`
* `formal/Gss2012/Core.lean`
* `.github/workflows/lean-formal.yml`
