# Session log — 2026-07-18 — entangled stabilizer code

## Intent

Fifth pull on the braided-clock thread: upgrade the D0 clocked repetition
code to a true entangled stabilizer simulation (D1), deriving rather than
importing the parity channel's zero logical cost.

## What was built

Experiment E inside `simulations/quantum_braiding_clock/quantum_braiding_clock.py`:

- state-vector dynamics (600 trajectories x 8 complex amplitudes) for the
  three-qubit phase-flip code `|0_L> = |+++>`, `|1_L> = |--->`;
- protected information stored as genuine quantum coherence: the
  logical-Y eigenstate `(|0_L> + i sb |1_L>)/sqrt(2)`;
- per-period independent `Z_i` phase flips at `p_flip`;
- weak measurements of the stabilizers `X1X2`, `X2X3` as proper Kraus
  pairs at readout fidelity `0.6`, EMA evidence decoding (alpha `0.2`,
  gate `0.35`, 5-period burn-in), terminal ideal decode for all code
  policies;
- five policies: bare, bare_monitored (same-strength weak X probe on an
  unencoded qubit), code_unchecked, code_checked, code_overactive;
- new outputs: `braiding_clock_stabilizer_scan.csv`,
  `braiding_clock_stabilizer_summary.csv`,
  `braiding_clock_stabilizer_curves.png`.

## Results

1. **Zero logical cost of syndrome extraction, derived.** Under the Z
   channel the state is always a stabilizer eigenstate, so the Kraus
   update acts as the identity on it: at zero noise the checked code
   retains `0.9967` coherence through 72 weak stabilizer measurements
   while the bare qubit probed at the same strength retains `0.0008`. The
   commutant, not the probe strength, decides whether monitoring is free
   or fatal.
2. **The correction productive interval survives the quantum upgrade.**
   Checked dominates every baseline on the same terminal readout for
   `p_flip ~ 0.005-0.04` (`0.930 / 0.817 / 0.533` vs unchecked
   `0.860 / 0.697 / 0.410`, bare `0.733 / 0.473 / 0.240`); at `0.08` the
   distance-3 decoder saturates and mid-run checking mildly hurts
   (`0.010` vs `0.030`). Overactive is destroyed everywhere.
3. **The D0 evidence-gating lesson reproduces with true state vectors.**
   Without burn-in and a higher gate, early EMA fluctuations false-fire
   the decoder and zero-noise retention falls to `0.54`; pairs of stray
   corrections on different qubits compound to logical `Z-bar` errors.
4. **Structural remark for the clock program** (bridge §14): stabilizer
   records are free exactly because they commute with the logical
   algebra — which is why they can never read a logical clock phase. A
   braided clock on a code must split its records into a noncentral
   syndrome channel and a deliberately central, costly clock channel; the
   single-qubit Experiment A was the degenerate case where one stream did
   both jobs badly.

## Files touched

- `simulations/quantum_braiding_clock/` (script, README, three new outputs).
- `bridges/quantum_braiding_timekeeping.md` (new section 14).
- `OPEN_PROBLEMS.md` (OP-22, OP-23).
- `STATUS.md` (changelog).

## Next steps

- Apply the H-ladder measured-trace replay discipline to a clocked code.
- Consider promoting the section 14 record-splitting remark to a small
  formal proposition (it is a corollary of Knill-Laflamme plus the
  definition of a clock record).
