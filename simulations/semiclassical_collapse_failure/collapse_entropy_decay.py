#!/usr/bin/env python3
"""Numerical check of the semiclassical collapse failure theorem.

Companion to `bridges/semiclassical_collapse_failure.md`.

Unlike `simulations/cosmic_coordination_floor/`, this is not a schematic
stochastic model. It integrates the exact kinematics of a geodesic congruence
and measures the coarse-grained future entropy directly, so the theorem's
inequalities can be checked rather than illustrated.

Model
-----
A bundle of neighbouring timelike geodesics is described by the Jacobi
deviation matrix J(tau), a 3x3 matrix with

    Jddot = -Rtidal(tau) J,        J(0) = I,   Jdot(0) = (theta0/3) I + sigma0.

The expansion tensor is B = Jdot J^{-1}, with

    theta   = tr(B) = d/dtau log det J,
    sigma   = symmetric traceless part of B,
    detJ    = cross-sectional volume element (up to the initial volume).

Taking the trace of Bdot = -Rtidal - B^2 reproduces the Raychaudhuri equation

    dtheta/dtau = -(1/3) theta^2 - sigma_ij sigma_ij - Rtidal_ab u^a u^b

identically, so this is geodesic-congruence kinematics, not an analogy.

The source is self-consistent pressureless dust: mass conservation gives
rho(tau) = rho0 / detJ(tau), and for dust

    Rtidal_ab u^a u^b = tr(Rtidal) = 4 pi G rho = kappa / detJ,

which is non-negative, so the strong energy condition holds throughout. A
constant traceless part W (a Weyl-like tidal shear source) may be added; it
does not affect the trace, hence does not affect the energy condition.

Measurement
-----------
A cloud of sample points is drawn uniformly from the initial unit ball, mapped
by x -> J(tau) x, and binned into cubes of side ell. The empirical distribution
over occupied cells gives the coarse-grained future entropy H_{ell,tau} in
bits, and the occupied-cell count N gives the shape-regularity constant

    c_meas = N * ell^3 / (detJ * V0),

which is the quantity that hypothesis (R) of the theorem bounds. Binning is
averaged over several random grid offsets so the result is not an artifact of
where the partition happens to fall.

Scenarios
---------
- `isotropic`      : shear-free collapse; the clean case for the theorem.
- `moderate_shear` : anisotropic collapse still within (R).
- `strong_shear`   : filamenting collapse; the stated loophole in (R).
- `expanding`      : theta0 > 0 control; no focusing, so no entropy decay.
"""

from __future__ import annotations

import csv
import math
import random
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
TIMESERIES_CSV = OUT / "collapse_entropy_timeseries.csv"
SUMMARY_CSV = OUT / "collapse_failure_summary.csv"

# Integration and measurement parameters.
TAU_MAX = 6.0
DT = 0.0005
SAMPLE_EVERY = 0.05

N_POINTS = 20000
CELL_ELL = 0.10
N_OFFSETS = 4
SEED = 20260726

# Dust source strength kappa = 4 pi G rho0, in units where the initial
# cross-sectional volume element is one.
KAPPA = 0.50

# Future-entropy floor, in bits. Matches FLOOR_BITS in the existing
# cosmic_coordination_floor toy so the two suites are commensurable.
FLOOR_BITS = 1.50

# Caustic detection. detJ -> 0 is the definition, but the ODE is singular
# there and a fixed-step integrator can jump straight through the caustic and
# re-emerge with detJ > 0, which is an artifact and not a continuation. The
# expansion scalar is the robust trigger: under the focusing hypotheses theta
# is monotonically decreasing, so theta < -THETA_CAUSTIC guarantees a caustic
# within a further proper time 3/THETA_CAUSTIC, with no possible recovery.
CAUSTIC_EPS = 1e-9
THETA_CAUSTIC = 1.0e5

# Near the caustic theta diverges, so a fixed step would lose the endgame that
# the entropy claim actually lives in. The step is shrunk to keep the
# fractional volume change per step, |theta| * dt, below this value.
MAX_LOG_VOLUME_STEP = 0.05

V0 = 4.0 / 3.0 * math.pi  # volume of the initial unit ball


# --------------------------------------------------------------------------
# minimal 3x3 linear algebra (stdlib only, matching project convention)
# --------------------------------------------------------------------------

Mat = list  # list[list[float]], 3x3


def mat_zero() -> Mat:
    return [[0.0] * 3 for _ in range(3)]


