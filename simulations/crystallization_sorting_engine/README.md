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
