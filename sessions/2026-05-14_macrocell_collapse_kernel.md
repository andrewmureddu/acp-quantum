# 2026-05-14 - Macrocell Collapse Kernel

## Prompt

Andrew asked what comes next and to continue the project.

## Work Completed

- Selected the next load-bearing step from the 2026-05-13 session: instantiate
  the OP-20 relational macrostate kernel in a finite semiclassical collapse
  toy.
- Upgraded `simulations/cosmic_coordination_floor/cosmic_coordination_floor.py`
  from a one-coordinate collapse model to a finite macrocell-vector model:

$$
m
=
(
M_{\partial},
J_{\partial},
Q_{\partial},
C_R,
\bar\theta_R,
\bar K_R,
A_{\partial},
N_0,
Y_{\partial}
).
$$

- Added the fourth comparison policy required by
  `bridges/relational_observable_macrostate_kernel.md`: a schematic
  `quantum_completion` kernel.
- Regenerated:
  - `simulations/cosmic_coordination_floor/outputs/cosmic_coordination_floor_timeseries.csv`
  - `simulations/cosmic_coordination_floor/outputs/cosmic_coordination_floor_summary.csv`
  - `simulations/cosmic_coordination_floor/outputs/cosmic_coordination_floor.svg`
- Updated `bridges/relational_observable_macrostate_kernel.md`,
  `bridges/cosmic_coordination_floor.md`,
  `bridges/quantum_gravity_derivation_program.md`,
  `simulations/cosmic_coordination_floor/README.md`, `STATUS.md`, and
  `OPEN_PROBLEMS.md`.

## Main Result

The toy now computes the OP-20 diagnostics directly:

$$
H_{\ell,\Delta}(m),
\qquad
I(G_\ell;R_{\partial}),
\qquad
I(L_R;R_{\partial}^{\mathrm{early}}\mid G_\ell),
\qquad
I(X_R;Y_{\partial}^{[t,t+T_{\mathrm{dec}}]}).
$$

The default run separates four policy classes:

| Policy | min \(H\) bits | min adm. mass | max sing. mass | max \(I(G;R_\partial)\) bits | max early leakage bits | final late decode bits | first floor violation |
|---|---:|---:|---:|---:|---:|---:|---:|
| naked collapse | 4.627 | 0.001 | 0.079 | 1.298 | 0.238 | 0.000 | 1 |
| hard exclusion | 0.205 | 1.000 | 0.000 | 2.101 | 0.000 | 0.000 | 22 |
| horizon transfer | 4.628 | 1.000 | 0.000 | 1.928 | 0.000 | 3.000 | none |
| quantum completion | 4.628 | 1.000 | 0.000 | 1.496 | 0.004 | 3.000 | none |

The important point is conceptual, not numerical:

1. naked collapse fails by losing admissible mass and privacy;
2. hard exclusion can keep normalization and even expose geometry records, but
   still crystallizes the future channel and emits no late decodable
   redistribution;
3. horizon transfer passes by converting collapse into finite boundary records;
4. a candidate completion must combine normalization, floor preservation,
   geometry-sector records, early privacy, and late decodability.

## Verification

- Ran `python3 simulations/cosmic_coordination_floor/cosmic_coordination_floor.py`.
- Ran `python3 -m py_compile simulations/cosmic_coordination_floor/cosmic_coordination_floor.py`.

## Honesty Boundary

This is still a finite toy, not numerical relativity and not a microscopic
quantum-gravity mechanism. It upgrades the scaffolding from a coordinate-like
collapse variable to the actual OP-20 diagnostic vector. The physics theorem is
still open.

## Next

Write the first theorem-level pass for the semiclassical collapse failure
claim: under focusing assumptions, finite relational collapse macrocells either
lose retained admissible mass, become postselected hard-exclusion channels, or
concentrate below the positive future-entropy floor unless a mechanism-changing
boundary-decodable completion is supplied.
