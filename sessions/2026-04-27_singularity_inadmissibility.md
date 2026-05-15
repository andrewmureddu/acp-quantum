# 2026-04-27 — Singularity Inadmissibility

## Prompt

Andrew sharpened the quantum-gravity direction:

> singularities are inadmissable. if they show up, there's a failure in the
> math. lets continue.

## Work Completed

- Read `STATUS.md` and `OPEN_PROBLEMS.md` first, per project startup routine.
- Rechecked the Schur complement bridge, restraint-power gravitational
  corollaries, and the dark-constraint quantum-gravity bridge.
- Added `bridges/singularity_inadmissibility.md`.
- Updated `bridges/dark_constraint_quantum_gravity.md`.
- Added OP-18 to `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Main Formal Move

The user constraint was translated into an admissibility principle:

> singularities are not physical states; they are failures of the effective
> description's admissible state space.

At the ACP/Schur level, this is already formal. If the internal block \(D\) is
singular, then

$$
Q/D=A-BD^{-1}B^T
$$

is undefined. In ACP variables this means at least one conditional direction has
reached the crystallization boundary:

$$
\lambda_{\min}(D)\to 0
\quad\Longleftrightarrow\quad
h_i(D)\to 0
\ \text{for at least one internal direction}.
$$

Total crystallization is the limiting case \(H(m'|m)\to 0\). Partial
singularity is already inadmissible for the original description because the
boundary law requires \(D^{-1}\) in every retained internal direction. Since
future-bearing dynamics require a nondegenerate interior block,

$$
0 < H(m'|m) < H_{\max},
$$

singular states are not admissible persistent states.

## Gravity Translation

The bridge note distinguishes three objects:

- **singularity:** inadmissible endpoint / failed state description;
- **naked singularity:** failed exterior boundary channel, because outside
  records depend on undefined interior data;
- **horizon:** candidate repair, converting direct exposure of undefined
  interior data into a finite structured boundary channel.

This links directly to the dark-constraint bridge: the singularity itself is not
the productive darkness. Horizon-bounded darkness is the structured constraint
that may keep exterior prediction finite while preserving interior privacy.

## Status

Added OP-18. The ACP/Schur part is formal; the GR/QG lift remains conjectural
and is explicitly marked that way.

## Next Step

Build a finite toy collapse model with three channels:

1. naked collapse: exterior likelihood depends on an undefined variable;
2. hard exclusion: singular histories are removed from the admissible class;
3. horizon transfer: the interior variable is replaced by a finite boundary
   register carrying mass/area-like charges.
