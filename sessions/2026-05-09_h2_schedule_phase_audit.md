# 2026-05-09 — H2 Schedule-Phase Audit

## Context

The active hardware front needed a robustness check after the H2 logical-process
audit. The previous H2 scaffold already avoided single-state probes by
reporting a cumulative logical bit-flip process and terminal phase-window
metrics. The remaining risk was that a modest adaptive win could still depend
on the arbitrary phase of the calibration/update schedule.

## Work Completed

- Upgraded
  `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`.
- Generated synthetic calibration candidates for every round, so different
  calibration-offset schedules can be replayed against the same physical noise
  trajectory.
- Added a `--calibration-phase` option for generated traces and
  `--skip-phase-scan` for faster single-phase runs.
- Added `outputs/circuit_level_phase_scan_summary.csv`.
- Added schedule-phase summary columns to
  `outputs/circuit_level_decoder_summary.csv`:
  `schedule_phase_count`, `schedule_phase_mean_logical_error`,
  `schedule_phase_std_logical_error`,
  `schedule_phase_span_logical_error`,
  `schedule_phase_mean_coherent_information_bits`, and
  `schedule_phase_mean_adaptive_benefit_log10`.
- Updated `bridges/hardware_adaptive_alignment.md`,
  `simulations/hardware_adaptive_decoder/README.md`, `STATUS.md`, and
  `OPEN_PROBLEMS.md`.

## Result

The default seeded H2 stress trace remains a modest adaptive win, now with a
stricter schedule-phase audit:

- `adaptive_decoder` updates 4 times and remains best with logical error
  `0.45452`;
- best fixed/static baseline remains `uniform_decoder` at `0.46772`;
- `overactive_decoder` updates every round and gives `0.46064`;
- average \(I(\mathrm{error};\mathrm{syndrome})\) remains `0.11486` bits;
- average \(I(\mathrm{logical};\mathrm{record}\mid\mathrm{error})\) remains
  `2.7e-17` bits.

The adaptive logical-process audit now reports:

- \(p_{0\to1}=p_{1\to0}=0.45452\);
- symmetrized logical bit-flip PTM entries \(R_{XX}=1\) and
  \(R_{YY}=R_{ZZ}=0.09096\);
- terminal coherent information `0.00598` bits;
- four-round terminal phase-window logical error `0.45411`;
- four-round terminal phase-window coherent information `0.00609` bits.

The four-offset calibration schedule-phase scan reports adaptive mean logical
error `0.45761`, logical-error span `0.00867`, and mean adaptive benefit
`0.010` log10 over the best fixed/static baseline. Interpretation: the default
adaptive win is not merely a final-tick artifact, but it is still
schedule-sensitive and should remain framed as a cautionary stress-test result.

## Verification

Ran:

```bash
.venv/bin/python -m py_compile simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py
.venv/bin/python simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py --generate-example
```

## Next

1. Feed H1/H2 measured backend calibration and syndrome-event logs when
   available.
2. Replace the H2 classical bit-flip circuit with a stabilizer/Pauli-frame
   simulator so \(X\), \(Y\), and \(Z\) logical transfer entries are audited
   directly.
3. Compute true steady-state per-cycle maps after the Pauli-frame upgrade.
