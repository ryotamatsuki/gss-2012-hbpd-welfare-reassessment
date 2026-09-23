# Theory Change Control after Stage 8

Stage 8 freezes the canonical theoretical object.

## Changes allowed without reopening theory

The following may proceed at Stages 9–14 provided mathematical content is unchanged:

- repository organization;
- deterministic build scripts and CI;
- manuscript exposition;
- notation cleanup that is provably equivalent;
- figure/table generation from frozen formulas;
- references and literature exposition consistent with Stage 6;
- journal formatting and positioning;
- declarations and submission files.

## Changes requiring rollback

| Proposed change | Earliest mandatory rollback |
|---|---|
| primitive utility, demand, timing, information, full-coverage assumption | Stage 4 or earlier |
| price strategy domain or equilibrium concept | Stage 4 |
| new pure or mixed equilibrium result | Stage 4 |
| change to \(x_H\), best-response partition, equality behavior | Stage 4 / 4A |
| new cross-model robustness/generality claim | Stage 7.5A |
| change to CS/profit/welfare formula or Result 1–7 classification | Stage 7 |
| change to mixed-equilibrium scope | Stage 3/4 as appropriate |
| change to strong-HBP selection convention | Stage 7 and 7.5A |
| stronger novelty claim / parent-theorem issue | Stage 6 |
| material change to formal theorem signature or assumptions | affected analytic stage + Stage 7.5A formal gate |
| unqualified VOR correction claim after new VOR evidence | Stage 1 source audit, then affected downstream source mappings |

## Formal certificate staleness

Any material change to a formalized definition or theorem makes \`results/stage075a_formal_verification_certificate.md\` stale. Stage 8 cannot remain frozen until Lean is rebuilt and statement fidelity is re-audited.

## Governance

No downstream journal preference may justify a theory change without explicit rollback.

No change may be made directly to \`main\` as part of this research line unless separately authorized.
