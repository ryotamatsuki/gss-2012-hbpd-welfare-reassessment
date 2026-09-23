# Stage 14 — Submission QA

**Final state:** CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED  
**Target journal:** Information Economics and Policy  
**Certified repaired content head:** `5908ae87ee6f00691ec304ccee134d708afc4a7e`  
**Independent-audit remediation:** COMPLETE for B1–B7  
**Stage 15 / actual submission:** NOT PERFORMED.

## 1. Final automated QA

All repaired-head workflows pass:

| Gate | Run | Result |
|---|---:|---|
| Stage-14 submission QA | `35858273318` | SUCCESS |
| Stage-13/14 submission preflight | `35858273323` | SUCCESS |
| Stage-9 reproducibility regression | `35858273226` | SUCCESS |
| Lean formal verification regression | `35858273237` | SUCCESS |

The Stage-14 run builds the manuscript/title page/cover letter, creates and clean-rebuilds the minimal source archive, checks PDF structure/font embedding, renders every manuscript page, audits submission/claim scope, runs the repaired exact/symbolic/unittest suite, regenerates and byte-compares committed artifacts, checks unresolved references/placeholders, records checksums, and uploads the final package.

## 2. Final package provenance

GitHub Actions artifact:

- name: `stage14-final-package`;
- artifact ID: `10748456861`;
- run: `35858273318`;
- artifact digest: `sha256:136e820ccd8592fcc0884f55432e0e74ccf10c2d4608000ef4f0d80bfdb613c1`.

Final files:

| File | SHA-256 |
|---|---|
| manuscript PDF | `002798ea4f5c657036ef30fb721dcfcca78c4e8fdcad5db0b1ac104b7a0bf942` |
| title-page PDF | `8455504f48fa290341d6d4dc6d381292c6dde43f43ac6e755b3590c2231d90bd` |
| cover-letter PDF | `a9567636d7e84ac061e8280b00a3f934566421effe971bfcf3a206a4fce53060` |
| minimal source archive | `9223d6c4d7b224a7fcaea0a589cd9d632d02fe443e35221f666dcb2d04f52fb9` |

The final manuscript is **22 pages**. The title page and cover letter are each one page.

## 3. Independent-audit remediation closure

B1–B7 are closed in `results/independent_submission_audit_remediation_20260923.md`.

Most importantly:

- accepted Eq. (15) is no longer falsely labelled erroneous; Eq. (16)'s sign inversion and the branch-extension problem are separated;
- weak Result 4 profits use realized piecewise demand outside the pure overlap;
- the smaller-firm loss claim is weak-domain only;
- (x_0=1) strong-HBP unused prices are treated as nonunique while realized outcomes are unique;
- Appendix A closes capture/margin, (s=0), (x_0=1), kink, and reverse-branch obligations;
- Lean statement fidelity and sentinel guards are repaired and rebuilt;
- the Umezawa corrigendum and nearby-model scope distinctions are integrated without an unsupported non-nesting theorem.

The central pure uniform-price threshold theorem and exact Eq. (12) counterexample are unchanged.

## 4. Numerical, formal, and reproducibility integrity

PASS.

The repaired head re-runs primitive clipped demand/global deviations, the exact (719/1800) witness, equality threshold, Eq. (15)/(16) source-fidelity regressions, weak no-switch profit witness, welfare identities, strong-HBP endpoint/selection regressions, independent SymPy checks, deterministic artifact regeneration, and Lean 4.19.0 with pinned mathlib.

Stage-8 change control was invoked for the audit repair and the theory freeze was re-established after the affected claims/certificates were corrected.

## 5. Manuscript metadata / declarations

PASS at package level.

- abstract: 208 words;
- keywords: 6;
- highlights: 5, each <=85 characters;
- author/title-page/cover-letter metadata synchronized;
- funding, competing interests, data/code, CRediT, and GenAI disclosures present;
- no TBD/TODO/FIXME/PLACEHOLDER text;
- no unresolved citations or references.

## 6. Figure / table / artwork QA

PASS. See `results/stage14_visual_qa.md`.

The repaired 22-page PDF was rendered page-by-page. Figure 1, Table 1, Table 2, title page, and cover letter were inspected at full size; the complete manuscript was also inspected as an all-page contact sheet. No clipping, overlap, broken glyph, accidental blank page, or material legibility defect was found.

## 7. Residual authenticated-portal dependency

The sole remaining pre-submission condition is the authenticated Information Economics and Policy Editorial Manager preflight:

1. inspect current required fields and file designations;
2. confirm anonymity/title-page handling;
3. reconcile author, funding, COI, CRediT, AI, data/code, and prior-publication fields;
4. satisfy reviewer fields if the portal requests them;
5. inspect the portal-generated review PDF;
6. resolve any conflict with the current requirements ledger.

## 8. Stage-14 decision

**CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED.**

No substantive correction remains pending in the repository/package. No Stage 15 action or actual submission has occurred.
