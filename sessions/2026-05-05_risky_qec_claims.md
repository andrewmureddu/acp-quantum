# 2026-05-05 — Risky QEC Claim Stress Tests

## Trigger

Andrew asked whether the risky or potentially incorrect parts of a
noise-tailoring interpretation could be tested directly.

## Work Done

Added `simulations/risky_qec_claims/`, an adversarial audit suite for four
overstrong claims:

1. positive logical/noise/environment synergy is automatically useful;
2. syndrome measurement is intrinsically crystallizing;
3. QEC is crystallization without specifying monitoring backaction or cost;
4. the noisiest qubit is where computation should begin.

The harness writes:

- `outputs/interaction_information_tests.csv`;
- `outputs/syndrome_measurement_tests.csv`;
- `outputs/monitoring_interval_scan.csv`;
- `outputs/noisiest_qubit_tests.csv`;
- `outputs/risk_audit_summary.csv`.

## Results

The interaction-information test gives the key correction. A split logical
record has positive logical/noise/environment synergy of `1.000000` bit, but
also conditional logical leakage of `1.000000` bit. It is not a resource; it is
a hidden logical measurement. Conversely, a clean error syndrome has
`I(error; syndrome)=0.721928` bits with zero logical synergy.

The syndrome-measurement test shows that ideal 3-qubit repetition-code
syndrome recovery preserves logical coherence (`1.000000`) and high bit
fidelity (`0.981824`) at `p_noise=0.08`. A centralizing logical-branch record
keeps the same bit fidelity but collapses logical coherence to `0.000000`.

A second pass added a logical-channel Pauli-transfer audit for the recovered
cases. This matters because the `|+_L>` branch-coherence probe is not a full
logical-channel metric: logical bit-flip failures leave `|+_L>` invariant.
Ideal syndrome recovery has identity-channel entanglement fidelity `0.981824`,
while full logical-branch recording drops it to `0.490912`.

The monitoring interval test separates ideal from costly correction. With zero
backaction, correcting every tick is best. With backaction `0.012`, the best
interval moves to `4`, matching the ACP productive-interval interpretation
only when monitoring has an explicit cost/backaction model.

The monitoring scan also revealed a design issue for future tests: a finite
terminal horizon creates divisibility artifacts when some correction intervals
land exactly on the final tick and others do not. Hardware/schedule benchmarks
should therefore report phase-averaged stopping times or steady-state
per-cycle logical channels, not only one terminal-time score.

The noisiest-qubit test uses rates `(0.12, 0.02, 0.02)`. The noisiest qubit has
the largest single-round syndrome information (`0.504414` bits) but the worst
bare 24-tick memory (`0.001379` bit advantage, compared with `0.375413` for a
quiet qubit). The safe claim is calibration/decoder/gauge priority, not
placing computation on the noisiest physical subsystem.

## Updated Claim Boundary

The safe ACP Quantum criterion is:

$$
I(\mathrm{error};\mathrm{syndrome})>0,
$$

with low excess logical leakage, e.g.

$$
I(R_L;E_{\mathrm{env}}\mid S)\approx 0,
$$

and improved induced logical-channel metrics after monitoring/adaptation
overhead. Generic positive \(I(L;N;E)\)-style language should be avoided unless
the variables are explicitly error-sector variables and logical leakage has
been audited separately.
