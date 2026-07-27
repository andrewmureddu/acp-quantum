# Session: Area-Derived Capacity in the Macrocell Toy

**Date:** 2026-07-26
**Branch:** `claude/singularity-sorting-mechanism-a7c917`
**Front:** OP-30, task (a); feeds OP-19 and OP-20
**Predecessors:** `sessions/2026-07-26_crystallization_sorting_engine.md`,
`sessions/2026-07-26_h2_sorting_efficiency_audit.md`,
`sessions/2026-07-26_coherent_information_ledger.md`

## Input

Andrew: "do the area-derived capacity in the macrocell toy."

This was the last untouched OP-30 item: compute the contraction rate for the
relational macrocell kernel, compare it against a capacity derived from the
Bekenstein-Hawking area law, and turn Conjecture SE-1 into a number.

## Method

`simulations/cosmic_coordination_floor/area_capacity_ledger.py` imports the
macrocell kernel unchanged. What is measured comes from the toy: the
contraction \(\gamma\), the exported record \(\sigma\), and the slot resolution
of the boundary record map. What is imported is the capacity in bits,
\(C_{\mathrm{area}}=A/(4\ln2)=4\pi M^2/(C_R^2\ln2)\) in Planck units, using the
toy's own compactness \(C_R=2M/R_{\mathrm{areal}}\).

Because the toy's boundary record is a deterministic function of the macrocell,
the one-step ledger with the current macrocell as reference is exact:
\(\delta_k=H(M_k)-I(M_k;M_{k+1})\), \(\sigma_k=I(M_k;R_{k+1})\),
\(\gamma_k=\sigma_k+\delta_k\).

**A component I built and then removed.** I first wrote a fixed-reference stock
ledger that propagated the full record history with branch pruning. It does not
work here: with 15 record values over 36 steps the branch count saturates any
affordable cap by step 4, the discarded mass exceeds 1 by step 12, and the
resulting export column goes negative — an impossible value for a genuine
ledger. Rather than ship a numerically broken component I deleted it, because
Theorem 1 gives the exact bound \(E_k\leq H(M_0)\) for all time, which is both
rigorous and stronger than any finite-horizon measurement for the purpose at
hand. The script and README say so explicitly.

## Result

Toy interior stock bound \(H(M_0)=2.909592\) bits. Boundary record map has 15
distinct tuples, so \(C_{\mathrm{slots}}=3.906891\) bits.

| Policy | mean \(\gamma\) | mean \(\sigma\) | mean \(\delta\) | \(\chi\) | peak \(\gamma\) | \(\gamma/C_{\mathrm{slots}}\) | BW-limited |
|---|---:|---:|---:|---:|---:|---:|---:|
| naked_collapse | 5.5445 | 1.5345 | 4.0100 | 0.27676 | 5.7525 | 1.4724 | 35/36 |
| hard_exclusion | 2.6707 | 1.0058 | 1.6649 | 0.37661 | 5.7510 | 1.4720 | 13/36 |
| horizon_transfer | 5.8275 | 2.2223 | 3.6053 | 0.38134 | 6.2154 | 1.5909 | 35/36 |
| quantum_completion | 6.0157 | 2.0294 | 3.9863 | 0.33735 | 6.3657 | 1.6294 | 35/36 |

Identity residual at most `8.9e-16` bits; \(\delta\geq\gamma-C\) never
violated, minimum slack `0.0961` bits.

### The negative finding, which is the useful one

**The toy is over-driven by its own record partition, not by the area law.**
Its kernel contracts 5.75-6.37 bits per step against a 3.907-bit slot capacity,
so Corollary 4.1 forces destruction and delivers it: \(\chi\) is 0.28-0.38 for
every policy. Even the quantum-completion policy destroys about two thirds of
what it contracts — not because its mechanism is wrong but because the toy's
boundary bins cannot resolve what its kernel merges.

The area law would permit far more: `18.13` bits at \(M=1,C_R=1\) (4.6 times
the slot capacity), `1813` bits at \(M=10\), and of order \(10^{77}\) bits for a
solar-mass hole. For the area capacity to fall below the toy's own interior
budget would require \(M<0.4006\) Planck masses, which is exactly where the
semiclassical area law stops meaning anything.

