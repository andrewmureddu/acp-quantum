#!/usr/bin/env python3
"""ACP phase scan for a 3-qubit repetition code.

This simulation asks a deliberately ACP-shaped QEC question:

    How often should a system look for errors?

Too little syndrome extraction leaves bit-flip noise uncorrected: dissolution.
Too much syndrome extraction, if monitoring has logical backaction, dephases
the protected superposition: crystallization. A middle band preserves both
code-space structure and logical coherence.

The code uses Qiskit's quantum_info objects for state initialization and then
evolves the 8x8 density matrix directly with NumPy. Direct density-matrix
evolution keeps the recovery channel transparent and fast for parameter scans.
"""

from __future__ import annotations

import csv
import os
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(__file__).resolve().parent / "outputs" / ".mpl-cache")
)
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from qiskit.quantum_info import DensityMatrix, Statevector


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
CSV_PATH = OUT / "repetition_code_scan.csv"
HEATMAP_PATH = OUT / "repetition_code_acp_heatmap.png"
CURVES_PATH = OUT / "repetition_code_acp_curves.png"

N_QUBITS = 3
DIM = 2**N_QUBITS
TOTAL_TICKS = 72
NOISE_VALUES = np.linspace(0.0, 0.04, 33)
CORRECTION_INTERVALS = np.arange(1, 73)
BACKACTION_PER_RECOVERY = 0.012


def basis(index: int) -> np.ndarray:
    v = np.zeros(DIM, dtype=complex)
    v[index] = 1.0
    return v


KET_000 = basis(0)
KET_111 = basis(7)
KET_ZERO_L = KET_000
KET_PLUS_L = (KET_000 + KET_111) / np.sqrt(2)
RHO_ZERO_L = np.asarray(DensityMatrix(Statevector(KET_ZERO_L)).data, dtype=complex)
RHO_PLUS_L = np.asarray(DensityMatrix(Statevector(KET_PLUS_L)).data, dtype=complex)
PROJECTOR_ZERO_L = np.outer(KET_ZERO_L, KET_ZERO_L.conjugate())
PROJECTOR_PLUS_L = np.outer(KET_PLUS_L, KET_PLUS_L.conjugate())
PROJECTOR_CODE = np.outer(KET_000, KET_000.conjugate()) + np.outer(
    KET_111, KET_111.conjugate()
)


def bitflip_operator(qubit: int) -> np.ndarray:
    op = np.zeros((DIM, DIM), dtype=complex)
    mask = 1 << (N_QUBITS - 1 - qubit)
    for i in range(DIM):
        op[i ^ mask, i] = 1.0
    return op


X_OPS = [bitflip_operator(q) for q in range(N_QUBITS)]
Z_LOGICAL = np.diag([1, 1, 1, 1, -1, -1, -1, -1]).astype(complex)


def mask_operator(mask: int) -> np.ndarray:
    op = np.eye(DIM, dtype=complex)
    for q in range(N_QUBITS):
        if mask & (1 << q):
            op = X_OPS[q] @ op
    return op


MASK_OPS = [mask_operator(mask) for mask in range(2**N_QUBITS)]
MASK_WEIGHTS = [bin(mask).count("1") for mask in range(2**N_QUBITS)]


def projector(indices: list[int]) -> np.ndarray:
    p = np.zeros((DIM, DIM), dtype=complex)
    for idx in indices:
        p[idx, idx] = 1.0
    return p


# Syndrome subspaces for the 3-qubit bit-flip repetition code.
# Each pair contains the errored images of |000> and |111> with the same
# stabilizer syndrome.
SYNDROME_PROJECTORS = [
    projector([0b000, 0b111]),  # no error
    projector([0b100, 0b011]),  # qubit 0 flipped
    projector([0b010, 0b101]),  # qubit 1 flipped
    projector([0b001, 0b110]),  # qubit 2 flipped
]

RECOVERY_OPS = [
    np.eye(DIM, dtype=complex),
    X_OPS[0],
    X_OPS[1],
    X_OPS[2],
]

RECOVERY_KRAUS = [u @ p for u, p in zip(RECOVERY_OPS, SYNDROME_PROJECTORS)]


def bitflip_noise(rho: np.ndarray, p: float) -> np.ndarray:
    out = np.zeros_like(rho)
    for mask, op, weight in zip(range(2**N_QUBITS), MASK_OPS, MASK_WEIGHTS):
        probability = (p**weight) * ((1.0 - p) ** (N_QUBITS - weight))
        out += probability * op @ rho @ op.conjugate().T
    return out


def recovery_channel(rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ k.conjugate().T for k in RECOVERY_KRAUS)


def logical_dephasing(rho: np.ndarray, strength: float) -> np.ndarray:
    strength = float(np.clip(strength, 0.0, 0.5))
    return (1.0 - strength) * rho + strength * Z_LOGICAL @ rho @ Z_LOGICAL


def evolve(initial_rho: np.ndarray, p_noise: float, correction_interval: int) -> np.ndarray:
    rho = initial_rho.copy()
    for tick in range(1, TOTAL_TICKS + 1):
        rho = bitflip_noise(rho, p_noise)
        if tick % correction_interval == 0:
            rho = recovery_channel(rho)
            rho = logical_dephasing(rho, BACKACTION_PER_RECOVERY)
    return rho


