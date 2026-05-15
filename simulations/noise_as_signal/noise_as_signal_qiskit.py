#!/usr/bin/env python3
"""Qiskit simulation: noise as signal, alignment as protection.

This simulation turns the ACP intuition into a small quantum information test:

    zero coupling -> no usable environmental syndrome (crystallization)
    unstructured noise -> logical leakage and state erasure (dissolution)
    structured noise -> syndrome geometry that an aligned encoding can ride

We compare two logical encodings under phase noise:

    unaligned: |+_U> = (|00> + |11>) / sqrt(2)
    aligned:   |+_A> = (|01> + |10>) / sqrt(2)

The aligned encoding is the two-qubit decoherence-free subspace for collective
dephasing. If both qubits receive the same random phase, |01> and |10> acquire
the same phase and the logical coherence survives. If the noise is independent,
the same encoding loses coherence.
"""

from __future__ import annotations

import csv
import os
from pathlib import Path
from typing import Sequence

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
CSV_PATH = OUT / "noise_as_signal_scan.csv"
HEATMAP_PATH = OUT / "noise_as_signal_heatmap.png"
CURVES_PATH = OUT / "noise_as_signal_curves.png"

LABELS = ["00", "01", "10", "11"]
NOISE_STRENGTHS = np.linspace(0.0, 2.5, 151)
STRUCTURE_VALUES = np.linspace(0.0, 1.0, 101)
GH_NODES, GH_WEIGHTS = np.polynomial.hermite.hermgauss(48)
GH_NORMAL_NODES = np.sqrt(2.0) * GH_NODES
GH_NORMAL_WEIGHTS = GH_WEIGHTS / np.sqrt(np.pi)


def superposition(label_a: str, label_b: str) -> np.ndarray:
    """Return density matrix for (|label_a> + |label_b>) / sqrt(2)."""

    ket = (Statevector.from_label(label_a).data + Statevector.from_label(label_b).data)
    ket = ket / np.linalg.norm(ket)
    return np.asarray(DensityMatrix(Statevector(ket)).data, dtype=complex)


RHO_UNALIGNED = superposition("00", "11")
RHO_ALIGNED = superposition("01", "10")
IDX = {label: i for i, label in enumerate(LABELS)}


def collective_charge(label: str) -> int:
    """Total Z charge: |0> contributes +1, |1> contributes -1."""

    return sum(1 if bit == "0" else -1 for bit in label)


def hamming(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))


CHARGES = [collective_charge(label) for label in LABELS]


def apply_structured_dephasing(
    rho: np.ndarray, noise_strength: float, structure_fraction: float
) -> np.ndarray:
    """Apply a mixed collective/independent dephasing channel.

    `structure_fraction=1` means fully collective dephasing: the environment has
    a coherent geometry that the DFS can align with.

    `structure_fraction=0` means fully independent dephasing: the noise carries
    no common structure for the two-qubit encoding to exploit.
    """

    sigma_collective = noise_strength * structure_fraction
    sigma_independent = noise_strength * (1.0 - structure_fraction)
    out = rho.copy()

    for i, label_i in enumerate(LABELS):
        for j, label_j in enumerate(LABELS):
            delta_charge = CHARGES[i] - CHARGES[j]
            distance = hamming(label_i, label_j)
            collective_decay = np.exp(-0.5 * (sigma_collective * delta_charge) ** 2)
            independent_decay = np.exp(-0.5 * (sigma_independent**2) * distance)
            out[i, j] *= collective_decay * independent_decay

    return out


def coherence(rho: np.ndarray, label_a: str, label_b: str) -> float:
    """Normalized branch coherence. A perfect superposition has value 1."""

    return float(2.0 * abs(rho[IDX[label_a], IDX[label_b]]))


def logsumexp(values: np.ndarray, axis: int | None = None) -> np.ndarray:
    """Small local logsumexp to keep the simulation dependency-light."""

    vmax = np.max(values, axis=axis, keepdims=True)
    summed = np.sum(np.exp(values - vmax), axis=axis, keepdims=True)
    out = vmax + np.log(summed)
    if axis is None:
        return np.squeeze(out)
    return np.squeeze(out, axis=axis)


