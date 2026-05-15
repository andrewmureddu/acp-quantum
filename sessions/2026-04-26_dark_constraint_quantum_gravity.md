# 2026-04-26 — Dark-Constraint Quantum Gravity

## Prompt

Andrew redirected the session toward quantum gravity:

> let's work on quantum gravity. darkness provides the constraint.
>
> in a room full of mirrors, watching from above, you could watch the light find
> the fastest path. i imagine that there would be competition. competing
> predicitons.

## Work Completed

- Read `STATUS.md` and `OPEN_PROBLEMS.md` first, per project startup routine.
- Checked the existing Schur complement, restraint-power, noise-tailoring, and syndrome-coordination bridges for relevant gravitational and quantum-information anchors.
- Added `bridges/dark_constraint_quantum_gravity.md`.
- Added `simulations/dark_constraint_inference/`.
- Added OP-17 to `OPEN_PROBLEMS.md`.
- Updated `STATUS.md` with an exploratory quantum-gravity front and changelog entry.

## Main Formal Move

The prompt was translated into the following bridge variable:

$$
I(G;R_0)>0,
$$

where \(G\) ranges over candidate geometries and \(R_0\) is a structured
dark/null optical record. Darkness is treated as a null measurement rather than
as absence: a geometry is constrained not only by where photons arrive, but by
where photons do not arrive.

The mirror-room intuition was formalized as stationary-phase competition among
candidate optical histories:

$$
\mathcal A(x_o|x_s)
\approx
\sum_{\gamma}
a_\gamma \exp(i\omega T[\gamma]).
$$

In the semiclassical limit, non-stationary paths cancel and the Fermat/stationary
paths survive. The quantum-gravity lift replaces competing optical paths
\(\gamma\) with competing geometry-field histories \((g,\phi)\) constrained by
positive and null boundary records.

## Status

Added a first dependency-free optical inverse-problem simulation. A hidden
absorber blocks ray histories in a mirrored room. The inference task compares a
posterior conditioned only on positive detections against a posterior
conditioned on both positive detections and dark detector windows.

First result: structured dark windows reduce posterior uncertainty by a mean
`0.6250` bits over the hidden absorber scan. The posterior-mean localization
error improves from `0.0073` to `0.0020`. MAP localization is already saturated
by the positive-only record, so the result is an uncertainty-sharpening result
rather than a hard classification win.

This is explicitly conjectural. It does not claim to solve quantum gravity,
derive Einstein's equations, or prove cosmic censorship. Its value is that it
gives the gravitational front a channel-level object analogous to syndrome
information in QEC.

## Next Step

Upgrade the mirror-room inverse-problem simulation:

1. Replace ray-count blocking with wave interference.
2. Add moving mirrors or time-dependent obstacles.
3. Replace the hidden absorber with a weak metric perturbation / lensing field.
4. Check whether the null-record advantage survives these upgrades.
