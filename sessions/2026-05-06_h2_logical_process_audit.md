# 2026-05-06 — H2 Logical-Process Audit

## Context

The active hardware front needed a concrete upgrade after the first H2
circuit-level syndrome-extraction scaffold. The risk audit had already shown
that single-state probes can hide logical-channel errors, so the next useful
step was to make the H2 output more process-native without pretending the
current classical bit-flip circuit is a full stabilizer/Pauli-frame simulator.

## Work Completed

- Upgraded
  `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`.
- The H2 replay now composes the physical 8-state transition matrices into a
  cumulative channel and extracts the induced logical codeword-transition
  rates after ideal final majority decoding.
- Added CSV columns for:
  `logical_p01`, `logical_p10`, `logical_bitflip_probability`,
  `logical_bitflip_asymmetry`, `logical_ptm_xx`, `logical_ptm_yy`,
  `logical_ptm_zz`, `logical_ptm_z_shift`,
  `logical_coherent_information_bits`, `phase_avg_logical_error`,
  `phase_avg_entanglement_fidelity`, and
  `phase_avg_coherent_information_bits`.
- Updated the H2 plot so the adaptive run includes a logical-process panel
  for PTM damping and coherent information.
- Regenerated the seeded H2 outputs:
  `outputs/circuit_level_noise_trace.csv`,
  `outputs/circuit_level_decoder_summary.csv`,
  `outputs/circuit_level_decoder_timeseries.csv`, and
  `outputs/circuit_level_decoder_curves.png`.
- Updated `bridges/hardware_adaptive_alignment.md`,
  `simulations/hardware_adaptive_decoder/README.md`, `STATUS.md`, and
  `OPEN_PROBLEMS.md`.

## Result

The default seeded H2 stress trace remains cautionary and stable:

- `adaptive_decoder` updates 5 times and remains best with logical error
  `0.45298`;
- the best fixed/static baseline remains `uniform_decoder` at `0.46772`;
- `overactive_decoder` remains worse than gated adaptation at `0.45940`;
- average \(I(\mathrm{error};\mathrm{syndrome})\) remains `0.11486` bits;
- average \(I(\mathrm{logical};\mathrm{record}\mid\mathrm{error})\) remains
  `2.7e-17` bits.

The new process audit for the adaptive run reports:

- \(p_{0\to1}=p_{1\to0}=0.45298\), with bit-flip asymmetry
  `5.6e-17`;
- symmetrized logical bit-flip PTM entries \(R_{XX}=1\) and
  \(R_{YY}=R_{ZZ}=0.09404\);
- terminal coherent information `0.00639` bits;
- four-round terminal phase-window logical error `0.45241`;
- four-round terminal phase-window coherent information `0.00654` bits.

Interpretation: H2 now states the modest adaptive advantage as an induced
logical-process statement, not only as a final population score. The audit is
still limited to the bit-flip component because the simulator is not yet a
full Pauli-frame/stabilizer circuit.

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
   directly rather than inferred from a symmetrized bit-flip channel.
3. Add steady-state cycle metrics after the Pauli-frame version exists.
