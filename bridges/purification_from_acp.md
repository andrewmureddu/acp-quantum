# Purification from ACP Conservation: Relational Mixedness and the Classical Regress

*Status: exploratory bridge note; the classical-regress theorem, the
classical-exclusion corollary, and the quantum existence/minimality/uniqueness
theorems are **proved**. The central axiom PU-2 (record locatability) is an
ACP-cast of the Chiribella–D'Ariano–Perinotti purification postulate: the
casting is argued from restraint-power conservation and reality-reflective
admissibility, but PU-2 is not yet derived from the CDT axiom set proper.
That derivation is the remaining hard core and is flagged in §9.*

## 1. Thesis

The reconstruction table in `bridges/hilbert_geometry_from_acp.md` §7 marked
purification as the most ACP-resonant reconstruction axiom. This note makes
that precise and extracts its first theorem-level payoff.

The ACP-cast of purification is a conservation principle:

> **No unlocated missingness.** A state with missing records — a mixed state —
> is admissible only if the missing information is *located*: there must exist
> a finite record system such that the joint description of system plus record
> is complete (extremal), with the mixed state as its marginal, and the record
> system carries exactly the missing information, no more.

The payoff is a fork:

- **Classical theories cannot satisfy it.** In a simplex theory, every
  extension of a mixed state by classical records is itself mixed: the
  location process is an infinite regress, so classical descriptions either
  violate conservation (dangling missingness) or violate finite-record
  admissibility (unterminated regress). Proved below as the classical-regress
  theorem.
- **Quantum theory satisfies it exactly.** Every density operator has a
  purification; the minimal record system has dimension equal to the state's
  rank; it carries entropy equal to the missing information; and any two
  minimal purifications differ by a reversible transformation of the record
  system alone. Proved below in the finite-dimensional case.

So within the GPT frame derived in
`bridges/operational_state_space_from_acp.md`, ACP conservation with finite
records forces **non-classical** state spaces — the first quantum/classical
fork result in the OP-21 program. What it does not yet force is quantum
theory specifically; that residual is the (cited) CDP reconstruction theorem
plus the still-open derivation of PU-2 from CDT.

## 2. Setup: States, Completeness, Composites

Work in the frame of `bridges/operational_state_space_from_acp.md`: a system
\(S\) at fixed resolution is a triple \((V_S,C_S,u_S)\) with compact convex
state space \(K_S\).

- A state \(\omega\in K_S\) is **complete** if it is an extreme point of
  \(K_S\), and **incomplete (mixed)** otherwise.

  Interpretation: an extreme point admits no nontrivial ensemble reading —
  there is no further "which alternative" record any channel could reveal. A
  mixed state \(\omega=\lambda\omega_1+(1-\lambda)\omega_2\) does: the
  ensemble label is information about \(S\) that the description of \(S\)
  does not carry.

- A **composite** \(SE\) of systems \(S\) and \(E\) is a system
  \((V_{SE},C_{SE},u_{SE})\) equipped with an affine surjective
  **marginalization** map
  \(\mathrm{tr}_E:K_{SE}\to K_S\) (operationally: apply the unit effect of
  \(E\), i.e., record nothing about \(E\)) and product states
  \(\omega\otimes\varphi\) with
  \(\mathrm{tr}_E(\omega\otimes\varphi)=\omega\).

- An **extension** of \(\omega\in K_S\) is a pair \((E,\Omega)\) with
  \(\Omega\in K_{SE}\) and \(\mathrm{tr}_E\,\Omega=\omega\). A **completion**
  is an extension whose \(\Omega\) is complete (extreme in \(K_{SE}\)).

Mixed states exist for any system inside the productive interval that is not
statistically trivial: OS-3 randomization followed by discarding the coin
record produces, for any two distinct states, every nontrivial mixture on the
open segment between them, and a segment interior point of a convex set with
two distinct points is non-extreme whenever the two endpoints are distinct.

## 3. ACP Conservation Axioms

### Axiom PU-1 (Mixedness is missing records)

The incomplete states of \(S\) are exactly the non-extreme points of
\(K_S\), and the missing information of
\(\omega=\sum_i\lambda_i\omega_i\) is ensemble information: which extremal
alternative is realized.

Interpretation: this is a definition-level axiom fixing the ACP reading of
convex structure. It inherits its legitimacy from
`bridges/operational_state_space_from_acp.md`, where mixing was derived as
total probability over a decodable coin: the coin record *is* the ensemble
label, and discarding it is what creates the missingness.

### Axiom PU-2 (Record locatability / no unlocated missingness)

Every admissible state \(\omega\in K_S\) has a completion: a finite
admissible record system \(E\) and a **complete** state \(\Omega\in K_{SE}\)
with \(\mathrm{tr}_E\,\Omega=\omega\).

