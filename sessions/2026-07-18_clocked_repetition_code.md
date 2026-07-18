# Session log — 2026-07-18 — clocked repetition code

## Intent

Fourth pull on the braided-clock thread: the small-code version connecting
the clock architecture to the OP-23 hardware ladder.

## What was built

Experiment D inside `simulations/quantum_braiding_clock/quantum_braiding_clock.py`:

- three braided-clock qubits carrying one logical bit (sign of each x
  component), sharing one detuning sector and one common-mode PLL drive;
- a per-period phase-flip channel (`(x, y) -> (-x, -y)` at `p_flip` per
  qubit per period);
- a pair-parity record channel: per in-phase tick, each qubit pair emits a
  binary record with bias `0.6 * sign(x_i x_j)`, noisy in readout but free
  of logical backaction (imported from the Knill-Laflamme argument — the
  parity operator commutes with the logical algebra);
- four policies on the same terminal median logical readout: bare,
  code_unchecked, code_checked (EMA parity evidence, gated at 0.25),
  code_overactive (raw single parity records);
- new outputs: `braiding_clock_code_scan.csv`,
  `braiding_clock_code_summary.csv`, `braiding_clock_code_curves.png`.

## Results

1. **Negative lemma (kept in the module docs): the tick stream cannot be
   its own syndrome.** The first design decoded flips from the weak tick
   records (a flipped qubit ticks upside-down). It fails structurally: a
   z-tick statistic with flip-identification SNR S costs `exp(-S^2/2)` of
   the coherence it protects, so memory-compatible ticks are too dilute to
   decode flips within a run. This is the cheapest statement of why codes
   exist — the syndrome must be a commuting observable that can be read
   strongly at zero logical cost.
2. **Correction has its own productive interval.** Checked beats bare,
   unchecked, and overactive only for `p_flip ~ 0.005-0.04` (at `0.02`:
   `0.140` vs `0.074` / `0.052` / `0.065`; sign fidelity `0.78` vs
   `0.625`). At zero noise the checker's residual false positives make it
   a net cost (`0.243` vs bare `0.321`); at `0.08` multi-flips overwhelm
   the distance-3 decoder (checked `0.000`). Same cautionary shape as the
   H0-H2 hardware scans, reproduced inside the braided-clock architecture.
3. **Noncentrality holds at code level:** grid-max leak on the common-mode
   clock record is `0.006` bits; the overactive policy is worse everywhere
   (7.4 corrections/run vs 1.7 at `p_flip = 0.02`).

## Honesty boundary

This is the D0 rung: product-state Bloch dynamics with classical parity
records standing in for collective stabilizer measurements. It tests the
control architecture (clock/syndrome separation by commutation, noncentral
common-mode feedback, evidence-gated correction under the OP-23 acceptance
discipline), not genuine stabilizer protection.

## Files touched

- `simulations/quantum_braiding_clock/` (script, README, three new outputs).
- `bridges/quantum_braiding_timekeeping.md` (new section 13).
- `OPEN_PROBLEMS.md` (OP-22, OP-23).
- `STATUS.md` (changelog).

## Next steps

- Entangled stabilizer simulation of the same clocked-code architecture,
  deriving rather than importing the parity channel's zero logical cost.
- Feed the clocked code into the H-ladder's measured-trace replay
  discipline.
