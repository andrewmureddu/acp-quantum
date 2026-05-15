# Dark Constraint Wave-Interference Simulation

This is the second toy simulation for
`bridges/dark_constraint_quantum_gravity.md`.

The first `dark_constraint_inference/` model used ray blocking by a hidden
absorber. This upgrade replaces blocking with scalar wave interference. A weak
hidden refractive bump changes optical phases in a mirrored room, shifting the
bright and dark fringes on a ceiling detector.

The model is still not quantum gravity. It tests a narrower bridge claim:

> dark interference fringes are null records that constrain candidate
> geometries.

## Model

A point source emits scalar waves in a two-dimensional mirrored room. The
ceiling detector records a one-dimensional fringe pattern. Candidate geometries
differ only in the horizontal position of a weak Gaussian refractive bump.

For each detector bin, the amplitude is a coherent sum over reflected image
paths:

```text
A(x_o|x_s,g) = sum_gamma a_gamma exp(i k S_gamma[g])
```

where the action includes a line integral through the hidden phase bump. The
detector counts are deterministic typical counts generated from a Poisson-rate
model.

Two observers infer the hidden bump location:

- `bright_only`: conditions only on bins above the brightness threshold.
- `bright_plus_dark`: conditions on the full fringe record, including bins
  below the threshold.

The second observer uses dark fringes as data.

## Run

```bash
python3 simulations/dark_constraint_wave_interference/dark_constraint_wave_interference.py
```

## Outputs

- `outputs/dark_constraint_wave_summary.csv`
- `outputs/dark_constraint_wave_posterior.csv`
- `outputs/dark_constraint_wave_fringe.csv`
- `outputs/dark_constraint_wave_posterior.svg`

## Current Result

Across the default scan of hidden bump locations, dark fringes reduce posterior
uncertainty in every case. Mean entropy reduction:

```text
dark_fringe_gain_bits = 0.1194
```

The MAP localization error is unchanged at `0.0015` because the bright-only
posterior already identifies the nearest candidate grid point in this toy.
Thus the present result is an uncertainty-sharpening result, not yet a hard
classification win.

## Metrics

- `bright_entropy_bits`: posterior entropy using bright fringes only.
- `full_entropy_bits`: posterior entropy using bright plus dark fringes.
- `dark_fringe_gain_bits`: entropy reduction attributable to dark fringes,
  computed as `bright_entropy_bits - full_entropy_bits`.
- `bright_map_abs_error` / `full_map_abs_error`: MAP localization error.
- `bright_mean_abs_error` / `full_mean_abs_error`: posterior-mean localization
  error.

The bridge prediction is:

```text
full_entropy_bits < bright_entropy_bits
```

or equivalently:

```text
dark_fringe_gain_bits > 0
```

when dark fringes are structured by the hidden geometry.
