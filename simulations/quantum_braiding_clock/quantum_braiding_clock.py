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
OPTIME_CSV = OUT / "braiding_clock_optime_scan.csv"
OPTIME_SUMMARY_CSV = OUT / "braiding_clock_optime_summary.csv"
OPTIME_PNG = OUT / "braiding_clock_optime_curves.png"
CODE_CSV = OUT / "braiding_clock_code_scan.csv"
CODE_SUMMARY_CSV = OUT / "braiding_clock_code_summary.csv"
CODE_PNG = OUT / "braiding_clock_code_curves.png"
STAB_CSV = OUT / "braiding_clock_stabilizer_scan.csv"
STAB_SUMMARY_CSV = OUT / "braiding_clock_stabilizer_summary.csv"
STAB_PNG = OUT / "braiding_clock_stabilizer_curves.png"
CONT_CSV = OUT / "braiding_clock_continuity_scan.csv"
CONT_PNG = OUT / "braiding_clock_continuity_curves.png"

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

# --- Experiment C: operational-time covariance probe (OP-29) ---
# A family of clocks with IDENTICAL operational length (same tick count,
# same per-tick strength, same per-tick feedback) but different lab-time
# tempos: the escapement fires every k-th period, and the run is stretched
# to k * OPTIME_MEASURED_PERIODS nominal periods so every member executes
# the same number of verification steps. The tempo map between members is
# linear in lab time and the identity in tick time. Per the OP-29 candidate
# transformation laws, tick-native scalars should be invariant across k
# exactly when the disturbance kernel commutes with the tempo map:
#   - co_clocked mode: detuning scaled by 1/k, so the phase error accrued
#     between consecutive ticks is the same for every member - the per-tick
#     transition kernels match (operational conjugacy) and ALL diagnostics
#     should collapse onto one point.
#   - lab_clocked mode: fixed detuning in lab time, so slower-ticking
#     members accrue k times the phase error per verification step - the
#     kernels do not match, conjugacy fails, and record-facing quantities
#     (error information, phase lock) should fan out with k while the
#     purely tick-native measurement cost (memory retention) stays flat.
# GAMMA is set to zero here so the detuning is the only lab-clocked process.
OPTIME_MEASURED_PERIODS = 16
OPTIME_K_LIST = [1, 2, 3, 4, 6]
OPTIME_KAPPA = 0.21
OPTIME_GAIN = 3.3

# --- Experiment D: clocked repetition code (OP-23 small-code rung) ---
# Three braided-clock qubits carry the same logical bit (sign of each x
# component) and share one clock (common detuning sector, common PLL drive).
# The channel adds phase flips: each period each qubit independently flips
# (x, y) -> (-x, -y) with probability p_flip.
#
# Syndrome channel. A first version tried to decode flips from the weak
# tick records alone (a flipped qubit's clock carrier inverts, so it ticks
# upside-down). That fails structurally, and the failure is worth keeping:
# a z-tick statistic with flip-identification SNR S costs exp(-S^2 / 2) of
# the logical coherence it is protecting, so tick records gentle enough to
# preserve memory are too dilute to decode flips within a run. This is
# precisely why codes exist. A phase-flip code measures X(i)X(j) parity
# STRONGLY at zero logical cost, because the parity operator commutes with
# the logical algebra - the Knill-Laflamme condition in its cheapest form.
# Experiment D therefore adds a dedicated parity record channel: per
# in-phase tick, each qubit pair emits a binary record with bias
# PARITY_KAPPA * sign(x_i x_j), noisy in readout but free of x backaction.
#
# Honesty note: this is a product-state Bloch scaffold, not an entangled
# stabilizer code; the parity records are classical comparisons standing in
# for collective stabilizer measurements, and their zero-backaction status
# is imported from the Knill-Laflamme argument, not derived here. This is
# the D0 rung of a small-code ladder: it tests the control architecture
# (clock and syndrome records kept separate by commutation, noncentral
# common-mode feedback, evidence-gated correction) rather than genuine
# stabilizer protection. The OP-23 acceptance discipline still applies: the
# checked code must beat bare and unchecked baselines on the same logical
# readout, and the overactive policy must be visibly worse.
CODE_PERIODS = 36
CODE_KAPPA = 0.18
CODE_GAIN = 3.3
PARITY_KAPPA = 0.6       # readout fidelity of the pair parity records
CODE_EMA_ALPHA = 0.30    # parity-record EMA (syndrome evidence)
CODE_THRESHOLD = 0.25    # evidence gate for the checked decoder
CODE_PFLIP_GRID = [0.0, 0.005, 0.01, 0.02, 0.04, 0.08]
CODE_POLICIES = ["bare", "code_unchecked", "code_checked", "code_overactive"]

