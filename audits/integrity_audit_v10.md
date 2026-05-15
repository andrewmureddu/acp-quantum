# ACP v10 Integrity Audit

**Date:** 2026-04-26
**Scope:** Re-audit of `paper/acp_main_v10.md` against the stale v07 audit findings, plus the A.20 / Schur-bridge Heisenberg reconciliation requested by OP-6.

---

## 1. Summary

The critical v07 issues are no longer blocking v10. Section 4.4 formal numbering is gapless, the step count in the introduction is current, Price/Fisher references are present, the T and σ notation clashes have been disambiguated, and the Lemma 4.2 qualification is now propagated into Theorem 4.3 by an explicit scope remark.

One remaining notation inconsistency was found and fixed during this audit: Prediction 7 used ε*(T) where the characteristic time was defined as T*. It now reads ε*(T*).

The audit also resolved OP-6. A.20 closes the Heisenberg connection as a reduction from an already-specified non-commutative two-MASA quantum partition to the ACP coordination floor. It does not derive the canonical commutation relation from ACP axioms alone. The Schur bridge and A.20 now state this distinction explicitly.

---

## 2. v07 Findings Rechecked

| v07 finding | v10 status | Notes |
|---|---|---|
| Introduction says "five steps" but lists six | Fixed | v10 now states seven steps, matching the expanded proof inventory through A.20. |
| Lemma 4.15 missing | Fixed | Lemma 4.15 is now the compounding lemma. |
| Theorem 4.18 missing | Fixed | Corollary 4.18 now exists as the Double Bind. |
| "Beyond T" should be "Beyond T*" | Fixed | The Section 4.4.6 prose already uses T*. |
| ε(t) / ε*(t) inconsistency | Fixed during this audit | Prediction 7 now uses ε*(T*) rather than ε*(T). The notation table uses ε*(t). |
| Price equation cited but not referenced | Fixed | Price (1970), Price (1972), and Fisher (1930) are present in References. |
| Lemma 4.2 qualification may propagate to Theorem 4.3 | Fixed | Remark 4.3a states the dissolution case is unconditional and the crystallization case inherits the strong-coarse-graining / timescale-separation condition. |
| σ overloaded between coarse-graining and entropy production | Fixed | Prigogine entropy production is σ_P in the main text and notation table. |
| T overloaded between dynamics and temperature | Fixed | Temperature is T_env in Axiom 1; T remains the time-evolution operator. |
| Corollary label "Restating Remark 4.6" | Fixed | The corollary no longer has the "Restating" label. |
| Section 7 "RESOLVED" headers | Fixed | Section 7 now lists genuine remaining open problems with contextual notes about resolved earlier gaps. |

---

## 3. Remaining Submission-Readiness Issues

These are not integrity blockers, but they remain before journal preparation:

1. The paper still has working-draft masthead text and internal versioning.
2. The paper still uses internal "Open problem" prose in the body. This is useful for the research draft, but a submission version should either formalize these as limitations or move some to a separate discussion section.
3. Appendix A.20 still contains a few explicitly marked conjectural physical extensions, especially Bekenstein and cosmic censorship. These are clearly flagged and do not weaken the Heisenberg reduction, but a submission venue may require moving them to a speculative outlook section.

---

## 4. OP-6 Reconciliation

The Schur bridge originally posed the uncertainty-principle connection as a five-step program:

1. rank(D) > 0 forces non-commutativity of the quantum operator algebra (still open in the first-principles direction).
2. Non-commutativity implies the Robertson uncertainty bound.
3. Stone-von Neumann fixes the canonical representation once the CCR is assumed.
4. Groenewold-van Hove makes the non-commutativity irremovable.
5. Symplectic rigidity gives the floor a geometric interpretation.

A.20 resolves steps 2 and the ACP interpretation of the floor: once a non-commutative two-MASA partition is specified, the Restraint-Power Theorem predicts a strictly positive coordination floor, and Robertson supplies its quantitative value κ/2. Therefore Heisenberg is the quantum-scale coordination floor in the ACP sense.

A.20 does not yet resolve step 1. The derivation of non-commutativity, or of the canonical commutation relation [Q, P] = iℏI, from rank(D) > 0 alone remains open. This residual issue is now tracked as OP-RP-5 in `bridges/restraint_power.md`.

---

## 5. Actions Taken

- Corrected `paper/acp_main_v10.md` Prediction 7 from ε*(T) to ε*(T*).
- Added the Schur/A.20 reconciliation note to `bridges/schur_complement.md` §6.4.
- Tightened `bridges/restraint_power.md` A.20.7.3 and A.20.9 to distinguish the proved reduction from the still-open first-principles derivation of the canonical commutator.
- Moved OP-6 and OP-8 to the resolved section of `OPEN_PROBLEMS.md`.
