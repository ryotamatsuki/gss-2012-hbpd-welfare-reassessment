"""Fail-closed Stage-13/14 submission package checks."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = (ROOT / "manuscript/main.tex").read_text(encoding="utf-8")
MANUSCRIPT_TEXT = "\n".join(
    p.read_text(encoding="utf-8")
    for p in sorted((ROOT / "manuscript").glob("**/*.tex"))
)
DECL = (ROOT / "manuscript/sections/D_declarations.tex").read_text(encoding="utf-8")
HIGHLIGHTS = [
    line.strip()
    for line in (ROOT / "submission/highlights.txt").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
COVER = (ROOT / "submission/cover_letter.tex").read_text(encoding="utf-8")
TITLE = (ROOT / "submission/title_page.tex").read_text(encoding="utf-8")

assert 3 <= len(HIGHLIGHTS) <= 5, HIGHLIGHTS
for bullet in HIGHLIGHTS:
    assert len(bullet) <= 85, (len(bullet), bullet)

profit_highlights = [b for b in HIGHLIGHTS if "smaller firm" in b.lower()]
assert len(profit_highlights) == 1, profit_highlights
assert "weak" in profit_highlights[0].lower(), profit_highlights[0]

abstract_match = re.search(
    r"\\begin\{abstract\}(.*?)\\end\{abstract\}", MAIN, flags=re.S
)
assert abstract_match
abstract = re.sub(r"\\[a-zA-Z]+(?:\[[^\]]*\])?", " ", abstract_match.group(1))
abstract = re.sub(r"[{}$\\^_~=]+", " ", abstract)
abstract_words = re.findall(r"\b[\w.-]+\b", abstract)
assert len(abstract_words) <= 250, len(abstract_words)

kw_match = re.search(r"\\textbf\{Keywords:\}\s*(.*?)\\\\", MAIN, flags=re.S)
assert kw_match
keywords = [x.strip() for x in kw_match.group(1).split(";") if x.strip()]
assert 1 <= len(keywords) <= 6, keywords

required_main = [
    "Declaration of generative AI and AI-assisted technologies",
    "This research received no external funding",
    "The author declares no competing interests",
    "No empirical datasets were generated or analysed",
    "PROOF-CRITICAL CORE",
    "accepted manuscript",
    "pure-strategy",
    "Eq.~(16)",
    "corrected weak-dominance pure-equilibrium overlap",
]
combined = MANUSCRIPT_TEXT + "\n" + DECL
for phrase in required_main:
    assert phrase in combined, phrase

for phrase in [
    "Information Economics and Policy",
    "Ryota Matsuki",
    "ryota.matsuki@gmail.com",
    "0009-0005-2329-531X",
]:
    assert phrase in COVER + "\n" + TITLE, phrase

assert "weak-dominance pure-equilibrium overlap" in COVER
assert "accepted Eq.~(15) matches the switching branch" in MAIN
assert "Eq.~(16) reverses its sign" in MAIN
assert "1279/3600" not in MANUSCRIPT_TEXT + "\n" + COVER
assert "source member is unique under the nonnegative-margin" not in combined
assert "family collapses to the source member" not in combined

for p in [ROOT / "manuscript", ROOT / "submission"]:
    for file in p.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".tex", ".md", ".txt", ".bib"}:
            data = file.read_text(encoding="utf-8", errors="replace")
            assert not re.search(r"\b(TBD|TODO|PLACEHOLDER)\b", data, flags=re.I), file

print(
    f"submission audit passed: abstract={len(abstract_words)} words, "
    f"keywords={len(keywords)}, highlights={len(HIGHLIGHTS)}"
)