# --- Experiment E: entangled stabilizer code (OP-23 D1 rung) ---
# The state-vector upgrade of Experiment D. Three qubits in the phase-flip
# code |0_L> = |+++>, |1_L> = |--->, protected information stored as a
# genuine quantum coherence: the logical-Y eigenstate
# (|0_L> + i*sb |1_L>)/sqrt(2). The channel applies Z_i phase flips per
# period. The syndrome is read by WEAK measurements of the stabilizers
# X1X2 and X2X3 implemented as proper Kraus pairs
#   M(s) = sqrt((1 + s*kappa)/2) P_+ + sqrt((1 - s*kappa)/2) P_-,
# so the parity channel's zero logical cost is DERIVED, not imported:
# because Z errors map stabilizer eigenstates to stabilizer eigenstates,
# the state is always an eigenstate of the measured operator, the Kraus
# update is proportional to the identity on it, and the backaction
# vanishes identically while the record stays noisy (readout fidelity
# STAB_KAPPA < 1). The control comparison `bare_monitored` probes a single
# unencoded qubit at the same strength with a weak X measurement, which
# anticommutes with the stored Y coherence: same measurement budget, total
# decoherence. The commutation structure - not the gentleness of the
# probe - is what makes syndrome extraction free.
STAB_PERIODS = 36
STAB_KAPPA = 0.6         # readout fidelity of weak stabilizer measurements
STAB_EMA_ALPHA = 0.20
STAB_THRESHOLD = 0.35
STAB_WARMUP = 5          # periods of EMA burn-in before the decoder may fire
STAB_PFLIP_GRID = [0.0, 0.005, 0.01, 0.02, 0.04, 0.08]
STAB_POLICIES = [
    "bare",
    "bare_monitored",
    "code_unchecked",
    "code_checked",
    "code_overactive",
]

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
    kappa: float,
    gain: float,
    rng: np.random.Generator,
    every_k: int = 1,
    periods: int = PERIODS,
    detuning: float = DETUNING,
    gamma: float = GAMMA,
) -> dict:
    """Run one scan cell. `every_k` sets the tick rate: the two-burst
    escapement fires only on every k-th nominal period. `periods`,
    `detuning`, and `gamma` are overridable for the operational-time
    covariance probe (Experiment C)."""
    n = N_TRAJ
    b = rng.integers(0, 2, size=n)          # logical bit -> sign of x
    e = rng.integers(0, 2, size=n)          # error sector -> clock fast/slow
    sb = np.where(b == 1, 1.0, -1.0)
    se = np.where(e == 1, 1.0, -1.0)

    omega_traj = OMEGA * (1.0 + se * detuning)
    theta = omega_traj * DT
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    contraction = 1.0 - gamma * DT
    steps = periods * STEPS_PER_PERIOD

    x = sb * X0
    y = np.full(n, Y0)
    z = np.zeros(n)
    ema = np.zeros(n)

    in_phase_records: list[np.ndarray] = []
    quadrature_records: list[np.ndarray] = []

    for t in range(steps):
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
    run_optime_experiment(rng)
    run_code_experiment(rng)
    run_stabilizer_experiment(rng)
    run_continuity_experiment()


