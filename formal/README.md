# Formal verification

This directory contains the proof-critical Lean 4 certification used at Stage 7.5A.

## Toolchain

- Lean: 4.19.0
- mathlib: \`c44e0c8ee63ca166450922a373c7409c5d26b00b\`

## Build

From this directory:

\`\`\`bash
lake update
lake exe cache get
lake build
\`\`\`

The GitHub Actions workflow \`.github/workflows/lean-formal.yml\` performs the same clean build and fails on project \`sorry\`, \`admit\`, or explicit project-specific \`axiom\` declarations.

## What is certified

The Lean core checks selected proof-critical algebra and inequalities:

- source-vs-kink B-payoff factorization underlying \(x_H\);
- \(x_u<x_H<1\) on the maintained \(0<s<1\) domain;
- exact \(719/1800\) counterexample gain;
- positive A gain at the equality kink;
- exact Eq. (15) discrepancy on a valid branch;
- positive branch-correct value at the rejected upstream CS regression point;
- weak-welfare endpoint identity;
- polynomial characterization of the weak-HBP / pure-uniform overlap boundary and its closed-form root.

## What is not certified

The formal project does **not** encode the complete continuum consumer-choice model, clipped demand correspondence, strategy space, Nash equilibrium definition, or mixed equilibrium. Those objects are independently certified analytically at Stages 4/4A.

Accordingly, manuscript wording may say that the proof-critical algebraic/inequality core is formally verified; it may not say that Lean proves the complete economic equilibrium theorem from primitive utilities.
