# Operational State Space from ACP Record Statistics

*Status: exploratory bridge note; the main theorems are **proved** from five
operational axioms (OS-1–OS-5), each with an explicit ACP motivation and two
flagged as idealizations. The note closes gap G1 of
`bridges/hilbert_geometry_from_acp.md` at the framework level: the convex,
finite-dimensional, linearizable state space that every operational
reconstruction of quantum theory takes as its starting point is here derived
from ACP-style record-statistics axioms rather than assumed. What remains of
G1 is the passage from the convex state space to the branch vector space,
which is the business of the reconstruction rows in
`bridges/hilbert_geometry_from_acp.md` §7.*

## 1. Thesis

The branch-homogeneity bridge proved that a finite-dimensional *normed linear*
branch space with transitive mechanism symmetries must be an inner-product
space, and named as gap G1 the deepest import: why prediction states form a
linear structure at all.

This note attacks G1 from the operational side. The claim:

> if a system at fixed resolution has reproducible record statistics, if its
> states are identified by their decodable records, if non-disturbing
> classical randomization is available, and if finitely many record outcomes
> suffice to identify a state, then the state space is (after statistical
> completion) a compact convex subset of a finite-dimensional real vector
> space, mixing is convex combination, every admissible outcome functional
> extends uniquely to a linear functional on the spanning cone, and the number
> of jointly perfectly distinguishable states is finite, bounded by both the
> record alphabet and the affine dimension plus one.

Linearity, in other words, is not a metaphysical posit about superposition.
At the state-space level it is a bookkeeping theorem about decodable classical
records: the law of total probability, applied to non-disturbing coins, *is*
the convex structure, and the cone lift of that convex structure *is* the
linear structure.

A modest but pleasing corollary falls out: both ACP absorbing boundaries —
dissolution and crystallization — degenerate the operational state space to a
single point. The productive interval is exactly the regime in which the
operational state space has positive affine dimension.

## 2. Setup: Preparations, Records, Statistics

Fix a system \(S\) and a resolution \(\ell\).

- Let \(\mathcal P\) be a nonempty set of **preparation procedures**: things
  the past boundary of \(S\) can do.
- Let \(\mathcal R\) be a nonempty **finite** set of **record channels**
  admissible at resolution \(\ell\); each \(M\in\mathcal R\) has a finite
  outcome alphabet \(O_M\).
- Statistics: for each \(P\in\mathcal P\) and \(M\in\mathcal R\), a
  probability distribution \(p(\,\cdot\mid P,M)\) on \(O_M\).

Write

$$
N:=\sum_{M\in\mathcal R}|O_M|
$$

and define the **fiducial map**

$$
\Phi:\mathcal P\to[0,1]^N,
\qquad
\Phi(P):=\big(p(o\mid P,M)\big)_{M\in\mathcal R,\;o\in O_M}.
$$

## 3. ACP-Motivated Operational Axioms

### Axiom OS-1 (Reproducible record statistics)

Each pair \((P,M)\) determines a well-defined outcome distribution
\(p(\,\cdot\mid P,M)\), stable under repetition of the procedure.

Interpretation: this is what a persistent boundary law *is* in ACP terms — a
reproducible statistic on a record channel. A "law" whose record statistics
do not reproduce is not a persistent law; the CDT applies to systems that
have this much stability, and admissibility
(`bridges/reality_reflective_mathematics.md`) requires finite verification
time for exactly these statistics.

### Axiom OS-2 (Record-native identification)

Preparations with identical statistics on every admissible record channel are
operationally the same state:

$$
\Phi(P)=\Phi(Q)
\ \Longrightarrow\
P\sim Q .
$$

The **state space at resolution \(\ell\)** is the image

$$
K_0:=\Phi(\mathcal P)\subseteq[0,1]^N ,
$$

so states are *by construction* their fiducial record vectors.

Interpretation: reality-reflective admissibility — a distinction that no
admissible record channel can decode is not part of a world-facing
description at this resolution. This is the kinematic form of the same
principle that makes undecodable interior distinctions inadmissible in the
gravitational program.

### Axiom OS-3 (Non-disturbing classical randomization)

For all \(P,Q\in\mathcal P\) and \(\lambda\in[0,1]\) there is a preparation
\(\mathrm{mix}_\lambda(P,Q)\in\mathcal P\) realized by sampling an auxiliary
classical record \(c\in\{0,1\}\) with \(\Pr(c=0)=\lambda\), independent of
\(S\), and preparing \(P\) if \(c=0\), \(Q\) if \(c=1\), such that the
coin is **non-disturbing**: for every \(M\) and \(o\),