def run_continuity_experiment() -> None:
    """Experiment F: exact verification of the Proposition 5 continuity
    bound (bridges/clock_syndrome_record_splitting.md).

    Two epsilon-transparent instruments are tested, both weak measurements
    at strength STAB_KAPPA of a deformed stabilizer, both with commutator
    defect epsilon = O(mu) against the logical clock generator
    X-bar = X1X2X3:

    - `conjugated`: measure V S1 V-dagger with V = exp(-i mu Z1 / 2), a
      miscalibrated readout axis obtained by rotating the whole apparatus.
      Numerically this instrument turns out to be EXACTLY clock-blind for
      every mu and every sequence length, even though its commutator
      defect is nonzero. The reason is algebraic: repeated QND measurement
      of one fixed observable A generates an abelian Kraus algebra
      (all products lie in span{I, A}), and P A P is proportional to P, so
      every record POVM element compresses to a scalar on the code sector.
      The Proposition 5 bound is therefore satisfied but infinitely loose
      here - evidence that the right defect measure is algebraic, not
      merely a commutator norm (recorded in OP-30).
    - `axis_leak`: measure B = cos(mu) S1 + sin(mu) Z-bar, a readout axis
      contaminated by a logical observable (crosstalk-style). This one
      genuinely reads the clock, with I(Theta;R) scaling like mu^2, and
      the Proposition 5 bound must and does hold nontrivially.

    Everything is computed exactly with 8x8 matrices and full
    record-branch enumeration - no Monte Carlo.
    """
    # Pauli matrices and 3-qubit operators, qubit 1 = leftmost factor.
    I2 = np.eye(2)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)

    def kron3(a, b, c):
        return np.kron(np.kron(a, b), c)

    S1 = kron3(sx, sx, I2)                 # stabilizer X1X2
    Z1 = kron3(sz, I2, I2)
    XL = kron3(sx, sx, sx)                 # logical clock generator X-bar
    v0 = _V0.astype(complex)
    v1 = _V1.astype(complex)
    P = np.outer(v0, v0.conj()) + np.outer(v1, v1.conj())
    psi0 = (v0 + 1j * v1) / math.sqrt(2.0)  # logical-Y eigenstate

    kappa = STAB_KAPPA
    n_seq = 8
    theta_grid = [2.0 * math.pi * t / 16 for t in range(16)]

    def u_theta(theta):
        return math.cos(theta / 2) * np.eye(8) - 1j * math.sin(theta / 2) * XL

    ZL = kron3(sz, sz, sz)                 # logical Z-bar

    def kraus_pair(mu, kind):
        if kind == "conjugated":
            v = math.cos(mu / 2) * np.eye(8) - 1j * math.sin(mu / 2) * Z1
            observable = v @ S1 @ v.conj().T
        else:  # axis_leak
            observable = math.cos(mu) * S1 + math.sin(mu) * ZL
        # Weak measurement Kraus pair M_s = sqrt((I + s*kappa*B)/2). For an
        # involution B this reduces to the projector form used elsewhere;
        # for the axis-leak observable it correctly retains the logical
        # tilt (a sign-projector construction would silently discard it,
        # because S1 and Z-bar commute and sign(B) = S1 for mu < pi/4).
        evals, evecs = np.linalg.eigh(observable)
        return [
            evecs
            @ np.diag(np.sqrt((1.0 + s * kappa * evals) / 2.0))
            @ evecs.conj().T
            for s in (+1, -1)
        ]

    def h2(p):
        p = min(max(p, 1e-15), 1 - 1e-15)
        return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))

    def mutual_information(mu, n, kind):
        kraus = kraus_pair(mu, kind)
        dists = []
        for theta in theta_grid:
            branches = [(u_theta(theta) @ psi0, 1.0)]
            for _ in range(n):
                new = []
                for phi, w in branches:
                    for M in kraus:
                        chi = M @ phi
                        pr = float(np.real(np.vdot(chi, chi)))
                        if pr * w > 1e-15:
                            new.append((chi / math.sqrt(pr), w * pr))
                        else:
                            new.append((chi, 0.0))
                branches = new
            dists.append(np.array([w for _, w in branches]))
        dists = np.array(dists)                      # (16, 2^n)
        marginal = dists.mean(axis=0)
        mi = 0.0
        for row in dists:
            mask = row > 0
            mi += np.sum(row[mask] * np.log2(row[mask] / marginal[mask]))
        return mi / len(theta_grid)

    def defect(mu, kind):
        kraus = kraus_pair(mu, kind)
        eps_sq = 0.0
        for M in kraus:
            worst = 0.0
            for theta in theta_grid:
                U = u_theta(theta)
                D = (M @ U - U @ M) @ P
                worst = max(worst, float(np.linalg.norm(D @ P, ord=2)))
            eps_sq += worst**2
        return math.sqrt(eps_sq)

    rows = []
    for kind in ("conjugated", "axis_leak"):
        for mu in (0.0, 0.05, 0.1, 0.2, 0.4):
            eps = defect(mu, kind)
            for n in (1, n_seq):
                tau = n * (eps + eps**2 / 2.0)
                bound = (
                    2.0 * tau * n * 1.0 + h2(min(2.0 * tau, 0.5))
                    if 2.0 * tau <= 0.5
                    else float("inf")
                )
                bound = min(bound, 4.0)  # H(Theta) = log2 16 trivial cap
                mi = mutual_information(mu, n, kind)
                rows.append(
                    {
                        "instrument": kind,
                        "mu": mu,
                        "n_measurements": n,
                        "epsilon": round(eps, 6),
                        "clock_info_bits": round(max(mi, 0.0), 8),
                        "prop5_bound_bits": round(bound, 6)
                        if bound != float("inf")
                        else "inf",
                        "bound_satisfied": bool(
                            bound == float("inf") or mi <= bound + 1e-9
                        ),
                    }
                )

    with CONT_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    plot_continuity(rows)

    print("continuity bound verification complete")
    for r in rows:
        print(
            f"  {r['instrument']:<11} mu={r['mu']:<5} n={r['n_measurements']} "
            f"eps={r['epsilon']:<9} I={r['clock_info_bits']:<12} "
            f"bound={r['prop5_bound_bits']} ok={r['bound_satisfied']}"
        )


