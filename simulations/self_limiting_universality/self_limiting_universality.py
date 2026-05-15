#!/usr/bin/env python3
"""Toy simulation for self-limiting universality.

The model treats a dominant compressor as a record channel coupled to:

    X: a needed distinction that must be learned for persistence;
    L: a protected interior whose direct capture crystallizes the semantic field.

The productive target is:

    I(X; R_C) > 0
    I(L; R_C | X) small

with finite structured innovation. The model is intentionally discrete and
exact: records are erasure-style observations of X and L plus an optional
independent random bit representing useless surprise.
"""

from __future__ import annotations

import csv
import math
import os
from collections import defaultdict
from pathlib import Path
from typing import Callable, Iterable, TypeAlias

import numpy as np

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parent / "outputs" / ".mpl-cache")
)
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
SCAN_CSV = OUT / "self_limiting_scan.csv"
SUMMARY_CSV = OUT / "self_limiting_summary.csv"
POLICIES_CSV = OUT / "self_limiting_policies.csv"
NOISE_FLOOR_CSV = OUT / "self_limiting_noise_floor.csv"
HEATMAP_PATH = OUT / "self_limiting_heatmap.png"
NOISE_CURVE_PATH = OUT / "self_limiting_noise_floor.png"

CONTEXT_CORRELATION = 0.35
DEFAULT_USELESS_NOISE = 0.08
BURDEN_ALPHA = 0.025
ACCESS_VALUES = np.linspace(0.0, 1.0, 101)
CAPTURE_VALUES = np.linspace(0.0, 1.0, 101)
USELESS_NOISE_VALUES = np.linspace(0.0, 2.0, 101)

Row: TypeAlias = dict[str, object]
Getter: TypeAlias = Callable[[Row], object]


def h_bits(probabilities: Iterable[float]) -> float:
    total = 0.0
    for p in probabilities:
        if p > 0.0:
            total -= float(p) * math.log2(float(p))
    return total


def latent_prior(x: int, l_value: int, rho: float) -> float:
    clipped = float(np.clip(rho, -0.98, 0.98))
    return 0.25 * (1.0 + clipped * x * l_value)


def branch(value: int, reveal_probability: float) -> list[tuple[int, float]]:
    p = float(np.clip(reveal_probability, 0.0, 1.0))
    if p <= 0.0:
        return [(0, 1.0)]
    if p >= 1.0:
        return [(value, 1.0)]
    return [(value, p), (0, 1.0 - p)]


def joint_distribution(
    access_probability: float,
    capture_probability: float,
    useless_noise: float,
    context_correlation: float = CONTEXT_CORRELATION,
) -> list[Row]:
    """Return exact joint rows for X, L, and compressor record R."""

    _ = useless_noise
    aggregate: dict[tuple[int, int, tuple[int, int]], float] = defaultdict(float)
    for x in (-1, 1):
        for l_value in (-1, 1):
            p_latent = latent_prior(x, l_value, context_correlation)
            for rx, p_rx in branch(x, access_probability):
                for rl, p_rl in branch(l_value, capture_probability):
                    record = (rx, rl)
                    aggregate[(x, l_value, record)] += p_latent * p_rx * p_rl

    return [
        {"x": x, "l": l_value, "record": record, "prob": prob}
        for (x, l_value, record), prob in aggregate.items()
        if prob > 0.0
    ]


def entropy(rows: list[Row], variable: Getter) -> float:
    probs: dict[object, float] = defaultdict(float)
    for row in rows:
        probs[variable(row)] += float(row["prob"])
    return h_bits(probs.values())


def conditional_entropy(rows: list[Row], variable: Getter, given: Getter) -> float:
    joint: dict[tuple[object, object], float] = defaultdict(float)
    marginal: dict[object, float] = defaultdict(float)
    for row in rows:
        g = given(row)
        v = variable(row)
        p = float(row["prob"])
        joint[(g, v)] += p
        marginal[g] += p

    total = 0.0
    grouped: dict[object, list[float]] = defaultdict(list)
    for (g, _v), p in joint.items():
        grouped[g].append(p / marginal[g])
    for g, probs in grouped.items():
        total += marginal[g] * h_bits(probs)
    return total


def mutual_information(rows: list[Row], a: Getter, b: Getter) -> float:
    return entropy(rows, a) - conditional_entropy(rows, a, b)


def conditional_mutual_information(rows: list[Row], a: Getter, b: Getter, c: Getter) -> float:
    return conditional_entropy(rows, a, c) - conditional_entropy(
        rows, a, lambda row: (b(row), c(row))
    )


