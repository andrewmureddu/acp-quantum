# Session log — 2026-07-06 — Closed preparability: PU-2 discharged as a theorem

## Context

Fifth same-day installment of the quantum-foundations push. Andrew green-lit
the queued PU-2 target: derive the purification bridge's central axiom
(record locatability — every admissible state has an extremal finite
composite extension) from CDT-style conservation rather than casting it.

## What was done

1. **New bridge:** `bridges/closed_preparability.md`.
   - The driving observation: PU-2 is a kinematic existence axiom, but
     conservation principles constrain processes. Since states are
     equivalence classes of preparations (OS-1/OS-2), translate the
     conservation demand to preparations.
   - **Axiom CL-1 (closed preparability):** every admissible state arises as
     \(\omega=\mathrm{tr}_E R(\varphi)\) for some finite record system
     \(E\), complete reference \(\varphi\in K_{SE}\), and reversible
     transformation \(R\) of the composite. ⚠ Flagged as an axiom — the
     preparation-facing sibling of UE-1, not yet a CDT theorem.
   - **Axiom CL-2 (blank initialization):** complete reference states are
     preparable (their mathematical existence is free by Minkowski).
   - **Lemma 3.1 (proved):** affine bijections with affine inverses map
     extreme points to extreme points — completeness is a dynamical
     invariant of the mechanism-preserving class, by convexity alone.
   - **Lemma 3.2 (proved):** under product-effect separation (LT-0) and
     conditional states, pure ⊗ pure is pure (marginal extremality plus
     conditional-state decomposition plus separation).
   - **Theorem 4.1 (proved):** CL-1 ⇒ PU-2 in two lines
     (\(\Omega:=R(\varphi)\) is complete with marginal \(\omega\)).
     Corollary 4.2: with CL-2 + LT-0 the reference may be a blank product —
     "initialize blanks, run a closed mechanism, discard the record."
   - **Remark 4.3 (tight factoring):** PU-2 ⇐ CL-1 always, and PU-2 ⇒ CL-1
     given transitive reversible action on complete states — i.e.
     PU-2 = CL-1 modulo composite branch homogeneity (HG-3 at the composite
     level). The geometry and conservation tracks interlock.
   - **Theorem 5.1 (proved):** classical theories violate CL-1: reversible
     transformations of a simplex are exactly alphabet permutations
     (affine bijections permute vertices and are determined by them), so
     closed classical dynamics map point masses to point masses and mixed
     states are never closed-preparable. The dynamical face of the
     classical-regress theorem: classical mixedness cannot be manufactured
     by any closed classical process.
   - **Proposition 5.2 (proved):** quantum theory satisfies CL-1 minimally
     (unitary from blanks to a purification; record dimension = rank).
   - §6: the OS-3 coin is a legitimate interface, but its closure must be
     non-classical; coin non-disturbance becomes a lemma target about
     product-preserving closed mechanisms.
   - Net reading (§7): one conservation principle, two shadows — inventory
     (PU-2) and closure (CL-1) — hinged by Lemma 3.1. The program's sole
     remaining conservation import is a single reversibility axiom
     (UE-1 ∧ CL-1) at one address.

2. **Cross-references:** update note in `bridges/purification_from_acp.md`
   §10; purification row of the reconstruction table in
   `bridges/hilbert_geometry_from_acp.md` updated.

3. **Trackers:** OP-21 statement/status extended in `OPEN_PROBLEMS.md`
   ("PU-2 reduced to the single reversibility axiom CL-1"); STATUS front 7,
   OP-21 headline, and changelog updated.

## Honesty boundary

- Proved: Lemmas 3.1/3.2, Theorem 4.1, Corollary 4.2, Theorem 5.1,
  Proposition 5.2, given the GPT frame plus stated composite structure.
- Axiomatic residue: CL-1 (and UE-1) — the reversibility of fundamental
  closed dynamics — remains underived from CDT; LT-0 is assumed for the
  blank-product form and is the open G3 item; PU-3 uniqueness reduced to
  Conjecture CP-C1 (fiber-wise composite branch homogeneity), open.

## Next steps

1. The reversibility residue: derive UE-1 ∧ CL-1 from CDT (no unaccountable
   one-way loss at any finite cut) — now the single conservation import.
2. Conjecture CP-C1 (uniqueness from fiber homogeneity).
3. LT-0 / local decodability (G3) — used by two bridges, selects the complex
   field, still owed its ACP derivation.
4. OP-30 items (cadence covariance C-1, hardware estimation) remain queued
   in parallel.
