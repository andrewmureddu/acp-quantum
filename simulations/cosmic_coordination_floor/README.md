# Cosmic Coordination Floor Toy Model

This is the first executable toy for
`bridges/cosmic_coordination_floor.md` and
`bridges/singularity_inadmissibility.md`, now upgraded to instantiate the
finite macrocell target in `bridges/relational_observable_macrostate_kernel.md`.

It is not a gravitational simulation. It is a finite stochastic model of the
ACP selection rule.

## Model

The simulation tracks a finite relational macrocell vector:

```text
(M_boundary, J_boundary, Q_boundary,
 C_R, theta_R, K_R, A_boundary, N_0, Y_boundary)
```

where `C_R` is compactness, `theta_R` is coarse expansion, `K_R` is a
curvature-density diagnostic, `A_boundary` is a finite boundary/horizon-area
bin, `N_0` is a structured null-record bin, and `Y_boundary` is an outgoing
radiation/boundary-record bin. Classical self-reinforcement increases
compactness, drives expansion negative, raises curvature, and narrows the
transition kernel.

Four policies are compared:

- `naked_collapse`: allows probability mass to leak into the singular state.
- `hard_exclusion`: removes singular histories and renormalizes the admissible
  remainder, but does not redistribute coordination.
- `horizon_transfer`: triggers near the floor, moves mass away from the
  singular boundary, and emits decodable exterior records.
- `quantum_completion`: triggers earlier as a schematic candidate completion,
  keeps the channel normalized, emits geometry-sector boundary records,
  suppresses early logical leakage, and releases late decodable information.

A second script, `raychaudhuri_floor_check.py`, is the numerical companion to
`proofs/semiclassical_collapse_failure.md`. It checks the theorem's three
quantitative claims in a finite ensemble:

1. **Lemma 1 focusing bound:** null Raychaudhuri integration with random
   NEC-respecting shear/Ricci terms diverges no later than the comparison
   bound `lambda* <= 2/alpha` (and the tighter `2/|theta0|`), sample by
   sample.
2. **Theorem 1(a) normalization failure:** the retained admissible mass
   `Z(Delta)` is monotone nonincreasing, strictly below 1 past the earliest
   failure time, and exactly 0 at `Delta*`.
3. **Theorem 1(b)-(c) exclusion/absorption failures:** the hard-exclusion
   channel's discarded coordination `-log2 Z` diverges while its surviving
   renormalized distribution concentrates (entropy collapse), and the
   terminal-absorption channel has exactly zero future entropy.

## Run

```bash
python3 simulations/cosmic_coordination_floor/cosmic_coordination_floor.py
python3 simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py
```

## Outputs

- `outputs/cosmic_coordination_floor_timeseries.csv`
- `outputs/cosmic_coordination_floor_summary.csv`
- `outputs/cosmic_coordination_floor.svg`
- `outputs/raychaudhuri_focusing_check.csv`
- `outputs/raychaudhuri_mass_loss.csv`
- `outputs/raychaudhuri_floor_check.svg`

## Metrics

- `future_entropy_bits`: entropy of the next admissible macrostate
  distribution.
- `admissible_mass`: probability mass remaining in the admissible state space.
- `singular_mass`: probability mass leaking into the inadmissible singular bin.
- `geometry_record_mi_bits`: mutual information between the geometry sector and
  finite boundary/null records.
- `early_privacy_leakage_bits`: toy conditional leakage of protected interior
  information into early records.
- `late_decodable_bits`: single-step decodable information emitted to the
  exterior record.
- `cumulative_late_decodable_bits`: accumulated late-decoding proxy, capped by
  the interior label entropy.
- `floor_violation`: whether the policy violates the toy coordination floor.
- `privacy_violation`: whether early protected-interior leakage exceeds the toy
  privacy threshold.

## Current Result

With the default parameters, `naked_collapse` fails by losing admissible mass
and leaking protected interior information, `hard_exclusion` keeps mass
normalized but eventually violates the future-entropy floor, and the two repair
policies preserve normalization, keep early privacy below threshold, and emit
late decodable boundary information.

Default summary:

```text
hard_exclusion: min_H=0.205, min_adm=1.000, max_sing=0.000, max_I_G_R=2.101, max_priv=0.000, final_I_late=0.000, first_floor=22, first_privacy=-1
horizon_transfer: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.928, max_priv=0.000, final_I_late=3.000, first_floor=-1, first_privacy=-1
naked_collapse: min_H=4.627, min_adm=0.001, max_sing=0.079, max_I_G_R=1.298, max_priv=0.238, final_I_late=0.000, first_floor=1, first_privacy=1
quantum_completion: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.496, max_priv=0.004, final_I_late=3.000, first_floor=-1, first_privacy=-1
```

Default `raychaudhuri_floor_check.py` result (seeded):

```text
focusing samples: 400
lambda* <= 2/alpha violations: 0
lambda* <= 2/|theta0| violations: 0
Z(Delta) monotone nonincreasing: True
Z(Delta*) = 0.000000
exclusion entropy: 3.6174 bits (early) -> 0.0000 bits (last surviving grid point)
absorption channel future entropy: 0.000000 bits by construction
```
