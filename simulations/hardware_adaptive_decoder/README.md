# Hardware Adaptive Decoder Benchmark

This is the first hardware-facing ACP Quantum benchmark for OP-16. It keeps the
logical encoding fixed and adapts only the decoder likelihoods used to interpret
noisy syndrome measurements.

The goal is to move beyond naive X/Z axis switching. A real device should not
claim logical-memory improvement by changing the protected logical channel. It
should preserve the same encoded information while using measured hardware noise
structure to decode better.

## Model

The memory is a 3-qubit bit-flip repetition code with two measured parity
checks:

```text
s_01 = d_0 xor d_1
s_12 = d_1 xor d_2
```

Each round has:

- drifting, non-identically distributed data-qubit bit-flip rates;
- noisy syndrome measurements;
- a weighted maximum-likelihood one-round decoder;
- optional characterization overhead when the decoder is updated.

The physical code is fixed across all protocols. The adaptation variable is the
decoder's estimate of the three data-qubit error rates.

## Protocols

- `uniform_decoder`: fixed decoder with identical data-qubit error weights.
- `static_tailored`: decoder weights calibrated at the first round and then
  held fixed.
- `adaptive_decoder`: decoder weights updated every 12 rounds with a lagged
  calibration model and explicit characterization overhead.
- `overactive_decoder`: decoder weights updated every round, paying avoidable
  characterization overhead.
- `oracle_decoder`: instant-rate diagnostic using the true current data-qubit
  error rates without overhead. It is not a globally optimal multi-round
  decoder.

## Metrics

The H0/H1 simulations propagate the exact 8-state diagonal bit-flip channel,
rather than sampling trajectories. The H2 circuit-level scaffold also propagates
a 64-state data Pauli frame for a diagonal logical Pauli-channel audit. It
reports:

- `logical_error`: final probability of majority data-qubit failure;
- `entanglement_fidelity = 1 - logical_error` for the induced logical bit-flip
  channel;
- H2 logical-process columns:
  `logical_p01`, `logical_p10`, `logical_bitflip_probability`,
  `logical_bitflip_asymmetry`, `logical_ptm_xx`, `logical_ptm_yy`,
  `logical_ptm_zz`, and `logical_coherent_information_bits`;
- H2 Pauli-frame columns:
  `pauli_logical_p_i`, `pauli_logical_p_x`, `pauli_logical_p_y`,
  `pauli_logical_p_z`, `pauli_logical_ptm_xx`, `pauli_logical_ptm_yy`,
  `pauli_logical_ptm_zz`, `pauli_logical_entanglement_fidelity`,
  `pauli_logical_coherent_information_bits`, and
  `pauli_bitflip_consistency_error`;
- H2 phase-window columns:
  `phase_avg_logical_error`, `phase_avg_entanglement_fidelity`, and
  `phase_avg_coherent_information_bits`, plus Pauli-frame phase-window
  analogues;
- H2 schedule-phase columns:
  `schedule_phase_mean_logical_error`,
  `schedule_phase_span_logical_error`,
  `schedule_phase_mean_coherent_information_bits`, and
  `schedule_phase_mean_adaptive_benefit_log10`, plus Pauli-frame schedule
  means;
- `adaptive_benefit_log10 = log10(best_static_error / adaptive_error)`;
- `overactive_penalty_log10`;
- `oracle_gap_log10`, the gap to the instant-rate diagnostic;
- `avg_l1_estimation_error`;
- `worst_q_star`, `worst_eta_star`, and `worst_alignment_floor`.

The last three are the classical diagonal version of the finite-cycle
contraction calibration in `bridges/sacr_contraction_calibration.md`, with
the correctable sector \(P\) defined as states of Hamming weight 0 or 1 and the
logical-failure sector \(Q\) defined as states of Hamming weight 2 or 3.

## Run

```bash
.venv/bin/python simulations/hardware_adaptive_decoder/hardware_adaptive_decoder.py
```

To run the H1 replay scaffold on a hardware-style trace:

```bash
.venv/bin/python simulations/hardware_adaptive_decoder/hardware_replay_decoder.py --generate-example
```

The replay trace format has one row per correction round. The required channel
columns are `channel_p0`, `channel_p1`, `channel_p2`, and `channel_meas`; the
controller-visible calibration columns are `calib_p0`, `calib_p1`, `calib_p2`,
`calib_meas`, and `calibration_fresh`. Optional `syndrome_rate_01` and
`syndrome_rate_12` columns record measured parity-event rates. For real backend
logs, the `channel_*` columns should be the best reconstructed per-round
physical channel used for offline logical-channel replay; the controller policy
only sees the `calib_*` and syndrome-rate fields.

To run the H2 circuit-level syndrome-extraction scaffold:

```bash
.venv/bin/python simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py --generate-example
```

The H2 trace expands each round into explicit fault columns: data idling,
data-gate faults, ancilla-gate faults, ancilla preparation error, measurement
error, leakage-like random records, correlated gate faults, crosstalk, and
feedback error. The decoder still sees only compressed calibration likelihoods;
the circuit-level columns are for offline logical-channel and record audits.
For generated traces, the script also replays all calibration schedule offsets
unless `--skip-phase-scan` is passed.

## Outputs

