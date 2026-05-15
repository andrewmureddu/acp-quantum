# The Algebraic Structure of Persistence: Formalizing the Schur Complement Bridge

*Connecting the Thermodynamic and Algebraic Programs*

Working Draft — April 2026

---

## 1. Purpose

This document formalizes the connection between two companion papers:

- **A General Theory of Persistence** (the ACP paper): derives the Anti-Crystallization Principle and Crystallization Drift Theorem from thermodynamic first principles, using conditional macrostate entropy H(m′|m) as the central quantity.

- **A Pattern Hiding in Plain Sight** (the algebraic paper): identifies the Schur complement as the universal algebraic operation implementing the persistence threshold across eight independent research programs, using the capacity ≥ complexity inequality as the central condition.

The claim: these are not merely compatible descriptions of the same phenomenon. They are *the same mathematical statement*, expressed in different coordinates. Specifically:

1. The ACP's productive interval (0 < H(m′|m) < H_max) is the regime where the Schur complement of the system's internal block is well-defined and non-degenerate.

2. Crystallization drift is progressive rank reduction of the internal block D.

3. The capacity ≥ complexity threshold of the algebraic paper is the ACP's persistence condition, stated in the language of effective boundary theory.

4. Anti-crystallization mechanisms are operations that restore the rank/condition number of D.

Formalizing these identifications closes the loop between the papers and establishes them as a single argument in two registers.

---

## 2. Setup: The Block Decomposition of Persistent Systems

### 2.1 The Partition

Consider a system S = (Ω, σ, T, μ) in the ACP framework. At any time t, the system's macrostate space M admits a natural partition into two classes:

**Boundary variables (B):** Macrostate components that mediate the system's interaction with its environment — the degrees of freedom visible from outside. These determine how the system couples to external perturbation and energy/entropy flows.

**Internal variables (I):** Macrostate components that are screened from the environment by the boundary — the degrees of freedom that constitute the system's "interior." These are the variables eliminated when computing effective boundary behavior.

This partition is not arbitrary. It is determined by the coarse-graining map σ and the environment-system coupling (Axiom 3 of the ACP). The boundary variables are those whose conditional distributions are directly modified by environmental interactions; the internal variables are conditionally independent of the environment given the boundary.

***Definition 2.1 (Block structure).*** For a system with macrostate transition kernel P(m′|m), define the joint precision matrix Q of the (boundary, internal) decomposition:

$$Q = \begin{pmatrix} A & B \\ B^T & D \end{pmatrix}$$

where A is the boundary-boundary precision block, D is the internal-internal precision block, and B is the boundary-internal coupling. The effective boundary dynamics is the Schur complement:

$$Q_{\text{eff}} = Q/D = A - B D^{-1} B^T$$

This is exact for Gaussian systems. For non-Gaussian systems, Q represents the quadratic (Gaussian) approximation to the full transition kernel, and the Schur complement provides the leading-order effective theory.

*Remark 2.2.* The partition into boundary and internal variables is precisely the structure formalized categorically by Stein, Zanasi, Piedeleu, and Samuelson (2025): an open system is a morphism in QuadRel with input (boundary-in) and output (boundary-out) interfaces, and composition — sequential coupling of open systems — is Schur complementation of the internal block. The ACP's system-environment coupling is categorical composition.

---

## 3. The Four Identifications

### 3.1 First Identification: The Productive Interval is Non-Degenerate D

***Theorem 3.1 (Persistence ⟺ Non-Degenerate Internal Block).*** A system S exhibits future-bearing dynamics (Definition 2.5 of the ACP) if and only if the internal block D of its macrostate precision matrix satisfies:

(a) D is invertible (det(D) ≠ 0), and

(b) The condition number κ(D) is finite but bounded away from 1.

*Proof sketch.*

**Crystallization boundary (D singular):** If D is singular, the Schur complement Q/D is undefined (in the standard sense) or requires the pseudoinverse D⁺ with an additional support constraint (Remark 3.2 of the algebraic paper). Physically: some internal degrees of freedom have collapsed. The system has fewer independent internal states than its boundary structure requires. The macrostate transition is deterministic along the degenerate directions of D — precisely the condition H(m′|m) → 0 for those components. When rank(D) = 0, all internal degrees of freedom have collapsed, and the system has become its own boundary with no interior. This is total crystallization.

