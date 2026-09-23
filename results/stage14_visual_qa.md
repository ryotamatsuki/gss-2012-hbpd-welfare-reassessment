# Stage 14 — Local Visual and Artwork QA

**Verdict:** PASS — RE-INSPECTED AFTER INDEPENDENT-AUDIT REPAIR  
**Certified repaired content head:** `5908ae87ee6f00691ec304ccee134d708afc4a7e`  
**Final QA artifact:** GitHub Actions artifact `10748456861` from run `35858273318`.

## PDFs inspected

- manuscript: **22 pages**;
- title page: 1 page;
- cover letter: 1 page.

All 22 manuscript pages were rendered to PNG by the final Stage-14 run. The complete page set was inspected as a contact sheet, with Figure 1/Table 1 (page 7) and Table 2 (page 11) inspected at full size. The title page and one-page cover letter were separately rendered and inspected at full size.

## Manuscript visual result

PASS.

Observed:

- no clipped equations;
- no overlapping prose or displays;
- no broken glyphs or black squares;
- no accidental blank pages;
- page numbering and margins consistent;
- appendix equations fit the text block;
- declarations and bibliography render correctly.

## Figure 1

PASS.

The legend is readable and does not cover the substantive curves; the (s_c) marker/vertical reference and the narrow weak/pure-overlap geometry remain visible. Line styles distinguish the series without relying on color alone, and the caption states the certified overlap interpretation.

## Tables

PASS.

### Table 1

The caption includes the full counterexample parameter tuple ((	au,sigma,x_0,c)=(1,1/2,3/5,0)). The exact candidate/deviation values and (719/1800) gain are legible.

### Table 2

The repaired Results 1–7 classification fits on the page. Result 4 is explicitly branch-specific outside the weak pure overlap; Result 6 separates (x_0<1) from the (x_0=1) empty-market endpoint.

## Fonts / PDF structure

The final Stage-14 font audit passed: all manuscript fonts are embedded. PDF structural QA passed.

## Title page

PASS. Author/contact, affiliation, ORCID, corresponding-author status, target journal, article type, funding, competing-interest, and data/code text are legible.

## Cover letter

PASS. One page, no clipping or overflow, and the source-fidelity/profit-scope wording matches the repaired manuscript.

## Visual-QA gate

**PASS.**