def mat_eye(s: float = 1.0) -> Mat:
    return [[s if i == j else 0.0 for j in range(3)] for i in range(3)]


def mat_add(a: Mat, b: Mat) -> Mat:
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def mat_scale(a: Mat, s: float) -> Mat:
    return [[a[i][j] * s for j in range(3)] for i in range(3)]


def mat_mul(a: Mat, b: Mat) -> Mat:
    return [
        [sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)
    ]


def mat_det(a: Mat) -> float:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def mat_inv(a: Mat) -> Mat:
    d = mat_det(a)
    if abs(d) < 1e-300:
        raise ZeroDivisionError("singular deviation matrix")
    c = [
        [
            a[1][1] * a[2][2] - a[1][2] * a[2][1],
            a[0][2] * a[2][1] - a[0][1] * a[2][2],
            a[0][1] * a[1][2] - a[0][2] * a[1][1],
        ],
        [
            a[1][2] * a[2][0] - a[1][0] * a[2][2],
            a[0][0] * a[2][2] - a[0][2] * a[2][0],
            a[0][2] * a[1][0] - a[0][0] * a[1][2],
        ],
        [
            a[1][0] * a[2][1] - a[1][1] * a[2][0],
            a[0][1] * a[2][0] - a[0][0] * a[2][1],
            a[0][0] * a[1][1] - a[0][1] * a[1][0],
        ],
    ]
    return [[c[i][j] / d for j in range(3)] for i in range(3)]


def mat_trace(a: Mat) -> float:
    return a[0][0] + a[1][1] + a[2][2]


def shear_sq(b: Mat) -> float:
    """sigma_ij sigma^ij for the symmetric traceless part of B."""
    th = mat_trace(b)
    total = 0.0
    for i in range(3):
        for j in range(3):
            s = 0.5 * (b[i][j] + b[j][i]) - (th / 3.0 if i == j else 0.0)
            total += s * s
    return total


# --------------------------------------------------------------------------
# congruence integration
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Scenario:
    name: str
    theta0: float
    shear0: float  # amplitude of the initial traceless shear
    weyl: float  # amplitude of the constant traceless tidal source


SCENARIOS = (
    Scenario("isotropic", theta0=-0.60, shear0=0.00, weyl=0.00),
    Scenario("moderate_shear", theta0=-0.60, shear0=0.12, weyl=0.05),
    Scenario("strong_shear", theta0=-0.60, shear0=0.45, weyl=0.25),
    # theta0 must exceed 3*sqrt(2*KAPPA/3) = 1.732... for the dust ball to be
    # unbound; below that it recollapses and is not a non-focusing control.
    Scenario("unbound_expansion", theta0=+2.00, shear0=0.00, weyl=0.00),
)


def traceless_diag(amp: float) -> Mat:
    """A traceless diagonal deformation: diag(amp, amp, -2 amp)."""
    m = mat_zero()
    m[0][0] = amp
    m[1][1] = amp
    m[2][2] = -2.0 * amp
    return m


def tidal(det_j: float, weyl_amp: float) -> Mat:
    """Rtidal = (kappa/detJ) I/3 + W, with tr(Rtidal) = kappa/detJ >= 0."""
    dj = max(det_j, CAUSTIC_EPS)
    r = mat_eye(KAPPA / dj / 3.0)
    return mat_add(r, traceless_diag(weyl_amp))


def deriv(j: Mat, jd: Mat, weyl_amp: float) -> tuple[Mat, Mat]:
    r = tidal(mat_det(j), weyl_amp)
    return jd, mat_scale(mat_mul(r, j), -1.0)


def rk4_step(j: Mat, jd: Mat, dt: float, weyl_amp: float) -> tuple[Mat, Mat]:
    k1j, k1v = deriv(j, jd, weyl_amp)
    k2j, k2v = deriv(
        mat_add(j, mat_scale(k1j, dt / 2)), mat_add(jd, mat_scale(k1v, dt / 2)), weyl_amp
    )
    k3j, k3v = deriv(
        mat_add(j, mat_scale(k2j, dt / 2)), mat_add(jd, mat_scale(k2v, dt / 2)), weyl_amp
    )
    k4j, k4v = deriv(
        mat_add(j, mat_scale(k3j, dt)), mat_add(jd, mat_scale(k3v, dt)), weyl_amp
    )

    def comb(a, b, c, d):
        out = mat_zero()
        for i in range(3):
            for k in range(3):
                out[i][k] = (a[i][k] + 2 * b[i][k] + 2 * c[i][k] + d[i][k]) * dt / 6.0
        return out

    return mat_add(j, comb(k1j, k2j, k3j, k4j)), mat_add(jd, comb(k1v, k2v, k3v, k4v))


