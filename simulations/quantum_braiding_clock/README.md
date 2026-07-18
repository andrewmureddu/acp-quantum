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

## Experiment C: operational-time covariance probe (OP-29)

A family of clocks with identical operational length — same tick count (32),
same per-tick strength (`kappa = 0.21`), same per-tick feedback — but
different lab-time tempos: ticks land on every k-th period, k in
{1,2,3,4,6}, with the run stretched so every member executes the same
number of verification steps. Two disturbance conventions:

- `co_clocked`: detuning scaled by 1/k, so the phase error accrued between
  consecutive ticks is identical for every member — the per-tick transition
  kernels match (OP-29 operational conjugacy);
- `lab_clocked`: fixed detuning in lab time, so slow-ticking members accrue
  k times the phase error per verification step — conjugacy fails.

`gamma = 0` here so the detuning is the only lab-clocked process.

## Experiment D: clocked repetition code (OP-23 D0 rung)

Three braided-clock qubits carry the same logical bit and share one clock
(common detuning sector, common PLL drive). The channel adds per-period
phase flips at probability `p_flip` per qubit. Policies compared on the
same logical readout (terminal median across the block): `bare` (single
qubit), `code_unchecked` (redundancy, no checks), `code_checked`
(evidence-gated correction from a pair-parity record channel), and
`code_overactive` (correction from single raw parity records).

Two design lessons are baked in and documented in the module:

- **The tick stream cannot be the syndrome.** A z-tick statistic with
  flip-identification SNR `S` costs `exp(-S^2 / 2)` of the coherence it
  protects, so gentle ticks are too dilute to decode flips in time. This
  is precisely why codes exist: parity operators commute with the logical
  algebra, so parity can be read strongly at zero logical cost
  (Knill-Laflamme in its cheapest form). Experiment D gives parity its own
  record channel — noisy in readout (`PARITY_KAPPA = 0.6`), free of x
  backaction — while the tick stream keeps the clock and PLL.
- This is a product-state Bloch scaffold, not an entangled stabilizer
  code; the zero-backaction status of the parity records is imported from
  the KL argument, not derived. D0 tests the control architecture, not
  stabilizer protection.

## Experiment E: entangled stabilizer code (OP-23 D1 rung)

The state-vector upgrade of Experiment D. Three qubits in the phase-flip
code `|0_L> = |+++>`, `|1_L> = |--->`, protected information stored as a
genuine quantum coherence (the logical-Y eigenstate
`(|0_L> + i sb |1_L>)/sqrt(2)`), a per-period `Z_i` phase-flip channel, and
weak measurements of the stabilizers `X1X2`, `X2X3` implemented as proper
Kraus pairs at readout fidelity `0.6`.

The point of D1 is that the parity channel's zero logical cost is now
**derived, not imported**: under this error model the state is always a
stabilizer eigenstate, so the Kraus update acts as the identity on it and
the backaction vanishes identically while the record stays noisy. The
control `bare_monitored` probes a single unencoded qubit at the same
strength with a weak X measurement, which anticommutes with the stored Y
coherence. Same measurement budget; the commutation structure alone decides
whether monitoring is free or fatal.

Policies: `bare`, `bare_monitored`, `code_unchecked` (terminal ideal decode
only), `code_checked` (EMA syndrome evidence, threshold `0.35`, 5-period
burn-in), `code_overactive` (raw single records). All code policies get the
same terminal ideal decode.

## Experiment F: continuity-bound verification (OP-30a)

Exact 8x8 computation (no Monte Carlo) verifying Proposition 5 of
`bridges/clock_syndrome_record_splitting.md`: nearly transparent
instruments are nearly clock-blind, `I(Theta;R) <= 2 tau log2|R| + h2(2 tau)`
with `tau = n (epsilon + epsilon^2/2)`. Two epsilon-transparent
instruments, both with commutator defect `O(mu)`:

- `conjugated` (apparatus rotated by `exp(-i mu Z1/2)`): nonzero defect but
  **exactly zero** clock information at every `mu` and every sequence
  length — repeated QND measurement of one fixed observable generates an
  abelian Kraus algebra whose record POVMs compress to scalars on the code
  sector. The bound holds but is infinitely loose; the sharper "algebraic
  defect" is folded into OP-30.
- `axis_leak` (readout axis contaminated by the logical `Z-bar`):
  genuinely reads the clock, `I ~ mu^2` and linear in `n`
  (`0.00051 / 0.0020 / 0.0079 / 0.029` bits at `mu = 0.05-0.4`, `n = 1`),
  confirming the proved `O(n^2 epsilon)` bound is loose against the true
  `O(n epsilon^2)` rate. All 20 cells satisfy the bound.

The same harness also runs the **Experiment G algebraic-defect audit**
(Proposition 6, `braiding_clock_algebraic_defect.csv`): all `2^n` record
POVM elements are compressed to the codeword basis and their clock
commutators computed exactly. The conjugated instrument gives filtered
defect exactly zero at every `n` — the Proposition 6 dichotomy assigns it
the blindness the commutator-norm defect missed. The axis-leak instrument
satisfies the chain `TV <= subset witness <= zeta_n` in every cell (the
witness is tight to a factor of 2), and its exact total variation grows
like `sqrt(n)` (`0.030 / 0.061 / 0.087` at `n = 1, 4, 8` for `mu = 0.1`),
confirming the martingale-type growth conjectured in the bridge's Remark 2.

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
- `outputs/braiding_clock_optime_scan.csv`
- `outputs/braiding_clock_optime_summary.csv`
- `outputs/braiding_clock_optime_curves.png`
- `outputs/braiding_clock_code_scan.csv`
- `outputs/braiding_clock_code_summary.csv`
- `outputs/braiding_clock_code_curves.png`
- `outputs/braiding_clock_stabilizer_scan.csv`
- `outputs/braiding_clock_stabilizer_summary.csv`
- `outputs/braiding_clock_stabilizer_curves.png`
- `outputs/braiding_clock_continuity_scan.csv`
- `outputs/braiding_clock_continuity_curves.png`
- `outputs/braiding_clock_algebraic_defect.csv`

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

