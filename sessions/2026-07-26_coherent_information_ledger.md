# Session: Coherent-Information Restatement of the Sorting Ledger

**Date:** 2026-07-26
**Branch:** `claude/singularity-sorting-mechanism-a7c917`
**Front:** OP-30, task (b)
**Predecessors:** `sessions/2026-07-26_crystallization_sorting_engine.md`,
`sessions/2026-07-26_h2_sorting_efficiency_audit.md`

## Input

Andrew: "do the coherent-information restatement."

## What came out

I expected a translation exercise — swap Shannon quantities for von Neumann
ones, watch the sign conventions, note that coherent information can go
negative. The ledger turned out to be stronger in the quantum register than in
the classical one, not weaker.

### The increments were always coherent-information quantities

For a purification, \(I_c(R\rangle X)=I(R;X)-H(R)\), and \(H(R)\) is constant.
So \(\gamma\), \(\sigma\), \(\delta\), and \(\chi\) are *identical* whether
computed from quantum mutual information or coherent information. Only the
absolute columns shift, and the identity survives as \(T^c=E^c+J\) because
\(J\) is a conditional mutual information and is unshifted. There was nothing
to translate: the classical presentation was hiding a coherent-information
object.

The one real strengthening in Theorem 1-Q is clause (3). \(J_k\geq0\) was
trivial classically. Quantum mechanically it is strong subadditivity.

### Theorem 6: the ledger is a conservation law

Purity of \(RABE\) gives

$$
I(R;B_{\leq k})+I(R;A_k\mid B_{\leq k})+I(R;E_{\leq k})=2H(R)
$$

exactly at every step, hence \(\delta_k=I(R;E_{\leq k+1})-I(R;E_{\leq k})\).

This is the sharpest form of the whole framework and it corrects the classical
vocabulary. The classical ledger had two columns and a leak to nowhere; the
quantum ledger has three columns and no leak. Contraction is a **routing
decision** — every bit leaving the interior arrives either in the boundary
record or in the environment:

$$
\gamma_k=\underbrace{\sigma_k}_{\text{filed in a slot}}+\underbrace{\delta_k}_{\text{on the floor}}.
$$

"Destruction" in Sections 3-7 is not annihilation but leakage to a party whose
records nobody reads. Whether that distinction is operational depends entirely
on whether the environment is recoverable, which is the black-hole information
question restated as a question about which column the contraction went into.

Two corollaries fell out. The quantum budget is \(2H(R)\), twice the classical
maximum, the extra half existing only as coherence. And because the three
columns sum to a constant, boundary and environment compete for one pool:
monogamy is the conservation law read sideways, not an extra principle.

### Theorem 7: classicality of the record is a slot-resolution limit

A decohered boundary record has \(I(R;B)=H(R)-\sum_bp_bH(\rho^b_R)\leq H(R)\),
so a fully drained interior gives

$$
\chi\leq\tfrac12,
$$

equivalently \(I_c(R\rangle B)\leq0\).

This is Corollary 4.2 reappearing in quantum form. A machine that files coins
by reading a classical label captures at most half of what a quantum interior
distinguishes, however many slots it has and however fast it runs.

### Theorem 3-Q: the design rule from the other side

\(\delta_k=0\) iff the environment learns nothing new about the reference —
decoupling, hence correctability, hence Knill-Laflamme. "Never merge a
distinction you have not already exported" becomes "never let the environment
learn something the record has not already learned." Same rule, other side of
the ledger. This closes the loop with `bridges/otherness_preserving_recovery.md`.

## Consequence for the derivation program

Stage 7 of `bridges/quantum_gravity_derivation_program.md` currently treats
holographic QEC as *evidence* for the structure ACP expects. Theorem 7 upgrades
that to an exclusion. If an admissible completion must reach \(\chi\to1\) —
which it must, because \(\delta>0\) is exactly information routed to a party the
exterior cannot read — then the boundary record channel cannot be classical. A
horizon emitting only decohered outcomes caps sorting at one half and strands
half the interior budget in the environment.

