# Session: Crystallization Sorting Engine

**Date:** 2026-07-26
**Branch:** `claude/singularity-sorting-mechanism-a7c917`
**Front:** ACP quantum-gravity derivation program (OP-18, OP-19, OP-20, new OP-30)

## Input

Andrew:

> hmm. singularity = where reality's sorting machine resides. you know how a
> change machine sorts coins? something like that. the pressure from the
> crystallization is put to work to sort/process.

## What I decided

The existing derivation program treats contraction toward the crystallization
boundary purely as a hazard: collapse narrows the future channel and must be
stopped before the coordination floor is breached. That reading says what
contraction costs and never says what it buys. Andrew's framing supplies the
missing half, and it turned out to be formalizable rather than metaphorical.

The formal object is a three-column distinguishability ledger. Everything else
in the session followed from writing it down.

## Result

### New bridge: `bridges/crystallization_sorting_engine.md`

With \(S_0\) the initial interior microstate, \(M_k\) the interior register,
and \(R_{\leq k}\) the retained boundary record, define

$$
T_k=I(S_0;M_k,R_{\leq k}),\quad
E_k=I(S_0;R_{\leq k}),\quad
J_k=I(S_0;M_k\mid R_{\leq k}),
$$

with per-step increments \(\gamma_k=J_k-J_{k+1}\) (contraction),
\(\sigma_k=E_{k+1}-E_k\) (sorted output), \(\delta_k=T_k-T_{k+1}\) (destroyed).

Five theorems, all proven in the note for any record-retaining Markov dynamics:

1. **Ledger identity.** \(T_k=J_k+E_k\) and \(\gamma_k=\sigma_k+\delta_k\) with
   all three increments non-negative, and \(\sum\gamma_k\leq H(S_0)\). The
   contraction budget is finite and each bit is spent exactly once.
2. **No record without contraction.** \(\sigma_k\leq\gamma_k\). A region whose
   retained interior distinguishability is constant emits no information about
   itself, however loudly it radiates. This is the exact content of "the
   pressure is put to work."
3. **Lossless sorting rule.** If a step merges only distinctions already
   determined by the record, \(\delta_k=0\). Converse in Petz-recoverability
   form. Design rule: *never merge a distinction you have not already
   exported.*
4. **Bandwidth.** \(\delta_k\geq\gamma_k-C_k\) with \(C_k\) the per-step record
   capacity, plus a separate resolution ceiling
   \(\chi\leq H(\Pi(S_0))/(J_0-J_\infty)\) from the slot partition \(\Pi\).
5. **Trigger time.** Destruction is bounded below by
   \(\sum_{k<\tau}\max(0,\gamma_k-C_k)\), so a completion engaged after
   contraction first outruns capacity leaves a debt no later mechanism repays.

Two structural consequences worth keeping:

- The ACP boundaries get an engine reading. Dissolution is no contraction or an
  uncorrelated channel; crystallization is contraction with \(\chi\to0\); the
  productive interval is contraction with \(\chi\) bounded away from zero. This
  strengthens CDT rather than restating it: refusing to contract is refusing to
  emit records, so persistence requires spending the budget and admissibility
  constrains only how.
- \(\gamma_k\leq C_k\) has exactly three solutions — throttle, widen, buffer —
  and bounces, horizon-area growth, and remnants/islands are terms in one
  inequality rather than competing intuitions.

Conjecture SE-1 (⚠): the completion scale is set by where \(\gamma=C\), a
bandwidth scale, not by a fixed curvature threshold alone.

### New simulation: `simulations/crystallization_sorting_engine/`

Exact, dependency-free, no sampling. Nine interior microstates factored as a
three-valued sector label and a three-valued protected label,
\(H(S_0)=3.169925\) bits. The joint over \((S_0,M_k,R_{\leq k})\) is propagated
as record branches; branches with equal posteriors are merged, which is exact
because every reported quantity is a weighted function of the branch posterior.

