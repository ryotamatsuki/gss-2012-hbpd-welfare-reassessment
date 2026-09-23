"""Generate deterministic Stage-9 tables and diagnostic SVG figures.

These are reproducibility artifacts derived from the Stage-8 frozen formulas.
They are not publication-final figure architecture; Stage 10 may reformat them
without changing the underlying frozen data.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


def x_h(s: float) -> float:
    return 0.5 - s / 3.0 + math.sqrt(3.0 * s * (s + 6.0)) / 6.0


def x_bar(s: float) -> float:
    return (3.0 - s) / 4.0


def x_u(s: float) -> float:
    return 0.5 + s / 6.0


def s_critical() -> float:
    return -3.0 + 6.0 * math.sqrt(33.0) / 11.0


def fmt(v: float) -> str:
    return f"{v:.12f}"


def fmt2(v: float) -> str:
    """Platform-stable two-decimal rounding for positive SVG coordinates."""
    return f"{math.floor(v * 100 + 0.5) / 100:.2f}"


def write_parameter_csv(out: Path) -> None:
    path = out / "parameter_domains.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["s", "x_u", "x_H", "x_bar", "weak_pure_overlap"])
        for i in range(0, 1001):
            s = i / 1000.0
            if s >= 1.0:
                s = 0.999999999999
            xu, xh, xb = x_u(s), x_h(s), x_bar(s)
            overlap = int((s < s_critical()) and (xh < xb))
            w.writerow([fmt(s), fmt(xu), fmt(xh), fmt(xb), overlap])


def write_regression_csv(out: Path) -> None:
    path = out / "frozen_regressions.csv"
    rows = [
        ["REG-UPE-01", "25/72", "56/75", "719/1800", "positive"],
        ["REG-UPE-02", "6/47", "67/94", "x_H equality", "singleton Nash"],
        ["REG-CS-01", "99/100", "501/1000", "17993/4500000", "positive realized no-switch gap"],
        ["REG-CS-02", "1/10", "7/10", "Eq15=221/720; Eq16=-221/720", "source fidelity; Eq16 sign inconsistency"],
        ["REG-PROFIT-01", "1/2", "51/100", "-227/4500 vs 4/375", "realized no-switch gap vs switching extension"],
        ["REG-PROFIT-02", "9/10", "19/20", "41/900", "strong B profit gain; weak claim not portable"],
        ["REG-W-01", "x_bar=(3-s)/4", "", "-(1+s)(1+9s)/144", "negative"],
        ["REG-OVERLAP-01", "", "", "11s^2+66s-9=0", "s_c=-3+6sqrt(33)/11"],
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["id", "parameter_1", "parameter_2", "exact_result", "status"])
        w.writerows(rows)


def svg_header(width: int, height: int, title: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f"<title>{title}</title>",
        '<rect x="0" y="0" width="100%" height="100%" fill="white"/>',
        '<g font-family="sans-serif" font-size="14" fill="black" stroke="black">',
    ]


def write_domain_svg(out: Path) -> None:
    width, height = 900, 600
    left, right, top, bottom = 90, 840, 50, 520

    def X(s: float) -> float:
        return left + (right - left) * s

    def Y(x: float) -> float:
        return bottom - (bottom - top) * ((x - 0.5) / 0.5)

    xs = [i / 500.0 for i in range(0, 500)]
    xh_pts = " ".join(f"{X(s):.2f},{Y(x_h(s)):.2f}" for s in xs)
    xb_pts = " ".join(f"{X(s):.2f},{Y(x_bar(s)):.2f}" for s in xs)
    sc = s_critical()

    lines = svg_header(width, height, "Frozen parameter-domain boundaries")
    lines += [
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke-width="1.5"/>',
        f'<line x1="{left}" y1="{bottom}" x2="{left}" y2="{top}" stroke-width="1.5"/>',
        f'<polyline points="{xh_pts}" fill="none" stroke-width="2.5"/>',
        f'<polyline points="{xb_pts}" fill="none" stroke-width="1.5" stroke-dasharray="8 6"/>',
        f'<line x1="{X(sc):.2f}" y1="{bottom}" x2="{X(sc):.2f}" y2="{top}" stroke-width="1" stroke-dasharray="3 5"/>',
        f'<text x="{(left+right)/2:.1f}" y="570" text-anchor="middle">s = sigma/tau</text>',
        f'<text x="28" y="{(top+bottom)/2:.1f}" transform="rotate(-90 28 {(top+bottom)/2:.1f})" text-anchor="middle">x_0</text>',
        f'<text x="{X(0.63):.2f}" y="{Y(x_h(0.63))-12:.2f}">x_H(s)</text>',
        f'<text x="{X(0.20):.2f}" y="{Y(x_bar(0.20))-12:.2f}">x_bar(s)</text>',
        f'<text x="{X(sc)+8:.2f}" y="{top+20}">s_c={sc:.6f}</text>',
    ]
    for s_tick in [0, .2, .4, .6, .8, 1.0]:
        lines.append(f'<line x1="{X(s_tick):.2f}" y1="{bottom}" x2="{X(s_tick):.2f}" y2="{bottom+6}" stroke-width="1"/>')
        lines.append(f'<text x="{X(s_tick):.2f}" y="{bottom+24}" text-anchor="middle">{s_tick:.1f}</text>')
    for x_tick in [.5, .6, .7, .8, .9, 1.0]:
        lines.append(f'<line x1="{left-6}" y1="{Y(x_tick):.2f}" x2="{left}" y2="{Y(x_tick):.2f}" stroke-width="1"/>')
        lines.append(f'<text x="{left-12}" y="{Y(x_tick)+5:.2f}" text-anchor="end">{x_tick:.1f}</text>')
    lines += ["</g>", "</svg>"]
    (out / "figure_parameter_domains.svg").write_text("\n".join(lines) + "\n", encoding="utf-8")


def share_a_piecewise(d: float, x: float, s: float) -> float:
    L = -1 - s
    alpha = 2 * x - 1 - s
    beta = 2 * x - 1 + s
    U = 1 + s
    if d <= L:
        return 0.0
    if d < alpha:
        return (d + 1 + s) / 2.0
    if d <= beta:
        return x
    if d < U:
        return (d + 1 - s) / 2.0
    return 1.0


def write_demand_svg(out: Path) -> None:
    width, height = 900, 600
    left, right, top, bottom = 90, 840, 50, 520
    x, s = 0.70, 0.10
    L, alpha, beta, U = -1 - s, 2 * x - 1 - s, 2 * x - 1 + s, 1 + s
    dmin, dmax = -1.5, 1.5

    def X(d: float) -> float:
        return left + (right - left) * (d - dmin) / (dmax - dmin)

    def Y(q: float) -> float:
        return bottom - (bottom - top) * q

    ds = [dmin + (dmax - dmin) * i / 600.0 for i in range(601)]
    pts = " ".join(
        f"{fmt2(X(d))},{fmt2(Y(share_a_piecewise(d, x, s)))}" for d in ds
    )

    lines = svg_header(width, height, "Uniform-price demand regimes")
    lines += [
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke-width="1.5"/>',
        f'<line x1="{left}" y1="{bottom}" x2="{left}" y2="{top}" stroke-width="1.5"/>',
        f'<polyline points="{pts}" fill="none" stroke-width="2.5"/>',
        f'<text x="{(left+right)/2:.1f}" y="570" text-anchor="middle">d = (p_B-p_A)/tau</text>',
        f'<text x="28" y="{(top+bottom)/2:.1f}" transform="rotate(-90 28 {(top+bottom)/2:.1f})" text-anchor="middle">q_A(d)</text>',
        f'<text x="{right-10}" y="{top+20}" text-anchor="end">diagnostic x_0=0.70, s=0.10</text>',
    ]
    for value, label in [(L,"L"),(alpha,"alpha"),(beta,"beta"),(U,"U")]:
        lines.append(f'<line x1="{fmt2(X(value))}" y1="{bottom}" x2="{fmt2(X(value))}" y2="{top}" stroke-width="1" stroke-dasharray="4 5"/>')
        lines.append(f'<text x="{fmt2(X(value))}" y="{bottom+24}" text-anchor="middle">{label}</text>')
    for q in [0,.25,.5,.75,1.0]:
        lines.append(f'<line x1="{left-6}" y1="{fmt2(Y(q))}" x2="{left}" y2="{fmt2(Y(q))}" stroke-width="1"/>')
        lines.append(f'<text x="{left-12}" y="{fmt2(Y(q)+5)}" text-anchor="end">{q:.2f}</text>')
    lines += ["</g>", "</svg>"]
    (out / "figure_uniform_demand_regimes.svg").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifest(out: Path) -> None:
    files = sorted(p for p in out.iterdir() if p.name != "manifest.json")
    data = {
        "generator": "code/generate_stage09_artifacts.py",
        "stage": 9,
        "theory_freeze": "Stage 8",
        "files": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files
        },
    }
    (out / "manifest.json").write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="generated")
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    write_parameter_csv(out)
    write_regression_csv(out)
    write_domain_svg(out)
    write_demand_svg(out)
    write_manifest(out)
    print(f"generated {len(list(out.iterdir()))} deterministic Stage-9 artifacts in {out}")


if __name__ == "__main__":
    main()