⚠ The step from "the record must be quantum" to "the boundary theory is a
specific holographic code" is not bridged. What is forced is only the
classicality exclusion, and it is forced given a premise (\(\chi\to1\)) that is
itself an ACP requirement rather than a theorem about gravity.

## Simulation

`simulations/crystallization_sorting_engine/quantum_sorting_ledger.py`. Exact
pure state on 16 qubits: two reference qubits maximally entangled with a
two-qubit interior, plus one record and one environment qubit per step over six
steps. Every von Neumann entropy computed from the state vector, using purity to
diagonalize the smaller side. Budget \(2H(R)=4\) bits.

| Policy | \(\gamma\) | \(\sigma\) | \(\delta\) | \(\chi\) | \(I(R;B)\) | \(I(R;E)\) | \(I_c(R\rangle B)\) | early prot. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| coherent_sort | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 2.0000 |
| classical_sort | 4.0000 | 2.0000 | 2.0000 | 0.50000 | 2.0000 | 2.0000 | 0.0000 | 1.0000 |
| leaky_sort | 4.0000 | 2.7982 | 1.2018 | 0.69956 | 2.7982 | 1.2018 | +0.7982 | 1.3991 |
| crush | 4.0000 | 0.0000 | 4.0000 | 0.00000 | 0.0000 | 4.0000 | −2.0000 | 0.0000 |
| sector_then_protected | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 0.0000 |
| centralizing_sort | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 2.0000 |

Validation, all six policies, all steps: conservation to `0.000e+00`; backlog
never negative, so strong subadditivity is saturated but never violated;
\(\sigma\leq\gamma\) and \(\sigma\leq2\log_2d_B\) never violated; and
\(|\delta_k-(L_{k+1}-L_k)|=\) `0.000e+00`, so destruction *is* leakage exactly
rather than merely bounded by it.

`classical_sort` lands on \(\chi=0.5\) and \(I_c(R\rangle B)=0.0000\)
simultaneously — Theorem 7 with both equivalent statements visible at once.
`crush` reaches the floor at \(I_c=-2=-H(R)\). `sector_then_protected` and
`centralizing_sort` again share an identical ledger and differ only in early
protected export, which is the efficiency-is-not-legitimacy separation carried
into the quantum register unchanged.

The dephasing scan makes record classicality a continuous knob. Sweeping the
record-environment coupling angle from 0 to \(\pi\) moves \(\chi\) from
`1.000000` to `0.500000` along

$$
\chi(\theta)=1-\tfrac12h_2\!\left(\tfrac{1+\cos(\theta/2)}{2}\right),
$$

matched to `0.00e+00` at all thirteen sample points. There is no sharp
classical/quantum transition in sorting efficiency: partial decoherence of the
record costs partial efficiency, and the classical limit is the endpoint of a
smooth curve rather than a separate regime.

## Files

- Added `simulations/crystallization_sorting_engine/quantum_sorting_ledger.py`
  and three output CSVs.
- Added Section 14 to `bridges/crystallization_sorting_engine.md`, renumbering
  the closing sections and updating the masthead status and honesty boundary.
- Added a quantum-ledger section to
  `simulations/crystallization_sorting_engine/README.md`.
- Updated OP-30 and `STATUS.md`.

## Next

1. The \(\epsilon\)-approximate version: replace the sharp decoupling condition
   of Theorem 3-Q with an approximate one and carry the error through Theorem 5,
   so the trigger-time bound survives when the completion is only approximately
   correctable. This is the remaining quantum gap and it is the version any real
   gravitational mechanism would satisfy.
2. The last untouched OP-30 item: compute \(\gamma_k\) for the macrocell kernel
   in `simulations/cosmic_coordination_floor/` against an area-derived \(C_k\),
   turning Conjecture SE-1 into a number.
3. Test the slot-partition prediction on the QEC side: gauge or check-schedule
   adaptation inside a phase-protecting stabilizer or subsystem code.