**Dissolution boundary (D maximally dispersed):** If D is proportional to the identity (D = σ²I), the internal degrees of freedom are uncorrelated and maximally entropic. The Schur complement Q/D = A − (1/σ²)BB^T approaches A as σ² → ∞ — the internal structure contributes nothing to boundary behavior. The system has lost coherent internal organization. This is dissolution: the internal block exists but carries no information. H(m′|m) → H_max.

**Productive interval:** D is invertible, well-conditioned, and non-trivial. The Schur complement is well-defined, the effective boundary theory captures genuine internal structure, and the system has both interior and boundary — the hallmark of future-bearing dynamics. ■

*Remark 3.2 (The two degeneracies).* The productive interval is bounded by two qualitatively different degeneracies of D:

| | Crystallization | Dissolution |
|---|---|---|
| **D** | rank-deficient → singular | ∝ identity → trivially invertible |
| **det(D)** | → 0 | → ∞ (or maximal) |
| **κ(D)** | → ∞ | → 1 |
| **Schur complement** | undefined | trivial (≈ A) |
| **H(m′\|m)** | → 0 | → H_max |
| **Interior** | collapsed | structureless |
| **Physical meaning** | system is all boundary | boundary has no system behind it |

This is the table that shows the ACP and the Schur complement program describe the same phenomenon from different vantage points: one tracks conditional entropy, the other tracks block structure. They are translations of each other.

### 3.2 Second Identification: Crystallization Drift is Rank Reduction of D

***Theorem 3.3 (Drift = Rank Reduction).*** Under the conditions of the Crystallization Drift Theorem (Theorem 4.17 of the ACP), the rank of the internal block D is monotonically non-increasing in t.

*Proof sketch.*

Each self-reinforcing mechanism Rᵢ corresponds to a constraint on the internal degrees of freedom — a direction in the internal state space along which the transition distribution is concentrated. By Lemma 4.13 (self-reinforcement reduces conditional entropy), activation of Rᵢ concentrates the transition kernel along a subspace. In precision coordinates, this concentration adds a rank-1 (or low-rank) positive semidefinite term to the precision along the constrained direction, but the *effective* dimensionality of D — the number of directions along which the system retains non-trivial stochastic dynamics — decreases.

More precisely: the compound reinforcement basin R̅(t) = R₁ ∩ ⋯ ∩ Rₖ constrains the system to a submanifold of M. The restriction of D to this submanifold has rank equal to dim(R̅(t)). By Theorem 4.17(c), R̅(t) is monotonically non-increasing in the set-inclusion sense, so dim(R̅(t)) is non-increasing. Therefore the effective rank of D is non-increasing.

The superadditive compounding (Lemma 4.15) corresponds to the Schur complement propagation identified in Appendix A.9: each new mechanism's constraint interacts with existing constraints through the off-diagonal blocks, creating indirect couplings (D acquires off-diagonal structure that accelerates rank reduction beyond what independent constraints would produce). The superadditive excess — the interaction information — is the additional rank reduction attributable to these indirect couplings.

The self-grounding property (Coherent Steering derived from stable coexistence) has a clean algebraic interpretation: anti-coherent mechanisms are those whose constraints conflict — they try to collapse D along incompatible directions. The channel erosion argument (Appendix A.10) shows that such conflicts resolve by shedding the weaker mechanism. The surviving mechanisms are *coherent* — their constraints are compatible — meaning they reduce rank along a consistent subspace. This is why crystallization is progressive and monotonic rather than oscillatory. ■

***Corollary 3.4 (Crystallization as boundary-without-interior).*** In the limit of complete crystallization (H(m′|m) → 0), rank(D) → 0 and the system's macrostate transition matrix has no internal block. The Schur complement is undefined because there is nothing left to eliminate. The system has become its own boundary — its future is entirely determined by its present configuration, with no hidden degrees of freedom mediating the transition. This is the algebraic content of the sentence: "the system has become its own boundary, with no interior."

### 3.3 Third Identification: Capacity ≥ Complexity is the Persistence Condition

The algebraic paper states the persistence threshold as: a system persists if and only if its information-processing capacity meets or exceeds the rate at which complexity threatens to overwhelm it. We now show this is the ACP's persistence condition in different coordinates.

