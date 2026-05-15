# Turbulence as an ACP Admissibility Test

*Status: exploratory bridge. Upgrades the lightweight Navier-Stokes entry in
`special_cases/acp_special_cases_v03.md` by applying the
reality-reflective-mathematics criterion. This is not a solution of the
Navier-Stokes regularity problem.*

Companion notes: `bridges/reality_reflective_mathematics.md`,
`reductions/prigogine.md`, `reductions/multiscale_rg.md`, and
`special_cases/acp_special_cases_v03.md` section 5.3.

---

## 1. Thesis

Turbulence is a sharp test for the ACP admissibility criterion because it
separates three questions that are often conflated:

1. Are the governing equations formally valid?
2. Which finite observables actually couple the mathematics to fluid records?
3. Which structures persist under coarse-graining, Reynolds-number change, and
   measurement limitation?

The existing special-cases catalog maps:

- laminar flow to crystallization;
- fully developed isotropic turbulence to dissolution;
- transitional/structured turbulence to the productive interval.

That mapping is directionally useful but too blunt. Real high-Reynolds-number
turbulence is not structureless. It contains coherent vortices, sheets, jets,
streaks, intermittency, and a scale-local energy cascade. Therefore high
Reynolds number alone is not the dissolution boundary.

The corrected ACP reading is scale-resolved:

> Turbulence persists by maintaining an inertial-range productive interval
> between large-scale laminar/coherent constraint and small-scale dissipative
> decorrelation.

At each scale \(\ell\), the flow can be laminarized, productively turbulent, or
effectively dissolved relative to the chosen observables.

## 2. Scale-Resolved Variables

Let \(u(x,t)\) be an incompressible velocity field on a domain with boundary
conditions and forcing. Let \(\ell\) denote a coarse-graining scale.

Define a scale-\(\ell\) macrostate

$$
m_\ell(t)
=
\left(
\bar u_\ell,
E_\ell(k),
\Pi_\ell,
\omega_\ell,
\mathcal C_\ell
\right),
$$

where:

- \(\bar u_\ell\) is the coarse-grained velocity field;
- \(E_\ell(k)\) is the resolved energy spectrum;
- \(\Pi_\ell\) is the inter-scale energy flux through scale \(\ell\);
- \(\omega_\ell=\nabla\times \bar u_\ell\) is resolved vorticity;
- \(\mathcal C_\ell\) is a coherent-structure inventory, e.g. vortex tubes,
  sheets, streaks, jets, or boundary-layer structures at that scale.

The relevant conditional entropy is

$$
H_\ell
=
H(m_\ell(t+\Delta t)\mid m_\ell(t)).
$$

The relevant record channel is any finite measurement or simulation record:

$$
P(R_\ell \mid u),
$$

where \(R_\ell\) may be particle-image velocimetry, hot-wire measurements,
pressure probes, DNS samples, LES filtered fields, or structure-function
estimates.

## 3. ACP Regimes for Turbulence

The productive-interval classification should be made at scale \(\ell\), not
only at the global Reynolds number.

| ACP regime | Turbulence condition | Information condition |
|---|---|---|
| Crystallization \(C_\ell\) | laminarized or overcontrolled scale; perturbations damp; \(\Pi_\ell\approx 0\) | \(H_\ell\to 0\) |
| Productive interval \(P_\ell\) | inertial-range structured turbulence; coherent structures plus active flux | \(0<H_\ell<H_{\max}\), \(I(\Pi_\ell;R_\ell)>0\) |
| Dissolution \(D_\ell\) | decorrelated/equipartitioned/unresolved scale; records do not predict future macrostates | \(H_\ell\to H_{\max}\), \(I(m_\ell(t);m_\ell(t+\Delta t))\to 0\) |

Thus the inertial range is not "the chaotic side." It is the ACP productive
interval in its cleanest fluid form:

$$
0 < H_\ell < H_{\max},
\qquad
\Pi_\ell > 0,
\qquad
I(\Pi_\ell;R_\ell)>0.
$$

Laminar flow fails by excessive constraint. Thermalized or observationally
unresolved small-scale flow fails by loss of decodable predictive structure.

## 4. Reality-Reflective Mathematics Test

Apply the admissibility conditions from
`bridges/reality_reflective_mathematics.md` to turbulence.

