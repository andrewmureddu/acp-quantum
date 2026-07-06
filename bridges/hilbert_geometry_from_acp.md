# Hilbert Branch Geometry from ACP Branch Homogeneity

*Status: exploratory bridge note; the main theorem is **proved** for
finite-dimensional real prediction spaces, and for complex prediction spaces
conditional on a complex structure with complex-linear symmetries. It removes
one imported assumption from the conditional quantum-kinematics quartet: the
*inner-product* (Hilbertian rather than merely normed) character of the branch
geometry now follows from an ACP homogeneity axiom plus finite records. The
linear-space structure itself, the complex field selection, and the full
operational grounding remain open; the residual gaps are named G1–G4 in §9.*

## 1. Thesis

The conditional quantum-kinematics quartet —

1. `bridges/born_rule_from_acp.md`: branch weights \(W(v)=\|v\|^2\);
2. `bridges/unitary_evolution_from_acp.md`: closed evolution is unitary;
3. `bridges/tensor_product_from_acp.md`: independent composition is tensor
   product;
4. `bridges/measurement_formalism_from_acp.md`: boundary resolution is
   POVM/projective —

imports complex Hilbert space in every note. OP-21 asks for the geometry
itself. This note takes the first provable step:

> if the prediction space is a finite-dimensional normed branch space
> (finite records), and the mechanism-preserving symmetries preserve pairwise
> distinguishability and act transitively on each capacity sphere (branch
> homogeneity), then the branch magnitude is induced by an inner product.
> Exclusivity is then not an extra primitive: weight-additive branch pairs are
> exactly the orthogonal pairs of the derived inner product.

In the ladder stated at the end of the Born-weight note —

1. norm-preserving prediction geometry,
2. Hilbertian rather than merely Banach,
3. unitary mechanism-preserving flow,
4. Born weights without importing BR-1 —

this note closes step 2 at the finite-dimensional level and derives the
precondition of step 4 (Lemma 4.1 of the Born note) rather than assuming it.

Two structural points make this more than a citation of classical geometry:

- **Finite records are load-bearing.** The corresponding infinite-dimensional
  question (the Banach–Mazur rotation problem) is open. ACP admissibility
  requires finite observables and finite record channels at fixed resolution
  (`bridges/reality_reflective_mathematics.md`), which is exactly the
  hypothesis under which the geometry theorem is decidable. The ACP does not
  merely tolerate the finite-dimensional restriction; it supplies it.
- **Exclusivity becomes derived, not primitive.** The Born note's orthogonal
  branch decomposition is recovered as the additivity relation of the derived
  inner product, and in the complex case full orthogonality is equivalent to
  *phase-robust* exclusivity (§5), which has a clean ACP reading.

## 2. Setup: Branch-Magnitude Spaces

Let \(V\) be a vector space over \(\mathbb F\in\{\mathbb R,\mathbb C\}\) with
\(1\le\dim V<\infty\). Elements of \(V\) are branch vectors: candidate
future-bearing prediction components of a premeasurement state.

A **branch magnitude** is a function \(\rho:V\to[0,\infty)\) that is a norm:

$$
\rho(v)=0 \iff v=0,
\qquad
\rho(\lambda v)=|\lambda|\,\rho(v),
\qquad
\rho(u+v)\le\rho(u)+\rho(v).
$$

The pair \((V,\rho)\) is a **branch-magnitude space**. The associated
**distinguishability metric** is

$$
d_\rho(u,v):=\rho(u-v).
$$

The **branch weight** is \(W:=\rho^2\), matching the Born note's convention
once the geometry is derived.

## 3. ACP-Motivated Geometry Axioms

### Axiom HG-1 (Normed prediction bookkeeping)

The prediction space is a branch-magnitude space \((V,\rho)\) over
\(\mathbb F\).

Interpretation: nondegeneracy says only the null branch carries zero capacity;
absolute homogeneity says magnitude bookkeeping is scale-consistent; the
triangle inequality says merging two branches cannot manufacture more
distinguishable capacity than the branches carried separately.

⚠ The linear structure of \(V\) — superposition as vector addition — is here
*imported*, not derived. This is gap G1 in §9 and is the deepest remaining
piece of OP-21.

### Axiom HG-2 (Finite records)

\(\dim V<\infty\).