def plot_continuity(rows: list[dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7.5, 5), constrained_layout=True)
    for n, marker in ((1, "o"), (8, "s")):
        sel = [
            r
            for r in rows
            if r["instrument"] == "axis_leak"
            and r["n_measurements"] == n
            and r["mu"] > 0
        ]
        mus = [r["mu"] for r in sel]
        mis = [max(r["clock_info_bits"], 1e-12) for r in sel]
        ax.loglog(mus, mis, marker=marker, label=f"axis_leak I(Theta;R), n={n}")
        finite = [
            (r["mu"], r["prop5_bound_bits"])
            for r in sel
            if r["prop5_bound_bits"] != "inf"
        ]
        if finite:
            ax.loglog(
                [m for m, _ in finite],
                [b for _, b in finite],
                marker=marker,
                linestyle="--",
                label=f"Prop. 5 bound, n={n}",
            )
    ref = np.array([0.05, 0.4])
    ax.loglog(ref, 0.5 * ref**2, ":", color="gray", label="mu^2 reference")
    ax.set_xlabel("miscalibration angle mu")
    ax.set_ylabel("bits")
    ax.set_title("Continuity of clock-blindness: exact I vs Proposition 5 bound")
    ax.grid(alpha=0.3, which="both")
    ax.legend()
    fig.savefig(CONT_PNG, dpi=130)
    plt.close(fig)


# Basis convention for Experiment E: index bits (b1 b2 b3), qubit 1 = MSB.
# X1X2 permutes index by XOR 0b110; X2X3 by XOR 0b011. Z_i puts a sign
# (-1)^(bit i). Codewords: |0_L> = |+++>, |1_L> = |--->.
_V0 = np.ones(8) / math.sqrt(8.0)
_V1 = np.array([(-1) ** bin(i).count("1") for i in range(8)]) / math.sqrt(8.0)
_S_PERMS = {1: np.arange(8) ^ 6, 2: np.arange(8) ^ 3}
_Z_SIGNS = {
    1: np.array([(-1) ** ((i >> 2) & 1) for i in range(8)], dtype=float),
    2: np.array([(-1) ** ((i >> 1) & 1) for i in range(8)], dtype=float),
    3: np.array([(-1) ** (i & 1) for i in range(8)], dtype=float),
}
# Syndrome (s1, s2) -> corrective Z. Z1 flips S1 only; Z2 flips both;
# Z3 flips S2 only.
_SYNDROME_TO_Z = {(-1, 1): 1, (-1, -1): 2, (1, -1): 3}


def _weak_stabilizer_measure(
    psi: np.ndarray, perm: np.ndarray, kappa: float, rng: np.random.Generator
) -> tuple[np.ndarray, np.ndarray]:
    """Weak measurement of a stabilizer S (S^2 = I) given its permutation.

    Returns (updated psi, outcome record in {-1, +1} per trajectory).
    """
    phi_plus = (psi + psi[:, perm]) / 2.0
    phi_minus = (psi - psi[:, perm]) / 2.0
    expect_s = np.sum(np.abs(phi_plus) ** 2 - np.abs(phi_minus) ** 2, axis=1)
    p_plus = (1.0 + kappa * expect_s) / 2.0
    s = np.where(rng.random(psi.shape[0]) < p_plus, 1.0, -1.0)
    w_plus = np.sqrt((1.0 + s * kappa) / 2.0)[:, None]
    w_minus = np.sqrt((1.0 - s * kappa) / 2.0)[:, None]
    psi_new = w_plus * phi_plus + w_minus * phi_minus
    norm = np.linalg.norm(psi_new, axis=1, keepdims=True)
    return psi_new / norm, s