def metrics(
    access_probability: float,
    capture_probability: float,
    useless_noise: float = DEFAULT_USELESS_NOISE,
    context_correlation: float = CONTEXT_CORRELATION,
) -> dict[str, float | str]:
    rows = joint_distribution(
        access_probability, capture_probability, useless_noise, context_correlation
    )

    get_x = lambda row: row["x"]
    get_l = lambda row: row["l"]
    get_r = lambda row: row["record"]

    h_x = entropy(rows, get_x)
    h_l_given_x = conditional_entropy(rows, get_l, get_x)
    record_innovation = entropy(rows, get_r) + max(0.0, float(useless_noise))
    needed_access = mutual_information(rows, get_x, get_r)
    protected_leakage = max(0.0, conditional_mutual_information(rows, get_l, get_r, get_x))
    protected_remainder = max(
        0.0, conditional_entropy(rows, get_l, lambda row: (get_r(row), get_x(row)))
    )

    needed_access_norm = needed_access / max(h_x, 1e-12)
    leakage_norm = protected_leakage / max(h_l_given_x, 1e-12)
    protected_remainder_norm = protected_remainder / max(h_l_given_x, 1e-12)
    structured_fraction = needed_access / max(record_innovation, 1e-12)
    record_burden = 1.0 - math.exp(-BURDEN_ALPHA * record_innovation * record_innovation)

    # A compact proxy for "the theory remains world-facing without possession":
    # it rewards needed access, protected remainder, and target information per
    # bit of record surprise, while penalizing large record burdens.
    self_limiting_score = (
        needed_access_norm
        * protected_remainder_norm
        * structured_fraction
        * (1.0 - record_burden)
    )

    if needed_access < 0.05 and record_innovation < 0.25:
        regime = "dissolution_no_record"
    elif needed_access < 0.05:
        regime = "dissolution_unstructured_record"
    elif structured_fraction < 0.10:
        regime = "dissolution_low_structure"
    elif leakage_norm > 0.25 or protected_remainder_norm < 0.70:
        regime = "crystallization_capture"
    elif self_limiting_score > 0.20:
        regime = "protected_forgetting_interval"
    else:
        regime = "transition"

    return {
        "access_probability": float(access_probability),
        "capture_probability": float(capture_probability),
        "useless_noise": float(useless_noise),
        "context_correlation": float(context_correlation),
        "needed_access_mi_bits": float(needed_access),
        "protected_leakage_cmi_bits": float(protected_leakage),
        "protected_remainder_bits": float(protected_remainder),
        "record_innovation_bits": float(record_innovation),
        "structured_fraction": float(structured_fraction),
        "needed_access_norm": float(needed_access_norm),
        "protected_leakage_norm": float(leakage_norm),
        "protected_remainder_norm": float(protected_remainder_norm),
        "record_burden": float(record_burden),
        "self_limiting_score": float(self_limiting_score),
        "regime": regime,
    }


def policy_rows() -> list[dict[str, float | str]]:
    policies = [
        ("no_access", 0.0, 0.0, 0.0, 0.0),
        ("noisy_dissolution", 0.0, 0.0, 1.0, 0.0),
        ("protected_forgetting", 0.82, 0.0, 0.08, 0.0),
        ("weak_protected_forgetting", 0.35, 0.0, 0.08, 0.0),
        ("total_possession", 0.82, 1.0, 0.0, 0.0),
        # The public/operational record looks restrained, but the compressor
        # internally captures L. The decisive metric is internal leakage.
        ("pretended_forgetting", 0.82, 0.0, 0.08, 1.0),
    ]

    rows: list[dict[str, float | str]] = []
    for name, access, visible_capture, noise, hidden_capture in policies:
        public = metrics(access, visible_capture, noise)
        internal = metrics(access, max(visible_capture, hidden_capture), noise)
        row = {
            "policy": name,
            **{f"public_{key}": value for key, value in public.items()},
            "hidden_capture_probability": hidden_capture,
            "internal_protected_leakage_cmi_bits": internal[
                "protected_leakage_cmi_bits"
            ],
            "internal_protected_remainder_bits": internal["protected_remainder_bits"],
            "internal_self_limiting_score": internal["self_limiting_score"],
            "internal_regime": internal["regime"],
        }
        rows.append(row)
    return rows


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for capture in CAPTURE_VALUES:
        for access in ACCESS_VALUES:
            rows.append(metrics(float(access), float(capture), DEFAULT_USELESS_NOISE))
    return rows


