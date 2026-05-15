# 2026-04-26 — v10 audit and Heisenberg reconciliation

## Context

Session goal: continue first-principles ACP Quantum formalization. Highest-value blocking item from `STATUS.md` was the stale v07 integrity audit, with OP-6 requiring a reconciliation between the Schur complement bridge's Heisenberg open problem and the newer A.20 Restraint-Power result.

## Work completed

1. Re-audited `paper/acp_main_v10.md` against the old v07 findings.
2. Added `audits/integrity_audit_v10.md`.
3. Fixed the remaining Prediction 7 notation inconsistency in the main paper:
   - changed ε*(T) to ε*(T*) in Section 6.7.
4. Added a reconciliation note to `bridges/schur_complement.md` §6.4.
5. Tightened `bridges/restraint_power.md` so A.20 no longer overstates what is proved:
   - A.20 proves that, given a non-commutative two-MASA partition, the Heisenberg/Robertson floor is the ACP coordination floor.
   - A.20 does not derive the canonical commutation relation from ACP axioms alone.
   - The residual first-principles quantum-kinematics task is now OP-RP-5.
6. Updated `OPEN_PROBLEMS.md`:
   - OP-6 moved to Resolved.
   - OP-8 moved to Resolved.
7. Updated `STATUS.md` to make `audits/integrity_audit_v10.md` the active audit and replace the v10-audit front with submission-readiness cleanup.

## Formal status

The Heisenberg connection is now correctly classified:

- **Proved reduction:** non-commutative two-MASA quantum partition + A.20 restraint-power machinery implies a strictly positive coordination floor, and Robertson supplies the quantitative value κ/2.
- **Still open:** derive non-commutativity or [Q, P] = iℏI from rank(D) > 0 and ACP axioms alone.

This distinction is important. It preserves the genuine ACP result while preventing the paper from claiming a first-principles derivation of quantum kinematics that has not yet been supplied.

## Next best steps

1. Submission-readiness cleanup of the main paper.
2. OP-14: replace toy quantum productive-interval proxy metrics with channel-native quantities.
3. OP-RP-5: begin the first-principles operator-algebra program for deriving when rank(D) > 0 forces non-commutativity.
