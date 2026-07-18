# Session log — 2026-07-18 — interior clock register

## Intent

Tenth pull on the braided-clock thread, direction chosen autonomously: the
executable rung named by `bridges/boundary_records_interior_time.md` —
test Corollaries G1 and G2 inside the macrocell collapse toy.

## What was built

Upgraded `simulations/cosmic_coordination_floor/cosmic_coordination_floor.py`:

- state is now a joint distribution over (macrocell, interior clock phase
  \(\theta\in\mathbb Z_8\)), uniform \(\theta\) prior, deterministic
  advance of one bin per step; the 8-class interior microstate of the
  late decode is identified with the clock, so what the boundary decodes
  at transfer is the phase frozen at absorption;
- per-step diagnostic `interior_clock_record_mi_bits`
  \(=I(\Theta;\mathrm{boundary\ record})\) on the joint distribution,
  folded into the privacy audit;
- fifth policy `leaky_completion`: identical to `quantum_completion`
  except the transfer's radiation record carries the clock parity — a
  deliberately clock-central, inadmissible channel;
- summary columns `max_interior_clock_record_mi_bits`,
  `clock_info_release_step` (thresholded at `1e-3` to remove a
  Gaussian-tail artifact), and `clock_leak_onset_step`.

## Results

| Policy | max \(I(\Theta;R)\) | leak onset | clock/info release |
|---|---:|---:|---:|
| naked_collapse | 0.000 | — | — |
| hard_exclusion | 0.000 | — | — |
| horizon_transfer | 0.000 | — | step 7 |
| quantum_completion | 0.000 | — | step 6 |
| leaky_completion | 0.210 | step 6 | step 6 |

- **G1 (interior clock censorship):** every admissible policy holds the
  clock-record information at exactly zero for the whole run while
  carrying `1.5`-`2.1` bits of geometry-record information.
- **G2 (time release = information release):** the clock becomes
  boundary-readable through the late decodable channel at the transfer
  step, the same step interior information is released.
- **Teeth:** the leaky control leaks `0.210` bits starting exactly at its
  trigger step and is flagged as a privacy violation (step 9, when
  triggered mass makes the leakage significant) despite satisfying the
  entropy floor and normalization — early clock reading alone renders a
  completion inadmissible.
- **Failure-route separation:** naked collapse leaks the interior via
  lost singular mass with zero record-channel clock information; the
  leaky channel leaks via the record itself. The two inadmissibility
  routes are now visibly distinct in the diagnostics.

## Files touched

- `simulations/cosmic_coordination_floor/` (script, README, regenerated
  outputs).
- `bridges/boundary_records_interior_time.md` (prediction marked tested).
- `OPEN_PROBLEMS.md` (OP-20).
- `STATUS.md` (changelog).

## Next steps

- OP-30(a) remaining half (information-to-algebra converse), which is
  also the certification gap for the gravitational lift.
- OP-19: the semiclassical collapse failure theorem, still the hard rung
  of the derivation program.
