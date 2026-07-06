# Session log — 2026-07-06 — Hilbert branch geometry from ACP branch homogeneity

## Context

Andrew asked to explore the quantum-foundations-from-ACP front (STATUS front 7,
OP-21). The session reviewed the conditional kinematics quartet
(`born_rule_from_acp.md`, `unitary_evolution_from_acp.md`,
`tensor_product_from_acp.md`, `measurement_formalism_from_acp.md`) and found
that all four import complex Hilbert space, with every note naming the same
keystone gap: derive the branch geometry itself.

## What was done

1. **New bridge:** `bridges/hilbert_geometry_from_acp.md`.
   - Defined branch-magnitude spaces and three ACP geometry axioms:
     HG-1 normed prediction bookkeeping (linearity flagged as imported, gap
     G1), HG-2 finite records (from reality-reflective admissibility),
     HG-3 branch homogeneity (distinguishability-preserving symmetries fixing
     the origin act transitively on each capacity sphere; the branch-space
     form of coordination neutrality and the static shadow of UE-1–UE-3).
   - **Theorem 4.2 (proved, real case):** HG-1–HG-3 force the branch magnitude
     to be an inner-product norm, and the inner product is unique. Proof:
     Mazur–Ulam makes the HG-3 symmetries linear; the linear isometry group is
     compact; Haar averaging of an auxiliary inner product produces an
     invariant Euclidean norm; sphere-transitivity makes it proportional to
     the branch magnitude.
   - **Theorem 4.3 (complex case):** same conclusion conditional on
     complex-linear symmetries (Mazur–Ulam gives only real-linearity; part of
     gap G3).
   - **Remark 4.4:** without HG-2 the statement is the open Banach–Mazur
     rotation problem, so ACP finite-record admissibility is doing real
     mathematical work, not just simplifying.
   - **Corollary 4.5:** the Born note's Lemma 4.1 (weight depends only on
     capacity) is derived from HG-3 plus G-invariance, so BR-1 is no longer an
     independent import in the Born chain.
   - **Propositions 5.1–5.2:** exclusivity is derived, not primitive.
     Weight-additivity is orthogonality in the real case; in the complex case
     full orthogonality is equivalent to *phase-robust* additivity under
     mechanism-preserving rephasing, sharpening BR-2.
   - **§6:** field selection is open (Conjecture HG-C1): branch homogeneity is
     field-blind; the designated ACP-native selector is local decodability of
     composition, continuous with the TP axioms (external anchors: Araki,
     Wootters, Hardy–Wootters).
   - **§7:** reduction map from ACP principles onto the Hardy / CDP /
     Masanes–Müller reconstruction axioms, classifying each as ACP-forced,
     ACP-plausible, or open, and restating OP-21 as a finite lemma list.
   - **§9:** residual gaps named G1 (linear prediction space), G2 (resolution
     limit / infinite dimensions), G3 (complex structure and field selection),
     G4 (reconnection to relational gravitational sector spaces).

2. **Cross-references:** added update pointers to the open-direction sections
   of all four quartet notes.

3. **Trackers:** OP-21 upgraded to Partial++++ in `OPEN_PROBLEMS.md` (statement
   rewritten to include the homogeneity theorem and gaps G1–G4); STATUS front 7,
   OP-21 headline, header date, and changelog updated.

## Honesty boundary

- Proved: Theorems 4.2/4.3 (4.3 conditional on complex-linearity),
  Corollary 4.5, Propositions 5.1–5.2, given HG-1–HG-3.
- Imported/open: linear structure of the prediction space (G1); the
  infinite-dimensional/resolution limit (G2); complex structure and field
  selection (G3, Conjecture HG-C1); gravitational reconnection (G4). The
  reconstruction-axiom mapping in §7 is classificatory, not a theorem.

## Next steps (recorded in the bridge's §10)

1. Attack G1 operationally: ACP-admissible record statistics ⇒ compact convex
   state space with finitely many perfectly distinguishable extreme points.
2. Formalize local decodability and attempt Conjecture HG-C1.
3. Prove the purification row of the §7 table from restraint-power
   conservation.
4. State HG axioms for the relational macrostate kernel's sector spaces (G4).
