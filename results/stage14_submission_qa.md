# Stage 14 — Submission QA

**Final state:** CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED  
**Target journal:** Information Economics and Policy  
**Certified content head:** `4d7f316b7f0529f1f3685c38a0acc566b38566ad`  
**Theory change:** NONE  
**Stage 15 / actual submission:** NOT PERFORMED.

## 1. Final automated QA

All final research/package workflows pass on the certified content head:

| Gate | Run | Result |
|---|---:|---|
| Stage-14 submission QA | 35831906641 | SUCCESS |
| Stage-13/14 submission preflight | 35831906612 | SUCCESS |
| Stage-9 reproducibility regression | 35831906606 | SUCCESS |
| Lean formal verification regression | 35831906623 | SUCCESS |

The Stage-14 QA run verifies:

- full manuscript build;
- title-page build;
- cover-letter build;
- minimal source archive creation;
- extraction of that archive into a clean directory;
- manuscript/title/cover compilation using only extracted package files;
- PDF structural inspection;
- embedded-font audit;
- rendering of every manuscript page;
- submission-package audit;
- manuscript claim/scope audit;
- exact clean-room regressions;
- symbolic reconstruction;
- downstream symbolic identities;
- unresolved-reference / placeholder scan;
- final file checksums;
- final QA artifact upload.

## 2. Final package provenance

GitHub Actions artifact:

- name: `stage14-final-package`;
- artifact ID: `10737916503`;
- run: `35831906641`;
- artifact digest: `sha256:4a31656c5f074f802e23462ebfce0d3f1593d4323b4304c88ed3847c869d1226`.

Final files and SHA-256:

| File | SHA-256 |
|---|---|
| manuscript PDF | `b6ed1479d4917724198ae91abe04119510d4fd04d6cba208c4226778cb230471` |
| title-page PDF | `6ce7fbd8c8244bb4fa5b793299c9f48a696cb0c7a577d1cba9b38c87ca4d7208` |
| cover-letter PDF | `0c9cd3f0f645c427f1ebb787ba1e1b1b800edaa56f4ef873b44b3401204ef0e2` |
| minimal source archive | `b88b70cf797e1eb11e32525373ff0b89e026e5409af0e20c021e6f9b2dcdf80e` |

The final manuscript is 20 pages. The title page and cover letter are each one page.

## 3. Source-package completeness

PASS.

The minimal source archive contains:

- manuscript main TeX;
- every manuscript section;
- bibliography source;
- generated parameter-domain data required by Figure 1;
- title-page source;
- cover-letter source;
- highlights;
- declarations;
- package manifest.

It excludes internal audit reports and copyrighted source PDFs.

The archive was extracted to a fresh directory in CI and successfully rebuilt without hidden repository paths.

## 4. Numerical and theoretical integrity

PASS.

Final CI re-runs:

- exact primitive clipped-demand / global-deviation regressions;
- exact (719/1800) counterexample;
- equality threshold checks;
- weak-CS exact regressions;
- welfare identities;
- strong-HBP selection regressions;
- independent SymPy primitive reconstruction;
- Stage-7 downstream symbolic identities;
- Lean 4.19.0 / pinned mathlib proof-critical core.

No Stage-8 frozen theorem, quantifier, domain, selection convention, or Results 1–7 classification changed during Stages 10–14.

## 5. Manuscript metadata / declarations

PASS at package level.

- title finalized;
- sole author / affiliation / corresponding author synchronized;
- email and ORCID synchronized;
- abstract: 206 words;
- keywords: 6;
- highlights: 5, each <=85 characters;
- funding statement present;
- competing-interest statement present;
- data/code statement present;
- CRediT statement present;
- Elsevier-style GenAI disclosure present immediately before references;
- AI-assisted research-process disclosure also appears in the reproducibility appendix;
- no TBD/TODO/FIXME/PLACEHOLDER text;
- no unresolved citations or references.

## 6. Figure / table / artwork QA

PASS.

See `results/stage14_visual_qa.md`.

- Figure 1 is reproducibly generated from frozen verified data;
- series remain distinguishable by line style;
- Figure 1 and Tables 1–2 were visually inspected;
- no clipping/overflow affecting legibility;
- all manuscript PDF fonts are embedded;
- figure/table interpretation matches the frozen proposition domains.

## 7. Current journal-requirements evidence

The journal requirements ledger has been reverified on 2026-09-23.

Current public evidence verifies:

- IEP identity/scope/article-family from the official Elsevier IEP page;
- active Information Economics and Policy Editorial Manager portal;
- current Elsevier GenAI disclosure policy;
- current Elsevier LaTeX/source-file guidance;
- current Elsevier artwork/file-format and accessibility guidance;
- current publisher-wide author-policy/declaration expectations.

The package conservatively satisfies the stricter known IEP highlight/keyword constraints from the last fully indexed journal-specific Author Information Pack and current secondary corroboration.

## 8. Residual authenticated-portal dependency

The live IEP journal-specific Guide body is linked from Elsevier but returns HTTP 403 in the automated environment. Several operative details are therefore correctly classified as authenticated/current-portal preflight items rather than guessed facts:

- current manuscript identification/anonymity setting;
- exact file-designation menu;
- separate title-page handling;
- reviewer-suggestion fields if required;
- any submission-fee field/status;
- any live IEP-specific override of highlight/keyword/file rules;
- portal author/affiliation/corresponding-author metadata;
- portal declaration fields;
- portal-generated review PDF.

Before any actual submit action, the authenticated Editorial Manager record must be opened, these fields reconciled, and the portal-generated review PDF inspected page by page.

This is the only remaining submission-readiness dependency.

## 9. Stage-14 decision

Under the canonical workflow's authenticated-portal rule, the correct state is:

**CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**

This is a closed Stage-14 research/package QA state, not a claim that the paper has been submitted.

No substantive correction remains pending. No fatal referee attack remains unresolved. The research, manuscript, reproducibility, formal-verification, and local submission package are complete.

**Stage 15 is not entered. No submit button was clicked.**
