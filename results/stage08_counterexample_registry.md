# Counterexample and Regression-Test Registry

**Frozen at Stage 8.** Every item below is permanent unless an explicit rollback invalidates the corresponding model definition.

| ID | Object | Exact target | Expected result | Artifact |
|---|---|---|---|---|
| REG-UPE-01 | Eq. (12) global failure | \((\tau,\sigma,x_0,c)=(1,1/2,3/5,0)\) | B gain \(719/1800>0\) | \`code/uniform_game_cleanroom.py\`; Lean theorem \`exact_counterexample_gain\` |
| REG-UPE-02 | equality threshold | \(s=6/47,\ x_0=67/94\) | \(x_0=x_H(s)\); B has two BRs but only source action is Nash-compatible | clean-room exact evaluator |
| REG-UPE-03 | all demand boundaries | \(d=L,\alpha,\beta,U\) | direct clipped demand equals piecewise demand | \`code/uniform_game_cleanroom.py\` |
| REG-UPE-04 | strategy domain | zero/negative margin and capture tails | no additional pure Nash profile | Stage 4A certificate |
| REG-CS-01 | rejected upstream negative CS point | \(s=99/100,\ x_0=501/1000\) | actual no-switch gap \(17993/4500000>0\) | Python + Lean |
| REG-CS-02 | Eq. (15)/(16) source fidelity | \(s=1/10,\ x_0=7/10\) | primitive gap = accepted Eq. (15) = \(221/720\); displayed Eq. (16) lhs = \(-221/720\) | Python + Lean |
| REG-PROFIT-01 | weak Result-4 branch validity | \(s=1/2,\ x_0=51/100\) | realized no-switch B gap \(-227/4500\); switching extension \(4/375\) | Python + unittest |
| REG-PROFIT-02 | weak-profit scope non-portability | \(s=9/10,\ x_0=19/20\) | source-selected strong B gap \(41/900>0\) | Python + unittest |
| REG-W-01 | weak welfare endpoint | \(x_0=\bar x=(3-s)/4\) | \(-\tau(1+s)(1+9s)/144\) | symbolic script + Lean |
| REG-OVERLAP-01 | weak/pure overlap | \(x_H=\bar x\) | \(11s^2+66s-9=0\), root \(s_c=-3+6\sqrt{33}/11\) | Stage 7 + Lean |
| REG-HBP-01 | strong-HBP below-cost selection | \(3-s-4x_0\le u\le0\) | same allocation/W, varying CS/profit distribution | clean-room regressions |
| REG-SCOPE-01 | no-pure region wording | \(x_0<x_H\) | no pure equilibrium only; mixed unresolved | mixed-scope memo |

## Required downstream behavior

Stage 9 CI must preserve these regressions. Stage 11 hostile review must re-run the high-stakes subset rather than merely citing this registry.