**A1. Finite observables.** Velocity increments, energy spectra, structure
functions, dissipation rates, and pressure statistics must remain finite at
the model's resolution:

$$
\langle |\delta_\ell u|^p\rangle < \infty,
\qquad
E(k)<\infty,
\qquad
\varepsilon=\nu\langle |\nabla u|^2\rangle < \infty.
$$

Blow-up is not a physical state in this register. It is an admissibility
failure of the effective description unless replaced by a finite regularizing
scale or a new state space.

**A2. Normalizable record channel.** The measurement or simulation procedure
must define a finite probability law over records:

$$
P(R_\ell|u)
$$

with explicit resolution, noise, and sampling window.

**A3. Nondegenerate continuation.** The model must retain finite predictive
structure over at least one eddy-turnover time:

$$
\tau_\ell \sim \ell/\delta_\ell u,
\qquad
0<H_\ell(m_\ell(t+\tau_\ell)|m_\ell(t))<H_{\max}.
$$

**A4. Finite verification.** Predictions must be checked against records over
a finite verification scale, not infinite-resolution fields:

$$
R_\ell(t:t+\tau_\ell).
$$

**A5. Perturbable record coupling.** Changes in forcing, boundary condition,
Reynolds number, roughness, or rotation/stratification must change the record
distribution:

