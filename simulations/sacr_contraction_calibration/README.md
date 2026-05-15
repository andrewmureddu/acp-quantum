# SACR Contraction Calibration

This simulation operationalizes the strongest finite claim in
`shadow geometry paper.docx`: an active alignment cycle should be judged by
the contraction parameters

```text
q_star = worst-case leakage-sector retention
eta_star = worst-case aligned-sector leakage
floor_bound = eta_star / (1 - q_star)
```

The calibration target associated with a 99.1% coherence floor is

```text
floor_bound <= 9e-3
```

## What This Is

The script computes `q_star` and `eta_star` directly from Kraus operators using
the Heisenberg-picture leakage effect

```text
E_Q = sum_a K_a^\dagger Q K_a
```

For a finite channel, the parameters are the largest eigenvalues of `E_Q`
restricted to the leakage sector and aligned sector respectively.

## Toy Model

The included scan uses a two-sector channel with a two-dimensional aligned
logical sector `P` and a two-dimensional leakage sector `Q`.

```text
leakage probability   ell : P -> Q
recovery probability  r   : Q -> P
q_star                    = 1 - r
eta_star                  = ell
floor_bound               = ell / r
```

This toy does not validate a hardware protocol. It is a calibration harness:
future work should replace the toy Kraus operators with the actual finite
cycle map for a syndrome-extraction, feedback, and recovery protocol.

## Run

```bash
.venv/bin/python simulations/sacr_contraction_calibration/sacr_contraction_calibration.py
```

## Outputs

- `outputs/sacr_contraction_scan.csv`
- `outputs/sacr_contraction_heatmap.png`
