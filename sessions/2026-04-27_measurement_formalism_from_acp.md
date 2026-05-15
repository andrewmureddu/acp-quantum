# 2026-04-27 — Conditional Measurement Formalism from ACP

## Prompt

After completing the conditional tensor-product note, I continued directly to
the remaining local ingredient:

> projective / POVM measurement formalism.

This was the natural next step because the other three local pieces were now in
place:

1. branch weights;
2. closed unitary flow;
3. tensor-product independent composition.

## Work Completed

- Added `bridges/measurement_formalism_from_acp.md`.
- Updated OP-21 in `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Main Formal Result

The note proves a conditional measurement theorem in two stages.

### Stage 1: general boundary resolution gives POVMs

Model a measurement outcome \(i\) as a map

$$
m_i(\sigma)
$$

from positive branch operators \(\sigma\ge 0\) to nonnegative outcome weights.
Assume:

1. positivity;
2. linearity on the positive cone;
3. normalization:
   \(\sum_i m_i(\sigma)=\mathrm{Tr}(\sigma)\).

Then there exist unique positive operators \(E_i\) such that

$$
m_i(\sigma)=\mathrm{Tr}(E_i\sigma),
\qquad
E_i\ge 0,
\qquad
\sum_i E_i=I .
$$

So the general ACP-compatible local measurement law is exactly a POVM.

### Stage 2: ideal sharp resolution gives projectors

Add the sharp-sector assumptions:

- each outcome is certain on its own resolved sector;
- exclusive across distinct sectors;
- the sectors are complete and orthogonal.

Then the POVM effects reduce to

$$
E_i=P_i ,
$$

the orthogonal projectors onto those resolved sectors.

So ideal sharp measurement is the projective special case of the more general
POVM law.

## Update Rule

I also added the minimal sharp-instrument proposition:

if the selected measurement outcome preserves states already in the resolved
sector, removes only inter-sector coherence, and adds no in-sector kick, then
the canonical selective update is Lüders:

$$
\mathcal I_i(\rho)=P_i\rho P_i,
\qquad
\rho_i=\frac{P_i\rho P_i}{\mathrm{Tr}(P_i\rho)} .
$$

## Program Status After This Note

This completes the conditional local quantum-kinematics quartet:

1. `bridges/born_rule_from_acp.md`: branch weights;
2. `bridges/unitary_evolution_from_acp.md`: closed unitary flow;
3. `bridges/tensor_product_from_acp.md`: independent composition;
4. `bridges/measurement_formalism_from_acp.md`: boundary resolution.

So the remaining frontier is now much cleaner than it was at the start of the
session:

> derive the complex Hilbert branch geometry itself from ACP persistence,
> coordination-floor, and branch-accounting requirements.

## Next Step

The next serious target should not be another conditional local theorem. It
should be the harder first-principles problem now exposed by OP-21:

- why the prediction geometry is complex Hilbertian rather than merely some
  other normed linear space.
