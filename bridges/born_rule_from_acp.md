# Born Weights from ACP Branch Axioms

*Status: exploratory bridge note; the uniqueness theorem below is **proved**
conditional on standard Hilbert-space kinematics and an ACP-motivated
branch-weight axiom set. A first-principles derivation of Hilbert space,
unitary evolution, or projective measurement from ACP alone remains open.*

## 1. Thesis

The ACP does not, by itself, derive the full kinematic structure of quantum
theory. In particular, it does not yet derive:

- the use of a complex Hilbert space;
- unitary evolution between measurements;
- the tensor-product composition rule; or
- the projective/POVM measurement formalism.

But once those kinematics are granted, the ACP does constrain how branch
weights can be assigned during a measurement-like coherence crisis.

The claim of this note is:

> if a premeasurement state is decomposed into mutually exclusive orthogonal
> branch sectors, and branch weights are required to satisfy ACP-style
> conservation, exclusivity, and coarse-graining consistency, then the only
> admissible branch-weight functional is the squared Hilbert norm.

That is exactly the Born rule.

The ACP contribution is not the importation of \(|\alpha_i|^2\) by hand. It is
the claim that a persistent prediction structure must use the unique
branch-accounting rule that is:

- invariant under mechanism-preserving branch rotations;
- additive across mutually exclusive branches; and
- normalized on the full premeasurement state.

## 2. Setup

Let \(\mathcal H\) be a finite-dimensional Hilbert space and let
\(\{\Pi_i\}_{i=1}^n\) be a projective measurement:

$$
\Pi_i \Pi_j = \delta_{ij}\Pi_i,
\qquad
\sum_{i=1}^n \Pi_i = I .
$$

For a normalized premeasurement state \(|\psi\rangle \in \mathcal H\), define
the branch vectors

$$
v_i := \Pi_i |\psi\rangle .
$$

Then

$$
|\psi\rangle = \sum_{i=1}^n v_i,
\qquad
\langle v_i, v_j\rangle = 0 \ \text{for } i\neq j .
$$

We seek a branch-weight functional

$$
W:\mathcal H \to [0,\infty)
$$

such that the probability of outcome \(i\) is

$$
p_i = W(v_i) .
$$

The question is: which \(W\) is compatible with ACP-style branch accounting?

## 3. ACP-Motivated Branch Axioms

The following axioms are the branch-level translation of the ACP's
conservation/coarse-graining logic.

### Axiom BR-1 (Mechanism-preserving invariance)

If two branch vectors differ only by a mechanism-preserving rotation of the
branch geometry, then they carry the same weight. In Hilbert-space form, for
any unitary \(U\) on \(\mathcal H\),

$$
W(Uv) = W(v) .
$$

Interpretation: details internal to a branch that do not change its externally
decodable outcome record cannot change the branch's betting weight.

### Axiom BR-2 (Orthogonal additivity)

If \(v\perp w\), then

$$
W(v+w) = W(v) + W(w) .
$$

Interpretation: mutually exclusive branches are coarse-grained by summing their
weights. Otherwise the total branch capacity would depend on arbitrary
bookkeeping choices.

### Axiom BR-3 (Continuity and positivity)

The map \(W\) is continuous and nonnegative:

$$
W(v)\geq 0 .
$$

Interpretation: infinitesimal perturbations of the branch vector cannot create
finite jumps in betting weight.

### Axiom BR-4 (Normalization)

For every normalized state \(|\psi\rangle\),

$$
W(|\psi\rangle)=1 .
$$

Equivalently, for any projective resolution of the identity,

$$
\sum_i W(\Pi_i |\psi\rangle) = 1 .
$$

Interpretation: the full premeasurement state carries unit total branch weight.

## 4. Uniqueness Theorem

### Lemma 4.1 (Weight depends only on branch norm)

Under Axiom BR-1, there exists a function

$$
f:[0,\infty)\to[0,\infty)
$$

such that

$$
W(v)=f(\|v\|) .
$$

*Proof.* Any two vectors in \(\mathcal H\) with the same norm are related by a
unitary transformation. By BR-1 they therefore have the same weight. So the
weight depends only on the norm. \(\square\)

### Theorem 4.2 (Born-weight uniqueness)

Under Axioms BR-1 through BR-4,

$$
W(v)=\|v\|^2
$$

for every branch vector \(v\in\mathcal H\).

Hence for the measurement \(\{\Pi_i\}\),

$$
p_i = W(\Pi_i|\psi\rangle)
=
\|\Pi_i|\psi\rangle\|^2
=
\langle \psi|\Pi_i|\psi\rangle .
$$

For rank-1 projectors \(\Pi_i = |i\rangle\langle i|\), this reduces to

$$
p_i = |\langle i|\psi\rangle|^2 .
$$

*Proof.* By Lemma 4.1, \(W(v)=f(\|v\|)\) for some nonnegative continuous
function \(f\).

Now let \(v\perp w\), and set \(x=\|v\|\), \(y=\|w\|\). By orthogonality,

