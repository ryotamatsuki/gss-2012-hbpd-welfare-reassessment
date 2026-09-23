# Stage 8 Closure Manifest

**Canonical verdict:** GO — CANONICAL THEORY FROZEN  
**Stage-8 input:** \`research/stage-075a-freeze-gate\` at \`d159a6d286d5547873decceb4cc26e6d3e0871ef\`  
**Frozen-content head before this manifest:** \`faf74ceddd01fdd9a338b236395e5b932a8d9036\`  
**Stage-8 branch:** \`research/stage-08-theory-freeze\`  
**Main:** unchanged.

## Entry-gate evidence

- Stage 4A: PASS / CLOSED.
- Stage 7.5A: GO / CLOSED.
- Formal Verification Gate: PASS.
- Lean 4.19.0 / mathlib \`c44e0c8ee63ca166450922a373c7409c5d26b00b\`.
- Accepted-manuscript source boundary recorded; exact Springer VOR equation text remains explicitly unverified.

## Frozen artifacts

1. \`results/stage08_canonical_theory_freeze.md\`
2. \`results/stage08_theorem_registry.md\`
3. \`results/stage08_counterexample_registry.md\`
4. \`results/stage08_benchmark_selection_register.md\`
5. \`docs/THEORY_CHANGE_CONTROL.md\`
6. upstream Stage 4A/7/7.5A certificates and formal artifacts listed by the canonical freeze.

## Frozen theory summary

- complete **pure-strategy** uniform-price equilibrium correspondence;
- exact threshold \(x_H(s)\);
- pure nonexistence below \(x_H\), with mixed equilibrium explicitly unresolved;
- weak-HBP / pure-uniform overlap boundary \(s_c\);
- corrected weak consumer-surplus branch formulas;
- corrected weak small-firm profit conclusion on the pure overlap;
- weak and strong welfare conclusions on certified domains;
- strong-HBP price-selection qualification for CS/profits;
- accepted-manuscript Results 1–7 impact classification;
- MODEL-SPECIFIC portability classification;
- formal coverage = PROOF-CRITICAL CORE.

## Permanent restrictions

Downstream stages may not:

- upgrade “accepted manuscript” to an unqualified VOR correction claim without Stage-1 source reopening;
- call pure nonexistence general Nash nonexistence;
- add mixed-equilibrium welfare;
- suppress the strong-HBP selection qualification;
- advertise generic cross-model portability;
- state that Lean verifies the full economic model;
- alter frozen equations, theorem quantifiers, or Result 1–7 classifications without rollback.

## Next-stage contract

Proceed to Stage 9 only for reproducibility/repository engineering:

- fresh-clone deterministic execution;
- exact regression tests;
- symbolic checks;
- Lean clean build;
- CI;
- generated tables/figures;
- manuscript build infrastructure;
- source/provenance manifests.

No substantive theory engineering is authorized inside Stage 9.
