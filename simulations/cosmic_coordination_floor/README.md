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
hard_exclusion: min_H=0.205, min_adm=1.000, max_sing=0.000, max_I_G_R=2.101, max_priv=0.000, final_I_late=0.000, first_floor=22, first_privacy=-1
horizon_transfer: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.928, max_priv=0.000, final_I_late=3.000, first_floor=-1, first_privacy=-1
naked_collapse: min_H=4.627, min_adm=0.001, max_sing=0.079, max_I_G_R=1.298, max_priv=0.238, final_I_late=0.000, first_floor=1, first_privacy=1
quantum_completion: min_H=4.628, min_adm=1.000, max_sing=0.000, max_I_G_R=1.496, max_priv=0.004, final_I_late=3.000, first_floor=-1, first_privacy=-1
```

---

# Area-Derived Record Capacity

`area_capacity_ledger.py` measures the sorting-engine ledger on this toy's own
kernel and calibrates the boundary capacity against the Bekenstein-Hawking area
law. It is the executable companion to Conjecture SE-1 of
`bridges/crystallization_sorting_engine.md` and closes OP-30 task (a).

```bash
python3 simulations/cosmic_coordination_floor/area_capacity_ledger.py
```

Pure standard library, no sampling, runtime a few seconds.

## What is measured and what is imported

Measured from the toy: the interior contraction `gamma`, the exported record
`sigma`, and the slot resolution of the boundary record map. Imported: the
capacity in bits, `C_area = A / (4 ln 2) = 4 pi M^2 / (C_R^2 ln 2)` in Planck
units, using the toy's own compactness `C_R = 2M/R_areal`.

## Rate ledger

The toy's boundary record is a deterministic function of the macrocell, so
taking the current macrocell as the reference gives the exact one-step ledger

```text
delta_k = H(M_k) - I(M_k; M_{k+1})
sigma_k = I(M_k; R_{k+1})
gamma_k = sigma_k + delta_k
```

The cumulative export is not tracked by branch propagation; Theorem 1 gives the
exact bound `E_k <= H(M_0)` for all time, which is what the Bekenstein stock
bound needs and is stronger than any finite-horizon measurement.

## Outputs

- `outputs/area_capacity_rate_ledger.csv`
- `outputs/area_capacity_summary.csv`
- `outputs/area_capacity_calibration.csv`
- `outputs/area_capacity_marginality.csv`

## Current Result

Toy interior stock bound `H(M0) = 2.909592` bits. Boundary record map has 15
distinct tuples, so `C_slots = 3.906891` bits.

| Policy | mean gamma | mean sigma | mean delta | chi | peak gamma | gamma/C_slots | BW-limited |
|---|---:|---:|---:|---:|---:|---:|---:|
| naked_collapse | 5.5445 | 1.5345 | 4.0100 | 0.27676 | 5.7525 | 1.4724 | 35/36 |
| hard_exclusion | 2.6707 | 1.0058 | 1.6649 | 0.37661 | 5.7510 | 1.4720 | 13/36 |
| horizon_transfer | 5.8275 | 2.2223 | 3.6053 | 0.38134 | 6.2154 | 1.5909 | 35/36 |
| quantum_completion | 6.0157 | 2.0294 | 3.9863 | 0.33735 | 6.3657 | 1.6294 | 35/36 |

Ledger identity residual at most `8.9e-16` bits; the bound
`delta >= gamma - C` is never violated, minimum slack `0.0961` bits.

## Interpretation

- **The toy is over-driven by its own record partition, not by the area law.**
  The kernel contracts 5.75-6.37 bits per step against a 3.907-bit slot
  capacity, so destruction is forced and `chi` is 0.28-0.38 for every policy.
  Even `quantum_completion` destroys about two thirds of what it contracts —
  because the toy's boundary bins cannot resolve what its kernel merges.
- **The area law would permit far more.** At `M = 1`, `C_R = 1` the area
  capacity is `18.13` bits, 4.6 times the toy's slot capacity; at `M = 10` it is
  `1813` bits, 464 times; for a solar-mass hole it is of order `1e77` bits.
- **The SE-1 area crossing does not occur here at any super-Planckian mass.** It
  would need `M < 0.4006` Planck masses at `C_R = 1`, which is where the
  semiclassical area law stops meaning anything. This toy cannot test SE-1; the
  bandwidth limit it exhibits is an artifact of coarse boundary bins.
- **The fix is specific.** The boundary record map needs resolution scaling with
  the boundary area, of order `A/4` bits rather than 15 fixed slots.
- **chi does not rank policies on its own.** `hard_exclusion` posts a
  competitive `chi = 0.3766` with the lowest contraction, and is nonetheless the
  policy this toy rejects for violating the future-entropy floor. Sorting
  efficiency is a third axis alongside the floor and the privacy condition.

## Horizon Marginality

Taking the standard identifications — a horizon of area `A` has
`S_BH = A/4` and about `exp(S_BH)` interior microstates — the quantum interior
budget is `2 S_BH` bits, a horizon record of `S_BH` qubits carries at most
`2 S_BH` bits of quantum mutual information, and at most `S_BH` bits once
decohered:

| M (Planck) | S_BH bits | budget 2S | quantum capacity | classical capacity | chi_max classical |
|---:|---:|---:|---:|---:|---:|
| 1 | 18.13 | 36.26 | 36.26 | 18.13 | 0.50 |
| 10 | 1813 | 3626 | 3626 | 1813 | 0.50 |
| 1e3 | 1.813e7 | 3.626e7 | 3.626e7 | 1.813e7 | 0.50 |
| 1e38 | 1.813e77 | 3.626e77 | 3.626e77 | 1.813e77 | 0.50 |

The interior budget and the quantum record capacity are equal at every mass,
with zero margin. Granting the imported identifications, a black hole is
exactly the object whose boundary can losslessly sort its own interior and not
one bit more — and only if the record is quantum.
