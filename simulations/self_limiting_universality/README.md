# Self-Limiting Universality Simulation

This toy simulation supports `bridges/self_limiting_universality.md`.

It does not simulate cosmology. It tests the information-channel claim behind
protected forgetting:

```text
I(needed distinction; compressor record) > 0
I(protected interior; compressor record | needed distinction) small
```

The simulation compares record policies for a dominant compressor coupled to a
needed distinction `X` and a protected remainder `L`.

## Model

Latent variables are binary:

```text
X in {-1, +1}
L in {-1, +1}
```

They may be correlated, representing a downstream semantic field where the
protected interior is statistically entangled with the needed distinction.

The compressor record has two erasure-style components plus an independent
surprise budget:

```text
R_X: reveals X with probability access_probability
R_L: reveals L with probability capture_probability
useless_noise: independent random surprise bits added to record entropy
```

`R_X` is syndrome-like access. `R_L` is totalizing capture. `useless_noise` is
surprise that increases record entropy without carrying target information.

## Metrics

- `needed_access_mi_bits`: \(I(X;R_C)\).
- `protected_leakage_cmi_bits`: \(I(L;R_C\mid X)\).
- `protected_remainder_bits`: \(H(L\mid R_C,X)\).
- `record_innovation_bits`: \(H(R_C)\).
- `structured_fraction`: \(I(X;R_C)/H(R_C)\).
- `self_limiting_score`: needed access times protected remainder times
  structured fraction, with a small record-burden penalty.

The policy audit includes `pretended_forgetting`: the public record looks
restrained, but the compressor internally captures `L`. The public score is
high while the internal score collapses, which is the operational distinction
between protected and merely pretended forgetting.

## Run

```bash
.venv/bin/python simulations/self_limiting_universality/self_limiting_universality.py
```

## Outputs

- `outputs/self_limiting_scan.csv`
- `outputs/self_limiting_summary.csv`
- `outputs/self_limiting_policies.csv`
- `outputs/self_limiting_noise_floor.csv`
- `outputs/self_limiting_heatmap.png`
- `outputs/self_limiting_noise_floor.png`

## Current Run

The seeded deterministic run currently reports:

| Probe | Result |
|---|---:|
| Grid points | `10201` |
| Max self-limiting score | `0.899316` |
| Max-score access probability | `1.000000` |
| Max-score capture probability | `0.000000` |
| Protected-forgetting policy internal score | `0.399800` |
| Total-possession policy internal score | `0.000000` |
| Noisy-dissolution policy internal score | `0.000000` |
| Pretended-forgetting public score | `0.399800` |
| Pretended-forgetting internal score | `0.000000` |

## Interpretation

- No record: the compressor cannot learn the needed distinction.
- Useless surprise: record entropy rises but target-bearing structure does not.
- Total possession: the protected interior is captured and downstream
  remainder collapses.
- Protected forgetting: the compressor learns `X` while leaving nonzero
  protected remainder in `L`.
