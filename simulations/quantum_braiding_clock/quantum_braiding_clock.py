#!/usr/bin/env python3
"""Toy braided-clock simulation: a pulsed-monitored qubit that keeps its own time.

This is the first executable companion to
`bridges/quantum_braiding_timekeeping.md` (OP-22). It tests the braided
persistence conjecture on the smallest honest instrument: a single qubit whose
own weak-measurement records are simultaneously

1. its clock (burst records ring in phase with the internal precession),
2. its syndrome channel (the records reveal a hidden detuning-error sector:
   whether this qubit's clock runs fast or slow),
3. its feedback input (quadrature records drive a phase-locked-loop
   correction), and
4. its principal hazard (each burst dephases the protected logical
   component).

A methodological finding from the first, continuous-monitoring version of
this model is retained as a comment because it is itself an ACP-shaped
result: under CONTINUOUS weak z monitoring there is no productive overlap.
Transverse coherence dies like exp(-kappa^2 * steps / 2), while reading a
z-drift error against measurement backaction requires near-Zeno strength
(kappa^2 exceeding the per-step rotation angle); the two regimes do not
intersect. Moreover a constant z-drift under fast precession hides in the
y quadrature, invisible to a z monitor. The braid needs rhythm: monitoring
must be pulsed, paying the dephasing cost only at clock ticks. That pulsed
structure is exactly the release/record/feedback braid of the bridge note.

Model, in Bloch coordinates r = (x, y, z):

- Logical bit b: the sign of the x component (magnitude X0). Every
  Hamiltonian and feedback rotation in the model is about x, so the logical
  component is never rotated into the monitored plane: the controller is
  logically noncentral by construction (the Knill-Laflamme shape). Only
  measurement backaction shrinks x.
- Clock carrier: the y-z components precess about x. With initial (y, z) =
  (Y0, 0), the z population rings like Y0 * sin(omega_e t).
- Error sector e: a hidden detuning omega_e = OMEGA * (1 +/- DETUNING).
  The clock runs fast or slow; phase error accumulates.
- Escapement: twice per nominal period the qubit is weakly measured along z
  with strength kappa. The in-phase burst (nominal z maximum) reads the
  clock amplitude; the quadrature burst (nominal z zero crossing) reads the
  accumulated phase error, with record bias -kappa * Y * sin(phase error).
- Feedback: after each quadrature burst, an exponential moving average of
  the quadrature records drives a rotation about x by g * PHI0 * ema - an
  integrating phase-locked loop. (A single-bit bang-bang PLL was tried
  first; its phase diffusion per tick is too large to lock against
  tick-level record noise.)
- Relaxation: uniform transverse contraction toward z-axis mixedness at
  GAMMA per step.

Weak z measurement update (single-qubit Kraus pair, outcome s = +/-1):

    p(s) = (1 + s * kappa * z) / 2
    z'   = (z + s * kappa) / (1 + s * kappa * z)
    x'   = x * sqrt(1 - kappa^2) / (1 + s * kappa * z)   (same for y)

Diagnostics per (kappa, g) grid point, matching bridge section 9:

- clock_slack_bits: empirical Markov conditional entropy H(r_{n+1} | r_n)
  of the pooled burst-record stream. A locked strong clock has nearly
  deterministic in-phase records (crystallized, h -> 0); an unlocked weak
  clock has fair-coin records (dissolved, h -> 1 bit).
- slack_gate: 4 * h * (1 - h), the ACP-interval gate on record slack.
- memory_retention: mean terminal signed retention sb * x / X0, clipped at
  zero. The sign matters: amplitude pumped back into x with scrambled sign
  must not count as memory.
- error_info_bits: I(e ; sign of mean quadrature record), the syndrome
  content of the tick stream (does the record know which way the clock
  drifts?).
- logical_leak_bits: I(b ; sign of mean quadrature record | e). Expected to
  sit at the finite-sample floor, because no operation couples x into the
  monitored plane.
- phase_lock: mean in-phase record bias divided by its ideal locked value
  kappa * Y0, clipped to [0, 1] - does the clock still ring where it
  should?
- braid_score: memory_retention * error_info_bits * phase_lock
  * (1 - min(1, logical_leak_bits / 0.5)).

The slack gate is reported but deliberately NOT multiplied into the score:
individual weak-measurement ticks are intrinsically near-fair-coin, so the
raw Markov record entropy sits near the dissolution end of its axis across
most of the grid and only approaches the crystallized end for kappa -> 1,
where deterministic ticks and dead memory coincide. The two-boundary story
is visible in the reported h; forcing it into the product would only
penalize the entire interior for a property of binary tick encoding.

This is not a derivation. It is a diagnostic instrument for the conjecture
that collapse-like record formation is useful for persistence exactly in a
middle interval: enough ticking to keep time and read the error sector, not
so much that the escapement consumes the memory it serves.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
SCAN_CSV = OUT / "braiding_clock_scan.csv"
SUMMARY_CSV = OUT / "braiding_clock_summary.csv"
HEATMAP_PNG = OUT / "braiding_clock_heatmaps.png"
BUDGET_CSV = OUT / "braiding_clock_budget_scan.csv"
BUDGET_SUMMARY_CSV = OUT / "braiding_clock_budget_summary.csv"
BUDGET_PNG = OUT / "braiding_clock_budget_heatmaps.png"

SEED = 20260717

DT = 0.05
OMEGA = 1.0
PERIODS = 24
STEPS_PER_PERIOD = int(round(2.0 * math.pi / (OMEGA * DT)))  # 126
STEPS = PERIODS * STEPS_PER_PERIOD
N_TRAJ = 600
GAMMA = 0.0015
DETUNING = 0.04
X0 = 0.6
Y0 = 0.8
PHI0 = 0.30          # feedback phase scale per quadrature tick, radians
EMA_ALPHA = 0.15     # integration constant of the record-driven PLL
LATE_FRACTION = 0.5

# Burst offsets within each nominal period: z(t) = Y0 sin(OMEGA t), so the
# in-phase burst sits at the z maximum (quarter period) and the quadrature
# burst at the descending zero crossing (half period).
IN_PHASE_STEP = STEPS_PER_PERIOD // 4
QUADRATURE_STEP = STEPS_PER_PERIOD // 2

# --- Experiment B: tick rate versus tick strength at fixed dephasing ---
# Each burst multiplies transverse coherence by roughly sqrt(1 - kappa^2),
# so a run with N ticks at strength kappa spends a total dephasing budget
# B = -(N / 2) * ln(1 - kappa^2) (ideal logical retention exp(-B)). The
# budget scan holds B fixed, varies the tick rate (escapement fires every
# k-th period), and sets kappa = sqrt(1 - exp(-2 B / N)). The question:
# should a clock spend its decoherence budget on many weak ticks or a few
# strong ones?
BUDGET_GRID = np.round(np.array([0.35, 0.7, 1.05, 1.4, 2.1, 2.8]), 4)
EVERY_K_GRID = [1, 2, 3, 4, 6, 8, 12]
BUDGET_GAINS = [0.0, 1.65, 3.3]

# --- Experiment A grid ---
# Each burst multiplies transverse coherence by roughly sqrt(1 - kappa^2),
# so terminal logical retention is about (1 - kappa^2)^PERIODS. This grid
# straddles the crossover: the top rows read the error sector loudly but
# destroy the memory; the bottom rows preserve memory but cannot keep time.
KAPPA_GRID = np.round(np.linspace(0.05, 0.95, 12), 4)
GAIN_GRID = np.round(np.linspace(0.0, 3.3, 12), 4)


def binary_entropy(p: float) -> float:
    p = min(max(p, 1e-12), 1.0 - 1e-12)
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def binary_mi(joint: np.ndarray) -> float:
    """Mutual information in bits for a 2x2 empirical joint count table."""
    total = joint.sum()
    if total == 0:
        return 0.0
    pxy = joint / total
    px = pxy.sum(axis=1, keepdims=True)
    py = pxy.sum(axis=0, keepdims=True)
    mask = pxy > 0
    return float(np.sum(pxy[mask] * np.log2(pxy[mask] / (px @ py)[mask])))


def weak_measure_z(
    x: np.ndarray, y: np.ndarray, z: np.ndarray, kappa: float, rng: np.random.Generator
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    p_plus = (1.0 + kappa * z) / 2.0
    s = np.where(rng.random(z.shape[0]) < p_plus, 1.0, -1.0)
    denom = 1.0 + s * kappa * z
    shrink = math.sqrt(1.0 - kappa * kappa) / denom
    z_new = (z + s * kappa) / denom
    return x * shrink, y * shrink, z_new, s


def run_grid_point(
    kappa: float, gain: float, rng: np.random.Generator, every_k: int = 1
) -> dict:
    """Run one scan cell. `every_k` sets the tick rate: the two-burst
    escapement fires only on every k-th nominal period, so the number of
    measured periods is PERIODS // every_k."""
    n = N_TRAJ
    b = rng.integers(0, 2, size=n)          # logical bit -> sign of x
    e = rng.integers(0, 2, size=n)          # error sector -> clock fast/slow
    sb = np.where(b == 1, 1.0, -1.0)
    se = np.where(e == 1, 1.0, -1.0)

    omega_traj = OMEGA * (1.0 + se * DETUNING)
    theta = omega_traj * DT
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    contraction = 1.0 - GAMMA * DT

    x = sb * X0
    y = np.full(n, Y0)
    z = np.zeros(n)
    ema = np.zeros(n)

    in_phase_records: list[np.ndarray] = []
    quadrature_records: list[np.ndarray] = []

    for t in range(STEPS):
        # Prediction flow: detuned precession about x (z = Y0 sin convention).
        y, z = y * cos_t - z * sin_t, y * sin_t + z * cos_t
        y *= contraction
        z *= contraction

        period_index, step_in_period = divmod(t, STEPS_PER_PERIOD)
        if period_index % every_k != 0:
            continue
        if step_in_period == IN_PHASE_STEP:
            x, y, z, s = weak_measure_z(x, y, z, kappa, rng)
            in_phase_records.append(s)
        elif step_in_period == QUADRATURE_STEP:
            x, y, z, s = weak_measure_z(x, y, z, kappa, rng)
            quadrature_records.append(s)
            # Thread-back: integrating phase-locked-loop correction about x.
            # At the descending zero crossing the record bias is
            # -kappa * Y * sin(phase error), so advancing the phase by
            # g * PHI0 * ema pushes the phase error back toward zero.
            ema = (1.0 - EMA_ALPHA) * ema + EMA_ALPHA * s
            if gain > 0.0:
                phi = gain * PHI0 * ema
                cphi, sphi = np.cos(phi), np.sin(phi)
                y, z = y * cphi - z * sphi, y * sphi + z * cphi

    n_measured = len(in_phase_records)
    ticks_in = np.array(in_phase_records)        # (n_measured, n)
    ticks_quad = np.array(quadrature_records)    # (n_measured, n)

    # --- Clock slack: pooled Markov conditional entropy of the interleaved
    # burst-record stream (in-phase, quadrature, in-phase, ...). ---
    stream = np.empty((2 * n_measured, n))
    stream[0::2] = ticks_in
    stream[1::2] = ticks_quad
    prev = stream[:-1].ravel()
    nxt = stream[1:].ravel()
    h_cond = 0.0
    for value in (-1.0, 1.0):
        mask = prev == value
        if mask.sum() == 0:
            continue
        p_up = float((nxt[mask] == 1.0).mean())
        h_cond += mask.mean() * binary_entropy(p_up)
    slack_gate = 4.0 * h_cond * (1.0 - h_cond)

    # --- Memory retention: signed terminal logical coherence. ---
    memory_retention = max(0.0, float(np.mean(sb * x) / X0))

    # --- Syndrome and leakage from the quadrature record mean. When the
    # loop locks, the steady correction bias needed to cancel the detuning
    # is itself the syndrome; when unlocked, the sign of the drifting
    # quadrature bias carries it. Either way the full window is usable. ---
    late = ticks_quad.mean(axis=0)
    r_sign = (late > np.median(late)).astype(int)

    joint_e = np.zeros((2, 2))
    for ei in range(2):
        for ri in range(2):
            joint_e[ei, ri] = np.sum((e == ei) & (r_sign == ri))
    error_info = binary_mi(joint_e)

    leak = 0.0
    for ei in range(2):
        mask = e == ei
        if mask.sum() < 8:
            continue
        sub_b = b[mask]
        sub_r = (late[mask] > np.median(late[mask])).astype(int)
        joint_b = np.zeros((2, 2))
        for bi in range(2):
            for ri in range(2):
                joint_b[bi, ri] = np.sum((sub_b == bi) & (sub_r == ri))
        leak += mask.mean() * binary_mi(joint_b)

    # --- Clock quality: does the in-phase burst still ring? ---
    ideal_bias = kappa * Y0
    phase_lock = float(np.clip(ticks_in.mean() / ideal_bias, 0.0, 1.0))

    leak_penalty = 1.0 - min(1.0, leak / 0.5)
    braid_score = memory_retention * error_info * phase_lock * leak_penalty

    return {
        "kappa": round(kappa, 6),
        "gain": gain,
        "every_k": every_k,
        "n_ticks": 2 * n_measured,
        "clock_slack_bits": round(h_cond, 6),
        "slack_gate": round(slack_gate, 6),
        "memory_retention": round(memory_retention, 6),
        "error_info_bits": round(error_info, 6),
        "logical_leak_bits": round(leak, 6),
        "phase_lock": round(phase_lock, 6),
        "braid_score": round(braid_score, 6),
    }


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rng = np.random.default_rng(SEED)

    rows = []
    for kappa in KAPPA_GRID:
        for gain in GAIN_GRID:
            rows.append(run_grid_point(float(kappa), float(gain), rng))

    fieldnames = list(rows[0].keys())
    with SCAN_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    best = max(rows, key=lambda r: r["braid_score"])
    weakest = [r for r in rows if r["kappa"] == KAPPA_GRID[0]]
    strongest = [r for r in rows if r["kappa"] == KAPPA_GRID[-1]]
    zero_gain = [r for r in rows if r["gain"] == 0.0]
    max_gain = [r for r in rows if r["gain"] == GAIN_GRID[-1]]

    def mean_of(rows_, key):
        return round(float(np.mean([r[key] for r in rows_])), 6)

    summary = [
        ("grid_points", len(rows)),
        ("best_braid_score", best["braid_score"]),
        ("best_kappa", best["kappa"]),
        ("best_gain", best["gain"]),
        ("best_clock_slack_bits", best["clock_slack_bits"]),
        ("best_memory_retention", best["memory_retention"]),
        ("best_error_info_bits", best["error_info_bits"]),
        ("best_logical_leak_bits", best["logical_leak_bits"]),
        ("best_phase_lock", best["phase_lock"]),
        ("weak_monitor_mean_braid", mean_of(weakest, "braid_score")),
        ("weak_monitor_mean_error_info", mean_of(weakest, "error_info_bits")),
        ("strong_monitor_mean_braid", mean_of(strongest, "braid_score")),
        ("strong_monitor_mean_memory", mean_of(strongest, "memory_retention")),
        ("strong_monitor_mean_error_info", mean_of(strongest, "error_info_bits")),
        ("zero_gain_mean_phase_lock", mean_of(zero_gain, "phase_lock")),
        ("max_gain_mean_phase_lock", mean_of(max_gain, "phase_lock")),
        ("grid_mean_leak_bits", mean_of(rows, "logical_leak_bits")),
        ("grid_max_leak_bits", round(max(r["logical_leak_bits"] for r in rows), 6)),
    ]
    with SUMMARY_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["metric", "value"])
        writer.writerows(summary)

    plot_heatmaps(rows)

    print("braided clock scan complete")
    for key, value in summary:
        print(f"  {key}: {value}")

    run_budget_experiment(rng)


