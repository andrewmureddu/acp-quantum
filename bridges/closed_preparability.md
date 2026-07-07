# Closed Preparability: PU-2 from Mechanism-Preserving Closure

*Status: exploratory bridge note; the reduction theorem (closed preparability
implies record locatability), the pure-product lemma, the classical violation
theorem, and the quantum verification are **proved**. The note discharges the
purification bridge's central axiom PU-2 as a *theorem*, at the cost of a new
axiom CL-1 (closed preparability) — but the trade is not circular bookkeeping:
CL-1 is a dynamical closure axiom, the preparation-facing sibling of the
reversibility axiom UE-1 that the kinematics quartet already uses, and it
lives where CDT-style conservation actually operates. The residue of OP-21's
"derive PU-2 from CDT" is thereby relocated from state-space kinematics to a
single dynamical principle, and the quantum/classical fork acquires a
dynamical form: classical theories provably violate CL-1.*

## 1. Thesis

`bridges/purification_from_acp.md` rested on PU-2: every admissible state has
a completion — an extremal state of a finite composite with the given state
as marginal. PU-2 was flagged as ACP-cast rather than ACP-derived. This note
derives it.

The observation driving the reduction: PU-2 quantifies over *states that
exist*, but conservation principles constrain *processes*. So translate. A
state does not simply exist; it is prepared (OS-1/OS-2: states are
equivalence classes of preparation procedures). The ACP conservation
statement about preparations is:

> **Closed preparability (CL-1).** Every admissible preparation is, at some
> finite cut, closed: it is realized by a mechanism-preserving (reversible)
> transformation of a finite composite initialized in a complete reference
> state, followed by discarding the non-system part.

From CL-1, record locatability is a two-line theorem, because reversible
transformations provably preserve completeness. The apparent irreversibility
of preparation (mixing, discarding, noise) is then *literally* tracing over a
record channel — not as an interpretive gloss but as the defining property of
an admissible preparation.

The fork of the purification bridge then reappears in dynamical form,
provably:

- **classical theories violate CL-1** — the reversible transformations of a
  simplex are exactly the alphabet permutations, so nothing mixed is ever
  closed-preparable at a classical cut (the dynamical face of the classical
  regress);
- **quantum theory satisfies CL-1 minimally** — one unitary on a record
  system of dimension equal to the target rank.

## 2. Setup

Work in the GPT frame of `bridges/operational_state_space_from_acp.md`:
systems \((V,C,u)\) with compact convex state spaces \(K\), effects
separating states. Additionally:

- A **transformation** from system \(A\) to system \(B\) is an affine map
  \(K_A\to K_B\). A **reversible (mechanism-preserving) transformation** of
  \(A\) is an affine bijection \(R:K_A\to K_A\) whose inverse is affine.
  These are the operational mechanism symmetries — the same class HG-3 and
  UE-1 quantify over.
- **Composites** \(AB\) carry product states \(\omega\otimes\varphi\),
  product effects \(a\otimes b\) with
  \((a\otimes b)(\omega\otimes\varphi)=a(\omega)\,b(\varphi)\),
  marginalization \(\mathrm{tr}_B=(\,\cdot\,\otimes u_B)\), and
  **conditional states**: for an effect \(a\) on \(A\) and
  \(\sigma\in K_{AB}\) there are \(\mu=(a\otimes u_B)(\sigma)\in[0,1]\) and,
  when \(\mu>0\), a state \(\sigma_{B|a}\in K_B\) with
  \((a\otimes b)(\sigma)=\mu\,b(\sigma_{B|a})\) for all effects \(b\).
- **LT-0 (product-effect separation):** product effects separate composite
  states: if \((a\otimes b)(\sigma)=(a\otimes b)(\tau)\) for all \(a,b\),
  then \(\sigma=\tau\). This is implied by (and weaker than) local
  tomography; its ACP reading is local decodability of composite records,
  the same principle designated as the G3 selector in
  `bridges/hilbert_geometry_from_acp.md` §6.

**Complete** = extreme in \(K\), as in the purification bridge. Note that
complete states always *exist* mathematically: a nonempty compact convex set
in finite dimension is the convex hull of its extreme points (Minkowski).
What is operational is their preparability:

### Axiom CL-2 (Blank initialization)

Each system can be initialized in at least one complete state.

Interpretation: a blank record — a fully resolved reference configuration —
is an admissible starting point. Without it, no description could ever begin
from a state with nothing missing, and "missing information" would have no
zero point.

### Axiom CL-1 (Closed preparability)

