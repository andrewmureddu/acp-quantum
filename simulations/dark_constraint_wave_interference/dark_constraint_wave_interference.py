#!/usr/bin/env python3
"""Wave-interference upgrade for the dark-constraint bridge.

This toy model replaces ray blocking with scalar wave competition. A point
source illuminates a mirrored room. A weak hidden refractive bump changes the
optical phase accumulated by reflected paths, shifting the bright and dark
interference fringes on a detector screen.

Two Bayesian observers infer the horizontal position of the hidden phase bump:

1. bright_only: conditions only on detector bins above a brightness threshold.
2. bright_plus_dark: conditions on the full fringe pattern, including dark bins.

The intended diagnostic is not "quantum gravity." It is the smaller claim that
structured dark fringes are genuine constraints on candidate geometries.
"""

from __future__ import annotations

import cmath
import csv
import math
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
SUMMARY_CSV = OUT / "dark_constraint_wave_summary.csv"
POSTERIOR_CSV = OUT / "dark_constraint_wave_posterior.csv"
FRINGE_CSV = OUT / "dark_constraint_wave_fringe.csv"
SVG_PATH = OUT / "dark_constraint_wave_posterior.svg"


WIDTH = 1.0
HEIGHT = 1.0
SOURCE = (0.37, 0.0)
DETECTOR_BINS = 91
CANDIDATE_COUNT = 131
TRUE_CASES = 21
REFLECTIONS = 4
LENS_Y = 0.55
LENS_SIGMA = 0.06
LENS_DELTA_N = 0.33
WAVE_NUMBER = 92.0
REFLECTION_LOSS = 0.42
SIGNAL_RATE = 18.0
BACKGROUND_RATE = 0.22
DARK_THRESHOLD = 9
REPRESENTATIVE_TRUE_CENTER = 0.64
INTEGRAL_STEPS = 72


def detector_centers() -> list[float]:
    return [(i + 0.5) * WIDTH / DETECTOR_BINS for i in range(DETECTOR_BINS)]


def candidate_centers() -> list[float]:
    margin = 0.12
    return [
        margin + (WIDTH - 2.0 * margin) * i / (CANDIDATE_COUNT - 1)
        for i in range(CANDIDATE_COUNT)
    ]


def true_centers() -> list[float]:
    lo = 0.18
    hi = 0.82
    return [lo + (hi - lo) * i / (TRUE_CASES - 1) for i in range(TRUE_CASES)]


def detector_images(x_detector: float) -> list[tuple[float, int]]:
    images: dict[float, int] = {}
    for k in range(-REFLECTIONS, REFLECTIONS + 1):
        for x_image, parity in (
            (x_detector + 2.0 * k * WIDTH, 2 * abs(k)),
            (-x_detector + 2.0 * k * WIDTH, 2 * abs(k) + 1),
        ):
            rounded = round(x_image, 12)
            images[rounded] = min(images.get(rounded, 999), parity)
    return sorted(images.items())


def gaussian_line_integral(x_end: float, lens_x: float) -> float:
    sx, sy = SOURCE
    dx = x_end - sx
    dy = HEIGHT - sy
    length = math.hypot(dx, dy)
    total = 0.0
    for step in range(INTEGRAL_STEPS):
        t = (step + 0.5) / INTEGRAL_STEPS
        x = sx + t * dx
        y = sy + t * dy
        r2 = (x - lens_x) ** 2 + (y - LENS_Y) ** 2
        total += math.exp(-0.5 * r2 / (LENS_SIGMA * LENS_SIGMA))
    return length * total / INTEGRAL_STEPS


def wave_amplitude(x_detector: float, lens_x: float) -> complex:
    amplitude = 0.0j
    for x_image, reflection_count in detector_images(x_detector):
        length = math.hypot(x_image - SOURCE[0], HEIGHT)
        phase_delay = LENS_DELTA_N * gaussian_line_integral(x_image, lens_x)
        optical_action = length + phase_delay
        attenuation = math.exp(-REFLECTION_LOSS * reflection_count) / math.sqrt(length)
        amplitude += attenuation * cmath.exp(1j * WAVE_NUMBER * optical_action)
    return amplitude


@lru_cache(maxsize=None)
def expected_counts_tuple(lens_x: float) -> tuple[float, ...]:
    rates = []
    for x_detector in detector_centers():
        intensity = abs(wave_amplitude(x_detector, lens_x)) ** 2
        rates.append(BACKGROUND_RATE + SIGNAL_RATE * intensity)
    return tuple(rates)


def expected_counts(lens_x: float) -> list[float]:
    return list(expected_counts_tuple(lens_x))


