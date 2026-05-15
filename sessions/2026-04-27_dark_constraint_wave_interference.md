# 2026-04-27 — Dark-Constraint Wave Interference

## Prompt

Andrew asked to continue ACP quantum gravity.

## Work Completed

- Read `STATUS.md` and `OPEN_PROBLEMS.md` first, per project startup routine.
- Reopened `bridges/dark_constraint_quantum_gravity.md` and the first
  `simulations/dark_constraint_inference/` ray-count model.
- Added `simulations/dark_constraint_wave_interference/`.
- Updated `bridges/dark_constraint_quantum_gravity.md` with a wave-interference
  section.
- Updated `OPEN_PROBLEMS.md` and `STATUS.md`.

## Main Formal Move

The first dark-constraint simulation used ray blocking by a hidden absorber. The
new simulation tests the same null-record claim in a phase-sensitive setting.

A point source illuminates a mirrored room. A weak hidden refractive bump shifts
the optical action along reflected image paths:

$$
\mathcal A(x_o|x_s,g)
=
\sum_\gamma a_\gamma \exp(i k S_\gamma[g]),
$$

with

$$
S_\gamma[g]=\ell_\gamma+\int_\gamma \delta n_g(x)\,ds .
$$

Candidate geometries differ by the horizontal position of the bump. The
observed detector record is a fringe pattern. Dark bins are now produced by
destructive interference rather than by simple occlusion.

## Result

The simulation compares:

- `bright_only`: posterior conditioned only on detector bins above the dark
  threshold.
- `bright_plus_dark`: posterior conditioned on the full fringe pattern,
  including dark bins.

Default scan result:

```text
mean dark-fringe gain: 0.1194 bits
mean MAP error bright-only: 0.0015
mean MAP error bright+dark: 0.0015
mean posterior-mean error bright-only: 0.0009
mean posterior-mean error bright+dark: 0.0011
```

The entropy gain is positive in every scanned hidden-bump case. MAP localization
is unchanged because the bright-only posterior already identifies the nearest
candidate grid point. Therefore the present result is an uncertainty-sharpening
result, not yet a classification improvement.

## Status

OP-17 is now partial+: the dark-constraint bridge has both a ray-count null
record result and a wave-interference null-fringe result.

## Next Step

Upgrade the wave toy in one of two directions:

1. Add time-dependent mirror or obstacle geometry and test whether dark records
   constrain dynamical histories, not only static geometry.
2. Replace the hidden refractive bump with an explicit weak metric/lensing
   perturbation, so that the candidate variable is closer to a gravitational
   geometry sector.
