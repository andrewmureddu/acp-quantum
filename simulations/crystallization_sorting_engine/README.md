# Crystallization Sorting Engine

Executable companion to `bridges/crystallization_sorting_engine.md`.

This is not a gravitational simulation. It is an exact finite-information model
of the claim that contraction toward the crystallization boundary is the only
power source for boundary record formation, and that the resulting sorting
operation is lossless or wasteful depending on whether distinctions are
exported before they are merged.

## Model

An interior microstate is a pair `s = (g, l)`: a three-valued sector label `g`
(the QEC error sector / gravitational geometry sector) and a three-valued
protected label `l` (the logical state / interior microstate). `S0` is uniform
over the nine microstates, so `H(S0) = log2(9) = 3.169925` bits.

Each step applies two channels to the interior register `M_k`:

1. **the sorter** — a slot partition of the microstate set. The sorter files a
   label into a slot only when the label's whole support lies inside one block.
   A coin whose denomination has already been melted away cannot be filed.
2. **contraction** — merges a still-present coordinate with probability `rate`,
   or (for `merge_all` policies) annihilates every remaining distinction in one
   step.

Both channels depend only on `(M_k, R_{<=k})` and never on `S0`, so the chain
`S0 -> (M_k, R_{<=k}) -> (M_{k+1}, R_{<=k+1})` is Markov and the data
processing inequality applies.

## Ledger

```text
T_k = I(S0; M_k, R_{<=k})     total surviving distinguishability
E_k = I(S0; R_{<=k})          exported (sorted) column
J_k = I(S0; M_k | R_{<=k})    retained interior column (the backlog)

gamma_k = J_k - J_{k+1}       contraction (the engine stroke)
sigma_k = E_{k+1} - E_k       sorted output
delta_k = T_k - T_{k+1}       destroyed (the waste)

gamma_k = sigma_k + delta_k   ledger identity
chi     = sum(sigma) / sum(gamma)
```

Three bounds are checked numerically at every step of every policy:
the ledger identity, `sigma_k <= gamma_k` (no record without contraction), and
`delta_k >= gamma_k - C_k` (bandwidth-limited sorting, with
`C_k = log2(#slots)`).

## Policies

All six share one boundary-channel schedule — emission probability `0.30`
before the decoding scale at step 10, `1.0` after — so the comparison isolates
what each policy reads and when it contracts, not how much bandwidth it was
handed.

- `classical_collapse` — one slot, accelerating contraction. Positive capacity,
  zero resolution: reports *that* collapse happens, never *what* collapses.
- `over_driven_sorter` — sector slots, but ungated accelerating contraction
  merges labels before they are filed.
- `late_completion` — silent until step 14, then the right mechanism engaged
  too late: one crush step of 3.01 bits against a 2-bit channel.
- `sort_then_contract` — merges a coordinate only once the accumulated record
  already determines it; sector-only slots before the decoding scale, protected
  release after.
- `centralizing_sorter` — same gating, but one slot per microstate from step 0.
  Lossless and inadmissible.
- `stalled_remnant` — same gating, sector slots forever; never opens a
  protected-release channel.

## Exactness

The joint distribution over `(S0, M_k, R_{<=k})` is propagated as a list of
record branches, each holding a normalized joint over `(S0, M)` plus a weight.
Branches with equal posteriors are merged, which is exact because every
reported quantity is a weighted function of the branch posterior alone. No
sampling is used, and there are no third-party dependencies.

## Run

```bash
python3 simulations/crystallization_sorting_engine/sorting_engine.py
```

Runtime is a few seconds; the throughput scan dominates.

## Outputs

- `outputs/sorting_engine_ledger.csv` — per-step ledger for each policy.
- `outputs/sorting_engine_summary.csv` — per-policy totals, checks, verdict.
- `outputs/sorting_engine_throughput_scan.csv` — 108-configuration sweep over
  contraction rate, emission throughput, and slot resolution.
- `outputs/sorting_engine_ledger.svg` — exported column (solid) against
  retained backlog (dashed).
- `outputs/sorting_engine_throughput_frontier.svg` — efficiency against
  contraction rate for five channels.

## Current Result

| Policy | chi | exported | backlog | early leak | BW-limited steps | verdict |
|---|---:|---:|---:|---:|---:|---|
| classical_collapse | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | destructive |
| over_driven_sorter | 0.443299 | 1.405225 | 0.000000 | 0.000000 | 0 | destructive |
| late_completion | 0.500003 | 1.584972 | 0.000000 | 0.000000 | 1 | destructive, capacity exceeded |
| stalled_remnant | 1.000000 | 1.584963 | 1.584963 | 0.000000 | 0 | lossless, permanent backlog |
| centralizing_sorter | 1.000000 | 3.169925 | 0.000000 | 1.540191 | 0 | lossless, centralizing |
| sort_then_contract | 1.000000 | 3.169925 | 0.000000 | 0.000000 | 0 | admissible |

Numerical validation: maximum ledger-identity residual `2.2e-15` bits, maximum
`sigma > gamma` excess `1.1e-15` bits, no violation of `delta >= gamma - C`.