def _logical_y(psi: np.ndarray, sb: np.ndarray) -> np.ndarray:
    alpha = psi @ _V0
    beta = psi @ _V1
    return sb * 2.0 * np.imag(np.conj(alpha) * beta)


def run_stabilizer_point(
    p_flip: float, policy: str, rng: np.random.Generator
) -> dict:
    """One cell of Experiment E: the entangled stabilizer code."""
    n = N_TRAJ
    b = rng.integers(0, 2, size=n)
    sb = np.where(b == 1, 1.0, -1.0)

    if policy.startswith("bare"):
        # Single qubit, logical-Y eigenstate (|0> + i*sb |1>)/sqrt(2).
        psi = np.stack(
            [np.full(n, 1.0 + 0.0j), 1j * sb.astype(complex)], axis=1
        ) / math.sqrt(2.0)
    else:
        psi = (
            _V0[None, :].astype(complex)
            + 1j * sb[:, None] * _V1[None, :]
        ) / math.sqrt(2.0)

    ema = np.zeros((2, n))
    corrections = np.zeros(n)
    x_perm_1q = np.array([1, 0])

    for _period in range(STAB_PERIODS):
        # Error channel: independent Z phase flips.
        if p_flip > 0.0:
            if policy.startswith("bare"):
                flip = rng.random(n) < p_flip
                psi[flip, 1] *= -1.0
            else:
                for q in (1, 2, 3):
                    flip = rng.random(n) < p_flip
                    psi[flip] *= _Z_SIGNS[q][None, :]

        if policy == "bare_monitored":
            # Same-strength weak X measurement on the bare qubit. X
            # anticommutes with the stored Y coherence, so this probe
            # decoheres exactly what it is trying to protect.
            psi, _ = _weak_stabilizer_measure(psi, x_perm_1q, STAB_KAPPA, rng)
        elif policy in ("code_checked", "code_overactive"):
            latest = np.empty((2, n))
            for si, stab in enumerate((1, 2)):
                psi, s = _weak_stabilizer_measure(
                    psi, _S_PERMS[stab], STAB_KAPPA, rng
                )
                latest[si] = s
                ema[si] = (1.0 - STAB_EMA_ALPHA) * ema[si] + STAB_EMA_ALPHA * s
            if policy == "code_checked":
                if _period < STAB_WARMUP:
                    continue
                evidence, gate = ema, STAB_THRESHOLD
            else:
                evidence, gate = latest, 0.5
            # The table lists the stabilizer pattern produced by Z_q; the
            # decoder fires when the evidence matches it beyond the gate.
            for (s1, s2), q in _SYNDROME_TO_Z.items():
                hit = (evidence[0] * s1 > gate) & (evidence[1] * s2 > gate)
                if not hit.any():
                    continue
                psi[hit] *= _Z_SIGNS[q][None, :]
                ema[0][hit] = 0.0
                ema[1][hit] = 0.0
                corrections[hit] += 1

    # Terminal ideal decode for all code policies: projective stabilizer
    # readout (states are exact eigenstates under this error model, so the
    # expectation values are +/-1) followed by the table correction.
    if not policy.startswith("bare"):
        s_vals = []
        for stab in (1, 2):
            perm = _S_PERMS[stab]
            phi_plus = (psi + psi[:, perm]) / 2.0
            phi_minus = (psi - psi[:, perm]) / 2.0
            s_vals.append(
                np.where(
                    np.sum(np.abs(phi_plus) ** 2, axis=1)
                    >= np.sum(np.abs(phi_minus) ** 2, axis=1),
                    1,
                    -1,
                )
            )
        for (s1, s2), q in _SYNDROME_TO_Z.items():
            hit = (s_vals[0] == s1) & (s_vals[1] == s2)
            if hit.any():
                psi[hit] *= _Z_SIGNS[q][None, :]

    if policy.startswith("bare"):
        retention = max(
            0.0,
            float(np.mean(sb * 2.0 * np.imag(np.conj(psi[:, 0]) * psi[:, 1]))),
        )
    else:
        retention = max(0.0, float(np.mean(_logical_y(psi, sb))))

    return {
        "p_flip": p_flip,
        "policy": policy,
        "logical_retention": round(retention, 6),
        "mean_corrections": round(float(corrections.mean()), 6),
    }