$$
p(o\mid \mathrm{mix}_\lambda(P,Q),M,\,c=0)=p(o\mid P,M),
\qquad
p(o\mid \mathrm{mix}_\lambda(P,Q),M,\,c=1)=p(o\mid Q,M).
$$

Interpretation: classical record channels exist (the dissolution side of the
interval guarantees entropy sources with decodable outcomes), and steering a
preparation by a decodable classical record is a coordination-neutral
composition — the coin coordinates *which* preparation runs without touching
the mechanism of either.

⚠ Non-disturbance is a genuine assumption, not a theorem: it posits that the
classical ancilla can be coupled to the choice of preparation without
back-action on the prepared statistics. It is the operational sibling of
TP-1 (independent preparation) in `bridges/tensor_product_from_acp.md`.

### Axiom OS-4 (Finite fiducial capacity)

\(\mathcal R\) is finite with finite alphabets, and identification (OS-2) is
relative to this finite set.

Interpretation: the finite-observable admissibility condition, and the
operational sibling of HG-2 in `bridges/hilbert_geometry_from_acp.md`. At
fixed resolution, a state is a finite record object.

### Axiom OS-5 (Statistical completion)

Limits of preparations that converge in statistics are admissible ideal
preparations: the state space is closed in \([0,1]^N\).

⚠ This is an idealization axiom, standard in operational frameworks: it adds
to \(K_0\) only points that are statistically indistinguishable in the limit
from realizable preparations. All results below except compactness hold for
\(K_0\) without it.

## 4. Linearization Theorems

### Lemma 4.1 (Mixing is affine)

For all \(P,Q\in\mathcal P\), \(\lambda\in[0,1]\):

$$
\Phi\big(\mathrm{mix}_\lambda(P,Q)\big)
=\lambda\,\Phi(P)+(1-\lambda)\,\Phi(Q).
$$

*Proof.* Fix \(M,o\). The coin outcome is a decodable record with
\(\Pr(c=0)=\lambda\), so the law of total probability gives

$$
p(o\mid\mathrm{mix}_\lambda,M)
=\lambda\,p(o\mid\mathrm{mix}_\lambda,M,c=0)
+(1-\lambda)\,p(o\mid\mathrm{mix}_\lambda,M,c=1),
$$

and non-disturbance (OS-3) replaces the conditionals by
\(p(o\mid P,M)\) and \(p(o\mid Q,M)\). \(\square\)

This is the exact sense in which convexity is *derived*: it is nothing but
total probability over a decodable classical record, and it fails only if the
coin disturbs or is undecodable.

### Theorem 4.2 (Compact convex state space)

Under OS-1–OS-5, the state space

$$
K:=\overline{K_0}\subseteq[0,1]^N
$$

is a nonempty compact convex set, and mixing of preparations is convex
combination of states.

*Proof.* \(K_0\) is nonempty and convex by Lemma 4.1 (its image points are
closed under all binary convex combinations, hence under finite ones by
iteration). It is bounded, being contained in the cube. Its closure \(K\) is
then compact (closed and bounded in \(\mathbb R^N\)) and convex (closure of a
convex set). OS-5 says \(K\) consists of admissible states. \(\square\)

### Lemma 4.3 (Affine functions respect finite convex combinations)

If \(f:K\to\mathbb R\) satisfies
\(f(\lambda x+(1-\lambda)y)=\lambda f(x)+(1-\lambda)f(y)\), then for any
finite convex combination,
\(f\big(\sum_i w_i x_i\big)=\sum_i w_i f(x_i)\).

*Proof.* Induction on the number of terms, splitting off one weight at a
time. \(\square\)

### Theorem 4.4 (Cone lift: linear structure)

Define the lift \(L:K\to\mathbb R^{1+N}\), \(L(x):=(1,x)\), and set

$$
V:=\mathrm{span}\,L(K),
\qquad
C:=\mathbb R_{\ge0}\,L(K),
\qquad
u(t,x):=t .
$$

Then:

1. \(C\) is a closed generating cone in \(V\), \(u\) is strictly positive on
   \(C\setminus\{0\}\), and \(K\) is affinely isomorphic to the base
   \(\{v\in C: u(v)=1\}\);
