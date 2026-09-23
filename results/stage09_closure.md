# Stage 9 Closure Manifest

**Canonical verdict:** GO / CLOSED  
**Stage-8 theory input:** b5bb95f083d4c855647314f90ba735eabf2476d3  
**Certified reproducibility code head:** ff695a6722bc7e17c7b8325db4eb947198a0e5ca  
**Branch:** research/stage-09-reproducibility  
**Main:** unchanged.

## Closed requirements

- deterministic exact rational checks;
- independent primitive demand/payoff evaluator;
- symbolic primitive reconstruction;
- Stage-7 symbolic impact identities;
- compact frozen-regression unittests;
- deterministic parameter tables;
- deterministic diagnostic SVG figures;
- byte-for-byte regeneration check;
- source provenance manifest and PDF redistribution guard;
- theorem certificate index;
- Lean 4.19.0 / pinned mathlib clean build;
- no Lean sorry/admit/project-specific axiom;
- pdfLaTeX production scaffold;
- fresh-checkout GitHub Actions.

## Certified CI evidence before closure documentation

Stage-9 workflow run 35820175443:

- Python job 107050137762 — SUCCESS;
- LaTeX job 107050138087 — SUCCESS.

Formal workflow run 35820175432:

- Lean job 107050137903 — SUCCESS.

## Reproducibility repairs made at Stage 9

1. Replaced SymPy structural-expression equality with exact zero-difference simplification.
2. Replaced runtime-sensitive two-decimal SVG formatting with an explicit deterministic rounding rule.

Both repairs affect verification/rendering infrastructure only. Stage-8 formulas, theorem statements, domains, selections, and result classifications are unchanged.

## Next-stage contract

Route to Stage 10. Manuscript construction must consume the frozen theorem registry and may not change theory without explicit rollback under docs/THEORY_CHANGE_CONTROL.md.
