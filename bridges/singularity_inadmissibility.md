# Singularity Inadmissibility: A Quantum-Gravity Boundary Criterion

*Status: active component of the ACP quantum-gravity derivation program; formal
at the ACP/Schur level; conjectural as a complete gravitational and
quantum-gravity derivation.*

Companion program notes: `bridges/quantum_gravity_derivation_program.md` and
`bridges/cosmic_coordination_floor.md`.

## 1. Thesis

Singularities are inadmissible physical states. This is the first hard rung in
the ACP derivation of quantum gravity.

If a singularity appears in a theory, the correct ACP reading is not "nature
contains an infinite-density object" or "spacetime includes an actual point of
infinite curvature." The correct reading is:

> the description has been pushed outside its admissible state space.

In ACP terms, a singularity is a boundary failure. It is the crystallization
boundary expressed in geometric variables: at least one required interior
direction has collapsed, the effective boundary law is no longer well-defined,
and the theory has lost degrees of freedom needed to continue predicting its
own future.

This note makes Andrew's constraint precise:

> singularities are inadmissible. If they show up, there is a failure in the
> math.

The word "failure" is not pejorative. It is diagnostic. Singularities mark where
an effective description has run out of legal coordinates, channels, or
resolution scale.

## 2. Admissible Description

Let a physical description \(\mathcal T\) specify:

1. a state space \(\mathcal S\);
2. an evolution or constraint law \(\Phi_t\);
3. a boundary record channel \(P(R|s)\);
4. a coarse-graining map from microscopic variables to observable macrostates.

Call \(\mathcal T\) admissible on a domain \(U\subseteq\mathcal S\) when the
following hold.

**Finite observables.** The quantities that define the description's empirical
content are finite at the resolution scale of the theory:

$$
|\mathcal O_i(s)| < \infty
\qquad
\text{for all required observables } \mathcal O_i .
$$

**Normalizable boundary channel.** The record channel is a genuine probability
law:

$$
0\leq P(R|s)\leq 1,
\qquad
\sum_R P(R|s)=1
$$

or the corresponding normalized measure in the continuum case.

**Nondegenerate interior.** Under the boundary/interior partition, the internal
block \(D\) is nondegenerate:

$$
0 < \mathrm{rank}(D),
\qquad
\kappa(D)<\infty .
$$

Equivalently, the conditional macrostate entropy remains in the ACP productive
interval:

