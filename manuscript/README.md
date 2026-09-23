# Manuscript

Stage 10 manuscript construction is complete against the Stage-8 frozen theory.

The production source is `main.tex`. It includes:

- Introduction
- Model and source benchmark
- Uniform-price equilibrium characterization
- Consumer-surplus and profit corrections
- Welfare and accepted Results 1–7 impact
- Strategy-domain, selection, portability, and formal-verification scope
- Related literature
- Discussion
- Conclusion
- three appendices covering the complete uniform proof, primitive surplus derivations, and reproducibility

The Figure/Table Architecture uses one quantitative parameter-domain figure and two tables. Figure 1 reads the verified Stage-9 `generated/parameter_domains.csv` data.

Build from repository root with:

`make manuscript`

The build runs the manuscript claim-scope audit, pdfLaTeX, BibTeX, settled cross-reference passes, and a final unresolved-reference check.

Substantive changes to the frozen theorem set remain governed by `docs/THEORY_CHANGE_CONTROL.md`. Stage 11 is the next gate.