For every admissible state \(\omega\in K_S\) there exist a finite system
\(E\), a complete state \(\varphi\in K_{SE}\), and a reversible
transformation \(R\) of \(SE\) such that

$$
\omega=\mathrm{tr}_E\,R(\varphi).
$$

Interpretation: at some finite cut, the preparation of \(\omega\) is a closed
mechanism-preserving process. Restraint-power conservation says
mechanism-preserving dynamics relocate prediction structure without
destroying it; reality-reflective admissibility says an admissible
description cannot invoke an unaccountable external mechanism at every cut.
CL-1 is the conjunction: whatever non-reversible appearance a preparation has
(noise, mixing, discarding the OS-3 coin) is attributable to the discarded
factor \(E\), not to a fundamental loss. It is the preparation-facing sibling
of UE-1 (`bridges/unitary_evolution_from_acp.md`), which posits exactly this
reversibility for *evolution* between records.

⚠ CL-1 is an axiom, not a CDT theorem. The claim of this note is a genuine
*factoring*, not a dissolution: PU-2 (kinematic existence of completions)
reduces to CL-1 (dynamical closure of preparations) plus provable lemmas, and
the remaining gap to CDT proper is sharply localized: derive "fundamental
closed dynamics are mechanism-preserving" — the ACP analog of unitarity —
once, for the whole program, rather than separately for evolution (UE-1) and
preparation (CL-1).

## 3. Lemmas

### Lemma 3.1 (Reversible transformations preserve completeness)

If \(R:K\to K\) is an affine bijection with affine inverse and \(\omega\) is
extreme, then \(R(\omega)\) is extreme.

*Proof.* Suppose \(R(\omega)=\lambda\sigma+(1-\lambda)\tau\) with
\(\lambda\in(0,1)\), \(\sigma,\tau\in K\). Applying the affine \(R^{-1}\):
\(\omega=\lambda R^{-1}(\sigma)+(1-\lambda)R^{-1}(\tau)\). Extremality of
\(\omega\) gives \(R^{-1}(\sigma)=R^{-1}(\tau)=\omega\), hence
\(\sigma=\tau=R(\omega)\). \(\square\)

This is the operational content of "mechanism-preserving dynamics cannot
create missingness": completeness is a *dynamical invariant* of the
reversible class, by convexity alone.

### Lemma 3.2 (Pure products are pure)

Under LT-0 and conditional states, if \(\omega_A\in K_A\) and
\(\omega_B\in K_B\) are extreme, then \(\omega_A\otimes\omega_B\) is extreme
in \(K_{AB}\).

*Proof.* Suppose
\(\omega_A\otimes\omega_B=\lambda\sigma+(1-\lambda)\tau\),
\(\lambda\in(0,1)\).

*Marginals.* For every effect \(a\):
\(a(\omega_A)=(a\otimes u_B)(\omega_A\otimes\omega_B)
=\lambda\,a(\sigma_A)+(1-\lambda)\,a(\tau_A)\), so
\(\omega_A=\lambda\sigma_A+(1-\lambda)\tau_A\) (effects separate states),
and extremality forces \(\sigma_A=\tau_A=\omega_A\); similarly for \(B\).

*Conditionals.* Fix an effect \(a\) with \(a(\omega_A)>0\). Then
\((a\otimes u_B)(\sigma)=a(\sigma_A)=a(\omega_A)>0\), so the conditional
state \(\sigma_{B|a}\) exists, and for every effect \(b\):

$$
a(\omega_A)\,b(\omega_B)
=(a\otimes b)(\omega_A\otimes\omega_B)
=\lambda\,a(\omega_A)\,b(\sigma_{B|a})
+(1-\lambda)\,a(\omega_A)\,b(\tau_{B|a}).
$$

Dividing by \(a(\omega_A)\) and using separation on \(B\):
\(\omega_B=\lambda\,\sigma_{B|a}+(1-\lambda)\,\tau_{B|a}\), so extremality
gives \(\sigma_{B|a}=\omega_B\). Hence
\((a\otimes b)(\sigma)=a(\omega_A)\,b(\omega_B)\) for all \(b\) and all
\(a\) with \(a(\omega_A)>0\). For \(a\) with \(a(\omega_A)=0\):
\(0\le(a\otimes b)(\sigma)\le(a\otimes u_B)(\sigma)=a(\omega_A)=0\), so both
sides vanish. Therefore
\((a\otimes b)(\sigma)=(a\otimes b)(\omega_A\otimes\omega_B)\) for all
product effects, and LT-0 gives \(\sigma=\omega_A\otimes\omega_B\); likewise
\(\tau\). \(\square\)

