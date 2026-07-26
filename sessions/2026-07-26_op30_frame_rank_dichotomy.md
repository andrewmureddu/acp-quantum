# Session: OP-30 — Frame Rank and the Two Failure Modes

**Date:** 2026-07-26
**Front:** ACP quantum-gravity derivation program (priority: highest)
**Closes:** OP-30 (both questions)
**Continues:** `sessions/2026-07-26_semiclassical_collapse_failure.md`

## The problem

The previous session proved the Stage 2 collapse failure theorem but left an
honest hole. The entropy branch (Theorem A) rested on hypothesis (R), shape
regularity at scale \(\ell\), and the numerics showed (R) was false in the
generic case: the shape constant rose from \(c=1.086\) to \(c=251.8\) under
strong shear, and filamented collapse retained 8.095 bits of coarse entropy
against a 1.50-bit floor.

That mattered more than a footnote, because realistic astrophysical collapse is
not shear-free — so the branch carrying the ACP-native content was the branch
failing in the generic case.

OP-30 posed two questions: is there a shear-robust replacement for (R), and
does filamented collapse instead fail a *different* admissibility condition?

## Question 1: replace (R), don't rescue it

The defect in (R) is that it tracks \(\det J\), a single number, when the
object determining cell count is the full deformation spectrum.

**Lemma 4.** Any \(\ell\)-cell meeting a convex body \(K\) lies inside
\(K\oplus B_r\) with \(r=\ell\sqrt3\), so \(N_\Delta\ell^3\leq\mathrm{vol}(K\oplus B_r)\).
Steiner's formula expands that in the intrinsic volumes, which for an ellipsoid
with semi-axes \(s_i\) are the elementary symmetric polynomials. The expansion
then factorizes:

$$
\frac{e_3+\ell e_2+\ell^2 e_1+\ell^3}{\ell^3}
=
\prod_{i=1}^{3}\left(1+\frac{s_i}{\ell}\right).
$$

