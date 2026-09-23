# Project Status

## Target

Thomas Gehrig, Oz Shy, and Rune Stenbacka (2012), “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393, DOI \`10.1007/s10842-011-0111-8\`.

## Current canonical position

**Stage 14 — CONDITIONAL PASS / CLOSED after independent-audit remediation. Authenticated IEP portal preflight is the sole remaining pre-submission condition. Stage 15 is not entered.**

Stage 4 and Stage 4A are now closed. The complete **pure-strategy** uniform-price correspondence has passed independent adversarial certification. This does not authorize any claim about mixed-strategy nonexistence.

## Current research branch

\`research/stage-04a-certification\`, created from \`research/stage-04-uniform-price-game\`. \`main\`, \`research/stage-00-evidence-freeze\`, and the separate 2011 correction repository remain unchanged.

## Gate state

| Gate | Status | Notes |
|---|---|---|
| Stage 0 evidence/source freeze | GO for accepted-manuscript-qualified research | Lawful post-referee accepted manuscript obtained; exact Springer VOR equation text still unavailable. |
| Stage 1 source & mathematical audit | RE-CERTIFIED GO | Eqs. (13)–(17) image-rechecked; Eq. (15) restored as source-faithful, Eq. (16) sign inversion separated from branch validity. |
| Stage 2 literature / novelty kill | GO | No prior correction or theorem absorption found for the source-specific \`x_H\` result. |
| Stage 3 architecture | GO | Route B: corrected complete pure-equilibrium reassessment. |
| Stage 4 global uniform-price game | GO / CLOSED | Five-piece clipped demand and complete pure correspondence proved. |
| Stage 4A independent certification | RE-CERTIFIED PASS / CLOSED | Capture/margin logic, `s=0`, `x_0=1`, reverse branch, equality, and all global deviations re-certified. |
| Mixed-equilibrium scope | FROZEN — Route B | Not solved; no claim of general equilibrium nonexistence and no equilibrium welfare in the no-pure region. |
| Stage 6 novelty re-kill | GO | Frozen UPE-2012-1 theorem survives source-specific absorption search. |
| Stage 7 downstream impact | RE-CERTIFIED GO | Result 4 is branch-correct; weak smaller-firm loss restricted to the pure overlap; strong endpoint/selection distinctions synchronized. |
| Formal verification | RE-CERTIFIED PASS | Lean 4.19.0 / pinned mathlib; repaired Eq. (15)/(16) targets and sentinel placeholder/axiom guard pass on final repaired head. |
| Stage 7.5 | GO / CLOSED | Full 15–20 page correction/reassessment architecture frozen; mixed pricing excluded. |
| Stage 7.5A | GO / CLOSED | MODEL-SPECIFIC scope certified; Contribution Robustness Certificate and Formal Verification PASS completed. |
| Stage 8 theory freeze | GO / FROZEN | Canonical theory, claim scope, benchmarks, regressions, formal coverage, and change-control rules frozen. |
| Stage 9 reproducibility | RE-CERTIFIED GO / CLOSED | Repaired 7-test suite, exact/symbolic checks, generated artifacts, source guard, Lean, and LaTeX all pass from clean checkout. |
| Stage 10 manuscript construction | GO / CLOSED | Full manuscript, proposition/corollary structure, 1 quantitative figure, 2 tables, appendices, bibliography, and claim-scope audit completed. |
| Stage 11 referee attack | RE-CERTIFIED GO / CLOSED | Later independent audit found B1–B7; limited rollback/change control completed and all blocking findings closed. |
| Stage 12 journal positioning | GO / CLOSED | Primary: Information Economics and Policy; JICT source-journal alternative; full candidate universe audited. |
| Stage 13 full-paper integration | RE-CERTIFIED GO / CLOSED | IEP manuscript, highlights, cover letter and declarations synchronized to repaired source/profit/endpoint/formal scope. |
| Stage 14 submission QA | CONDITIONAL PASS / CLOSED | Repaired local/package QA complete. Clean source rebuild, 22-page visual QA, artwork/font checks, preflight/reproducibility/Lean CI all pass. Authenticated Editorial Manager preflight remains required. |
| Stage 15 / actual submission | NOT ENTERED / PROHIBITED IN THIS WORKFLOW RUN | No submit action, payment, portal freeze, or final legal attestation performed. |

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

## Post-freeze state

No mathematical or scope gate remains open. The independent-audit repair invoked change control, the affected stages were re-certified, and theory is refrozen. Further substantive changes require rollback under `docs/THEORY_CHANGE_CONTROL.md`.


## Stage 7.5A evidence

* `results/stage075_full_theory_freeze_decision.md`
* `results/stage075a_scope_portability_redteam.md`
* `results/contribution_robustness_certificate.md`
* `results/claim_scope_ledger.md`
* `results/stage075a_formal_verification_certificate.md`
* `formal/Gss2012/Core.lean`
* `.github/workflows/lean-formal.yml`


## Stage 8 freeze evidence

* `results/stage08_canonical_theory_freeze.md`
* `results/stage08_theorem_registry.md`
* `results/stage08_counterexample_registry.md`
* `results/stage08_benchmark_selection_register.md`
* `docs/THEORY_CHANGE_CONTROL.md`


## Stage 9 reproducibility evidence

* `results/stage09_reproducibility_report.md`
* `docs/REPRODUCIBILITY.md`
* `requirements.txt`
* `Makefile`
* `.github/workflows/reproducibility.yml`
* `tests/test_frozen_regressions.py`
* `generated/manifest.json`
* `sources/SOURCE_MANIFEST.md`
* `theorem_certificates/INDEX.md`


## Stage 10 manuscript evidence

* `manuscript/main.tex`
* `manuscript/sections/01_introduction.tex` through `09_conclusion.tex`
* `manuscript/sections/A_uniform_proof.tex`
* `manuscript/sections/B_surplus_derivations.tex`
* `manuscript/sections/C_reproducibility.tex`
* `manuscript/references.bib`
* `results/stage10_figure_table_architecture.md`
* `results/stage10_claim_traceability.md`
* `code/audit_manuscript_claims.py`
* `sources/BIBLIOGRAPHY_PROVENANCE.md`


## Stage 11–14 evidence

* `results/stage11_referee_attack.md`
* `results/stage11_closure.md`
* `results/stage12_journal_positioning.md`
* `results/stage12_closure.md`
* `submission/journal_requirements_ledger.md`
* `results/stage13_integration_report.md`
* `results/stage13_closure.md`

## Stage 14 submission-QA evidence

* `results/stage14_visual_qa.md`
* `results/stage14_submission_qa.md`
* `results/stage14_closure.md`
* `code/build_submission_source_archive.py`
* `.github/workflows/stage14-submission-qa.yml`
* final repaired content head: `5908ae87ee6f00691ec304ccee134d708afc4a7e`
* final Stage-14 QA run: `35858273318` — SUCCESS
* final submission preflight: `35858273323` — SUCCESS
* final reproducibility regression: `35858273226` — SUCCESS
* final Lean regression: `35858273237` — SUCCESS
* final package artifact: `10748456861`

### Residual condition before any submission

Open the authenticated Information Economics and Policy Editorial Manager record, reconcile current file designations/anonymity/title-page/reviewer/declaration fields, and inspect the portal-generated review PDF. Until that is complete, the Stage-14 state remains **CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**.