def run_budget_experiment(rng: np.random.Generator) -> None:
    """Experiment B: fixed dephasing budget, tick rate vs tick strength."""
    rows = []
    for budget in BUDGET_GRID:
        for every_k in EVERY_K_GRID:
            n_ticks = 2 * (PERIODS // every_k + (1 if PERIODS % every_k else 0))
            # kappa implied by spending the whole budget across n_ticks.
            inner = 1.0 - math.exp(-2.0 * budget / n_ticks)
            kappa = math.sqrt(inner)
            if kappa > 0.98:
                continue  # budget not spendable at this rate without kappa ~ 1
            for gain in BUDGET_GAINS:
                row = run_grid_point(float(kappa), float(gain), rng, every_k=every_k)
                row["budget"] = float(budget)
                rows.append(row)

    fieldnames = list(rows[0].keys())
    with BUDGET_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Best gain per (budget, rate) cell for the headline comparison.
    best_cells: dict[tuple[float, int], dict] = {}
    for row in rows:
        key = (row["budget"], row["every_k"])
        if key not in best_cells or row["braid_score"] > best_cells[key]["braid_score"]:
            best_cells[key] = row

    best = max(best_cells.values(), key=lambda r: r["braid_score"])
    fastest = [r for r in best_cells.values() if r["every_k"] == 1]
    slowest = [r for r in best_cells.values() if r["every_k"] == EVERY_K_GRID[-1]]

    def mean_of(rows_, key):
        return round(float(np.mean([r[key] for r in rows_])), 6)

    summary = [
        ("budget_cells", len(best_cells)),
        ("best_braid_score", best["braid_score"]),
        ("best_budget", best["budget"]),
        ("best_every_k", best["every_k"]),
        ("best_kappa", best["kappa"]),
        ("best_gain", best["gain"]),
        ("best_n_ticks", best["n_ticks"]),
        ("best_memory_retention", best["memory_retention"]),
        ("best_error_info_bits", best["error_info_bits"]),
        ("best_phase_lock", best["phase_lock"]),
        ("fastest_rate_mean_braid", mean_of(fastest, "braid_score")),
        ("slowest_rate_mean_braid", mean_of(slowest, "braid_score")),
        ("fastest_rate_mean_error_info", mean_of(fastest, "error_info_bits")),
        ("slowest_rate_mean_error_info", mean_of(slowest, "error_info_bits")),
        ("fastest_rate_mean_memory", mean_of(fastest, "memory_retention")),
        ("slowest_rate_mean_memory", mean_of(slowest, "memory_retention")),
        ("grid_max_leak_bits", round(max(r["logical_leak_bits"] for r in rows), 6)),
    ]
    with BUDGET_SUMMARY_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["metric", "value"])
        writer.writerows(summary)

    plot_budget_heatmaps(best_cells)

    print("budget (tick-rate vs tick-strength) scan complete")
    for key, value in summary:
        print(f"  {key}: {value}")


