#!/usr/bin/env python3
"""Toy mirror-room inference model for the dark-constraint bridge.

The model asks whether structured non-detections improve recovery of a hidden
geometry. A point source illuminates a mirrored rectangular room. A hidden
circular absorber blocks some ray histories. Detectors on the ceiling record
counts across position bins.

Two observers infer the absorber's horizontal position:

1. positive_only: conditions only on detector bins with counts > 0.
2. positive_plus_dark: conditions on all observed bins, including zero counts.

If darkness is a real constraint, the second posterior should have lower
entropy and better localization when null windows are structured by the hidden
geometry.
"""

from __future__ import annotations

import csv
import math
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
SUMMARY_CSV = OUT / "dark_constraint_summary.csv"
POSTERIOR_CSV = OUT / "dark_constraint_posterior.csv"
SVG_PATH = OUT / "dark_constraint_posterior.svg"


WIDTH = 1.0
HEIGHT = 1.0
SOURCE = (0.5, 0.0)
OBSTACLE_Y = 0.56
OBSTACLE_RADIUS = 0.075
REFLECTIONS = 2
DETECTOR_BINS = 61
CANDIDATE_COUNT = 121
TRUE_CASES = 21
SIGNAL_RATE = 26.0
BACKGROUND_RATE = 0.04
WEIGHT_DECAY = 1.15
DARK_THRESHOLD = 16
REPRESENTATIVE_TRUE_CENTER = 0.63


def detector_centers() -> list[float]:
    return [(i + 0.5) * WIDTH / DETECTOR_BINS for i in range(DETECTOR_BINS)]


def candidate_centers() -> list[float]:
    lo = OBSTACLE_RADIUS
    hi = WIDTH - OBSTACLE_RADIUS
    return [lo + (hi - lo) * i / (CANDIDATE_COUNT - 1) for i in range(CANDIDATE_COUNT)]


def true_centers() -> list[float]:
    lo = 0.18
    hi = 0.82
    return [lo + (hi - lo) * i / (TRUE_CASES - 1) for i in range(TRUE_CASES)]


def folded_images(x: float, radius: int) -> list[float]:
    images: list[float] = []
    for k in range(-radius, radius + 1):
        images.append(x + 2.0 * k * WIDTH)
        images.append(-x + 2.0 * k * WIDTH)
    return sorted(set(round(v, 12) for v in images))


def detector_images(x_detector: float) -> list[float]:
    return folded_images(x_detector, REFLECTIONS)


def obstacle_images(x_obstacle: float) -> list[float]:
    return folded_images(x_obstacle, REFLECTIONS + 1)


def segment_distance_to_point(
    a: tuple[float, float], b: tuple[float, float], p: tuple[float, float]
) -> float:
    ax, ay = a
    bx, by = b
    px, py = p
    dx = bx - ax
    dy = by - ay
    denom = dx * dx + dy * dy
    if denom == 0.0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / denom
    t = max(0.0, min(1.0, t))
    closest = (ax + t * dx, ay + t * dy)
    return math.hypot(px - closest[0], py - closest[1])


def path_blocked(x_detector_image: float, x_obstacle: float) -> bool:
    end = (x_detector_image, HEIGHT)
    for x_image in obstacle_images(x_obstacle):
        if (
            segment_distance_to_point(SOURCE, end, (x_image, OBSTACLE_Y))
            <= OBSTACLE_RADIUS
        ):
            return True
    return False


def bin_rate(x_detector: float, x_obstacle: float) -> float:
    direct_length = math.hypot(x_detector - SOURCE[0], HEIGHT)
    total_weight = 0.0
    unblocked_weight = 0.0

    for x_image in detector_images(x_detector):
        length = math.hypot(x_image - SOURCE[0], HEIGHT)
        weight = math.exp(-WEIGHT_DECAY * (length - direct_length))
        total_weight += weight
        if not path_blocked(x_image, x_obstacle):
            unblocked_weight += weight

    visibility = unblocked_weight / total_weight
    return BACKGROUND_RATE + SIGNAL_RATE * visibility


@lru_cache(maxsize=None)
def expected_counts_tuple(x_obstacle: float) -> tuple[float, ...]:
    return tuple(bin_rate(x, x_obstacle) for x in detector_centers())


