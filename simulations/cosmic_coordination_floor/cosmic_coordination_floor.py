#!/usr/bin/env python3
"""Finite macrocell toy for the ACP cosmic coordination floor.

This is not a gravitational simulation. It is a finite stochastic skeleton of
the relational macrostate program in:

- bridges/cosmic_coordination_floor.md
- bridges/relational_observable_macrostate_kernel.md

The original toy tracked one collapse coordinate z. This version tracks a
finite relational macrocell vector

    (M_boundary, J_boundary, Q_boundary, C_R, theta_R, K_R,
     A_boundary, N_0, Y_boundary)

where the last two entries are boundary/null-record bins. The transition laws
are still schematic. Their purpose is to separate four logical possibilities:

1. naked_collapse: classical focusing leaks mass to an inadmissible endpoint;
2. hard_exclusion: singular histories are removed and the remainder is
   renormalized, but no coordination is redistributed;
3. horizon_transfer: near the floor, a finite boundary transfer regularizes the
   channel and emits late decodable records;
4. quantum_completion: a deliberately modest candidate completion that triggers
   earlier, keeps the channel normalized, records geometry sectors, suppresses
   early logical leakage, and releases interior information only as a late
   decodable channel;
5. leaky_completion: a control policy identical to quantum_completion except
   that its transfer record bin depends on the interior clock phase — an
   inadmissible channel that reads the interior clock early.

Interior clock register (bridges/boundary_records_interior_time.md). The
interior microstate is now explicit: a clock phase theta in Z_8 with uniform
prior, advancing deterministically by one bin per step. The per-step
diagnostic I(Theta; boundary record) tests Corollary G1 — admissible
policies must keep it at zero before decoding — and the summary records the
step at which interior (clock) information first becomes boundary-decodable,
testing Corollary G2: clock release and information release are the same
transition, and what is decoded is the phase frozen at the transfer step.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
TIMESERIES_CSV = OUT / "cosmic_coordination_floor_timeseries.csv"
SUMMARY_CSV = OUT / "cosmic_coordination_floor_summary.csv"
SVG_PATH = OUT / "cosmic_coordination_floor.svg"


STEPS = 36
COMPACTNESS_BIN_COUNT = 101
INITIAL_COMPACTNESS = 0.12
INITIAL_SIGMA = 0.018

COLLAPSE_RATE = 0.30
BASE_SIGMA = 0.075
SIGMA_MIN = 0.004

FLOOR_BITS = 1.50
PRIVACY_EPS_BITS = 0.08

HORIZON_TRIGGER_C = 0.78
HORIZON_TRANSFER_CENTER = 0.36
HORIZON_TRANSFER_SIGMA = 0.085
HORIZON_DECODE_CORRECT_PROB = 0.86

QG_TRIGGER_C = 0.66
QG_TRANSFER_SIGMA = 0.12
QG_DECODE_CORRECT_PROB = 0.74

INTERIOR_CLASSES = 8
# The interior microstate is identified with a clock phase in Z_8: the
# INTERIOR_CLASSES-way late decode is now literally a readout of the
# interior clock frozen at the transfer step.
CLOCK_PHASES = INTERIOR_CLASSES


@dataclass(frozen=True)
class Macrocell:
    """Finite relational macrocell label.

    The first three bins are fixed in this toy because the run is meant to
    isolate collapse-channel structure rather than spin/charge dynamics.
    """

    mass_boundary: int
    spin_boundary: int
    charge_boundary: int
    compactness: int
    expansion: int
    curvature: int
    boundary_area: int
    null_record: int
    radiation_record: int


Distribution = dict[Macrocell, float]
# Joint state: (macrocell, interior clock phase in Z_8) -> mass.
JointState = tuple[Macrocell, int]
JointDistribution = dict[JointState, float]


def compactness_centers() -> list[float]:
    return [0.99 * i / (COMPACTNESS_BIN_COUNT - 1) for i in range(COMPACTNESS_BIN_COUNT)]


CENTERS = compactness_centers()


def entropy_bits(probabilities: list[float]) -> float:
    return -sum(p * math.log2(p) for p in probabilities if p > 0.0)


def normalize(weights: list[float]) -> list[float]:
    total = sum(weights)
    if total <= 0.0:
        return [0.0 for _ in weights]
    return [w / total for w in weights]


def normalize_distribution(distribution: Distribution) -> Distribution:
    total = sum(distribution.values())
    if total <= 0.0:
        return {}
    return {cell: mass / total for cell, mass in distribution.items() if mass > 0.0}


def gaussian_weights(center: float, sigma: float) -> list[float]:
    sigma = max(sigma, 1e-6)
    return [
        math.exp(-0.5 * ((compactness - center) / sigma) ** 2)
        for compactness in CENTERS
    ]


def mixture_weights(components: list[tuple[float, float, float]]) -> list[float]:
    weights = [0.0 for _ in CENTERS]
    for center, sigma, component_weight in components:
        for i, w in enumerate(gaussian_weights(center, sigma)):
            weights[i] += component_weight * w
    return weights


def bin_index(value: float, thresholds: list[float]) -> int:
    for i, threshold in enumerate(thresholds):
        if value < threshold:
            return i
    return len(thresholds)


def expansion_value(compactness: float) -> float:
    # Negative expansion strengthens as compactness rises.
    return -0.05 - 1.55 * compactness**2


def curvature_value(compactness: float) -> float:
    # Bounded toy proxy for a curvature-density diagnostic.
    return compactness**2 / max(0.04, (1.0 - compactness + 0.08) ** 2)


def area_value(compactness: float, record_kind: str) -> float:
    # A finite boundary/horizon-area proxy. Transfer records lift the boundary
    # area bin to mark a newly active finite boundary register.
    base = 1.0 / (1.0 + 2.5 * compactness)
    if record_kind == "horizon":
        return min(1.0, base + 0.38)
    if record_kind in ("qg", "qg_leak0", "qg_leak1"):
        return min(1.0, base + 0.24)
    return base


def expansion_bin(compactness: float) -> int:
    theta = expansion_value(compactness)
    return bin_index(theta, [-1.25, -0.85, -0.50, -0.25, -0.10])


def curvature_bin(compactness: float) -> int:
    return bin_index(curvature_value(compactness), [0.03, 0.10, 0.25, 0.60, 1.50, 3.00])


def area_bin(compactness: float, record_kind: str) -> int:
    return bin_index(area_value(compactness, record_kind), [0.24, 0.32, 0.44, 0.58, 0.74])


def null_record_bin(compactness: float, record_kind: str) -> int:
    base = bin_index(compactness, [0.35, 0.55, 0.70, 0.84])
    if record_kind == "horizon":
        return 5
    if record_kind in ("qg", "qg_leak0", "qg_leak1"):
        return 6
    return base


def radiation_record_bin(compactness: float, record_kind: str) -> int:
    if record_kind == "horizon":
        return 3
    if record_kind == "qg":
        return 2
    # Leaky control: the transfer's radiation record depends on the interior
    # clock parity - a deliberately inadmissible, clock-central record.
    if record_kind == "qg_leak0":
        return 2
    if record_kind == "qg_leak1":
        return 4
    if compactness > 0.90:
        return 1
    return 0


def macrocell_from_index(compactness_idx: int, record_kind: str) -> Macrocell:
    compactness = CENTERS[compactness_idx]
    return Macrocell(
        mass_boundary=5,
        spin_boundary=0,
        charge_boundary=0,
        compactness=compactness_idx,
        expansion=expansion_bin(compactness),
        curvature=curvature_bin(compactness),
        boundary_area=area_bin(compactness, record_kind),
        null_record=null_record_bin(compactness, record_kind),
        radiation_record=radiation_record_bin(compactness, record_kind),
    )


def add_weight(
    distribution: defaultdict[JointState, float],
    compactness_weights: list[float],
    mass: float,
    record_kind: str,
    theta: int,
) -> None:
    for idx, weight in enumerate(normalize(compactness_weights)):
        if weight == 0.0:
            continue
        distribution[(macrocell_from_index(idx, record_kind), theta)] += mass * weight


def collapse_center(compactness: float) -> float:
    return compactness + COLLAPSE_RATE * (compactness + 0.08) ** 2


def collapse_sigma(compactness: float) -> float:
    return max(SIGMA_MIN, BASE_SIGMA * (1.0 - compactness) ** 1.8)


def singular_escape_probability(center: float) -> float:
    if center >= 1.0:
        return 1.0
    outside = 1.0 - max(0.0, 1.0 - center) ** 0.4
    return max(0.0, min(1.0, outside))


def symmetric_channel_mi_bits(classes: int, correct_prob: float) -> float:
    if classes <= 1 or correct_prob <= 1.0 / classes:
        return 0.0
    wrong_prob = (1.0 - correct_prob) / (classes - 1)
    conditional_entropy = 0.0
    conditional_entropy -= correct_prob * math.log2(correct_prob)
    conditional_entropy -= (classes - 1) * wrong_prob * math.log2(wrong_prob)
    return math.log2(classes) - conditional_entropy


def mutual_information_bits(
    distribution: Distribution,
    x_key: Callable[[Macrocell], tuple[int, ...]],
    y_key: Callable[[Macrocell], tuple[int, ...]],
) -> float:
    total = sum(distribution.values())
    if total <= 0.0:
        return 0.0

    px: dict[tuple[int, ...], float] = defaultdict(float)
    py: dict[tuple[int, ...], float] = defaultdict(float)
    pxy: dict[tuple[tuple[int, ...], tuple[int, ...]], float] = defaultdict(float)

    for cell, mass in distribution.items():
        x = x_key(cell)
        y = y_key(cell)
        p = mass / total
        px[x] += p
        py[y] += p
        pxy[(x, y)] += p

    info = 0.0
    for (x, y), p in pxy.items():
        denominator = px[x] * py[y]
        if p > 0.0 and denominator > 0.0:
            info += p * math.log2(p / denominator)
    return info


def clock_record_mi_bits(joint: JointDistribution) -> float:
    """I(Theta; boundary record) over the joint distribution - the G1 audit."""
    total = sum(joint.values())
    if total <= 0.0:
        return 0.0
    px: dict[int, float] = defaultdict(float)
    py: dict[tuple[int, ...], float] = defaultdict(float)
    pxy: dict[tuple[int, tuple[int, ...]], float] = defaultdict(float)
    for (cell, theta), mass in joint.items():
        record = boundary_record(cell)
        p = mass / total
        px[theta] += p
        py[record] += p
        pxy[(theta, record)] += p
    info = 0.0
    for (theta, record), p in pxy.items():
        denominator = px[theta] * py[record]
        if p > 0.0 and denominator > 0.0:
            info += p * math.log2(p / denominator)
    return max(0.0, info)


def macrocell_marginal(joint: JointDistribution) -> Distribution:
    marginal: defaultdict[Macrocell, float] = defaultdict(float)
    for (cell, _theta), mass in joint.items():
        marginal[cell] += mass
    return dict(marginal)


def geometry_sector(cell: Macrocell) -> tuple[int, ...]:
    compactness_band = cell.compactness // 10
    return (compactness_band, cell.expansion, cell.curvature)


def boundary_record(cell: Macrocell) -> tuple[int, ...]:
    return (cell.null_record, cell.radiation_record)


def transition(
    policy: str, current: JointDistribution
) -> tuple[JointDistribution, dict[str, float]]:
    raw_next: defaultdict[JointState, float] = defaultdict(float)
    singular_mass = 0.0
    triggered_mass = 0.0
    late_decodable = 0.0
    early_privacy_leakage = 0.0

    completion_like = policy in ("quantum_completion", "leaky_completion")

    for (cell, theta), mass in current.items():
        if mass == 0.0:
            continue

        compactness = CENTERS[cell.compactness]
        theta_next = (theta + 1) % CLOCK_PHASES

        if policy == "horizon_transfer" and compactness >= HORIZON_TRIGGER_C:
            triggered_mass += mass
            late_decodable += mass * symmetric_channel_mi_bits(
                INTERIOR_CLASSES, HORIZON_DECODE_CORRECT_PROB
            )
            add_weight(
                raw_next,
                gaussian_weights(HORIZON_TRANSFER_CENTER, HORIZON_TRANSFER_SIGMA),
                mass,
                "horizon",
                theta_next,
            )
            continue

        if completion_like and compactness >= QG_TRIGGER_C:
            triggered_mass += mass
            late_decodable += mass * symmetric_channel_mi_bits(
                INTERIOR_CLASSES, QG_DECODE_CORRECT_PROB
            )
            # A schematic completion: part bounce-like redistribution, part
            # horizon-scale broadening. The point is nonzero future entropy
            # with a finite, privacy-preserving boundary record. The leaky
            # control instead writes the interior clock parity into its
            # transfer record - a clock-central, inadmissible channel.
            if policy == "leaky_completion":
                record_kind = f"qg_leak{theta_next % 2}"
            else:
                record_kind = "qg"
            add_weight(
                raw_next,
                mixture_weights(
                    [
                        (0.34, QG_TRANSFER_SIGMA, 0.58),
                        (0.55, QG_TRANSFER_SIGMA * 1.25, 0.42),
                    ]
                ),
                mass,
                record_kind,
                theta_next,
            )
            early_privacy_leakage += 0.018 * mass
            continue

        center = collapse_center(compactness)
        sigma = collapse_sigma(compactness)

        if policy == "naked_collapse":
            outside = singular_escape_probability(center)
            singular_mass += mass * outside
            early_privacy_leakage += mass * outside * math.log2(INTERIOR_CLASSES)
            retained_mass = mass * (1.0 - outside)
        else:
            retained_mass = mass

        add_weight(
            raw_next,
            gaussian_weights(min(center, 0.995), sigma),
            retained_mass,
            "collapse",
            theta_next,
        )

    admissible_mass = sum(raw_next.values())
    if policy != "naked_collapse":
        next_distribution = normalize_distribution(dict(raw_next))
        admissible_mass = 1.0
    else:
        next_distribution = dict(raw_next)

    normalized_next = normalize_distribution(next_distribution)
    cell_marginal = macrocell_marginal(normalized_next)
    probabilities = list(cell_marginal.values())
    future_entropy = entropy_bits(probabilities)
    geometry_record_mi = mutual_information_bits(
        cell_marginal, geometry_sector, boundary_record
    )
    clock_record_mi = clock_record_mi_bits(normalized_next)

    mean_compactness = sum(
        mass * CENTERS[cell.compactness] for cell, mass in cell_marginal.items()
    )
    mean_expansion = sum(
        mass * expansion_value(CENTERS[cell.compactness])
        for cell, mass in cell_marginal.items()
    )
    mean_curvature = sum(
        mass * curvature_value(CENTERS[cell.compactness])
        for cell, mass in cell_marginal.items()
    )

    floor_violation = float(future_entropy < FLOOR_BITS or admissible_mass < 0.999)
    privacy_violation = float(
        early_privacy_leakage > PRIVACY_EPS_BITS
        or clock_record_mi > PRIVACY_EPS_BITS
    )

    return next_distribution, {
        "interior_clock_record_mi_bits": clock_record_mi,
        "future_entropy_bits": future_entropy,
        "admissible_mass": admissible_mass,
        "singular_mass": singular_mass,
        "triggered_mass": triggered_mass,
        "geometry_record_mi_bits": geometry_record_mi,
        "early_privacy_leakage_bits": early_privacy_leakage,
        "late_decodable_bits": late_decodable,
        "mean_compactness": mean_compactness,
        "mean_expansion": mean_expansion,
        "mean_curvature": mean_curvature,
        "floor_violation": floor_violation,
        "privacy_violation": privacy_violation,
    }


def initial_distribution() -> JointDistribution:
    distribution: defaultdict[JointState, float] = defaultdict(float)
    for theta in range(CLOCK_PHASES):
        add_weight(
            distribution,
            gaussian_weights(INITIAL_COMPACTNESS, INITIAL_SIGMA),
            1.0 / CLOCK_PHASES,
            "quiet",
            theta,
        )
    return dict(distribution)


def simulate_policy(policy: str) -> list[dict[str, float | int | str]]:
    distribution = initial_distribution()
    rows: list[dict[str, float | int | str]] = []
    cumulative_decodable = 0.0
    max_info = math.log2(INTERIOR_CLASSES)

    for step in range(STEPS):
        distribution, metrics = transition(policy, distribution)
        cumulative_decodable = min(
            max_info, cumulative_decodable + metrics["late_decodable_bits"]
        )
        rows.append(
            {
                "policy": policy,
                "step": step + 1,
                "mean_compactness": metrics["mean_compactness"],
                "mean_expansion": metrics["mean_expansion"],
                "mean_curvature": metrics["mean_curvature"],
                "future_entropy_bits": metrics["future_entropy_bits"],
                "admissible_mass": metrics["admissible_mass"],
                "singular_mass": metrics["singular_mass"],
                "triggered_mass": metrics["triggered_mass"],
                "geometry_record_mi_bits": metrics["geometry_record_mi_bits"],
                "interior_clock_record_mi_bits": metrics[
                    "interior_clock_record_mi_bits"
                ],
                "early_privacy_leakage_bits": metrics["early_privacy_leakage_bits"],
                "late_decodable_bits": metrics["late_decodable_bits"],
                "cumulative_late_decodable_bits": cumulative_decodable,
                "floor_bits": FLOOR_BITS,
                "privacy_epsilon_bits": PRIVACY_EPS_BITS,
                "floor_violation": metrics["floor_violation"],
                "privacy_violation": metrics["privacy_violation"],
            }
        )

    return rows


def write_csv(path: Path, rows: list[dict[str, float | int | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, float | int | str]]) -> list[dict[str, float | str]]:
    policies = sorted(set(str(r["policy"]) for r in rows))
    summary: list[dict[str, float | str]] = []
    for policy in policies:
        pr = [r for r in rows if r["policy"] == policy]
        first_floor_violation = next(
            (int(r["step"]) for r in pr if float(r["floor_violation"]) > 0.0),
            -1,
        )
        first_privacy_violation = next(
            (int(r["step"]) for r in pr if float(r["privacy_violation"]) > 0.0),
            -1,
        )
        summary.append(
            {
                "policy": policy,
                "min_future_entropy_bits": min(
                    float(r["future_entropy_bits"]) for r in pr
                ),
                "min_admissible_mass": min(float(r["admissible_mass"]) for r in pr),
                "max_singular_mass": max(float(r["singular_mass"]) for r in pr),
                "max_geometry_record_mi_bits": max(
                    float(r["geometry_record_mi_bits"]) for r in pr
                ),
                "max_early_privacy_leakage_bits": max(
                    float(r["early_privacy_leakage_bits"]) for r in pr
                ),
                "max_interior_clock_record_mi_bits": max(
                    float(r["interior_clock_record_mi_bits"]) for r in pr
                ),
                # First step with non-negligible late decodable output. The
                # 1e-3 threshold removes the Gaussian-tail artifact of
                # infinitesimal mass sitting above the trigger from step 1.
                "clock_info_release_step": next(
                    (
                        int(r["step"])
                        for r in pr
                        if float(r["late_decodable_bits"]) > 1e-3
                    ),
                    -1,
                ),
                "clock_leak_onset_step": next(
                    (
                        int(r["step"])
                        for r in pr
                        if float(r["interior_clock_record_mi_bits"]) > 1e-3
                    ),
                    -1,
                ),
                "final_mean_compactness": float(pr[-1]["mean_compactness"]),
                "final_cumulative_late_decodable_bits": float(
                    pr[-1]["cumulative_late_decodable_bits"]
                ),
                "first_floor_violation_step": first_floor_violation,
                "first_privacy_violation_step": first_privacy_violation,
            }
        )
    return summary


def svg_polyline(
    rows: list[dict[str, float | int | str]],
    key: str,
    y_max: float,
    y_min: float = 0.0,
) -> str:
    x0, y0, width, height = 70, 52, 760, 300
    span = max(1e-9, y_max - y_min)
    points = []
    for r in rows:
        x = x0 + width * (int(r["step"]) - 1) / (STEPS - 1)
        y = y0 + height * (1.0 - (float(r[key]) - y_min) / span)
        points.append(f"{x:.1f},{y:.1f}")
    return " ".join(points)


def write_svg(rows: list[dict[str, float | int | str]]) -> None:
    colors = {
        "naked_collapse": "#9d0208",
        "hard_exclusion": "#2364aa",
        "horizon_transfer": "#2d6a4f",
        "quantum_completion": "#6f4aa8",
        "leaky_completion": "#c77700",
    }
    labels = {
        "naked_collapse": "naked collapse",
        "hard_exclusion": "hard exclusion",
        "horizon_transfer": "horizon transfer",
        "quantum_completion": "quantum completion",
        "leaky_completion": "leaky completion",
    }
    entropy_max = max(
        float(r["future_entropy_bits"]) for r in rows + [{"future_entropy_bits": FLOOR_BITS}]
    )
    info_max = math.log2(INTERIOR_CLASSES)
    x0, y0, width, height = 70, 52, 760, 300
    y2 = 420

    entropy_lines = []
    info_lines = []
    legend = []
    for i, policy in enumerate(colors):
        pr = [r for r in rows if r["policy"] == policy]
        entropy_lines.append(
            f'<polyline points="{svg_polyline(pr, "future_entropy_bits", entropy_max)}" '
            f'fill="none" stroke="{colors[policy]}" stroke-width="3"/>'
        )
        info_lines.append(
            f'<polyline points="{svg_polyline(pr, "cumulative_late_decodable_bits", info_max)}" '
            f'fill="none" stroke="{colors[policy]}" stroke-width="3" '
            f'transform="translate(0,{y2 - y0})"/>'
        )
        legend.append(
            f'<text x="{92 + 180 * i}" y="34" font-size="13" font-family="Arial" '
            f'fill="{colors[policy]}">{labels[policy]}</text>'
        )

    floor_y = y0 + height * (1.0 - FLOOR_BITS / entropy_max)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="790" viewBox="0 0 920 790">
  <rect width="920" height="790" fill="#ffffff"/>
  <text x="70" y="24" font-size="21" font-family="Arial" font-weight="700">Relational Macrocell Collapse Toy</text>
  {''.join(legend)}
  <text x="70" y="48" font-size="13" font-family="Arial" fill="#444">Conditional future entropy over finite collapse macrocells</text>
  <rect x="{x0}" y="{y0}" width="{width}" height="{height}" fill="#fafafa" stroke="#222"/>
  <line x1="{x0}" y1="{floor_y:.1f}" x2="{x0 + width}" y2="{floor_y:.1f}" stroke="#555" stroke-dasharray="5 5"/>
  <text x="{x0 + width - 112}" y="{floor_y - 6:.1f}" font-size="12" font-family="Arial" fill="#555">floor</text>
  {''.join(entropy_lines)}
  <text x="70" y="380" font-size="12" font-family="Arial" fill="#555">state label: (M, J, Q, compactness, expansion, curvature, area, null record, radiation)</text>
  <text x="70" y="408" font-size="13" font-family="Arial" fill="#444">Cumulative late decodable boundary information</text>
  <rect x="{x0}" y="{y2}" width="{width}" height="{height}" fill="#fafafa" stroke="#222"/>
  {''.join(info_lines)}
  <text x="70" y="760" font-size="12" font-family="Arial" fill="#555">The toy separates normalization, entropy floor, geometry records, early privacy, and late decoding.</text>
</svg>
'''
    SVG_PATH.write_text(svg)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, float | int | str]] = []
    for policy in (
        "naked_collapse",
        "hard_exclusion",
        "horizon_transfer",
        "quantum_completion",
        "leaky_completion",
    ):
        rows.extend(simulate_policy(policy))
    write_csv(TIMESERIES_CSV, rows)
    summary = summarize(rows)
    write_csv(SUMMARY_CSV, summary)
    write_svg(rows)

    print(f"wrote {TIMESERIES_CSV}")
    print(f"wrote {SUMMARY_CSV}")
    print(f"wrote {SVG_PATH}")
    for row in summary:
        print(
            f"{row['policy']}: "
            f"min_H={float(row['min_future_entropy_bits']):.3f}, "
            f"min_adm={float(row['min_admissible_mass']):.3f}, "
            f"max_sing={float(row['max_singular_mass']):.3f}, "
            f"max_I_G_R={float(row['max_geometry_record_mi_bits']):.3f}, "
            f"max_priv={float(row['max_early_privacy_leakage_bits']):.3f}, "
            f"max_I_clock_R={float(row['max_interior_clock_record_mi_bits']):.3f}, "
            f"clock_release={int(row['clock_info_release_step'])}, "
            f"final_I_late={float(row['final_cumulative_late_decodable_bits']):.3f}, "
            f"first_floor={int(row['first_floor_violation_step'])}, "
            f"first_privacy={int(row['first_privacy_violation_step'])}"
        )


if __name__ == "__main__":
    main()
