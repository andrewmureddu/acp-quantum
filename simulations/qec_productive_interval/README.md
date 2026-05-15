# QEC Productive Interval Simulation

This is the first quantum-error-correction version of the ACP simulation.

It uses a 3-qubit bit-flip repetition code. The scan probes two initial states:

```text
|0_L> = |000>
|+_L> = (|000> + |111>) / sqrt(2)
```

`|0_L>` measures whether the code preserves a classical logical bit under
bit-flip noise. `|+_L>` measures whether the same correction schedule preserves
logical phase coherence.

The scan varies:

- `p_noise`: bit-flip probability per qubit per tick.
- `correction_interval`: how often syndrome recovery is applied.

Each correction round performs the standard repetition-code syndrome recovery.
To make the ACP double-boundary visible, the model includes a small logical
dephasing cost per recovery round. This represents imperfect monitoring:
syndrome extraction is not assumed to be free, and over-monitoring can leak or
collapse logical phase.

## ACP Interpretation

- Under-correction: bit-flip noise accumulates and the encoded state dissolves.
- Over-correction: repeated monitoring preserves the classical code subspace
  while dephasing the logical superposition, a crystallization failure.
- Productive interval: syndrome extraction is frequent enough to correct noise
  but restrained enough to preserve logical coherence.

## Run

```bash
.venv/bin/python simulations/qec_productive_interval/repetition_code_acp.py
```

## Outputs

- `outputs/repetition_code_scan.csv`
- `outputs/repetition_code_acp_heatmap.png`
- `outputs/repetition_code_acp_curves.png`

## Metrics

- `bit_fidelity`: overlap of evolved `|0_L>` with `|0_L>`.
- `bit_advantage`: logical-bit survival above random guessing,
  `max(0, 2 * bit_fidelity - 1)`.
- `plus_fidelity`: overlap of evolved `|+_L>` with `|+_L>`.
- `code_population`: population remaining in the code space spanned by
  `|000>` and `|111>`.
- `logical_coherence`: magnitude of the protected `|000><111|` coherence.
- `productive_score`: product of bit advantage, plus-state fidelity, code
  population, and logical coherence.

This is a toy model. In ideal stabilizer QEC, syndrome extraction can be
quantum non-demolition and need not dephase the logical qubit. The backaction
term here is explicitly modeling imperfect, costly monitoring so the ACP
tradeoff can be explored.
