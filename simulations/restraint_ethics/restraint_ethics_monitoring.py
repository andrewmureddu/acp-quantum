#!/usr/bin/env python3
"""Toy ACP restraint-ethics record-channel simulation.

The model tests a civil analogue of syndrome extraction:

    useful record:       I(public error; record) > 0
    protected agency:    I(agency; record | public error) approximately 0

Too little monitoring gives no record. Too much leakage captures the protected
state. Excessive monitoring strength carries an independent burden. The
productive regime is a syndrome-selective channel with bounded burden.
"""

from __future__ import annotations

import csv
import os
from pathlib import Path

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
SCAN_CSV = OUT / "restraint_ethics_scan.csv"
SUMMARY_CSV = OUT / "restraint_ethics_summary.csv"
CONTEXT_AUDIT_CSV = OUT / "restraint_ethics_context_audit.csv"
HEATMAP_PATH = OUT / "restraint_ethics_heatmap.png"
CURVES_PATH = OUT / "restraint_ethics_curves.png"

MONITOR_STRENGTHS = np.linspace(0.0, 4.0, 121)
LEAKAGE_FRACTIONS = np.linspace(0.0, 1.0, 101)
MAIN_CONTEXT_CORRELATION = 0.35
BURDEN_ALPHA = 0.05
GH_NODES, GH_WEIGHTS = np.polynomial.hermite.hermgauss(18)
NORMAL_NODES_1D = np.sqrt(2.0) * GH_NODES
NORMAL_WEIGHTS_1D = GH_WEIGHTS / np.sqrt(np.pi)
NODE_X, NODE_Y = np.meshgrid(NORMAL_NODES_1D, NORMAL_NODES_1D, indexing="ij")
WEIGHT_GRID = np.outer(NORMAL_WEIGHTS_1D, NORMAL_WEIGHTS_1D).reshape(-1)
NOISE_NODES = np.column_stack([NODE_X.reshape(-1), NODE_Y.reshape(-1)])

CLASSES = np.array(
    [
        [-1.0, -1.0],
        [-1.0, 1.0],
        [1.0, -1.0],
        [1.0, 1.0],
    ]
)
ERROR_VALUES = CLASSES[:, 0]
AGENCY_VALUES = CLASSES[:, 1]


def logsumexp(values: np.ndarray, axis: int | None = None) -> np.ndarray:
    vmax = np.max(values, axis=axis, keepdims=True)
    summed = np.sum(np.exp(values - vmax), axis=axis, keepdims=True)
    out = vmax + np.log(summed)
    if axis is None:
        return np.squeeze(out)
    return np.squeeze(out, axis=axis)


def joint_priors(context_correlation: float) -> np.ndarray:
    """Return P(E=e, L=l) = 1/4 * (1 + rho e l)."""

    rho = float(np.clip(context_correlation, -0.98, 0.98))
    priors = 0.25 * (1.0 + rho * ERROR_VALUES * AGENCY_VALUES)
    priors = np.clip(priors, 0.0, None)
    return priors / priors.sum()


def channel_means(monitor_strength: float, leakage_fraction: float) -> np.ndarray:
    """Mean record vector for each (E,L) class."""

    strength = float(monitor_strength)
    leak = float(np.clip(leakage_fraction, 0.0, 1.0))
    error_gain = strength * (1.0 - leak)
    agency_gain = strength * leak
    return np.column_stack([error_gain * ERROR_VALUES, agency_gain * AGENCY_VALUES])


def mixture_logpdf(
    y: np.ndarray, means: np.ndarray, weights: np.ndarray, mask: np.ndarray | None = None
) -> np.ndarray:
    """Log density up to the shared Gaussian normalizing constant.

    The missing constant cancels in every mutual-information ratio because all
    conditional densities have the same unit covariance.
    """

    active = np.ones(len(weights), dtype=bool) if mask is None else mask
    active_weights = weights[active]
    active_means = means[active]
    if active_weights.sum() <= 0:
        raise ValueError("mixture has no active probability mass")
    normalized = active_weights / active_weights.sum()
    log_weights = np.log(normalized)
    deltas = y[None, :, :] - active_means[:, None, :]
    log_components = log_weights[:, None] - 0.5 * np.sum(deltas * deltas, axis=2)
    return logsumexp(log_components, axis=0)


