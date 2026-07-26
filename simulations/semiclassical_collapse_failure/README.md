# Semiclassical Collapse Failure: Numerical Check

Numerical verification for `bridges/semiclassical_collapse_failure.md`, which
proves the Stage 2 / Stage B collapse failure theorem named in
`bridges/quantum_gravity_derivation_program.md` and
`bridges/cosmic_coordination_floor.md`.

Unlike `simulations/cosmic_coordination_floor/`, this is **not** a schematic
stochastic model. It integrates the exact kinematics of a geodesic congruence
and measures the coarse-grained future entropy directly, so the theorem's
inequalities can be checked rather than illustrated.

## Model

A bundle of neighbouring timelike geodesics is described by the Jacobi
deviation matrix `J(tau)`:

```text
Jddot = -Rtidal(tau) J,     J(0) = I,    Jdot(0) = (theta0/3) I + sigma0
```

with expansion tensor `B = Jdot J^{-1}`, expansion `theta = tr(B)`, and volume
element `detJ`. Taking the trace of `Bdot = -Rtidal - B^2` reproduces the
Raychaudhuri equation identically, so this is congruence kinematics rather than
an analogy.

The source is self-consistent pressureless dust: mass conservation gives
`rho = rho0/detJ`, hence `tr(Rtidal) = kappa/detJ >= 0`, so the strong energy
condition (F1) holds throughout by construction. An optional constant traceless
Weyl-like tidal term adds anisotropy without affecting the trace, hence without
affecting the energy condition.

The coarse entropy is measured by mapping 20 000 points sampled from the
initial unit ball through `J(tau)`, binning at resolution `ell = 0.10`, and
averaging over four random grid offsets so the result is not an artifact of
where the partition falls.

## Run

```bash
python3 simulations/semiclassical_collapse_failure/collapse_entropy_decay.py
```

Pure standard library; no third-party dependencies. Runtime is roughly 15
seconds.

## Outputs

- `outputs/collapse_entropy_timeseries.csv`
- `outputs/collapse_failure_summary.csv`

## Scenarios

All focusing runs start at `theta0 = -0.60`, so `alpha = 0.60` and the Lemma 2
bound is `tau_caustic <= 3/alpha = 5.0`. The floor is `1.50` bits, matching the
`cosmic_coordination_floor` toy.

| scenario | sigma0 | H_final bits | slope bits/tau | Thm A bound | tau floor breach | tau caustic | max c in (R) regime |
|---|---:|---:|---:|---:|---:|---:|---:|
| `isotropic` | 0.00 | 0.000 | −5.563 | −0.866 | 1.8621 | 1.8717 | 9.09 |
| `moderate_shear` | 0.12 | 4.221 | −4.477 | −0.866 | none | 1.7294 | 23.0 |
| `strong_shear` | 0.45 | 8.095 | −3.920 | −0.866 | none | 0.9868 | 251.8 |
| `unbound_expansion` | 0.00 | 14.220 | +0.376 | n/a | none | none | 1.086 |

Initial entropy is 11.963 bits in every run.

## Validation

For the isotropic case the model reduces to `addot = -kappa/(3 a^2)`, whose
collapse time is available in closed form. The analytic value is `1.871746`;
the simulation gives `1.8717`.

## What the numbers show

1. **Theorem C holds in every focusing run.** All three collapse scenarios
   reach a caustic well inside the bound `3/alpha = 5.0`, so the normalization
   branch fires universally.
2. **Theorem A's bound is valid but conservative.** Measured decay slopes are
   4.5–6.4x steeper than the guaranteed `-alpha/ln2 = -0.866` bits per unit
   proper time, because self-consistent dust drives `theta` far below `-alpha`
   instead of holding it at its initial value.
3. **The entropy branch alone is not robust.** Only the isotropic run breaches
   the floor before frame breakdown. Under shear the coarse entropy is still
   4.2 and 8.1 bits at the caustic.
4. **The shear trade-off (Proposition D) is confirmed.** Across
   `sigma0 = 0.00, 0.12, 0.45` the caustic time falls monotonically
   (`1.8717 -> 1.7294 -> 0.9868`) while final entropy rises monotonically
   (`0.000 -> 4.221 -> 8.095`).
5. **Hypothesis (R) fails under shear.** The shape constant starts at `1.086`
   and stays there for the isotropic control, but reaches `251.8` under strong
   shear while the image still has more than one cell of volume. This is
   tracked as OP-30.
6. **The control behaves.** The unbound run has no focusing, constant
   `c = 1.086`, and monotonically growing entropy, confirming that focusing —
   not coarse-graining as such — drives the decay.

## Caveats

- The measured initial entropy `11.963` bits is sample-limited; the ceiling is
  `log2(20000) = 14.29` bits. Initial entropies are therefore underestimates
  and the unbound control's final value is a lower bound. No conclusion depends
  on absolute level, only on decay toward zero.
- Near the caustic `theta` diverges, so the integrator shrinks its step to keep
  the fractional volume change per step below 5%. A fixed step jumps straight
  through the singular point and re-emerges with `detJ > 0`, which is an
  artifact rather than a continuation; the caustic trigger is therefore placed
  on `theta`, which is monotone under the focusing hypotheses.
- This is congruence kinematics with a homogeneous dust source, not numerical
  relativity.
