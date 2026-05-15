# Unitary Evolution from ACP Mechanism-Preserving Dynamics

*Status: exploratory bridge note; the main theorem is **proved** conditional on
Hilbert-space ray kinematics and the Born-weight structure established in
`bridges/born_rule_from_acp.md`. A first-principles derivation of Hilbert
space, ray geometry, and the relevant symmetry axioms from ACP alone remains
open.*

## 1. Thesis

The Born-weight note solved one part of the quantum-foundations problem:

> once a premeasurement state is decomposed into orthogonal Hilbert branches,
> ACP-style invariance and coarse-graining force branch weights
> \(W(v)=\|v\|^2\).

The next question is what happens *between* measurements. Why should the
prediction structure evolve unitarily rather than by some other reversible map?

This note gives the clean conditional answer:

> if a closed ACP system evolves between measurements by reversible,
> mechanism-preserving transformations that preserve the Born transition
> structure on rays, then the evolution is unitary (more precisely:
> unitary-or-antiunitary by Wigner, and continuous time excludes the
> antiunitary branch).

So the ACP does not yet derive Hilbert space from scratch, but once Hilbert
branch geometry is in place, unitary evolution is the unique continuous
mechanism-preserving flow.

## 2. Setup

Let \(\mathcal H\) be a complex Hilbert space, finite-dimensional for
simplicity. Let

$$
\mathbb P(\mathcal H)
$$

denote its ray space: nonzero vectors modulo phase.

For rays \(r=[\psi]\) and \(s=[\phi]\), define the transition probability

$$
T(r,s)
:=
\frac{|\langle \psi,\phi\rangle|^2}{\|\psi\|^2\|\phi\|^2} .
$$

By `bridges/born_rule_from_acp.md`, this is exactly the Born overlap weight.

We study a one-parameter family of ray transformations

$$
F_t:\mathbb P(\mathcal H)\to\mathbb P(\mathcal H),
\qquad t\in\mathbb R ,
$$

interpreted as closed evolution between measurements.

## 3. ACP-Motivated Evolution Axioms

### Axiom UE-1 (Mechanism-preserving reversibility)

Between measurements, the evolution is reversible and composes in time:

$$
F_0 = \mathrm{id},
\qquad
F_{t+s}=F_t\circ F_s,
$$

and each \(F_t\) is bijective.

Interpretation: no branch is created or destroyed during the interval; the
prediction structure is rearranged rather than collapsed.

### Axiom UE-2 (Transition-structure preservation)

For all rays \(r,s\in\mathbb P(\mathcal H)\),

$$
T(F_t r, F_t s)=T(r,s) .
$$

Interpretation: a mechanism-preserving transformation cannot alter the branch
overlap geometry that fixes Born weights and interference relations.

### Axiom UE-3 (Temporal continuity)

For every ray \(r\), the map \(t\mapsto F_t r\) is continuous.

Interpretation: between measurements, closed evolution is a continuous flow,
not a sequence of discrete symmetry jumps.

## 4. Main Theorem

### Theorem 4.1 (Wigner reduction)

Under Axiom UE-2, each \(F_t\) admits a lift

$$
U_t:\mathcal H\to\mathcal H
$$

that is either unitary or antiunitary and satisfies

$$
F_t([\psi])=[U_t\psi]
$$

for every nonzero \(\psi\in\mathcal H\).

*Proof.* This is Wigner's theorem: any bijection on ray space preserving
transition probabilities is implemented by a unitary or antiunitary operator.
\(\square\)

### Theorem 4.2 (Continuous mechanism-preserving evolution is unitary)

Under Axioms UE-1 through UE-3, the family \(\{F_t\}_{t\in\mathbb R}\) can be
lifted to a one-parameter family of **unitary** operators
\(\{U_t\}_{t\in\mathbb R}\) satisfying

$$
U_{t+s}=U_tU_s,
\qquad
U_0=I .
$$

Thus between measurements, a closed ACP evolution is unitary.

*Proof.* By Theorem 4.1, each \(F_t\) is implemented by either a unitary or an
antiunitary operator.

At \(t=0\), \(F_0=\mathrm{id}\), so the lift is the identity, which is unitary.
By continuity (UE-3), \(F_t\) for sufficiently small \(t\) must lie in the
same connected component of the symmetry group as the identity. Antiunitary
transformations lie in the disconnected component: they cannot be reached
continuously from the identity while preserving the ray-transition structure.
Hence \(F_t\) is implemented by a unitary operator for all sufficiently small
\(t\).