def gaussian_mixture_mi_1d(means: Sequence[float], priors: Sequence[float]) -> float:
    """I(X;Y) in bits for Y = mean_X + N, N ~ Normal(0,1)."""

    mu = np.asarray(means, dtype=float)
    p = np.asarray(priors, dtype=float)
    p = p / p.sum()
    log_p = np.log(p)
    mi_nats = 0.0

    for class_index, prior in enumerate(p):
        y = mu[class_index] + GH_NORMAL_NODES
        log_components = log_p[:, None] - 0.5 * (y[None, :] - mu[:, None]) ** 2
        log_py = logsumexp(log_components, axis=0)
        log_py_given_x = -0.5 * (y - mu[class_index]) ** 2
        mi_nats += prior * float(
            np.sum(GH_NORMAL_WEIGHTS * (log_py_given_x - log_py))
        )

    return max(0.0, float(mi_nats / np.log(2.0)))


def binary_gaussian_mi_from_half_distance(half_distance: float) -> float:
    """I(X;Y) in bits for two equiprobable unit-covariance Gaussian classes.

    Only the distance between class means matters after projection onto the
    discriminating axis. `half_distance` is half the Euclidean mean separation.
    """

    a = float(max(0.0, half_distance))
    if a == 0.0:
        return 0.0

    y = a + GH_NORMAL_NODES
    conditional_entropy = np.sum(
        GH_NORMAL_WEIGHTS * np.logaddexp(0.0, -2.0 * a * y) / np.log(2.0)
    )
    return float(np.clip(1.0 - conditional_entropy, 0.0, 1.0))


def structured_syndrome_mi(noise_strength: float, structure_fraction: float) -> float:
    """I(collective charge; collective environment fragment), in bits.

    The fragment model is Y_c = sigma*s*q(X) + N. The prior is uniform over the
    four computational basis states, giving charge probabilities
    P(q=-2)=1/4, P(q=0)=1/2, P(q=2)=1/4.
    """

    sigma_collective = noise_strength * structure_fraction
    return gaussian_mixture_mi_1d(
        means=[-2.0 * sigma_collective, 0.0, 2.0 * sigma_collective],
        priors=[0.25, 0.5, 0.25],
    )


def aligned_logical_environment_mi(
    noise_strength: float, structure_fraction: float
) -> float:
    """I(aligned logical branch; environment fragments), in bits.

    For |01> and |10>, collective charge is identical. Only independent
    fragments distinguish the two logical branches.
    """

    sigma_independent = noise_strength * (1.0 - structure_fraction)
    return binary_gaussian_mi_from_half_distance(np.sqrt(2.0) * sigma_independent)


def unaligned_logical_environment_mi(
    noise_strength: float, structure_fraction: float
) -> float:
    """I(unaligned logical branch; environment fragments), in bits."""

    sigma_collective = noise_strength * structure_fraction
    sigma_independent = noise_strength * (1.0 - structure_fraction)
    half_distance = np.sqrt(4.0 * sigma_collective**2 + 2.0 * sigma_independent**2)
    return binary_gaussian_mi_from_half_distance(half_distance)


def binary_entropy_bits(probability: float) -> float:
    """Binary Shannon entropy H_2(p), in bits."""

    p = float(np.clip(probability, 0.0, 1.0))
    if p == 0.0 or p == 1.0:
        return 0.0
    return float(-p * np.log2(p) - (1.0 - p) * np.log2(1.0 - p))


def logical_entanglement_fidelity(coherence_factor: float) -> float:
    """Entanglement fidelity of the induced logical dephasing channel.

    For a logical qubit dephasing channel with off-diagonal multiplier eta,
    the maximally mixed entanglement fidelity is (1+eta)/2.
    """

    eta = float(np.clip(coherence_factor, 0.0, 1.0))
    return 0.5 * (1.0 + eta)