## Current Operational-Time Run

| Quantity | co-clocked (conjugate) | lab-clocked (non-conjugate) |
|---|---:|---:|
| Memory retention across k | `0.479 - 0.494` (flat) | `0.458 - 0.482` (flat) |
| Clock slack `H(r'\|r)` across k | spread `0.0008` | spread `0.0007` |
| Phase lock across k | `0.281 - 0.443` (one band) | `0.363` at k=1, `~0` for k>=2 |
| `I(error; record)` across k | `0.020 - 0.079` bits (one band) | `0.053` at k=1, `<= 0.004` bits for k>=2 |
| Logical leak across k | `<= 0.0036` bits everywhere | `<= 0.0069` bits everywhere |

## Current Code Run

Signed logical retention by policy (seeded, 600 trajectories per cell):

| `p_flip` | bare | unchecked | checked | overactive | checked sign fid. | checked corrections |
|---:|---:|---:|---:|---:|---:|---:|
| 0.000 | **0.3209** | 0.2503 | 0.2432 | 0.1272 | 1.000 | 0.24 |
| 0.005 | 0.2174 | 0.2055 | **0.2233** | 0.1118 | 0.963 | 0.79 |
| 0.010 | 0.1326 | 0.1273 | **0.1947** | 0.1008 | 0.918 | 1.17 |
| 0.020 | 0.0741 | 0.0524 | **0.1399** | 0.0648 | 0.780 | 1.71 |
| 0.040 | 0.0200 | 0.0287 | **0.0317** | 0.0001 | 0.592 | 2.57 |
| 0.080 | 0.0329 | 0.0048 | 0.0000 | 0.0045 | 0.498 | 3.28 |

Grid-max logical leak on the common-mode record: `0.006029` bits.

## Current Stabilizer Run

Logical-Y retention by policy (seeded, 600 trajectories per cell):

| `p_flip` | bare | bare_monitored | unchecked | checked | overactive |
|---:|---:|---:|---:|---:|---:|
| 0.000 | 1.0000 | 0.0008 | 1.0000 | 0.9967 | 0.0567 |
| 0.005 | 0.7333 | 0.0001 | 0.8600 | **0.9300** | 0.0000 |
| 0.010 | 0.4733 | 0.0000 | 0.6967 | **0.8167** | 0.0300 |
| 0.020 | 0.2400 | 0.0003 | 0.4100 | **0.5333** | 0.0967 |
| 0.040 | 0.0200 | 0.0000 | 0.0567 | **0.1000** | 0.0000 |
| 0.080 | 0.0033 | 0.0001 | 0.0300 | 0.0100 | 0.0000 |

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
- **Operational-time covariance behaves exactly as OP-29 predicts.**
  Tick-native scalars — memory retention (the pure per-tick measurement
  cost) and record slack — are invariant across lab tempos in BOTH modes:
  they depend only on how many verification steps were executed, not on
  how sparsely those steps sit in lab time. Record-facing diagnostics
  (phase lock, syndrome information) are invariant only in the co-clocked
  mode, where the disturbance kernel commutes with the tempo map; when the
  error process keeps lab time, every slowed member fails as a clock in
  its own tick frame — by k=2 the lock is gone and the tick stream carries
  essentially no syndrome. Covariance holds exactly when OP-29's
  conjugacy condition holds, and fails catastrophically, not gracefully,
  when it does not. Residual co-clocked scatter is consistent with mutual-
  information estimator noise at 600 trajectories.
- **The code run passes the OP-23 acceptance discipline, with a productive
  interval for correction itself.** Evidence-gated correction beats bare,
  unchecked, and overactive baselines on the same logical readout — but
  only in the middle noise window `p_flip ~ 0.005-0.04`. Below it, the
  decoder's residual false positives make checking a net cost (bare wins
  at zero noise: `0.321` vs `0.243`); above it, multi-flips overwhelm a
  distance-3 decoder (checked retention `0.000` at `p_flip = 0.08`).
  Correction is not free and not unconditional: it wins exactly where
  error structure is real, decodable, and not yet saturating — the same
  cautionary shape as the H0-H2 hardware scans, now reproduced inside the
  braided-clock architecture. The overactive policy is worse everywhere,
  and the common-mode clock feedback stays logically noncentral
  (grid-max leak `0.006` bits).
- **The stabilizer run derives what D0 imported.** At zero noise the
  checked code retains `0.9967` logical coherence through 72 weak
  stabilizer measurements, while the bare qubit probed at the same
  strength retains `0.0008` — three orders of magnitude, decided entirely
  by whether the measured operator commutes with the protected
  information. In the working window `p_flip ~ 0.005-0.04` the checked
  code dominates every baseline on the same readout (`0.93 / 0.82 / 0.53`
  vs unchecked `0.86 / 0.70 / 0.41`); at `0.08` multi-flips saturate the
  distance-3 decoder and mid-run checking mildly hurts (`0.01` vs
  unchecked `0.03`). The evidence gate matters at this rung too: without
  the burn-in and higher threshold, early EMA fluctuations false-fire and
  the zero-noise retention drops to `0.54` — the D0 lesson reproduced with
  true state vectors.
