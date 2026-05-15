# 2026-04-27 — Conditional Unitary Evolution from ACP

## Prompt

Andrew asked to pick one of the imported quantum-kinematics ingredients and
work on it. I selected:

> unitary evolution between measurements.

This was the best next step because it sits immediately downstream of the new
Born-weight note and the existing ACP notion of mechanism-preserving
transformations.

## Work Completed

- Re-read the most relevant local material:
  - `bridges/born_rule_from_acp.md`;
  - `bridges/restraint_power.md`;
  - `reductions/zurek.md`.
- Added `bridges/unitary_evolution_from_acp.md`.
- Updated OP-21 in `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Main Formal Result

The note proves a clean conditional theorem.

Let \(F_t\) be a one-parameter family of ray transformations on a complex
Hilbert space. Assume:

1. reversibility and composition in time;
2. preservation of Born transition probabilities on rays;
3. continuity in time.

Then:

- Wigner's theorem gives a unitary-or-antiunitary lift of each \(F_t\);
- continuity from the identity excludes the antiunitary branch;
- the resulting between-measurement flow is unitary.

So the final statement is:

$$
F_t([\psi]) = [U_t\psi],
\qquad
U_{t+s}=U_tU_s,
\qquad
U_t \text{ unitary.}
$$

In finite dimensions this yields a self-adjoint generator:

$$
U_t=e^{-itH},
\qquad
i\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle ,
$$

or with physical units,

$$
i\hbar\frac{d}{dt}|\psi(t)\rangle = \hat H|\psi(t)\rangle .
$$

## ACP Interpretation

This note sharpens the older remark in `bridges/restraint_power.md` that
mechanism-preserving transformations are the ACP analog of closed unitary
evolution.

The translation is now explicit:

- mechanism-preserving interval = no branch collapse, no decohering trace-out,
  no change in the branch-accounting law;
- preserving Born transition structure = preserving the overlap geometry of the
  prediction space;
- continuous closed evolution = unitary flow.

So the new result pairs naturally with the Born-weight theorem:

1. branch weights are fixed by squared norm;
2. closed between-measurement evolution is fixed by unitary symmetry.

## Remaining Frontier

This is still conditional on imported Hilbert kinematics.

What remains open is stronger:

- derive Hilbert ray geometry from ACP persistence itself;
- derive preservation of transition probabilities rather than postulating it;
- derive measurement/effect structure rather than taking projective partitions
  as given.

That broader task is now tracked as OP-21 in its upgraded form:

> first-principles Hilbert branch structure / quantum kinematics from ACP.

## Best Next Step

The most natural continuation is now:

1. derive the tensor-product composition rule from ACP branch accounting and
   independent composition; or
2. derive projective / POVM measurement structure from ACP coarse-graining and
   decodability constraints.

The easiest of those two is probably the tensor-product rule, because the
Born-weight note already gives multiplicativity under independent composition.