def run_stabilizer_experiment(rng: np.random.Generator) -> None:
    """Experiment E: entangled stabilizer code (OP-23 D1 rung)."""
    rows = [
        run_stabilizer_point(p, policy, rng)
        for p in STAB_PFLIP_GRID
        for policy in STAB_POLICIES
    ]

    with STAB_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    def get(p, policy, key="logical_retention"):
        return next(
            r[key] for r in rows if r["p_flip"] == p and r["policy"] == policy
        )

    summary = [
        ("pflip_grid", " ".join(str(p) for p in STAB_PFLIP_GRID)),
        ("zero_noise_checked_retention", get(0.0, "code_checked")),
        ("zero_noise_bare_monitored_retention", get(0.0, "bare_monitored")),
        ("zero_noise_bare_retention", get(0.0, "bare")),
        ("mid_noise_bare_retention", get(0.02, "bare")),
        ("mid_noise_unchecked_retention", get(0.02, "code_unchecked")),
        ("mid_noise_checked_retention", get(0.02, "code_checked")),
        ("mid_noise_overactive_retention", get(0.02, "code_overactive")),
        ("high_noise_checked_retention", get(0.08, "code_checked")),
        ("mid_noise_checked_corrections", get(0.02, "code_checked", "mean_corrections")),
        ("mid_noise_overactive_corrections", get(0.02, "code_overactive", "mean_corrections")),
    ]
    with STAB_SUMMARY_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["metric", "value"])
        writer.writerows(summary)

    plot_stabilizer_curves(rows)

    print("entangled stabilizer code scan complete")
    for key, value in summary:
        print(f"  {key}: {value}")


def plot_stabilizer_curves(rows: list[dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7.5, 5), constrained_layout=True)
    for policy, marker in zip(STAB_POLICIES, "osd^v"):
        ps = [r["p_flip"] for r in rows if r["policy"] == policy]
        vals = [r["logical_retention"] for r in rows if r["policy"] == policy]
        ax.plot(ps, vals, marker=marker, label=policy)
    ax.set_xlabel("phase-flip probability per qubit per period")
    ax.set_ylabel("logical-Y retention")
    ax.set_title(
        "Entangled stabilizer code: syndrome extraction is free by commutation"
    )
    ax.grid(alpha=0.3)
    ax.legend()
    fig.savefig(STAB_PNG, dpi=130)
    plt.close(fig)


