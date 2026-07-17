# Session log — 2026-07-17 — braided quantum clock

## Intent

Andrew asked for something fun, interesting, and speculative with the corpus.
The chosen target was the one named front with zero executable content:
OP-22, collapse as internal timekeeping (`bridges/quantum_braiding_timekeeping.md`),
whose section 9 specified a monitored-qubit feedback simulation that did not
yet exist.

## What was built

`simulations/quantum_braiding_clock/quantum_braiding_clock.py`, a seeded
Bloch-vector toy in which a single qubit keeps time by being measured:

- logical bit in the x component; every Hamiltonian and feedback rotation is
  about x, so the controller is Knill-Laflamme-noncentral by construction;
- clock carrier precessing in the y-z plane at a hidden detuned frequency;
  the detuning sign is the error sector (the clock runs fast or slow);
- a two-burst-per-period weak-measurement escapement (in-phase amplitude
  tick plus quadrature phase-error readout);
- an integrating phase-locked loop driven by the qubit's own quadrature
  records, threading collapse entropy back into the dynamics.

Diagnostics follow the bridge: Markov record slack, signed logical
retention, tick-stream error information, conditional logical leak, phase
lock, and a composite braid score.

## Results

1. **Continuous monitoring admits no braid** (methodological null from the
   first model iteration, preserved in the module docstring): coherence
   decay `exp(-kappa^2 t / 2)` and drift readability against backaction
   never overlap, and a constant z drift under fast precession hides in the
   unmonitored y quadrature. The braid needs pulsed rhythm.
2. **Pulsed monitoring opens a modest interior interval**: best point at
   `kappa = 0.2136`, `g = 3.3` with memory retention `0.307318`, error
   information `0.061023` bits, phase lock `0.344621` (feedback raises the
   grid mean from `0.094241` at zero gain to `0.425850` at max gain), and
   logical leak at the finite-sample floor everywhere (grid max `0.011986`
   bits).
3. Both ACP boundaries are fatal in the expected ways; notably strong
   monitoring destroys not only the memory but the syndrome channel itself,
   because the escapement's backaction dissolves the oscillation it reads.

## Modeling honesty notes

- The first memory metric (unsigned |x|) was corrected to signed retention
  after feedback rotations were seen pumping sign-scrambled amplitude back
  into x.
- The record slack gate is reported but not multiplied into the braid
  score: binary weak ticks are near-fair-coin by encoding, so the raw
  Markov entropy would penalize the whole interior for a property of the
  tick alphabet.
- A single-bit bang-bang PLL failed to lock (phase diffusion per tick too
  large); the shipped version integrates an EMA of the quadrature records.

## Files touched

- Added `simulations/quantum_braiding_clock/` (script, README, three seeded
  outputs).
- Extended `bridges/quantum_braiding_timekeeping.md` with section 10.
- Upgraded OP-22 to partial+ in `OPEN_PROBLEMS.md`.
- Updated `STATUS.md` (front 8, changelog, date).

## Next steps

- Tick-rate versus tick-strength tradeoff at fixed total dephasing budget.
- Clock-slack and regularity metrics stated in operational time (OP-29).
- A small-code version connecting the braided clock to the hardware ladder
  (OP-23).
