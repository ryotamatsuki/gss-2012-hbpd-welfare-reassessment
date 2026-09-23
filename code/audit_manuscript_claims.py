from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "manuscript").glob("**/*.tex"))
text = "\n".join(p.read_text(encoding="utf-8") for p in paths)

forbidden = {
    "unqualified Nash nonexistence": [
        r"no Nash equilibrium exists",
        r"Nash equilibrium does not exist",
    ],
    "formal scope inflation": [
        r"Lean proves the complete",
        r"formally proves the complete",
        r"formally verified the complete economic model",
    ],
    "VOR inflation": [
        r"the published Eq\.",
        r"the published equation",
        r"the Version of Record states",
    ],
}

failures = []
for label, patterns in forbidden.items():
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            failures.append(f"{label}: {pattern}")

required = [
    "pure-strategy",
    "accepted manuscript",
    "MODEL-SPECIFIC",
    "mixed",
    "selection",
    "PROOF-CRITICAL CORE",
]
for needle in required:
    if needle.lower() not in text.lower():
        failures.append(f"required scope phrase missing: {needle}")

if failures:
    print("manuscript claim-scope audit FAILED")
    for item in failures:
        print(" -", item)
    sys.exit(1)

print("manuscript claim-scope audit passed")