def run_code_point(p_flip: float, policy: str, rng: np.random.Generator) -> dict:
    """One cell of Experiment D: the clocked repetition code."""
    n = N_TRAJ
    nq = 1 if policy == "bare" else 3
    b = rng.integers(0, 2, size=n)
    e = rng.integers(0, 2, size=n)
    sb = np.where(b == 1, 1.0, -1.0)
    se = np.where(e == 1, 1.0, -1.0)

    theta = OMEGA * (1.0 + se * DETUNING) * DT
    cos_t, sin_t = np.cos(theta), np.sin(theta)

    PAIRS = [(0, 1), (1, 2), (0, 2)]
    x = np.tile((sb * X0)[None, :], (nq, 1))
    y = np.full((nq, n), Y0)
    z = np.zeros((nq, n))
    pm = np.zeros((3, n))            # pair parity-record EMAs (syndrome)
    ema_c = np.zeros(n)              # common-mode quadrature EMA (PLL)
    corrections = np.zeros(n)
    first_flip = np.zeros(n, dtype=int)   # 0 = none, 1..nq = first flipped qubit
    quad_common: list[np.ndarray] = []

    steps = CODE_PERIODS * STEPS_PER_PERIOD
    for t in range(steps):
        y, z = y * cos_t - z * sin_t, y * sin_t + z * cos_t

        step_in_period = t % STEPS_PER_PERIOD
        if step_in_period == 0 and p_flip > 0.0:
            flips = rng.random((nq, n)) < p_flip
            sign = np.where(flips, -1.0, 1.0)
            x *= sign
            y *= sign
            for q in range(nq):
                newly = flips[q] & (first_flip == 0)
                first_flip[newly] = q + 1

        if step_in_period == IN_PHASE_STEP:
            for q in range(nq):
                x[q], y[q], z[q], _ = weak_measure_z(x[q], y[q], z[q], CODE_KAPPA, rng)
            if nq == 3:
                # Parity record channel: binary readout of sign(x_i x_j),
                # noisy at PARITY_KAPPA, no x backaction (KL-justified).
                latest_p = np.empty((3, n))
                for pi, (i, j) in enumerate(PAIRS):
                    bias = PARITY_KAPPA * np.sign(x[i] * x[j])
                    r = np.where(rng.random(n) < (1.0 + bias) / 2.0, 1.0, -1.0)
                    latest_p[pi] = r
                    pm[pi] = (1.0 - CODE_EMA_ALPHA) * pm[pi] + CODE_EMA_ALPHA * r
                if policy == "code_checked":
                    evidence, gate = pm, CODE_THRESHOLD
                elif policy == "code_overactive":
                    evidence, gate = latest_p, 0.5
                else:
                    evidence = None
                if evidence is not None:
                    for q in range(3):
                        own = [pi for pi, pr in enumerate(PAIRS) if q in pr]
                        other = next(
                            pi for pi, pr in enumerate(PAIRS) if q not in pr
                        )
                        hit = (
                            (evidence[own[0]] < -gate)
                            & (evidence[own[1]] < -gate)
                            & (evidence[other] > gate)
                        )
                        if not hit.any():
                            continue
                        x[q][hit] *= -1.0
                        y[q][hit] *= -1.0
                        pm[own[0]][hit] = 0.0
                        pm[own[1]][hit] = 0.0
                        corrections[hit] += 1
        elif step_in_period == QUADRATURE_STEP:
            s_sum = np.zeros(n)
            for q in range(nq):
                x[q], y[q], z[q], s = weak_measure_z(x[q], y[q], z[q], CODE_KAPPA, rng)
                s_sum += s
            s_common = s_sum / nq
            quad_common.append(s_common)
            ema_c = (1.0 - EMA_ALPHA) * ema_c + EMA_ALPHA * s_common
            phi = CODE_GAIN * PHI0 * ema_c
            cphi, sphi = np.cos(phi), np.sin(phi)
            y, z = y * cphi - z * sphi, y * sphi + z * cphi

    # --- Logical readout: median over the block (majority for sign,
    # amplitude-honest), assumed ideal. ---
    x_logical = x[0] if nq == 1 else np.median(x, axis=0)
    retention = max(0.0, float(np.mean(sb * x_logical) / X0))
    sign_fidelity = float(np.mean(np.sign(x_logical) == sb))

    # --- Syndrome decode audit: first flipped qubit vs terminal parity
    # verdict (which qubit, if any, the pair EMAs currently implicate). ---
    if nq == 3:
        inferred = np.zeros(n, dtype=int)
        for q in range(3):
            own = [pi for pi, pr in enumerate(PAIRS) if q in pr]
            other = next(pi for pi, pr in enumerate(PAIRS) if q not in pr)
            hit = (
                (pm[own[0]] < 0) & (pm[own[1]] < 0) & (pm[other] > 0)
            )
            inferred[hit] = q + 1
        joint = np.zeros((4, 4))
        for a in range(4):
            for c in range(4):
                joint[a, c] = np.sum((first_flip == a) & (inferred == c))
        flip_id_mi = binary_mi(joint)
    else:
        flip_id_mi = 0.0

    # --- Leak audit on the common-mode quadrature record. ---
    late = np.array(quad_common).mean(axis=0)
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

    return {
        "p_flip": p_flip,
        "policy": policy,
        "logical_retention": round(retention, 6),
        "sign_fidelity": round(sign_fidelity, 6),
        "flip_id_mi_bits": round(flip_id_mi, 6),
        "logical_leak_bits": round(leak, 6),
        "mean_corrections": round(float(corrections.mean()), 6),
    }


def run_code_experiment(rng: np.random.Generator) -> None:
    """Experiment D: the clocked repetition code (OP-23 D0 rung)."""
    rows = [
        run_code_point(p, policy, rng)
        for p in CODE_PFLIP_GRID
        for policy in CODE_POLICIES
    ]

    with CODE_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    def get(p, policy, key):
        return next(
            r[key] for r in rows if r["p_flip"] == p and r["policy"] == policy
        )

    mid = 0.02
    summary = [
        ("pflip_grid", " ".join(str(p) for p in CODE_PFLIP_GRID)),
        ("zero_noise_bare_retention", get(0.0, "bare", "logical_retention")),
        ("zero_noise_checked_retention", get(0.0, "code_checked", "logical_retention")),
        ("mid_noise_bare_retention", get(mid, "bare", "logical_retention")),
        ("mid_noise_unchecked_retention", get(mid, "code_unchecked", "logical_retention")),
        ("mid_noise_checked_retention", get(mid, "code_checked", "logical_retention")),
        ("mid_noise_overactive_retention", get(mid, "code_overactive", "logical_retention")),
        ("mid_noise_checked_sign_fidelity", get(mid, "code_checked", "sign_fidelity")),
        ("mid_noise_bare_sign_fidelity", get(mid, "bare", "sign_fidelity")),
        ("mid_noise_checked_flip_id_mi", get(mid, "code_checked", "flip_id_mi_bits")),
        ("mid_noise_checked_corrections", get(mid, "code_checked", "mean_corrections")),
        ("mid_noise_overactive_corrections", get(mid, "code_overactive", "mean_corrections")),
        ("grid_max_leak_bits", round(max(r["logical_leak_bits"] for r in rows), 6)),
    ]
    with CODE_SUMMARY_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["metric", "value"])
        writer.writerows(summary)

    plot_code_curves(rows)

    print("clocked repetition code scan complete")
    for key, value in summary:
        print(f"  {key}: {value}")