def observed_counts(lens_x: float) -> list[int]:
    # Deterministic typical counts keep the scan exactly reproducible while
    # retaining the Poisson observation model for candidate scoring.
    return [int(round(rate)) for rate in expected_counts(lens_x)]


def poisson_loglike(
    counts: list[int], rates: list[float], include_dark_bins: bool
) -> float:
    loglike = 0.0
    for count, rate in zip(counts, rates):
        if count <= DARK_THRESHOLD and not include_dark_bins:
            continue
        rate = max(rate, 1e-12)
        loglike += count * math.log(rate) - rate
    return loglike


def normalize_logs(loglikes: list[float]) -> list[float]:
    peak = max(loglikes)
    weights = [math.exp(v - peak) for v in loglikes]
    total = sum(weights)
    return [w / total for w in weights]


def posterior(counts: list[int], include_dark_bins: bool) -> list[float]:
    loglikes = [
        poisson_loglike(counts, expected_counts(center), include_dark_bins)
        for center in candidate_centers()
    ]
    return normalize_logs(loglikes)


def entropy_bits(probabilities: list[float]) -> float:
    return -sum(p * math.log2(p) for p in probabilities if p > 0.0)


def posterior_mean(probabilities: list[float]) -> float:
    return sum(p * x for p, x in zip(probabilities, candidate_centers()))


def posterior_map(probabilities: list[float]) -> float:
    centers = candidate_centers()
    return centers[max(range(len(probabilities)), key=lambda i: probabilities[i])]


def summarize_case(true_center: float) -> dict[str, float | int]:
    counts = observed_counts(true_center)
    bright = posterior(counts, include_dark_bins=False)
    full = posterior(counts, include_dark_bins=True)
    prior_entropy = math.log2(CANDIDATE_COUNT)
    bright_entropy = entropy_bits(bright)
    full_entropy = entropy_bits(full)
    bright_mean = posterior_mean(bright)
    full_mean = posterior_mean(full)
    bright_map = posterior_map(bright)
    full_map = posterior_map(full)

    return {
        "true_lens_center": true_center,
        "bright_bins": sum(1 for c in counts if c > DARK_THRESHOLD),
        "dark_bins": sum(1 for c in counts if c <= DARK_THRESHOLD),
        "bright_entropy_bits": bright_entropy,
        "full_entropy_bits": full_entropy,
        "bright_info_bits": prior_entropy - bright_entropy,
        "full_info_bits": prior_entropy - full_entropy,
        "dark_fringe_gain_bits": bright_entropy - full_entropy,
        "bright_map": bright_map,
        "full_map": full_map,
        "bright_mean": bright_mean,
        "full_mean": full_mean,
        "bright_map_abs_error": abs(bright_map - true_center),
        "full_map_abs_error": abs(full_map - true_center),
        "bright_mean_abs_error": abs(bright_mean - true_center),
        "full_mean_abs_error": abs(full_mean - true_center),
    }


def write_summary(rows: list[dict[str, float | int]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with SUMMARY_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_posterior_case(true_center: float) -> None:
    counts = observed_counts(true_center)
    bright = posterior(counts, include_dark_bins=False)
    full = posterior(counts, include_dark_bins=True)
    centers = candidate_centers()
    with POSTERIOR_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "candidate_lens_center",
                "bright_only_posterior",
                "bright_plus_dark_posterior",
            ],
        )
        writer.writeheader()
        for center, p_bright, p_full in zip(centers, bright, full):
            writer.writerow(
                {
                    "candidate_lens_center": center,
                    "bright_only_posterior": p_bright,
                    "bright_plus_dark_posterior": p_full,
                }
            )


def write_fringe_case(true_center: float) -> None:
    counts = observed_counts(true_center)
    rates = expected_counts(true_center)
    with FRINGE_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["detector_x", "expected_count", "observed_count", "is_dark"],
        )
        writer.writeheader()
        for x, rate, count in zip(detector_centers(), rates, counts):
            writer.writerow(
                {
                    "detector_x": x,
                    "expected_count": rate,
                    "observed_count": count,
                    "is_dark": int(count <= DARK_THRESHOLD),
                }
            )


def polyline(values: list[float], x0: int, y0: int, width: int, height: int) -> str:
    vmax = max(values) or 1.0
    points = []
    for i, value in enumerate(values):
        x = x0 + width * i / (len(values) - 1)
        y = y0 + height * (1.0 - value / vmax)
        points.append(f"{x:.1f},{y:.1f}")
    return " ".join(points)


