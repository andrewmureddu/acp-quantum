# Session log — 2026-07-18 — algebraic defect refinement

## Intent

Eighth pull on the braided-clock thread: replace the commutator-norm
transparency defect (which the Experiment F counterexample showed can be
infinitely loose) with the correct algebraic object, and prove the
corresponding bound.

## What was proved

Added to `bridges/clock_syndrome_record_splitting.md`:

- **Definition 4.** Record monomials \(W=M_{i_n}\cdots M_{i_1}\), their
  POVM elements \(E_W=W^\dagger W\) (exactly the outcome probabilities of
  length-\(n\) adaptive schedules), and the filtered algebraic defect
  \(\zeta_n=\sup\{\sup_\theta\|[\Phi(X),U_\theta]\|:X\in\mathcal K_n,\
  0\le X\le I\}\) over the span of compressed record elements.
- **Proposition 6.1 (sharp dichotomy).** Clock-blindness for every finite
  schedule and every code state holds iff every \(\Phi(E_W)\) commutes
  with the clock rotation. The "only if" direction is constructive: a
  non-commuting Hermitian compression has a code state witnessing
  \(\theta\)-dependence of that record's probability.
- **Proposition 6.2 (sufficient condition).** If the compression of the
  full generated \(*\)-algebra lies in the clock commutant, blindness
  follows; for a QND instrument on one fixed observable \(A\) with
  \(\Phi(A)\propto P\), the algebra is \(\mathrm{span}\{I,A\}\) and the
  Experiment F counterexample becomes a corollary.
- **Proposition 6.3 (algebraic continuity bound).**
  \(\mathrm{TV}\le\zeta_n\) via subset POVM elements
  \(E_S\in\mathcal K_n\), hence
  \(I(\Theta;R)\le2\zeta_n\log_2|\mathcal R|+h_2(2\zeta_n)\). With
  \(\zeta_n\le2\tau\) this subsumes Proposition 5 up to a constant while
  assigning zero to the abelian case at every \(n\).
- **Remark.** The unfiltered \(\zeta_\infty\) saturates at 2 for any axis
  leak (the generated algebra contains \(\bar Z\) exactly), so the
  dichotomy is Eastin-Knill-like: all-or-nothing in the limit, with the
  quantitative content living in how fast \(\zeta_n\) grows.

## Numerical verification (Experiment G)

Exact enumeration of all \(2^n\) record POVM elements, compressed to the
codeword basis (`braiding_clock_algebraic_defect.csv`):

- Conjugated miscalibration: filtered defect exactly zero at every
  \(n\in\{1,4,8\}\) and both \(\mu\) values — the dichotomy classifies it
  correctly where the commutator norm (up to `0.246`) did not.
- Axis leak: the chain \(\mathrm{TV}\le\zeta_S\le\zeta_n\) holds in every
  cell, with the subset witness tight to a factor of 2
  (\(\mathrm{TV}=\zeta_S/2\) in most cells).
- Exact total variation grows like \(\sqrt n\): `0.030 / 0.061 / 0.087`
  at \(n=1,4,8\) (\(\mu=0.1\); ratios `2.04`, `2.91` vs \(\sqrt4,\sqrt8\)),
  confirming the martingale-type rate conjectured in Remark 2. A detail
  caught along the way: the records read \(\langle\bar Z\rangle\), so
  \(\theta=\pi\) is indistinguishable from \(\theta=0\) and the maximally
  distinguishing phase is \(\pi/2\).

## Files touched

- `bridges/clock_syndrome_record_splitting.md` (Definition 4, Proposition
  6, updated OP-30 section, renumbered open problems to section 9).
- `simulations/quantum_braiding_clock/` (Experiment G, README, new CSV).
- `OPEN_PROBLEMS.md` (OP-30 to open/partial++).
- `STATUS.md` (changelog).

## Next steps

- Prove the \(\sqrt n\) total-variation growth for structured weak-leak
  families (martingale / Azuma-style argument on the record process).
- OP-30(a) companion: \(\epsilon\)-approximate codes; OP-30(b): covariant
  reconciliation; OP-23: measured-trace replay.
