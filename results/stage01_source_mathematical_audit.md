# Stage 1 — Source & mathematical audit

**Canonical verdict:** RE-CERTIFIED GO after 2026-09-23 source-fidelity re-audit, with an explicit accepted-manuscript/VOR wording boundary.  
**Input project SHA:** `7c10043ad91f67505c68bf0f99f3b51263a041fb`  
**Evidence snapshot before this report:** `118c5eba7c566d617d7edec185b0352e507d1d5e`  
**Workflow:** `research-paper-workflow` main `63f11a50a13d9328213498a5a6576d00b9bceef7` (pipeline v2.4; `GOVERNANCE.md` still displays v2.3, preserved as a workflow-repository inconsistency).  
**Production branch:** `research/stage-04-uniform-price-game`

## 1. Source lineage

The source gate is no longer limited to HECER 2010. A lawful Hanken/DHANKEN institutional copy explicitly identifies itself as the **post-referee accepted manuscript** of the 2012 JICT article. It is now the controlling equation-level source. The Springer VOR body remains subscription-restricted in the current environment, so every discrepancy claim remains version-qualified to the accepted manuscript.

See:

* `sources/gss_2012_version_boundary.md`
* `sources/gss_2012_accepted_manuscript_comparison.md`

No copyrighted article PDF is committed.

## 2. Source-faithful result ledger

The accepted manuscript contains seven numbered Results:

| Source result | Subject | Stage-1 status |
|---|---|---|
| Result 1 | `σ>τ` and profitable history-based poaching | outside maintained Assumption 1 after it is imposed; no correction claim |
| Result 2 | dominant firm's share larger under uniform pricing | qualitative sign survives; displayed weak-branch share difference is algebraically wrong |
| Result 3 | weak-dominance consumer-surplus iff condition (17) | formula/branch error; the stated reversal is not reproduced by primitive integration |
| Result 4 | weak-dominance small-firm profit comparison | downstream equilibrium interpretation restricted by corrected uniform pure-equilibrium domain |
| Result 5 | weak-dominance social welfare higher under uniform pricing | sign survives on branch-correct accounting; accepted-manuscript endpoint substitution is algebraically wrong |
| Result 6 | strong-dominance consumer-surplus threshold | source formula is branch-sensitive; outside uniform pure-existence region it is only a profile comparison |
| Result 7 | strong-dominance social welfare higher under uniform pricing | sign survives branch-correct accounting; equilibrium interpretation restricted to corrected uniform pure-existence region |

Earlier project shorthand “Results 1–5” for the downstream objects is retired.

## 3. Equation inventory and audit routing

The complete mathematical inventory was reconstructed by section and purpose. Critical formulas were independently re-derived; noncritical equations are retained as source mappings rather than presumed proofs.

| Equation(s) | Object | Audit status |
|---|---|---|
| (1) | four primitive HBP utilities | reconstructed from primitives |
| (2) | HBP history-segment indifference cutoffs | reconstructed and clipped |
| (3) | HBP profits | reconstructed by segment |
| (4) | weak-HBP loyalty prices | reproduced |
| (5) | weak-HBP poaching prices | reproduced |
| (6) | weak-HBP equilibrium cutoffs | reproduced |
| (7) | weak-HBP market shares | reproduced; comparison immediately before Result 2 is inconsistent with these shares |
| (8) | downstream weak-HBP share/profit expression in source sequence | checked as part of HBP branch ledger |
| (9) | strong-HBP price profile with `q_A=c` | reproduced under the nonnegative-margin/no-loss convention; unrestricted prices create a payoff-equivalent zero-sales family described below |
| (10) | strong-HBP allocation / shares | reproduced |
| (11) | uniform-price primitive utility | reconstructed with both history states, including the B→A option omitted from the source's preferred allocation picture |
| (12) | uniform-price candidate and share | local FOC solution reproduced; global Nash claim fails outside the exact domain characterized at Stage 4/4A |
| (13) | uniform CS integral | one-way-switch allocation integral; valid only when its stated switching interval is correctly ordered, and not an actual-allocation integral when `x_0<x_u` |
| (14) | weak-HBP CS integral | reconstructed directly from primitive utilities |
| (15) | weak CS difference | image-level re-transcription confirms the accepted display equals the primitive one-way-switch CS difference on `x_0≥x_u` |
| (16) | normalized sign display | after `σ=sτ`, the accepted display is the negative of Eq. (15)'s normalized left-hand side; this is the source algebraic sign error |
| (17) | weak-CS sign condition | inherits the Eq. (16) sign inversion and does not survive branch-correct primitive integration |
| (18) | uniform firm profits | valid only as equilibrium profits on the corrected pure-equilibrium domain |
| (19) | weak-HBP firm profits | reproduced on its source branch |
| (20)–(22) | weak aggregate / firm-specific profit comparisons | algebra may be evaluated as profile comparisons, but equilibrium wording inherits the corrected uniform pure-equilibrium domain |
| (23) | weak uniform welfare | switching-branch formula; branch qualification required |
| (24) | weak HBP welfare | primitive resource accounting reproduced |
| (25) | weak welfare difference | formula reproduced on the switching branch; the following endpoint substitution in the accepted manuscript is algebraically incorrect |
| (26)–(28) | strong-dominance CS/profit sequence | reconstructed with an additional uniform no-switch branch where applicable |
| post-(28) strong welfare expression | strong welfare difference / Result 7 | reconstructed directly from transport and switching resource costs |