## 4. Main Theorem

### Theorem 4.1 (Closed preparability implies record locatability)

Under CL-1, every admissible state \(\omega\in K_S\) has a completion; that
is, PU-2 of `bridges/purification_from_acp.md` holds.

*Proof.* Take \(E\), complete \(\varphi\in K_{SE}\), and reversible \(R\)
from CL-1. Set \(\Omega:=R(\varphi)\). By Lemma 3.1, \(\Omega\) is complete;
by CL-1, \(\mathrm{tr}_E\,\Omega=\omega\). \((E,\Omega)\) is a completion.
\(\square\)

### Corollary 4.2 (Blank-product form)

Under CL-2 and LT-0, the reference state in CL-1 may be taken to be a blank
product \(\varphi_S\otimes\varphi_E\) of complete local states: by
Lemma 3.2 such a product is complete, so any preparation realized as a
reversible transformation of blank-initialized system and record satisfies
CL-1 and hence yields a completion.

This is the operational picture: *initialize blanks, run a closed mechanism,
discard the record side* — every admissible preparation, with completeness
conserved throughout and mixedness appearing only at the final trace.

### Remark 4.3 (The factoring is tight)

Conversely, PU-2 implies CL-1 whenever the reversible transformations of the
composite act transitively on its complete states (take \(R\) carrying the
blank reference to the completion \(\Omega\)). Transitivity on complete
states is precisely composite branch homogeneity — HG-3 of
`bridges/hilbert_geometry_from_acp.md` at the level of \(K_{SE}\)'s extreme
points. So the exact relation is:

$$
\text{PU-2}
\;=\;
\text{CL-1}
\quad\text{modulo composite branch homogeneity.}
$$

The two derivation tracks (geometry via HG-3, conservation via CL-1) are
therefore not parallel but interlocking: homogeneity converts between the
kinematic and dynamical forms of conservation.

## 5. The Dynamical Fork

### Theorem 5.1 (Classical theories violate CL-1)

Let \(S\) and all record systems be classical (simplex state spaces,
classical composition as in `bridges/purification_from_acp.md` §4). Then the
closed-preparable states of \(S\) are exactly the pure states: no mixed
classical state satisfies CL-1 at any finite classical cut.

*Proof.* First, the reversible transformations of a classical system are the
alphabet permutations: an affine bijection \(R\) of a simplex \(\Delta\)
with affine inverse maps extreme points bijectively onto extreme points
(Lemma 3.1 applied to \(R\) and \(R^{-1}\)), i.e., permutes the vertices;
and an affine map on a simplex is determined by its vertex values, so \(R\)
is the affine extension of that permutation.

Now let \(\varphi\) be a complete state of the classical composite
\(SE_1\cdots E_k\): a point mass. A permutation of the composite alphabet
maps it to a point mass; the marginal of a point mass is a point mass:
pure. So \(\mathrm{tr}_{E}R(\varphi)\) is pure for every classical cut,
every blank reference, every reversible \(R\). \(\square\)

This is the dynamical face of the classical-regress theorem: kinematically,
classical extensions never complete a mixed state; dynamically, closed
classical mechanisms never *produce* one. Classical mixedness cannot be
manufactured by any closed classical process — it must be injected from
outside the description, which is exactly the unaccountable external
mechanism that admissibility rejects. A theory with mixed states inside the
productive interval must therefore have non-classical closed dynamics.

### Proposition 5.2 (Quantum theory satisfies CL-1 minimally)

For any density operator \(\rho\) on \(\mathcal H_S\) with
\(r=\mathrm{rank}\,\rho\): take \(\dim\mathcal H_E=r\), blanks
\(|0\rangle_S,|0\rangle_E\), and any unitary \(U\) on
\(\mathcal H_S\otimes\mathcal H_E\) with
\(U|0\rangle_S|0\rangle_E=|\Omega_\rho\rangle\), a purification of \(\rho\)
(Theorem 5.1 of `bridges/purification_from_acp.md`); such \(U\) exists by
orthonormal extension. Then
\(\mathrm{Tr}_E\,U(|00\rangle\langle00|)U^\dagger=\rho\). The record size
\(r\) is minimal by the same theorem. \(\square\)

So the fork is now stated twice over, once kinematically (regress /
exclusion) and once dynamically (CL-1 violation / minimal satisfaction), and
the two statements are linked by Remark 4.3.

## 6. What Happened to the OS-3 Coin

