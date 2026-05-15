#!/usr/bin/env python3
r"""Compute SACR-style contraction parameters for finite CPTP cycle maps.

The useful finite diagnostic from the shadow-geometry paper is:

    q*   = sup_{rho supported on Q} Tr(Q Phi(rho))
    eta* = sup_{rho supported on P} Tr(Q Phi(rho))

For a Kraus representation Phi(rho)=sum_a K_a rho K_a^\dagger, these are the
largest eigenvalues of Phi^\dagger(Q) restricted to the leakage sector Q and
aligned sector P respectively.

The included scan is a deliberately small two-sector toy. It is a harness for
the calibration target, not a validation of any hardware SACR protocol.
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


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
CSV_PATH = OUT / "sacr_contraction_scan.csv"
HEATMAP_PATH = OUT / "sacr_contraction_heatmap.png"

TARGET_FLOOR = 9.0e-3
LEAKAGE_VALUES = np.linspace(0.0, 0.02, 81)
RECOVERY_VALUES = np.linspace(0.01, 1.0, 100)


def sector_projectors() -> tuple[np.ndarray, np.ndarray]:
    """Return projectors P and Q for a 2+2 aligned/leakage decomposition."""

    p = np.diag([1.0, 1.0, 0.0, 0.0]).astype(complex)
    q = np.diag([0.0, 0.0, 1.0, 1.0]).astype(complex)
    return p, q


def sector_transfer_kraus(leakage: float, recovery: float) -> list[np.ndarray]:
    """Kraus operators for a label-preserving P<->Q sector-transfer toy map."""

    leakage = float(np.clip(leakage, 0.0, 1.0))
    recovery = float(np.clip(recovery, 0.0, 1.0))
    p, q = sector_projectors()

    w_pq = np.zeros((4, 4), dtype=complex)
    w_pq[2, 0] = 1.0
    w_pq[3, 1] = 1.0

    w_qp = np.zeros((4, 4), dtype=complex)
    w_qp[0, 2] = 1.0
    w_qp[1, 3] = 1.0

    return [
        np.sqrt(1.0 - leakage) * p,
        np.sqrt(leakage) * w_pq,
        np.sqrt(recovery) * w_qp,
        np.sqrt(1.0 - recovery) * q,
    ]


def assert_cptp(kraus: list[np.ndarray], atol: float = 1e-10) -> None:
    """Raise if the supplied Kraus operators are not trace-preserving."""

    dim = kraus[0].shape[1]
    completeness = sum(k.conj().T @ k for k in kraus)
    if not np.allclose(completeness, np.eye(dim), atol=atol):
        raise ValueError("Kraus operators are not trace-preserving")


def restricted_lambda_max(effect: np.ndarray, projector: np.ndarray) -> float:
    """Largest eigenvalue of projector @ effect @ projector on its support."""

    support = np.flatnonzero(np.real(np.diag(projector)) > 0.5)
    restricted = effect[np.ix_(support, support)]
    eigvals = np.linalg.eigvalsh((restricted + restricted.conj().T) / 2.0)
    return float(np.clip(eigvals[-1], 0.0, 1.0))


def contraction_parameters(
    kraus: list[np.ndarray], p: np.ndarray, q: np.ndarray
) -> tuple[float, float, float]:
    """Return q_star, eta_star, and eta_star/(1-q_star)."""

    assert_cptp(kraus)
    leakage_effect = sum(k.conj().T @ q @ k for k in kraus)
    q_star = restricted_lambda_max(leakage_effect, q)
    eta_star = restricted_lambda_max(leakage_effect, p)
    if q_star >= 1.0:
        floor_bound = float("inf")
    else:
        floor_bound = eta_star / (1.0 - q_star)
    return q_star, eta_star, floor_bound


def scan() -> list[dict[str, float | int]]:
    """Scan leakage and recovery probabilities for the two-sector toy map."""

    p, q = sector_projectors()
    rows: list[dict[str, float | int]] = []
    for leakage in LEAKAGE_VALUES:
        for recovery in RECOVERY_VALUES:
            kraus = sector_transfer_kraus(float(leakage), float(recovery))
            q_star, eta_star, floor_bound = contraction_parameters(kraus, p, q)
            rows.append(
                {
                    "leakage": float(leakage),
                    "recovery": float(recovery),
                    "q_star": q_star,
                    "eta_star": eta_star,
                    "floor_bound": floor_bound,
                    "coherence_floor": 1.0 - floor_bound,
                    "passes_99p1_target": int(floor_bound <= TARGET_FLOOR),
                }
            )
    return rows


def write_csv(rows: list[dict[str, float | int]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def heatmap_grid(rows: list[dict[str, float | int]], key: str) -> np.ndarray:
    values = np.zeros((len(LEAKAGE_VALUES), len(RECOVERY_VALUES)))
    index = {
        (round(float(row["leakage"]), 8), round(float(row["recovery"]), 8)): float(row[key])
        for row in rows
    }
    for i, leakage in enumerate(LEAKAGE_VALUES):
        for j, recovery in enumerate(RECOVERY_VALUES):
            values[i, j] = index[(round(float(leakage), 8), round(float(recovery), 8))]
    return values


def write_heatmap(rows: list[dict[str, float | int]]) -> None:
    floor = heatmap_grid(rows, "floor_bound")
    passes = heatmap_grid(rows, "passes_99p1_target")

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.5), constrained_layout=True)

    clipped_floor = np.minimum(floor, 0.05)
    im0 = axes[0].imshow(
        clipped_floor,
        origin="lower",
        aspect="auto",
        extent=[
            RECOVERY_VALUES[0],
            RECOVERY_VALUES[-1],
            LEAKAGE_VALUES[0],
            LEAKAGE_VALUES[-1],
        ],
        cmap="magma_r",
        vmin=0.0,
        vmax=0.05,
    )
    axes[0].contour(
        RECOVERY_VALUES,
        LEAKAGE_VALUES,
        floor,
        levels=[TARGET_FLOOR],
        colors="white",
        linewidths=1.2,
    )
    axes[0].set_title("asymptotic misalignment bound")
    axes[0].set_xlabel("recovery probability r")
    axes[0].set_ylabel("leakage probability ell")
    fig.colorbar(im0, ax=axes[0], label="eta*/(1-q*)")

    im1 = axes[1].imshow(
        passes,
        origin="lower",
        aspect="auto",
        extent=[
            RECOVERY_VALUES[0],
            RECOVERY_VALUES[-1],
            LEAKAGE_VALUES[0],
            LEAKAGE_VALUES[-1],
        ],
        cmap="Greens",
        vmin=0.0,
        vmax=1.0,
    )
    axes[1].set_title("passes 99.1% floor target")
    axes[1].set_xlabel("recovery probability r")
    axes[1].set_ylabel("leakage probability ell")
    fig.colorbar(im1, ax=axes[1], ticks=[0, 1])

    fig.suptitle("SACR contraction calibration toy: target ell/r <= 9e-3")
    fig.savefig(HEATMAP_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_heatmap(rows)

    passing = [row for row in rows if int(row["passes_99p1_target"]) == 1]
    best = min(rows, key=lambda row: float(row["floor_bound"]))
    largest_passing_leakage = max((float(row["leakage"]) for row in passing), default=0.0)
    weakest_passing_recovery = min((float(row["recovery"]) for row in passing), default=float("nan"))

    print(f"wrote {CSV_PATH}")
    print(f"wrote {HEATMAP_PATH}")
    print(
        "best floor bound: "
        f"{float(best['floor_bound']):.6f} at leakage={float(best['leakage']):.5f}, "
        f"recovery={float(best['recovery']):.3f}"
    )
    print(f"grid points passing 99.1% target: {len(passing)} / {len(rows)}")
    print(f"largest passing leakage in scan: {largest_passing_leakage:.5f}")
    print(f"weakest passing recovery in scan: {weakest_passing_recovery:.3f}")


if __name__ == "__main__":
    main()