Interpretation: restraint-power conservation says mechanism-preserving
dynamics never destroy prediction structure — they relocate it into channels.
Reality-reflective admissibility says uncertainty in an admissible
description must be *allocated*: carried by a normalizable, decodable record
channel, not free-floating. A mixed state whose ensemble information existed
nowhere — not in \(S\), not in any finite record system coupled to \(S\) —
would be missingness without a channel: unallocated uncertainty, which the
admissibility ladder rejects.

⚠ Honesty: PU-2 is the purification postulate of
Chiribella–D'Ariano–Perinotti (2011), *re-derived in motivation but not in
mathematics*. The ACP argument above is a casting, not a proof from CDT
axioms; the gap is recorded in §9.

### Axiom PU-3 (Minimal records / uniqueness up to record symmetry)

Completions are unique up to reversible transformations of the record system:
if \((E,\Omega_1)\) and \((E,\Omega_2)\) are completions of the same
\(\omega\) with \(E\) minimal, there is a reversible transformation \(R_E\)
of \(E\) alone with \((\mathrm{id}_S\otimes R_E)\,\Omega_1=\Omega_2\).

Interpretation: the located record channel carries exactly the missing
information. If two completions were not related by a relabeling of the
record side, the composite would encode a physical difference invisible in
\(\omega\) and not attributable to record bookkeeping — surplus structure of
the kind `bridges/self_limiting_universality.md` calls undecodable
possession. Restraint on the record channel is what makes the location
*minimal*.

## 4. The Classical Regress

Define a **classical system** as one whose state space is a simplex: \(K_S\)
is the convex hull of a finite set of extreme points \(\{\delta_s\}_{s\in A_S}\)
(the alphabet), every state having a *unique* extremal decomposition — the
defining property of classical probability at the GPT level. Define
**classical composition**: the composite of classical systems \(S,E\) is the
classical system on the product alphabet \(A_S\times A_E\) (states are joint
distributions), with marginalization the usual sum over \(A_E\) and products
the product distributions.

### Theorem 4.1 (Classical regress)

Let \(S\) be classical and \(\omega\in K_S\) mixed. Then **every** classical
extension of \(\omega\) is mixed: for every classical \(E\) and every
\(\Omega\in K_{SE}\) with \(\mathrm{tr}_E\,\Omega=\omega\), the state
\(\Omega\) is not extreme. Consequently no finite iteration of classical
record adjunction ever completes \(\omega\): if
\(\Omega_k\in K_{SE_1\cdots E_k}\) extends \(\omega\), then \(\Omega_k\) is
mixed, for every \(k\).

*Proof.* Extreme points of the classical composite are the point masses
\(\delta_{(s,e)}\) on \(A_S\times A_E\). The marginal of \(\delta_{(s,e)}\)
is \(\delta_s\), which is extreme in \(K_S\). Hence any \(\Omega\) whose
marginal is the mixed \(\omega\) cannot be a point mass, i.e., is not
extreme. The iterated statement follows by applying the same argument to the
classical composite \(S(E_1\cdots E_k)\), which is again classical on the
product alphabet. \(\square\)

### Corollary 4.2 (Classical exclusion)

A theory in which (i) some admissible system has a mixed state (OS-3 with
discarded coins inside a statistically nontrivial productive interval),
(ii) PU-2 holds, and (iii) systems and their record extensions compose
classically, is inconsistent. Hence ACP conservation with finite records
forces non-classical state spaces: some composite must possess complete
(extreme) states with mixed marginals.

*Proof.* Immediate from Theorem 4.1: (i) provides \(\omega\) mixed, (iii)
makes every finite extension mixed, contradicting (ii). The final statement
is the contrapositive: keeping (i) and (ii) requires dropping (iii), and a
complete state with a mixed marginal is exactly what classical composition
forbids. \(\square\)

The ACP reading is sharp. Classically, locating missing records only ever
*re-describes* the missingness one system further out — the coin that
explains the mixture is itself jointly mixed with the system, requiring a
second coin, and so on. Classical descriptions therefore face a trilemma:
dangling missingness (violating conservation, PU-2), infinite regress
(violating finite-record admissibility, OS-4/HG-2), or statistical
triviality (crystallization: no mixed states, no interval). The only escape
is structural: composites whose complete states are correlated — pure states
with mixed marginals. Entanglement-like structure is not an exotic addition;
it is the unique way to conserve prediction structure with finite records.

## 5. Quantum Theory Terminates the Regress in One Step

We now verify that finite-dimensional quantum theory satisfies PU-1–PU-3
exactly, with quantitative control of the record system. Everything here is
standard; it is included to fix the minimality and uniqueness statements in
the forms the ACP axioms require.