Interpretation: at fixed resolution, an admissible system supports only
finitely many independent decodable prediction components. This is the
branch-space form of the finite-observable and normalizable-record-channel
admissibility conditions in `bridges/reality_reflective_mathematics.md`, and
of the coordination-floor requirement that macrostates be finitely
distinguishable at fixed \(\ell\).

### Axiom HG-3 (Branch homogeneity / mechanism-preserving transitivity)

For all \(u,v\in V\) with \(\rho(u)=\rho(v)=1\) there exists a bijection
\(F:V\to V\) such that

$$
F(0)=0,
\qquad
d_\rho(F(x),F(y))=d_\rho(x,y)\ \ \forall x,y\in V,
\qquad
F(u)=v .
$$

Interpretation: mechanism-preserving transformations preserve the pairwise
distinguishability structure of prediction states (the same invariant used in
Axiom UE-2 of the unitary note, stated metrically rather than in Born form),
and no two branches of equal capacity are structurally privileged: the
mechanism-preserving symmetry group is rich enough to relabel any
equal-capacity branch onto any other. This is the branch-space form of
coordination neutrality: the persistence law cannot depend on *which*
equal-capacity branch carries the future, only on the accounting structure.

Note what is *not* assumed: linearity of \(F\), any inner product, any
orthogonality relation, and any specific weight functional.

## 4. Main Theorem

### Lemma 4.1 (Mechanism symmetries are linear; real case)

Let \(\mathbb F=\mathbb R\). Every \(F\) as in HG-3 is a linear
\(\rho\)-isometry: \(F\in GL(V)\) and \(\rho(Fx)=\rho(x)\) for all \(x\).

*Proof.* \(F\) is a surjective isometry of the normed space \((V,\rho)\)
fixing the origin. By the Mazur–Ulam theorem, every surjective isometry
between real normed spaces is affine; fixing \(0\), it is linear. Linearity
plus \(d_\rho(Fx,0)=d_\rho(x,0)\) gives \(\rho(Fx)=\rho(x)\). Bijectivity
gives invertibility. \(\square\)

For \(\mathbb F=\mathbb C\), Mazur–Ulam yields only real-linearity. We
therefore *assume* complex-linearity of the mechanism symmetries in the
complex case; this is part of gap G3.

### Theorem 4.2 (Branch homogeneity forces inner-product geometry)

Let \((V,\rho)\) satisfy HG-1–HG-3 with \(\mathbb F=\mathbb R\). Then there
exists an inner product \(\langle\cdot,\cdot\rangle\) on \(V\) with

$$
\rho(x)=\sqrt{\langle x,x\rangle}
\qquad\forall x\in V ,
$$

and this inner product is unique. Moreover, every mechanism symmetry in HG-3
is orthogonal with respect to \(\langle\cdot,\cdot\rangle\).

*Proof.* Let

$$
G:=\{T\in GL(V):\rho(Tx)=\rho(x)\ \forall x\in V\}
$$

be the group of linear \(\rho\)-isometries. By Lemma 4.1, the maps supplied by
HG-3 lie in \(G\), so \(G\) acts transitively on the unit sphere
\(S_\rho:=\{x:\rho(x)=1\}\).

**\(G\) is compact.** Fix any auxiliary inner product \((\cdot,\cdot)_0\) on
\(V\). By norm equivalence in finite dimension there are \(0<a\le b\) with
\(a\|x\|_0\le\rho(x)\le b\|x\|_0\), so every \(T\in G\) has operator norm at
most \(b/a\) with respect to \(\|\cdot\|_0\): \(G\) is bounded. If
\(T_k\to T\) pointwise with \(T_k\in G\), then \(\rho(Tx)=\rho(x)\) for all
\(x\), so \(T\) is injective, hence invertible in finite dimension, hence
\(T\in G\): \(G\) is closed. A closed bounded subgroup of \(GL(V)\) is
compact.

**Invariant inner product by averaging.** Let \(\mu\) be the Haar probability
measure on the compact group \(G\) and define

$$
\langle u,v\rangle_G:=\int_G (Tu,Tv)_0\,d\mu(T).
$$

This is bilinear and symmetric; it is positive definite because for
\(u\neq 0\) the continuous integrand \((Tu,Tu)_0\) is strictly positive for
every invertible \(T\). For any \(S\in G\), right-invariance of \(\mu\) gives

$$
\langle Su,Sv\rangle_G
=\int_G (TSu,TSv)_0\,d\mu(T)
=\langle u,v\rangle_G .
$$

