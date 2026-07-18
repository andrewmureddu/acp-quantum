# Session log — 2026-07-18 — operational-time covariance probe

## Intent

Third pull on the braided-clock thread: connect OP-22 to OP-29 by turning
the braided quantum clock into the first executable probe of the
operational-time covariance principle.

## What was built

Experiment C inside `simulations/quantum_braiding_clock/quantum_braiding_clock.py`:

- `run_grid_point` gained `periods`, `detuning`, and `gamma` overrides;
- a five-member family of clocks with identical operational length — 32
  verification ticks at `kappa = 0.21`, gain `3.3` — but lab tempos dilated
  by k in {1,2,3,4,6} (ticks on every k-th nominal period, run stretched to
  keep the tick count fixed);
- two disturbance conventions: `co_clocked` (detuning / k, so per-tick
  transition kernels match — OP-29 operational conjugacy) and `lab_clocked`
  (fixed detuning, conjugacy fails); `gamma = 0` so detuning is the only
  lab-clocked process;
- new outputs: `braiding_clock_optime_scan.csv`,
  `braiding_clock_optime_summary.csv`, `braiding_clock_optime_curves.png`.

## Results

1. **Tick-native scalars are invariant unconditionally.** Memory retention
   sits in `0.458`-`0.494` across all ten runs and record slack has
   relative spread below `1e-3` — these depend only on how many
   verification steps were executed, not how sparsely they sit in lab time.
2. **Record-facing diagnostics obey the conjugacy condition.** Co-clocked,
   phase lock (`0.281`-`0.443`) and syndrome information (`0.020`-`0.079`
   bits) stay in one band, residual scatter consistent with MI estimator
   noise at 600 trajectories. Lab-clocked, covariance fails sharply: lock
   is zero from k=2 and syndrome falls to `0.0003` bits by k=6. A slowed
   clock facing a lab-tempo disturbance is not a slower version of the same
   productive interval — it exits the interval in its own proper time,
   through failure of the record-selectivity condition.
3. **Noncentrality is tempo-independent:** logical leak stays at the
   finite-sample floor in every member of both families.

## Files touched

- `simulations/quantum_braiding_clock/` (script, README, three new outputs).
- `bridges/quantum_braiding_timekeeping.md` (new section 12).
- `bridges/operational_time_relativity.md` (new section 6).
- `OPEN_PROBLEMS.md` (OP-29 to open/partial+, OP-22 updated).
- `STATUS.md` (changelog).

## Next steps

- The OP-29 covariance theorem now has a concrete instance to generalize:
  linear tempo maps, matching macrostate partitions, disturbance kernel
  either commuting or not with the tempo map. The theorem should predict
  the observed sharp (not gradual) failure in the non-conjugate case.
- Small-code braided clock connecting to the hardware ladder (OP-23).