2. every affine \(f:K\to\mathbb R\) extends to a **unique** linear functional
   \(\hat f:V\to\mathbb R\) with \(\hat f(1,x)=f(x)\);
3. in particular every admissible outcome functional
   \(x\mapsto p(o\mid x,M)\) is the restriction of a unique linear
   \(\hat e_{M,o}\) with \(0\le\hat e_{M,o}\le u\) on \(C\), and for each
   channel \(\sum_{o\in O_M}\hat e_{M,o}=u\).

*Proof.* (1) \(C\) is a cone by construction and spans \(V\); \(u\) equals
the lifted first coordinate, which is \(1\) on \(L(K)\) and scales with the
cone parameter, so it is strictly positive on \(C\setminus\{0\}\) and
\(u^{-1}(1)\cap C=L(K)\cong K\). Closedness of \(C\) follows from compactness
of \(K\): a convergent sequence \(t_k(1,x_k)\to(t,y)\) has \(t_k\to t\); if
\(t>0\) then \(x_k\to y/t\in K\); if \(t=0\) then boundedness of \(K\) forces
\(y=0\).

(2) Uniqueness is immediate since \(L(K)\) spans \(V\). Existence requires
well-definedness of

$$
\hat f\Big(\sum_i\alpha_i(1,x_i)\Big):=\sum_i\alpha_i f(x_i).
$$

Suppose \(\sum_i\alpha_i(1,x_i)=0\). The first coordinate gives
\(\sum_i\alpha_i=0\). Split \(\alpha_i=\beta_i-\gamma_i\) into positive and
negative parts over disjoint index sets, with
\(s:=\sum_i\beta_i=\sum_i\gamma_i\). If \(s=0\) all \(\alpha_i\) vanish.
Otherwise \(p:=\sum_i(\beta_i/s)x_i\) and \(q:=\sum_i(\gamma_i/s)x_i\) lie in
\(K\) by convexity, and the remaining coordinates give
\(\sum_i\beta_ix_i=\sum_i\gamma_ix_i\), i.e. \(p=q\). Lemma 4.3 then gives

$$
\sum_i\beta_i f(x_i)=s\,f(p)=s\,f(q)=\sum_i\gamma_i f(x_i),
$$

so \(\sum_i\alpha_i f(x_i)=0\), as required. Linearity of \(\hat f\) is then
immediate from the definition.

(3) Outcome functionals are affine on \(K\): on \(K_0\) this is Lemma 4.1,
and affinity passes to the closure by continuity of the coordinate
functionals (on the fiducial channels the outcome functionals *are*
coordinates of the embedding). Apply (2); the bounds \(0\le\hat e\le u\) on
\(C\) and the completeness relation \(\sum_o\hat e_{M,o}=u\) hold on
\(L(K)\) by normalization of probability and extend to \(C\) by homogeneity.
\(\square\)

The triple \((V,C,u)\) — an ordered finite-dimensional vector space with
closed generating cone and order unit, states as the compact base, effects as
the unit interval of the dual cone — is precisely the general probabilistic
theory (GPT) framework object that operational reconstructions of quantum
theory postulate on page one. Here it is a theorem from OS-1–OS-5.

## 5. Finite Record Capacity

### Definition 5.1 (Joint perfect distinguishability)

States \(x_1,\dots,x_k\in K\) are **jointly perfectly distinguishable** if
there exist a record channel \(M\) and a partition of \(O_M\) into nonempty
sets \(S_1,\dots,S_k\) with

$$
p(S_i\mid x_j,M)=\delta_{ij} .
$$

### Theorem 5.2 (Record-capacity bounds)

If \(x_1,\dots,x_k\) are jointly perfectly distinguishable, then:

1. \(k\le|O_M|\) for the distinguishing channel \(M\);
2. \(x_1,\dots,x_k\) are affinely independent, hence
   \(k\le\dim_{\mathrm{aff}}(K)+1\le N+1\).

Consequently the **record capacity**

$$
N_{\mathrm{dist}}(\ell)
:=\max\{k:\ \exists\ k\ \text{jointly perfectly distinguishable states}\}
$$

is finite, with

$$
N_{\mathrm{dist}}(\ell)
\;\le\;
\min\Big(\max_{M\in\mathcal R}|O_M|,\ \dim_{\mathrm{aff}}(K)+1\Big).
$$

*Proof.* (1) The \(S_i\) are nonempty and disjoint in \(O_M\).

