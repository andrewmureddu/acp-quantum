#!/usr/bin/env python3
"""Boundary decodability: Page turnover and the remnant capacity bound.

Companion to `bridges/boundary_decodability.md`, the Stage 5 rung of the
quantum-gravity derivation ladder.

Stage 5 asks whether ACP's decodable-redistribution criterion (Criterion 3 of
`bridges/cosmic_coordination_floor.md`) can be derived rather than posited.
The engine is the exact complementarity identity for a tripartite pure state:

    I(X_R ; Y_boundary) + I(X_R ; S_hidden) = 2 S(X_R),

which says boundary-decodable information and permanently hidden information
are in exact trade-off. Combined with finite-record admissibility -- no
unbounded permanently hidden capacity -- this forces the boundary record
entropy to turn over, and bounds how much capacity a completion may hide.

Model
-----
A reference register R purifies the protected interior information. The
collapsing region is a register H of n_H qubits. The global state on R (x) H is
Haar-random, which is the standard Page / Hayden-Preskill setting: it models a
maximally scrambling interior, the most favourable case for information return.

Evaporation releases hole qubits to the boundary record one at a time. A
completion that permanently hides `r` qubits releases only n_H - r of them.

Everything is computed from exact reduced density matrices and exact von
Neumann entropies -- no proxies. Pure standard library.

Predictions under test
----------------------
1. Complementarity is exact:  I(R;rad) + I(R;hid) = 2 S(R)  at every step.
2. Page turnover: for full evaporation S(rad) rises then falls, peaking when
   the radiation reaches half the total.
3. Remnant capacity bound: the interior information is decodable from the
   boundary only while

       log dim H_hidden  <=  log dim H_boundary - S(X_R),

   which for this model is r <= (n_H - r) - S(R), i.e. a sharp threshold in r.
"""

from __future__ import annotations

import cmath
import csv
import math
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
PAGE_CSV = OUT / "page_curve_timeseries.csv"
REMNANT_CSV = OUT / "remnant_bound_scan.csv"

N_REF = 1  # reference qubits purifying the protected interior information
N_HOLE = 9  # collapsing-region qubits
N_TOTAL = N_REF + N_HOLE

N_SAMPLES = 6
SEED = 20260726

JACOBI_SWEEPS = 12
JACOBI_TOL = 1e-12


# --------------------------------------------------------------------------
# random pure states
# --------------------------------------------------------------------------


def haar_state(dim: int, rng: random.Random) -> list[complex]:
    """A Haar-random pure state: normalized complex Gaussian vector."""
    vec = []
    for _ in range(dim):
        u1 = rng.random() or 1e-16
        u2 = rng.random()
        rad = math.sqrt(-2.0 * math.log(u1))
        vec.append(complex(rad * math.cos(2 * math.pi * u2), rad * math.sin(2 * math.pi * u2)))
    norm = math.sqrt(sum(abs(z) ** 2 for z in vec))
    return [z / norm for z in vec]


# --------------------------------------------------------------------------
# reduced density matrices
# --------------------------------------------------------------------------


def reduced_density_matrix(
    psi: list[complex], n_qubits: int, subset: list[int]
) -> list[list[complex]]:
    """rho_A for a subset A of qubit indices (qubit 0 = most significant).

    Builds M[a][b] = psi[index(a, b)] and returns M M^dagger.
    """
    subset = sorted(subset)
    comp = [q for q in range(n_qubits) if q not in subset]
    ka, kb = len(subset), len(comp)
    da, db = 1 << ka, 1 << kb

    # Bit position (from the most significant end) -> shift in the global index.
    def shift(q: int) -> int:
        return n_qubits - 1 - q

    m = [[0j] * db for _ in range(da)]
    for a in range(da):
        # Scatter the subset bits into their global positions.
        base_a = 0
        for i, q in enumerate(subset):
            if (a >> (ka - 1 - i)) & 1:
                base_a |= 1 << shift(q)
        row = m[a]
        for b in range(db):
            idx = base_a
            for i, q in enumerate(comp):
                if (b >> (kb - 1 - i)) & 1:
                    idx |= 1 << shift(q)
            row[b] = psi[idx]

    rho = [[0j] * da for _ in range(da)]
    for i in range(da):
        ri = m[i]
        for j in range(i, da):
            rj = m[j]
            acc = 0j
            for b in range(db):
                acc += ri[b] * rj[b].conjugate()
            rho[i][j] = acc
            if i != j:
                rho[j][i] = acc.conjugate()
    return rho