# --------------------------------------------------------------------------
# coarse-grained entropy measurement
# --------------------------------------------------------------------------


def unit_ball_points(n: int, rng: random.Random) -> list[tuple[float, float, float]]:
    pts = []
    while len(pts) < n:
        x = rng.uniform(-1.0, 1.0)
        y = rng.uniform(-1.0, 1.0)
        z = rng.uniform(-1.0, 1.0)
        if x * x + y * y + z * z <= 1.0:
            pts.append((x, y, z))
    return pts


def coarse_entropy(
    j: Mat, pts: list[tuple[float, float, float]], offsets: list[tuple[float, float, float]]
) -> tuple[float, float]:
    """Return (mean entropy in bits, mean occupied-cell count) over grid offsets."""
    h_total = 0.0
    n_total = 0.0
    for ox, oy, oz in offsets:
        counts: dict[tuple[int, int, int], int] = {}
        for x, y, z in pts:
            u = j[0][0] * x + j[0][1] * y + j[0][2] * z
            v = j[1][0] * x + j[1][1] * y + j[1][2] * z
            w = j[2][0] * x + j[2][1] * y + j[2][2] * z
            key = (
                math.floor((u - ox) / CELL_ELL),
                math.floor((v - oy) / CELL_ELL),
                math.floor((w - oz) / CELL_ELL),
            )
            counts[key] = counts.get(key, 0) + 1
        total = float(len(pts))
        h = 0.0
        for c in counts.values():
            p = c / total
            h -= p * math.log2(p)
        h_total += h
        n_total += len(counts)
    k = float(len(offsets))
    return h_total / k, n_total / k


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def run_scenario(sc: Scenario, pts, offsets) -> tuple[list[dict], dict]:
    j = mat_eye()
    jd = mat_add(mat_eye(sc.theta0 / 3.0), traceless_diag(sc.shear0))

    rows: list[dict] = []
    tau = 0.0
    next_sample = 0.0
    last_det = None
    max_steps = 20_000_000

    h0 = None
    h_last = None
    tau_floor = None
    tau_caustic = None
    max_c = 0.0
    c_initial = None
    alpha = abs(sc.theta0) if sc.theta0 < 0 else 0.0

    for _ in range(max_steps):
        if tau > TAU_MAX:
            break
        det_j = mat_det(j)
        theta_now = mat_trace(mat_mul(jd, mat_inv(j))) if det_j > CAUSTIC_EPS else None
        if det_j <= CAUSTIC_EPS or (
            theta_now is not None and theta_now < -THETA_CAUSTIC
        ):
            if tau_caustic is None:
                tau_caustic = tau
            break

        # Sample on the fixed proper-time grid, but also whenever the volume
        # element halves, so the endgame near caustic formation is resolved
        # rather than stepped over.
        due = tau + 1e-12 >= next_sample or (
            last_det is not None and det_j < 0.5 * last_det
        )
        if due:
            b = mat_mul(jd, mat_inv(j))
            theta = mat_trace(b)
            s2 = shear_sq(b)
            h_bits, n_cells = coarse_entropy(j, pts, offsets)
            vol = det_j * V0
            c_meas = n_cells * CELL_ELL**3 / vol if vol > 0 else float("nan")

            # Hypothesis (R) is a statement about the regime where the image
            # still fills at least one cell's worth of volume. Below that,
            # c_meas diverges trivially because N >= 1 while V -> 0, which is
            # crystallization, not a failure of shape regularity.
            in_r_regime = vol >= CELL_ELL**3
            if in_r_regime:
                max_c = max(max_c, c_meas)

            if h0 is None:
                h0 = h_bits
                c_initial = c_meas
            h_last = h_bits
            if tau_floor is None and h_bits < FLOOR_BITS:
                tau_floor = tau

            last_det = det_j

            # Theorem bounds (only meaningful for the focusing scenarios).
            if alpha > 0.0:
                vol_bound_exp = V0 * math.exp(-alpha * tau)
                cubic = 1.0 - alpha * tau / 3.0
                vol_bound_cubic = V0 * cubic**3 if cubic > 0 else 0.0
            else:
                vol_bound_exp = float("nan")
                vol_bound_cubic = float("nan")

            rows.append(
                {
                    "scenario": sc.name,
                    "tau": round(tau, 6),
                    "theta": round(theta, 8),
                    "shear_sq": round(s2, 8),
                    "det_J": f"{det_j:.10g}",
                    "volume": f"{vol:.10g}",
                    "volume_bound_exp": f"{vol_bound_exp:.10g}",
                    "volume_bound_cubic": f"{vol_bound_cubic:.10g}",
                    "cells_occupied": round(n_cells, 3),
                    "entropy_bits": round(h_bits, 6),
                    "shape_constant_c": round(c_meas, 6),
                    "in_R_regime": int(in_r_regime),
                }
            )
            next_sample = tau + SAMPLE_EVERY

        dt = DT
        if theta_now is not None and abs(theta_now) > 1e-12:
            dt = min(DT, MAX_LOG_VOLUME_STEP / abs(theta_now))
        j, jd = rk4_step(j, jd, dt, sc.weyl)
        tau += dt

    if tau_caustic is None and mat_det(j) <= CAUSTIC_EPS:
        tau_caustic = tau

    # Empirical entropy decay slope, in bits per unit proper time, taken over
    # the window where the entropy is still resolved above the floor.
    slope = float("nan")
    usable = [r for r in rows if r["entropy_bits"] > FLOOR_BITS]
    if len(usable) >= 2:
        t0, t1 = usable[0]["tau"], usable[-1]["tau"]
        e0, e1 = usable[0]["entropy_bits"], usable[-1]["entropy_bits"]
        if t1 > t0:
            slope = (e1 - e0) / (t1 - t0)

    predicted_slope = -alpha / math.log(2.0) if alpha > 0 else float("nan")
    tau_x_bound = 3.0 / alpha if alpha > 0 else float("nan")

    summary = {
        "scenario": sc.name,
        "theta0": sc.theta0,
        "shear0": sc.shear0,
        "weyl": sc.weyl,
        "alpha": round(alpha, 6),
        "H0_bits": round(h0, 6) if h0 is not None else float("nan"),
        "H_final_bits": round(h_last, 6) if h_last is not None else float("nan"),
        "entropy_slope_bits_per_tau": round(slope, 6),
        "predicted_slope_bound": round(predicted_slope, 6)
        if alpha > 0
        else float("nan"),
        "slope_within_bound": bool(slope <= predicted_slope + 1e-9)
        if alpha > 0 and not math.isnan(slope)
        else "n/a",
        "tau_floor_breach": round(tau_floor, 4) if tau_floor is not None else "none",
        "tau_caustic_measured": round(tau_caustic, 4)
        if tau_caustic is not None
        else "none",
        "tau_caustic_bound_3_over_alpha": round(tau_x_bound, 4)
        if alpha > 0
        else float("nan"),
        "c_initial": round(c_initial, 4) if c_initial is not None else float("nan"),
        "max_shape_constant_c_in_R_regime": round(max_c, 4),
    }
    return rows, summary


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    pts = unit_ball_points(N_POINTS, rng)
    offsets = [
        (
            rng.uniform(0.0, CELL_ELL),
            rng.uniform(0.0, CELL_ELL),
            rng.uniform(0.0, CELL_ELL),
        )
        for _ in range(N_OFFSETS)
    ]

    all_rows: list[dict] = []
    summaries: list[dict] = []
    for sc in SCENARIOS:
        rows, summary = run_scenario(sc, pts, offsets)
        all_rows.extend(rows)
        summaries.append(summary)

    with TIMESERIES_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
        writer.writeheader()
        writer.writerows(all_rows)

    with SUMMARY_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(summaries[0].keys()))
        writer.writeheader()
        writer.writerows(summaries)

    width = 22
    print("semiclassical collapse failure: numerical check")
    print()
    keys = [
        "scenario",
        "alpha",
        "H0_bits",
        "H_final_bits",
        "entropy_slope_bits_per_tau",
        "predicted_slope_bound",
        "slope_within_bound",
        "tau_floor_breach",
        "tau_caustic_measured",
        "tau_caustic_bound_3_over_alpha",
        "c_initial",
        "max_shape_constant_c_in_R_regime",
    ]
    for k in keys:
        print(k.ljust(width + 10), "  ".join(str(s[k]).rjust(14) for s in summaries))
    print()
    print(f"wrote {TIMESERIES_CSV}")
    print(f"wrote {SUMMARY_CSV}")


if __name__ == "__main__":
    main()
