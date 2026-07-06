# Session log — 2026-07-06 — Purification from ACP conservation: the classical regress

## Context

Third same-day installment of the quantum-foundations push (after
`sessions/2026-07-06_hilbert_geometry_from_acp.md` and
`sessions/2026-07-06_operational_state_space_from_acp.md`). Andrew green-lit
the purification target: the most powerful axiom in the CDP reconstruction
and the most ACP-resonant, now attackable because the GPT frame is derived.

## What was done

1. **New bridge:** `bridges/purification_from_acp.md`.
   - ACP-cast of the CDP purification postulate as a conservation principle,
     stated as three axioms: PU-1 mixedness is missing ensemble records
     (extreme = complete), PU-2 record locatability — no unlocated
     missingness: every admissible state has a completion, i.e., an extremal
     state of a finite composite with the given state as marginal
     (⚠ explicitly flagged as an axiom *casting* motivated by restraint-power
     conservation and reality-reflective admissibility, not a CDT theorem),
     PU-3 minimal records — completions unique up to reversible record-side
     symmetry (restraint on the record channel).
   - **Theorem 4.1, classical regress (proved):** in a simplex theory with
     classical composition (joint distributions on product alphabets), every
     finite classical extension of a mixed state is mixed, because marginals
     of point masses are point masses. Record location never terminates
     classically.
   - **Corollary 4.2, classical exclusion (proved):** mixed states inside the
     productive interval + PU-2 + classical composition are jointly
     inconsistent; hence ACP conservation with finite records forces
     non-classical composites — complete states with mixed marginals
     (entanglement-like structure) must exist. This is the program's first
     quantum/classical fork result.
   - **Theorems 5.1–5.2 and Proposition 5.3 (proved):** finite-dimensional
     quantum theory satisfies the axioms tightly: purifications exist iff
     \(\dim\mathcal H_E\ge\mathrm{rank}\,\rho\) (minimal record dimension =
     rank), the minimal record's entropy equals the missing information
     (Schmidt symmetry), and any two purifications on the same record system
     differ by a record-side unitary.
   - Readings: the classical trilemma (dangling missingness / infinite
     regress / triviality) as a kinematic shadow of the CDT; entanglement as
     conservation infrastructure, the kinematic companion of gravitational
     boundary records; the purifier as a KL-style legitimate controller.
   - Reconstruction payoff: with the frame derived (G1a), classical
     realizations excluded (this note), the residual selection of quantum
     theory is the remaining CDP rows: sharp records, ideal compression,
     local discriminability (= G3), causality — plus the CDT derivation of
     PU-2 itself.

2. **Cross-references:** purification row updated in the reconstruction table
   of `bridges/hilbert_geometry_from_acp.md`; update paragraph in
   `bridges/operational_state_space_from_acp.md` §10.

3. **Trackers:** OP-21 statement/status extended in `OPEN_PROBLEMS.md`
   ("classical exclusion proved in G1b"); STATUS front 7, OP-21 headline, and
   changelog updated.

## Honesty boundary

- Proved: Theorem 4.1, Corollary 4.2 (given the classical-composition
  definition, which is flagged as load-bearing), Theorems 5.1–5.2,
  Proposition 5.3.
- Cast, not derived: PU-2 is the CDP purification postulate with an ACP
  motivation; deriving it from CDT conservation for persistent record
  channels is the named hard core.
- Not claimed: quantumness. Corollary 4.2 excludes simplex theories only;
  selection among non-classical GPTs still requires the remaining
  reconstruction rows.

## Next steps (recorded in the bridge's §10)

1. Derive PU-2 from CDT via the Stinespring-direction route: model the
   discarded OS-3 coin as a physical record channel inside a closed
   mechanism-preserving composite.
2. Sharp records lemma (shared with the state-space bridge).
3. Local discriminability as ACP boundary decodability (G3 / HG-C1).
4. Gravitational lift of PU-2: interior mixedness located on boundary
   records, compared against the quantum-completion policy in
   `simulations/cosmic_coordination_floor/`.