So \(N(x):=\sqrt{\langle x,x\rangle_G}\) is a \(G\)-invariant Euclidean norm.

**Transitivity collapses the two norms.** Fix \(u_0\in S_\rho\) and set
\(c:=N(u_0)>0\). For any \(v\in S_\rho\), transitivity supplies \(T\in G\)
with \(Tu_0=v\); \(G\)-invariance of \(N\) gives \(N(v)=N(u_0)=c\). So \(N\)
is constant on \(S_\rho\), and by homogeneity of both norms,

$$
\rho(x)=\frac{N(x)}{c}
\qquad\forall x\in V .
$$

Hence \(\rho\) is the norm of the inner product
\(\langle\cdot,\cdot\rangle:=\langle\cdot,\cdot\rangle_G/c^2\).

**Uniqueness.** An inner product is determined by its norm through the
polarization identity, so \(\langle\cdot,\cdot\rangle\) is unique. Every
\(T\in G\) preserves \(\rho\), hence by polarization preserves
\(\langle\cdot,\cdot\rangle\): \(G\) is a subgroup of the orthogonal group of
the derived geometry. \(\square\)

### Theorem 4.3 (Complex case, conditional)

Let \(\mathbb F=\mathbb C\) and assume additionally that the maps in HG-3 can
be chosen complex-linear. Then there exists a unique Hermitian inner product
\(\langle\cdot,\cdot\rangle\) on \(V\) with
\(\rho(x)=\sqrt{\langle x,x\rangle}\), and the mechanism symmetries are
unitary with respect to it.

*Proof.* Identical averaging argument with an auxiliary Hermitian form
\((\cdot,\cdot)_0\): the averaged form is sesquilinear, Hermitian, positive
definite, and \(G\)-invariant; transitivity on \(S_\rho\) collapses the norms
as before; uniqueness follows from complex polarization. \(\square\)

### Remark 4.4 (Why finite dimension is not a loss)

Without HG-2 the statement of Theorem 4.2 becomes the Banach–Mazur rotation
problem — whether a separable Banach space with transitive isometry group must
be Hilbertian — which remains open in general. The ACP position is that HG-2
is not an approximation but a physical admissibility condition: fixed-\(\ell\)
record channels are finite, and infinite-dimensional state spaces should enter
only as inductive limits over resolutions, in the same way
\(\mathcal M_\ell\) refines in
`bridges/relational_observable_macrostate_kernel.md`. Gap G2 in §9 records
what a controlled \(\ell\to\infty\) limit still requires.

### Corollary 4.5 (Weight depends only on capacity; BR-1 derived)

Let \(W:V\to[0,\infty)\) be continuous and invariant under the mechanism
group \(G\) of Theorem 4.2. Then there is \(f:[0,\infty)\to[0,\infty)\) with
\(W(v)=f(\rho(v))\).

*Proof.* Any two vectors of equal \(\rho\)-magnitude are related by an element
of \(G\) (transitivity plus homogeneity), and \(W\) is \(G\)-invariant.
\(\square\)

This is exactly Lemma 4.1 of `bridges/born_rule_from_acp.md`, previously
obtained from the *imported* axiom BR-1 (invariance under all unitaries). With
Corollary 4.5, the Born chain reads: HG-1–HG-3 give the inner-product
geometry and \(W=f(\rho)\); BR-2 (additivity on exclusive pairs, with
exclusivity now the *derived* orthogonality of §5), BR-3, and BR-4 then force
\(W=\rho^2\) as before.

## 5. Exclusivity Is Orthogonality

With the derived inner product in hand, the Born note's orthogonal branch
decomposition stops being an import.

### Proposition 5.1 (Real case)

In the geometry of Theorem 4.2, for \(u,v\in V\),

$$
W(u+v)=W(u)+W(v)
\iff
\langle u,v\rangle=0 .
$$

*Proof.* \(W(u+v)=\rho(u+v)^2=\rho(u)^2+\rho(v)^2+2\langle u,v\rangle\).
\(\square\)

So the additive-capacity relation — the ACP notion of mutually exclusive
future channels — coincides with orthogonality. Exclusivity is a theorem of
the derived geometry, not a postulate about it.

### Proposition 5.2 (Complex case: phase-robust exclusivity)

In the geometry of Theorem 4.3, for \(u,v\in V\):