$$
D_{\mathrm{KL}}
\left(
P(R_\ell|do(\mathrm{Re}))
\;\|\;
P(R_\ell|do(\mathrm{Re}'))
\right)>0.
$$

**A6. Non-totalizing remainder.** A closure model should not pretend to
capture the full microstate. It should preserve residual uncertainty in
unresolved phases while remaining informative about fluxes and future
coarse-grained records:

$$
I(\Pi_\ell;R_\ell)>0,
\qquad
H(u_{<\ell}\mid R_\ell,\Pi_\ell)>0.
$$

This is the turbulence analogue of "learn syndrome, not logical state." A
useful closure learns enough about energy transfer to predict the resolved
flow, not the exact unresolved velocity field.

## 5. The Closure Problem as ACP

The famous practical problem of turbulence is closure: finite records of the
resolved flow do not determine the effects of unresolved scales without a
model.

ACP separates three closure failures.

**Underclosed closure: dissolution.** The unresolved scales dominate the
resolved future, so the current resolved macrostate carries little information:

$$
I(m_\ell(t);m_\ell(t+\Delta t))\approx 0.
$$

The closure has not extracted a decodable syndrome of the cascade.

**Overclosed closure: crystallization.** The closure suppresses fluctuations so
strongly that the resolved flow becomes artificially laminar or locked into a
single dissipative pathway:

$$
H_\ell\to 0.
$$

Many eddy-viscosity closures risk this failure when they erase coherent
structures while reducing mean error.

**Productive closure.** The closure preserves a nonzero flux record and
nonzero future-bearing entropy:

$$
I(\Pi_\ell;R_\ell)>0,
\qquad
0<H_\ell<H_{\max},
\qquad
\varepsilon_{\mathrm{pred}}\ \text{bounded}.
$$

This gives a clean ACP version of the turbulence modeling target: the closure
should expose the cascade's syndrome without collapsing the flow's unresolved
interior.

## 6. Inertial Range as Productive Interval

Kolmogorov-style inertial-range scaling is reality-reflective mathematics in
the ACP sense because it is not a pointwise solution. It is an invariant record
law under coarse-graining:

$$
E(k)\sim C_K \varepsilon^{2/3}k^{-5/3}
$$

in the idealized homogeneous/isotropic regime, with known intermittency
corrections in real flows.

The ACP reading is:

- the forcing range is too constrained by boundary injection;
- the dissipation range is too dominated by viscous erasure;
- the inertial range preserves a finite flux and nondegenerate scale-to-scale
  uncertainty.

In scale-tower language, the inertial range is a moving productive interval:

$$
\ell_\eta \ll \ell \ll L,
$$

where \(L\) is the forcing scale and \(\ell_\eta\) is the Kolmogorov scale.
Increasing Reynolds number does not simply push the whole flow toward
dissolution. It widens the number of scales on which \(P_\ell\) can exist.

## 7. Kolmogorov Cascade as Uncertainty Allocation

The uncertainty-allocation reading makes the Kolmogorov cascade sharper. The
small-scale fluctuations are not waste relative to the large-scale flow. They
are the structured innovation channel through which injected energy remains
mobile rather than locking into a single coherent mode.

The optimized object is not a scalar turbulence level. It is a scale-indexed
allocation:

$$
N(k)
\quad\text{or equivalently}\quad
N_\ell,
\qquad
k\sim \ell^{-1}.
$$

The shape of this allocation is the physical content. A theory that predicts
"some turbulence" has not said much. A theory that predicts how uncertainty is
distributed across wavenumber has made a world-facing claim.

The relevant control parameter is not only the global Reynolds number

$$
\mathrm{Re}=\frac{UL}{\nu},
$$

but the scale-local Reynolds number

$$
\mathrm{Re}_\ell
=
\frac{\delta_\ell u\,\ell}{\nu}.
$$

Low \(\mathrm{Re}_\ell\) is viscous overconstraint: perturbations are erased and
\(\Pi_\ell\approx 0\). Very high \(\mathrm{Re}_\ell\) can be dissolution
relative to a structure-blind record channel: the resolved records no longer
decode the relevant future macrostate. The inertial range is the middle regime
where \(\mathrm{Re}_\ell\) is large enough for nonlinear transfer but the record
channel still resolves flux-bearing structure:

$$
0<H_\ell<H_{\max},
\qquad
I(\Pi_\ell;R_\ell)>0,
\qquad
I(m_\ell(t);m_\ell(t+\tau_\ell))>0.
$$

In this sense, the cascade supplies an adaptive allocation. If a closure
removes subgrid fluctuation entirely at some scale, it risks crystallization
there:

$$
N_\ell=H(R_{\ell,t+\tau_\ell}\mid Z_{\ell,t})\to 0,
\qquad
\Pi_\ell\to 0.
$$

If it replaces subgrid structure with uncorrelated noise at some scale, it
risks dissolution there:

$$
N_\ell>0,
\qquad
S_\ell=I(\Pi_\ell;R_{\ell,t+\tau_\ell}\mid Z_{\ell,t})\to 0.
$$

A productive closure keeps the allocation structured:

$$
0<S_\ell\leq N_\ell<H(R_{\ell,t+\tau_\ell}),
$$

with \(S_\ell\) concentrated in flux, strain, vorticity, coherent-structure
features, and backscatter events rather than in arbitrary microstate detail.
This is the fluid analogue of the QEC rule: extract the syndrome of the
cascade, not the full unresolved logical state of the fluid.

This reframes the role of the Kolmogorov \(-5/3\) law. Its importance is not
the magnitude of the spectrum at one wavenumber, but the slope:

$$
E(k)\propto k^{-5/3}.
$$

Under the homogeneous, isotropic, constant-flux assumptions, that slope is the
fingerprint of the admissible allocation selected by the constraints. Different
systems impose different admissible classes \(\mathfrak A\), conservation laws,
boundary conditions, and record channels; they should therefore produce
different spectra. The ACP claim is that these spectra are generated by the
same kind of variational problem:

$$
N^*(k)
\in
\arg\max_{N\in\mathfrak A}
\mathcal P[N],
$$

where \(\mathcal P[N]\) rewards scale-local flux information, nondegenerate
continuation, and future predictive information, while penalizing protected
interior capture, singularity, and unresolved record burden.

**Conjecture T-2 (spectral allocation fingerprint).** In any cascade-like
persistent system with scale-local records, the observed scaling exponent or
spectral profile is the fingerprint of the persistence-maximizing uncertainty
allocation under that domain's constraints. K41's \(-5/3\) exponent is the
homogeneous/isotropic constant-flux instance, not the universal exponent of
ACP itself.

## 8. Intermittency as Nonuniform Drift

The old catalog note proposed that intermittency reflects multi-scale
crystallization drift. The admissibility version sharpens this:

> Intermittency is the nonuniform concentration of cascade capacity into rare
> structures whose records carry more flux information than their volume
> fraction would predict.

A scale-local diagnostic is:

$$
J_\ell
=
I(\Pi_\ell;\mathcal C_\ell)
-
\sum_i I(\Pi_\ell;C_{\ell,i}),
$$

where \(C_{\ell,i}\) are individual coherent-structure features and
\(\mathcal C_\ell\) is their joint inventory.

Positive \(J_\ell\) means the joint structure inventory carries superadditive
information about energy flux. This is the turbulence analogue of the ACP
interaction-information excess.

**Prediction T-1 (intermittency-information link).** Scales and flow regions
with stronger anomalous intermittency should show larger positive
interaction-information excess \(J_\ell\) between coherent-structure features
and local energy flux.

## 9. Correction to the Existing Special-Case Mapping

The special-cases catalog originally treated "fully developed isotropic
turbulence" as the dissolution boundary. The catalog now carries the refined
reading:

> Fully developed turbulence is not automatically dissolution. It is
> dissolution only relative to a coarse-graining that cannot decode its
> coherent structures or scale-local flux. Relative to inertial-range records,
> it remains in the productive interval.

This matters because turbulence is famous precisely because it is chaotic but
not random. It is wild enough to defeat pointwise prediction, but structured
enough to support universal spectra, flux laws, coherent objects, and
engineering models.

That is exactly the distinction the reality-reflective-mathematics bridge was
meant to expose.

## 10. Relation to Navier-Stokes Regularity

The Navier-Stokes existence/smoothness problem can be read as an admissibility
question:

> Does the mathematical description preserve finite continuation for smooth,
> finite-energy initial data?

In ACP terms, a finite-time singularity would not be a physical fluid state. It
would mark the point at which the chosen continuum description exits its
admissible domain unless new variables, viscosity, molecular cutoff, weak
solution criteria, or dissipation conditions restore finite records.

This bridge does not solve regularity. It says why regularity matters for
reality-reflective mathematics: a model whose observables or continuation law
fail cannot remain world-facing without an admissible completion.

## 11. Testable Program

A minimal computational test does not require solving the full problem.

1. Choose a DNS dataset or shell-model cascade with resolved energy transfer.
2. Define scale macrostates \(m_\ell\) from filtered velocities and structure
   inventories.
3. Estimate:

$$
H_\ell
=
H(m_\ell(t+\tau_\ell)|m_\ell(t)),
$$

$$
I_\ell
=
I(m_\ell(t);m_\ell(t+\tau_\ell)),
$$

$$
S_\ell
=
I(\Pi_\ell;R_\ell),
$$

the structured innovation quantities

$$
N_\ell
=
H(R_{\ell,t+\tau_\ell}\mid Z_{\ell,t}),
\qquad
S_\ell^{\mathrm{innov}}
=
I(\Pi_\ell;R_{\ell,t+\tau_\ell}\mid Z_{\ell,t}),
$$

and the interaction excess \(J_\ell\).

4. Estimate the uncertainty-allocation spectrum

$$
\ell\mapsto N_\ell
\qquad
\text{or}
\qquad
k\mapsto N(k),
$$

and its fitted slope or profile over the inertial range.

5. Define a provisional productive score:

$$
P_\ell
=
S_\ell
\cdot
\frac{H_\ell}{H_{\max}}
\cdot
\left(1-\frac{H_\ell}{H_{\max}}\right)
\cdot
\frac{I_\ell}{H(m_\ell(t+\tau_\ell))}.
$$

The ACP prediction is that \(P_\ell\) peaks in the inertial range, falls near
the forcing/laminarized scale, and falls again near the dissipation/unresolved
scale.

6. Compare closures by whether they preserve the \(P_\ell\) profile while
reducing prediction error at fixed computational budget.
7. Vary the closure's stochastic or dissipative allocation across scales and
   check whether the maximizing spectrum \(N^*(k)\) shifts with distance from
   the laminar and unresolved boundaries.

## 12. What This Shows

Turbulence is a better test of the new meta-criterion than of the older simple
three-region slogan.

The lesson is:

> Reality-reflective mathematics need not predict every microstate. It must
> preserve the finite record channels, invariants, and productive intervals
> through which the system remains intelligible.

For turbulence, the reality-reflective object is not "the exact velocity field
forever." It is the finite, scale-local structure that survives between
laminar overconstraint and unresolved decorrelation: energy flux, spectra,
structure functions, coherent structures, and intermittency.

That is why turbulence feels like the ACP written in fluid.