So: **this toy cannot test SE-1.** The bandwidth limit it exhibits is an
artifact of coarse boundary bins. The fix is specific rather than a vague call
for realism — the boundary record map needs resolution scaling with the
boundary area, of order \(A/4\) bits, rather than 15 fixed slots. That is now
the concrete next step for OP-19/OP-20.

### The positive finding, which I did not expect

The calibration exposes something the toy was never needed for. Take the
standard identifications: a horizon of area \(A\) has \(S_{\mathrm{BH}}=A/4\)
and about \(e^{S_{\mathrm{BH}}}\) interior microstates. Then Corollary 6.1
gives the quantum interior budget \(2S_{\mathrm{BH}}\), while a horizon record
of \(S_{\mathrm{BH}}\) qubits carries at most \(2S_{\mathrm{BH}}\) bits by
Theorem 4-Q and at most \(S_{\mathrm{BH}}\) once decohered by Theorem 7.

| \(M\) | \(S_{\mathrm{BH}}\) | budget \(2S\) | quantum capacity | classical capacity | \(\chi_{\max}\) cl. |
|---:|---:|---:|---:|---:|---:|
| 1 | 18.13 | 36.26 | 36.26 | 18.13 | 0.50 |
| 10 | 1813 | 3626 | 3626 | 1813 | 0.50 |
| \(10^3\) | 1.813e7 | 3.626e7 | 3.626e7 | 1.813e7 | 0.50 |
| \(10^{38}\) | 1.813e77 | 3.626e77 | 3.626e77 | 1.813e77 | 0.50 |

**Interior budget and quantum record capacity are equal at every mass, with
zero margin.** Granting the imported identifications, a black hole is exactly
the object whose boundary can losslessly sort its own interior and not one bit
more — and only if the record is quantum.

This revises SE-1 rather than confirming it. The conjecture supposed a crossing
\(\gamma=C\) somewhere and asked where. For a horizon the two are *equal*
identically, at every scale: gravity is the domain where the sorting engine
runs permanently at capacity, which is why the three strategies of Section 7 —
throttle, widen, buffer — are not refinements there but the entire available
response. The revised gravitational statement is recorded in the bridge and
marked ⚠ open.

### A methodological caution

\(\chi\) does not rank policies on its own. `hard_exclusion` posts a
competitive `0.37661` with the lowest mean contraction and only 13
bandwidth-limited steps, and is nonetheless the policy the parent toy rejects
for violating the future-entropy floor. Sorting efficiency is a third
independent axis alongside the floor and the Section 8 selectivity condition. A
policy can contract little, waste little, and still crystallize.

## Honesty boundary

The capacity in bits is imported, not derived; the toy supplies only the
compactness that feeds it. The microstate count behind the marginality table is
the standard one and is likewise imported. Nothing here proves that
gravitational focusing merges relational macrocells at the measured rate — the
measured rate is the toy's, and the toy's record map has just been shown to be
the wrong size by many orders of magnitude.

## Files

- Added `simulations/cosmic_coordination_floor/area_capacity_ledger.py` and
  four output CSVs.
- Added Section 15 to `bridges/crystallization_sorting_engine.md`, renumbering
  the closing sections, updating the masthead and the SE-1 discussion, and
  marking next-target 1 done with a specific successor.
- Added an area-capacity section to
  `simulations/cosmic_coordination_floor/README.md`.
- Updated OP-19, OP-20, OP-30, and `STATUS.md`.

## Next

1. Rebuild the macrocell toy's boundary record map so its resolution scales as
   \(A/4\), then re-run this ledger. Only then is the crossing test about
   gravity rather than about binning.
2. The \(\epsilon\)-approximate decoupling version of Theorem 3-Q carried
   through the trigger-time bound of Theorem 5 — the remaining quantum gap, and
   the version any real gravitational mechanism would satisfy.
3. On the QEC side, test the slot-partition prediction: gauge or check-schedule
   adaptation inside a phase-protecting stabilizer or subsystem code should move
   \(\chi\) where likelihood adaptation cannot.
