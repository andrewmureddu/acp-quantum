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

## Run

```bash
python3 simulations/cosmic_coordination_floor/cosmic_coordination_floor.py
```

## Outputs

- `outputs/cosmic_coordination_floor_timeseries.csv`
- `outputs/cosmic_coordination_floor_summary.csv`
- `outputs/cosmic_coordination_floor.svg`

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
hard_exclusion: min_H=0.205, min_adm=1.000, max_sing=0.000, max_I_G_R=2.101, max_priv=0.000, max_I_clock_R=0.000, clock_release=-1, final_I_late=0.000, first_floor=22, first_privacy=-1
horizon_transfer: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.928, max_priv=0.000, max_I_clock_R=0.000, clock_release=7, final_I_late=3.000, first_floor=-1, first_privacy=-1
leaky_completion: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.496, max_priv=0.004, max_I_clock_R=0.210, clock_release=6, final_I_late=3.000, first_floor=-1, first_privacy=9
naked_collapse: min_H=4.627, min_adm=0.001, max_sing=0.079, max_I_G_R=1.298, max_priv=0.238, max_I_clock_R=0.000, clock_release=-1, final_I_late=0.000, first_floor=1, first_privacy=1
quantum_completion: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.496, max_priv=0.004, max_I_clock_R=0.000, clock_release=6, final_I_late=3.000, first_floor=-1, first_privacy=-1
```

## Interior Clock Register (G1/G2 test)

The interior microstate is now an explicit clock: a phase `theta` in `Z_8`
with uniform prior, advancing one bin per step. This implements the
checkable prediction of `bridges/boundary_records_interior_time.md`:

- **Corollary G1 (interior clock censorship):** every admissible policy
  keeps `I(Theta; boundary record)` at exactly `0.000` bits for the whole
  run, while still carrying `I(geometry; record) ~ 1.5-2.1` bits. The
  boundary reads geometry-sector tempo, never the interior clock.
- **Corollary G2 (time release = information release):** the interior
  clock first becomes boundary-readable through the late decodable channel
  at the transfer step (`quantum_completion` step 6, `horizon_transfer`
  step 7) - the same step interior information is released, and what is
  decoded is the phase frozen at absorption.
- **The diagnostic has teeth:** the new `leaky_completion` control policy
  writes the clock parity into its transfer record; it shows
  `I(Theta; record) = 0.210` bits with leak onset at exactly its trigger
  step and is flagged as a privacy violation (step 9). An early-clock-
  reading channel is inadmissible even though it satisfies the entropy
  floor and normalization.
- `naked_collapse` leaks the interior through lost singular mass, not
  through the record channel: its clock-record MI stays zero while its
  privacy leakage is maximal - the two failure routes are now visibly
  distinct.
