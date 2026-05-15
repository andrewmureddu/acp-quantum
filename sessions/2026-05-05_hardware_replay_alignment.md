# 2026-05-05 — Hardware Replay Alignment

## Context

The active ACP Quantum front is hardware-level adaptive syndrome alignment. The
previous H0 scaffold kept a 3-qubit repetition memory fixed and adapted only
decoder likelihoods under synthetic drifting, non-iid data-qubit rates. The
next roadmap rung was H1: define a replay path for calibration/syndrome traces
so measured backend logs can later be tested without changing the logical
channel.

## Work Completed

- Added `simulations/hardware_adaptive_decoder/hardware_replay_decoder.py`.
- Extended `hardware_adaptive_decoder.py` so one-round transitions can accept a
  per-round true measurement-error rate while preserving the old default.
- Added seeded replay outputs:
  `outputs/hardware_replay_trace.csv`,
  `outputs/hardware_replay_summary.csv`,
  `outputs/hardware_replay_timeseries.csv`, and
  `outputs/hardware_replay_curves.png`.
- Updated `simulations/hardware_adaptive_decoder/README.md`.
- Updated `bridges/hardware_adaptive_alignment.md`.
- Updated `STATUS.md` and `OPEN_PROBLEMS.md` for OP-16 and OP-23.

## Replay Interface

The replay trace separates the reconstructed physical channel from the
controller-visible record.

Physical channel columns:

- `channel_p0`
- `channel_p1`
- `channel_p2`
- `channel_meas`

Controller-visible columns:

- `calib_p0`
- `calib_p1`
- `calib_p2`
- `calib_meas`
- `calibration_fresh`
- optional `syndrome_rate_01`
- optional `syndrome_rate_12`

The replay uses the reconstructed channel for the offline logical-channel
audit, but decoder policies only update from the calibration/syndrome record.
This keeps the hardware discipline intact: no policy can win by reading hidden
physical truth or by changing the protected logical channel.

## Default Replay Result

The default seeded trace is synthetic and should not be read as hardware data.
It is a file-format and acceptance-test scaffold.

Over 96 rounds:

- `uniform_decoder` remained best: logical error `0.15504`;
- stale `static_tailored` failed under drift: logical error `0.38631`;
- gated `adaptive_decoder` updated 4 times and improved stale tailoring to
  logical error `0.17826`;
- `overactive_decoder` updated every round and fell to logical error `0.21512`;
- the average single-round syndrome information was `0.22624` bits.

Interpretation: adaptive replay repaired a stale calibration failure but did
not beat the fixed uniform decoder on this trace. This is the correct standard:
adaptation has to beat fixed and static-tailored baselines after overhead, not
merely improve a weak stale baseline.

## Verification

Ran:

```bash
.venv/bin/python simulations/hardware_adaptive_decoder/hardware_replay_decoder.py --generate-example
.venv/bin/python simulations/hardware_adaptive_decoder/hardware_adaptive_decoder.py
```

The original H0 scan reproduced its previous headline values:

- maximum adaptive benefit `0.069` log10 at anisotropy `1.800`, drift `0.667`;
- best logical error `0.05589` from `uniform_decoder`;
- best-protocol counts: `uniform_decoder` 600, `static_tailored` 17,
  `adaptive_decoder` 8.

## Next

1. Replace the seeded trace with measured backend calibration/syndrome logs.
2. Add circuit-level trace columns: ancilla preparation, CNOT/CZ schedule,
   measurement, idle exposure, leakage, and correlated faults.
3. Add a controller-record audit for logical-state leakage once the replay
   includes explicit record registers rather than only rate logs.
