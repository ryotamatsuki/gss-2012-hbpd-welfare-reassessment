# Stage 0 — Evidence Freeze

## Objective

Establish a self-contained evidentiary base before any publication-facing correction claim is frozen.

## Bibliographic identity

Thomas Gehrig, Oz Shy, and Rune Stenbacka, “A Welfare Evaluation of History-Based Price Discrimination,” *Journal of Industry, Competition and Trade* 12(4), 373–393 (December 2012), DOI `10.1007/s10842-011-0111-8`.

The current Springer page reports received 17 November 2010, revised 11 April 2011, accepted 1 June 2011, and online publication 28 June 2011. Publisher metadata and abstract have been inspected; full VOR mathematical text has not.

## Mathematical-source lineage

Equation-level reconstruction uses HECER Discussion Paper No. 299 (July 2010), complete 25-page author version. The public HELDA bitstream URL, access date, PDF page map, redistribution status, and VOR qualification are in `sources/gss_2012_version_boundary.md`. No copyrighted PDF is committed. HECER 2010 findings are not attributed to the VOR unless later version comparison verifies them.

## Independent reproduction status

The uniform game has been reconstructed from primitive utility differences in the local research workspace. The exact positive-price regime-crossing deviation at ((\tau,\sigma,x_0,c)=(1,1/2,3/5,0)) reproduces with exact fractions, and a clean-room Python regression passes. See `code/uniform_game_cleanroom.py` and `derivations/uniform_price_game_full_demand.md`.

Primitive CS integration has also been independently implemented. It shows that the upstream negative CS value at ((s,x_0)=(99/100,501/1000)) was an invalid branch extension; direct integration is positive. The HECER Eq. (15) display remains false on a valid switching branch. See `derivations/consumer_surplus_primitive_reconstruction.md`.

These are preliminary, version-qualified findings. They do not close the full model inventory, Stage 4A, or theorem freeze.

## Prior-disclosure search

Preliminary searches covered exact title variants with erratum/correction/corrigendum/comment/reply, DOI with correction, author pages, RePEc, and later HBP work. No direct correction was surfaced in those searches. This is not an exhaustive novelty clearance; the complete Stage 2 search and final-claim re-kill remain open.

## Unresolved evidence

1. Obtain and compare the VOR body or a lawful authoritative post-referee manuscript against HECER Eqs. (11)–(12), Results 1–3, Eqs. (13)–(15), Eqs. (21)–(23), Results 4–5, Figure 5, abstract, introduction, and conclusion.
2. Close the prior-disclosure search against the actual surviving pure-equilibrium theorem and welfare claims.
3. Complete the source-to-equation inventory and distinguish author-version transcription from VOR statements.

## Verdict

**HOLD — Stage 0 not closed.** The source-specific mathematical signal is independently reproducible in the HECER 2010 version, but the prior-disclosure audit is preliminary and VOR body comparison is unresolved. Exploratory Stage 4 derivations may proceed as research notes, but cannot be frozen or presented as a VOR correction.
