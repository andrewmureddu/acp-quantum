# Session: Semiclassical Collapse Failure Theorem

**Date:** 2026-07-26
**Front:** ACP quantum-gravity derivation program (priority: highest)
**Closes:** Stage 2 of the derivation ladder; Stage B of the coordination-floor
roadmap; the named next step of OP-18 and OP-19
**Opens:** OP-30

## What was chosen and why

Four documents named the same missing step — Stage 2 of
`bridges/quantum_gravity_derivation_program.md`, Stage B of
`bridges/cosmic_coordination_floor.md`, OP-18, and OP-19 — so the target was
not in doubt.

The existing statement was Proposition 2 of
`bridges/relational_observable_macrostate_kernel.md`. It is honest but weak in
a specific way: it *assumes* that a positive-measure subset of the initial cell
reaches an inadmissible singular set before \(\Delta\), which is most of the
content, and leaves the entropy branch qualitative. The work of this session
was to derive that hypothesis instead of assuming it.

## The move that made it work

The unlock was noticing that the relational reference structure
\(\mathcal F_\ell\) — defined in the kernel bridge as a finite set of clocks,
rods, and boundary cuts — *is a congruence* when physically realized. That is
the object the Raychaudhuri equation governs. Once the frame is a congruence,
the focusing theorems speak directly to the ACP kernel rather than by analogy.

The second observation is that \(d(\ln\delta V)/d\tau=\theta\) is already the
rate of change of a log-measure, which is the functional form of an entropy
drift rate. This gives the identification:

> the expansion scalar \(\theta\) is the CDT crystallization drift rate,
> written in geometric variables.

This is the sharpest contact the program has made with general relativity.

## What was proven

`bridges/semiclassical_collapse_failure.md`:

- **Lemma 1** (volume law) — exact, no energy condition needed.
- **Lemma 2** (quantitative focusing) — \(\theta\) non-increasing;
  \(\theta\leq-3\alpha/(3-\alpha\tau)\); caustic by \(\tau_\times\leq3/\alpha\);
  \(\delta V\leq\delta V_0e^{-\alpha\tau}\) uniformly and
  \(\delta V\leq\delta V_0(1-\alpha\tau/3)^3\) sharply. The exponent 3 is the
  spatial dimension, and for a homogeneous dust ball \(\delta V\propto a^3\).
- **Lemma 3** (coarse-graining bound) plus hypothesis **(R)**, shape regularity
  at scale \(\ell\).
- **Theorem A** (entropy floor breach) — decay at rate at least \(\alpha\) nats
  per unit proper time; explicit breach time; \(H=0\) exactly at the caustic.
- **Theorem B1/B2** (normalization failure) — frame tier and spacetime tier,
  kept deliberately separate.
- **Theorem C** — the collapse failure trichotomy. This is the Stage 2 theorem.
- **Proposition D** (shear trade-off) — why the disjunction is the right form.
- **Corollary** (forced completion) — deadline \(3/\alpha\), rate \(|\theta|\),
  decodable discharge, shear robustness.

## Two deliberate choices about honesty

**Geodesic incompleteness, not curvature divergence.** The singularity theorems
prove incompleteness; curvature blow-up is a separate and less securely
established matter. Stating the theorem in terms of incompleteness and frame
breakdown means it rests on what is actually provable — and it turns out ACP's
*finite continuation* admissibility condition is exactly the one gravity
violates, while the *finite observables* condition (curvature) is the weaker
one. That is a strengthening of the framework's position, not a concession, and
`bridges/singularity_inadmissibility.md` §9 now records it.

**Two tiers of Theorem B kept separate.** A caustic is a breakdown of a chosen
congruence, not necessarily of spacetime; one can often re-choose the frame.
B1 alone therefore says *this description* has failed — which is precisely the
reading of singularities the project already holds. B2 (Penrose) is what rules
out repair by re-description within classical GR. Conflating them would be an
overclaim, and keeping them apart is what makes the ACP trigger fire earlier
than the curvature singularity, which is what "redistribution before the floor
is breached" requires.

## Numerical verification

`simulations/semiclassical_collapse_failure/` integrates the exact Jacobi
deviation equation \(\ddot J=-\mathcal R J\) with a self-consistent dust source
\(\mathrm{tr}\,\mathcal R=\kappa/\det J\), so the strong energy condition holds
by construction. Taking the trace of \(\dot B=-\mathcal R-B^2\) reproduces
Raychaudhuri identically — this is congruence kinematics, not an analogy. Pure
stdlib, matching project convention.

**Integrator validated** against the closed-form isotropic dust collapse time:
analytic `1.871746`, simulated `1.8717`.

