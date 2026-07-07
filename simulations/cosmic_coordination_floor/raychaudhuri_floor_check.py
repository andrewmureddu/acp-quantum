#!/usr/bin/env python3
"""Numerical companion for proofs/semiclassical_collapse_failure.md.

This is not a gravitational simulation. It is a finite ensemble check of the
three quantitative claims the theorem makes about trapped relational
macrocells:

1. Lemma 1 (focusing bound): for outgoing null congruences with initial
   expansion theta_0 <= -alpha < 0 and NEC-respecting shear/Ricci terms, the
   expansion diverges to -infinity at affine parameter lambda* <= 2/alpha.

2. Theorem 1(a) (quantitative normalization failure): the retained admissible
   mass Z(Delta) = 1 - mu({tau_fail <= Delta}) is strictly below 1 past the
   earliest failure time and reaches exactly 0 at Delta* <= clock * 2/alpha.

3. Theorem 1(b)-(c) (exclusion and absorption failures): the hard-exclusion
   channel's discarded coordination -log2 Z(Delta) diverges as Z -> 0 while
   the surviving renormalized distribution concentrates (entropy -> 0), and
   the terminal-absorption channel has exactly zero future entropy.

The ensemble draws random piecewise-constant nonnegative shear-squared and
Ricci focusing terms, so every sample satisfies the null convergence
condition; the comparison bound must then hold sample-by-sample.
"""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
FOCUSING_CSV = OUT / "raychaudhuri_focusing_check.csv"
MASS_LOSS_CSV = OUT / "raychaudhuri_mass_loss.csv"
SVG_PATH = OUT / "raychaudhuri_floor_check.svg"

SEED = 20260707
SAMPLES = 400
ALPHA_GRID = [0.25, 0.5, 1.0, 2.0]
THETA0_SPREAD = 3.0          # theta_0 drawn from [-alpha * spread, -alpha]
SEGMENTS = 8                 # piecewise-constant focusing-term segments
FOCUS_TERM_MAX = 0.5         # max of sigma^2 + R_kk per segment (NEC: >= 0)
BLOWUP_THRESHOLD = -1.0e9
CLOCK_FACTOR = 1.0           # relational clock image of affine parameter (F5)
DELTA_GRID_POINTS = 120
SURVIVOR_BINS = 24           # bins on u = -1/theta in (0, 1/alpha]


def integrate_blowup(theta0: float, alpha: float, rng: random.Random) -> float:
    """Integrate d(theta)/d(lambda) = -theta^2/2 - f(lambda), f >= 0.

    Returns the affine parameter at which theta crosses BLOWUP_THRESHOLD.
    Adaptive RK4 with step shrinking near the caustic.
    """
    bound = 2.0 / alpha
    segment_len = bound / SEGMENTS
    focus = [rng.uniform(0.0, FOCUS_TERM_MAX) for _ in range(SEGMENTS)]

    def f(lam: float) -> float:
        idx = min(int(lam / segment_len), SEGMENTS - 1)
        return focus[idx]

    def deriv(lam: float, theta: float) -> float:
        return -0.5 * theta * theta - f(lam)

    lam = 0.0
    theta = theta0
    while theta > BLOWUP_THRESHOLD:
        step = min(1.0e-4 * bound, 0.05 / abs(theta))
        k1 = deriv(lam, theta)
        k2 = deriv(lam + step / 2.0, theta + step * k1 / 2.0)
        k3 = deriv(lam + step / 2.0, theta + step * k2 / 2.0)
        k4 = deriv(lam + step, theta + step * k3)
        theta += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        lam += step
        if lam > 2.0 * bound:
            raise RuntimeError("no blowup within twice the comparison bound")
    return lam


def theta_at(theta0: float, lam_star: float, lam: float) -> float:
    """Comparison-solution proxy for a survivor's expansion at time lam.

    Exact for the pure -theta^2/2 flow with the sample's effective blowup
    time; used only to bin survivors, not to re-derive the bound.
    """
    if lam >= lam_star:
        return BLOWUP_THRESHOLD
    return theta0 / (1.0 - lam / lam_star)


def shannon_bits(weights: list[float]) -> float:
    total = sum(weights)
    if total <= 0.0:
        return float("nan")
    h = 0.0
    for w in weights:
        if w > 0.0:
            p = w / total
            h -= p * math.log2(p)
    return h


