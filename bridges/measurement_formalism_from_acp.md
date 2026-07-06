# Measurement Formalism from ACP Coarse-Graining and Decodability

*Status: exploratory bridge note; the main results are **proved** conditional
on local Hilbert-space kinematics and the Born-weight structure already
established in `bridges/born_rule_from_acp.md`. A first-principles derivation
of Hilbert space from ACP alone remains open.*

## 1. Thesis

With the previous three bridge notes, the conditional local kinematics package
already contains:

1. `bridges/born_rule_from_acp.md`: branch weights \(W(v)=\|v\|^2\);
2. `bridges/unitary_evolution_from_acp.md`: continuous closed evolution is
   unitary;
3. `bridges/tensor_product_from_acp.md`: independent composition is tensor
   product up to unitary equivalence.

The remaining local ingredient is measurement structure itself.

This note gives the conditional answer:

> if a measurement is a branch-resolving coarse-graining that assigns
> nonnegative additive outcome weights to positive branch operators, then the
> outcome statistics are represented by a POVM.

And in the ideal sharp repeatable case:

> if each resolved outcome sector is exclusive, certain on its own sector, and
> complete, then the POVM reduces to an orthogonal projective measurement.

So POVMs and projectors are not extra decorations. They are the unique operator
form of ACP-compatible branch resolution once local Hilbert kinematics is in
view.

## 2. Setup

Let \(\mathcal H\) be a finite-dimensional complex Hilbert space. A
subnormalized branch state is a positive operator

$$
\sigma \ge 0
$$

with trace

$$
\mathrm{Tr}(\sigma)\le 1 .
$$

Interpretation: \(\sigma\) is a branch-weight-bearing positive state fragment;
its trace is its total unresolved branch budget.

A measurement with outcomes \(i=1,\dots,n\) assigns outcome weights

$$
m_i(\sigma)\in[0,\infty)
$$

to each positive branch operator \(\sigma\).

## 3. ACP-Motivated Measurement Axioms

### Axiom MF-1 (Positivity)

For every positive branch operator \(\sigma\),

$$
m_i(\sigma)\ge 0 .
$$

Interpretation: an outcome weight cannot be negative.

### Axiom MF-2 (Linearity on the positive cone)

For positive branch operators \(\sigma,\tau\),

$$
m_i(\sigma+\tau)=m_i(\sigma)+m_i(\tau) .
$$

For every scalar \(c\ge 0\),

$$
m_i(c\sigma)=c\,m_i(\sigma) .
$$

Interpretation: unresolved branch budgets coarse-grain additively.

### Axiom MF-3 (Normalization / budget conservation)

For every positive branch operator \(\sigma\),

$$
\sum_{i=1}^n m_i(\sigma)=\mathrm{Tr}(\sigma) .
$$

Interpretation: a measurement redistributes branch budget across outcomes; it
does not create or destroy total weight.

These three axioms are the operator-level translation of the same logic used in
the Born-weight note: positivity, additivity across exclusive branches, and
global normalization.

## 4. Main Theorem: POVM Form

### Theorem 4.1 (POVM realization)

Under Axioms MF-1 through MF-3, there exists a unique family of positive
operators \(\{E_i\}_{i=1}^n\) such that

$$
m_i(\sigma)=\mathrm{Tr}(E_i \sigma)
$$

for every positive branch operator \(\sigma\), with

$$
E_i\ge 0,
\qquad
\sum_{i=1}^n E_i = I .
$$

Therefore \(\{E_i\}\) is a POVM.

*Proof.* By MF-2, each \(m_i\) is linear on the positive cone. In finite
dimensions, linearity on the positive cone extends uniquely to a linear
functional on the real vector space of Hermitian operators. By the
Hilbert-Schmidt Riesz representation theorem, there exists a unique Hermitian
operator \(E_i\) such that

$$
m_i(\sigma)=\mathrm{Tr}(E_i \sigma)
$$

for all positive \(\sigma\).

Positivity MF-1 implies \(E_i\ge 0\): if \(|\psi\rangle\) is any vector and
\(\sigma=|\psi\rangle\langle\psi|\), then

$$
\langle\psi|E_i|\psi\rangle
=
\mathrm{Tr}(E_i |\psi\rangle\langle\psi|)
=
m_i(|\psi\rangle\langle\psi|)
\ge 0 .
$$

Normalization MF-3 gives

$$
\mathrm{Tr}\!\left(\left(\sum_i E_i\right)\sigma\right)
=
\sum_i m_i(\sigma)
=
\mathrm{Tr}(\sigma)
$$

for all positive \(\sigma\). Hence

$$
\sum_i E_i = I .
$$

So \(\{E_i\}\) is a POVM, and uniqueness follows from uniqueness in the Riesz
representation. \(\square\)

### Corollary 4.2 (Born probability form)

For a normalized state \(\rho\),

$$
p_i(\rho)=m_i(\rho)=\mathrm{Tr}(E_i\rho) .
$$

For a pure state \(\rho=|\psi\rangle\langle\psi|\),

$$
p_i(\psi)=\langle\psi|E_i|\psi\rangle .
$$

So the general ACP-compatible outcome law on local Hilbert states is exactly
the standard POVM probability rule.

## 5. Sharp Measurements as Projectors

We now add the extra structure corresponding to an ideal sharp resolved
measurement.

### Axiom MF-4 (Sharp outcome sectors)

For each outcome \(i\), there exists a subspace \(S_i\subseteq \mathcal H\)
with projector \(P_i\) such that:

1. **certainty on sector \(i\):**

   $$
   m_i(\sigma)=\mathrm{Tr}(\sigma)
   $$

   whenever \(\sigma\) is supported in \(S_i\);

2. **exclusivity across sectors:**

   $$
   m_j(\sigma)=0
   \qquad
   (j\neq i)
   $$

   whenever \(\sigma\) is supported in \(S_i\);

3. **completeness:**

   $$
   \mathcal H=\bigoplus_{i=1}^n S_i .
   $$

Interpretation: if a state is already fully resolved into outcome sector \(i\),
the measurement returns \(i\) with certainty, never confuses it with another
sector, and the sectors exhaust the sharp outcome space.

### Theorem 5.1 (Sharp POVMs are projective)

Under MF-1 through MF-4, the POVM effects are exactly the orthogonal
projectors:

$$
E_i=P_i .
$$

Thus the measurement is projective.

*Proof.* By certainty on sector \(i\), for every vector \(|\psi\rangle\in S_i\),

$$
\langle\psi|E_i|\psi\rangle
=
m_i(|\psi\rangle\langle\psi|)
=
\langle\psi|\psi\rangle .
$$

Since \(0\le E_i\le I\), this implies \(E_i\) acts as the identity on \(S_i\).

By exclusivity, for \(|\psi\rangle\in S_j\) with \(j\neq i\),

$$
\langle\psi|E_i|\psi\rangle
=
m_i(|\psi\rangle\langle\psi|)
=
0 .
$$

Positivity then implies \(E_i\) vanishes on \(S_j\) for \(j\neq i\).

Because the sectors are orthogonal and complete,

$$
\mathcal H=\bigoplus_j S_j ,
$$

the operator that is identity on \(S_i\) and zero on all other sectors is
precisely the orthogonal projector \(P_i\). Hence \(E_i=P_i\). \(\square\)

## 6. Canonical Sharp Update Rule

The effect operators determine only the outcome probabilities. To specify the
post-measurement state one needs an instrument.

For the sharp projective case, the ACP-minimal update is the Lüders rule.

### Axiom MF-5 (Minimal sharp disturbance)

Conditioned on outcome \(i\), the measurement:

1. preserves every state already supported in \(S_i\);
2. removes coherence between distinct sharp outcome sectors;
3. introduces no additional in-sector unitary kick.

### Proposition 6.1 (Lüders update)

Under MF-5, the selective sharp update is

$$
\mathcal I_i(\rho)=P_i\rho P_i .
$$

After normalization, the post-measurement state is

$$
\rho_i=\frac{P_i\rho P_i}{\mathrm{Tr}(P_i\rho)} .
$$

The nonselective update is

$$
\rho\mapsto \sum_i P_i\rho P_i .
$$

*Proof.* Decompose

$$
\rho=\sum_{k,\ell} P_k \rho P_\ell .
$$

By MF-5, outcome \(i\) must delete all off-sector terms and retain the
\(i\)-sector unchanged, with no extra in-sector rotation. Therefore only the
\(P_i\rho P_i\) block survives in the selective branch. \(\square\)

## 7. ACP Reading

### 7.1 POVMs as generalized boundary channels

A POVM is the most general way to resolve branch budget into a classical record
while preserving positivity and normalization. In ACP language, a POVM is a
finite decodable boundary channel.

### 7.2 Projectors as ideal sharp resolution

Projectors appear when the measurement is sharp enough that each outcome sector
is already a stable resolved subspace. Then the boundary channel does not
partially blur sectors; it simply identifies which sector the system occupied.

### 7.3 POVM versus projector

The distinction is structural:

- POVM: noisy, partial, coarse, or overcomplete boundary access;
- projector: ideal repeatable sharp access to mutually exclusive resolved
  sectors.

So the projective formalism is not the generic rule. It is the sharp limit of
the more general ACP-compatible POVM rule.

## 8. Relation to Existing ACP Quantum Material

This note completes the conditional local quantum-kinematics quartet:

1. `bridges/born_rule_from_acp.md`: branch weights;
2. `bridges/unitary_evolution_from_acp.md`: closed evolution;
3. `bridges/tensor_product_from_acp.md`: independent composition;
4. `bridges/measurement_formalism_from_acp.md`: boundary resolution.

The remaining deepest imported assumption is now the first one on the original
list:

- why the underlying prediction geometry is a complex Hilbert space at all.

## 9. What This Does Not Yet Do

This note does **not** derive Hilbert space or the operator-state formalism
from ACP alone. It still imports:

- local complex Hilbert branch spaces;
- positive branch operators as the right macrostate objects;
- additivity on the positive cone;
- the sharp-sector axioms in the projective case.

So the actual theorem is:

> given local Hilbert branch kinematics, ACP-style branch-resolution axioms
> force POVMs in general and orthogonal projectors in the ideal sharp case.

## 10. Open Direction

With this note in place, the remaining foundational frontier is cleaner.

The next serious step would be to attack the first item directly:

- derive the complex Hilbert prediction geometry from ACP persistence,
  coordination-floor, and branch-accounting requirements, rather than importing
  it.

That would turn the present quartet from

> ACP-selected quantum kinematics

into

> ACP-derived quantum kinematics.

*Update:* the first step is now taken in
`bridges/hilbert_geometry_from_acp.md`: branch homogeneity forces
inner-product geometry in finite dimension, with the remaining gaps named
G1–G4 there.
