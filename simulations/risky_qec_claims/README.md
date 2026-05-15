# Risk Tests for Overstrong QEC Claims

This directory tests the risky claims in the 2026-05-05 discussion output.
The purpose is adversarial: keep the useful ACP Quantum thesis while rejecting
claims that are too strong, ambiguous, or false in standard QEC language.

## Run

```bash
.venv/bin/python simulations/risky_qec_claims/risky_qec_claims.py
```

## Outputs

- `outputs/interaction_information_tests.csv`
- `outputs/syndrome_measurement_tests.csv`
- `outputs/monitoring_interval_scan.csv`
- `outputs/noisiest_qubit_tests.csv`
- `outputs/risk_audit_summary.csv`

## Current Run

The seeded deterministic audit currently reports:

| Probe | Result |
|---|---:|
| Split logical-leak synergy | `1.000000` bit |
| Split logical-leak conditional leakage | `1.000000` bit |
| Clean syndrome `I(error; syndrome)` | `0.721928` bits |
| Clean syndrome logical synergy | `0.000000` bits |
| Ideal syndrome-recovery logical coherence | `1.000000` |
| Ideal syndrome-recovery identity entanglement fidelity | `0.981824` |
| Centralizing logical-record coherence | `0.000000` |
| Centralizing logical-record identity entanglement fidelity | `0.490912` |
| Centralizing logical-record bit fidelity | `0.981824` |
| Best interval, zero backaction | `1` |
| Best interval, backaction `0.012` | `4` |
| Noisiest-qubit bare bit advantage, 24 ticks | `0.001379` |
| Quiet-qubit bare bit advantage, 24 ticks | `0.375413` |
| Noisiest-qubit syndrome MI | `0.504414` bits |

## Tests

### 1. Positive logical/noise/environment synergy is not enough

The `split_logical_leak` distribution creates two records that are separately
blind to the logical bit but jointly reveal it. It has positive

```text
I(L; A,B) - I(L; A) - I(L; B)
```

but this is logical leakage, not useful syndrome information. Conversely, the
`clean_error_syndrome` distribution has positive `I(error; syndrome)` and zero
logical synergy.

Conclusion: the safe diagnostic is not generic positive logical interaction
information. The QEC-native target is syndrome information plus conditional
logical privacy:

```text
I(error; syndrome) > 0
I(logical; record | error) ~= 0
```

### 2. Syndrome measurement is not automatically crystallization

The repetition-code test compares no recovery, ideal syndrome recovery,
partial logical-branch recording, and full logical-branch recording. Ideal
syndrome recovery improves the bit and preserves the tested `|+_L>` branch
coherence; the centralizing logical record preserves the classical bit while
destroying the superposition.

Conclusion: standard syndrome extraction is not the enemy. The enemy is
logical-state capture, excessive backaction, or overhead.

Second-pass caveat: the `|+_L>` coherence probe is not a full logical-channel
audit. Logical bit-flip failures leave `|+_L>` invariant, so the script also
reports a one-round recovered logical-channel identity entanglement fidelity.
In the current run, ideal syndrome recovery has `F_e=0.981824`, while the full
logical-branch record falls to `F_e=0.490912`.

### 3. Productive intervals require a cost model

The monitoring scan repeats the 3-qubit repetition-code memory experiment with
two monitoring models. With zero logical backaction, correcting every tick is
best. With nonzero backaction per recovery, the optimum moves to an interior
correction interval.

Conclusion: "QEC pushes to crystallization" is only true for imperfect,
centralizing, or costly monitoring. Ideal QND syndrome extraction should not be
described that way.

Second-pass caveat: terminal-horizon scans can contain divisibility artifacts,
because a correction interval may or may not land exactly on the final tick.
Future schedule tests should report a phase-averaged stopping time,
steady-state per-cycle logical channel, or both.

### 4. The noisiest qubit is not where computation should start

The noisiest-qubit test compares bare storage on three physical qubits with
rates `(0.12, 0.02, 0.02)`. The noisiest qubit can be the most informative
target for syndrome/decoder attention, but it is the worst bare storage
location.

Conclusion: salvage the claim as "prioritize calibration, routing avoidance,
decoder weighting, or gauge/schedule adaptation around the highest-coupled
subsystems," not "start the computation on the noisiest qubit."