1. \(W(u+v)=W(u)+W(v)\iff \operatorname{Re}\langle u,v\rangle=0\);
2. \(W(\lambda u+v)=W(u)+W(v)\) for **all** \(\lambda\in\mathbb C\) with
   \(|\lambda|=1\) \(\iff\) \(\langle u,v\rangle=0\).

*Proof.* \(\rho(\lambda u+v)^2=\rho(u)^2+\rho(v)^2
+2\operatorname{Re}(\bar\lambda\langle u,v\rangle)\) for \(|\lambda|=1\).
Statement 1 is \(\lambda=1\). For statement 2,
\(\operatorname{Re}(\bar\lambda\langle u,v\rangle)=0\) for all unimodular
\(\lambda\) forces \(\langle u,v\rangle=0\). \(\square\)

ACP reading: in a complex branch geometry, single-instance additivity is too
weak a notion of exclusivity — two branches can have additive weights at one
relative phase and interfere at another. Genuinely exclusive future channels
must have weights that add *robustly under internal mechanism-preserving
rephasing*, and phase-robust exclusivity is exactly complex orthogonality.
This sharpens BR-2: the mutually exclusive branches of the Born note are the
phase-robustly additive pairs.

## 6. What Selects the Complex Field (Open, Mapped)

Theorems 4.2 and 4.3 are field-blind: the homogeneity argument produces a
Euclidean geometry over \(\mathbb R\) and a Hermitian one over \(\mathbb C\),
and a quaternionic analog also exists. ACP branch homogeneity therefore does
*not* by itself select complex quantum theory. The known operational selector
is composition: local tomography — the requirement that joint states of
independent subsystems be determined by correlations of local measurements —
holds in complex quantum theory and fails in the real and quaternionic
variants (external inputs: Araki 1980; Wootters 1990; Hardy and Wootters
2012). In ACP terms this is a boundary-decodability requirement on
composition, continuous with TP-1–TP-4 of
`bridges/tensor_product_from_acp.md`:

> the record channels of the parts, plus their correlations, must suffice to
> decode the state of the whole; no composite prediction structure may be
> hidden from every local record.

Conjecture HG-C1 (field selection). *In a branch-homogeneity space
satisfying an ACP-native local-decodability composition axiom, the derived
geometry admits a complex structure and the composite geometry is the complex
tensor product; real and quaternionic realizations violate local
decodability.* ⚠ Open; this is the precise residual content of gap G3.

## 7. Reduction Map to Operational Reconstructions

The remaining route from ACP to the full complex Hilbert kinematics does not
need to be built from nothing. The operational reconstruction programs
(external inputs: Hardy 2001; Chiribella–D'Ariano–Perinotti 2011;
Masanes–Müller 2011) already derive finite-dimensional complex quantum theory
from short axiom lists. OP-21 therefore decomposes into proving that ACP
admissibility *forces* those axioms. The current mapping:

| Reconstruction axiom (source) | Operational content | ACP counterpart | Status |
|---|---|---|---|
| Causality (CDP) | no signaling from future measurement choices | directedness of persistent record channels; boundary laws condition on past records only | ACP-plausible, unproven |
| Perfect distinguishability (CDP; MM subspace axiom; Hardy) | every state outside the complete mixture is perfectly distinguishable from some state | existence of decodable records: finitely many perfectly distinguishable macrostates at fixed resolution (coordination floor) | ACP-plausible, close to forced at fixed \(\ell\) |
| Ideal compression (CDP) | every source has a lossless minimal encoding | finite-record sufficiency of macrostate kernels (`bridges/relational_observable_macrostate_kernel.md`) | ACP-plausible, unproven |
| Local discriminability / tomographic locality (Hardy; CDP; MM) | local records + correlations decode joint states | boundary-decodable independent composition (TP lineage; §6) | ACP-plausible; known to select \(\mathbb C\) |
| Continuous reversibility (MM; Hardy) | reversible transformations form a continuous group connecting pure states | UE-1/UE-3 mechanism-preserving continuous flow; HG-3 transitivity is its transitive-action shadow | ACP-forced within the quartet's axiom set |
| Purification (CDP) | every mixed state has a pure mechanism-preserving dilation, unique up to reversible symmetry | conservation of prediction structure: no unlocated missingness; now ACP-cast as PU-1–PU-3 in `bridges/purification_from_acp.md`, with the classical-regress/classical-exclusion theorems proved and quantum minimality/uniqueness verified | ACP-cast; classical exclusion proved; CDT derivation of PU-2 open |