def write_svg(true_center: float) -> None:
    counts = observed_counts(true_center)
    bright = posterior(counts, include_dark_bins=False)
    full = posterior(counts, include_dark_bins=True)
    summary = summarize_case(true_center)

    x0, y0, width, height = 70, 52, 760, 340
    fringe_y = y0 + height + 70
    max_count = max(counts) or 1
    bar_w = width / len(counts)
    true_x = x0 + width * (true_center - 0.12) / (WIDTH - 0.24)

    bars = []
    for i, count in enumerate(counts):
        x = x0 + i * bar_w
        h = 62 * count / max_count
        color = "#101010" if count > DARK_THRESHOLD else "#d5d5d5"
        bars.append(
            f'<rect x="{x:.1f}" y="{fringe_y + 62 - h:.1f}" '
            f'width="{max(1.0, bar_w - 1):.1f}" height="{h:.1f}" '
            f'fill="{color}"/>'
        )

    bright_entropy = float(summary["bright_entropy_bits"])
    full_entropy = float(summary["full_entropy_bits"])
    gain = float(summary["dark_fringe_gain_bits"])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="630" viewBox="0 0 920 630">
  <rect width="920" height="630" fill="#ffffff"/>
  <text x="70" y="30" font-size="22" font-family="Arial" font-weight="700">Dark Constraint Wave Interference</text>
  <text x="70" y="53" font-size="13" font-family="Arial" fill="#444">Posterior over a hidden weak phase bump; dark interference fringes included vs. ignored</text>
  <rect x="{x0}" y="{y0}" width="{width}" height="{height}" fill="#fafafa" stroke="#222"/>
  <line x1="{true_x:.1f}" y1="{y0}" x2="{true_x:.1f}" y2="{y0 + height}" stroke="#777" stroke-dasharray="5 5"/>
  <polyline points="{polyline(bright, x0, y0, width, height)}" fill="none" stroke="#2364aa" stroke-width="3"/>
  <polyline points="{polyline(full, x0, y0, width, height)}" fill="none" stroke="#c1121f" stroke-width="3"/>
  <text x="84" y="86" font-size="13" font-family="Arial" fill="#2364aa">bright fringes only</text>
  <text x="84" y="106" font-size="13" font-family="Arial" fill="#c1121f">bright fringes + dark fringes</text>
  <text x="84" y="128" font-size="13" font-family="Arial" fill="#444">H_bright = {bright_entropy:.3f} bits; H_full = {full_entropy:.3f} bits; dark-fringe gain = {gain:.3f} bits</text>
  <text x="{true_x + 6:.1f}" y="{y0 + 18}" font-size="12" font-family="Arial" fill="#555">true</text>
  <text x="70" y="{fringe_y - 10}" font-size="14" font-family="Arial" font-weight="700">Detector fringe counts</text>
  {''.join(bars)}
  <text x="70" y="592" font-size="12" font-family="Arial" fill="#555">Gray bins are dark interference fringes. They are ignored by the bright-only observer and scored by the full observer.</text>
</svg>
'''
    SVG_PATH.write_text(svg)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = [summarize_case(center) for center in true_centers()]
    write_summary(rows)
    write_posterior_case(REPRESENTATIVE_TRUE_CENTER)
    write_fringe_case(REPRESENTATIVE_TRUE_CENTER)
    write_svg(REPRESENTATIVE_TRUE_CENTER)

    mean_gain = sum(float(r["dark_fringe_gain_bits"]) for r in rows) / len(rows)
    mean_bright_map_error = sum(
        float(r["bright_map_abs_error"]) for r in rows
    ) / len(rows)
    mean_full_map_error = sum(float(r["full_map_abs_error"]) for r in rows) / len(rows)
    mean_bright_mean_error = sum(
        float(r["bright_mean_abs_error"]) for r in rows
    ) / len(rows)
    mean_full_mean_error = sum(
        float(r["full_mean_abs_error"]) for r in rows
    ) / len(rows)

    print(f"wrote {SUMMARY_CSV}")
    print(f"wrote {POSTERIOR_CSV}")
    print(f"wrote {FRINGE_CSV}")
    print(f"wrote {SVG_PATH}")
    print(f"mean dark-fringe gain: {mean_gain:.4f} bits")
    print(f"mean MAP error bright-only: {mean_bright_map_error:.4f}")
    print(f"mean MAP error bright+dark: {mean_full_map_error:.4f}")
    print(f"mean posterior-mean error bright-only: {mean_bright_mean_error:.4f}")
    print(f"mean posterior-mean error bright+dark: {mean_full_mean_error:.4f}")


if __name__ == "__main__":
    main()
