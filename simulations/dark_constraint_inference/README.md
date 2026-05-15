# Dark Constraint Inference Simulation

This is the first toy simulation for `bridges/dark_constraint_quantum_gravity.md`.

The model is not quantum gravity. It is the weakest executable version of the
bridge claim:

> structured darkness is not absence; it is a null record that can constrain
> candidate geometries.

## Model

A point source illuminates a two-dimensional mirrored room. Detectors on the
ceiling count light in position bins. A hidden circular absorber blocks some
ray histories. Candidate geometries differ only in the absorber's horizontal
position.

The script compares two Bayesian observers:

- `positive_only`: conditions only on detector bins above the detection
  threshold.
- `positive_plus_dark`: conditions on the full detector record, including bins
  below the low-light threshold.

The second observer uses darkness as data.

In this toy model, "dark" means no detector bin exceeds the calibrated
low-light threshold. This represents a null record at the coarse detector
resolution, not necessarily an exact zero-photon event.

## Run

```bash
python3 simulations/dark_constraint_inference/dark_constraint_inference.py
```

## Outputs

- `outputs/dark_constraint_summary.csv`
- `outputs/dark_constraint_posterior.csv`
- `outputs/dark_constraint_posterior.svg`

## Metrics

- `positive_entropy_bits`: posterior entropy using positive detections only.
- `full_entropy_bits`: posterior entropy using detections plus dark windows.
- `null_gain_bits`: entropy reduction attributable to the null record,
  computed as `positive_entropy_bits - full_entropy_bits`.
- `positive_abs_error` / `full_abs_error`: MAP recovery error for the hidden
  absorber center.
- `positive_mean` / `full_mean`: posterior-mean estimates for the hidden
  absorber center.

The bridge prediction is:

```text
full_entropy_bits < positive_entropy_bits
```

or equivalently:

```text
null_gain_bits > 0
```

when the dark detector windows are structured by the hidden geometry.
