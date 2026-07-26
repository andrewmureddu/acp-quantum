# Session: Sorting Efficiency Measured on the H2 QEC Scaffold

**Date:** 2026-07-26
**Branch:** `claude/singularity-sorting-mechanism-a7c917`
**Front:** OP-30 (crystallization sorting engine), feeding OP-16 and OP-23
**Predecessor:** `sessions/2026-07-26_crystallization_sorting_engine.md`

## Input

Andrew: "measure chi on the H2 scaffold."

This was next target 3 of the sorting-engine bridge: the fraction of physical
decoherence that reaches the decoder as syndrome is exactly \(\chi\), and the
hardware program had never measured it.

## Method

`simulations/hardware_adaptive_decoder/sorting_ledger_audit.py` imports the H2
circuit primitives unchanged — same fault model, parity-extraction circuit,
decoder policies, drift, and calibration schedule already audited for logical
error. Nothing about the scaffold was modified to accommodate the measurement.

**Probe.** At the start of a measurement window the data register is placed in
an unknown error configuration \(S_0\), uniform over the eight three-qubit
states. The window then runs ordinary H2 rounds with the protocol's real
decoder state, carried forward from round 0 of the full 96-round trace so drift
and calibration history are faithful.

**Exactness.** The joint over \((S_0,D_k,R_{\leq k})\) is propagated with all
\(4^8\) syndrome histories retained: no sampling, no pruning, no branch
merging. The 8-round window length is set by that enumeration.

**Reference split.** \(S_0\) factors bijectively into the syndrome class
\(G_0\) (two bits, the error sector) and the logical component \(L_0\) (one
bit). The identification that made the whole audit work: **the stabilizer group
is the sorter's slot partition.** For an [[n,k]] code it resolves \(n-k\) bits
against \(n\) bits of error space, so Corollary 4.2's ceiling is \((n-k)/n\),
here \(2/3\) asymptotically, with the finite-window ceiling
\(2/(J_0-J_\infty)\) reported alongside. The missing third is not waste; it is
the logical label the code is designed to be blind to.

## Result

Uniform decoder, 8-round windows:

| Window | \(\gamma\) | \(\sigma\) | \(\delta\) | \(\chi\) | ceiling | \(\chi_G\) | leak |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.00195 | 1.92876 | 0.07319 | 0.963442 | 0.99903 | 0.96438 | 0 |
| 44 | 2.29867 | 1.52677 | 0.77189 | 0.664199 | 0.87007 | 0.76339 | 0 |
| 52 | 2.39818 | 1.34780 | 1.05038 | 0.562009 | 0.83396 | 0.67390 | 0 |
| 60 | 2.28404 | 1.37541 | 0.90863 | 0.602184 | 0.87564 | 0.68771 | 0 |
| 72 | 2.04528 | 1.70805 | 0.33723 | 0.835116 | 0.97786 | 0.85402 | 0 |
| 88 | 2.00277 | 1.92233 | 0.08045 | 0.959833 | 0.99862 | 0.96117 | 0 |

Validation across all thirty protocol-window pairs: ledger identity to
`0.000e+00`, \(\sigma\leq\gamma\) never violated, \(\sigma\leq H(R\mid R)\)
never violated, zero bandwidth-limited steps.

### The main finding

**\(\chi\) is a property of the extraction circuit, not of the decoder.**

- spread across the five decoder policies: `0.00479` at window 0, `0.00215` at
  window 52;
- spread from scaling only the ancilla/readout fault rates, data-qubit noise
  held fixed: `0.142` at window 44 (`0.70558` at quarter rates, `0.56349` at
  quadruple rates);
- spread across windows of the same trace: `0.401`.

A decoder can only spend what was already sorted. This is an upstream
explanation for a result the hardware program has been circling since H0: every
adaptive-decoding scaffold so far has produced modest gains, and the ledger says
why. Likelihood adaptation cannot touch the quantity that determines how much
error information exists to decode. Corollary 4.2 makes the follow-up
prediction sharp: gauge or check-schedule adaptation, which changes the *slot
partition*, should move \(\chi\) where likelihood adaptation cannot. That is now
the strongest reason to prioritize the phase-protecting stabilizer/subsystem
step in OP-23.

### Four secondary findings

- **Adaptation overhead is a measurable charge against \(\chi\).**
  `overactive_decoder` scores `0.95939` against `0.96418` at window 0 and
  `0.95486` against `0.96100` at window 88. Characterization faults are
  contraction that produces no record — the cost appears in the right column of
  the ledger, with the right sign, without being put there by hand.
- **The H2 extraction is a perfectly selective sorter.** \(I(L_0;R\mid G_0)=0\)
  exactly, every window, every policy. Knill-Laflamme holding numerically
  rather than by assertion. In Section 8's terms the scaffold is nothing like
  `centralizing_sorter`; the only open question about it was ever efficiency.
- **What stays inside is exactly the protected label.** After eight rounds the
  retained column equals the protected column to five decimals (`0.99805` at
  window 0, `0.60182` at window 52). The sector column drains to the boundary
  and the logical component is all that remains in the register. Real syndrome
  extraction exhibits the `sort_then_contract` structure of the toy without
  having been designed to.
- **Bandwidth is not the binding constraint; noise is.** Peak \(\gamma/C\) runs
  `0.876` to `0.951` and never exceeds 1, so the alphabet bound is close but
  never active. The informative gap is \(\sigma\) against the realized record
  entropy: up to `0.278` bits at window 0 and `0.740` bits at window 52. The
  syndrome register carries about two bits per extraction round, of which up to
  three quarters of a bit is readout noise rather than error information. That
  gap is the sorter misfiling coins, and it is where the losses live.

Drift also turns out to degrade the record channel itself, not only the
decoder's estimate of it: at the drift peak near round 52, \(\chi_G=0.674\)
against a ceiling of 1, so a third of the error-sector information never reaches
the decoder at all. The adaptive-alignment program has been measuring drift's
effect on the estimate; this is drift's effect on the thing the estimate is
computed from.

## Honesty boundary

The 8-round window is forced by exact enumeration and is not a steady-state
measurement. The probe is an injected uniform error, not the memory's
stationary state, so \(\chi\) here answers "how much of a fresh unknown error
gets sorted" and not "what is the steady-state efficiency of this memory." The
[[3,1]] repetition scaffold remains what the existing H2 Pauli-frame audit
already says it is: a diagnostic rung, not a full logical-qubit memory. Nothing
here changes the logical-error results of the H2 audit; it adds a diagnostic
alongside them.

## Files

- Added `simulations/hardware_adaptive_decoder/sorting_ledger_audit.py` and
  three output CSVs.
- Added Section 13 to `bridges/crystallization_sorting_engine.md`, renumbering
  the closing sections, and marked next-target 3 done with a sharper successor.
- Added a sorting-ledger section to
  `simulations/hardware_adaptive_decoder/README.md`.
- Updated OP-16, OP-23, OP-30, and `STATUS.md`.

## Next

1. Steady-state per-cycle \(\chi\) rather than a probe window, which needs
   either pruning with a reported mass bound or an analytic fixed point.
2. Test the slot-partition prediction: gauge or check-schedule adaptation
   inside a phase-protecting stabilizer or subsystem code.
3. The two remaining OP-30 items untouched by this session: an area-derived
   capacity inside the macrocell collapse toy, and the coherent-information
   restatement of the ledger for a quantum record channel.