def plot_code_curves(rows: list[dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    panels = [
        ("logical_retention", "signed logical retention"),
        ("sign_fidelity", "logical sign fidelity"),
        ("flip_id_mi_bits", "I(first flip; decoder verdict) bits"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(14, 4), constrained_layout=True)
    for ax, (key, title) in zip(axes, panels):
        for policy, marker in zip(CODE_POLICIES, "osd^"):
            ps = [r["p_flip"] for r in rows if r["policy"] == policy]
            vals = [r[key] for r in rows if r["policy"] == policy]
            ax.plot(ps, vals, marker=marker, label=policy)
        ax.set_xlabel("phase-flip probability per qubit per period")
        ax.set_title(title)
        ax.grid(alpha=0.3)
    axes[0].legend()
    fig.suptitle("Clocked repetition code: the tick stream as syndrome (OP-23 D0)")
    fig.savefig(CODE_PNG, dpi=130)
    plt.close(fig)


def run_optime_experiment(rng: np.random.Generator) -> None:
    """Experiment C: operational-time covariance across lab tempos (OP-29)."""
    rows = []
    for mode in ("co_clocked", "lab_clocked"):
        for k in OPTIME_K_LIST:
            detuning = DETUNING / k if mode == "co_clocked" else DETUNING
            row = run_grid_point(
                OPTIME_KAPPA,
                OPTIME_GAIN,
                rng,
                every_k=k,
                periods=OPTIME_MEASURED_PERIODS * k,
                detuning=detuning,
                gamma=0.0,
            )
            row["mode"] = mode
            row["lab_periods"] = OPTIME_MEASURED_PERIODS * k
            rows.append(row)

    fieldnames = list(rows[0].keys())
    with OPTIME_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    def spread(mode: str, key: str) -> float:
        vals = [r[key] for r in rows if r["mode"] == mode]
        mean = float(np.mean(vals))
        if abs(mean) < 1e-12:
            return 0.0
        return round((max(vals) - min(vals)) / mean, 6)

    metrics = [
        "memory_retention",
        "clock_slack_bits",
        "error_info_bits",
        "phase_lock",
        "logical_leak_bits",
    ]
    summary = [("tick_count_per_member", 2 * OPTIME_MEASURED_PERIODS)]
    for key in metrics:
        summary.append((f"co_clocked_spread_{key}", spread("co_clocked", key)))
        summary.append((f"lab_clocked_spread_{key}", spread("lab_clocked", key)))
    with OPTIME_SUMMARY_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["metric", "value"])
        writer.writerows(summary)

    plot_optime_curves(rows)

    print("operational-time covariance probe complete")
    for key, value in summary:
        print(f"  {key}: {value}")


def plot_optime_curves(rows: list[dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    panels = [
        ("memory_retention", "memory retention (tick-native cost)"),
        ("error_info_bits", "I(error; record) bits"),
        ("phase_lock", "phase lock"),
        ("clock_slack_bits", "H(r_{n+1} | r_n) bits"),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(17, 4), constrained_layout=True)
    for ax, (key, title) in zip(axes, panels):
        for mode, marker in (("co_clocked", "o"), ("lab_clocked", "s")):
            ks = [r["every_k"] for r in rows if r["mode"] == mode]
            vals = [r[key] for r in rows if r["mode"] == mode]
            ax.plot(ks, vals, marker=marker, label=mode)
        ax.set_xlabel("lab-time dilation k (ticks every k-th period)")
        ax.set_title(title)
        ax.grid(alpha=0.3)
    axes[0].legend()
    fig.suptitle(
        "Operational-time covariance probe: same tick count, different lab tempo"
    )
    fig.savefig(OPTIME_PNG, dpi=130)
    plt.close(fig)


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
