#!/usr/bin/env python3
"""Otherness-preserving recovery toy model.

The recovery apparatus is treated as a powerful controller. It can observe the
error syndrome and apply recovery. A separate `centrality` parameter controls
whether the apparatus also records the logical branch, which dephases the
protected superposition.
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
SCAN_CSV = OUT / "otherness_recovery_scan.csv"
SUMMARY_CSV = OUT / "otherness_recovery_summary.csv"
HEATMAP_PATH = OUT / "otherness_recovery_heatmap.png"
CURVES_PATH = OUT / "otherness_recovery_curves.png"

N_QUBITS = 3
DIM = 2**N_QUBITS
P_NOISE_VALUES = np.linspace(0.0, 0.25, 126)
CENTRALITY_VALUES = np.linspace(0.0, 1.0, 101)


def basis(index: int) -> np.ndarray:
    ket = np.zeros(DIM, dtype=complex)
    ket[index] = 1.0
    return ket


KET_0L = basis(0)
KET_1L = basis(7)
KET_PLUS = (KET_0L + KET_1L) / np.sqrt(2.0)
RHO_0L = np.outer(KET_0L, KET_0L.conjugate())
RHO_PLUS = np.outer(KET_PLUS, KET_PLUS.conjugate())
PROJECTOR_0L = np.outer(KET_0L, KET_0L.conjugate())
PROJECTOR_PLUS = np.outer(KET_PLUS, KET_PLUS.conjugate())
LOGICAL_Z = np.diag([1, 1, 1, 1, -1, -1, -1, -1]).astype(complex)


def bitflip_operator(qubit: int) -> np.ndarray:
    op = np.zeros((DIM, DIM), dtype=complex)
    mask = 1 << (N_QUBITS - 1 - qubit)
    for index in range(DIM):
        op[index ^ mask, index] = 1.0
    return op


X_OPS = [bitflip_operator(qubit) for qubit in range(N_QUBITS)]


def mask_operator(mask: int) -> np.ndarray:
    op = np.eye(DIM, dtype=complex)
    for qubit in range(N_QUBITS):
        if mask & (1 << qubit):
            op = X_OPS[qubit] @ op
    return op


MASKS = list(range(2**N_QUBITS))
MASK_OPS = [mask_operator(mask) for mask in MASKS]
MASK_WEIGHTS = np.array([bin(mask).count("1") for mask in MASKS])


def projector(indices: list[int]) -> np.ndarray:
    p = np.zeros((DIM, DIM), dtype=complex)
    for index in indices:
        p[index, index] = 1.0
    return p


SYNDROME_PROJECTORS = [
    projector([0b000, 0b111]),
    projector([0b100, 0b011]),
    projector([0b010, 0b101]),
    projector([0b001, 0b110]),
]
RECOVERY_OPS = [np.eye(DIM, dtype=complex), X_OPS[0], X_OPS[1], X_OPS[2]]
RECOVERY_KRAUS = [u @ p for u, p in zip(RECOVERY_OPS, SYNDROME_PROJECTORS)]


def syndrome(mask: int) -> int:
    """Return stabilizer syndrome label for a physical bit-flip mask."""

    e0 = (mask >> 2) & 1
    e1 = (mask >> 1) & 1
    e2 = mask & 1
    return (e0 ^ e1) * 2 + (e1 ^ e2)


SYNDROMES = np.array([syndrome(mask) for mask in MASKS])


def bitflip_noise(rho: np.ndarray, p_noise: float) -> np.ndarray:
    out = np.zeros_like(rho)
    for mask, op, weight in zip(MASKS, MASK_OPS, MASK_WEIGHTS):
        probability = (p_noise**weight) * ((1.0 - p_noise) ** (N_QUBITS - weight))
        out += probability * op @ rho @ op.conjugate().T
    return out


def syndrome_recovery(rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ k.conjugate().T for k in RECOVERY_KRAUS)


def logical_branch_record_backaction(rho: np.ndarray, centrality: float) -> np.ndarray:
    """Nonselective logical branch measurement with retained record probability."""

    c = float(np.clip(centrality, 0.0, 1.0))
    measured = 0.5 * (rho + LOGICAL_Z @ rho @ LOGICAL_Z)
    return (1.0 - c) * rho + c * measured


def entropy(probabilities: np.ndarray) -> float:
    p = probabilities[probabilities > 0.0]
    if len(p) == 0:
        return 0.0
    return float(-np.sum(p * np.log2(p)))


def syndrome_mi(p_noise: float) -> float:
    """I(error mask; syndrome), with deterministic syndrome map."""

    mask_probs = np.array(
        [
            (p_noise**weight) * ((1.0 - p_noise) ** (N_QUBITS - weight))
            for weight in MASK_WEIGHTS
        ],
        dtype=float,
    )
    syndrome_probs = np.zeros(4, dtype=float)
    for prob, s in zip(mask_probs, SYNDROMES):
        syndrome_probs[s] += prob
    return entropy(syndrome_probs)


def protocol_metrics(p_noise: float, centrality: float) -> dict[str, float | str]:
    rho_0 = logical_branch_record_backaction(
        syndrome_recovery(bitflip_noise(RHO_0L, p_noise)), centrality
    )
    rho_plus = logical_branch_record_backaction(
        syndrome_recovery(bitflip_noise(RHO_PLUS, p_noise)), centrality
    )

    bit_fidelity = float(np.real(np.trace(PROJECTOR_0L @ rho_0)))
    plus_fidelity = float(np.real(np.trace(PROJECTOR_PLUS @ rho_plus)))
    logical_coherence = float(2.0 * abs(rho_plus[0, 7]))
    syndrome_bits = syndrome_mi(p_noise)

    # Model the centralizing record as a binary erasure observation of the
    # logical branch. With probability centrality the branch is retained.
    logical_leakage = float(np.clip(centrality, 0.0, 1.0))
    bit_advantage = max(0.0, 2.0 * bit_fidelity - 1.0)
    otherness_score = (
        syndrome_bits * bit_advantage * plus_fidelity * logical_coherence * (1.0 - logical_leakage)
    )

    if syndrome_bits < 0.05:
        regime = "abandonment_no_syndrome"
    elif logical_leakage > 0.35 or logical_coherence < 0.45:
        regime = "centralized"
    elif otherness_score > 0.20:
        regime = "otherness_preserving"
    else:
        regime = "transition"

    return {
        "p_noise": float(p_noise),
        "centrality": float(centrality),
        "syndrome_mi_bits": float(syndrome_bits),
        "controller_logical_leakage_bits": logical_leakage,
        "bit_fidelity": bit_fidelity,
        "bit_advantage": bit_advantage,
        "plus_fidelity": plus_fidelity,
        "logical_coherence": logical_coherence,
        "otherness_score": float(otherness_score),
        "regime": regime,
    }


def no_recovery_metrics(p_noise: float) -> dict[str, float]:
    rho_0 = bitflip_noise(RHO_0L, p_noise)
    rho_plus = bitflip_noise(RHO_PLUS, p_noise)
    return {
        "p_noise": float(p_noise),
        "syndrome_mi_bits": 0.0,
        "controller_logical_leakage_bits": 0.0,
        "bit_fidelity": float(np.real(np.trace(PROJECTOR_0L @ rho_0))),
        "plus_fidelity": float(np.real(np.trace(PROJECTOR_PLUS @ rho_plus))),
        "logical_coherence": float(2.0 * abs(rho_plus[0, 7])),
    }


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for p_noise in P_NOISE_VALUES:
        for centrality in CENTRALITY_VALUES:
            rows.append(protocol_metrics(float(p_noise), float(centrality)))
    return rows


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, float | str]]) -> list[dict[str, str]]:
    best = max(rows, key=lambda row: float(row["otherness_score"]))
    counts: dict[str, int] = {}
    for row in rows:
        regime = str(row["regime"])
        counts[regime] = counts.get(regime, 0) + 1

    p_mid = 0.08
    restrained = protocol_metrics(p_mid, 0.0)
    central = protocol_metrics(p_mid, 1.0)
    absent = no_recovery_metrics(p_mid)

    summary = [
        {"metric": "grid_points", "value": str(len(rows))},
        {"metric": "max_otherness_score", "value": f"{float(best['otherness_score']):.6f}"},
        {"metric": "max_score_p_noise", "value": f"{float(best['p_noise']):.6f}"},
        {"metric": "max_score_centrality", "value": f"{float(best['centrality']):.6f}"},
        {"metric": "max_score_syndrome_mi_bits", "value": f"{float(best['syndrome_mi_bits']):.6f}"},
        {"metric": "max_score_logical_coherence", "value": f"{float(best['logical_coherence']):.6f}"},
        {"metric": "max_score_regime", "value": str(best["regime"])},
        {"metric": "p_mid", "value": f"{p_mid:.6f}"},
        {"metric": "p_mid_absent_bit_fidelity", "value": f"{absent['bit_fidelity']:.6f}"},
        {"metric": "p_mid_restrained_bit_fidelity", "value": f"{float(restrained['bit_fidelity']):.6f}"},
        {"metric": "p_mid_central_bit_fidelity", "value": f"{float(central['bit_fidelity']):.6f}"},
        {"metric": "p_mid_absent_logical_coherence", "value": f"{absent['logical_coherence']:.6f}"},
        {"metric": "p_mid_restrained_logical_coherence", "value": f"{float(restrained['logical_coherence']):.6f}"},
        {"metric": "p_mid_central_logical_coherence", "value": f"{float(central['logical_coherence']):.6f}"},
    ]
    for regime, count in sorted(counts.items()):
        summary.append({"metric": f"count_{regime}", "value": str(count)})
    return summary


def grid(rows: list[dict[str, float | str]], key: str) -> np.ndarray:
    return np.array([float(row[key]) for row in rows]).reshape(
        len(P_NOISE_VALUES), len(CENTRALITY_VALUES)
    )


def plot_heatmap(rows: list[dict[str, float | str]]) -> None:
    score = grid(rows, "otherness_score")
    coherence = grid(rows, "logical_coherence")

    fig, ax = plt.subplots(figsize=(8.4, 5.6), constrained_layout=True)
    image = ax.imshow(
        score,
        origin="lower",
        aspect="auto",
        extent=[
            CENTRALITY_VALUES.min(),
            CENTRALITY_VALUES.max(),
            P_NOISE_VALUES.min(),
            P_NOISE_VALUES.max(),
        ],
        cmap="viridis",
    )
    ax.contour(
        CENTRALITY_VALUES,
        P_NOISE_VALUES,
        coherence,
        levels=[0.45],
        colors="red",
        linewidths=1.0,
    )
    ax.set_title("Otherness-preserving recovery score")
    ax.set_xlabel("controller centrality")
    ax.set_ylabel("physical bit-flip probability")
    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label("otherness score")
    ax.text(
        0.03,
        0.94,
        "red: logical coherence = 0.45",
        transform=ax.transAxes,
        color="white",
        fontsize=9,
        bbox={"facecolor": "black", "alpha": 0.35, "edgecolor": "none"},
    )
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def plot_curves(rows: list[dict[str, float | str]]) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5), constrained_layout=True)
    centrality_slices = [0.0, 0.2, 0.5, 1.0]

    for centrality in centrality_slices:
        selected = [
            row for row in rows if abs(float(row["centrality"]) - centrality) < 1e-9
        ]
        p_values = [float(row["p_noise"]) for row in selected]
        scores = [float(row["otherness_score"]) for row in selected]
        coherences = [float(row["logical_coherence"]) for row in selected]
        axes[0].plot(p_values, scores, label=f"centrality={centrality:.1f}")
        axes[1].plot(p_values, coherences, label=f"centrality={centrality:.1f}")

    axes[0].set_title("Otherness score")
    axes[0].set_xlabel("physical bit-flip probability")
    axes[0].set_ylabel("score")
    axes[0].legend(frameon=False)
    axes[1].set_title("Logical coherence")
    axes[1].set_xlabel("physical bit-flip probability")
    axes[1].set_ylabel("coherence")
    axes[1].legend(frameon=False)
    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = scan()
    write_csv(SCAN_CSV, rows)
    summary_rows = summarize(rows)
    write_csv(SUMMARY_CSV, summary_rows)
    plot_heatmap(rows)
    plot_curves(rows)

    best = max(rows, key=lambda row: float(row["otherness_score"]))
    print("Otherness-preserving recovery scan complete")
    print(f"grid points: {len(rows)}")
    print(
        "max score: "
        f"{float(best['otherness_score']):.4f} at "
        f"p_noise={float(best['p_noise']):.3f}, "
        f"centrality={float(best['centrality']):.3f}"
    )
    print(
        "at max: "
        f"I(error;syndrome)={float(best['syndrome_mi_bits']):.4f} bits, "
        f"logical leakage={float(best['controller_logical_leakage_bits']):.4f} bits, "
        f"logical coherence={float(best['logical_coherence']):.4f}, "
        f"regime={best['regime']}"
    )


if __name__ == "__main__":
    main()
