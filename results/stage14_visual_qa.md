# Stage 14 — Local Visual and Artwork QA

**Verdict:** PASS  
**Certified content head:** `4d7f316b7f0529f1f3685c38a0acc566b38566ad`  
**Final QA artifact:** GitHub Actions artifact `10737916503` from run `35831906641`.

## PDFs inspected

- manuscript: 20 pages;
- title page: 1 page;
- cover letter: 1 page.

All 20 manuscript pages were rendered to PNG and visually inspected. The first page, quantitative figure/counterexample page, Result-map table page, declarations/references pages, title page, and cover letter were additionally inspected at higher resolution.

## Manuscript visual result

PASS.

Observed:

- no clipped equations;
- no overlapping prose or mathematical displays;
- no broken glyphs or black squares;
- page numbering stable;
- propositions/equation labels readable;
- appendix equations fit the text block;
- declarations and bibliography render correctly;
- no blank accidental pages;
- margins remain consistent.

## Figure 1

PASS.

- plots the verified objects (x_H(s)), (ar x(s)), and (x_u(s));
- axes and mathematical labels readable;
- solid/dashed/dotted series distinguish the curves without relying on color alone;
- critical-point marker is visible;
- legend is readable and does not obscure the plotted result;
- caption states the certified pure-overlap interpretation;
- source is `generated/parameter_domains.csv`, regenerated and byte-compared in CI.

## Tables

PASS.

### Table 1

The exact counterexample values (5/6), (5/12), (25/72), (28/15), (2/5), (56/75), and gain (719/1800) are readable and consistent with the frozen regression.

### Table 2

The accepted-manuscript Results 1–7 impact map fits within the page, remains readable, and preserves the Stage-8 scope qualifications.

## Fonts / PDF structure

`pdffonts` reports `emb=yes` for every font used in the manuscript PDF.

Some pdfTeX-generated EC glyph sets appear as embedded Type-3 fonts; they render correctly in the review PDF and no current public Elsevier evidence retrieved at Stage 14 prohibits them for initial review. Editable LaTeX source is included in the source archive.

## Title page

PASS.

Author name, Independent Researcher affiliation, Matsuyama/Ehime/Japan address, email, ORCID, corresponding-author status, article type, target journal, funding, competing-interest and data/code statements are legible and internally consistent.

## Cover letter

The first Stage-14 render placed the signature alone on page 2. This presentation-only defect was corrected by using a 10pt letter with 0.8-inch margins.

Final state:

- one page;
- no clipping;
- target journal and title correct;
- contribution/scope wording consistent with the manuscript;
- sole-author signature/contact block fully visible.

## Visual-QA gate

**PASS.**