Now use the group law \(F_{t+s}=F_t\circ F_s\). Any finite \(t\) can be written
as a sum of sufficiently small increments. A composition of unitary lifts is
unitary, so the lift for every \(t\) is unitary. Choosing phases consistently
gives a unitary one-parameter group \(\{U_t\}\) with

$$
F_t([\psi])=[U_t\psi] .
$$

\(\square\)

### Corollary 4.3 (Hamiltonian generator)

In finite dimensions, there exists a self-adjoint operator \(H\) such that

$$
U_t = e^{-itH} .
$$

Equivalently, for state vectors,

$$
i\frac{d}{dt}|\psi(t)\rangle = H |\psi(t)\rangle .
$$

If physical units are restored, one writes

$$
i\hbar\frac{d}{dt}|\psi(t)\rangle = \hat H |\psi(t)\rangle .
$$

*Proof.* A continuous one-parameter unitary group on a finite-dimensional
Hilbert space has a self-adjoint generator. This is the finite-dimensional case
of Stone's theorem. \(\square\)

## 5. ACP Reading

### 5.1 Mechanism-preserving intervals

In `bridges/restraint_power.md`, mechanism-preserving transformations conserve
the total coordination capacity. The quantum translation is:

- no measurement occurs;
- no branch sector is eliminated;
- no decohering environment is traced out;
- the total branch-accounting geometry is preserved.

That is exactly the regime modeled by UE-1.

### 5.2 Why transition-probability preservation is the right invariant

The Born-weight note showed that branch weights are fixed by the squared norm.
Once that is in place, the natural closed-system invariant is not merely the
norm of one state but the whole transition-probability structure

$$
T(r,s)=|\langle r,s\rangle|^2 .
$$

Preserving \(T\) means preserving:

- branch distinguishability;
- interference capacity;
- relative betting power between candidate future channels.

If a closed evolution changed \(T\), it would not merely move the prediction
structure around. It would alter the branch-accounting law itself, which is not
mechanism-preserving.

### 5.3 Why antiunitary is excluded

Antiunitary maps are valid isolated symmetries, but not continuous time flows.
They can represent discrete symmetries such as time reversal. They cannot serve
as the generic between-measurement evolution because closed time evolution must
connect continuously to the identity. The ACP reading is simple:

- unitary flow = ordinary mechanism-preserving continuation;
- antiunitary symmetry = exceptional discrete re-labeling, not the ambient
  temporal dynamics.

## 6. Relation to Existing ACP Quantum Material

This note is the direct sequel to `bridges/born_rule_from_acp.md`.

The two notes now give a clean pair:

1. **Branch weights:** on a Hilbert branch decomposition, ACP-style
   coarse-graining forces \(W(v)=\|v\|^2\).
2. **Closed evolution:** on that same branch geometry, ACP-style
   mechanism-preserving flow forces continuous time evolution to be unitary.

The connection to prior notes is:

- `reductions/zurek.md`: decoherence and measurement are the non-unitary,
  entropy-producing boundary events that interrupt the unitary intervals.
- `bridges/restraint_power.md`: mechanism-preserving transformations are the ACP
  analog of closed reversible evolution.

## 7. What This Does Not Yet Do

This note does **not** derive unitary evolution from ACP alone in a fully
foundational sense. It still imports:

- complex Hilbert-space ray kinematics;
- transition probabilities as the relevant closed-system invariant;
- continuity in time.

So the actual theorem is:

> given Hilbert ray geometry and the Born overlap law, ACP-style
> mechanism-preserving evolution is unitary.

The remaining deeper problem is to derive the ray geometry and transition
structure themselves from ACP persistence requirements.

## 8. Open Direction

The clean next step is to remove the strongest imported assumption in UE-2.
Instead of postulating preservation of Hilbert transition probabilities, one
would like to prove:

1. the conserved quantity on closed intervals is total branch capacity;
2. branch capacity induces an inner-product geometry on prediction states;
3. the automorphism group of that geometry is unitary;
4. continuous mechanism-preserving flow therefore yields the Schrödinger form.

That would move the program from

> ACP-compatible quantum kinematics

to

> ACP-derived quantum kinematics.
