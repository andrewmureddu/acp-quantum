# Restraint Ethics Record-Channel Simulation

This simulation tests the ACP civil-systems bridge in
`bridges/restraint_ethics.md`.

The model is intentionally small. A power-bearing institution observes a record
channel with two possible contents:

- a public error sector `E`, the thing the institution is allowed to correct;
- a protected agency/logical state `L`, the thing the institution should avoid
  capturing beyond what is necessary to correct `E`.

The ACP target is:

```text
I(E; record) > 0
I(L; record | E) approximately 0
```

with a bounded record burden.

## Model

The latent variables are binary:

```text
E in {-1, +1}
L in {-1, +1}
```

They may be correlated, representing social context in which a protected state
and a public error sector are not statistically independent. The record is a
two-dimensional Gaussian readout:

```text
Y_E = monitor_strength * (1 - leakage_fraction) * E + noise
Y_L = monitor_strength * leakage_fraction * L + noise
```

The first coordinate is syndrome-like: it targets the public error. The second
coordinate is surveillance-like: it targets the protected state.

The simulation computes deterministic Gaussian-quadrature mutual information:

- `public_error_mi_bits`: `I(E; record)`;
- `excess_agency_leakage_bits`: `I(L; record | E)`;
- `raw_agency_mi_bits`: `I(L; record)`;
- `record_burden`: a monotone cost of monitoring strength;
- `restraint_score`: `I(E; record) * (1 - I(L; record | E)) *
  exp(-alpha * monitor_strength^2)`.

## Run

```bash
.venv/bin/python simulations/restraint_ethics/restraint_ethics_monitoring.py
```

## Outputs

- `outputs/restraint_ethics_scan.csv`
- `outputs/restraint_ethics_summary.csv`
- `outputs/restraint_ethics_context_audit.csv`
- `outputs/restraint_ethics_heatmap.png`
- `outputs/restraint_ethics_curves.png`

## Interpretation

- Low monitoring strength: no usable record, the abandonment/dissolution side.
- High leakage fraction: the record captures protected agency, the
  surveillance/crystallization side.
- High monitoring strength: even clean records incur increasing burden.
- Intermediate syndrome-selective channels: the restraint interval.

The context audit varies the correlation between `E` and `L` while holding
`leakage_fraction = 0`. It shows why the bridge uses conditional leakage. Raw
`I(L; record)` can rise merely because `L` is correlated with the public error
sector, while `I(L; record | E)` stays near zero. That diagnostic is the civil
insight fed back into the quantum OP-15 target.
