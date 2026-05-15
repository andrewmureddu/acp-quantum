# 2026-05-05 — H2 Circuit-Level Syndrome Extraction

## Context

The active ACP Quantum front is hardware-level adaptive syndrome alignment. H0
provided an exact diagonal fixed-code decoder-likelihood benchmark, and H1
added a replay interface for per-round calibration/channel traces. The next
roadmap rung was H2: replace the abstract per-round data-error model with an
explicit syndrome-extraction circuit while preserving the same logical channel
and adding a controller-record leakage audit.

## Work Completed

- Added `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`.
- Added seeded H2 outputs:
  `outputs/circuit_level_noise_trace.csv`,
  `outputs/circuit_level_decoder_summary.csv`,
  `outputs/circuit_level_decoder_timeseries.csv`, and
  `outputs/circuit_level_decoder_curves.png`.
- Updated `simulations/hardware_adaptive_decoder/README.md`.
- Updated `bridges/hardware_adaptive_alignment.md`.
- Updated `STATUS.md` and `OPEN_PROBLEMS.md` for OP-16 and OP-23.

## Model

The H2 scaffold keeps the same 3-qubit repetition memory but expands each
round into explicit parity extraction:

```text
prepare a_01 -> CNOT d_0,a_01 -> CNOT d_1,a_01 -> measure a_01
prepare a_12 -> CNOT d_1,a_12 -> CNOT d_2,a_12 -> measure a_12
```

The synthetic circuit fault model includes:

- data idling faults;
- data and ancilla gate faults;
- correlated data-ancilla faults;
- crosstalk on the nonparticipating data qubit;
- preparation error;
- measurement error;
- leakage-like random records;
- correction failure.

The adaptive policy only updates decoder likelihoods. It does not change the
code, reset the data, reencode the logical state, or switch the protected
logical channel.

## Default H2 Result

The default seeded trace is a synthetic stress trace, not a hardware result.

Over 96 rounds:

- `adaptive_decoder` updated 5 times and was best, with logical error
  `0.45298`;
- `uniform_decoder` gave logical error `0.46772`;
- stale `static_tailored` gave logical error `0.47317`;
- `overactive_decoder` updated every round and gave logical error `0.45940`;
- the adaptive benefit over the best fixed/static baseline was `0.014` log10;
- average \(I(\mathrm{error};\mathrm{syndrome})\) was `0.11486` bits;
- average \(I(\mathrm{logical};\mathrm{record}\mid\mathrm{error})\) was
  `2.7e-17` bits.

Interpretation: the circuit-level stress trace shows a real but modest
adaptive advantage after overhead. The more important result is methodological:
the scaffold now tests both syndrome informativeness and logical noncentrality
of the controller record.

## Verification

Ran:

```bash
.venv/bin/python -m py_compile simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py
.venv/bin/python simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py --generate-example
```

## Next

1. Feed H1/H2 measured backend calibration and syndrome-event logs when
   available.
2. Upgrade H2 from a classical bit-flip circuit to a stabilizer/Pauli-frame
   circuit with data and ancilla Pauli faults.
3. Replace the induced logical bit-flip metric with a fuller logical PTM or
   small process reconstruction.
4. Use phase-averaged or steady-state cycle metrics to avoid terminal-time
   schedule artifacts.
