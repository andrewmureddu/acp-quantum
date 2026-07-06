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

The target theorem was:

> For a finite-resolution relational collapse macrostate satisfying the
> classical focusing assumptions, the classical transition kernel either
> becomes undefined on admissible future macrostates or violates the positive
> future-entropy floor.

This is now proven at the finite relational-kernel level:
`proofs/classical_collapse_failure_theorem.md` states the focusing assumptions
F1–F4 explicitly and proves the quantitative trichotomy — geometric
normalization failure, sub-floor crystallization of the postselected kernel,
or mechanism change — plus a record-starvation corollary showing the classical
boundary channel cannot satisfy the Stage 5 decodability requirement. The
residual Stage 2 work is deriving F1–F4 from explicit general-relativistic
collapse pushforwards instead of assuming them.

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
`simulations/cosmic_coordination_floor/`, and the collapse failure theorem is
proven in `proofs/classical_collapse_failure_theorem.md`; the next step is to
derive the focusing assumptions from explicit semiclassical pushforwards and
instantiate candidate quantum-gravity mechanisms.

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

- `bridges/singularity_inadmissibility.md`: singularities are inadmissible
  physical states; horizons are candidate finite boundary transfers.
- `proofs/classical_collapse_failure_theorem.md`: the Stage 2 theorem — under
  explicit focusing assumptions, classical collapse ends in normalization
  failure, sub-floor crystallization, or mechanism change, with explicit
  failure-time bounds and a record-starvation corollary.
- `bridges/relational_observable_macrostate_kernel.md`: finite relational
  observables to macrocells, transition kernels, Schur-block diagnostics, and
  the predecessor classical-collapse failure proposition.
- `bridges/cosmic_coordination_floor.md`: future-entropy floor, collapse
  trigger, and visible redistribution criteria.
- `bridges/dark_constraint_quantum_gravity.md`: null records as
  syndrome-like constraints on candidate geometry/path histories.
- `bridges/quantum_gravity_convergence_map.md`: contact with holographic QEC,
  islands/Page curves, relational observable algebras, crossed products, and
  regular-black-hole work.
- `bridges/quantum_noise_as_signal.md`: finite QEC prototype for structured
  records that reveal error sectors while preserving logical states.

## 5. Near-Term Work

1. Derive the focusing assumptions F1–F4 of
   `proofs/classical_collapse_failure_theorem.md` from explicit semiclassical
   collapse pushforwards (Oppenheimer–Snyder, Vaidya, or numerical interiors),
   turning the drift, defect, and concentration constants into computed
   quantities rather than hypotheses.
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