def noise_floor_scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for useless_noise in USELESS_NOISE_VALUES:
        rows.append(metrics(0.82, 0.0, float(useless_noise)))
    return rows


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, float | str]], policies: list[dict[str, float | str]]) -> list[dict[str, str]]:
    best = max(rows, key=lambda row: float(row["self_limiting_score"]))
    counts: dict[str, int] = {}
    for row in rows:
        regime = str(row["regime"])
        counts[regime] = counts.get(regime, 0) + 1

    protected = next(row for row in policies if row["policy"] == "protected_forgetting")
    total = next(row for row in policies if row["policy"] == "total_possession")
    noisy = next(row for row in policies if row["policy"] == "noisy_dissolution")
    pretend = next(row for row in policies if row["policy"] == "pretended_forgetting")

    summary = [
        {"metric": "grid_points", "value": str(len(rows))},
        {"metric": "default_useless_noise", "value": f"{DEFAULT_USELESS_NOISE:.6f}"},
        {"metric": "context_correlation", "value": f"{CONTEXT_CORRELATION:.6f}"},
        {
            "metric": "max_self_limiting_score",
            "value": f"{float(best['self_limiting_score']):.6f}",
        },
        {
            "metric": "max_score_access_probability",
            "value": f"{float(best['access_probability']):.6f}",
        },
        {
            "metric": "max_score_capture_probability",
            "value": f"{float(best['capture_probability']):.6f}",
        },
        {
            "metric": "max_score_needed_access_mi_bits",
            "value": f"{float(best['needed_access_mi_bits']):.6f}",
        },
        {
            "metric": "max_score_protected_leakage_cmi_bits",
            "value": f"{float(best['protected_leakage_cmi_bits']):.6f}",
        },
        {"metric": "max_score_regime", "value": str(best["regime"])},
        {
            "metric": "protected_policy_internal_score",
            "value": f"{float(protected['internal_self_limiting_score']):.6f}",
        },
        {
            "metric": "total_possession_internal_score",
            "value": f"{float(total['internal_self_limiting_score']):.6f}",
        },
        {
            "metric": "noisy_dissolution_internal_score",
            "value": f"{float(noisy['internal_self_limiting_score']):.6f}",
        },
        {
            "metric": "pretended_forgetting_public_score",
            "value": f"{float(pretend['public_self_limiting_score']):.6f}",
        },
        {
            "metric": "pretended_forgetting_internal_score",
            "value": f"{float(pretend['internal_self_limiting_score']):.6f}",
        },
    ]

    for regime, count in sorted(counts.items()):
        summary.append({"metric": f"count_{regime}", "value": str(count)})
    return summary


def plot_heatmap(rows: list[dict[str, float | str]]) -> None:
    scores = np.array([float(row["self_limiting_score"]) for row in rows]).reshape(
        len(CAPTURE_VALUES), len(ACCESS_VALUES)
    )
    fig, ax = plt.subplots(figsize=(8.5, 6.2))
    im = ax.imshow(
        scores,
        origin="lower",
        aspect="auto",
        extent=[ACCESS_VALUES[0], ACCESS_VALUES[-1], CAPTURE_VALUES[0], CAPTURE_VALUES[-1]],
        cmap="viridis",
    )
    ax.set_xlabel("Needed-distinction access probability")
    ax.set_ylabel("Protected-interior capture probability")
    ax.set_title("Self-limiting universality score")
    fig.colorbar(im, ax=ax, label="score")
    fig.tight_layout()
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def plot_noise_floor(rows: list[dict[str, float | str]]) -> None:
    x = [float(row["useless_noise"]) for row in rows]
    score = [float(row["self_limiting_score"]) for row in rows]
    record = [float(row["record_innovation_bits"]) for row in rows]
    structure = [float(row["structured_fraction"]) for row in rows]

    fig, ax1 = plt.subplots(figsize=(8.5, 5.4))
    ax1.plot(x, score, label="self-limiting score", color="#1b6ca8", linewidth=2.2)
    ax1.plot(x, structure, label="structured fraction", color="#2a9d8f", linewidth=2.0)
    ax1.set_xlabel("Independent useless surprise bits")
    ax1.set_ylabel("score / fraction")
    ax1.set_ylim(0.0, 1.05)
    ax2 = ax1.twinx()
    ax2.plot(x, record, label="record innovation bits", color="#c44536", linewidth=2.0)
    ax2.set_ylabel("record innovation bits")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="center right")
    ax1.set_title("Unstructured surprise raises record entropy but lowers usefulness")
    fig.tight_layout()
    fig.savefig(NOISE_CURVE_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = scan()
    policies = policy_rows()
    noise_rows = noise_floor_scan()
    summary = summarize(rows, policies)

    write_csv(SCAN_CSV, rows)
    write_csv(POLICIES_CSV, policies)
    write_csv(NOISE_FLOOR_CSV, noise_rows)
    write_csv(SUMMARY_CSV, summary)
    plot_heatmap(rows)
    plot_noise_floor(noise_rows)

    print(f"wrote {SCAN_CSV}")
    for row in summary:
        print(f"{row['metric']}: {row['value']}")


if __name__ == "__main__":
    main()