def mi_metrics(
    monitor_strength: float,
    leakage_fraction: float,
    context_correlation: float = MAIN_CONTEXT_CORRELATION,
) -> dict[str, float]:
    """Compute I(E;Y), I(L;Y|E), and I(L;Y) in bits."""

    priors = joint_priors(context_correlation)
    means = channel_means(monitor_strength, leakage_fraction)

    mi_error_nats = 0.0
    cmi_agency_given_error_nats = 0.0
    mi_agency_raw_nats = 0.0

    for class_index, prior in enumerate(priors):
        if prior <= 0.0:
            continue

        y = means[class_index] + NOISE_NODES
        e_value = ERROR_VALUES[class_index]
        l_value = AGENCY_VALUES[class_index]
        error_mask = ERROR_VALUES == e_value
        agency_mask = AGENCY_VALUES == l_value

        log_py = mixture_logpdf(y, means, priors)
        log_py_given_error = mixture_logpdf(y, means, priors, error_mask)
        log_py_given_agency = mixture_logpdf(y, means, priors, agency_mask)
        log_py_given_class = -0.5 * np.sum((y - means[class_index]) ** 2, axis=1)

        mi_error_nats += prior * float(
            np.sum(WEIGHT_GRID * (log_py_given_error - log_py))
        )
        cmi_agency_given_error_nats += prior * float(
            np.sum(WEIGHT_GRID * (log_py_given_class - log_py_given_error))
        )
        mi_agency_raw_nats += prior * float(
            np.sum(WEIGHT_GRID * (log_py_given_agency - log_py))
        )

    record_factor = float(np.exp(-BURDEN_ALPHA * float(monitor_strength) ** 2))
    record_burden = 1.0 - record_factor
    mi_error = max(0.0, mi_error_nats / np.log(2.0))
    cmi_agency = max(0.0, cmi_agency_given_error_nats / np.log(2.0))
    mi_agency_raw = max(0.0, mi_agency_raw_nats / np.log(2.0))
    restraint_score = mi_error * max(0.0, 1.0 - cmi_agency) * record_factor

    return {
        "public_error_mi_bits": float(mi_error),
        "excess_agency_leakage_bits": float(cmi_agency),
        "raw_agency_mi_bits": float(mi_agency_raw),
        "record_burden": float(record_burden),
        "restraint_score": float(restraint_score),
    }


def classify(metrics: dict[str, float]) -> str:
    if metrics["public_error_mi_bits"] < 0.05:
        return "abandonment_no_record"
    if metrics["excess_agency_leakage_bits"] > 0.25:
        return "capture_leakage"
    if metrics["record_burden"] > 0.50:
        return "capture_burden"
    if metrics["restraint_score"] > 0.25:
        return "restraint_interval"
    return "transition"


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for leakage_fraction in LEAKAGE_FRACTIONS:
        for monitor_strength in MONITOR_STRENGTHS:
            metrics = mi_metrics(
                float(monitor_strength),
                float(leakage_fraction),
                MAIN_CONTEXT_CORRELATION,
            )
            row: dict[str, float | str] = {
                "monitor_strength": float(monitor_strength),
                "leakage_fraction": float(leakage_fraction),
                "context_correlation": MAIN_CONTEXT_CORRELATION,
                **metrics,
            }
            row["regime"] = classify(metrics)
            rows.append(row)
    return rows


def context_audit() -> list[dict[str, float]]:
    """Show why conditional leakage is sharper than raw leakage."""

    rows: list[dict[str, float]] = []
    for rho in np.linspace(0.0, 0.9, 19):
        metrics = mi_metrics(
            monitor_strength=2.5,
            leakage_fraction=0.0,
            context_correlation=float(rho),
        )
        rows.append(
            {
                "context_correlation": float(rho),
                "monitor_strength": 2.5,
                "leakage_fraction": 0.0,
                **metrics,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, float | str]]) -> list[dict[str, str]]:
    best = max(rows, key=lambda row: float(row["restraint_score"]))
    counts: dict[str, int] = {}
    for row in rows:
        regime = str(row["regime"])
        counts[regime] = counts.get(regime, 0) + 1

    summary = [
        {"metric": "grid_points", "value": str(len(rows))},
        {
            "metric": "main_context_correlation",
            "value": f"{MAIN_CONTEXT_CORRELATION:.3f}",
        },
        {"metric": "max_restraint_score", "value": f"{float(best['restraint_score']):.6f}"},
        {
            "metric": "max_score_monitor_strength",
            "value": f"{float(best['monitor_strength']):.6f}",
        },
        {
            "metric": "max_score_leakage_fraction",
            "value": f"{float(best['leakage_fraction']):.6f}",
        },
        {
            "metric": "max_score_public_error_mi_bits",
            "value": f"{float(best['public_error_mi_bits']):.6f}",
        },
        {
            "metric": "max_score_excess_agency_leakage_bits",
            "value": f"{float(best['excess_agency_leakage_bits']):.6f}",
        },
        {"metric": "max_score_regime", "value": str(best["regime"])},
    ]
    for regime, count in sorted(counts.items()):
        summary.append({"metric": f"count_{regime}", "value": str(count)})
    return summary


