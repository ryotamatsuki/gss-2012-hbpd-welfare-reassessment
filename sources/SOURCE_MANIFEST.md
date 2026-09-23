# Source Manifest

**Stage:** 9 reproducibility  
**Policy:** provenance records only. Copyrighted source PDFs are not committed.

| Source | Version / role | Public locator | Redistribution status | Local committed object |
|---|---|---|---|---|
| Gehrig, Shy & Stenbacka (2012), JICT, DOI 10.1007/s10842-011-0111-8 | publisher metadata / Version of Record bibliographic identity | DOI: 10.1007/s10842-011-0111-8 | publisher-controlled | metadata only |
| Hanken / DHANKEN institutional repository copy | post-referee accepted manuscript; controlling equation-level source | https://helda.helsinki.fi/server/api/core/bitstreams/6484e4b9-eeb4-4b72-ad79-99e2a817e16d/content | lawful public access; PDF not redistributed by this repo | sources/gss_2012_accepted_manuscript_comparison.md |
| HECER Discussion Paper No. 299, July 2010 | earlier complete author version / lineage cross-check | recorded in source-boundary notes | public working-paper provenance; PDF not redistributed here | sources/gss_2012_version_boundary.md |
| historical clean-room audit | hypothesis/regression provenance only | ryotamatsuki/ozshypapers, branch final-cleanroom-theorem-audit-20260919 | repository reference | no copied proof accepted as evidence |

## Integrity rules

1. sources/*.pdf and sources/private/ are gitignored.
2. Source-facing mathematical claims remain accepted-manuscript-qualified until exact Springer VOR body comparison is available.
3. No source PDF is required to run the mathematical reproducibility suite.
4. The Stage-9 CI fails if a PDF is committed under sources/.
