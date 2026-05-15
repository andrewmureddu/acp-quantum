# Otherness-Preserving Recovery Simulation

This simulation supports `bridges/otherness_preserving_recovery.md`.

It treats a quantum error corrector as an asymmetrically powerful controller.
The controller may learn the error syndrome, but it should not learn the
protected logical branch. In QEC terms, this is the Knill-Laflamme discipline:
error information is allowed; logical information leakage is not.

## Model

The physical system is the 3-qubit bit-flip repetition code:

```text
|0_L> = |000>
|1_L> = |111>
|+_L> = (|000> + |111>) / sqrt(2)
```

Each round applies independent bit-flip noise, then a standard syndrome
recovery. After recovery, the controller may also perform a logical-branch
measurement with probability `centrality`. This final measurement represents a
centralizing intervention: it can preserve classical branch population while
destroying superposition/coherence.

The scan varies:

- `p_noise`: physical bit-flip probability per qubit;
- `centrality`: probability that the controller records the logical branch
  after syndrome recovery.

## Metrics

- `syndrome_mi_bits`: `I(error mask; syndrome)`.
- `controller_logical_leakage_bits`: branch leakage retained by the controller.
- `bit_fidelity`: survival of `|0_L>`.
- `plus_fidelity`: survival of `|+_L>`.
- `logical_coherence`: protected `|000><111|` coherence.
- `otherness_score`: syndrome information times logical survival times
  controller noncentrality.

## Run

```bash
.venv/bin/python simulations/otherness_preserving_recovery/otherness_preserving_recovery.py
```

## Outputs

- `outputs/otherness_recovery_scan.csv`
- `outputs/otherness_recovery_summary.csv`
- `outputs/otherness_recovery_heatmap.png`
- `outputs/otherness_recovery_curves.png`

## Interpretation

- No syndrome information: abandonment.
- Syndrome recovery with low centrality: otherness-preserving recovery.
- High centrality: the controller becomes the central fact of the protected
  logical system; coherence is destroyed even if classical branch survival
  looks good.

This is a toy model, but it makes the "creator/intervener" analogy operational:
the corrector is allowed to know what error occurred, not what logical state is
being protected.
