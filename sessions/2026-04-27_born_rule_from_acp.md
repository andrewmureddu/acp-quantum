# 2026-04-27 — Conditional Born Rule from ACP

## Prompt

Andrew asked whether we can do a formal Born-rule derivation from ACP axioms
and to proceed with it.

## Work Completed

- Re-read the nearby quantum foundation material:
  - `bridges/restraint_power.md`;
  - `reductions/zurek.md`;
  - `bridges/dark_constraint_quantum_gravity.md`;
  - `bridges/cosmic_coordination_floor.md`.
- Added `bridges/born_rule_from_acp.md`.
- Added OP-21 to `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Main Formal Result

The right honest claim is conditional, not absolute.

The new bridge proves:

> once a measurement is represented as an orthogonal Hilbert-space branch
> decomposition, ACP-style branch axioms force the unique branch-weight rule
> \(W(v)=\|v\|^2\).

The branch axioms are:

1. mechanism-preserving invariance;
2. orthogonal additivity;
3. continuity and positivity;
4. normalization of the full premeasurement state.

The proof is short:

- BR-1 implies \(W(v)=f(\|v\|)\).
- BR-2 plus orthogonality gives
  \(f(\sqrt{x^2+y^2})=f(x)+f(y)\).
- Setting \(g(t)=f(\sqrt t)\) reduces this to the continuous Cauchy equation
  \(g(x+y)=g(x)+g(y)\).
- Normalization fixes the proportionality constant.

Therefore

$$
W(v)=\|v\|^2,
\qquad
p_i=W(\Pi_i|\psi\rangle)=\|\Pi_i|\psi\rangle\|^2
=\langle \psi|\Pi_i|\psi\rangle .
$$

For rank-1 projectors this is the usual Born rule
\(p_i = |\langle i|\psi\rangle|^2\).

## Why This Matters

This gives a real theorem rather than a metaphor:

- the Born weight is the unique additive conserved branch capacity on an
  orthogonal Hilbert branch decomposition;
- the ACP reading is that measurement branch weights are fixed by conservation
  and coarse-graining consistency, not by arbitrary probabilistic choice.

It also clarifies the exact frontier:

- the note does **not** derive Hilbert space, unitarity, or projective
  measurement from ACP alone;
- it shows that **given** those kinematics, ACP-style branch accounting singles
  out the squared norm uniquely.

## New Open Problem

Added OP-21:

> derive the Hilbert branch structure, unitary mechanism-preserving flow, and
> branch-weight axioms from ACP itself, rather than importing them from standard
> quantum theory.

This is now the cleanest route to a genuinely first-principles ACP derivation
of quantum probability.

## Next Step

Two viable continuations:

1. connect the branch-weight theorem to decoherence / pointer-state selection so
   the collapse side is tied back to `reductions/zurek.md`;
2. try the harder move: derive BR-1 and the Hilbert norm from ACP persistence
   and coordination-floor constraints, which would advance OP-21 directly.
