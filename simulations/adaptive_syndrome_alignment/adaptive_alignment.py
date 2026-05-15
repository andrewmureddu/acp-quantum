#!/usr/bin/env python3
"""Toy benchmark: adaptive syndrome alignment under drifting biased Pauli noise.

This is a deliberately small QEC-native benchmark. A 3-qubit repetition memory
can be oriented to correct either X-dominated or Z-dominated physical noise:

    orientation "x": computational-basis repetition, corrects physical X flips
    orientation "z": Hadamard-rotated repetition, corrects physical Z flips

The noise has fixed total strength but a bias that drifts between X and Z. We
compare fixed, static-tailored, adaptive, and overactive-adaptive protocols.
The reported metric is the entanglement fidelity of the induced logical Pauli
channel after a memory experiment, not GHZ branch population.
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parent / "outputs" / ".mpl-cache")
)
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
CSV_PATH = OUT / "adaptive_alignment_scan.csv"
HEATMAP_PATH = OUT / "adaptive_alignment_heatmap.png"
CURVES_PATH = OUT / "adaptive_alignment_curves.png"

TOTAL_ROUNDS = 48
TOTAL_PHYSICAL_ERROR = 0.025
ADAPTIVE_INTERVAL = 12
OVERACTIVE_INTERVAL = 1
CHARACTERIZATION_ERROR = 0.0007
SWITCH_ERROR = 0.004

ANISOTROPY_VALUES = np.linspace(0.0, 0.9, 46)
DRIFT_VALUES = np.linspace(0.0, 2.0, 41)


@dataclass(frozen=True)
class Protocol:
    name: str
    mode: str
    update_interval: int | None = None


PROTOCOLS = [
    Protocol("fixed_x", "fixed_x"),
    Protocol("fixed_z", "fixed_z"),
    Protocol("static_tailored", "static"),
    Protocol("adaptive_tailored", "adaptive", ADAPTIVE_INTERVAL),
    Protocol("overactive_adaptive", "adaptive", OVERACTIVE_INTERVAL),
]


def majority_failure(p: float) -> float:
    """Logical failure probability for a 3-bit repetition code correcting p."""

    p = float(np.clip(p, 0.0, 1.0))
    return 3.0 * p * p * (1.0 - p) + p**3


def odd_parity_probability(p: float) -> float:
    """Probability that an odd number of three independent errors occurred."""

    p = float(np.clip(p, 0.0, 1.0))
    return 0.5 * (1.0 - (1.0 - 2.0 * p) ** 3)


def physical_noise(anisotropy: float, drift_cycles: float, round_index: int) -> tuple[float, float, float]:
    """Return physical (p_x, p_z, bias) at one memory round."""

    phase = 2.0 * np.pi * drift_cycles * round_index / max(1, TOTAL_ROUNDS - 1)
    bias = float(anisotropy * np.cos(phase))
    p_x = TOTAL_PHYSICAL_ERROR * (1.0 + bias) / 2.0
    p_z = TOTAL_PHYSICAL_ERROR * (1.0 - bias) / 2.0
    return p_x, p_z, bias


def target_orientation(bias: float) -> str:
    """Choose the repetition-code orientation for the dominant Pauli error."""

    return "x" if bias >= 0.0 else "z"


def logical_error_rates(p_x: float, p_z: float, orientation: str) -> tuple[float, float]:
    """Logical Pauli X and Z error probabilities for one correction round."""

    if orientation == "x":
        logical_x = majority_failure(p_x)
        logical_z = odd_parity_probability(p_z)
    elif orientation == "z":
        logical_x = odd_parity_probability(p_x)
        logical_z = majority_failure(p_z)
    else:
        raise ValueError(f"unknown orientation {orientation!r}")
    return logical_x, logical_z


def apply_logical_pauli_round(
    lambdas: np.ndarray,
    logical_x: float,
    logical_z: float,
) -> np.ndarray:
    """Compose a logical Pauli channel using Pauli-transfer eigenvalues."""

    logical_x = float(np.clip(logical_x, 0.0, 0.5))
    logical_z = float(np.clip(logical_z, 0.0, 0.5))
    round_lambdas = np.array(
        [
            1.0 - 2.0 * logical_z,
            (1.0 - 2.0 * logical_x) * (1.0 - 2.0 * logical_z),
            1.0 - 2.0 * logical_x,
        ],
        dtype=float,
    )
    return lambdas * round_lambdas


def entanglement_fidelity(lambdas: np.ndarray) -> float:
    """Entanglement fidelity of a one-qubit Pauli channel."""

    return float(np.clip((1.0 + float(np.sum(lambdas))) / 4.0, 0.0, 1.0))


def run_protocol(protocol: Protocol, anisotropy: float, drift_cycles: float) -> dict[str, float | str]:
    """Run one protocol for one noise trajectory."""

    _, _, initial_bias = physical_noise(anisotropy, drift_cycles, 0)
    if protocol.mode == "fixed_x":
        orientation = "x"
    elif protocol.mode == "fixed_z":
        orientation = "z"
    else:
        orientation = target_orientation(initial_bias)

    lambdas = np.ones(3, dtype=float)
    updates = 0
    switches = 0
    mismatched_rounds = 0

    for round_index in range(TOTAL_ROUNDS):
        p_x, p_z, bias = physical_noise(anisotropy, drift_cycles, round_index)
        dominant = target_orientation(bias)

        if protocol.mode == "adaptive" and round_index % int(protocol.update_interval or 1) == 0:
            updates += 1
            lambdas = apply_logical_pauli_round(
                lambdas, CHARACTERIZATION_ERROR, CHARACTERIZATION_ERROR
            )
            if orientation != dominant:
                switches += 1
                orientation = dominant
                lambdas = apply_logical_pauli_round(lambdas, SWITCH_ERROR, SWITCH_ERROR)

        if orientation != dominant:
            mismatched_rounds += 1

        logical_x, logical_z = logical_error_rates(p_x, p_z, orientation)
        lambdas = apply_logical_pauli_round(lambdas, logical_x, logical_z)

    fidelity = entanglement_fidelity(lambdas)
    return {
        "protocol": protocol.name,
        "anisotropy": float(anisotropy),
        "drift_cycles": float(drift_cycles),
        "entanglement_fidelity": fidelity,
        "logical_error": 1.0 - fidelity,
        "lambda_x": float(lambdas[0]),
        "lambda_y": float(lambdas[1]),
        "lambda_z": float(lambdas[2]),
        "updates": float(updates),
        "switches": float(switches),
        "mismatched_round_fraction": mismatched_rounds / TOTAL_ROUNDS,
    }


def summarize_point(anisotropy: float, drift_cycles: float) -> list[dict[str, float | str]]:
    rows = [
        run_protocol(protocol, float(anisotropy), float(drift_cycles))
        for protocol in PROTOCOLS
    ]
    best_static_error = min(
        float(row["logical_error"])
        for row in rows
        if row["protocol"] in {"fixed_x", "fixed_z", "static_tailored"}
    )
    adaptive_error = next(
        float(row["logical_error"])
        for row in rows
        if row["protocol"] == "adaptive_tailored"
    )
    overactive_error = next(
        float(row["logical_error"])
        for row in rows
        if row["protocol"] == "overactive_adaptive"
    )
    best_protocol = min(rows, key=lambda row: float(row["logical_error"]))["protocol"]
    eps = 1e-12

    for row in rows:
        row["best_static_logical_error"] = best_static_error
        row["adaptive_benefit_log10"] = float(
            np.log10((best_static_error + eps) / (adaptive_error + eps))
        )
        row["overactive_penalty_log10"] = float(
            np.log10((overactive_error + eps) / (adaptive_error + eps))
        )
        row["best_protocol"] = str(best_protocol)
    return rows


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for anisotropy in ANISOTROPY_VALUES:
        for drift_cycles in DRIFT_VALUES:
            rows.extend(summarize_point(float(anisotropy), float(drift_cycles)))
    return rows


def write_csv(rows: list[dict[str, float | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def protocol_rows(rows: list[dict[str, float | str]], protocol: str) -> list[dict[str, float | str]]:
    return [row for row in rows if row["protocol"] == protocol]


def grid(rows: list[dict[str, float | str]], key: str) -> np.ndarray:
    values = np.zeros((len(ANISOTROPY_VALUES), len(DRIFT_VALUES)))
    index = {
        (round(float(r["anisotropy"]), 6), round(float(r["drift_cycles"]), 6)): float(r[key])
        for r in rows
    }
    for i, anisotropy in enumerate(ANISOTROPY_VALUES):
        for j, drift_cycles in enumerate(DRIFT_VALUES):
            values[i, j] = index[(round(float(anisotropy), 6), round(float(drift_cycles), 6))]
    return values


def write_heatmap(rows: list[dict[str, float | str]]) -> None:
    adaptive = protocol_rows(rows, "adaptive_tailored")
    overactive = protocol_rows(rows, "overactive_adaptive")
    benefit = grid(adaptive, "adaptive_benefit_log10")
    adaptive_error = grid(adaptive, "logical_error")
    mismatch = grid(adaptive, "mismatched_round_fraction")
    overactive_penalty = grid(overactive, "overactive_penalty_log10")

    fig, axes = plt.subplots(1, 4, figsize=(18, 4), constrained_layout=True)
    panels = [
        ("adaptive benefit vs best static", benefit, "coolwarm", None, None),
        ("adaptive logical error", adaptive_error, "magma", 0.0, None),
        ("adaptive mismatch fraction", mismatch, "viridis", 0.0, 1.0),
        ("overactive penalty", overactive_penalty, "cividis", 0.0, None),
    ]
    for ax, (title, values, cmap, vmin, vmax) in zip(axes, panels):
        im = ax.imshow(
            values,
            origin="lower",
            aspect="auto",
            extent=[
                DRIFT_VALUES[0],
                DRIFT_VALUES[-1],
                ANISOTROPY_VALUES[0],
                ANISOTROPY_VALUES[-1],
            ],
            cmap=cmap,
            vmin=vmin if vmin is not None else float(values.min()),
            vmax=vmax if vmax is not None else float(values.max()),
        )
        ax.set_title(title)
        ax.set_xlabel("drift cycles over memory")
        ax.set_ylabel("noise anisotropy")
        fig.colorbar(im, ax=ax)
    fig.suptitle("Adaptive syndrome alignment: 3-qubit repetition benchmark")
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def write_curves(rows: list[dict[str, float | str]]) -> None:
    selected_anisotropies = [0.0, 0.3, 0.6, 0.9]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)

    for target in selected_anisotropies:
        anisotropy = min(ANISOTROPY_VALUES, key=lambda x: abs(float(x) - target))
        adaptive = [
            r
            for r in protocol_rows(rows, "adaptive_tailored")
            if abs(float(r["anisotropy"]) - float(anisotropy)) < 1e-9
        ]
        adaptive.sort(key=lambda r: float(r["drift_cycles"]))
        x = [float(r["drift_cycles"]) for r in adaptive]
        axes[0].plot(
            x,
            [float(r["adaptive_benefit_log10"]) for r in adaptive],
            label=f"anisotropy={float(anisotropy):.2f}",
        )
        axes[1].plot(
            x,
            [float(r["logical_error"]) for r in adaptive],
            label=f"anisotropy={float(anisotropy):.2f}",
        )

    axes[0].axhline(0.0, color="black", linewidth=1.0, alpha=0.5)
    axes[0].set_title("Benefit over best static baseline")
    axes[0].set_xlabel("drift cycles over memory")
    axes[0].set_ylabel("log10(error_static / error_adaptive)")
    axes[0].grid(alpha=0.25)
    axes[0].legend()

    axes[1].set_title("Adaptive logical error")
    axes[1].set_xlabel("drift cycles over memory")
    axes[1].set_ylabel("1 - entanglement fidelity")
    axes[1].grid(alpha=0.25)
    axes[1].legend()

    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_heatmap(rows)
    write_curves(rows)

    adaptive = protocol_rows(rows, "adaptive_tailored")
    best_adaptive = max(adaptive, key=lambda r: float(r["adaptive_benefit_log10"]))
    best_overall = min(rows, key=lambda r: float(r["logical_error"]))
    best_counts: dict[str, int] = {}
    for row in adaptive:
        best_counts[str(row["best_protocol"])] = best_counts.get(str(row["best_protocol"]), 0) + 1

    print(f"wrote {CSV_PATH}")
    print(f"wrote {HEATMAP_PATH}")
    print(f"wrote {CURVES_PATH}")
    print(
        "max adaptive benefit: "
        f"{float(best_adaptive['adaptive_benefit_log10']):.3f} log10 at "
        f"anisotropy={float(best_adaptive['anisotropy']):.3f}, "
        f"drift={float(best_adaptive['drift_cycles']):.3f}"
    )
    print(
        "best logical error: "
        f"{float(best_overall['logical_error']):.4f} from {best_overall['protocol']} "
        f"at anisotropy={float(best_overall['anisotropy']):.3f}, "
        f"drift={float(best_overall['drift_cycles']):.3f}"
    )
    print(f"best protocol counts over grid: {best_counts}")


if __name__ == "__main__":
    main()