def logical_coherent_information(coherence_factor: float) -> float:
    """Coherent information of the induced logical dephasing channel, in bits.

    The input is the maximally mixed logical qubit. The output entropy is one
    bit and the entropy exchange is H_2((1+eta)/2).
    """

    fidelity = logical_entanglement_fidelity(coherence_factor)
    return float(max(0.0, 1.0 - binary_entropy_bits(fidelity)))


def classify(
    syndrome_mi: float,
    aligned_leak_mi: float,
    aligned_coherence: float,
    noise_tailored_score: float,
) -> str:
    if syndrome_mi < 0.05:
        return "no_syndrome"
    if aligned_coherence < 0.45 or aligned_leak_mi > 0.55:
        return "leakage_limited"
    if noise_tailored_score > 0.20 and aligned_leak_mi < 0.25:
        return "noise_tailored"
    return "transition"


def scan() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []

    for structure in STRUCTURE_VALUES:
        for strength in NOISE_STRENGTHS:
            rho_unaligned = apply_structured_dephasing(
                RHO_UNALIGNED, float(strength), float(structure)
            )
            rho_aligned = apply_structured_dephasing(
                RHO_ALIGNED, float(strength), float(structure)
            )

            unaligned_coherence = coherence(rho_unaligned, "00", "11")
            aligned_coherence = coherence(rho_aligned, "01", "10")
            syndrome_mi = structured_syndrome_mi(float(strength), float(structure))
            aligned_leak_mi = aligned_logical_environment_mi(
                float(strength), float(structure)
            )
            unaligned_leak_mi = unaligned_logical_environment_mi(
                float(strength), float(structure)
            )
            alignment_gain = aligned_coherence - unaligned_coherence
            noise_tailored_score = syndrome_mi * aligned_coherence * (1.0 - aligned_leak_mi)
            aligned_entanglement_fidelity = logical_entanglement_fidelity(
                aligned_coherence
            )
            unaligned_entanglement_fidelity = logical_entanglement_fidelity(
                unaligned_coherence
            )
            aligned_coherent_info = logical_coherent_information(aligned_coherence)
            unaligned_coherent_info = logical_coherent_information(unaligned_coherence)

            rows.append(
                {
                    "noise_strength": float(strength),
                    "structure_fraction": float(structure),
                    "structured_syndrome_mi_bits": syndrome_mi,
                    "aligned_logical_env_mi_bits": aligned_leak_mi,
                    "unaligned_logical_env_mi_bits": unaligned_leak_mi,
                    "unaligned_coherence": unaligned_coherence,
                    "aligned_coherence": aligned_coherence,
                    "alignment_gain": alignment_gain,
                    "aligned_entanglement_fidelity": aligned_entanglement_fidelity,
                    "unaligned_entanglement_fidelity": unaligned_entanglement_fidelity,
                    "aligned_coherent_information_bits": aligned_coherent_info,
                    "unaligned_coherent_information_bits": unaligned_coherent_info,
                    "noise_tailored_score": noise_tailored_score,
                    "regime": classify(
                        syndrome_mi,
                        aligned_leak_mi,
                        aligned_coherence,
                        noise_tailored_score,
                    ),
                }
            )

    return rows