Six policies share one boundary-channel schedule:

| Policy | \(\chi\) | exported | backlog | early leak | BW-limited | verdict |
|---|---:|---:|---:|---:|---:|---|
| classical_collapse | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | destructive |
| over_driven_sorter | 0.443299 | 1.405225 | 0.000000 | 0.000000 | 0 | destructive |
| late_completion | 0.500003 | 1.584972 | 0.000000 | 0.000000 | 1 | capacity exceeded |
| stalled_remnant | 1.000000 | 1.584963 | 1.584963 | 0.000000 | 0 | permanent backlog |
| centralizing_sorter | 1.000000 | 3.169925 | 0.000000 | 1.540191 | 0 | centralizing |
| sort_then_contract | 1.000000 | 3.169925 | 0.000000 | 0.000000 | 0 | admissible |

Validation: maximum ledger-identity residual `2.2e-15` bits; \(\sigma\leq\gamma\)
never violated beyond `1.1e-15` bits; \(\delta\geq\gamma-C\) never violated.

Four readings I did not expect to come out this cleanly:

- The classical baseline fails on **resolution, not bandwidth**. It has a
  positive-capacity channel and exports exactly zero, because it reports *that*
  collapse occurs and nothing about *what* collapses.
- **Trigger time is decisive.** `sort_then_contract` and `late_completion` use
  the same mechanism and the same slots. Engaging at step 0 gives \(\chi=1\);
  engaging at step 14 crushes 3.01 bits against a 2-bit channel in one step and
  burns exactly half the budget. Theorem 5 in one line of output.
- **Efficiency is not legitimacy.** `centralizing_sorter` matches the admissible
  policy's ledger exactly and is inadmissible. Nothing in Theorems 1-5 separates
  them; only the Knill-Laflamme selectivity condition does. This is the main
  trap the framework creates and it is now flagged in the bridge.
- **Lossless can still fail.** `stalled_remnant` wastes nothing and ends holding
  \(\log_23\) bits it can never spend — a frozen rather than a burnt budget.

The 108-configuration throughput scan reproduces the predicted frontier,
including \(\chi=1\) at *every* contraction rate when resolution and throughput
are maximal (destruction is the channel's failure, not the pressure's), and the
exact `0.500000` sector-resolution ceiling once contraction completes.

## Honesty boundary

Theorems 1-5 are elementary — chain rule plus data processing — and the content
is the identification of the terms, not the difficulty of the proofs. The
gravitational identifications are imported and marked ⚠ throughout: nothing
here derives that focusing merges relational macrocells at rate \(\gamma_k\),
nor that the Bekenstein-Hawking area law gives \(C_k\). The two-phase export
curve is Page-like in shape; the toy is a classical finite record model and the
resemblance is not a derivation.

## Files

- Added `bridges/crystallization_sorting_engine.md`.
- Added `simulations/crystallization_sorting_engine/sorting_engine.py`,
  `README.md`, and five output files.
- Added OP-30 to `OPEN_PROBLEMS.md`; updated OP-18 and OP-19.
- Updated `STATUS.md` (focus line, new front 1a, open-problem list, changelog),
  `README.md`, `AGENTS.md`, `CLAUDE.md`.

## Next

1. Compute \(\gamma_k\) for the macrocell kernel in
   `simulations/cosmic_coordination_floor/` against an area-derived \(C_k\),
   turning Conjecture SE-1 into a number inside the existing collapse toy.
2. Restate the ledger for a quantum record channel with coherent information in
   place of \(I(S_0;\cdot)\).
3. Measure \(\chi\) for the H2 circuit-level scaffold in
   `simulations/hardware_adaptive_decoder/`. The fraction of physical
   decoherence that reaches the decoder as syndrome is exactly this quantity and
   has never been measured there.
4. Score the candidate completions in
   `bridges/relational_observable_macrostate_kernel.md` §10 by throttle / widen
   / buffer.