Let \(\rho\) be a density operator on \(\mathcal H_S\),
\(\dim\mathcal H_S=d\), with spectral decomposition
\(\rho=\sum_{i=1}^{r}p_i|i\rangle\langle i|\), \(p_i>0\),
\(r=\mathrm{rank}\,\rho\).

### Theorem 5.1 (Existence and minimality)

For any \(\mathcal H_E\) with \(\dim\mathcal H_E\ge r\) there is a pure state
\(|\Omega\rangle\in\mathcal H_S\otimes\mathcal H_E\) with
\(\mathrm{Tr}_E|\Omega\rangle\langle\Omega|=\rho\); and no
\(\mathcal H_E\) with \(\dim\mathcal H_E<r\) admits one. Thus the minimal
record dimension is exactly \(\mathrm{rank}\,\rho\).

*Proof.* Existence: pick orthonormal \(\{|e_i\rangle\}_{i=1}^r\) in
\(\mathcal H_E\) and set
\(|\Omega\rangle=\sum_{i=1}^r\sqrt{p_i}\,|i\rangle|e_i\rangle\); the partial
trace is \(\rho\) by direct computation. Minimality: for any pure
\(|\Omega\rangle\), the Schmidt decomposition gives marginals of equal rank
on both factors, and the rank of the \(E\)-marginal is at most
\(\dim\mathcal H_E\); so \(\dim\mathcal H_E\ge\mathrm{rank}\,\rho\).
\(\square\)

### Theorem 5.2 (Uniqueness up to record symmetry)

Let \(|\Omega_1\rangle,|\Omega_2\rangle\in\mathcal H_S\otimes\mathcal H_E\)
be purifications of the same \(\rho\). Then there is a unitary \(U_E\) on
\(\mathcal H_E\) with
\((I_S\otimes U_E)|\Omega_1\rangle=|\Omega_2\rangle\).

*Proof.* Expand \(|\Omega_k\rangle=\sum_{i=1}^{d}|i\rangle|w^{(k)}_i\rangle\)
in the eigenbasis of \(\rho\) (completed to an orthonormal basis). The
marginal condition
\(\mathrm{Tr}_E|\Omega_k\rangle\langle\Omega_k|
=\sum_{i,j}\langle w^{(k)}_j|w^{(k)}_i\rangle\,|i\rangle\langle j|=\rho\)
forces \(\langle w^{(k)}_j|w^{(k)}_i\rangle=p_i\delta_{ij}\) (with
\(p_i=0\) for \(i>r\)). Hence \(w^{(k)}_i=\sqrt{p_i}\,e^{(k)}_i\) for
orthonormal families \(\{e^{(k)}_i\}_{i\le r}\), and \(w^{(k)}_i=0\) for
\(i>r\). Define \(U_E\) by \(e^{(1)}_i\mapsto e^{(2)}_i\) on the span and
extend unitarily (the orthogonal complements have equal dimension). Then
\((I\otimes U_E)|\Omega_1\rangle=|\Omega_2\rangle\). \(\square\)

### Proposition 5.3 (The record carries exactly the missing information)

For a minimal purification, the record marginal
\(\rho_E=\mathrm{Tr}_S|\Omega\rangle\langle\Omega|\) has
\(S(\rho_E)=S(\rho_S)=-\sum_ip_i\log p_i\): the located record channel
carries entropy equal to the missing ensemble information of \(\rho\), no
more.

*Proof.* Schmidt symmetry: the two marginals of a pure bipartite state have
identical nonzero spectra. \(\square\)

So quantum theory realizes the ACP conservation axioms *tightly*: one record
system suffices (no regress), its size is the rank (finite records, matching
the record-capacity bound of
`bridges/operational_state_space_from_acp.md` §5), its entropy is exactly
the missingness (PU-3 restraint quantified), and completions are unique up
to record relabeling (Theorem 5.2). The structural resonance with
`bridges/otherness_preserving_recovery.md` is direct: the purifying system is
the legitimate asymmetric partner — it holds the ensemble sector while
remaining, by Theorem 5.2, interchangeable under symmetries that never touch
\(S\).

## 6. Reconstruction Payoff

With PU-2 in place as an ACP conservation axiom, the reconstruction route of
`bridges/hilbert_geometry_from_acp.md` §7 sharpens:

- the GPT frame is derived (`bridges/operational_state_space_from_acp.md`);
- classical simplex realizations of that frame are excluded
  (Corollary 4.2) — the fork is crossed;
- by the CDP reconstruction theorem (external input: Chiribella, D'Ariano,
  Perinotti, Phys. Rev. A 84, 012311, 2011), purification together with
  causality, perfect distinguishability, ideal compression, local
  discriminability, and atomicity of composition characterizes
  finite-dimensional quantum theory exactly.