The accepted manuscript's equation numbering in the final strong-dominance pages is visually sparse in extracted text; manuscript-facing claims cite the source page/result as well as the equation number where unambiguous. This does not affect any headline correction.

## 4. Uniform-price full demand

With
[
s=sigma/	au,quad a=(p_A-c)/	au,quad b=(p_B-c)/	au,quad d=b-a,
]
the two primitive thresholds are
[
t_A=(d+1+s)/2,qquad t_B=(d+1-s)/2.
]
The exact clipped share is
[
q_A(d)=operatorname{clip}(t_A,0,x_0)+operatorname{clip}(t_B-x_0,0,1-x_0).
]

For `0<s<1`, define
[
L=-1-s,quad alpha=2x_0-1-s,quad eta=2x_0-1+s,quad U=1+s.
]
This yields the exhaustive five-piece partition: full B capture; A→B-only switching; no-switch plateau; B→A-only switching; full A capture. Simultaneous two-way switching is impossible because `t_A-t_B=s>0`.

## 5. Exact regression A

At
[
(	au,sigma,x_0,c)=(1,1/2,3/5,0),
]
the accepted-manuscript Eq. (12) candidate is
[
(p_A,p_B)=(7/6,5/6).
]
Firm B earns `25/72`. The positive-price deviation `p'_B=28/15` moves to the no-poaching kink and yields `56/75`, a gain
[
719/1800>0.
]
This clean-room exact arithmetic regression survives.

## 6. Eq. (15) regression correction

The earlier upstream audit's proposed negative CS point
[
s=99/100,quad x_0=501/1000
]
does **not** reproduce. It lies below
[
x_u=1/2+s/6,
]
where the actual uniform allocation has no switching. Direct primitive integration gives a positive gap, not the previously claimed negative value.

A valid one-way-switch point such as `s=1/10,x_0=7/10` confirms that the accepted-manuscript Eq. (15) is nevertheless algebraically wrong: the primitive integral and printed formula differ exactly, but both have the same positive sign there.

Thus the Stage-1 correction is:

* **formula error:** survives;
* **upstream claimed exact sign-reversal regression:** rejected;
* **accepted-manuscript Result-3 reversal region:** not supported by branch-correct primitive integration.

This negative finding is permanent project evidence.

## 7. HBP audit

The weak-HBP interior solution is reproduced from the two independent history segments, including global comparison with their capture boundaries.

The strong-HBP source member `q_A=c` is reproduced under a nonnegative-margin/no-loss strategy convention. If prices below marginal cost are admitted, the B-history segment has a payoff-equivalent zero-sales family. In normalized margins `u=(q_A-c)/τ`:
[
3-s-4x_0le ule0,qquad
(p_B-c)/	au=u+2x_0-1+s.
]
All members have the same no-poaching allocation and the same social welfare, but prices, profits, and consumer surplus redistribute with `u`. Under the natural restriction `p_i,q_ige c`, the family collapses to the source member `u=0`.

This is a strategy-domain/selection qualification, not evidence that the source HBP allocation fails.

## 8. Welfare primitive accounting

With full market coverage,
[
W=CS+pi_A+pi_B
=eta-c-	auint_0^1|z-y(z)|,dz-sigma N_{m sw}.
]
Prices cancel as transfers. This identity is reproduced against the direct consumer-surplus and profit evaluators.

The weak and strong welfare signs in the accepted manuscript can survive even when their displayed profile formulas require branch correction. No equilibrium welfare is assigned to the parameter region where the uniform game has no pure equilibrium.

## 9. Prior-correction preliminary search

Exact-title searches for erratum, correction, corrigendum, comment, reply, and DOI-plus-correction did not identify a prior correction to this article. RePEc's “Corrections” footer is its generic metadata-correction facility, not a corrigendum. Forward-citation records and later HBP literature identify the 2012 article as prior work but, in the searches completed here, do not report the `x_H(s)` correction.

Full theorem-absorption/novelty certification is Stage 2/6, not asserted here.

## 10. Stage-1 gate

**RE-CERTIFIED GO.** The project has an authoritative post-referee mathematical source, an image-rechecked Eqs. (13)–(17) transcription, a source-faithful result ledger, independent primitive reconstruction, exact counterexample regressions, and an explicit VOR wording boundary.

The residual lack of direct VOR equation access does not block research under the user-specified fallback rule because the accepted manuscript is available and all discrepancy language remains version-qualified. It does block upgrading any statement to an unqualified claim about the exact Springer typeset VOR.
