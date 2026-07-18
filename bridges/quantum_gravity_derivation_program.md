# Quantum Gravity Derivation Program

*Status: active derivation roadmap; proven at the ACP/Schur admissibility level,
partial at the relational-kernel level, conjectural as a complete microscopic
derivation of quantum gravity.*

## 1. Thesis

The goal is to derive quantum gravity from ACP.

More precisely:

> Quantum gravity is the persistence-forced completion of classical spacetime.
> When classical gravitational dynamics would drive a relational macrostate
> channel into singular inadmissibility, the admissible completion must replace
> that endpoint with a finite, boundary-decodable quantum channel that preserves
> nonzero future entropy while protecting interior logical information until
> the appropriate decoding scale.

This is stronger than treating ACP as an external audit of quantum-gravity
proposals. The selection-rule language remains useful, but it is now a rung in
the derivation program: if the ACP admissibility constraints are strong enough,
they should force the core structural features usually associated with quantum
gravity.

## 2. Honesty Boundary

The program should state its ambition directly while preserving the status of
each claim.

**Proven inside ACP/Schur.** Singular internal blocks are inadmissible for
persistent effective boundary laws. If the internal block \(D\) required by a
Schur complement becomes singular, the effective boundary law is undefined
unless new structure is supplied.

**Structurally derived from ACP.** A system approaching a coordination floor
must undergo a mechanism-changing, decodable redistribution before its
future-bearing channel crystallizes.

**Conjectural in quantum gravity.** The microscopic mechanism implementing
that redistribution for spacetime is quantum gravity.

**Open.** The relational observable macrostate kernel has not yet been
constructed inside a full candidate quantum-gravity theory. A first finite
relational kernel skeleton now exists in
`bridges/relational_observable_macrostate_kernel.md`, but ACP has not yet
derived the exact microscopic Hilbert/algebraic dynamics of gravity.

## 3. The Derivation Ladder

### Stage 1: Admissible Descriptions

A physical description is admissible only when it supplies finite observables,
a normalizable record channel, a nondegenerate interior/boundary partition, and
finite continuation over a verification interval.

This stage is shared with `bridges/singularity_inadmissibility.md` and
`bridges/reality_reflective_mathematics.md`.

### Stage 2: Classical GR Failure

Classical gravitational collapse is a self-reinforcing concentration mechanism.
Under the focusing assumptions captured by the Raychaudhuri equation, collapse
narrows the set of admissible future macrostates and pushes the effective
description toward geodesic incompleteness, divergent observables, or an
undefined future channel.

The target theorem is:

> For a finite-resolution relational collapse macrostate satisfying the
> classical focusing assumptions, the classical transition kernel either
> becomes undefined on admissible future macrostates or violates the positive
> future-entropy floor.

### Stage 3: Required Completion

ACP requires that the gravitational channel avoid both endpoints:

$$
0 < H_{\ell,\Delta}(m) < H_{\max}
$$

and, for active collapse,

$$
H_{\ell,\Delta}(m)
\geq
H_{\mathrm{floor}}(m;\ell,\partial R)
>
0 .
$$

Therefore the physical completion of classical gravity must introduce a
mechanism-changing transformation before singular crystallization.

### Stage 4: Relational Observables

Because gravitational field variables are gauge-dependent, the admissible
states cannot be coordinate snapshots. They must be finite-resolution
relational macrocells:

$$
m\in\mathcal M_\ell .
$$

The central object is a relational transition kernel:

$$
P_{\ell,\Delta}(m'|m).
$$

`bridges/relational_observable_macrostate_kernel.md` now gives the first
OP-20 construction: finite relational observables, macrocells, quantum/channel
and classical-pushforward kernel forms, and diagnostics for future entropy,
geometry-record information, protected interior leakage, and late boundary
decodability. The first executable macrocell toy now lives in
`simulations/cosmic_coordination_floor/`; the next step is to strengthen the
semiclassical collapse failure theorem and then instantiate candidate
quantum-gravity mechanisms.

### Stage 5: Boundary Decodability

The repair cannot merely hide collapse. The exterior or boundary record must
receive decodable coordination:

$$
I(X_R;Y_{\partial}^{[t,t+T_{\mathrm{dec}}]})
\geq
\eta\,\Delta C_R-\varepsilon .
$$

A remnant, baby universe, bounce, wormhole, horizon microstructure, or island
mechanism is ACP-admissible only if it supplies a finite recoverable boundary
channel for the relevant redistributed coordination.

### Stage 6: Protected Interior Information

The boundary record must constrain geometry without prematurely leaking the
protected interior microstate:

$$
I(\mathrm{geometry\ sector};R_{\partial})>0
$$

while

$$
I(\mathrm{interior\ microstate};R_{\partial}^{\mathrm{early}})\approx 0 .
$$

This is the gravitational lift of the QEC condition:

$$
I(\mathrm{error};\mathrm{syndrome})>0
$$

while

$$
I(\mathrm{logical\ state};\mathrm{environment})\approx 0 .
$$

### Stage 7: Holographic/QEC Structure

If exterior-accessible records must constrain geometry sectors while protecting
interior logical states, then the admissible gravitational channel is
code-like. Bulk/interior information is not simply exposed; it is encoded into
boundary records with constrained recoverability.

This does not assume AdS/CFT as the whole answer. It treats holographic QEC as
evidence for the structure ACP expects any viable quantum gravity to contain.

### Stage 8: Classical Limit

The final derivation must recover classical spacetime as the coarse effective
law of the relational channel in the regime where:

- future entropy remains comfortably above the floor;
- boundary records are sufficiently stable;
- interior logical leakage is bounded;
- quantum redistribution mechanisms are inactive or coarse-grain into ordinary
  semiclassical stress-energy corrections.

The expected result is not "quantize the metric" as a starting axiom, but:

> Einstein-like geometry is the large-scale effective law of an admissible
> relational record channel.

## 4. Current Anchors

- `proofs/semiclassical_collapse_failure.md`: the Stage 2/3 theorem at kernel
  level. Under an explicit Raychaudhuri-shadow drift assumption, classical
  collapse kernels lose all admissible mass in finite expected time
  (Theorem 1), postselected survivor theories are exponentially unnatural
  and record-free, and any normalized floor-respecting kernel family must
  change mechanism strictly before the singular threshold, at compactness
  \(C_{\mathrm{trig}}\le1-\delta\) (Theorem 2). The remaining physics gap
  is OP-19a, the drift transfer lemma.
- `bridges/singularity_inadmissibility.md`: singularities are inadmissible
  physical states; horizons are candidate finite boundary transfers.
- `bridges/relational_observable_macrostate_kernel.md`: finite relational
  observables to macrocells, transition kernels, Schur-block diagnostics, and
  the first classical-collapse failure proposition.
- `bridges/cosmic_coordination_floor.md`: future-entropy floor, collapse
  trigger, and visible redistribution criteria.
- `bridges/dark_constraint_quantum_gravity.md`: null records as
  syndrome-like constraints on candidate geometry/path histories.
- `bridges/quantum_gravity_convergence_map.md`: contact with holographic QEC,
  islands/Page curves, relational observable algebras, crossed products, and
  regular-black-hole work.
- `bridges/quantum_noise_as_signal.md`: finite QEC prototype for structured
  records that reveal error sectors while preserving logical states.
- `bridges/boundary_records_interior_time.md`: interior clock censorship.
  Lifting the proved clock-syndrome record-splitting propositions
  (`bridges/clock_syndrome_record_splitting.md`), Stage 6 privacy forces
  early boundary records to be blind to every interior relational clock,
  and the transition where the boundary can first read interior time
  coincides with the decoding transition of Stage 5. The admissible
  gravitational record channel is therefore split — geometry-central
  versus interior-transparent — as a theorem-backed substructure of
  Stage 6 rather than a modeling choice.

## 5. Near-Term Work

1. Strengthen the classical failure theorem for the finite semiclassical
   collapse macrocell using compactness, expansion, curvature, boundary area,
   null records, and outgoing radiation bins.
2. Instantiate candidate completion kernels for that macrocell and compare them
   against the floor, privacy, and decodability diagnostics.
3. Upgrade the dark-constraint simulations from hidden optical phase bumps to
   weak metric/lensing perturbations.
4. Connect the boundary-record privacy condition to decoupling/QEC
   recoverability bounds.
5. Audit candidate mechanisms against the full derivation ladder: holographic
   QEC, islands, loop/effective bounces, asymptotic-safety black holes,
   remnants, baby universes, and regular black-hole metrics.

## 6. Working Conjecture

**Conjecture (ACP derivation of quantum gravity).** The conjunction of ACP
admissibility, singularity exclusion, relational observability, positive
future-entropy floor, boundary decodability, and protected interior information
forces a holographic/QEC-like quantum gravitational channel whose classical
limit is ordinary spacetime dynamics away from the coordination floor.

The conjecture is not yet proven. It is now the organizing target of ACP
Quantum.
