# 2026-05-10 - Operational-Time Relativity

## Prompt

Write a short formal bridge on operational-time relativity for ACP. Starting
from the existing use of operational time in the core theorem chain, define
candidate transformation laws or invariants between systems with different
operational tempos, clarify what would count as a `proper productive interval`,
and update `STATUS.md` plus `OPEN_PROBLEMS.md` if this creates a real new
problem rather than just commentary.

## Work Completed

- Read `STATUS.md`, `OPEN_PROBLEMS.md`, the core paper's operational-time
  section, and the Schur/QEC bridge passages where \(\tau_v\), per-cycle
  thresholds, \(q^*\), and \(\eta^*/(1-q^*)\) appear.
- Added `bridges/operational_time_relativity.md`.
- Defined operational tempo \(\nu_S=d\tau_S/dt\) and candidate
  reparameterization laws:
  - scalar structural quantities pull back as scalars;
  - loads and contraction/leakage rates transform as rate densities;
  - verification horizons transform as operational durations;
  - \(L\delta_v\), boundary membership, per-cycle information quantities,
    \(q^*\), and \(\eta^*/(1-q^*)\) are invariant under a valid
    reparameterization.
- Defined a proper productive interval as a connected interval of a system's
  own operational clock with finite tempo, two-boundary separation,
  capacity-load margin, memory with innovation, and record selectivity where a
  controller or environment is present.
- Added OP-29 because the cross-system theorem is real work, not commentary:
  the bridge still needs formal operational-time morphisms for systems with
  different tempos, coarse-grainings, and record channels.
- Updated `STATUS.md` with the new active bridge, active-front entry,
  open-problem headline, and changelog entry.

## Next

Prove or disprove the operational-time covariance theorem: characterize the
weakest transition-kernel and record-channel relation under which two systems
with different tempos realize the same ACP productive interval.
