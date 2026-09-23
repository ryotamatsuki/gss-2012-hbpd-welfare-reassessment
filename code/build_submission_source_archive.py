"""Build a clean, minimal submission-source archive for Stage 14."""

from __future__ import annotations
import hashlib, json, shutil, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "stage14"
PKG = OUT / "source_package"
ZIP = OUT / "gss2012_iep_submission_source.zip"

INCLUDE = [
    "manuscript/main.tex",
    "manuscript/references.bib",
    "manuscript/sections/01_introduction.tex",
    "manuscript/sections/02_model.tex",
    "manuscript/sections/03_uniform_equilibrium.tex",
    "manuscript/sections/04_hbp_comparisons.tex",
    "manuscript/sections/05_welfare.tex",
    "manuscript/sections/06_scope_robustness.tex",
    "manuscript/sections/07_related_literature.tex",
    "manuscript/sections/08_discussion.tex",
    "manuscript/sections/09_conclusion.tex",
    "manuscript/sections/A_uniform_proof.tex",
    "manuscript/sections/B_surplus_derivations.tex",
    "manuscript/sections/C_reproducibility.tex",
    "manuscript/sections/D_declarations.tex",
    "generated/parameter_domains.csv",
    "submission/title_page.tex",
    "submission/cover_letter.tex",
    "submission/highlights.txt",
    "submission/declarations.md",
]

if OUT.exists():
    shutil.rmtree(OUT)
PKG.mkdir(parents=True)

for rel in INCLUDE:
    src = ROOT / rel
    if not src.is_file():
        raise SystemExit(f"missing package input: {rel}")
    dst = PKG / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

manifest = {}
for p in sorted(x for x in PKG.rglob("*") if x.is_file()):
    rel = p.relative_to(PKG).as_posix()
    manifest[rel] = hashlib.sha256(p.read_bytes()).hexdigest()

(PKG / "PACKAGE_MANIFEST.json").write_text(
    json.dumps(
        {
            "stage": 14,
            "target_journal": "Information Economics and Policy",
            "files": manifest,
        },
        indent=2,
        sort_keys=True,
    ) + "\n",
    encoding="utf-8",
)

with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(x for x in PKG.rglob("*") if x.is_file()):
        z.write(p, p.relative_to(PKG).as_posix())

sha = hashlib.sha256(ZIP.read_bytes()).hexdigest()
(OUT / "SOURCE_ARCHIVE_SHA256.txt").write_text(f"{sha}  {ZIP.name}\n", encoding="utf-8")
print(f"built {ZIP} sha256={sha}")
