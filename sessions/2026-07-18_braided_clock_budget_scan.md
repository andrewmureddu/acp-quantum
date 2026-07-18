# Session log — 2026-07-18 — braided clock budget scan

## Intent

Follow-up to the 2026-07-17 braided-quantum-clock session. Andrew asked for
the named next step: the tick-rate versus tick-strength tradeoff at fixed
total dephasing budget.

## What was built

Experiment B inside `simulations/quantum_braiding_clock/quantum_braiding_clock.py`:

- `run_grid_point` gained an `every_k` parameter so the two-burst
  escapement fires only on every k-th nominal period;
- a run with N ticks at strength kappa spends budget
  `B = -(N/2) ln(1 - kappa^2)` (ideal retention `exp(-B)`); the scan holds
  B fixed, varies the rate over k in {1,2,3,4,6,8,12}, sets kappa to spend
  the whole budget, and takes the best of gains {0, 1.65, 3.3} per cell;
- new outputs: `braiding_clock_budget_scan.csv`,
  `braiding_clock_budget_summary.csv`, `braiding_clock_budget_heatmaps.png`.

## Results

1. **Distribution: many weak ticks win decisively.** Memory retention is
   rate-independent at fixed budget (`0.329` vs `0.336` at the extremes,
   which doubles as the budget-normalization check), but error information
   collapses from `0.0646` to `0.0024` bits and braid score from `0.004503`
   to `0.000071` going from fastest to slowest rate. Sparse strong ticks
   let phase error accumulate between corrections, alias the drift, and
   inject large backaction jitter.
2. **Amount: interior optimum in the budget.** At the fastest rate, memory
   falls monotonically in B, error information rises monotonically, and the
   braid score peaks at `B = 1.05` (braid `0.006942`), falling toward both
   ends. The ACP productive interval reappears in the spend dimension.
3. Logical leak stays at the finite-sample floor across the budget grid
   (max `0.010816` bits) — the controller remains noncentral at every rate.

Combined design rule, bracketed from both sides by this scan and the
previous continuous-monitoring null: tick as often as possible, as gently
as possible, and spend neither too little nor too much coherence on it.

## Files touched

- `simulations/quantum_braiding_clock/` (script, README, three new outputs).
- `bridges/quantum_braiding_timekeeping.md` (new section 11).
- `OPEN_PROBLEMS.md` (OP-22).
- `STATUS.md` (changelog, date).

## Next steps

- Clock-slack and regularity metrics in operational time (OP-29): the
  natural clock of this system is its own tick count, so the budget scan is
  implicitly comparing systems with different operational tempos.
- Small-code braided clock connecting to the hardware ladder (OP-23).
