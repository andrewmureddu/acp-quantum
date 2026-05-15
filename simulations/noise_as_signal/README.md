# Noise-Tailored DFS Encoding: Qiskit Alignment Simulation

This simulation tests a minimal noise-tailoring claim: when dephasing noise has
a correlated component, a symmetry-adapted decoherence-free-subspace (DFS)
encoding can preserve logical coherence while an unadapted encoding decoheres.

## Model

Two logical encodings are compared under phase noise:

```text
unaligned |+_U> = (|00> + |11>) / sqrt(2)
aligned   |+_A> = (|01> + |10>) / sqrt(2)
```

The aligned state lives in the two-qubit decoherence-free subspace for
collective dephasing. If both qubits receive the same random phase, `|01>` and
`|10>` acquire the same phase, so their relative phase survives. Independent
dephasing still destroys it.

The scan varies:

- `noise_strength`: amount of environmental coupling.
- `structure_fraction`: how much of the dephasing is collective/correlated
  rather than independent/local.

## Interpretation

- Low coupling: coherence remains, but no syndrome information is available.
- Mostly independent/local noise: logical coherence decays and the environment
  leaks the DFS logical branch.
- Mostly correlated noise: the environment carries collective-charge syndrome
  information while the DFS logical branch remains private.

## Run

```bash
.venv/bin/python simulations/noise_as_signal/noise_as_signal_qiskit.py
```

## Outputs

- `outputs/noise_as_signal_scan.csv`
- `outputs/noise_as_signal_heatmap.png`
- `outputs/noise_as_signal_curves.png`

## Metrics

- `structured_syndrome_mi_bits`: explicit Shannon
  `I(collective charge; collective environment fragment)`.
- `aligned_logical_env_mi_bits`: explicit Shannon
  `I(aligned logical branch; environment fragments)`.
- `unaligned_logical_env_mi_bits`: the same leakage metric for the unaligned
  logical branch.
- `unaligned_coherence`: true branch coherence of `( |00> + |11> ) / sqrt(2)`.
- `aligned_coherence`: true branch coherence of `( |01> + |10> ) / sqrt(2)`.
- `alignment_gain`: aligned coherence minus unaligned coherence.
- `aligned_entanglement_fidelity`: entanglement fidelity of the induced aligned
  logical dephasing channel.
- `unaligned_entanglement_fidelity`: the same logical-channel fidelity for the
  unaligned encoding.
- `aligned_coherent_information_bits`: coherent information of the induced
  aligned logical channel for a maximally mixed logical input.
- `unaligned_coherent_information_bits`: the same coherent-information metric
  for the unaligned encoding.
- `noise_tailored_score`:
  `structured_syndrome_mi_bits * aligned_coherence *
  (1 - aligned_logical_env_mi_bits)`.

The environment-fragment model is a classical Gaussian readout coupled to the
same collective and independent coordinates that define the dephasing channel.
The logical-channel metrics use the exact induced dephasing channel on each
two-branch encoding: if the coherence multiplier is `eta`, then
`F_e=(1+eta)/2` and `I_c=1-H_2((1+eta)/2)`. This is not yet a full microscopic
Stinespring environment-state or active-recovery calculation, but it removes
the earlier hand-built environmental-signal proxy and adds channel-native
memory diagnostics.

In current domain language, this is a toy example of noise-tailored encoding,
correlated-noise exploitation, and separation between detectable error-sector
information and protected logical information.

A reviewable technical write-up is available at
`bridges/quantum_noise_as_signal.md`.
