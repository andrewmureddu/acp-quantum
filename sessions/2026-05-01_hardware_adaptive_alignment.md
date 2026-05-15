# 2026-05-01 — Hardware Adaptive Alignment

## Context

Andrew clarified the project goal: hardware-level implementation. I promoted
that from an implied downstream ambition to the active ACP Quantum target.

The working interpretation is now:

> adaptive syndrome alignment is valuable only if it can be implemented as a
> device-facing control stack that preserves the same logical information while
> using measured hardware noise structure to improve decoding, gauge choice,
> schedule choice, or local frame updates after overhead.

## Work Completed

- Added `bridges/hardware_adaptive_alignment.md`.
- Added `simulations/hardware_adaptive_decoder/`.
- Updated `bridges/adaptive_syndrome_alignment.md` to point beyond naive axis
  switching toward fixed-code likelihood adaptation.
- Updated `STATUS.md`.
- Updated `OPEN_PROBLEMS.md`, upgrading OP-16 to Partial++ and adding OP-23.

## Hardware Bridge

The new bridge defines the hardware implementation stack:

1. physical noise stream;
2. syndrome stream;
3. online estimator;
4. update policy;
5. logical-channel audit.

It also defines the acceptance criteria for a hardware-relevant result:

- compare against fixed, static-tailored, and overactive baselines;
- preserve the same logical channel;
- count update overhead, latency, measurement error, and idle exposure;
- report logical-channel metrics, not branch population;
- avoid artificial wins under stationary noise;
- compute finite-cycle contraction diagnostics when a cycle map is available.

## First Hardware-Facing Benchmark

The new simulator keeps the physical code fixed:

- 3-qubit repetition memory;
- noisy parity-check syndrome measurements;
- drifting, non-identically distributed data-qubit bit-flip rates;
- weighted maximum-likelihood decoder;
- adaptive decoder-likelihood updates every 12 rounds;
- overactive every-round update baseline;
- exact 8-state diagonal Pauli-channel propagation.

Outputs:

- `simulations/hardware_adaptive_decoder/outputs/hardware_adaptive_decoder_scan.csv`;
- `simulations/hardware_adaptive_decoder/outputs/hardware_adaptive_decoder_heatmap.png`;
- `simulations/hardware_adaptive_decoder/outputs/hardware_adaptive_decoder_curves.png`.

First run:

- maximum adaptive benefit: `0.069` log10 units;
- location: anisotropy `1.800`, drift `0.667`;
- best observed logical error: `0.05589`, from `uniform_decoder`;
- best-protocol counts: `uniform_decoder` `600`, `static_tailored` `17`,
  `adaptive_decoder` `8`.

## Interpretation

This is not yet a hardware advantage. It is the correct cautionary scaffold.
Adaptive likelihood updates only help in a small drifting-anisotropic crossover
region. The project should treat that as discipline, not disappointment:
hardware adaptation must earn its overhead against strong static baselines.

The contraction diagnostic is intentionally severe in this first model. With
the \(Q\) sector defined as majority logical failure, worst-round \(q^*\) can
sit close to one, so the 3-bit diagonal memory is not yet an active contraction
protocol for already-failed logical sectors. The next implementation model
should either compute contraction on a better leakage/alignment sector or move
to a code/decoder where recovery genuinely contracts the relevant misalignment.

## Next

1. Optimize or vectorize the hardware-adaptive decoder scan so larger grids are
   cheap.
2. Add a hardware-data replay format: syndrome/calibration traces in, baseline
   comparison out.
3. Build a circuit-level syndrome-extraction model with data, ancilla,
   measurement, idle, leakage, and correlated fault channels.
4. Move to a small stabilizer/subsystem-code patch while preserving the same
   logical channel.