# --------------------------------------------------------------------------
# Hermitian eigenvalues via real-symmetric Jacobi
# --------------------------------------------------------------------------


def jacobi_eigenvalues(a: list[list[float]]) -> list[float]:
    """Eigenvalues of a real symmetric matrix by cyclic Jacobi rotation."""
    n = len(a)
    m = [row[:] for row in a]
    for _ in range(JACOBI_SWEEPS):
        off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                off += m[i][j] * m[i][j]
        if off < JACOBI_TOL:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = m[p][q]
                if abs(apq) < 1e-300:
                    continue
                app, aqq = m[p][p], m[q][q]
                theta = (aqq - app) / (2.0 * apq)
                t = (1.0 if theta >= 0 else -1.0) / (
                    abs(theta) + math.sqrt(theta * theta + 1.0)
                )
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = m[k][p], m[k][q]
                    m[k][p] = c * akp - s * akq
                    m[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = m[p][k], m[q][k]
                    m[p][k] = c * apk - s * aqk
                    m[q][k] = s * apk + c * aqk
    return sorted((m[i][i] for i in range(n)), reverse=True)


def hermitian_eigenvalues(rho: list[list[complex]]) -> list[float]:
    """Eigenvalues of a Hermitian matrix via the real symmetric embedding.

    For H = A + iB with A symmetric and B antisymmetric, the real symmetric
    block matrix [[A, -B], [B, A]] has every eigenvalue of H exactly twice.
    """
    n = len(rho)
    big = [[0.0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            re, im = rho[i][j].real, rho[i][j].imag
            big[i][j] = re
            big[i][j + n] = -im
            big[i + n][j] = im
            big[i + n][j + n] = re
    doubled = jacobi_eigenvalues(big)
    return [doubled[2 * i] for i in range(n)]


def von_neumann_entropy(rho: list[list[complex]]) -> float:
    """S(rho) in bits."""
    total = 0.0
    for lam in hermitian_eigenvalues(rho):
        if lam > 1e-12:
            total -= lam * math.log2(lam)
    return total


def subsystem_entropy(psi: list[complex], n_qubits: int, subset: list[int]) -> float:
    """S of a subsystem, always computed on the cheaper side (the state is pure)."""
    comp = [q for q in range(n_qubits) if q not in subset]
    target = subset if len(subset) <= len(comp) else comp
    if not target:
        return 0.0
    return von_neumann_entropy(reduced_density_matrix(psi, n_qubits, target))


# --------------------------------------------------------------------------
# experiment
# --------------------------------------------------------------------------

# Qubit layout: index 0 .. N_REF-1 is the reference R; the rest is the hole H.
REF = list(range(N_REF))
HOLE = list(range(N_REF, N_TOTAL))


def measure(psi: list[complex], n_released: int, n_hidden: int) -> dict:
    """Entropies and mutual informations for a given release/hide split."""
    rad = HOLE[:n_released]
    hid = HOLE[n_released : n_released + n_hidden]

    s_ref = subsystem_entropy(psi, N_TOTAL, REF)
    s_rad = subsystem_entropy(psi, N_TOTAL, rad) if rad else 0.0
    s_hid = subsystem_entropy(psi, N_TOTAL, hid) if hid else 0.0
    s_ref_rad = subsystem_entropy(psi, N_TOTAL, REF + rad)
    s_ref_hid = subsystem_entropy(psi, N_TOTAL, REF + hid)

    i_rad = s_ref + s_rad - s_ref_rad
    i_hid = s_ref + s_hid - s_ref_hid
    return {
        "S_ref": s_ref,
        "S_rad": s_rad,
        "S_hid": s_hid,
        "S_ref_rad": s_ref_rad,
        "S_ref_hid": s_ref_hid,
        "I_ref_rad": i_rad,
        "I_ref_hid": i_hid,
        "complementarity_sum": i_rad + i_hid,
        "complementarity_target": 2.0 * s_ref,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    states = [haar_state(1 << N_TOTAL, rng) for _ in range(N_SAMPLES)]

    # --- Page curve: full evaporation, nothing permanently hidden ---
    page_rows = []
    max_comp_violation = 0.0
    for t in range(N_HOLE + 1):
        acc: dict[str, float] = {}
        for psi in states:
            m = measure(psi, n_released=t, n_hidden=N_HOLE - t)
            for k, v in m.items():
                acc[k] = acc.get(k, 0.0) + v / N_SAMPLES
        max_comp_violation = max(
            max_comp_violation,
            abs(acc["complementarity_sum"] - acc["complementarity_target"]),
        )
        row = {"released_qubits": t}
        row.update({k: round(v, 8) for k, v in acc.items()})
        page_rows.append(row)

    # --- Remnant scan: r qubits permanently hidden, the rest released ---
    remnant_rows = []
    for r in range(N_HOLE + 1):
        released = N_HOLE - r
        acc = {}
        for psi in states:
            m = measure(psi, n_released=released, n_hidden=r)
            for k, v in m.items():
                acc[k] = acc.get(k, 0.0) + v / N_SAMPLES
        # Corollary F2 predicts decodability exactly while
        #   log dim hidden <= log dim boundary - S(X_R).
        predicted_admissible = r <= released - acc["S_ref"] + 1e-9
        row = {
            "hidden_qubits": r,
            "released_qubits": released,
            "predicted_admissible": int(predicted_admissible),
            "decodable_fraction": round(
                acc["I_ref_rad"] / acc["complementarity_target"], 6
            )
            if acc["complementarity_target"] > 0
            else float("nan"),
        }
        row.update({k: round(v, 8) for k, v in acc.items()})
        remnant_rows.append(row)

    with PAGE_CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(page_rows[0].keys()))
        w.writeheader()
        w.writerows(page_rows)
    with REMNANT_CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(remnant_rows[0].keys()))
        w.writeheader()
        w.writerows(remnant_rows)

    print(f"boundary decodability: R={N_REF} qubit(s), hole={N_HOLE} qubits, "
          f"{N_SAMPLES} Haar samples")
    print()
    print("Page curve (full evaporation)")
    print("  released   S(rad)   S(hid)  I(R;rad)  I(R;hid)      sum   2S(R)")
    for r_ in page_rows:
        print(
            f"  {r_['released_qubits']:>8}  {r_['S_rad']:>7.4f} {r_['S_hid']:>8.4f}"
            f" {r_['I_ref_rad']:>9.4f} {r_['I_ref_hid']:>9.4f}"
            f" {r_['complementarity_sum']:>8.4f} {r_['complementarity_target']:>7.4f}"
        )
    peak = max(page_rows, key=lambda x: x["S_rad"])
    print(f"  peak S(rad) = {peak['S_rad']:.4f} bits at {peak['released_qubits']}"
          f" released qubits (half of {N_TOTAL} total = {N_TOTAL/2:.1f})")
    print(f"  max complementarity violation: {max_comp_violation:.3e} bits")
    print()
    print("Remnant capacity scan")
    print("  hidden released  predicted   I(R;rad)  decodable_frac")
    for r_ in remnant_rows:
        print(
            f"  {r_['hidden_qubits']:>6} {r_['released_qubits']:>8}"
            f"  {'admissible' if r_['predicted_admissible'] else '  inadmis.'}"
            f"  {r_['I_ref_rad']:>9.4f}  {r_['decodable_fraction']:>13.4f}"
        )
    print()
    print(f"wrote {PAGE_CSV}")
    print(f"wrote {REMNANT_CSV}")


if __name__ == "__main__":
    main()
