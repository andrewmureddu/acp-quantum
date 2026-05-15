#!/usr/bin/env python3
"""Recreate reproducible results from the formal shadow-geometry paper.

This script intentionally separates analytic/numeric reproductions from the
under-specified original SACR simulation. The paper's 99.1% coherence floor can
be recreated only as the stated Lyapunov calibration target unless the full
implemented cycle map is supplied.
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

SUMMARY_PATH = OUT / "reproduction_summary.csv"
PROTECTION_PATH = OUT / "protection_factor.csv"
DECOHERENCE_PATH = OUT / "decoherence_t2.csv"
LINDBLAD_PATH = OUT / "lindblad_dfs.csv"
KL_PATH = OUT / "approximate_kl_defect.csv"
LYAPUNOV_PATH = OUT / "lyapunov_floor.csv"
PLOT_PATH = OUT / "shadow_geometry_reproduction.png"


@dataclass
class Result:
    claim: str
    target: str
    measured: float
    tolerance: float
    passed: bool
    note: str


def write_rows(path: Path, rows: list[dict[str, float | int | str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def spectral_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord=2))


def lindblad_dissipator(l_op: np.ndarray, rho: np.ndarray) -> np.ndarray:
    return l_op @ rho @ l_op.conj().T - 0.5 * (
        l_op.conj().T @ l_op @ rho + rho @ l_op.conj().T @ l_op
    )


def protection_factor_reproduction(rng: np.random.Generator) -> tuple[list[dict[str, float]], Result]:
    rows: list[dict[str, float]] = []
    samples = 120_000
    for dim in range(2, 9):
        x = rng.normal(size=(samples, dim))
        x /= np.linalg.norm(x, axis=1, keepdims=True)
        projection = x[:, 0] ** 2
        beta_mc = 1.0 - float(np.mean(projection))
        beta_exact = 1.0 - 1.0 / dim
        rows.append(
            {
                "dimension": float(dim),
                "beta_exact": beta_exact,
                "beta_monte_carlo": beta_mc,
                "absolute_error": abs(beta_mc - beta_exact),
            }
        )

    beta3 = next(row for row in rows if int(row["dimension"]) == 3)
    return rows, Result(
        claim="projection protection beta(3)",
        target="2/3",
        measured=float(beta3["beta_monte_carlo"]),
        tolerance=4.0e-3,
        passed=abs(float(beta3["beta_monte_carlo"]) - (2.0 / 3.0)) < 4.0e-3,
        note="Monte Carlo confirmation of beta(d)=1-1/d.",
    )


def berry_phase_reproduction() -> Result:
    steps = 4096
    phis = np.linspace(0.0, 2.0 * np.pi, steps, endpoint=False)
    states = np.column_stack(
        [
            np.ones(steps, dtype=complex) / np.sqrt(2.0),
            np.exp(1j * phis) / np.sqrt(2.0),
        ]
    )
    product = 1.0 + 0.0j
    for i in range(steps):
        product *= np.vdot(states[i], states[(i + 1) % steps])
    phase = float(np.mod(np.angle(product), 2.0 * np.pi))
    distance_to_pi = abs(phase - np.pi)
    return Result(
        claim="dark-state full-loop Berry phase",
        target="pi mod 2pi",
        measured=phase,
        tolerance=1.0e-6,
        passed=distance_to_pi < 1.0e-6,
        note="Pancharatnam product for (|0>+exp(i phi)|1>)/sqrt(2).",
    )


def decoherence_t2_reproduction() -> tuple[list[dict[str, float | str]], Result]:
    times = np.linspace(0.0, 3.0, 121)
    aligned_ell = (1.0, 1.0)
    misaligned_ell = (0.0, 2.0)

    def rate(ells: tuple[float, float]) -> float:
        return 0.5 * abs(ells[0] - ells[1]) ** 2

    aligned_rate = rate(aligned_ell)
    misaligned_rate = rate(misaligned_ell)
    rows: list[dict[str, float | str]] = []
    for t in times:
        rows.append(
            {
                "case": "aligned",
                "time": float(t),
                "rate": aligned_rate,
                "coherence": float(np.exp(-aligned_rate * t)),
            }
        )
        rows.append(
            {
                "case": "misaligned",
                "time": float(t),
                "rate": misaligned_rate,
                "coherence": float(np.exp(-misaligned_rate * t)),
            }
        )

    target_at_t1 = float(np.exp(-2.0))
    measured_at_t1 = next(
        float(row["coherence"])
        for row in rows
        if row["case"] == "misaligned" and abs(float(row["time"]) - 1.0) < 1e-12
    )
    return rows, Result(
        claim="standard T2 dephasing law",
        target="exp(-2) at t=1",
        measured=measured_at_t1,
        tolerance=1.0e-12,
        passed=abs(measured_at_t1 - target_at_t1) < 1.0e-12,
        note="Misaligned eigenvalue gap 2 gives 1/T2=2; aligned gap 0 gives no decay.",
    )


def lindblad_dfs_reproduction() -> tuple[list[dict[str, float | str]], Result]:
    l_op = np.diag([1.0, 1.0, -1.0, 0.3]).astype(complex)

    rho_aligned = np.zeros((4, 4), dtype=complex)
    rho_aligned[:2, :2] = np.array([[0.5, 0.4], [0.4, 0.5]], dtype=complex)

    rho_misaligned = np.zeros((4, 4), dtype=complex)
    rho_misaligned[np.ix_([0, 2], [0, 2])] = np.array(
        [[0.5, 0.4], [0.4, 0.5]], dtype=complex
    )

    dissipator_aligned = lindblad_dissipator(l_op, rho_aligned)
    dissipator_misaligned = lindblad_dissipator(l_op, rho_misaligned)
    aligned_norm = spectral_norm(dissipator_aligned)
    misaligned_norm = spectral_norm(dissipator_misaligned)

    rows = [
        {
            "case": "aligned_scalar_lindblad_action",
            "dissipator_spectral_norm": aligned_norm,
        },
        {
            "case": "misaligned_non_scalar_lindblad_action",
            "dissipator_spectral_norm": misaligned_norm,
        },
    ]

    return rows, Result(
        claim="exact DFS Lindblad cancellation",
        target="aligned dissipator norm 0",
        measured=aligned_norm,
        tolerance=1.0e-12,
        passed=aligned_norm < 1.0e-12 and misaligned_norm > 0.0,
        note="L acts as a scalar on the aligned code and non-scalar on the misaligned code.",
    )


def approximate_kl_reproduction() -> tuple[list[dict[str, float | str]], Result]:
    tau = 0.1
    g = 1.2
    eps = 0.03
    r_mu = 0.8
    delta_bound = g * eps * r_mu
    actual_delta_norm = 0.75 * delta_bound
    perturbation = actual_delta_norm * np.diag([1.0, -1.0]).astype(complex)
    identity = np.eye(2, dtype=complex)

    rows: list[dict[str, float | str]] = []
    all_passed = True
    max_ratio = 0.0
    for lambda_mu, label in [(0.7, "noncentered"), (0.0, "centered")]:
        l_eff = lambda_mu * identity + perturbation
        defect_operator = tau * (l_eff.conj().T @ l_eff - abs(lambda_mu) ** 2 * identity)
        defect = spectral_norm(defect_operator)
        bound = tau * (
            2.0 * abs(lambda_mu) * delta_bound + delta_bound * delta_bound
        )
        ratio = defect / bound if bound > 0.0 else 0.0
        max_ratio = max(max_ratio, ratio)
        all_passed = all_passed and defect <= bound + 1.0e-12
        rows.append(
            {
                "case": label,
                "tau": tau,
                "lambda": lambda_mu,
                "actual_delta_norm": actual_delta_norm,
                "delta_bound": delta_bound,
                "defect_norm": defect,
                "paper_bound": bound,
                "defect_to_bound_ratio": ratio,
            }
        )

    return rows, Result(
        claim="approximate Knill-Laflamme defect bound",
        target="defect <= perturbative bound",
        measured=max_ratio,
        tolerance=1.0,
        passed=all_passed,
        note="Includes centered lambda=0 case where degradation is second-order.",
    )


def lyapunov_floor_reproduction() -> tuple[list[dict[str, float]], Result]:
    q_star = 0.9
    eta_star = 9.0e-4
    floor = eta_star / (1.0 - q_star)
    rows: list[dict[str, float]] = []
    v0 = 1.0
    v = v0
    for n in range(81):
        bound = (q_star**n) * v0 + eta_star * (1.0 - q_star**n) / (1.0 - q_star)
        rows.append(
            {
                "cycle": float(n),
                "q_star": q_star,
                "eta_star": eta_star,
                "misalignment": v,
                "bound": bound,
                "coherence_floor_bound": 1.0 - floor,
            }
        )
        v = q_star * v + eta_star

    return rows, Result(
        claim="99.1% Lyapunov calibration floor",
        target="eta*/(1-q*) = 0.009",
        measured=floor,
        tolerance=1.0e-15,
        passed=abs(floor - 0.009) < 1.0e-15,
        note="Recreates calibration target, not the missing original SACR cycle map.",
    )


def write_summary(results: list[Result]) -> None:
    rows = [
        {
            "claim": r.claim,
            "target": r.target,
            "measured": r.measured,
            "tolerance": r.tolerance,
            "passed": int(r.passed),
            "note": r.note,
        }
        for r in results
    ]
    write_rows(SUMMARY_PATH, rows)


def write_plot(
    protection_rows: list[dict[str, float]],
    decoherence_rows: list[dict[str, float | str]],
    kl_rows: list[dict[str, float | str]],
    lyapunov_rows: list[dict[str, float]],
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8.0), constrained_layout=True)

    dims = [row["dimension"] for row in protection_rows]
    axes[0, 0].plot(dims, [row["beta_exact"] for row in protection_rows], label="exact")
    axes[0, 0].scatter(
        dims,
        [row["beta_monte_carlo"] for row in protection_rows],
        label="Monte Carlo",
        s=24,
    )
    axes[0, 0].set_title("projection protection factor")
    axes[0, 0].set_xlabel("effective dimension d")
    axes[0, 0].set_ylabel("beta(d)")
    axes[0, 0].grid(alpha=0.25)
    axes[0, 0].legend()

    for case in ["aligned", "misaligned"]:
        rows = [row for row in decoherence_rows if row["case"] == case]
        axes[0, 1].plot(
            [float(row["time"]) for row in rows],
            [float(row["coherence"]) for row in rows],
            label=case,
        )
    axes[0, 1].set_title("T2 coherence law")
    axes[0, 1].set_xlabel("time")
    axes[0, 1].set_ylabel("coherence")
    axes[0, 1].grid(alpha=0.25)
    axes[0, 1].legend()

    labels = [str(row["case"]) for row in kl_rows]
    defects = [float(row["defect_norm"]) for row in kl_rows]
    bounds = [float(row["paper_bound"]) for row in kl_rows]
    x = np.arange(len(labels))
    width = 0.35
    axes[1, 0].bar(x - width / 2, defects, width, label="defect")
    axes[1, 0].bar(x + width / 2, bounds, width, label="bound")
    axes[1, 0].set_xticks(x, labels)
    axes[1, 0].set_title("approximate KL defect")
    axes[1, 0].set_ylabel("spectral norm")
    axes[1, 0].grid(axis="y", alpha=0.25)
    axes[1, 0].legend()

    axes[1, 1].plot(
        [row["cycle"] for row in lyapunov_rows],
        [row["misalignment"] for row in lyapunov_rows],
        label="affine recurrence",
    )
    axes[1, 1].axhline(0.009, color="black", linewidth=1.0, linestyle="--", label="0.009 target")
    axes[1, 1].set_title("Lyapunov calibration floor")
    axes[1, 1].set_xlabel("cycle")
    axes[1, 1].set_ylabel("misalignment V")
    axes[1, 1].grid(alpha=0.25)
    axes[1, 1].legend()

    fig.suptitle("Formal shadow-geometry paper: reproducible numeric claims")
    fig.savefig(PLOT_PATH, dpi=180)
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(20260428)

    protection_rows, protection_result = protection_factor_reproduction(rng)
    berry_result = berry_phase_reproduction()
    decoherence_rows, decoherence_result = decoherence_t2_reproduction()
    lindblad_rows, lindblad_result = lindblad_dfs_reproduction()
    kl_rows, kl_result = approximate_kl_reproduction()
    lyapunov_rows, lyapunov_result = lyapunov_floor_reproduction()

    write_rows(PROTECTION_PATH, protection_rows)
    write_rows(DECOHERENCE_PATH, decoherence_rows)
    write_rows(LINDBLAD_PATH, lindblad_rows)
    write_rows(KL_PATH, kl_rows)
    write_rows(LYAPUNOV_PATH, lyapunov_rows)
    write_summary(
        [
            protection_result,
            berry_result,
            decoherence_result,
            lindblad_result,
            kl_result,
            lyapunov_result,
        ]
    )
    write_plot(protection_rows, decoherence_rows, kl_rows, lyapunov_rows)

    print(f"wrote {SUMMARY_PATH}")
    print(f"wrote {PROTECTION_PATH}")
    print(f"wrote {DECOHERENCE_PATH}")
    print(f"wrote {LINDBLAD_PATH}")
    print(f"wrote {KL_PATH}")
    print(f"wrote {LYAPUNOV_PATH}")
    print(f"wrote {PLOT_PATH}")
    print()
    for result in [
        protection_result,
        berry_result,
        decoherence_result,
        lindblad_result,
        kl_result,
        lyapunov_result,
    ]:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status}: {result.claim} -> measured {result.measured:.12g} ({result.target})")


if __name__ == "__main__":
    main()