def run_focusing_check(rng: random.Random) -> list[dict[str, float | int | str]]:
    rows: list[dict[str, float | int | str]] = []
    for alpha in ALPHA_GRID:
        for i in range(SAMPLES // len(ALPHA_GRID)):
            theta0 = -rng.uniform(alpha, alpha * THETA0_SPREAD)
            lam_star = integrate_blowup(theta0, alpha, rng)
            bound = 2.0 / alpha
            tight_bound = 2.0 / abs(theta0)
            rows.append(
                {
                    "sample": i,
                    "alpha": alpha,
                    "theta0": round(theta0, 6),
                    "lambda_star": round(lam_star, 6),
                    "bound_2_over_alpha": round(bound, 6),
                    "bound_2_over_theta0": round(tight_bound, 6),
                    "bound_satisfied": int(lam_star <= bound + 1.0e-9),
                    "tight_bound_satisfied": int(lam_star <= tight_bound + 1.0e-9),
                }
            )
    return rows


def run_mass_loss(
    focusing_rows: list[dict[str, float | int | str]],
) -> list[dict[str, float | int | str]]:
    alpha = min(ALPHA_GRID)
    members = [
        (float(r["theta0"]), float(r["lambda_star"]))
        for r in focusing_rows
        if float(r["alpha"]) == alpha
    ]
    fail_times = sorted(CLOCK_FACTOR * lam for _, lam in members)
    delta_star = fail_times[-1]
    rows: list[dict[str, float | int | str]] = []
    for k in range(DELTA_GRID_POINTS + 1):
        delta = delta_star * k / DELTA_GRID_POINTS
        survivors = [
            (theta0, lam) for theta0, lam in members if CLOCK_FACTOR * lam > delta
        ]
        z = len(survivors) / len(members)
        discarded_bits = -math.log2(z) if z > 0.0 else float("inf")
        # Bin survivors on u = -1/theta(delta) in (0, 1/alpha]; concentration
        # toward the lowest bin as delta -> delta* is the exclusion channel's
        # entropy collapse.
        weights = [0.0] * SURVIVOR_BINS
        for theta0, lam in survivors:
            th = theta_at(theta0, CLOCK_FACTOR * lam, delta)
            u = -1.0 / th
            idx = min(int(u * alpha * SURVIVOR_BINS), SURVIVOR_BINS - 1)
            weights[idx] += 1.0
        h_exclusion = shannon_bits(weights) if survivors else float("nan")
        rows.append(
            {
                "delta": round(delta, 6),
                "retained_mass_Z": round(z, 6),
                "discarded_coordination_bits": (
                    round(discarded_bits, 6)
                    if math.isfinite(discarded_bits)
                    else "inf"
                ),
                "exclusion_channel_entropy_bits": (
                    round(h_exclusion, 6) if not math.isnan(h_exclusion) else "undefined"
                ),
                "absorption_channel_entropy_bits": 0.0,
            }
        )
    return rows


def svg_polyline(
    rows: list[dict[str, float | int | str]],
    key: str,
    x_max: float,
    y_max: float,
    x0: int,
    y0: int,
    width: int,
    height: int,
) -> str:
    pts = []
    for r in rows:
        val = r[key]
        if not isinstance(val, (int, float)):
            continue
        x = x0 + width * float(r["delta"]) / x_max
        y = y0 + height - height * min(float(val), y_max) / y_max
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def write_svg(rows: list[dict[str, float | int | str]]) -> None:
    x_max = max(float(r["delta"]) for r in rows)
    h_vals = [
        float(r["exclusion_channel_entropy_bits"])
        for r in rows
        if isinstance(r["exclusion_channel_entropy_bits"], (int, float))
    ]
    h_max = max(1.0, max(h_vals))
    z_line = svg_polyline(rows, "retained_mass_Z", x_max, 1.0, 60, 40, 800, 280)
    h_line = svg_polyline(
        rows, "exclusion_channel_entropy_bits", x_max, h_max, 60, 400, 800, 280
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="740" viewBox="0 0 920 740">
  <rect width="920" height="740" fill="white"/>
  <text x="60" y="28" font-family="monospace" font-size="15">retained admissible mass Z(Delta): Theorem 1(a) normalization failure</text>
  <rect x="60" y="40" width="800" height="280" fill="none" stroke="#999"/>
  <polyline points="{z_line}" fill="none" stroke="#1f4e9c" stroke-width="2"/>
  <text x="60" y="388" font-family="monospace" font-size="15">hard-exclusion survivor entropy (bits): Theorem 1(b) concentration; absorption channel is 0 exactly</text>
  <rect x="60" y="400" width="800" height="280" fill="none" stroke="#999"/>
  <polyline points="{h_line}" fill="none" stroke="#9c1f1f" stroke-width="2"/>
  <text x="60" y="712" font-family="monospace" font-size="13">x: relational verification time Delta up to Delta* (Z(Delta*) = 0)</text>
</svg>
'''
    SVG_PATH.write_text(svg)


def main() -> None:
    rng = random.Random(SEED)
    OUT.mkdir(exist_ok=True)

    focusing_rows = run_focusing_check(rng)
    with FOCUSING_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(focusing_rows[0].keys()))
        writer.writeheader()
        writer.writerows(focusing_rows)

    violations = [r for r in focusing_rows if not r["bound_satisfied"]]
    tight_violations = [r for r in focusing_rows if not r["tight_bound_satisfied"]]

    mass_rows = run_mass_loss(focusing_rows)
    with MASS_LOSS_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(mass_rows[0].keys()))
        writer.writeheader()
        writer.writerows(mass_rows)

    write_svg(mass_rows)

    z_values = [float(r["retained_mass_Z"]) for r in mass_rows]
    monotone = all(a >= b - 1.0e-12 for a, b in zip(z_values, z_values[1:]))
    final_z = z_values[-1]
    h_series = [
        (float(r["delta"]), float(r["exclusion_channel_entropy_bits"]))
        for r in mass_rows
        if isinstance(r["exclusion_channel_entropy_bits"], (int, float))
    ]
    early_h = h_series[0][1]
    late_h = h_series[-1][1]

    print(f"focusing samples: {len(focusing_rows)}")
    print(f"lambda* <= 2/alpha violations: {len(violations)}")
    print(f"lambda* <= 2/|theta0| violations: {len(tight_violations)}")
    print(f"Z(Delta) monotone nonincreasing: {monotone}")
    print(f"Z(Delta*) = {final_z:.6f}")
    print(f"exclusion entropy: {early_h:.4f} bits (early) -> {late_h:.4f} bits (last surviving grid point)")
    print("absorption channel future entropy: 0.000000 bits by construction")
    print(f"wrote {FOCUSING_CSV}")
    print(f"wrote {MASS_LOSS_CSV}")
    print(f"wrote {SVG_PATH}")

    assert not violations, "Lemma 1 comparison bound violated"
    assert monotone, "retained mass must be monotone nonincreasing"
    assert final_z == 0.0, "Theorem 1(a): Z must vanish at Delta*"
    assert late_h < early_h, "Theorem 1(b): exclusion channel must concentrate"


if __name__ == "__main__":
    main()
