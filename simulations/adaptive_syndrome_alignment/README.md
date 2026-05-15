# Adaptive Syndrome Alignment Benchmark

This simulation is the first QEC-native benchmark for OP-16. It tests when
adaptive syndrome-space alignment beats both standard fixed and static
noise-tailored baselines under drifting structured noise.

## Model

The memory is a 3-qubit repetition code with two possible orientations:

```text
x orientation: computational-basis repetition, corrects physical X errors
z orientation: Hadamard-rotated repetition, corrects physical Z errors
```

The physical noise is independent biased Pauli noise with fixed total strength
and a drifting X/Z bias:

```text
p_x(t) + p_z(t) = constant
b(t) = anisotropy * cos(2*pi*drift_cycles*t/T)
```

Positive bias means X-dominated noise. Negative bias means Z-dominated noise.
The current scan uses 48 memory rounds and total physical error probability
`p_x(t) + p_z(t) = 0.025` per round.

## Protocols

- `fixed_x`: always use the X-correcting orientation.
- `fixed_z`: always use the Z-correcting orientation.
- `static_tailored`: choose the initially dominant orientation and keep it.
- `adaptive_tailored`: re-estimate the dominant orientation every 12 rounds and
  switch when the bias sign changes.
- `overactive_adaptive`: re-estimate every round, paying avoidable
  characterization overhead.

The adaptive protocols include explicit characterization overhead per update
and switching overhead when the orientation changes.

## Metrics

The simulation reports the induced logical Pauli channel after the memory
experiment. The primary metrics are:

- `entanglement_fidelity`
- `logical_error = 1 - entanglement_fidelity`
- logical Pauli-transfer eigenvalues `lambda_x`, `lambda_y`, `lambda_z`
- `adaptive_benefit_log10 = log10(best_static_error / adaptive_error)`
- `overactive_penalty_log10`
- `mismatched_round_fraction`

The benchmark intentionally avoids GHZ-support or branch-population scores.

## Run

```bash
.venv/bin/python simulations/adaptive_syndrome_alignment/adaptive_alignment.py
```

## Outputs

- `outputs/adaptive_alignment_scan.csv`
- `outputs/adaptive_alignment_heatmap.png`
- `outputs/adaptive_alignment_curves.png`

## Interpretation

This is still a toy model, but it targets the mature QEC question directly:

> Adaptive alignment helps only when the accumulated logical-error penalty of
> staying statically misaligned exceeds the characterization and switching
> overhead required to track the drifting noise.

In the stationary limit, adaptive alignment should not beat a correct static
tailoring choice. If it does, the overhead model is too weak or the comparison
is unfair.

The first scan confirms the cautionary version of the claim: adaptive
axis-switching wins only in a small crossover region. The maximum observed
advantage is `0.0276` log10 units at anisotropy `0.9` and drift `0.6`, while
fixed static orientations win most of the grid. This is a useful negative
constraint: a mature protocol should adapt decoder likelihoods, gauge choices,
or local Clifford tailoring while preserving the same encoded logical channel,
not merely switch which Pauli axis a repetition code protects.