The factorization is exact, not asymptotic — checked symbolically before
committing to it. So (R\('\)) is a theorem rather than a hypothesis, and
Theorem A\('\) follows unconditionally:

$$
H_{\ell,\Delta}(m)\leq\ln c_3+\sum_i\ln\!\left(1+\frac{s_i}{\ell}\right).
$$

## Question 2: which condition actually fails

Theorem A\('\) makes the mechanism transparent, and the answer falls out
immediately. The right-hand side vanishes only when **every** \(s_i\) drops
below \(\ell\). But Lemma 2 guarantees only that the *product*
\(\det J=s_1s_2s_3\to0\).

> Focusing constrains the volume. It does not constrain the individual axes.
> Shear is exactly the difference between the two.

So define the frame resolution rank \(\mathrm{rank}_\ell(J)=\#\{i:s_i\geq\ell\}\).
If it drops below 3, the reference structure no longer supplies three
directions resolvable at scale \(\ell\), the smearing functions cannot resolve
the degenerate direction, and the bin map defining the macrocell is undefined
there.

The satisfying part: this is not a new axiom. It is the *nondegenerate
interior* condition of `bridges/singularity_inadmissibility.md` §2 —
\(\mathrm{rank}(D)>0\) and \(\kappa(D)<\infty\) — specialized to a
congruence-realized frame. The framework already contained the criterion that
shear-dominated collapse violates. It had simply never been connected to the
collapse kernel.

**Theorem E.** Since \(\det J\to0\) at the caustic forces \(s_3<\ell\), the
description *always* loses frame rank. It breaches the entropy floor only in
the special case \(\mathrm{rank}_\ell=0\). Exhaustive, mutually exclusive, and
requiring no shape hypothesis at all — strictly stronger than the entropy
branch it replaces.

| failure | \(\mathrm{rank}_\ell\) | clause violated | regime |
|---|---:|---|---|
| entropy floor breach | 0 | \(\mathrm{rank}(D)>0\) | near-isotropic |
| frame rank failure | 1 or 2 | \(\kappa(D)<\infty\) | shear-dominated (generic) |

## Numerical confirmation

Extended the simulation with singular values (closed-form symmetric 3x3
eigensolver, stdlib), `rank_ell`, the (R\('\)) bound, and \(c_3\).

| scenario | \(s_{\mathrm{final}}\) | \(\mathrm{rank}_\ell\) | \(\tau\) rank-def. | \(\tau_\times\) | \(H_{\mathrm{final}}\) | A\('\) ceiling | \(c_3\) | old \(c\) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| isotropic | (0.00118, 0.00118, 0.00118) | 0 | 1.843 | 1.8717 | 0.000 | 1.90 | 3.43 | 9.09 |
| moderate shear | (0.234, 0.234, 1.8e−05) | 2 | 1.6485 | 1.7294 | 4.221 | 5.33 | 3.44 | 23.0 |
| strong shear | (0.961, 0.961, 1.84e−05) | 2 | 0.900 | 0.9868 | 8.095 | 8.67 | 3.61 | 251.8 |
| unbound | (4.03, 4.03, 4.03) | 3 | none | none | 14.220 | 17.96 | 3.42 | 1.086 |

1. **(R\('\)) holds uniformly.** \(c_3\) is 3.43–3.61 across every scenario,
   where the old \(c\) spanned two orders of magnitude. The deformation
   spectrum is the right variable.
2. **Theorem A\('\) is tight**, not merely valid: 8.67 predicted vs 8.095
   measured under strong shear; 5.33 vs 4.221 moderate.
3. **The dichotomy holds with no exceptions.** \(\mathrm{rank}_\ell\) drops
   below 3 before the caustic in all three focusing runs, and hits 0 only in
   the isotropic run — precisely the only run that breaches the floor.
4. **The control stays admissible**: rank 3 throughout, all axes growing.

The final shear spectrum says it in one line: \(s_3\sim10^{-5}\ell\) while
\(s_1=s_2\approx10\,\ell\). Vanishing volume, 8 bits of coarse entropy, and no
ability to resolve its own third direction.

## What this changes for the program

The completion corollary gains a fourth acceptance condition, and it is
independent of the others: a mechanism can inject entropy at rate \(|\theta|\)
and still permit one axis to collapse. The requirement is \(s_i\geq\ell\) for
*every* \(i\) — arrest contraction in all directions, not merely in volume.

Since the generic astrophysical case is the shear-dominated one, this is the
acceptance test candidate completions will actually have to pass.

## Residual gap

Proposition E1 identifies frame rank failure with \(\kappa(D)\to\infty\) in the
Schur reading. Pinning \(D\) to the deformation spectrum requires the local
Gaussian approximation of `bridges/relational_observable_macrostate_kernel.md`
§8, whose regularity conditions are exactly **OP-3**. Recorded as structural
until OP-3 closes, and OP-3 is now flagged as load-bearing for the
quantum-gravity front rather than a Schur-bridge housekeeping item.

## Files touched

- **Updated** `bridges/semiclassical_collapse_failure.md` — new §11 (Lemma 4,
  Theorem A\('\), Definition + Proposition E1, Theorem E, verification);
  §12 corollary gains requirement 4; §1, §2, §6, §13 revised; sections
  renumbered
- **Updated** `simulations/semiclassical_collapse_failure/collapse_entropy_decay.py`
  — symmetric 3x3 eigensolver, singular values, `rank_ell`, (R\('\)) bound,
  \(c_3\)
- **Updated** `simulations/semiclassical_collapse_failure/README.md`
- **Updated** `OPEN_PROBLEMS.md` — OP-30 moved to Resolved with full trail;
  OP-3 upgraded; OP-18/19/20 cross-references
- **Updated** `STATUS.md`

## Next

1. Stage 5, boundary decodability — the next unproven rung of the ladder.
2. Candidate completion kernels against the now-four acceptance conditions.
3. OP-3, which has become load-bearing rather than peripheral.