- `outputs/hardware_adaptive_decoder_scan.csv`
- `outputs/hardware_adaptive_decoder_heatmap.png`
- `outputs/hardware_adaptive_decoder_curves.png`
- `outputs/hardware_replay_trace.csv`
- `outputs/hardware_replay_summary.csv`
- `outputs/hardware_replay_timeseries.csv`
- `outputs/hardware_replay_curves.png`
- `outputs/circuit_level_noise_trace.csv`
- `outputs/circuit_level_decoder_summary.csv`
- `outputs/circuit_level_decoder_timeseries.csv`
- `outputs/circuit_level_decoder_curves.png`
- `outputs/circuit_level_phase_scan_summary.csv`

## First Run

Default scan: 25 anisotropy values by 25 drift values, with five protocols per
grid point.

Current output:

- maximum adaptive benefit: `0.069` log10 units at anisotropy `1.800` and
  drift `0.667`;
- best observed logical error: `0.05589`, from `uniform_decoder` at anisotropy
  `1.800` and drift `0.000`;
- best-protocol counts over the grid: `uniform_decoder` won `600` points,
  `static_tailored` won `17`, and `adaptive_decoder` won `8`.

This is a cautionary first result. Adaptive likelihood updates do not win
generically. They only help in a small drifting-anisotropic crossover region,
and the gain is modest. That is useful: a hardware implementation has to earn
its overhead against strong static baselines.

## Interpretation

This is still not a fault-tolerant surface-code result. It is a first
device-stack scaffold:

- fixed code;
- noisy syndrome stream;
- decoder-likelihood adaptation;
- explicit update overhead;
- logical-channel output;
- contraction-floor diagnostics.

The next hardware-grade step is to replace the synthetic drifting rates with
calibrated or measured syndrome-event statistics from an actual backend, then
repeat the same baseline comparison without changing the logical channel.

## H1 Replay Scaffold

The replay harness adds the first hardware-data interface. The included
synthetic trace is not a hardware claim; it is a file-format and policy test
for measured calibration streams.

Default replay result over a 96-round synthetic trace:

- `uniform_decoder` remains best with logical error `0.15504`;
- stale `static_tailored` fails under drift with logical error `0.38631`;
- gated `adaptive_decoder` updates `4` times and improves the stale tailored
  decoder to logical error `0.17826`;
- `overactive_decoder` updates every round and falls to logical error
  `0.21512`, exposing avoidable overhead;
- average single-round \(I(\mathrm{error};\mathrm{syndrome})\) is `0.22624`
  bits in the trace.

This is again cautionary. Adaptive replay repaired stale calibration, but it
did not beat the simpler fixed-uniform decoder on the example trace. The next
useful step is to feed the same harness measured calibration/syndrome logs or a
circuit-level trace with ancilla, idle, leakage, and correlated-fault columns.

## H2 Circuit-Level Scaffold

The circuit-level harness adds the next roadmap rung. It still uses the same
3-qubit repetition memory, but each round explicitly models two ancilla parity
checks:

```text
prepare a_01 -> CNOT d_0,a_01 -> CNOT d_1,a_01 -> measure a_01
prepare a_12 -> CNOT d_1,a_12 -> CNOT d_2,a_12 -> measure a_12
```

Faults include data idle flips, data idle phase faults, data and ancilla gate
flips, data gate phase faults, correlated data-ancilla faults, correlated
phase faults, crosstalk on the nonparticipating data qubit, preparation error,
measurement error, leakage-like random records, correction failure, and
correction-induced phase faults. The adaptive policy changes only the decoder
likelihoods; it never changes the code or protected logical channel.

Default H2 stress trace over 96 rounds:

- `adaptive_decoder` updates `4` times and is best, with logical error
  `0.45452`;
- `uniform_decoder` gives logical error `0.46772`;
- stale `static_tailored` gives logical error `0.47317`;
- `overactive_decoder` updates every round and falls to `0.46064`;
- the cumulative induced logical bit-flip channel is symmetric to numerical
  precision, with adaptive `logical_bitflip_asymmetry` `0.0`;
- adaptive logical PTM entries are `XX=1.00000` and
  `YY=ZZ=0.09096`, with coherent information `0.00598` bits;
- the Pauli-frame logical-channel audit reports
  `(pI,pX,pY,pZ)=(0.27373,0.22809,0.22643,0.27174)`, actual diagonal PTM
  `(XX,YY,ZZ)=(0.00365,0.00033,0.09096)`, and coherent information
  `-0.99401` bits;
- the 4-round terminal phase-window audit gives adaptive
  `phase_avg_logical_error` `0.45411` and phase-averaged coherent information
  `0.00609` bits;
- the four-offset calibration schedule-phase scan gives adaptive mean logical
  error `0.45761`, logical-error span `0.00867`, and mean benefit `0.010`
  log10 over the best fixed/static baseline; the Pauli-frame schedule mean is
  `0.72781` logical-Pauli error with coherent information `-0.99476` bits;
- average circuit-level \(I(\mathrm{error};\mathrm{syndrome})\) is `0.11486`
  bits;
- average controller-record leakage
  \(I(\mathrm{logical};\mathrm{record}\mid\mathrm{error})\) is
  `2.7e-17` bits.

The default-phase gain is modest: `0.012` log10 over the best fixed/static
baseline, and the schedule-phase mean is smaller still. That is the point. In a
circuit-level stress trace, adaptation can help, but only after overhead, only
with schedule-phase robustness, and only if the controller record remains
syndrome-informative rather than logical-state-informative.

The Pauli-frame audit is the harsher result. The repetition memory can still
show a small adaptive advantage in the protected bit-flip component while the
full logical Pauli channel is badly phase-damaged. That does not invalidate the
adaptive-alignment scaffold; it says the next serious H2 step is a code or
gauge with phase protection, not a stronger claim about the current repetition
memory.
