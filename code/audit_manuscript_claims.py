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
    "retired Eq15 diagnosis": [
        r"Eq\.?~?\(15\).{0,50}(algebraically wrong|formula error|incorrect)",
        r"printed Eq\.?~?\(15\).{0,80}1279/3600",
        r"1279/3600",
    ],
    "strong-HBP uniqueness inflation": [
        r"source member is unique under the nonnegative-margin",
        r"family collapses to the source member",
    ],
}

failures = []
for label, patterns in forbidden.items():
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            failures.append(f"{label}: {pattern}")

required = [
    "pure-strategy",
    "accepted manuscript",
    "MODEL-SPECIFIC",
    "mixed",
    "selection",
    "PROOF-CRITICAL CORE",
    "Eq.~(16)",
    "weak pure",
    "x_0=1",
]
for needle in required:
    if needle.lower() not in text.lower():
        failures.append(f"required scope phrase missing: {needle}")

# Any affirmative smaller-firm profit claim must be scoped to weak dominance,
# or explicitly explain that the weak sign does not extend to strong dominance.
for sentence in re.split(r"(?<=[.!?])\s+", text):
    low = sentence.lower()
    if "smaller firm" in low and ("earns less" in low or "profit" in low):
        if not any(tag in low for tag in ["weak", "strong", "does not", "not extend", "counterexample"]):
            failures.append("smaller-firm weak-scope guard: " + sentence[:180])

if failures:
    print("manuscript claim-scope audit FAILED")
    for item in failures:
        print(" -", item)
    sys.exit(1)

print("manuscript claim-scope audit passed")