def write_csv(rows: list[dict[str, float | str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def grid(rows: list[dict[str, float | str]], key: str) -> np.ndarray:
    values = np.zeros((len(STRUCTURE_VALUES), len(NOISE_STRENGTHS)))
    index = {
        (round(float(r["structure_fraction"]), 6), round(float(r["noise_strength"]), 6)): float(r[key])
        for r in rows
    }
    for i, structure in enumerate(STRUCTURE_VALUES):
        for j, strength in enumerate(NOISE_STRENGTHS):
            values[i, j] = index[(round(float(structure), 6), round(float(strength), 6))]
    return values


def write_heatmap(rows: list[dict[str, float | str]]) -> None:
    score = grid(rows, "noise_tailored_score")
    coherent_info = grid(rows, "aligned_coherent_information_bits")
    syndrome_mi = grid(rows, "structured_syndrome_mi_bits")
    logical_leak = grid(rows, "aligned_logical_env_mi_bits")

    fig, axes = plt.subplots(1, 4, figsize=(18, 4), constrained_layout=True)
    panels = [
        ("Noise-tailored score", score, "viridis"),
        ("I(charge; collective fragment)", syndrome_mi, "cividis"),
        ("I(aligned logical; environment)", logical_leak, "magma"),
        ("aligned coherent information", coherent_info, "plasma"),
    ]

    for ax, (title, values, cmap) in zip(axes, panels):
        im = ax.imshow(
            values,
            origin="lower",
            aspect="auto",
            extent=[
                NOISE_STRENGTHS[0],
                NOISE_STRENGTHS[-1],
                STRUCTURE_VALUES[0],
                STRUCTURE_VALUES[-1],
            ],
            cmap=cmap,
            vmin=float(values.min()),
            vmax=float(values.max()),
        )
        ax.set_title(title)
        ax.set_xlabel("noise / coupling strength")
        ax.set_ylabel("structure fraction")
        fig.colorbar(im, ax=ax)

    fig.suptitle("Noise as signal: aligned DFS vs unaligned encoding")
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def write_curves(rows: list[dict[str, float | str]]) -> None:
    selected_structures = [0.0, 0.25, 0.5, 0.75, 1.0]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)

    for target in selected_structures:
        structure = min(STRUCTURE_VALUES, key=lambda x: abs(float(x) - target))
        subset = [
            r
            for r in rows
            if abs(float(r["structure_fraction"]) - float(structure)) < 1e-9
        ]
        subset.sort(key=lambda r: float(r["noise_strength"]))
        x = [float(r["noise_strength"]) for r in subset]
        axes[0].plot(
            x,
            [float(r["aligned_coherence"]) for r in subset],
            label=f"structured={float(structure):.2f}",
        )
        axes[1].plot(
            x,
            [float(r["noise_tailored_score"]) for r in subset],
            label=f"structured={float(structure):.2f}",
        )

    axes[0].set_title("Aligned logical coherence")
    axes[0].set_xlabel("noise / coupling strength")
    axes[0].set_ylabel("2 |rho_01,10|")
    axes[0].grid(alpha=0.25)
    axes[0].legend()

    axes[1].set_title("Noise-tailored score")
    axes[1].set_xlabel("noise / coupling strength")
    axes[1].set_ylabel("syndrome MI x coherence x privacy")
    axes[1].grid(alpha=0.25)
    axes[1].legend()

    fig.savefig(CURVES_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_heatmap(rows)
    write_curves(rows)

    best = max(rows, key=lambda r: float(r["noise_tailored_score"]))
    regimes = {
        name: sum(1 for r in rows if r["regime"] == name)
        for name in sorted({str(r["regime"]) for r in rows})
    }

    print(f"wrote {CSV_PATH}")
    print(f"wrote {HEATMAP_PATH}")
    print(f"wrote {CURVES_PATH}")
    print(
        "best noise-tailored score: "
        f"{float(best['noise_tailored_score']):.4f} at "
        f"noise={float(best['noise_strength']):.3f}, "
        f"structure={float(best['structure_fraction']):.3f}"
    )
    print(f"regime counts: {regimes}")

    for structure in [0.0, 0.5, 0.9, 1.0]:
        subset = [
            r
            for r in rows
            if abs(float(r["structure_fraction"]) - structure) < 1e-9
        ]
        best_subset = max(subset, key=lambda r: float(r["noise_tailored_score"]))
        print(
            f"structure={structure:.1f}: best score="
            f"{float(best_subset['noise_tailored_score']):.3f} at "
            f"noise={float(best_subset['noise_strength']):.3f}; "
            f"aligned coherence={float(best_subset['aligned_coherence']):.3f}"
        )


if __name__ == "__main__":
    main()