`bridges/operational_state_space_from_acp.md` derived convexity from
non-disturbing classical coins with the coin record discarded. Under CL-1
the coin is part of \(E\) — but Theorem 5.1 says a *classical* coin alone
cannot close the preparation of the resulting mixed state. The resolution is
not that the coin model was wrong; it is that the coin, its correlations
with \(S\), and whatever mechanism set the coin must jointly admit a
non-classical closed description at some larger cut. The OS-3 coin is a
legitimate *interface*; CL-1 concerns the *closure* behind it. This also
sharpens the OS-3 open item (deriving non-disturbance): in a CL-1 theory the
coin's non-disturbance should follow from the closed mechanism's
product-preserving structure, which is a concrete lemma target.

## 7. ACP Reading

### 7.1 Conservation as closure, not as inventory

The purification bridge phrased conservation as an inventory constraint
(missing information must be located somewhere). This note phrases it as a
closure constraint (preparations must be closed at some cut). The inventory
form quantifies over states and invites the question "why should such a
state exist?"; the closure form quantifies over processes and inherits its
force from the same source as UE-1: mechanism-preserving dynamics as the
fundamental class. One conservation principle, two shadows — and
Lemma 3.1 is the hinge, making completeness an invariant of the
mechanism-preserving class by convex geometry alone.

### 7.2 The unitarity analog, isolated

The program's remaining conservation import is now exactly one statement:
*fundamental closed dynamics are reversible* (UE-1 for evolution, CL-1 for
preparation, plausibly one axiom at the level of the theory's process
category). Deriving it from CDT — presumably from the requirement that
persistent boundary laws admit no unaccountable one-way loss at every finite
cut — is the single hard residue, and it now sits at a well-defined address
shared by two bridges instead of being diffused across kinematic postulates.

## 8. Relation to Existing ACP Quantum Material

- `bridges/purification_from_acp.md`: PU-2 upgraded from ACP-cast axiom to
  theorem-given-CL-1 (Theorem 4.1); PU-3's uniqueness is, per Remark 4.3,
  fiber-wise composite branch homogeneity — connecting it to HG-3 rather
  than leaving it free-standing.
- `bridges/unitary_evolution_from_acp.md`: CL-1 aligns preparation with
  UE-1's reversible evolution; the two should eventually be one axiom about
  the process category.
- `bridges/hilbert_geometry_from_acp.md`: Remark 4.3 interlocks the
  homogeneity and conservation tracks; LT-0 is the G3 selector doing double
  duty here.
- `bridges/operational_state_space_from_acp.md`: §6 relocates the OS-3
  non-disturbance question inside the closed-mechanism picture.
- `bridges/quantum_gravity_derivation_program.md`: CL-1 is the local form of
  the program's global demand that gravitational collapse admit a
  mechanism-changing but conservation-respecting completion — preparation of
  the post-collapse state must be closed at the boundary-record cut.

## 9. What This Does Not Yet Do

- **CL-1 is not derived from CDT.** The reduction relocates and unifies the
  gap (one reversibility axiom for the whole program) but does not close it.
- **LT-0 is assumed** for the blank-product form (Corollary 4.2) and is
  itself the open G3 item; the abstract form (Theorem 4.1) does not need it.
- **Uniqueness (PU-3) is not derived**; Remark 4.3 reduces it to composite
  branch homogeneity on fixed-marginal fibers, stated here as Conjecture
  CP-C1: *in any GPT satisfying CL-1 whose reversible transformations act
  transitively on complete states of each composite, completions of a given
  state on a minimal record system are unique up to reversible record
  symmetry.* Open.
- **Finite dimension throughout** (G2 untouched).

So the actual theorems of this note are:

> reversible transformations preserve completeness; pure products are pure
> under product-effect separation; hence closed preparability implies record
> locatability (PU-2), with the blank-product operational form; classical
> theories provably violate closed preparability (their reversible dynamics
> are permutations), while quantum theory satisfies it with records of
> minimal size equal to the rank.

## 10. Open Direction

1. **The reversibility residue.** Derive the single closure axiom
   (UE-1 ∧ CL-1) from CDT: persistent boundary laws admit no unaccountable
   one-way loss at any finite cut. This is now the sole conservation import
   of the foundations program.
2. **Conjecture CP-C1** (uniqueness from fiber homogeneity), unifying PU-3
   with HG-3.
3. **Non-disturbance of the OS-3 coin** as a lemma about product-preserving
   closed mechanisms (§6).
4. **Local decodability (LT-0 / G3)**: the last structural axiom, now used
   by two bridges, still owed its ACP derivation — and it is the axiom that
   selects the complex field.