(2) Let \(f_i(x):=p(S_i\mid x,M)=\sum_{o\in S_i}p(o\mid x,M)\), affine on
\(K\) with lift \(\hat f_i\) by Theorem 4.4, and \(f_i(x_j)=\delta_{ij}\).
Suppose \(\sum_j\alpha_j(1,x_j)=0\). Applying \(\hat f_i\) gives
\(\alpha_i=0\) for each \(i\). So the lifted vectors \((1,x_j)\) are linearly
independent in \(V\), which is affine independence of the \(x_j\); a convex
set of affine dimension \(d\) contains at most \(d+1\) affinely independent
points, and \(\dim_{\mathrm{aff}}(K)\le N\). \(\square\)

This is the operational coordination floor in kinematic form: at fixed
resolution, the number of perfectly separable futures is finite and bounded
by the record geometry — by the alphabet on one side and by the state-space
dimension on the other. In quantum theory the second bound is the statement
that a \(d\)-dimensional system admits at most \(d\) jointly perfectly
distinguishable states while its state space has affine dimension
\(d^2-1\); the bound is respected, not saturated, which is one signature of
the non-classicality the reconstruction rows must supply.

## 6. Boundary Degeneracy

### Proposition 6.1 (Operational singletons)

The following are equivalent:

1. \(K\) is a singleton;
2. every record channel's statistics are preparation-independent:
   \(p(o\mid P,M)=p(o\mid Q,M)\) for all \(P,Q,M,o\);
3. for every ensemble of preparations and every record channel \(M\), the
   mutual information between the ensemble label and the record outcome
   vanishes: \(I(\mathrm{prep};O_M)=0\).

*Proof.* (1)\(\Leftrightarrow\)(2): states are their fiducial vectors, so
\(K\) is a singleton iff all fiducial probabilities are
preparation-independent. (2)\(\Rightarrow\)(3): if the conditional
distribution of \(O_M\) does not depend on the label, the joint distribution
factorizes and the mutual information vanishes. (3)\(\Rightarrow\)(2): apply
(3) to the two-point ensemble \(\{P,Q\}\) with equal weights; zero mutual
information for a two-point label forces the two conditionals to coincide.
\(\square\)

### ACP reading: both absorbing boundaries are operational singletons

The two ACP boundaries degenerate \(K\) in the same kinematic way while
differing dynamically:

- **Dissolution.** Record channels decouple from preparations: every
  preparation is washed to the same statistics before any record forms.
  Condition (2) holds; \(K\) collapses to one point.
- **Crystallization.** A single absorbing macrostate captures all
  preparations: records are perfectly reproducible but carry no
  preparation dependence. Condition (2) holds again; \(K\) collapses to the
  same kind of point.

So kinematics alone cannot tell the boundaries apart — a maximally noisy
channel and a perfectly frozen one both read as "one state." The distinction
between the boundaries is dynamical (how the transition kernel behaves, what
\(H_{\ell,\Delta}\) does), which is consistent with the CDT being a statement
about dynamics rather than state-space shape.

### Proposition 6.2 (Productive interval requires nondegenerate state space)

If a system at resolution \(\ell\) occupies the productive interval — in
particular, if some record channel carries nonzero information about the
preparation, \(I(\mathrm{prep};O_M)>0\) for some ensemble and channel — then
\(\dim_{\mathrm{aff}}(K)\ge 1\).

*Proof.* Immediate contrapositive of Proposition 6.1. \(\square\)

Note the gap between Proposition 6.2 and sharp structure: positive mutual
information yields two *distinct* states, not two *perfectly distinguishable*
ones. \(N_{\mathrm{dist}}(\ell)\ge2\) — the existence of genuinely decodable
records — is strictly stronger, which is why the perfect-distinguishability
row of the reconstruction table in `bridges/hilbert_geometry_from_acp.md` §7
is classified "close to forced" rather than "forced": ACP guarantees
informative records inside the interval; making them sharp requires an
additional decodability postulate or a limit argument.

## 7. ACP Reading

### 7.1 Linearity as record bookkeeping

The chain is short and each link is auditable:

1. persistent boundary law \(\Rightarrow\) reproducible record statistics
   (OS-1);
2. admissible description \(\Rightarrow\) states are record-equivalence
   classes (OS-2);
3. decodable classical records + coordination-neutral coins
   \(\Rightarrow\) total probability \(\Rightarrow\) convexity (OS-3,
   Lemma 4.1);