def plot_budget_heatmaps(best_cells: dict[tuple[float, int], dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    budgets = sorted({k[0] for k in best_cells})
    rates = sorted({k[1] for k in best_cells})
    panels = [
        ("braid_score", "braid score (best gain)"),
        ("memory_retention", "memory retention"),
        ("error_info_bits", "I(error; record) bits"),
        ("phase_lock", "phase lock"),
        ("kappa", "implied burst strength kappa"),
        ("clock_slack_bits", "H(r_{n+1} | r_n) bits"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8), constrained_layout=True)
    for ax, (key, title) in zip(axes.ravel(), panels):
        grid = np.full((len(budgets), len(rates)), np.nan)
        for (b, k), row in best_cells.items():
            grid[budgets.index(b), rates.index(k)] = row[key]
        im = ax.imshow(grid, origin="lower", aspect="auto", cmap="viridis")
        ax.set_xticks(range(len(rates)), [str(r) for r in rates])
        ax.set_yticks(range(len(budgets)), [f"{b:g}" for b in budgets])
        ax.set_xlabel("escapement fires every k-th period")
        ax.set_ylabel("dephasing budget B")
        ax.set_title(title)
        fig.colorbar(im, ax=ax, shrink=0.85)
    fig.suptitle("Braided clock: tick rate vs tick strength at fixed dephasing budget")
    fig.savefig(BUDGET_PNG, dpi=130)
    plt.close(fig)


def plot_heatmaps(rows: list[dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    nk, ng = len(KAPPA_GRID), len(GAIN_GRID)
    panels = [
        ("braid_score", "braid score"),
        ("memory_retention", "memory retention"),
        ("error_info_bits", "I(error; record) bits"),
        ("logical_leak_bits", "I(logical; record | error) bits"),
        ("clock_slack_bits", "H(r_{n+1} | r_n) bits"),
        ("phase_lock", "phase lock"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8), constrained_layout=True)
    for ax, (key, title) in zip(axes.ravel(), panels):
        grid = np.array([r[key] for r in rows]).reshape(nk, ng)
        im = ax.imshow(
            grid,
            origin="lower",
            aspect="auto",
            extent=[GAIN_GRID[0], GAIN_GRID[-1], KAPPA_GRID[0], KAPPA_GRID[-1]],
            cmap="viridis",
        )
        ax.set_title(title)
        ax.set_xlabel("feedback gain g")
        ax.set_ylabel("burst measurement strength kappa")
        fig.colorbar(im, ax=ax, shrink=0.85)
    fig.suptitle("Braided quantum clock: pulsed-monitored qubit with PLL feedback")
    fig.savefig(HEATMAP_PNG, dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    main()