Derivation strategy for OP-21, restated as a finite lemma list:

1. formalize ACP admissibility as an operational probabilistic theory (states,
   effects, transformations with finite decodable records) — gap G1 is the
   convexity/linearity step;
2. prove each ACP-plausible row above as a theorem from ACP axioms;
3. invoke a reconstruction theorem to obtain finite-dimensional complex
   Hilbert kinematics;
4. the quartet then upgrades from ACP-selected to ACP-derived, with
   Theorem 4.2 available as an independent shortcut for the geometry step.

## 8. Relation to Existing ACP Quantum Material

This note modifies the standing of the quartet as follows:

- `bridges/born_rule_from_acp.md`: BR-1 is no longer an independent import;
  Corollary 4.5 derives its consequence (weight depends only on capacity)
  from HG-3. Orthogonal branch decomposition is reinterpreted via §5 as
  (phase-robust) additive exclusivity.
- `bridges/unitary_evolution_from_acp.md`: HG-3 is the static (transitive
  relabeling) shadow of UE-1–UE-3; conversely the unitary note's flow now
  acts on a geometry that is itself ACP-motivated rather than assumed.
- `bridges/tensor_product_from_acp.md`: unchanged conditionally; §6 assigns
  it the additional role of field selector via local decodability.
- `bridges/measurement_formalism_from_acp.md`: unchanged conditionally; the
  positive-cone linearity it assumes belongs to gap G1.
- `bridges/reality_reflective_mathematics.md`: HG-2 is its finite-observable
  admissibility condition doing concrete mathematical work (Remark 4.4).
- `bridges/coordination_neutrality.md` and `bridges/restraint_power.md`:
  HG-3 is a branch-space instance of coordination neutrality —
  equal-capacity branches are dynamically interchangeable.

## 9. What This Does Not Yet Do

The honest residue, named:

- **G1 (linear prediction space).** Why prediction states form a vector space
  with superposition as addition, and why weights/outcome functionals are
  additive on the positive cone. This is the deepest gap; the operational
  route in §7 (convex state spaces from record statistics) is the intended
  attack, but nothing is proved.
- **G2 (infinite dimensions).** Theorem 4.2 is finite-dimensional and the
  unrestricted analog is the open rotation problem. Required: a controlled
  inductive limit over resolutions \(\ell\), compatible with the macrostate
  kernel refinements, that preserves the derived inner product.
- **G3 (complex structure).** The complex case of Theorem 4.3 assumes
  complex-linearity; field selection is Conjecture HG-C1 and rests on an
  ACP-native local-decodability axiom not yet formalized.
- **G4 (reconnection to gravity).** OP-21 exists inside a program whose
  primary front is gravitational. The branch space at resolution \(\ell\)
  should be identified with the sector space of the relational macrostate
  kernel, so that the derived inner product appears as the overlap geometry
  of boundary records \(R_\partial\). Nothing here yet touches that
  identification.

So the actual theorem of this note is:

> given a finite-dimensional normed branch space whose
> distinguishability-preserving symmetries relabel equal-capacity branches
> transitively, the branch geometry is inner-product, its exclusivity relation
> is orthogonality, and the Born chain proceeds without importing unitary
> invariance.

## 10. Open Direction

Priority order for continuing OP-21:

1. **G1 first, operationally.** Define ACP-admissible record statistics for a
   finite system and prove the state space is a compact convex set with
   finitely many perfectly distinguishable extreme points at fixed
   resolution — the entry point of every reconstruction program.
2. **Formalize the local-decodability composition axiom** and attempt
   Conjecture HG-C1, using the tensor-product note's TP axioms as the
   template.
3. **Prove the purification row** of the §7 table from restraint-power
   conservation; it is the single most powerful reconstruction axiom and the
   most ACP-resonant.
4. **G4 reconnection:** state the branch-homogeneity axioms for the
   relational macrostate kernel's sector spaces and check whether the
   gravitational boundary-record overlap structure satisfies HG-3.

*Update:* step 1 is now taken in
`bridges/operational_state_space_from_acp.md`: ACP record-statistics axioms
(OS-1–OS-5) force the compact convex state space, the linear effect structure
on a generating cone with order unit, and finite record capacity. This closes
G1 at the framework (GPT) level — G1a — leaving G1b: the passage from the
convex state space to the branch vector space via the §7 reconstruction rows.