The reconstruction table row for purification accordingly upgrades from
"ACP-plausible" to "ACP-cast, with classical exclusion proved"; the rows
still owing theorems are perfect distinguishability (sharp records), ideal
compression, local discriminability (= G3 field selection), and causality.

## 7. ACP Reading

### 7.1 Conservation, not interpretation

The purification postulate is often glossed epistemically ("mixed states
reflect ignorance"). The ACP casting is structural: persistence bookkeeping
cannot tolerate unallocated uncertainty. Either the ensemble information has
a channel, or the description is inadmissible. Classical kinematics cannot
provide the channel with finite resources (Theorem 4.1); quantum kinematics
provides it minimally (Theorems 5.1–5.3).

### 7.2 Entanglement as conservation infrastructure

Corollary 4.2 recasts entanglement: complete composite states with mixed
marginals are the *load-bearing mechanism* by which prediction structure is
conserved under subsystem cuts. This is the kinematic companion of the
tensor-product bridge's reading of entanglement as productive surplus — and
it is the same structural role boundary records play in the gravitational
program: the interior's missing information is located on the boundary
channel, not destroyed.

### 7.3 The trilemma as a drift diagnosis

The classical trilemma of §4 — dangling missingness, infinite regress, or
triviality — is a kinematic shadow of the CDT: a classical description
inside the productive interval must keep exporting its ensemble labels
outward forever (a dissolution-like flight of records), or freeze
(crystallization), or cheat (violate conservation). The quantum resolution
holds the interval open with finite records.

## 8. Relation to Existing ACP Quantum Material

- `bridges/hilbert_geometry_from_acp.md`: fills the purification row of the
  §7 table; together with the branch-homogeneity theorem it now pincers the
  quantum/classical fork from the geometry side (inner product) and the
  composition side (non-simplex completions).
- `bridges/operational_state_space_from_acp.md`: supplies the frame, the
  mixed-state existence argument (OS-3 coins), and the record-capacity bound
  matched by Theorem 5.1's minimality.
- `bridges/tensor_product_from_acp.md`: TP-4 (span generation) said
  entangled states arise as superpositions of products; Corollary 4.2 says
  some such states *must* exist for conservation — existence, not just
  admissibility.
- `bridges/restraint_power.md` and `bridges/self_limiting_universality.md`:
  PU-3's minimality is restraint applied to the record channel; the purifier
  is a KL-style legitimate controller in the sense of
  `bridges/otherness_preserving_recovery.md`.
- `bridges/quantum_gravity_derivation_program.md`: the conservation reading
  of purification is the local, kinematic form of boundary decodability —
  interior missingness located on a finite boundary record.

## 9. What This Does Not Yet Do

- **PU-2 is not derived from CDT.** The casting via restraint-power
  conservation and admissibility is an argument of fit, not a theorem. The
  hard core of OP-21's G1b now has an exact address: prove that CDT-style
  conservation for persistent record channels implies completability of
  every admissible state. Until then, purification is ACP-cast, not
  ACP-derived.
- **Non-classicality is not quantumness.** Corollary 4.2 excludes simplex
  theories; it does not select quantum theory among non-classical GPTs. The
  remaining CDP axioms (notably local discriminability = G3) are still owed.
- **The classical-composition definition is load-bearing.** Theorem 4.1
  fixes classical composition as joint distributions on product alphabets.
  Exotic non-local classical composites are not covered; the theorem should
  later be restated for arbitrary simplex-preserving composition rules.
- **Infinite dimensions are untouched** (G2), as is the gravitational
  reconnection (G4) beyond the structural analogy of §7.2.

So the actual theorems of this note are:

> in the derived GPT frame, classical record adjunction can never complete a
> mixed state (regress), so ACP conservation with finite records forces
> non-classical composites; finite-dimensional quantum theory satisfies the
> conservation axioms exactly, with minimal record dimension equal to rank,
> record entropy equal to missing information, and completions unique up to
> record symmetry.

## 10. Open Direction

1. **Derive PU-2 from CDT.** Candidate route: model the discarded coin of
   OS-3 as a physical record channel inside a closed mechanism-preserving
   composite (Stinespring direction), and show that CDT conservation for the
   closed system forces an extremal joint description at some finite cut.
2. **Sharp records lemma** (shared with
   `bridges/operational_state_space_from_acp.md` §10): perfect
   distinguishability from asymptotic repetition.
3. **Local discriminability as ACP boundary decodability** (G3 / HG-C1):
   the last structural axiom separating complex quantum theory from its
   real and quaternionic siblings.
4. **Gravitational lift:** restate PU-2 for the relational macrostate kernel
   — interior mixedness located on boundary records — and compare with the
   quantum-completion policy in `simulations/cosmic_coordination_floor/`.
