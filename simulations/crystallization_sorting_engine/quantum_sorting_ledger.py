#!/usr/bin/env python3
"""Coherent-information form of the crystallization sorting ledger.

Executable companion to Section 14 of `bridges/crystallization_sorting_engine.md`.

The classical ledger tracks a classical reference `S0` and reports contraction
as `destroyed`. Quantum mechanically nothing is destroyed: the global evolution
is an isometry and every bit that leaves the interior arrives somewhere. This
script makes that exact.

Setup
-----
A reference `R` (two qubits) is maximally entangled with the interior `A` (two
qubits), so the budget is

    I(R;A) = 2 H(R) = 4 bits.

Each step acts by a unitary on the interior together with one fresh boundary
record qubit `b_k` and one fresh environment qubit `e_k`, both prepared in
|0>. The global state on `R A B E` therefore stays pure and every entropy is
computed exactly from the state vector.

Ledger
------
    E_k = I(R; B_<=k)          exported to the boundary record
    J_k = I(R; A_k | B_<=k)    retained interior backlog
    T_k = I(R; A_k B_<=k)      total still reachable without the environment
    L_k = I(R; E_<=k)          leaked to the unrecorded environment

Purity of `R A B E` gives the three-way conservation law

    I(R; B) + I(R; A | B) + I(R; E) = 2 H(R)      exactly, at every step,

so the classical `destroyed` column is revealed as leakage:

    gamma_k = sigma_k + delta_k,    delta_k = L_{k+1} - L_k.

Coherent information differs from quantum mutual information by the constant
H(R), so the increments gamma, sigma, delta and the efficiency chi are
identical in either language:

    I_c(R>X) = I(R;X) - H(R),      T_k = E_k + J_k  in both.

Bounds checked numerically
--------------------------
    J_k >= 0                       strong subadditivity
    sigma_k <= gamma_k             no record without contraction
    sigma_k <= 2 log2 d_b          quantum bandwidth (2 bits per record qubit)
    conservation to 2 H(R)         purity

Classical-record cap
--------------------
If the boundary record is decohered, I(R;B) <= H(R) rather than 2 H(R), so a
purely classical record channel cannot exceed

    chi <= 1/2.

The dephasing scan traces the whole curve between the coherent and classical
limits and compares it against the closed form

    chi(theta) = 1 - h2((1 + cos(theta/2)) / 2) / 2.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
LEDGER_CSV = OUT / "quantum_sorting_ledger.csv"
SUMMARY_CSV = OUT / "quantum_sorting_summary.csv"
DEPHASING_CSV = OUT / "quantum_sorting_dephasing_scan.csv"

STEPS = 6
N_REF = 2
N_INT = 2
N_QUBITS = N_REF + N_INT + 2 * STEPS

REF = tuple(range(N_REF))
INT = tuple(range(N_REF, N_REF + N_INT))
REC = tuple(range(N_REF + N_INT, N_REF + N_INT + STEPS))
ENV = tuple(range(N_REF + N_INT + STEPS, N_QUBITS))

H_REF = float(N_REF)
BUDGET = 2.0 * H_REF
RECORD_CAPACITY_BITS = 2.0  # 2 log2 d for one record qubit

TOLERANCE = 1e-10


# --------------------------------------------------------------------------
# state vector machinery
# --------------------------------------------------------------------------


def bell_initial_state() -> np.ndarray:
    """Two Bell pairs: reference qubit i maximally entangled with interior i."""

    psi = np.zeros([2] * N_QUBITS, dtype=complex)
    for a in range(2):
        for b in range(2):
            index = [0] * N_QUBITS
            index[REF[0]] = a
            index[INT[0]] = a
            index[REF[1]] = b
            index[INT[1]] = b
            psi[tuple(index)] = 0.5
    return psi.reshape(-1)


def apply_two_qubit(state: np.ndarray, q1: int, q2: int, gate: np.ndarray) -> np.ndarray:
    psi = state.reshape([2] * N_QUBITS)
    psi = np.moveaxis(psi, (q1, q2), (0, 1)).reshape(4, -1)
    psi = gate @ psi
    psi = psi.reshape([2, 2] + [2] * (N_QUBITS - 2))
    psi = np.moveaxis(psi, (0, 1), (q1, q2))
    return psi.reshape(-1)


SWAP = np.array(
    [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex
)


def controlled_ry(theta: float) -> np.ndarray:
    """Control on the first qubit, RY(theta) on the second.

    At theta = pi this is CNOT, which copies the control's computational basis
    into the target: a complete measurement of the control by the target.
    """

    c, s = math.cos(theta / 2.0), math.sin(theta / 2.0)
    gate = np.eye(4, dtype=complex)
    gate[2:, 2:] = np.array([[c, -s], [s, c]], dtype=complex)
    return gate


# --------------------------------------------------------------------------
# entropies
# --------------------------------------------------------------------------


def reduced_density(state: np.ndarray, keep: Sequence[int]) -> np.ndarray:
    keep = sorted(keep)
    rest = [q for q in range(N_QUBITS) if q not in keep]
    psi = state.reshape([2] * N_QUBITS)
    psi = np.transpose(psi, keep + rest).reshape(2 ** len(keep), -1)
    return psi @ psi.conj().T


def entropy_bits(state: np.ndarray, keep: Sequence[int]) -> float:
    """Von Neumann entropy of a subsystem of a pure global state.

    Uses purity to diagonalize whichever side is smaller.
    """

    keep = sorted(keep)
    if not keep:
        return 0.0
    if len(keep) > N_QUBITS - len(keep):
        keep = [q for q in range(N_QUBITS) if q not in keep]
    if not keep:
        return 0.0
    eigenvalues = np.linalg.eigvalsh(reduced_density(state, keep))
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-(eigenvalues * np.log2(eigenvalues)).sum())


def mutual_information(state: np.ndarray, first: Sequence[int], second: Sequence[int]) -> float:
    return (
        entropy_bits(state, first)
        + entropy_bits(state, second)
        - entropy_bits(state, list(first) + list(second))
    )


def clamp(value: float, tolerance: float = 1e-12) -> float:
    return 0.0 if abs(value) < tolerance else float(value)


# --------------------------------------------------------------------------
# policies
# --------------------------------------------------------------------------


StepOp = Callable[[np.ndarray, int], np.ndarray]


@dataclass
class Policy:
    name: str
    step: StepOp
    note: str
    capacity_at: Callable[[int], float] = lambda k: (
        RECORD_CAPACITY_BITS if k < N_INT else 0.0
    )


def coherent_sort(state: np.ndarray, k: int) -> np.ndarray:
    """Move one interior qubit coherently into its record qubit."""

    if k < N_INT:
        return apply_two_qubit(state, INT[k], REC[k], SWAP)
    return state


def classical_sort(state: np.ndarray, k: int) -> np.ndarray:
    """Coherent transfer, then the environment reads the record in a fixed basis."""

    if k < N_INT:
        state = apply_two_qubit(state, INT[k], REC[k], SWAP)
        state = apply_two_qubit(state, REC[k], ENV[k], controlled_ry(math.pi))
    return state


def crush(state: np.ndarray, k: int) -> np.ndarray:
    """Contraction routed entirely to the unrecorded environment."""

    if k < N_INT:
        return apply_two_qubit(state, INT[k], ENV[k], SWAP)
    return state


def leaky_sort(state: np.ndarray, k: int) -> np.ndarray:
    """The environment gets a partial look before the record is written."""

    if k < N_INT:
        state = apply_two_qubit(state, INT[k], ENV[k], controlled_ry(math.pi / 2.0))
        state = apply_two_qubit(state, INT[k], REC[k], SWAP)
    return state


def sector_then_protected(state: np.ndarray, k: int) -> np.ndarray:
    """Export the sector qubit immediately, hold the protected qubit until late."""

    if k == 0:
        return apply_two_qubit(state, INT[0], REC[0], SWAP)
    if k == 4:
        return apply_two_qubit(state, INT[1], REC[4], SWAP)
    return state


def centralizing_sort(state: np.ndarray, k: int) -> np.ndarray:
    """Export both qubits immediately, including the protected one."""

    if k == 0:
        state = apply_two_qubit(state, INT[0], REC[0], SWAP)
        state = apply_two_qubit(state, INT[1], REC[1], SWAP)
    return state


def policies() -> list[Policy]:
    return [
        Policy("coherent_sort", coherent_sort, "lossless quantum transfer to the record"),
        Policy("classical_sort", classical_sort, "record decohered by the environment"),
        Policy("leaky_sort", leaky_sort, "environment gets a partial look first"),
        Policy("crush", crush, "contraction routed entirely to the environment", lambda k: 0.0),
        Policy(
            "sector_then_protected",
            sector_then_protected,
            "sector early, protected late",
            lambda k: RECORD_CAPACITY_BITS if k in (0, 4) else 0.0,
        ),
        Policy(
            "centralizing_sort",
            centralizing_sort,
            "lossless but reads the protected qubit",
            lambda k: 2.0 * RECORD_CAPACITY_BITS if k == 0 else 0.0,
        ),
    ]


# --------------------------------------------------------------------------
# ledger
# --------------------------------------------------------------------------


def measure(state: np.ndarray) -> dict[str, float]:
    exported = mutual_information(state, REF, REC)
    total = mutual_information(state, REF, list(INT) + list(REC))
    leaked = mutual_information(state, REF, ENV)
    return {
        "exported": clamp(exported),
        "total": clamp(total),
        "retained": clamp(total - exported),
        "leaked": clamp(leaked),
        "protected_exported": clamp(mutual_information(state, [REF[1]], REC)),
        "sector_exported": clamp(mutual_information(state, [REF[0]], REC)),
    }


def run_policy(policy: Policy) -> list[dict[str, float | str]]:
    state = bell_initial_state()
    stats = measure(state)
    rows: list[dict[str, float | str]] = [
        {
            "policy": policy.name,
            "step": 0,
            "exported_bits": stats["exported"],
            "retained_bits": stats["retained"],
            "total_bits": stats["total"],
            "leaked_bits": stats["leaked"],
            "conservation_residual": clamp(
                stats["exported"] + stats["retained"] + stats["leaked"] - BUDGET
            ),
            "contraction_bits": 0.0,
            "sorted_bits": 0.0,
            "destroyed_bits": 0.0,
            "coherent_exported_bits": stats["exported"] - H_REF,
            "coherent_total_bits": stats["total"] - H_REF,
            "sector_exported_bits": stats["sector_exported"],
            "protected_exported_bits": stats["protected_exported"],
            "capacity_bits": 0.0,
        }
    ]

    for k in range(STEPS):
        previous = stats
        state = policy.step(state, k)
        stats = measure(state)
        rows.append(
            {
                "policy": policy.name,
                "step": k + 1,
                "exported_bits": stats["exported"],
                "retained_bits": stats["retained"],
                "total_bits": stats["total"],
                "leaked_bits": stats["leaked"],
                "conservation_residual": clamp(
                    stats["exported"] + stats["retained"] + stats["leaked"] - BUDGET
                ),
                "contraction_bits": clamp(previous["retained"] - stats["retained"]),
                "sorted_bits": clamp(stats["exported"] - previous["exported"]),
                "destroyed_bits": clamp(previous["total"] - stats["total"]),
                "coherent_exported_bits": stats["exported"] - H_REF,
                "coherent_total_bits": stats["total"] - H_REF,
                "sector_exported_bits": stats["sector_exported"],
                "protected_exported_bits": stats["protected_exported"],
                "capacity_bits": policy.capacity_at(k),
            }
        )
    return rows


def summarize(policy: Policy, rows: Sequence[dict[str, float | str]]) -> dict[str, float | str]:
    body = rows[1:]
    contraction = clamp(sum(float(r["contraction_bits"]) for r in body))
    sorted_bits = clamp(sum(float(r["sorted_bits"]) for r in body))
    destroyed = clamp(sum(float(r["destroyed_bits"]) for r in body))
    leak_identity = max(
        abs(float(r["destroyed_bits"]) - (float(r["leaked_bits"]) - float(p["leaked_bits"])))
        for p, r in zip(rows[:-1], body)
    )
    early = max(float(r["protected_exported_bits"]) for r in rows[:3])
    return {
        "policy": policy.name,
        "contraction_bits": round(contraction, 9),
        "sorted_bits": round(sorted_bits, 9),
        "destroyed_bits": round(destroyed, 9),
        "chi": round(sorted_bits / contraction, 9) if contraction > 1e-12 else "",
        "final_exported_bits": round(float(rows[-1]["exported_bits"]), 9),
        "final_retained_bits": round(float(rows[-1]["retained_bits"]), 9),
        "final_leaked_bits": round(float(rows[-1]["leaked_bits"]), 9),
        "final_coherent_exported_bits": round(float(rows[-1]["coherent_exported_bits"]), 9),
        "early_protected_exported_bits": round(early, 9),
        "max_conservation_residual": f"{max(abs(float(r['conservation_residual'])) for r in rows):.3e}",
        "max_negative_backlog": f"{min(float(r['retained_bits']) for r in rows):.3e}",
        "max_sigma_minus_gamma": f"{max(float(r['sorted_bits']) - float(r['contraction_bits']) for r in body):.3e}",
        "max_sigma_minus_capacity": f"{max(float(r['sorted_bits']) - float(r['capacity_bits']) for r in body):.3e}",
        "max_delta_minus_leak_increment": f"{leak_identity:.3e}",
        "note": policy.note,
    }


# --------------------------------------------------------------------------
# dephasing scan
# --------------------------------------------------------------------------


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def predicted_chi(theta: float) -> float:
    """Closed form for the swap-then-dephase policy."""

    return 1.0 - binary_entropy((1.0 + math.cos(theta / 2.0)) / 2.0) / 2.0


def dephasing_scan(points: int = 13) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for index in range(points):
        theta = math.pi * index / (points - 1)

        def step(state: np.ndarray, k: int, theta: float = theta) -> np.ndarray:
            if k < N_INT:
                state = apply_two_qubit(state, INT[k], REC[k], SWAP)
                state = apply_two_qubit(state, REC[k], ENV[k], controlled_ry(theta))
            return state

        ledger = run_policy(Policy(f"dephasing_{index}", step, "scan"))
        body = ledger[1:]
        contraction = clamp(sum(float(r["contraction_bits"]) for r in body))
        sorted_bits = clamp(sum(float(r["sorted_bits"]) for r in body))
        chi = sorted_bits / contraction if contraction > 1e-12 else float("nan")
        rows.append(
            {
                "dephasing_theta": round(theta, 9),
                "dephasing_fraction": round(theta / math.pi, 9),
                "contraction_bits": round(contraction, 9),
                "sorted_bits": round(sorted_bits, 9),
                "destroyed_bits": round(
                    clamp(sum(float(r["destroyed_bits"]) for r in body)), 9
                ),
                "chi": round(chi, 9),
                "chi_closed_form": round(predicted_chi(theta), 9),
                "chi_residual": round(abs(chi - predicted_chi(theta)), 12),
            }
        )
    return rows


# --------------------------------------------------------------------------


def write_csv(path: Path, rows: Sequence[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict[str, float | str]] = []
    summaries: list[dict[str, float | str]] = []
    for policy in policies():
        rows = run_policy(policy)
        all_rows.extend(rows)
        summaries.append(summarize(policy, rows))

    scan = dephasing_scan()

    write_csv(LEDGER_CSV, all_rows)
    write_csv(SUMMARY_CSV, summaries)
    write_csv(DEPHASING_CSV, scan)

    print(
        f"H(R) = {H_REF:.1f} bits, budget 2H(R) = {BUDGET:.1f} bits, "
        f"{N_QUBITS} qubits, {STEPS} steps"
    )
    print(f"wrote {LEDGER_CSV}")
    print(f"wrote {SUMMARY_CSV}")
    print(f"wrote {DEPHASING_CSV}")
    print()
    header = (
        f"{'policy':<22}{'gamma':>8}{'sigma':>8}{'delta':>8}{'chi':>9}"
        f"{'B_end':>8}{'A_end':>8}{'E_end':>8}{'Ic(R>B)':>10}{'earlyL':>8}"
    )
    print(header)
    print("-" * len(header))
    for row in summaries:
        print(
            f"{row['policy']:<22}{float(row['contraction_bits']):>8.4f}"
            f"{float(row['sorted_bits']):>8.4f}{float(row['destroyed_bits']):>8.4f}"
            f"{float(row['chi']):>9.5f}"
            f"{float(row['final_exported_bits']):>8.4f}"
            f"{float(row['final_retained_bits']):>8.4f}"
            f"{float(row['final_leaked_bits']):>8.4f}"
            f"{float(row['final_coherent_exported_bits']):>10.4f}"
            f"{float(row['early_protected_exported_bits']):>8.4f}"
        )

    print()
    print("dephasing scan: classicality of the record as a continuous knob")
    print(f"{'theta/pi':>9}{'gamma':>9}{'sigma':>9}{'chi':>10}{'closed form':>13}{'residual':>12}")
    for row in scan:
        print(
            f"{row['dephasing_fraction']:>9.4f}{row['contraction_bits']:>9.4f}"
            f"{row['sorted_bits']:>9.4f}{row['chi']:>10.6f}"
            f"{row['chi_closed_form']:>13.6f}{row['chi_residual']:>12.2e}"
        )

    print()
    for row in summaries:
        print(
            f"{row['policy']}: conservation {row['max_conservation_residual']}, "
            f"min backlog {row['max_negative_backlog']}, "
            f"max(sigma-gamma) {row['max_sigma_minus_gamma']}, "
            f"max(sigma-capacity) {row['max_sigma_minus_capacity']}, "
            f"max|delta - dI(R;E)| {row['max_delta_minus_leak_increment']}"
        )


if __name__ == "__main__":
    main()
