#!/usr/bin/env python3
"""Cadence control law: exact objective curves and exponent fits.

This harness tests the two cadence laws stated in
`bridges/cadence_control_law.md`:

1. Correction cadence (square-root law). A 3-qubit repetition memory with
   per-tick bit-flip probability p per qubit is corrected every T ticks by
   majority vote; each correction event applies logical dephasing backaction b.
   Logical flips across cycles compose by XOR, so the exact per-tick decay
   rate of the logical bit channel is -ln(1 - 2 P_cycle) / (2T), and the
   total per-tick cost is

       J(T) = [ -ln(1 - 2 P_cycle(p, T)) / 2 + gamma(b) ] / T,
       P_cycle(p, T) = 3 q^2 (1 - q) + q^3,
       q(p, T) = (1 - (1 - 2p)^T) / 2,
       gamma(b) = -ln(1 - b),

   with continuum prediction T* ~ sqrt(gamma / 3) / p, i.e. exponent 1/2 in
   the backaction and -1 in the drift rate.

2. Adaptation cadence (cube-root law). A controller tracks a parameter
   drifting at rate a per round through observations with noise variance
   sigma^2 using a moving average over the last W rounds. The exact
   mean-squared misalignment of the window estimator is

       M(W) = sigma^2 / W + a^2 (W - 1)^2 / 4,

   with continuum prediction W* ~ (2 sigma^2 / a^2)^{1/3}, i.e. exponent
   -2/3 in the drift rate.

Everything is computed exactly (no Monte Carlo); optima are integer argmins
of the exact objectives, and exponents are least-squares slopes in log-log.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(exist_ok=True)

T_MAX = 2000
W_MAX = 4000


def q_odd(p: float, ticks: int) -> float:
    """Probability a single qubit has flipped an odd number of times."""
    return 0.5 * (1.0 - (1.0 - 2.0 * p) ** ticks)


def cycle_failure(p: float, ticks: int) -> float:
    """Probability majority-vote correction inflicts a logical flip."""
    q = q_odd(p, ticks)
    return 3.0 * q * q * (1.0 - q) + q ** 3


def correction_cost(p: float, ticks: int, b: float) -> float:
    """Exact per-tick logical cost rate for correction interval `ticks`."""
    gamma = -math.log(1.0 - b)
    contrast = max(1.0 - 2.0 * cycle_failure(p, ticks), 1e-300)
    flip_gamma = -0.5 * math.log(contrast)
    return (flip_gamma + gamma) / ticks


def adaptation_cost(sigma2: float, a: float, window: int) -> float:
    """Exact mean-squared misalignment of a moving-average tracker."""
    bias = a * (window - 1) / 2.0
    return sigma2 / window + bias * bias


def argmin_int(fn, upper: int) -> tuple[int, float]:
    best_x, best_v = 1, fn(1)
    for x in range(2, upper + 1):
        v = fn(x)
        if v < best_v:
            best_x, best_v = x, v
    return best_x, best_v


def loglog_slope(xs: list[float], ys: list[float]) -> float:
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx)
    mx, my = sum(lx) / n, sum(ly) / n
    num = sum((a - mx) * (b - my) for a, b in zip(lx, ly))
    den = sum((a - mx) ** 2 for a in lx)
    return num / den


def logspace(lo: float, hi: float, n: int) -> list[float]:
    llo, lhi = math.log10(lo), math.log10(hi)
    return [10 ** (llo + (lhi - llo) * i / (n - 1)) for i in range(n)]


def correction_backaction_scan() -> tuple[list[dict], float]:
    # Small drift rate so the integer optimum spans a wide range and the
    # log-log fit is not flattened by discretization.
    p = 0.002
    rows = []
    for b in logspace(1e-4, 5e-2, 14):
        gamma = -math.log(1.0 - b)
        t_star, j_star = argmin_int(lambda t: correction_cost(p, t, b), T_MAX)
        t_pred = math.sqrt(gamma / 3.0) / p
        rows.append(
            {
                "p_noise": p,
                "backaction": b,
                "gamma": gamma,
                "T_star": t_star,
                "T_pred_continuum": t_pred,
                "J_star": j_star,
            }
        )
    slope = loglog_slope([r["backaction"] for r in rows], [r["T_star"] for r in rows])
    return rows, slope


def correction_drift_scan() -> tuple[list[dict], float]:
    b = 0.012
    rows = []
    for p in logspace(1e-3, 1e-2, 12):
        gamma = -math.log(1.0 - b)
        t_star, j_star = argmin_int(lambda t: correction_cost(p, t, b), T_MAX)
        t_pred = math.sqrt(gamma / 3.0) / p
        rows.append(
            {
                "p_noise": p,
                "backaction": b,
                "gamma": gamma,
                "T_star": t_star,
                "T_pred_continuum": t_pred,
                "J_star": j_star,
            }
        )
    slope = loglog_slope([r["p_noise"] for r in rows], [r["T_star"] for r in rows])
    return rows, slope


def adaptation_scan() -> tuple[list[dict], float]:
    sigma2 = 1.0
    rows = []
    for a in logspace(1e-3, 1e-1, 12):
        w_star, m_star = argmin_int(lambda w: adaptation_cost(sigma2, a, w), W_MAX)
        w_pred = (2.0 * sigma2 / (a * a)) ** (1.0 / 3.0)
        rows.append(
            {
                "sigma2": sigma2,
                "drift_rate": a,
                "W_star": w_star,
                "W_pred_continuum": w_pred,
                "M_star": m_star,
            }
        )
    slope = loglog_slope([r["drift_rate"] for r in rows], [r["W_star"] for r in rows])
    return rows, slope


def risky_qec_crosscheck() -> dict:
    """Compare the law against the prior monitoring scan's operating point."""
    p, b = 0.02, 0.012
    gamma = -math.log(1.0 - b)
    t_star, _ = argmin_int(lambda t: correction_cost(p, t, b), T_MAX)
    t_pred = math.sqrt(gamma / 3.0) / p
    t_star_zero, _ = argmin_int(lambda t: correction_cost(p, t, 0.0), T_MAX)
    return {
        "p_noise": p,
        "backaction": b,
        "T_star_exact_objective": t_star,
        "T_pred_continuum": t_pred,
        "T_star_zero_backaction": t_star_zero,
        "risky_qec_claims_best_interval": 4,
        "risky_qec_claims_best_interval_zero_backaction": 1,
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    back_rows, back_slope = correction_backaction_scan()
    drift_rows, drift_slope = correction_drift_scan()
    adapt_rows, adapt_slope = adaptation_scan()
    cross = risky_qec_crosscheck()

    write_csv(OUT / "correction_backaction_scan.csv", back_rows)
    write_csv(OUT / "correction_drift_scan.csv", drift_rows)
    write_csv(OUT / "adaptation_drift_scan.csv", adapt_rows)
    write_csv(OUT / "risky_qec_crosscheck.csv", [cross])

    summary = [
        {"metric": "correction_backaction_exponent_fit", "value": f"{back_slope:.4f}", "prediction": "0.5"},
        {"metric": "correction_drift_exponent_fit", "value": f"{drift_slope:.4f}", "prediction": "-1.0"},
        {"metric": "adaptation_drift_exponent_fit", "value": f"{adapt_slope:.4f}", "prediction": "-0.6667"},
        {
            "metric": "crosscheck_T_star_exact_vs_prior_sim",
            "value": f"{cross['T_star_exact_objective']} vs {cross['risky_qec_claims_best_interval']}",
            "prediction": f"continuum {cross['T_pred_continuum']:.2f}",
        },
        {
            "metric": "crosscheck_T_star_zero_backaction",
            "value": str(cross["T_star_zero_backaction"]),
            "prediction": "1",
        },
    ]
    write_csv(OUT / "cadence_summary.csv", summary)

    for row in summary:
        print(f"{row['metric']}: {row['value']} (prediction {row['prediction']})")


if __name__ == "__main__":
    main()
