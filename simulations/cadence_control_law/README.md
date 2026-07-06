# Cadence Control Law Verification

Companion harness for `bridges/cadence_control_law.md`. Everything is exact
(analytic objectives, integer argmins, log-log least-squares fits); there is
no Monte Carlo sampling and no external dependency beyond the Python
standard library.

## What it computes

1. **Correction cadence (square-root law).** 3-qubit repetition memory,
   per-tick bit-flip probability `p` per qubit, majority correction every `T`
   ticks, logical dephasing backaction `b` per correction event. Exact
   per-tick cost `J(T) = [-ln(1 - 2 P_cyc)/2 + gamma(b)] / T` with
   `P_cyc = 3q^2(1-q) + q^3`, `q = (1-(1-2p)^T)/2`, `gamma = -ln(1-b)`.
   Predicted optimum `T* ~ sqrt(gamma/3)/p`: exponent `1/2` in backaction,
   `-1` in drift.
2. **Adaptation cadence (cube-root law).** Moving-average tracking of a
   parameter drifting at rate `a` with observation noise `sigma^2`. Exact
   misalignment `M(W) = sigma^2/W + a^2 (W-1)^2 / 4`. Predicted optimum
   `W* ~ (2 sigma^2 / a^2)^{1/3}`: exponent `-2/3` in drift.
3. **Retrodiction cross-check.** At the operating point of
   `simulations/risky_qec_claims/` (`p=0.02`, `b=0.012`), the exact
   objective's integer optimum is compared with that scan's empirical best
   correction interval.

## Results (exact, deterministic)

| Check | Fitted | Predicted |
|---|---|---|
| `T*` vs backaction `b` (`p=0.002`) | `0.5515` | `0.5` |
| `T*` vs drift `p` (`b=0.012`) | `-0.9942` | `-1.0` |
| `W*` vs drift `a` (`sigma^2=1`) | `-0.6571` | `-0.6667` |
| Cross-check `T*` at (`p=0.02`, `b=0.012`) | `4` | prior sim best `4`; continuum `3.17` |
| Cross-check `T*` at `b=0` | `1` | prior sim best `1` |

The backaction fit exceeds `1/2` slightly from finite-`b` curvature (the
`(1-q)` factor and the convexity of `-ln(1-b)`); the exponent scans use a
small drift rate so integer discretization does not flatten the slopes.

## Files

- `cadence_control_law.py` — the harness.
- `outputs/correction_backaction_scan.csv` — `T*(b)` at fixed `p`.
- `outputs/correction_drift_scan.csv` — `T*(p)` at fixed `b`.
- `outputs/adaptation_drift_scan.csv` — `W*(a)` at fixed `sigma^2`.
- `outputs/risky_qec_crosscheck.csv` — retrodiction of the prior scan.
- `outputs/cadence_summary.csv` — fitted exponents and checks.

Run with `python3 cadence_control_law.py`.