4. finite records \(\Rightarrow\) finite dimension (OS-4);
5. cone lift \(\Rightarrow\) linear effects on a generating cone
   (Theorem 4.4).

Superposition is *not* derived here — \(K\) is a state space, and its convex
combinations are classical mixtures, not coherent sums. What is derived is
the ambient linear-functional structure that makes "superposition" a
formulable hypothesis at all.

### 7.2 The floor in kinematic form

Theorem 5.2 bounds separable futures by record geometry. Read against
`bridges/restraint_power.md`: the coordination floor said monitoring capacity
is conserved and strictly positive in noncommutative partitions; the record
capacity says the *kinematic budget* of perfectly separable alternatives is
finite at fixed resolution. The dynamical floor and the kinematic budget are
the two halves the reconstruction program must eventually join.

## 8. Relation to Existing ACP Quantum Material

- `bridges/hilbert_geometry_from_acp.md`: this note is the G1a step of its
  §7 strategy (item 1: operational grounding). Its HG-1 axiom posited a
  normed linear branch space; the present note derives the linear operational
  shell \((V,C,u)\) but **not** the branch space itself — see §9.
- `bridges/born_rule_from_acp.md` and
  `bridges/measurement_formalism_from_acp.md`: MF-1–MF-3 (positivity,
  cone-linearity, budget conservation) were *axioms* on positive branch
  operators; Theorem 4.4(3) derives their operational analogs for record
  functionals on \(K\). The Born-note structure remains conditional on the
  branch space.
- `bridges/tensor_product_from_acp.md`: OS-3's non-disturbing coin is the
  classical shadow of TP-1 independent preparation; the composite-system
  version of this note (product states, local decodability) is exactly the
  G3 selector question.
- `bridges/relational_observable_macrostate_kernel.md`: \(K\) at resolution
  \(\ell\) is the kinematic companion of the macrocell partition
  \(\mathcal M_\ell\); the G4 reconnection task is to present the
  gravitational sector statistics as a \((V,C,u)\) triple.

## 9. What This Does Not Yet Do

- **It does not produce the branch (Hilbert) vector space.** \(V\) is the
  span of *states*; quantum theory's \(V\) is the space of density operators,
  not the underlying \(\mathcal H\). Passing from \((V,C,u)\) to a branch
  space requires the reconstruction rows (perfect distinguishability, ideal
  compression, local decodability, continuous reversibility, purification) —
  that is G1b, and it is where the quantum/classical fork lies: classical
  probability satisfies OS-1–OS-5 too, with \(K\) a simplex. Nothing in this
  note separates quantum from classical; it derives their common frame.
- **OS-3 and OS-4 are ACP-motivated, not ACP-derived.** Non-disturbing
  randomizers and finite fiducial sets are argued from coordination
  neutrality and finite-record admissibility informally; deriving them from
  the CDT axiom set proper is open.
- **OS-5 is an idealization** (statistical completion), inherited by
  compactness claims only.
- **Sharpness is not free.** Proposition 6.2 gives nondegeneracy inside the
  productive interval, not \(N_{\mathrm{dist}}\ge2\); the sharp-records
  postulate remains a separate lemma target.

So the actual theorem of this note is:

> ACP-style record-statistics axioms force the general-probabilistic-theory
> state-space frame — compact convex states, linear effects on a generating
> cone with order unit, finite record capacity — and both ACP absorbing
> boundaries appear in it as the degenerate (singleton) case.

## 10. Open Direction

1. **Sharp records lemma.** Derive \(N_{\mathrm{dist}}(\ell)\ge2\) inside the
   productive interval from a decodability or asymptotic-repetition argument
   (many-copy record channels sharpening statistical distinctness into
   perfect distinguishability), closing the gap flagged in §6.
2. **Derive OS-3 from coordination neutrality.** State the coin as an
   explicit CN ancilla and prove non-disturbance from mechanism-preserving
   composition instead of postulating it.
3. **Composite systems.** Extend OS-1–OS-5 to pairs of systems and formalize
   local decodability as an axiom on the composite \((V,C,u)\); this is the
   entry point for Conjecture HG-C1 (field selection).
4. **Purification next.** With the GPT frame now derived, the purification
   row of the reconstruction table is the highest-value single target: it is
   the most powerful axiom in the CDP reconstruction and the most
   ACP-resonant (conservation of prediction structure under dilation).