| scenario | \(\sigma_0\) | \(H_{\mathrm{final}}\) | slope | bound | \(\tau\) breach | \(\tau_\times\) | max \(c\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| isotropic | 0.00 | 0.000 | −5.563 | −0.866 | 1.8621 | 1.8717 | 9.09 |
| moderate shear | 0.12 | 4.221 | −4.477 | −0.866 | none | 1.7294 | 23.0 |
| strong shear | 0.45 | 8.095 | −3.920 | −0.866 | none | 0.9868 | 251.8 |
| unbound expansion | 0.00 | 14.220 | +0.376 | n/a | none | none | 1.086 |

Initial entropy `11.963` bits throughout; floor `1.50` bits; \(3/\alpha=5.0\).

Theorem C holds in every focusing run. Theorem A's bound holds but is
conservative by 4.5–6.4x, because self-consistent dust drives \(\theta\) far
below \(-\alpha\) rather than holding it at the initial value.

## The honest negative result

Hypothesis (R) fails under shear, and it fails hard. The shape constant rises
`1.086 -> 23.0 -> 251.8` while the image still has more than one cell of
volume. Consequently only the isotropic run breaches the entropy floor at all;
the shear runs are still at `4.221` and `8.095` bits when the frame breaks.

Filamented collapse has vanishing volume and high coarse entropy at the same
time. This is Proposition D: shear enters Raychaudhuri with the same sign as
the energy term so it *accelerates* the caustic, while the anisotropic
distortion it causes *degrades* (R). The two effects are the same quantity
acting on the two branches in opposite directions, which is why the disjunction
is stable even though neither disjunct is.

This matters more than a footnote, because realistic astrophysical collapse is
not shear-free — so the branch carrying the ACP-native content is the branch
that fails in the generic case. Logged as **OP-30** with two concrete routes: a
deformation-spectrum replacement for (R) using the singular values of \(J\), or
the more interesting possibility that filamented collapse breaches
admissibility through reference-frame failure rather than through the entropy
floor. A congruence one cell thick in some direction cannot support the
relational observables that define its own macrocell.

## Two bugs found and fixed during the numerics

Both were in the simulation, and both would have produced wrong conclusions.

1. **Fixed-step integration jumped through the caustic.** With `dt` constant,
   RK4 stepped past \(\det J=0\) and re-emerged with \(\det J>0\) growing
   without bound — an artifact presented as a continuation. Caught because the
   control scenario reported a floor breach at \(\tau=3.81\) while also
   reporting maximum final entropy, which is contradictory. Fixed by triggering
   on \(\theta\) (monotone under the focusing hypotheses) and shrinking the step
   to hold \(|\theta|\,dt\) below 5%.
2. **The shape constant was measured in the degenerate regime.** Once
   \(\delta V<v_\ell\), \(c=N v_\ell/\delta V\) diverges trivially because
   \(N\geq1\) — that is crystallization, not a failure of shape regularity.
   Restricting the measurement to \(\delta V\geq v_\ell\) is what revealed the
   real signal (`251.8` under shear versus `1.086` for the control); before the
   fix, the strong-shear run misleadingly reported a *lower* constant than the
   isotropic one.

Separately, the original "expanding" control was gravitationally bound and
recollapsed, so it was not a non-focusing control at all. It needed
\(\theta_0>3\sqrt{2\kappa/3}=1.732\) to be unbound.

## Files touched

- **Added** `bridges/semiclassical_collapse_failure.md`
- **Added** `simulations/semiclassical_collapse_failure/collapse_entropy_decay.py`
- **Added** `simulations/semiclassical_collapse_failure/README.md`
- **Added** `simulations/semiclassical_collapse_failure/outputs/` (2 CSVs)
- **Updated** `bridges/quantum_gravity_derivation_program.md` (Stage 2 marked
  proven; anchor list; near-term work)
- **Updated** `bridges/relational_observable_macrostate_kernel.md` (Proposition
  2 marked superseded)
- **Updated** `bridges/cosmic_coordination_floor.md` (Stage B complete;
  Criterion 1 and §12 updated)
- **Updated** `bridges/singularity_inadmissibility.md` (§9)
- **Updated** `OPEN_PROBLEMS.md` (OP-18, OP-19, OP-20; added OP-30)
- **Updated** `STATUS.md`

## Next

1. **OP-30**, and specifically its question 2 — whether filamented collapse
   fails admissibility through the reference frame rather than the entropy
   floor. An affirmative answer would mean the entropy floor is not the only
   ACP boundary gravitational collapse can hit, and would connect this work to
   `bridges/operational_time_relativity.md`.
2. Instantiate candidate completion kernels against the corollary's four
   acceptance conditions, which now include the rate condition.
3. Stage 5 (boundary decodability) is the next unproven rung.