def expected_counts(x_obstacle: float) -> list[float]:
    return list(expected_counts_tuple(x_obstacle))


def observed_counts(x_obstacle: float) -> list[int]:
    # Deterministic "typical" counts keep the toy scan reproducible while
    # preserving the Poisson likelihood structure used for inference.
    return [int(round(rate)) for rate in expected_counts(x_obstacle)]


def poisson_loglike(
    counts: list[int], rates: list[float], include_zero_bins: bool
) -> float:
    loglike = 0.0
    for count, rate in zip(counts, rates):
        if count <= DARK_THRESHOLD and not include_zero_bins:
            continue
        rate = max(rate, 1e-12)
        # The log(count!) term is candidate-independent, so it cancels in the
        # posterior normalization and can be omitted.
        loglike += count * math.log(rate) - rate
    return loglike


def normalize_logs(loglikes: list[float]) -> list[float]:
    peak = max(loglikes)
    weights = [math.exp(v - peak) for v in loglikes]
    total = sum(weights)
    return [w / total for w in weights]


def entropy_bits(probabilities: list[float]) -> float:
    return -sum(p * math.log2(p) for p in probabilities if p > 0.0)


def posterior(counts: list[int], include_zero_bins: bool) -> list[float]:
    logs = []
    for center in candidate_centers():
        logs.append(poisson_loglike(counts, expected_counts(center), include_zero_bins))
    return normalize_logs(logs)


def posterior_mean(probabilities: list[float]) -> float:
    return sum(p * c for p, c in zip(probabilities, candidate_centers()))


def posterior_map(probabilities: list[float]) -> float:
    centers = candidate_centers()
    return centers[max(range(len(probabilities)), key=lambda i: probabilities[i])]


def summarize_case(true_center: float) -> dict[str, float | int]:
    counts = observed_counts(true_center)
    pos = posterior(counts, include_zero_bins=False)
    full = posterior(counts, include_zero_bins=True)
    prior_entropy = math.log2(CANDIDATE_COUNT)
    pos_entropy = entropy_bits(pos)
    full_entropy = entropy_bits(full)

    return {
        "true_center": true_center,
        "lit_bins": sum(1 for c in counts if c > DARK_THRESHOLD),
        "dark_bins": sum(1 for c in counts if c <= DARK_THRESHOLD),
        "positive_entropy_bits": pos_entropy,
        "full_entropy_bits": full_entropy,
        "positive_info_bits": prior_entropy - pos_entropy,
        "full_info_bits": prior_entropy - full_entropy,
        "null_gain_bits": pos_entropy - full_entropy,
        "positive_map": posterior_map(pos),
        "full_map": posterior_map(full),
        "positive_mean": posterior_mean(pos),
        "full_mean": posterior_mean(full),
        "positive_abs_error": abs(posterior_map(pos) - true_center),
        "full_abs_error": abs(posterior_map(full) - true_center),
    }


def write_summary(rows: list[dict[str, float | int]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with SUMMARY_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_posterior_case(true_center: float) -> None:
    counts = observed_counts(true_center)
    pos = posterior(counts, include_zero_bins=False)
    full = posterior(counts, include_zero_bins=True)
    centers = candidate_centers()

    with POSTERIOR_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "candidate_center",
                "positive_only_posterior",
                "positive_plus_dark_posterior",
            ],
        )
        writer.writeheader()
        for center, p_pos, p_full in zip(centers, pos, full):
            writer.writerow(
                {
                    "candidate_center": center,
                    "positive_only_posterior": p_pos,
                    "positive_plus_dark_posterior": p_full,
                }
            )


def polyline(values: list[float], x0: int, y0: int, width: int, height: int) -> str:
    vmax = max(values) or 1.0
    pts = []
    for i, value in enumerate(values):
        x = x0 + width * i / (len(values) - 1)
        y = y0 + height * (1.0 - value / vmax)
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


