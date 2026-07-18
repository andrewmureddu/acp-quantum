# Quantum Braiding Clock Simulation

This toy simulation supports `bridges/quantum_braiding_timekeeping.md` (OP-22).

It tests the braided persistence conjecture on the smallest honest
instrument: a single qubit whose own weak-measurement records are its clock,
its syndrome channel, its feedback input, and its principal hazard at the
same time.

```text
I(error sector; record) > 0        the ticks know if the clock runs fast/slow
I(logical; record | error) ~ 0     the ticks never read the protected bit
signed logical retention > 0       the escapement has not consumed the memory
```

## Model

Bloch-vector qubit, seeded and deterministic:

- **Logical bit** `b`: sign of the x component. All Hamiltonian and feedback
  rotations are about x, so the controller is logically noncentral by
  construction (the Knill-Laflamme shape); only measurement backaction can
  shrink x.
- **Clock carrier**: the y-z components precess about x at a hidden detuned
  frequency `omega * (1 +/- 0.04)`; the detuning sign is the error sector `e`.
- **Escapement**: twice per nominal period the qubit is weakly measured along
  z with strength `kappa` — an in-phase burst at the nominal z maximum (the
  tick) and a quadrature burst at the nominal zero crossing (the phase-error
  readout).
- **Feedback braid**: an exponential moving average of quadrature records
  drives a phase correction about x with gain `g` — an integrating
  phase-locked loop built from the qubit's own collapse records.

## Why pulsed rather than continuous

The first version of this model used continuous weak monitoring and found a
null with content: transverse coherence dies like `exp(-kappa^2 t / 2)`,
while reading a drift against measurement backaction needs near-Zeno
strength, and the two regimes never overlap; worse, a constant z drift under
fast precession hides in the y quadrature, invisible to a z monitor. A
single continuously monitored qubit cannot be its own clock, syndrome meter,
and memory at once. Pulsing the monitor — paying the dephasing cost only at
tick times — is what opens a productive interval. The braid needs rhythm.

## Metrics

- `clock_slack_bits`: Markov conditional record entropy `H(r_{n+1} | r_n)`
  (reported, not scored; binary weak ticks sit near the dissolution end by
  encoding, and reach the crystallized end only at `kappa -> 1`).
- `memory_retention`: signed terminal logical retention `mean(sb * x) / x0`.
  The sign matters: amplitude pumped back into x with scrambled sign must
  not count as memory.
- `error_info_bits`: `I(e; sign of mean quadrature record)`.
- `logical_leak_bits`: `I(b; sign of mean quadrature record | e)`.
- `phase_lock`: mean in-phase tick bias over its ideal locked value.
- `braid_score`: memory x error-info x phase-lock x (1 - leak penalty).

## Experiment B: tick rate vs tick strength at fixed dephasing budget

A run with `N` ticks at strength `kappa` spends a total dephasing budget
`B = -(N/2) ln(1 - kappa^2)` (ideal logical retention `exp(-B)`). The budget
scan holds `B` fixed, fires the escapement only every k-th period, sets
`kappa` to spend the whole budget, and takes the best feedback gain per
cell. The question: should a clock spend its decoherence budget on many
weak ticks or a few strong ones?

## Run

```bash
python3 simulations/quantum_braiding_clock/quantum_braiding_clock.py
```

## Outputs

- `outputs/braiding_clock_scan.csv`
- `outputs/braiding_clock_summary.csv`
- `outputs/braiding_clock_heatmaps.png`
- `outputs/braiding_clock_budget_scan.csv`
- `outputs/braiding_clock_budget_summary.csv`
- `outputs/braiding_clock_budget_heatmaps.png`

## Current Run

The seeded 12 x 12 scan over burst strength `kappa` in [0.05, 0.95] and
feedback gain `g` in [0, 3.3] currently reports:

| Probe | Result |
|---|---:|
| Grid points | `144` |
| Best braid score | `0.006390` |
| Best-point burst strength `kappa` | `0.2136` |
| Best-point feedback gain `g` | `3.3` |
| Best-point memory retention | `0.307318` |
| Best-point `I(error; record)` | `0.061023` bits |
| Best-point `I(logical; record \| error)` | `0.005604` bits |
| Best-point phase lock | `0.344621` |
| Weakest-monitor row mean braid score | `0.000214` |
| Strongest-monitor row mean memory | `0.000000` |
| Strongest-monitor row mean `I(error; record)` | `0.004040` bits |
| Zero-gain mean phase lock | `0.094241` |
| Max-gain mean phase lock | `0.425850` |
| Grid max logical leak | `0.011986` bits |

## Current Budget Run

The seeded budget scan (6 budgets x 7 tick rates x 3 gains, best gain per
cell) currently reports:

| Probe | Result |
|---|---:|
| Budget cells | `42` |
| Best braid score | `0.006942` |
| Best budget `B` | `1.05` |
| Best tick rate | every period (`k = 1`, 48 ticks) |
| Best implied `kappa` | `0.206898` |
| Fastest-rate mean braid score | `0.004503` |
| Slowest-rate (`k = 12`) mean braid score | `0.000071` |
| Fastest-rate mean `I(error; record)` | `0.064618` bits |
| Slowest-rate mean `I(error; record)` | `0.002415` bits |
| Fastest-rate mean memory | `0.329269` |
| Slowest-rate mean memory | `0.336041` |
| Grid max logical leak | `0.010816` bits |

Braid score against budget at the fastest tick rate (best gain per cell):

| Budget `B` | Memory | `I(error; record)` bits | Braid score |
|---:|---:|---:|---:|
| 0.35 | 0.701223 | 0.019014 | 0.002040 |
| 0.70 | 0.509784 | 0.031569 | 0.005918 |
| 1.05 | 0.361444 | 0.060515 | **0.006942** |
| 1.40 | 0.227764 | 0.064292 | 0.004973 |
| 2.10 | 0.119064 | 0.088765 | 0.004288 |
| 2.80 | 0.056334 | 0.123555 | 0.002856 |

## Interpretation

- **Weak monitoring** (`kappa ~ 0.05`): memory survives but the record
  carries no syndrome and the clock never locks — no braid.
- **Strong monitoring** (`kappa ~ 0.95`): the memory is dead AND the error
  information also collapses, because the escapement's own backaction
  destroys the oscillation it is trying to read. Over-measurement dissolves
  the clock itself, not just the memory. Both ACP boundaries are fatal.
- **Intermediate monitoring with feedback**: the productive braid. The
  record stream partially phase-locks (feedback raises mean lock from
  `0.094` to `0.426`), the tick stream carries nonzero detuning syndrome,
  roughly a third of the logical coherence survives the run, and the
  logical leak audit stays at the finite-sample floor everywhere on the
  grid — the record-driven controller reads the clock's tempo without ever
  reading the protected bit.
- The result is modest rather than triumphal, in keeping with the hardware
  scaffolds: the productive interval exists, but backaction phase jitter
  (`~kappa / Y0` radians per quadrature tick) keeps the lock partial.
- **Budget verdict: spend the decoherence budget on many weak ticks.** With
  the budget held fixed, memory retention is rate-independent (the
  normalization check: `0.329` vs `0.336` at the two extremes), but the
  syndrome and the lock live almost entirely at the fast end — sparse
  strong ticks let phase error accumulate between corrections, alias the
  slow drift, and inject large per-tick backaction jitter, so the slowest
  rate loses ~26x in error information and ~60x in braid score against the
  fastest. Continuous-in-spirit but pulsed-in-form monitoring is optimal:
  the earlier "the braid needs rhythm" result plus this one bracket the
  design rule as tick as often as possible, as gently as possible.
- **The budget itself has an interior optimum** (`B ~ 1.05`, retention
  `exp(-B) ~ 0.35`): memory falls monotonically in `B`, error information
  rises monotonically, and the braid score peaks between — the ACP
  productive interval reappearing in the spend dimension.