$$
\|v+w\| = \sqrt{x^2+y^2} .
$$

Applying BR-2 gives

$$
f(\sqrt{x^2+y^2}) = f(x) + f(y) .
$$

Define

$$
g(t) := f(\sqrt{t}), \qquad t\geq 0 .
$$

Then

$$
g(x+y) = g(x) + g(y)
$$

for all \(x,y\geq 0\) with \(x+y\leq 1\) on normalized states. Since \(g\) is
continuous and nonnegative, the Cauchy functional equation on this interval has
the unique solution

$$
g(t)=ct
$$

for some constant \(c\geq 0\). Therefore

$$
f(r)=cr^2 .
$$

Now use BR-4 on any normalized vector \(|\psi\rangle\), for which
\(\|\psi\|=1\):

$$
1 = W(\psi)=f(1)=c .
$$

Hence \(c=1\), so

$$
W(v)=\|v\|^2 .
$$

This yields

$$
p_i=W(\Pi_i|\psi\rangle)=\|\Pi_i|\psi\rangle\|^2
=\langle\psi|\Pi_i|\psi\rangle .
$$

\(\square\)

## 5. ACP Reading

Theorem 4.2 can be read as an ACP branch-accounting theorem.

### 5.1 Conservation

Before decoherence resolves the outcome, the premeasurement interaction is
mechanism-preserving in the quantum sense: the total prediction structure is
rearranged but not destroyed. BR-4 encodes the conserved total branch budget,
while BR-1 says that internal rearrangements within a branch do not change that
budget.

### 5.2 Exclusivity

Orthogonal branches are mutually exclusive future channels. BR-2 says that if
two such channels are coarse-grained into one larger outcome sector, their
weights add. This is the branch-level analog of summing conditional capacity
across disjoint sectors.

### 5.3 Why the square appears

The square is not inserted by hand. It is forced by the combination of:

- orthogonality in Hilbert space, which gives
  \(\|v+w\|^2=\|v\|^2+\|w\|^2\) for \(v\perp w\);
- additivity of mutually exclusive branch weights; and
- continuity plus normalization.

So the Born weight is the unique additive conserved capacity compatible with
orthogonal branch decomposition.

## 6. Immediate Corollaries

### Corollary 6.1 (Equal-amplitude symmetry)

If

$$
|\psi\rangle = \frac{1}{\sqrt{N}}\sum_{k=1}^N |k\rangle
$$

in an orthonormal basis, then each branch has weight

$$
W\!\left(\frac{1}{\sqrt{N}}|k\rangle\right)=\frac{1}{N} .
$$

This reproduces the equal-branch counting intuition without using it as a
primitive axiom.

### Corollary 6.2 (Independent composition)

For independent branch vectors \(v\in\mathcal H_1\) and \(w\in\mathcal H_2\),

$$
W(v\otimes w)
=
\|v\otimes w\|^2
=
\|v\|^2 \|w\|^2
=
W(v)W(w) .
$$

So the branch-weight rule is automatically multiplicative under independent
composition.

## 7. Relation to Existing ACP Quantum Material

This note sits downstream of two existing ACP quantum bridges:

- `bridges/restraint_power.md`, which shows that a strictly positive
  coordination floor appears at the quantum scale once a non-commutative
  partition is specified; and
- `reductions/zurek.md`, which shows that decoherence and pointer-state
  selection are productive-interval / drift phenomena.

The present note adds the missing branch-weight statement:

- A.20 identifies the existence of a quantum floor.
- Zurek reduction identifies measurement-like decoherence as the branch
  selection mechanism.
- The present theorem identifies the unique additive conserved branch weight on
  that Hilbert-space branch structure.

## 8. What This Does Not Yet Do

This is not yet a derivation of quantum theory from ACP alone.

What is imported rather than derived:

- Hilbert-space kinematics;
- orthogonal branch decomposition;
- unitary symmetry of premeasurement dynamics;
- projective measurement as the branch partition.

So the theorem should be read as:

> given standard quantum branch structure, ACP-style conservation and
> coarse-graining single out Born weights uniquely.

The deeper ambition remains open:

> derive the Hilbert-space branch structure itself from ACP persistence
> requirements, rather than taking it as background kinematics.

## 9. Open Direction

The natural next step is to upgrade Theorem 4.2 from a Hilbert-space uniqueness
result to a true first-principles derivation. The target would be:

1. start from ACP persistence, coarse-graining, and coordination-floor axioms;
2. derive the necessity of a norm-preserving prediction geometry;
3. show that the compatible geometry is Hilbertian rather than merely Banach;
4. recover unitary evolution as the mechanism-preserving flow; and
5. rederive Theorem 4.2 without importing BR-1 as a separate symmetry axiom.

That is the real "Born rule from ACP" problem.

*Update:* the first step is now taken in
`bridges/hilbert_geometry_from_acp.md`, which derives the inner-product
geometry (step 3) from an ACP branch-homogeneity axiom in finite dimension and
recovers Lemma 4.1 without importing BR-1.