def write_svg(true_center: float) -> None:
    counts = observed_counts(true_center)
    pos = posterior(counts, include_zero_bins=False)
    full = posterior(counts, include_zero_bins=True)
    summary = summarize_case(true_center)

    x0, y0, width, height = 70, 45, 760, 360
    count_y = y0 + height + 72
    max_count = max(counts) or 1
    bar_w = width / len(counts)

    bars = []
    for i, count in enumerate(counts):
        x = x0 + i * bar_w
        h = 58 * count / max_count
        color = "#111111" if count > DARK_THRESHOLD else "#d9d9d9"
        bars.append(
            f'<rect x="{x:.1f}" y="{count_y + 58 - h:.1f}" '
            f'width="{max(1.0, bar_w - 1):.1f}" height="{h:.1f}" '
            f'fill="{color}"/>'
        )

    true_x = x0 + width * (true_center - OBSTACLE_RADIUS) / (
        WIDTH - 2.0 * OBSTACLE_RADIUS
    )
    pos_entropy = float(summary["positive_entropy_bits"])
    full_entropy = float(summary["full_entropy_bits"])
    gain = float(summary["null_gain_bits"])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="610" viewBox="0 0 920 610">
  <rect width="920" height="610" fill="#ffffff"/>
  <text x="70" y="28" font-size="22" font-family="Arial" font-weight="700">Dark Constraint Inference</text>
  <text x="70" y="52" font-size="13" font-family="Arial" fill="#444">Posterior over hidden absorber position; dark detector windows included vs. ignored</text>
  <rect x="{x0}" y="{y0}" width="{width}" height="{height}" fill="#fafafa" stroke="#222"/>
  <line x1="{true_x:.1f}" y1="{y0}" x2="{true_x:.1f}" y2="{y0 + height}" stroke="#777" stroke-dasharray="5 5"/>
  <polyline points="{polyline(pos, x0, y0, width, height)}" fill="none" stroke="#2364aa" stroke-width="3"/>
  <polyline points="{polyline(full, x0, y0, width, height)}" fill="none" stroke="#d00000" stroke-width="3"/>
  <text x="85" y="82" font-size="13" font-family="Arial" fill="#2364aa">positive detections only</text>
  <text x="85" y="102" font-size="13" font-family="Arial" fill="#d00000">positive detections + dark windows</text>
  <text x="85" y="124" font-size="13" font-family="Arial" fill="#444">H_pos = {pos_entropy:.3f} bits; H_full = {full_entropy:.3f} bits; null gain = {gain:.3f} bits</text>
  <text x="{true_x + 6:.1f}" y="{y0 + 18}" font-size="12" font-family="Arial" fill="#555">true</text>
  <text x="70" y="{count_y - 10}" font-size="14" font-family="Arial" font-weight="700">Detector counts</text>
  {''.join(bars)}
  <text x="70" y="570" font-size="12" font-family="Arial" fill="#555">Gray bins are structured null records: they carry likelihood weight only in the full posterior.</text>
</svg>
'''
    SVG_PATH.write_text(svg)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = [summarize_case(center) for center in true_centers()]
    write_summary(rows)
    write_posterior_case(REPRESENTATIVE_TRUE_CENTER)
    write_svg(REPRESENTATIVE_TRUE_CENTER)

    mean_gain = sum(float(r["null_gain_bits"]) for r in rows) / len(rows)
    mean_pos_error = sum(float(r["positive_abs_error"]) for r in rows) / len(rows)
    mean_full_error = sum(float(r["full_abs_error"]) for r in rows) / len(rows)
    mean_pos_mean_error = sum(
        abs(float(r["positive_mean"]) - float(r["true_center"])) for r in rows
    ) / len(rows)
    mean_full_mean_error = sum(
        abs(float(r["full_mean"]) - float(r["true_center"])) for r in rows
    ) / len(rows)
    print(f"wrote {SUMMARY_CSV}")
    print(f"wrote {POSTERIOR_CSV}")
    print(f"wrote {SVG_PATH}")
    print(f"mean null gain: {mean_gain:.4f} bits")
    print(f"mean MAP error positive-only: {mean_pos_error:.4f}")
    print(f"mean MAP error positive+dark: {mean_full_error:.4f}")
    print(f"mean posterior-mean error positive-only: {mean_pos_mean_error:.4f}")
    print(f"mean posterior-mean error positive+dark: {mean_full_mean_error:.4f}")


if __name__ == "__main__":
    main()