def metrics(
    rho_zero: np.ndarray, rho_plus: np.ndarray, p_noise: float, correction_interval: int
) -> dict[str, float | int | str]:
    bit_fidelity = float(np.real(np.trace(PROJECTOR_ZERO_L @ rho_zero)))
    bit_advantage = max(0.0, 2.0 * bit_fidelity - 1.0)
    plus_fidelity = float(np.real(np.trace(PROJECTOR_PLUS_L @ rho_plus)))
    code_population = float(np.real(np.trace(PROJECTOR_CODE @ rho_zero)))
    logical_coherence = float(2.0 * abs(rho_plus[0, 7]))
    correction_rate = 1.0 / correction_interval
    record = 1.0 - (1.0 - correction_rate) ** TOTAL_TICKS
    monitoring_cost = 1.0 - (1.0 - 2.0 * BACKACTION_PER_RECOVERY) ** (
        TOTAL_TICKS // correction_interval
    )

    productive_score = bit_advantage * plus_fidelity * code_population * logical_coherence

    if code_population < 0.55 or bit_fidelity < 0.58:
        regime = "dissolved"
    elif logical_coherence < 0.42 and code_population >= 0.72:
        regime = "crystallized"
    else:
        regime = "productive"

    return {
        "p_noise": p_noise,
        "correction_interval": int(correction_interval),
        "correction_rate": correction_rate,
        "record": record,
        "monitoring_cost": monitoring_cost,
        "bit_fidelity": bit_fidelity,
        "bit_advantage": bit_advantage,
        "plus_fidelity": plus_fidelity,
        "code_population": code_population,
        "logical_coherence": logical_coherence,
        "productive_score": productive_score,
        "regime": regime,
    }


def scan() -> list[dict[str, float | int | str]]:
    rows: list[dict[str, float | int | str]] = []
    for p_noise in NOISE_VALUES:
        for interval in CORRECTION_INTERVALS:
            rho_zero = evolve(RHO_ZERO_L, float(p_noise), int(interval))
            rho_plus = evolve(RHO_PLUS_L, float(p_noise), int(interval))
            rows.append(metrics(rho_zero, rho_plus, float(p_noise), int(interval)))
    return rows


def write_csv(rows: list[dict[str, float | int | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def grid(rows: list[dict[str, float | int | str]], key: str) -> np.ndarray:
    values = np.zeros((len(NOISE_VALUES), len(CORRECTION_INTERVALS)))
    by_pair = {
        (round(float(r["p_noise"]), 6), int(r["correction_interval"])): float(r[key])
        for r in rows
    }
    for i, p in enumerate(NOISE_VALUES):
        for j, interval in enumerate(CORRECTION_INTERVALS):
            values[i, j] = by_pair[(round(float(p), 6), int(interval))]
    return values


def write_heatmap(rows: list[dict[str, float | int | str]]) -> None:
    score = grid(rows, "productive_score")
    bit_fidelity = grid(rows, "bit_fidelity")
    coherence = grid(rows, "logical_coherence")

    fig, axes = plt.subplots(1, 3, figsize=(15, 4), constrained_layout=True)
    panels = [
        ("productive score", score, "viridis"),
        ("bit fidelity", bit_fidelity, "magma"),
        ("logical coherence", coherence, "cividis"),
    ]
    for ax, (title, values, cmap) in zip(axes, panels):
        im = ax.imshow(
            values,
            origin="lower",
            aspect="auto",
            extent=[
                CORRECTION_INTERVALS[0],
                CORRECTION_INTERVALS[-1],
                NOISE_VALUES[0],
                NOISE_VALUES[-1],
            ],
            cmap=cmap,
            vmin=0,
            vmax=max(0.01, float(values.max())),
        )
        ax.set_title(title)
        ax.set_xlabel("correction interval")
        ax.set_ylabel("bit-flip probability per tick")
        fig.colorbar(im, ax=ax)
    fig.suptitle("3-qubit repetition code: ACP scan")
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def write_curves(rows: list[dict[str, float | int | str]]) -> None:
    selected_noise = [0.02, 0.06, 0.10, 0.14]
    fig, ax = plt.subplots(figsize=(8.5, 5))
    for target in selected_noise:
        p = min(NOISE_VALUES, key=lambda x: abs(float(x) - target))
        subset = [r for r in rows if abs(float(r["p_noise"]) - float(p)) < 1e-9]
        subset.sort(key=lambda r: int(r["correction_interval"]))
        ax.plot(
            [int(r["correction_interval"]) for r in subset],
            [float(r["productive_score"]) for r in subset],
            marker="o",
            label=f"p={float(p):.3f}",
        )
    ax.set_title("Productive interval ridge by noise level")
    ax.set_xlabel("correction interval")
    ax.set_ylabel("productive score")
    ax.legend()
    ax.grid(alpha=0.25)
    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_heatmap(rows)
    write_curves(rows)

    best = max(rows, key=lambda r: float(r["productive_score"]))
    regimes = {name: sum(1 for r in rows if r["regime"] == name) for name in sorted({str(r["regime"]) for r in rows})}
    print(f"wrote {CSV_PATH}")
    print(f"wrote {HEATMAP_PATH}")
    print(f"wrote {CURVES_PATH}")
    print(
        "best productive score: "
        f"{float(best['productive_score']):.4f} at "
        f"p={float(best['p_noise']):.3f}, interval={int(best['correction_interval'])}"
    )
    print(f"regime counts: {regimes}")


if __name__ == "__main__":
    main()
