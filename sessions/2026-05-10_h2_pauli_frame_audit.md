# 2026-05-10 — H2 Pauli-Frame Logical-Channel Audit

## Context

The hardware-adaptive H2 scaffold already reported a cumulative logical
bit-flip process and a schedule-phase audit, but it still inferred a logical
PTM from a classical repetition-code bit-flip channel. That was useful but
incomplete: the repetition code can look acceptable in the protected bit-flip
component while accumulating unprotected phase damage.

## Work Completed

- Upgraded
  `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`.
- Added explicit phase-fault columns to generated H2 traces:
  `data_idle_z_*`, `data_gate_z_*`, `correlated_phase`, `data_crosstalk_z`,
  and `correction_phase_error`.
- Added a 64-state data Pauli-frame propagation path in parallel with the
  existing exact 8-state bit-flip propagation.
- Added output columns for logical Pauli probabilities, actual diagonal logical
  PTM entries, Pauli-channel entanglement fidelity, Pauli coherent information,
  and a bit-flip consistency check.
- Regenerated the seeded H2 outputs:
  `outputs/circuit_level_noise_trace.csv`,
  `outputs/circuit_level_decoder_summary.csv`,
  `outputs/circuit_level_decoder_timeseries.csv`,
  `outputs/circuit_level_decoder_curves.png`, and
  `outputs/circuit_level_phase_scan_summary.csv`.
- Updated `bridges/hardware_adaptive_alignment.md`,
  `simulations/hardware_adaptive_decoder/README.md`, `STATUS.md`, and
  `OPEN_PROBLEMS.md`.

## Result

The adaptive bit-flip story is unchanged:

- `adaptive_decoder` updates 4 times and remains best on the default H2 stress
  trace with logical error `0.45452`;
- the best fixed/static baseline remains `uniform_decoder` at `0.46772`;
- the bit-flip PTM audit reports `XX=1.00000`, `YY=ZZ=0.09096`, and coherent
  information `0.00598` bits;
- the four-offset schedule-phase audit still reports adaptive mean logical
  error `0.45761`, span `0.00867`, and mean benefit `0.010` log10.

The Pauli-frame audit is much harsher:

- `(pI,pX,pY,pZ)=(0.27373,0.22809,0.22643,0.27174)`;
- actual diagonal PTM `(XX,YY,ZZ)=(0.00365,0.00033,0.09096)`;
- Pauli-channel entanglement fidelity `0.27373`;
- Pauli coherent information `-0.99401` bits;
- bit-flip consistency error `4.4e-16`.

Interpretation: the earlier bit-flip audit was internally correct, but it was
not a full logical-qubit audit. The current repetition scaffold demonstrates
adaptive syndrome interpretation in one component while failing as a protected
qubit memory because phase faults are essentially unprotected.

## Verification

Ran:

```bash
.venv/bin/python -m py_compile simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py
.venv/bin/python simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py --generate-example
```

## Next

1. Feed H1/H2 measured backend calibration and syndrome-event logs when
   available.
2. Move the H2 Pauli-frame audit into a phase-protecting stabilizer or
   subsystem-code patch.
3. Compute true steady-state per-cycle maps after the phase-protecting circuit
   exists.