$$
0 < H(m'|m) < H_{\max}.
$$

**Finite continuation.** The law \(\Phi_t\) carries admissible states to
admissible states over the verification timescale:

$$
s\in U
\Rightarrow
\Phi_t(s)\in U
\qquad
0\leq t\leq \tau_v .
$$

An inadmissible state is not a strange but valid physical object. It is a point
where at least one of these requirements fails.

## 3. ACP/Schur Proposition

**Proposition 1 (Schur singularities are inadmissible).** In the ACP/Schur
formalism, a state with singular internal block \(D\) is not an admissible
persistent state.

**Proof.** The effective boundary law is computed by the Schur complement

$$
Q/D=A-BD^{-1}B^T .
$$

If \(D\) is singular, \(D^{-1}\) does not exist. One may replace it by a
pseudoinverse only after imposing an additional support condition; that
additional condition is new structure, not part of the original effective
description. Without it, the boundary theory is undefined.

In ACP variables, singular \(D\) means at least one conditional direction has
reached the crystallization boundary:

$$
\lambda_{\min}(D)\to 0
\quad\Longleftrightarrow\quad
h_i(D)\to 0
\ \text{for at least one internal direction}.
$$

Total crystallization is the limiting case

$$
\mathrm{rank}(D)\to 0
\quad\Longleftrightarrow\quad
H(m'|m)\to 0,
$$

where the system has become all boundary and no interior. Partial singularity
is already inadmissible for the original description because the boundary law
requires \(D^{-1}\) in every retained internal direction. Since future-bearing
dynamics require a nondegenerate interior block, the singular state is outside
the admissible productive interval for that description. \(\square\)

This is already a formal result inside the ACP framework. The gravitational
claim below is a conjectural lift of the same criterion.

## 4. Geometric Translation

In general relativity, familiar singularity diagnostics include:

- curvature scalars diverging, e.g. \(R_{abcd}R^{abcd}\to\infty\);
- geodesic incompleteness;
- stress-energy quantities exceeding the domain where the effective matter
  model is meaningful;
- boundary-value problems becoming nonunique or nonnormalizable.

The ACP translation is:

| Geometric failure | ACP/Schur reading |
|---|---|
| Curvature invariant diverges | finite-observable condition fails |
| Geodesic incompleteness | finite-continuation condition fails |
| Infinite density / pressure | coarse-grained state variable leaves domain |
| Naked singularity | boundary channel exposes undefined interior |
| Schur \(D\) singular | boundary/interior decomposition fails |
| Horizon formation | boundary transfer may restore admissibility |

A singularity is therefore not a member of the physical state space. It is the
signal that the chosen state space was too small or the chosen variables were
not legal at that scale.

## 5. Horizon Versus Naked Singularity

The distinction between a horizon and a naked singularity becomes clean in this
language.

A naked singularity is inadmissible because the exterior record channel couples
directly to a region where the effective description is undefined:

$$
P(R_{\mathrm{ext}}|g,\phi)
\quad\text{depends on inadmissible interior data.}
$$

The problem is not merely high curvature. The problem is that the outside
theory is asked to assign probabilities conditioned on variables that the
inside theory cannot define.

A horizon can be admissible if it performs a boundary transfer. The exterior no
longer requires direct access to the interior microstate. Instead, it receives a
finite set of boundary observables:

$$
R_{\mathrm{ext}}
\sim
(M,J,Q,A_{\mathrm{hor}},\ldots),
$$

and the remaining interior details are hidden behind a structured dark
constraint. In the language of `bridges/dark_constraint_quantum_gravity.md`:

$$
I(\mathrm{charges,area};R_{\mathrm{ext}})>0,
$$

while

$$
I(\mathrm{interior\ microstate};R_{\mathrm{ext}})\approx 0
$$

until the appropriate decoding scale.

Thus the horizon is not the singularity. The horizon is the candidate repair:
it converts an inadmissible direct coupling into an admissible finite boundary
channel.

## 6. Principle of Singularity Exclusion

**Principle 1 (Singularity exclusion).** A candidate physical theory must not
treat singularities as physical states. It must either:

1. resolve them by extending the state space;
2. exclude them by a boundary condition or censorship principle;
3. replace them with a finite boundary transfer; or
4. identify them as artifacts of an invalid coarse-graining.

In path-integral language, the admissible history class should be written as

$$
\mathcal C_{\mathrm{adm}}(R)
=
\{(g,\phi): (g,\phi)\ \text{satisfies the admissibility conditions and
matches } R\}.
$$

Then

$$
Z[R]
=
\int_{\mathcal C_{\mathrm{adm}}(R)}
\mathcal Dg\,\mathcal D\phi\,
\exp(iS[g,\phi]/\hbar).
$$

Singular configurations are not summed as ordinary histories. If they appear,
they must be resolved by new variables, cancelled by destructive interference,
excluded by admissibility, or converted into boundary data.

This is the quantum-gravity analog of the QEC rule:

> do not let the environment measure the logical state directly; expose only
> syndrome-compatible boundary information.

Here:

> do not let the exterior couple to undefined interior geometry; expose only
> admissible boundary information.

## 7. Conjectures

**Conjecture 1 (Naked singularities are inadmissible boundary channels).** A
classical spacetime containing a naked singularity is not a complete physical
state because the exterior record channel depends on undefined interior data.
Cosmic censorship is therefore not merely a dynamical regularity; it is an
admissibility condition for exterior prediction.

**Conjecture 2 (Horizon formation is boundary regularization).** In generic
collapse, horizon formation is the gravitational instance of restraint-power:
the collapsing high-concentration interior transfers finite coordination
capacity to horizon degrees of freedom before the exterior channel becomes
inadmissible.

**Conjecture 3 (Quantum gravity is singularity-excluding completion).** A
quantum theory of gravity is admissible only if its physical Hilbert space,
history class, or boundary algebra excludes singular configurations as
ordinary states. What replaces them may be a bounce, a horizon boundary algebra,
a topology change, a fuzzball-like microstate family, or some other finite
structure. The ACP requirement is not one preferred mechanism; it is the
exclusion of the singular endpoint as physical.

**Conjecture 4 (Darkness as admissible privacy).** Structured darkness is the
allowed substitute for singular exposure. The exterior may be constrained by
what it cannot see, provided the null record is finite, structured, and
predictive. This is exactly the role played by dark fringes in the toy optical
models and by horizon records in the gravitational conjecture.

## 8. What This Does Not Claim

This note does not prove cosmic censorship, derive Einstein's equations,
quantize the metric, or identify the correct microscopic resolution of black
hole interiors.

It states a selection criterion for acceptable mathematics:

> singular endpoints are not physical states; they are instructions to change
> the description.

That criterion is already forced inside the ACP/Schur formalism. Its extension
to gravity remains conjectural, but it is structurally aligned with the
restraint-power reading of horizons and the dark-constraint reading of null
records.

## 9. Next Formal Target

**The first hard rung is now proven.**
`bridges/semiclassical_collapse_failure.md` derives, rather than assumes, that
classical collapse leaves the admissible state space: under the strong energy
condition, an irrotational congruence, and initial focusing
\(\theta(0)\leq-\alpha<0\), a caustic forms by \(\tau_\times\leq3/\alpha\) and
the relational frame ceases to define the macrocell label.

That note also sharpens the reading of this document in one respect worth
recording. The theorem is stated in terms of geodesic incompleteness and
reference-frame breakdown, not curvature divergence — because that is what the
singularity theorems actually deliver. Section 2's *finite continuation*
condition is therefore the admissibility criterion that gravity genuinely
violates, and the *finite observables* condition (curvature blow-up) is the
weaker and less securely established one. The framework's admissibility ladder
happens to be better matched to provable GR than a curvature-based criterion
would be.

The broader formalization program is laid out in
`bridges/cosmic_coordination_floor.md`. The first executable toy model exists
in `simulations/cosmic_coordination_floor/` and implements three competing
descriptions:

1. **naked collapse:** the boundary channel is forced to score records against
   an undefined interior variable;
2. **hard exclusion:** histories reaching the singular set are removed from the
   admissible class;
3. **horizon transfer:** the interior variable is replaced by a finite boundary
   register carrying mass/area-like charges.

The measurable target is:

$$
P(R_{\mathrm{ext}}|\mathrm{naked})
\ \text{fails normalization or stability,}
$$

while

$$
P(R_{\mathrm{ext}}|\mathrm{horizon})
$$

remains finite and informative about charges but approximately blind to the
interior microstate.