def plot_heatmap(rows: list[dict[str, float | str]]) -> None:
    strength_count = len(MONITOR_STRENGTHS)
    leakage_count = len(LEAKAGE_FRACTIONS)
    score = np.array([float(row["restraint_score"]) for row in rows]).reshape(
        leakage_count, strength_count
    )
    excess_leakage = np.array(
        [float(row["excess_agency_leakage_bits"]) for row in rows]
    ).reshape(leakage_count, strength_count)
    public_error = np.array([float(row["public_error_mi_bits"]) for row in rows]).reshape(
        leakage_count, strength_count
    )

    fig, ax = plt.subplots(figsize=(8.4, 5.7), constrained_layout=True)
    image = ax.imshow(
        score,
        origin="lower",
        aspect="auto",
        extent=[
            MONITOR_STRENGTHS.min(),
            MONITOR_STRENGTHS.max(),
            LEAKAGE_FRACTIONS.min(),
            LEAKAGE_FRACTIONS.max(),
        ],
        cmap="viridis",
    )
    ax.contour(
        MONITOR_STRENGTHS,
        LEAKAGE_FRACTIONS,
        public_error,
        levels=[0.05],
        colors="white",
        linewidths=1.0,
    )
    ax.contour(
        MONITOR_STRENGTHS,
        LEAKAGE_FRACTIONS,
        excess_leakage,
        levels=[0.25],
        colors="red",
        linewidths=1.0,
    )
    ax.set_title("ACP restraint score: correctable record without agency capture")
    ax.set_xlabel("monitor strength")
    ax.set_ylabel("leakage fraction")
    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label("restraint score")
    ax.text(
        0.05,
        0.94,
        "white: I(E;R)=0.05   red: I(L;R|E)=0.25",
        transform=ax.transAxes,
        color="white",
        fontsize=9,
        bbox={"facecolor": "black", "alpha": 0.35, "edgecolor": "none"},
    )
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def plot_curves(rows: list[dict[str, float | str]]) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5), constrained_layout=True)
    leakage_slices = [0.05, 0.15, 0.30, 0.50]

    for leakage in leakage_slices:
        selected = [
            row
            for row in rows
            if abs(float(row["leakage_fraction"]) - leakage) < 1e-9
        ]
        strengths = [float(row["monitor_strength"]) for row in selected]
        scores = [float(row["restraint_score"]) for row in selected]
        leaks = [float(row["excess_agency_leakage_bits"]) for row in selected]
        axes[0].plot(strengths, scores, label=f"leak={leakage:.2f}")
        axes[1].plot(strengths, leaks, label=f"leak={leakage:.2f}")

    axes[0].set_title("Restraint score")
    axes[0].set_xlabel("monitor strength")
    axes[0].set_ylabel("score")
    axes[0].legend(frameon=False)
    axes[1].set_title("Excess agency leakage")
    axes[1].set_xlabel("monitor strength")
    axes[1].set_ylabel("I(L;R|E) bits")
    axes[1].axhline(0.25, color="red", linewidth=1.0, linestyle="--")
    axes[1].legend(frameon=False)
    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = scan()
    audit_rows = context_audit()
    summary_rows = summarize(rows)
    write_csv(SCAN_CSV, rows)
    write_csv(CONTEXT_AUDIT_CSV, audit_rows)
    write_csv(SUMMARY_CSV, summary_rows)
    plot_heatmap(rows)
    plot_curves(rows)

    best = max(rows, key=lambda row: float(row["restraint_score"]))
    print("ACP restraint-ethics scan complete")
    print(f"grid points: {len(rows)}")
    print(
        "max score: "
        f"{float(best['restraint_score']):.4f} at "
        f"monitor_strength={float(best['monitor_strength']):.3f}, "
        f"leakage_fraction={float(best['leakage_fraction']):.3f}"
    )
    print(
        "at max: "
        f"I(E;R)={float(best['public_error_mi_bits']):.4f} bits, "
        f"I(L;R|E)={float(best['excess_agency_leakage_bits']):.4f} bits, "
        f"burden={float(best['record_burden']):.4f}, "
        f"regime={best['regime']}"
    )


if __name__ == "__main__":
    main()