***Definition 3.5 (Information-processing capacity).*** The information-processing capacity of a system S at time t is:

$$C(t) = \text{rank}(D(t)) \cdot \bar{h}(D(t))$$

where rank(D(t)) is the effective rank (number of non-degenerate internal degrees of freedom) and h̄(D(t)) is the mean per-direction conditional entropy — the average information content per surviving internal degree of freedom. This is the system's total capacity to generate distinguishable internal states.

***Definition 3.6 (Complexity load).*** The complexity load on system S at time t is the rate of conditional entropy reduction driven by the active self-reinforcing mechanisms:

$$L(t) = -\frac{dH(m'|m)}{dt}\bigg|_{\text{self-reinforcement}}$$

By the Crystallization Drift Theorem, L(t) ≥ 0 whenever self-reinforcing mechanisms are active, and the superadditive compounding guarantees L(t) accelerates as mechanisms accumulate.

***Theorem 3.7 (Equivalence of persistence conditions).*** The following are equivalent:

(i) The system exhibits future-bearing dynamics (ACP, Definition 2.5).

(ii) 0 < H(m′|m) < H_max (ACP, Theorem 4.3).

(iii) The internal block D is invertible and non-trivial (Theorem 3.1 above).

(iv) The system's capacity to generate new internal states exceeds the rate at which self-reinforcing mechanisms eliminate them: C(t) > L(t) · τ_v, where τ_v is the verification latency.

*Proof sketch.*

(i) ⟺ (ii) is Theorem 4.3 of the ACP.

(ii) ⟺ (iii) is Theorem 3.1 above.

For (ii) ⟺ (iv): The conditional entropy H(m′|m) is the integral of the per-direction entropies over the non-degenerate directions of D:

$$H(m'|m) = \sum_{i=1}^{\text{rank}(D)} h_i(D)$$

The capacity C(t) = rank(D) · h̄(D) = H(m′|m) (by definition). The complexity load L(t) is the rate at which H decreases. The system persists as long as H(m′|m) > 0, which requires that the remaining capacity exceeds the accumulated load over the verification timescale:

$$H(m'|m) > L(t) \cdot \tau_v$$

Rearranging: C(t) > L(t) · τ_v. This is the capacity ≥ complexity condition, stated in the ACP's variables. ■

*Remark 3.8 (Domain instantiations).* Each domain-specific persistence threshold identified in the algebraic paper is now a special case of (iv):

| Domain | Capacity C | Complexity load L | Threshold |
|--------|-----------|-------------------|-----------|
| Shannon | Channel capacity C | Transmission rate R | C ≥ R |
| Ashby | V(controller) | V(system) | V(ctrl) ≥ V(sys) |
| Prigogine | Entropy export rate | Entropy production rate | Export ≥ production |
| QEC | Error correction rate | Error generation rate | Correction ≥ generation |
| ACP | rank(D) · h̄(D) | −dH/dt from drift | H > L · τ_v |

The Schur complement is the algebraic operation that *computes* C from the full system specification — it eliminates the internal block D and reveals what effective capacity remains at the boundary.

### 3.4 Fourth Identification: Anti-Crystallization is Rank Restoration

***Theorem 3.9 (Anti-crystallization = rank restoration of D).*** The anti-crystallization mechanisms identified in the ACP (Section 4.4.5) — external perturbation exceeding ε*(t), coherence crises inducing phase transitions, and deliberate self-disruption — all operate by restoring rank to the internal block D.

*Proof sketch.*

(a) **External perturbation:** A perturbation of magnitude > ε*(t) disrupts one or more self-reinforcing mechanisms, releasing the corresponding constraints on D. This restores the degenerate directions, increasing rank(D) and re-opening the Schur complement to non-trivial internal structure.

(b) **Coherence crisis:** When R̅ = ∅ (the compound reinforcement basin is empty), the system's constraints are mutually incompatible. Algebraically, the constraints try to collapse D along incompatible directions, creating contradictory rank-1 projections. The system resolves this by shedding mechanisms — a phase transition that releases constraints and restores rank.

(c) **Deliberate self-disruption:** Active mechanisms that introduce controlled noise into the internal block (e.g., exploratory behavior, genetic recombination, institutional reform) prevent the eigenvalues of D from reaching zero. They maintain a floor on the smallest eigenvalue of D, ensuring invertibility.

In all three cases, the operation is the same: restore eigenvalues of D that have been driven toward zero by crystallization drift. This is the algebraic content of the ACP's assertion that anti-crystallization is "time renewal" (Proposition 8.4): restoring rank to D reopens the internal degrees of freedom, enabling new macrostate transitions — which is what operational time *is*. ■

---

## 4. The Unified Picture

### 4.1 One Theorem, Two Registers

The ACP and the algebraic program are now revealed as the same theorem in two registers:

**Thermodynamic register (ACP):**
- State variable: H(m′|m) (conditional macrostate entropy)
- Persistence condition: 0 < H < H_max
- Drift: dH/dt ≤ 0 (Crystallization Drift Theorem)
- Boundaries: H → 0 (crystallization), H → H_max (dissolution)
- Renewal: mechanisms that increase H

**Algebraic register (Schur complement):**
- State variable: D (internal precision block)
- Persistence condition: D invertible and non-trivial
- Drift: rank(D) non-increasing (rank reduction)
- Boundaries: det(D) → 0 (crystallization), D → σ²I (dissolution)
- Renewal: operations that restore rank/eigenvalues of D

**Categorical register (QuadRel):**
- State variable: morphism f : m → n in QuadRel
- Persistence condition: composition g ∘ f well-defined (D invertible at interface)
- Drift: sequential composition progressively eliminates internal interface
- Boundaries: composition fails (singular D) or becomes trivial (structureless D)
- Renewal: morphisms that re-enrich the internal interface

The translation dictionary:

| ACP concept | Algebraic concept | Categorical concept |
|-------------|------------------|-------------------|
| Conditional entropy H(m′\|m) | rank(D) · h̄(D) | informational content of internal interface |
| Self-reinforcing mechanism | rank-1 constraint on D | endomorphism that projects internal wires |
| Superadditive compounding | Schur complement propagation | composition creating indirect couplings |
| Interaction information | additional rank reduction from off-diagonal blocks | information generated by composition |
| Coherent Steering | compatible constraint directions | composable projections |
| Channel erosion | incompatible constraints resolving via rank selection | non-composable morphisms being shed |
| Crystallization | D singular | internal interface collapsed |
| Dissolution | D trivial (∝ I) | internal interface structureless |
| Anti-crystallization | rank restoration of D | morphisms that re-open internal interface |
| Operational time | # of rank-preserving transitions | # of non-trivial compositions |
| Verification loop | Predict (from Q/D) → Verify → Update D → Re-predict | Compose → Observe → Update → Re-compose |

### 4.2 What This Unification Accomplishes

**For the ACP paper:** The Schur complement formalization (previously an open problem, Remark 4.22) is resolved. The heuristic claim that "crystallization is D approaching singularity" is now a theorem. The connection to the categorical program is exact, not analogical.

**For the algebraic paper:** The capacity ≥ complexity condition, previously stated as a convergent observation across eight domains, is now *derived* from thermodynamic first principles via the ACP. The Schur complement's universality is explained: it is universal because it computes the effective theory of a system whose persistence is governed by the CDT. The question "why does the same algebraic operation appear everywhere?" has an answer: because every persistent system has internal and boundary structure, and the physics of persistence (the ACP) governs the relationship between them.

**For both papers jointly:** They are no longer siblings — they are a single argument. The ACP provides the physics (why persistence requires the productive interval). The Schur complement provides the algebra (how the productive interval is computed). The categorical framework provides the syntax (what composition means for open systems). The drift theorem provides the dynamics (how the productive interval erodes). Together they constitute a complete theory: physics + algebra + dynamics + syntax.

---

## 5. The Understanding-Complexity Relationship as the Viable Band

### 5.1 Reformulation

The algebraic paper's central claim can be restated in the ACP's language with new precision:

**Original (algebraic paper):** A system persists if and only if its information-processing capacity grows at least as fast as its complexity load.

**Reformulated (unified):** A system exhibits future-bearing dynamics if and only if the rate of internal state generation (rank-preserving dynamics of D) exceeds the rate of internal state elimination (rank reduction from crystallization drift):

$$\frac{d}{dt}\text{rank}_{\text{eff}}(D)\bigg|_{\text{renewal}} > \frac{d}{dt}\text{rank}_{\text{eff}}(D)\bigg|_{\text{drift}}$$

where the left side is the anti-crystallization contribution and the right side is the crystallization drift contribution.

This is *exactly* the viable band of persistence. The system persists in the region where renewal outpaces drift. The boundaries are:

- **Crystallization (right boundary):** drift > renewal. D loses rank faster than it gains it. H(m′|m) → 0. The system rigidifies.

- **Dissolution (left boundary):** neither drift nor renewal is coherent. D becomes structureless. H(m′|m) → H_max. The system dissipates.

- **Productive interval (the band):** renewal ≥ drift, with both active. D maintains rank while evolving. H(m′|m) stays in (0, H_max). The system persists.

### 5.2 The Capacity-Complexity Inequality as a Rate Condition

The key insight is that the capacity ≥ complexity condition is not a *static* inequality but a *rate* condition. It's not that the system must have more capacity than complexity at any instant — it's that the rate of capacity generation must match or exceed the rate of capacity consumption by crystallization drift.

This resolves a longstanding puzzle in the algebraic paper: why is the threshold sharp? Why isn't there a gradual degradation? The answer comes from the CDT: crystallization drift is *accelerating* (Theorem 4.17(c), superadditive compounding). Once the system falls behind — once drift exceeds renewal even slightly — the gap widens monotonically. There is no recovery without an external perturbation or phase transition. This is the algebraic content of the CDT's self-grounding property: the drift accelerates because the mechanisms driving it are coherent (Coherent Steering), and they are coherent because non-coherent mechanisms have been shed (channel erosion). The threshold is sharp because the dynamics above and below it are qualitatively different: above the threshold, the system can maintain D; below it, D collapses irreversibly.

### 5.3 Domain Instantiations Revisited

With the unified framework, each domain's persistence threshold can be stated as a rate condition on D:

**Shannon:** The channel's internal noise matrix D evolves under coding. The channel capacity C = max I(X;Y) is the maximum rate at which the encoder can maintain rank in the effective channel matrix against the noise's tendency to degrade it. R > C means the encoder cannot keep up; the message degrades — crystallization of the channel.

**Prigogine:** The dissipative structure's internal degrees of freedom (chemical concentrations, velocity fields) form D. Entropy export maintains D's rank by flushing entropy to the environment. When entropy export < entropy production, D degenerates — the structure collapses to equilibrium (dissolution) or locks into a rigid pattern (crystallization, e.g., Bénard cells freezing into a single convection pattern).

**Kauffman:** The Boolean network's unfrozen component is D. Selection pressure drives frozen component expansion (rank reduction of D). The edge of chaos is the regime where D has intermediate rank — enough unfrozen variables for computation, not so many that dynamics are chaotic.

**Friston:** The agent's internal model precision matrix is D. Prediction errors drive D toward overfitting (excessive precision on experienced states, zero precision on unexperienced ones — crystallization). Active inference maintains D's rank by seeking novel observations — the exploratory drive is anti-crystallization, algebraically expressed as rank restoration of D.

**Zurek:** The quantum system's off-diagonal density matrix elements are D. Decoherence drives D toward diagonality (rank reduction of the off-diagonal block). Quantum Darwinism selects the pointer states that survive — the states for which D's diagonal structure is maximally redundantly encoded in the environment. The classical world emerges when D has fully collapsed; quantum coherence persists where D retains rank.

---

## 6. Open Problems

### 6.1 Non-Gaussian Extension

The identification Theorem 3.1 is exact for Gaussian systems (where the precision matrix fully characterizes the transition kernel) and leading-order for non-Gaussian systems. The full non-Gaussian bridge requires showing that the rank reduction of D — defined for the Gaussian approximation — tracks the true conditional entropy reduction H(m′|m) with controlled error. Appendix A.17 of the ACP paper provides the necessary bounds: non-Gaussian corrections to the interaction information are generically positive (Corollary A.17.15), meaning the Gaussian rank reduction is a *conservative* estimate of the true drift. The formal statement: rank reduction of D(Gaussian) ≤ true drift rate ≤ rank reduction of D(Gaussian) + non-Gaussian correction. The correction is bounded by the three techniques of A.17.

### 6.2 The Measure Problem for D

For systems where the macrostate space M is not finite-dimensional, the internal block D may be an operator rather than a matrix. The notion of "rank" needs to be replaced by spectral properties (essential spectrum, Fredholm index). The ACP's H(m′|m) generalizes naturally (it's defined information-theoretically, not algebraically), but the Schur complement M/D requires more care for infinite-dimensional operators. The Bach-Ballesteros-Fröhlich (2025) semigroup property of the smooth Feshbach-Schur map provides the necessary technical framework.

### 6.3 The Categorical Completion

The categorical register (Section 4.1) is sketched but not fully formalized. A complete treatment would require:

(a) Defining a category **Persist** whose objects are systems with the ACP block structure and whose morphisms are persistence-preserving maps.

(b) Showing that the Crystallization Drift Theorem defines a functor from **Persist** to a poset category (rank(D), ≤), capturing the monotonic drift.

(c) Showing that anti-crystallization mechanisms are natural transformations that reverse the functor's direction.

(d) Connecting **Persist** to QuadRel via the Gaussian truncation functor.

This would place the full ACP on categorical foundations, completing the bridge to the Stein-Zanasi-Piedeleu-Samuelson program.

### 6.4 The Uncertainty Principle Connection

The algebraic paper's Section 4 identifies the mathematical ingredients for deriving the Heisenberg uncertainty principle from persistence requirements. With the Schur complement bridge formalized, this program can be restated more precisely as a proposed chain from persistence to the quantum uncertainty floor:

1. rank(D) > 0 → internal degrees of freedom exist → the observable algebra is non-commutative (open in the first-principles direction; likely Tomita-Takesaki territory)
2. Non-commutativity → Robertson bound → entropic uncertainty (Maassen-Uffink)
3. Stone-von Neumann uniqueness → the conjugate structure is canonical
4. Groenewold-van Hove → the non-commutativity is irremovable
5. Gromov → symplectic rigidity → the uncertainty floor is geometric

**Reconciliation with A.20.** Appendix A.20 closes the part of this program that begins after a non-commutative quantum partition has been specified. Given a two-MASA partition (𝒜_A, 𝒜_B) generated by conjugate observables with [A, B] = iκI, Theorem A.20.27 proves that the Restraint-Power coordination floor is strictly positive and that its quantitative value coincides with the Robertson bound σ(A)σ(B) ≥ κ/2. In the Schur register, the nonzero commutator is the coupling block that prevents the two MASAs from being jointly collapsed; in the ACP register, the same obstruction is the positive coordination floor γ_AB > 0.

This resolves the original Heisenberg connection as a *reduction*: Heisenberg is the quantum-scale instantiation of the ACP coordination floor for a non-commutative two-MASA subsystem partition. It does not yet resolve the stronger first-principles derivation of quantum kinematics itself. Step 1 above remains open in the stricter sense: one still must show, without importing the canonical commutation relation, that the persistence condition rank(D) > 0 selects a non-commutative operator algebra, and then identify when that algebra is forced into the canonical [Q, P] = iℏI form. That residual problem is now tracked in A.20 as OP-RP-5 rather than as a separate Schur-bridge gap.

---

## 7. Conclusion

The Schur complement bridge transforms the relationship between the ACP paper and the algebraic paper from structural analogy to mathematical identity. The productive interval of the ACP *is* the regime of non-degenerate internal block D. Crystallization drift *is* progressive rank reduction of D. The capacity ≥ complexity threshold *is* the ACP's persistence condition in algebraic coordinates. Anti-crystallization *is* rank restoration.

With this bridge, the unified theory has three layers:

1. **Physics** (ACP): Why persistence requires the productive interval. Derived from thermodynamic axioms.

2. **Algebra** (Schur complement): How the productive interval is computed. The universal operation for eliminating internal degrees of freedom.

3. **Dynamics** (CDT): How the productive interval erodes. The monotonic drift toward crystallization driven by self-reinforcing mechanisms.

The papers are no longer companions. They are chapters of a single argument. The pattern that was hiding in plain sight is the algebraic shadow of a thermodynamic law.