The four load-bearing readings:

- **Resolution, not bandwidth, kills the classical baseline.** A one-slot
  channel with positive capacity exports exactly zero bits.
- **Trigger time is decisive.** `sort_then_contract` and `late_completion` use
  the same idea and the same slots; engaging at step 0 gives `chi = 1`,
  engaging at step 14 burns half the budget.
- **Efficiency is not legitimacy.** `centralizing_sorter` matches the admissible
  policy's ledger exactly while leaking 1.540 bits of protected label before the
  decoding scale.
- **Lossless can still fail.** `stalled_remnant` wastes nothing and ends holding
  `log2(3) = 1.585` bits it can never spend.

The throughput scan reproduces the predicted frontier: `chi` falls
monotonically with contraction rate at fixed channel; a full-resolution
full-throughput channel holds `chi = 1.000000` at every contraction rate; a
one-slot channel holds `chi = 0` at every rate; and sector-resolution channels
sit at exactly `chi = 0.500000` once contraction completes, matching the
Corollary 4.2 ceiling `log2(3)/log2(9)`.

---

# Quantum Sorting Ledger

`quantum_sorting_ledger.py` is the coherent-information form of the same ledger,
the executable companion to Section 14 of the bridge.

The classical model above calls the residual column *destroyed*. Quantum
mechanically the global evolution is an isometry, nothing is destroyed, and the
ledger becomes a conservation law.

## Model

A reference `R` (two qubits) is maximally entangled with the interior `A` (two
qubits), so the budget is `I(R;A) = 2 H(R) = 4` bits — twice the classical
maximum, with the extra half existing only as coherence. Each step acts by a
unitary on the interior together with one fresh boundary record qubit and one
fresh environment qubit. The global state on `R A B E` stays pure and every
von Neumann entropy is computed exactly from the 16-qubit state vector.

```text
E_k = I(R; B)        exported to the boundary record
J_k = I(R; A | B)    retained interior backlog
T_k = I(R; A B)      total still reachable without the environment
L_k = I(R; E)        leaked to the unrecorded environment

I(R;B) + I(R;A|B) + I(R;E) = 2 H(R)     exactly, at every step
gamma = sigma + delta,   delta = L_{k+1} - L_k
```

Coherent information differs from quantum mutual information by the constant
`H(R)`, so `gamma`, `sigma`, `delta`, and `chi` are identical in either
language. Sorting efficiency was already a coherent-information quantity.

## Run

```bash
python3 simulations/crystallization_sorting_engine/quantum_sorting_ledger.py
```

Unlike `sorting_engine.py`, this one needs `numpy` for the state-vector
linear algebra. There is still no sampling: every entropy is exact.

## Outputs

- `outputs/quantum_sorting_ledger.csv`
- `outputs/quantum_sorting_summary.csv`
- `outputs/quantum_sorting_dephasing_scan.csv`

## Current Result

| Policy | gamma | sigma | delta | chi | I(R;B) | I(R;E) | Ic(R>B) | early protected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| coherent_sort | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 2.0000 |
| classical_sort | 4.0000 | 2.0000 | 2.0000 | 0.50000 | 2.0000 | 2.0000 | 0.0000 | 1.0000 |
| leaky_sort | 4.0000 | 2.7982 | 1.2018 | 0.69956 | 2.7982 | 1.2018 | +0.7982 | 1.3991 |
| crush | 4.0000 | 0.0000 | 4.0000 | 0.00000 | 0.0000 | 4.0000 | -2.0000 | 0.0000 |
| sector_then_protected | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 0.0000 |
| centralizing_sort | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 2.0000 |

Validation across all six policies and all steps: the conservation law holds to
`0.000e+00`; the backlog never goes negative, so strong subadditivity is
saturated but never violated; `sigma <= gamma` and `sigma <= 2 log2 d_B` are
never violated; and `|delta - (L_next - L)| = 0.000e+00`, confirming that
destruction *is* leakage exactly rather than merely bounded by it.

- **`classical_sort` lands on `chi = 0.5` and `Ic(R>B) = 0.0000` together.** A
  decohered boundary record caps sorting efficiency at one half, which is the
  same statement as its coherent information being non-positive. Classicality
  of the record is a slot-resolution limit.
- **`crush` reaches `Ic = -2.0000 = -H(R)`,** the floor.
- **`sector_then_protected` and `centralizing_sort` have identical ledgers** and
  differ only in early protected export (`0.0000` against `2.0000`), the same
  efficiency-is-not-legitimacy separation as the classical model.

## Dephasing Scan

Sweeping the record-environment coupling angle from 0 to pi turns the
classicality of the record into a continuous knob, moving chi from `1.000000`
to `0.500000` along the closed form

```text
chi(theta) = 1 - h2((1 + cos(theta/2)) / 2) / 2
```

which the simulation matches to `0.00e+00` at all thirteen sample points. There
is no sharp classical/quantum transition in sorting efficiency: partial
decoherence of the record costs partial efficiency, and the classical limit is
the endpoint of a smooth curve rather than a separate regime.
