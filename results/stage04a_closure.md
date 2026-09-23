# Stage 4A closure manifest

**Canonical verdict:** PASS / CLOSED  
**Claim certified:** UPE-2012-1 — complete pure-strategy uniform-price Nash correspondence  
**Closure branch:** \`research/stage-04a-certification\`  
**Closure input SHA:** \`c0a3419895bf0a4d0d4e2ad87feb03ed8b75eed0\`  
**Certificate output SHA:** \`28e9e299dc164feef0828bc34d10c55439100399\`  
**Workflow:** research-paper-workflow v2.4, main \`63f11a50a13d9328213498a5a6576d00b9bceef7\`

## Files changed for closure

- \`results/stage04a_formal_verification_target_map.md\` — formal-verification applicability and Stage-7.5A target contract.
- \`results/stage04a_independent_certificate.md\` — final D1/D2/D3, strategy-domain, boundary and scope certificate.
- \`results/stage04_global_uniform_game_progress.md\` — Stage 4 synchronized to GO/CLOSED.
- \`PROJECT_STATUS.md\` — canonical routing synchronized; next pre-freeze gate is Stage 7.5/7.5A.
- \`README.md\` — repository overview synchronized.

## Certified theorem

For
\[
s=\sigma/\tau\in[0,1),\qquad x=x_0\in(1/2,1],
\]
define
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

At \(x=x_H(s)\), firm B has a second payoff-equal kink best response, but that action does not form a second Nash profile.

## Attacks closed

1. Candidate-deviation audit over every clipping piece and feasible boundary — PASS.
2. Alternative-pure-equilibrium search over capture, both switching interiors, plateau, both kinks, zero-margin and negative-margin cases — PASS.
3. Indifference trigger at \(x=x_H\) — PASS; kink action fails A's best response.
4. Strategy-space reduction from unrestricted real prices to positive-margin equilibrium actions — PASS for the uniform game.
5. Boundary attacks at \(x\downarrow1/2\), \(x\uparrow1\), \(s\downarrow0\), \(s\uparrow1\), \(x=x_u\), \(x=x_H\), \(x=\bar x\), and \(d=L,\alpha,\beta,U\) — PASS.
6. Independent primitive-clipping evaluator and exact-rational regressions — reconciled with the analytic proof.
7. Mixed-strategy scope — frozen Route B; below \(x_H\) only pure-strategy nonexistence is claimed.

## Exact regressions retained

- Eq. (12) failure point: \(25/72 \to 56/75\), gain \(719/1800>0\).
- Equality witness: \(s=6/47,\ x=67/94=x_H(s)\).
- Upstream CS negative regression rejected: branch-correct primitive gap at \(s=99/100,x=501/1000\) is positive.
- Valid one-way-switch Eq. (15) discrepancy retained separately.

## Formal-verification state

**APPLICABLE / DEFERRED TO STAGE 7.5A AS REQUIRED BY v2.4.**

This is not an unresolved Stage-4A mathematical item. The target map is committed, but Stage 8 remains blocked until the Lean 4/mathlib build, statement-fidelity audit, axiom/placeholder audit, and toolchain provenance pass at Stage 7.5A.

## Surviving limitations

- Mixed pricing below \(x_H\) is not characterized.
- Exact Springer typeset VOR equations remain uninspected; claims are accepted-manuscript-qualified.
- Strong-HBP CS/profit comparisons retain the documented below-cost price-selection qualification.

None of these limitations weakens the certified pure-strategy uniform-price theorem.
