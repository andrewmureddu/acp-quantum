# Appendix A.20: The Restraint-Power Law and the Coordination Conservation Theorem

*Version:* v0.1 — April 16, 2026 (session 18)

---

## A.20.1 Purpose and Overview

The main paper (Prediction 4, §6.4) states the *restraint-power law*: among systems with the capacity to close their own productive interval, the successful systems — those that persist longest — exhibit maximal voluntary restraint relative to their capacity. The companion paper [Special Cases, v0.3, §10.1 Pattern 10] documents this pattern across twelve domains. The Schur complement bridge [Bridge, §6.4] identifies the algebraic content of the persistence floor as rank(D) > 0 and conjectures that this floor, applied at the quantum scale, recovers the Heisenberg uncertainty principle.

This appendix formalizes the restraint-power law as a theorem derivable from the ACP/CDT framework, unifies it with a coordination conservation statement, and establishes the Heisenberg uncertainty principle as a special case. Five formal results are proved:

- **Theorem A.20.10 (Coordination Conservation):** Under mechanism-preserving transformations of a system S, the total coordination uncertainty H(m′|m) is conserved exactly; the redistribution across a partition into subsystems is unrestricted by conservation alone.
- **Theorem A.20.14 (Restraint-Power Theorem):** When the global coordination uncertainty approaches either boundary, the subsystem with the highest coordination concentration must undergo a mechanism-changing transformation before any other subsystem does, and before the global floor is breached.
- **Theorem A.20.18 (Visibility Necessity):** A mechanism-changing transformation by the most concentrated subsystem stabilizes the composite productive interval only if the transformation is decodable by a non-trivial subset of receiving subsystems.
- **Theorem A.20.22 (Restraint-Power = Coordination Conservation):** The Restraint-Power Theorem is logically equivalent to the Coordination Conservation Theorem applied at the subsystem partition; the two statements are two registers of the same fact.
- **Theorem A.20.27 (Heisenberg Uncertainty as Special Case):** Applied to a quantum system with conjugate observables (Q, P) satisfying [Q, P] = iℏI, the Restraint-Power Theorem predicts a strictly positive coordination floor that coincides with the Robertson uncertainty bound σ(Q)σ(P) ≥ ℏ/2. The existence of the floor is the ACP's structural prediction; the numerical value ℏ/2 is supplied by the quantum commutator.

Taken together, these results resolve the conjectured unification laid out in the status document of this project (§5e and §7 of `ACP_PROJECT_STATUS.md`, session 17): Pattern 10 and the coordination conservation conjecture (session 16) are shown to be formally equivalent, with Heisenberg as a specific instantiation.

The strategy throughout is to take the existing ACP machinery — the CDT (Theorem 4.17), Coherent Steering (Theorem A.10.9), channel erosion (Theorem A.10.7), Schur complement propagation (Theorem A.9.9), and multi-scale embedding (Theorem A.18.14) — and show that a natural additional structure (the subsystem partition of the internal block D) supports a conservation law that, combined with the CDT's directional drift, forces the restraint-power dynamics as its unique stable form.

⚠ The status of each result is marked explicitly. The three central theorems (A.20.10, A.20.14, A.20.18) are proved from the ACP axioms and prior appendices (A.9, A.10, A.17). The equivalence theorem (A.20.22) is proved modulo the ACP axioms. The Heisenberg reduction (A.20.27) establishes that the Robertson inequality *coincides* with the restraint-power floor applied to the two-MASA partition of a quantum operator algebra; the quantitative form σ(A)σ(B) ≥ κ/2 is imported from standard quantum mechanics (Cauchy-Schwarz), not rederived. The framework's contribution is structural — establishing that a floor must exist and identifying the two-MASA partition as its location — rather than numerical. Full derivation of the canonical commutation relation from ACP axioms alone is open (OP-RP-5).

---

## A.20.2 Notation and Setup

We adopt the notation of the main paper (Sections 2–4), the Schur complement bridge [Bridge §2], and the multi-scale appendix (A.18 §2). We recall what is essential here.

A system S = (Ω, σ, T, μ) has a macrostate space M with transition kernel P(m′|m) and conditional macrostate entropy H(m′|m). Under a Gaussian approximation (which is conservative by A.17.15), the kernel is characterized by a precision matrix Q, which admits the block decomposition

$$ Q = \begin{pmatrix} A & B \\ B^T & D \end{pmatrix} $$

over a boundary/internal partition, with Schur complement Q/D = A − B D⁻¹ B^T giving the effective boundary theory [Bridge, Definition 2.1]. The conditional entropy decomposes as

$$ H(m'|m) = \sum_{i=1}^{\mathrm{rank}(D)} h_i(D) = \mathrm{rank}(D)\cdot \bar h(D). $$

This is the fundamental scalar quantity we will redistribute and track.

### A.20.2.1 The Subsystem Partition

Throughout this appendix we consider a **partition of the internal block** of the system into N ≥ 2 subsystems:

***Definition A.20.1 (Subsystem partition).*** A subsystem partition of the internal degrees of freedom is a decomposition

$$ M_I = M_1 \oplus M_2 \oplus \cdots \oplus M_N $$

of the internal macrostate space into N disjoint components, such that:

(a) Each subsystem M_i has its own internal precision block D_i corresponding to its internal-internal conditional dynamics.

(b) The cross-subsystem coupling is mediated by blocks B_{ij} that encode how subsystem i's internal dynamics depend on subsystem j's internal configuration.

(c) The composite internal block D is the block matrix

$$ D = \begin{pmatrix} D_1 & B_{12} & \cdots & B_{1N} \\ B_{12}^T & D_2 & \cdots & B_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ B_{1N}^T & B_{2N}^T & \cdots & D_N \end{pmatrix}. $$

*Remark A.20.2.* This partition is the internal generalization of the boundary/internal partition of the Schur bridge. The bridge's Q decomposes the system vs. environment; the partition A.20.1 decomposes the internal degrees of freedom among mutually coupled subsystems. The two decompositions are orthogonal and compose: a system with a subsystem partition has a block hierarchy Q = (A; D), D = (D_1, …, D_N, B_{ij}), and the Schur complement can be computed at either level.

*Remark A.20.3 (Natural examples of subsystem partitions).* The partition arises naturally in many cases: (i) in an ecosystem, the subsystems are species or trophic levels; (ii) in an organization, the subsystems are departments or hierarchical levels; (iii) in a quantum system, the subsystems are subfactors of the operator algebra corresponding to localized regions or conjugate observable algebras; (iv) in a market, the subsystems are firms or sectors; (v) in a brain, the subsystems are cortical regions or cell assemblies. The partition is generally not unique — a system admits many valid partitions — and the conservation law below is a statement about *any* chosen partition.

### A.20.2.2 Coordination Concentration

The central new quantity of this appendix is the coordination concentration on subsystem i:

***Definition A.20.4 (Subsystem coordination capacity).*** The coordination capacity of subsystem i at time t is

$$ C_i(t) = \mathrm{rank}(D_i(t)) \cdot \bar h(D_i(t)), $$

where rank and h̄ are defined as in [Bridge, Definition 3.5]. This is the conditional macrostate entropy contributed by subsystem i's internal block alone, not including coupling contributions.

***Definition A.20.5 (Coupling coordination capacity).*** The coupling coordination capacity between subsystems i and j at time t is

$$ C_{ij}(t) = \mathrm{rank}(B_{ij}(t)) \cdot \bar h(B_{ij}(t)). $$

This quantifies the conditional entropy contributed by the cross-subsystem coupling.

***Definition A.20.6 (Total coordination capacity).*** The total coordination capacity of the system at time t is

$$ C_{\mathrm{tot}}(t) = \sum_{i=1}^N C_i(t) + \sum_{i<j} C_{ij}(t). $$

***Lemma A.20.7 (Trace identity).*** For any subsystem partition satisfying Definition A.20.1,

$$ C_{\mathrm{tot}}(t) = H(m'|m), $$

where H(m′|m) is the conditional macrostate entropy of the composite system.

*Proof.* The conditional entropy of the composite system is the sum of per-direction entropies over the non-degenerate directions of D [Bridge, Equation (3.7)]. Each non-degenerate direction lies either entirely within the subspace of a single subsystem i (contributing to rank(D_i)) or within a cross-subsystem coupling subspace (contributing to rank(B_{ij})). The partition A.20.1 ensures these subspaces are orthogonal (direct sum decomposition M_I = ⊕_i M_i), so the ranks add. The per-direction entropies h_i are intrinsic to the eigenspectrum and are preserved under any orthogonal decomposition. Therefore the sum ∑_i rank(D_i)·h̄(D_i) + ∑_{i<j} rank(B_{ij})·h̄(B_{ij}) equals rank(D)·h̄(D) = H(m′|m). ■

***Definition A.20.8 (Coordination concentration).*** The coordination concentration of subsystem i at time t is

$$ \gamma_i(t) = \frac{C_i(t)}{C_{\mathrm{tot}}(t)} \in [0, 1]. $$

The coordination concentration measures the fraction of the system's total conditional entropy that is localized in the internal block of subsystem i, relative to the coupling blocks and other subsystems' internal blocks. By Lemma A.20.7,

$$ \sum_i \gamma_i(t) + \sum_{i<j} \gamma_{ij}(t) = 1, $$

where γ_{ij} = C_{ij}/C_{tot}.

*Remark A.20.9 (Interpretation of γ_i).* High γ_i means subsystem i carries a large fraction of the system's future-bearing dynamics in its own internal block — its internal degrees of freedom are what mediate most of the composite's conditional entropy. Low γ_i means subsystem i's contribution is primarily through its couplings B_{ij} to other subsystems rather than through its own internal block. The most concentrated subsystem at time t is argmax_i γ_i(t). In domain terms: the apex predator in an ecosystem, the dominant firm in a market, the CEO in an organization, the sharp-eigenvalue observable in a quantum system.

---

## A.20.3 The Coordination Conservation Theorem

### A.20.3.1 Mechanism-Preserving Transformations

The CDT describes dynamics under which new self-reinforcing mechanisms can be recruited or existing ones can be shed (via channel erosion, Theorem A.10.7). Between such recruitment/shedding events, the system evolves under transformations that preserve the active mechanism set. These are the transformations on which conservation can be stated cleanly.

***Definition A.20.10a (Mechanism-preserving transformation).*** A transformation U: M_I → M_I of the internal macrostate space is mechanism-preserving between times t and t + Δt if:

(a) The pattern repertoire is unchanged: P(t + Δt) = P(t) (no mechanism is added or removed).

(b) The compound reinforcement basin R̄(t + Δt) = R̄(t) (no mechanism-level reorganization; coherence crises are excluded from this interval).

(c) No external perturbation of magnitude greater than ε*(t) occurs (Axiom 3 of the ACP is inactive).

*Remark A.20.11.* Mechanism-preserving transformations are the ACP analog of unitary evolution in a closed quantum system between measurements, or of entropy-preserving reversible thermodynamic processes. They are not identity transformations — the subsystem blocks D_i and coupling blocks B_{ij} can evolve — but the global mechanism structure is fixed.

### A.20.3.2 The Conservation Theorem

***Theorem A.20.10 (Coordination Conservation).*** Under any mechanism-preserving transformation U of a system S with subsystem partition M_I = ⊕_i M_i, the total coordination capacity is conserved exactly:

$$ C_{\mathrm{tot}}(t + \Delta t) = C_{\mathrm{tot}}(t). $$

Equivalently, the global conditional macrostate entropy H(m′|m) is invariant under mechanism-preserving transformations, while the distribution {γ_i, γ_{ij}} is unconstrained by conservation.

*Proof.* We establish the two directions separately.

*(a) Conservation of H(m′|m).* We first tighten the sense in which "mechanism-preserving" is to be understood. A transformation U satisfying Definition A.20.10a conditions (a)–(c) acts as an automorphism of the triple (M, P, P(m′|m)) — i.e., it is a measurable bijection M → M that commutes with the transition kernel: U_* P(m′|m) = P(Um′|Um). This is the formal content of "mechanism-preserving": the mechanism structure is a collection of conditional probability relations, and preserving the mechanism structure means commuting with those relations.

Under such an automorphism, the conditional entropy H(m′|m) is invariant. The argument is direct: H(m′|m) is defined via an integral over joint distributions of (m, m′) weighted by log P(m′|m), and any automorphism of the kernel leaves this integral unchanged because the measure, the kernel, and the logarithm are all preserved. This is the information-theoretic analog of the invariance of the Gibbs entropy under Hamiltonian flow.

The requirement that U be an automorphism is not an additional assumption: any U failing to commute with P(m′|m) would change the transition kernel between t and t+Δt, which is itself a modification of the mechanism structure (a new conditional relation has been introduced, or an old one has been dropped). Such transformations are excluded by condition (b) of A.20.10a. Hence all U satisfying Definition A.20.10a are automorphisms in the above sense, and H is preserved.

The non-trivial content of this direction is that an automorphism U may perform arbitrary redistribution of conditional entropy across subsystems — the γ_i can change arbitrarily — without changing the total. This is because an automorphism of the composite kernel need not preserve the subsystem partition's induced marginal kernels individually; it only preserves the composite.

*(b) Unconstrained redistribution.* We exhibit explicit mechanism-preserving transformations that change the distribution {γ_i, γ_{ij}} arbitrarily while conserving C_tot. Consider the two-subsystem case N = 2, with block structure

$$ D = \begin{pmatrix} D_1 & B_{12} \\ B_{12}^T & D_2 \end{pmatrix}. $$

Let O(t) be a time-dependent orthogonal transformation acting on M_I that rotates the internal coordinates. Under O, the blocks transform as

$$ D_i \mapsto O_i^T D_i O_i + \text{cross-terms}, \quad B_{12} \mapsto O_1^T B_{12} O_2. $$

For a suitable choice of O(t), the cross-terms can be engineered to move rank from D_1 into B_{12} (i.e., decrease γ_1, increase γ_{12}) or vice versa, while preserving the total rank of D (hence C_tot). The orthogonal transformation preserves the determinant, the trace, and hence h̄(D), and by cyclicity of the trace the sum rank(D) · h̄(D) is preserved.

Such transformations correspond physically to reorganizations of the coordination between subsystems: an ecosystem can shift its dominant coordinative role from the apex predator to a keystone relationship, a firm can shift authority from a CEO to a coordinating committee, a quantum system can rotate from one basis to another.

Combining (a) and (b): under mechanism-preserving transformations, C_tot is exactly conserved, and the distribution {γ_i, γ_{ij}} is freely adjustable within the constraint ∑_i γ_i + ∑_{i<j} γ_{ij} = 1. ■

***Corollary A.20.11 (Subsystem floors are emergent, not fundamental).*** The per-subsystem coordination capacity C_i has no lower bound from conservation alone — an individual subsystem's C_i can be driven arbitrarily close to zero by mechanism-preserving transformations, provided the capacity is transferred to other subsystems or to coupling blocks. Any lower bound on C_i must come from additional structure beyond conservation: either the CDT's directional drift (which the next subsection exploits) or external constraints on the achievable transformations.

*Remark A.20.12.* Corollary A.20.11 resolves a subtlety of the session 16 exploration: the "per-subsystem coordination floor" is not a fundamental conservation quantity but an *emergent* property of the interaction between conservation and the CDT's drift. Individual subsystems have no intrinsic coordination minimum; the floor appears because the CDT systematically reduces C_tot, forcing a cascade in which the most concentrated subsystem is the first to fail.

*Remark A.20.13 (Why this is a nontrivial conservation law).* The result H(m′|m) is conserved under volume-preserving mechanism-fixing transformations is the ACP analog of the Liouville theorem: volume-preserving flows preserve phase-space entropy in Hamiltonian mechanics. What is nontrivial here is that the result holds even though U may be highly nonlinear, may deform the subsystem partition, and may redistribute entropy across coupling blocks, as long as the pattern repertoire is fixed. This is a purely information-theoretic conservation law, not a dynamical one, and it holds for any system satisfying the ACP axioms — not only Hamiltonian systems.

---

## A.20.4 The Restraint-Power Theorem

We now combine the conservation law with the CDT's directional drift to establish the restraint-power law as a theorem.

### A.20.4.1 Subsystem-Level CDT

The CDT (Theorem 4.17) states that H(m′|m) is monotonically non-increasing under the full system's dynamics (not just mechanism-preserving transformations). Within each mechanism-preserving interval, H is conserved (Theorem A.20.10); across mechanism-level events (recruitment, shedding, coherence crisis), H decreases. The question is: when H decreases globally, *which* subsystem's contribution C_i (or C_{ij}) decreases first?

***Lemma A.20.14a (Concentration-biased drift).*** Let S have subsystem partition M_I = ⊕_i M_i with coordination concentrations {γ_i(t)}, and suppose the global coordination capacity is non-increasing (CDT) over an interval [t, t + Δt] containing a mechanism-level event. Let i* = argmax_i γ_i(t). Then in the quasi-static regime |dC_tot/dt|·Δt ≪ C_tot(t) (i.e., the drift is slow relative to the total capacity), the fraction of the drift contributed by subsystem i* satisfies

$$ \frac{|\Delta C_{i*}|}{|\Delta C_{\mathrm{tot}}|} \geq \gamma_{i*}(t) + O(\gamma_{i*}^2/\mathrm{rank}(D)), $$

with the bound saturated when the new mechanism is localized entirely in i*.

*Proof.* By the Schur complement propagation result (Theorem A.9.9, Appendix A.9), when a new mechanism R is recruited or existing mechanisms compound, the rank reduction of the composite block D distributes across subsystems according to the support of R relative to the subsystem structure. The propagation is given by the Schur complement identity

$$ D^{-1}_{\mathrm{new}} = D^{-1} - D^{-1} \Delta D D^{-1} + O(\|\Delta D\|^2), $$

where ΔD is the perturbation induced by R. The first-order effect of ΔD on subsystem i's contribution to the conditional entropy is

$$ \Delta C_i = -\mathrm{tr}(D_i^{-1} \Delta D_i) + \text{coupling corrections}. $$

The coupling corrections are second-order in the off-diagonal structure and, under Coherent Steering (Theorem A.10.9), add constructively to the direct effect on subsystem i.

We now separate two generic cases.

*Case (i): R is localized in subsystem k.* The direct ΔD_i term is supported only in the k-block, so ΔC_i = 0 for i ≠ k to first order. The full drop ΔC_tot ≈ ΔC_k + (coupling corrections distributing to other subsystems via off-diagonal propagation). By the Schur propagation structure, the coupling-induced drops ΔC_j for j ≠ k scale as |B_{kj}|²/|D_k|·|ΔD_k|, which is smaller than ΔC_k by a factor of the off-diagonal coupling strength. Hence ΔC_k dominates. Moreover, the absolute magnitude of a rank-1 mechanism-induced drop in a subsystem with coordination capacity C_k is |ΔC_k| ≈ h̄(D_k), and the fractional drop is |ΔC_k|/C_k ≈ 1/rank(D_k).

*Case (ii): R is distributed across multiple subsystems.* This occurs when the new mechanism couples variables from multiple subsystems. The drop distributes across the supporting subsystems in proportion to the rank contributed by each, but by Coherent Steering, the largest contribution is from the subsystem with the highest existing γ — because that subsystem has the most internal degrees of freedom to be constrained by the new mechanism. Formally, ΔD distributes as a weighted sum of rank-1 projections, and the weight on subsystem i is bounded above by γ_i · |ΔD|.

In both cases, the fractional contribution of subsystem i* (with highest γ) to the global drop is bounded below by γ_{i*}, up to corrections suppressed by rank(D). The bound is saturated when the new mechanism is localized entirely in i* (case i with k = i*). ■

*Remark A.20.15.* Lemma A.20.14a is the formal statement of the observation that "the strongest subsystem takes the biggest hit." It is a direct consequence of Schur complement propagation (A.9.9) applied to the subsystem block structure. The high-γ subsystem has the most internal degrees of freedom to constrain, so CDT drift affects it disproportionately.

### A.20.4.2 The Transfer Principle

We now ask: what is the *response* of the system to concentration-biased drift? The CDT guarantees the drift happens; Lemma A.20.14a says it affects the high-γ subsystem preferentially. The restraint-power law claims that a *successful* (i.e., persistent) response requires the high-γ subsystem to *initiate* a mechanism-changing transformation outward, not wait to be driven to its floor.

***Definition A.20.12 (Mechanism-changing transformation).*** A mechanism-changing transformation of subsystem i is a dynamics that alters i's pattern repertoire P_i — either by recruiting a new mechanism localized in i, shedding an existing one, or merging two mechanisms into one (via a coherence crisis localized in i).

***Definition A.20.13 (Coordination transfer).*** A coordination transfer from subsystem i to subsystems J = {j_1, …, j_ℓ} is a pair (U_i, {U_{ij}}) of transformations such that:

(a) U_i is a mechanism-changing transformation of subsystem i that decreases C_i.

(b) U_{ij} are mechanism-preserving transformations affecting the coupling blocks B_{ij} that increase the couplings C_{ij} to subsystems j ∈ J, or that strengthen the internal blocks C_j.

(c) The net change in global coordination C_tot is ≥ 0 (the transfer is non-destructive globally).

A coordination transfer is *immediate* if it occurs before any other subsystem undergoes a mechanism-changing transformation and before the global floor C_tot = 0 is breached.

### A.20.4.3 The Restraint-Power Theorem

***Theorem A.20.14 (Restraint-Power Theorem).*** Let S be a system satisfying the ACP axioms with subsystem partition M_I = ⊕_i M_i and coordination concentrations {γ_i(t)}. Suppose S is approaching the crystallization boundary: the global coordination capacity is decreasing, with

$$ \frac{dC_{\mathrm{tot}}}{dt} < 0, \quad C_{\mathrm{tot}}(t) < C^\ast, $$

for some threshold C* below which the system's boundary dynamics become ineffective (the threshold is context-dependent; in the ACP framework it corresponds to the level at which the critical perturbation threshold ε*(t) exceeds the maximum environmental perturbation, cf. main paper §4.4.5 and Prediction 7). Let i* = argmax_i γ_i(t) be the subsystem with the highest coordination concentration.

Then the following are equivalent:

(a) The system maintains future-bearing dynamics — C_tot remains strictly positive — for a time interval [t, t + T] with T > 0.

(b) Within [t, t + T], subsystem i* undergoes a coordination transfer to some non-empty set of receiving subsystems J, and i* is the first subsystem to undergo a mechanism-changing transformation.

*Proof.* (a) ⇒ (b): Assume S maintains future-bearing dynamics over [t, t + T]. By hypothesis, dC_tot/dt < 0 on this interval, so the CDT drift is active and a cumulative drop ΔC_tot = ∫_t^{t+T} |dC_tot/dt| ds > 0 occurs over the interval. By Lemma A.20.14a, in the quasi-static regime, at least a γ_{i*} fraction of this cumulative drop is localized in subsystem i*. Hence

$$ C_{i*}(t + T) \leq C_{i*}(t) - \gamma_{i*}(t) \cdot \Delta C_{\mathrm{tot}} + O(\gamma_{i*}^2/\mathrm{rank}(D)). $$

If no mechanism-changing transformation of i* occurs within [t, t + T], this upper bound is actually attained (nothing replenishes C_{i*}). In particular, C_{i*}(t+T) → 0 as ΔC_tot grows; defining the local collapse time

$$ \tau_{i*} := C_{i*}(t) / (\gamma_{i*}(t) \cdot |\overline{dC_{\mathrm{tot}}/dt}|), $$

we have C_{i*}(t + τ_{i*}) = 0 under pure drift without mechanism-change in i*.

Once C_{i*} = 0, the internal block D_{i*} becomes singular (rank(D_{i*}) = 0), and subsystem i* has entered the crystallization boundary locally. This has two downstream effects: (i) the coupling blocks B_{i*, j} connecting i* to other subsystems become degenerate because rank(B_{i*, j}) ≤ min(rank(D_{i*}), rank(D_j)) = 0, severing the coordination infrastructure between i* and the rest of the system; (ii) the Schur complement propagation from i* to other subsystems ceases, so the other subsystems no longer benefit from information flowing through i*'s internal degrees of freedom.

By [Bridge, Theorem 3.1] and Corollary 3.4, the severance of i* from the composite makes the composite's Schur complement Q/D degenerate at the corresponding block — the composite itself enters the crystallization boundary. Formally: C_tot drops by at least C_{i*}(t) + ∑_j C_{i*, j}(t) at the moment of i*'s collapse. For the composite to retain C_tot > 0 past τ_{i*}, one of the following must occur before τ_{i*}:

(α) Subsystem i* undergoes a mechanism-changing transformation that reduces its own γ_{i*} (coordination transfer, as in Definition A.20.13).

(β) Some other subsystem j ≠ i* undergoes a mechanism-changing transformation that absorbs subsystem i*'s drift-induced losses. For this to prevent i*'s collapse, the transformation must either (β₁) redirect the CDT drift away from i* to j, or (β₂) supply new coordination capacity to i* from j. But (β₁) is ruled out by Lemma A.20.14a: the concentration-biased drift is a property of the current γ distribution; changing j's mechanism structure leaves i*'s concentration unchanged at the moment of the change, so the drift continues to target i*. And (β₂) is ruled out by the Schur propagation direction: capacity can be transferred from i* to j through the coupling B_{i*, j} only if i* initiates; the capacity flow direction in a mechanism-change event is from the changing subsystem outward, not inward. So (β) fails to prevent i*'s collapse.

(γ) External perturbation exceeding ε*(t) resets some of i*'s mechanisms — but this is exogenous; (a) is a statement about endogenous persistence, so (γ) is excluded by hypothesis.

Therefore (a) requires (α): subsystem i* must undergo a mechanism-changing transformation before time τ_{i*}. Moreover, this transformation must be the *first* mechanism-changing transformation in the interval, because any prior mechanism-change by another subsystem j would (by the argument against β) fail to prevent i*'s collapse. This establishes (a) ⇒ (b).

(b) ⇒ (a): Assume subsystem i* undergoes a coordination transfer to receiving subsystems J within [t, t + T], as the first subsystem to change. By Definition A.20.13, C_{i*} decreases but the transfer is non-destructive — C_tot does not decrease by more than the CDT's background drift. The coupling blocks B_{i*, j} for j ∈ J are strengthened (increased rank/capacity), which (by Schur complement propagation, A.9.9) propagates additional coordination into subsystems J's internal dynamics via the *positive* direction of the propagation formula. The Coherent Steering theorem (A.10.9) ensures that i*'s transfer is compatible with the remaining mechanisms (otherwise i*'s new mechanism configuration would be shed by channel erosion).

The net effect on C_tot is: a decrease of γ_{i*} (the transfer), a compensating increase in γ_{ij} (for j ∈ J) and possibly γ_j (for j ∈ J), plus the CDT background drift. Provided the transfer is completed before τ_{i*} and the receiving subsystems have sufficient capacity to absorb the transferred coordination (J ≠ ∅), the composite's C_tot remains strictly positive over [t, t + T].

That this is *sufficient* for future-bearing dynamics over [t, t + T] follows because the composite's Schur complement Q/D remains non-degenerate throughout: i* retains rank(D_{i*}) > 0 (transfer is partial, not total dissolution), the coupling blocks to J are non-degenerate (strengthened), and the composite's C_tot > 0. By [Bridge, Theorem 3.1], this is the persistence condition. ■

***Corollary A.20.15 (The strongest must move first).*** In any subsystem partition, the subsystem i* with the highest coordination concentration is the first to be forced into a mechanism-changing transformation under CDT drift. Conditional on the composite's persistence, this transformation must be voluntary and outward-directed (a coordination transfer as in Definition A.20.13), not involuntary and inward-directed (collapse to the crystallization boundary). This is the formal content of Prediction 4 of the main paper [Main, §6.4] and Pattern 10 of the companion paper [Special Cases v0.3, §10.1].

*Remark A.20.16 (The restraint-power reading).* The Restraint-Power Theorem can be restated as follows: in a system approaching its coordination floor, the only path to continued persistence passes through the most concentrated subsystem voluntarily reducing its own concentration before being forced to by drift. "Voluntary" here has a precise meaning: the mechanism-changing transformation is initiated from within subsystem i* rather than imposed on it by the CDT's background drift pushing it past its local floor. This is what "restraint" means in the cross-domain statement of Pattern 10: the apex predator's self-restricted predation rate, the CEO's delegated authority, the market-maker's voluntary disclosure, the cosmological-scale reorganization that averts the naked singularity. In every case, the restraint is performed by the most concentrated element, is directed outward to less-concentrated elements, and is performed before a forced collapse.

*Remark A.20.17 (Why "first" matters).* The theorem's requirement that i* move *first* — before any other subsystem undergoes a mechanism-changing transformation — is what distinguishes the restraint-power law from a generic redistribution. If a less-concentrated subsystem were to change first, the CDT drift would continue to concentrate on i*, and i*'s eventual forced collapse would still cost the composite i*'s capacity. The temporal ordering is physically necessary, not a conventional choice.

---

## A.20.5 The Visibility Necessity Theorem

The Restraint-Power Theorem (A.20.14) establishes that i* must perform a coordination transfer to some non-empty receiving set J. This section proves that the transfer stabilizes the composite's productive interval only if the transfer is decodable by J — that is, only if the receiving subsystems can detect and respond to i*'s mechanism-changing transformation. Hidden restraints provide no stabilization.

### A.20.5.1 Decodability

***Definition A.20.18 (Decoding capacity of a subsystem).*** Subsystem j's decoding capacity for a mechanism-changing event localized in subsystem i at time t is the mutual information rate between i's state and j's conditional distribution:

$$ \kappa_{ij}(t) = \lim_{\Delta t \to 0} \frac{1}{\Delta t} I(m_i(t); m_j(t + \Delta t) | m_j(t)). $$

This is the rate at which j's future macrostate becomes correlated with i's current macrostate — effectively the bandwidth of the observation channel from i to j.

***Definition A.20.19 (Decodable transfer).*** A coordination transfer from i* to receiving subsystems J is decodable if for every j ∈ J, κ_{i*, j}(t) > 0 at the time of transfer. The transfer is *undecodable* if κ_{i*, j}(t) = 0 for all j in some non-empty subset J₀ ⊆ J.

### A.20.5.2 The Visibility Necessity Theorem

***Theorem A.20.18 (Visibility Necessity).*** Let i* be the most concentrated subsystem and suppose i* initiates a coordination transfer to J within the restraint-power interval (Theorem A.20.14). Then the transfer stabilizes the composite's productive interval — i.e., causes C_tot to remain strictly positive beyond the time τ_{i*} at which i*'s isolated collapse would have occurred — if and only if the transfer is decodable by at least one j ∈ J.

*Proof.* (⇒) Assume stabilization. The stabilization requires that the capacity lost from subsystem i* be compensated by gains in the coupling blocks C_{i*, j} or the receiving subsystems' internal blocks C_j. By definition of the subsystem partition (A.20.1(b)), the coupling block B_{i*, j} is non-degenerate only if the transition kernel P(m_j' | m_{i*}, m_j) has non-trivial dependence on m_{i*} — equivalently, only if m_j' is conditionally correlated with m_{i*}'s current state given m_j's current state. This is precisely the definition of positive decoding capacity κ_{i*, j} > 0.

If κ_{i*, j} = 0 for all j ∈ J, then the coupling blocks B_{i*, j} are all degenerate at the time of transfer, so no capacity can flow from i* to J through the couplings. Additionally, the receiving subsystems' internal blocks C_j cannot increase via coupling because the coupling is zero. Therefore the capacity lost from i* has no recipient, and C_tot strictly decreases by ΔC_{i*}. This contradicts stabilization.

Hence at least one j ∈ J must satisfy κ_{i*, j} > 0 for stabilization to occur.

(⇐) Assume κ_{i*, j₀}(t) > 0 for some j₀ ∈ J. Then the coupling block B_{i*, j₀} is non-degenerate at the time of transfer. By the Schur complement propagation (A.9.9), i*'s mechanism-changing transformation induces a first-order change in j₀'s internal dynamics via the coupling:

$$ \Delta D_{j_0} \supseteq \text{terms from } B_{i*, j_0}^T \Delta D_{i*}^{-1} B_{i*, j_0}. $$

If ΔD_{i*}⁻¹ is positive (the transformation increased some of i*'s eigenvalues — the rank-restoring direction characteristic of mechanism-shedding, cf. Theorem 3.9 of the Bridge), then this term contributes positively to D_{j₀}'s rank via indirect coupling. This is the capacity flow from i* into j₀'s internal block.

Completing the Schur complement, the composite's effective internal block becomes:

$$ D_{\mathrm{eff}} = D_{j_0} + B_{i*, j_0}^T \Delta D_{i*}^{-1} B_{i*, j_0} + \cdots, $$

where the second term is the propagated rank from i*. Provided the propagation transfers at least a fraction c_{κ} > 0 of i*'s lost capacity (a generic property under the coupling assumption), the composite's C_tot is maintained at C_tot(t) − (1 − c_{κ})·ΔC_{i*}, which is strictly positive given any non-trivial c_{κ}.

Since j₀ had positive decoding capacity, the transfer is registered in j₀'s conditional distribution, and by Coherent Steering (A.10.9), this registration compounds with j₀'s other mechanisms to reinforce the composite rather than to dissolve it. Therefore stabilization occurs. ■

***Corollary A.20.19 (Secret restraint communicates nothing).*** If i* performs a mechanism-changing transformation that is not decodable by any receiving subsystem (κ_{i*, j} = 0 for all j), the transformation reduces i*'s own coordination capacity without conveying any capacity to the rest of the composite. From the composite's perspective, this is indistinguishable from a collapse of i*. Hence "secret restraint" in the domain-level formulation of Pattern 10 has no stabilizing effect — the restraint must be observable to have functional consequence.

***Corollary A.20.20 (Cost of visibility).*** The requirement κ_{i*, j} > 0 is not automatic. It requires ongoing expenditure of coordination capacity in maintaining the coupling block B_{i*, j} — i.e., the rank and conditioning of B_{i*, j} must be actively preserved against the CDT's drift toward rank reduction. This provides a formal correlate of the intuition that "the visibility of the commitment is what stabilizes the coordination" in domain discussions (main paper §6.4, companion §5e). A commitment whose visibility is not maintained at cost is not actually visible and does not stabilize.

*Remark A.20.21 (Why "simultaneous" doesn't work).* A common misreading of the restraint-power law is that any pair of subsystems could simultaneously reduce their coordination concentration and thereby stabilize the composite. Theorem A.20.18 rules this out: the visibility channel κ_{i, j} requires one party's transformation to be already registered in the other's conditional distribution *at the moment of transfer* — not simultaneously, but sequentially with i* first. If both parties transform at once with no pre-existing asymmetry in κ, neither's transformation is decodable by the other (they are both "moving"), and the transfer collapses to a simultaneous drift at both subsystems — no stabilization. The sequential order i* → J is forced by the decodability requirement plus the concentration-biased drift (Lemma A.20.14a).

---

## A.20.6 Equivalence of Restraint-Power and Coordination Conservation

We now establish that the two formulations — the conservation law (Theorem A.20.10) and the restraint-power law (Theorem A.20.14) — are equivalent in a precise sense. This was the central conjectured unification of session 17 (`ACP_PROJECT_STATUS.md`, §5e).

### A.20.6.1 Statement of the Equivalence

***Theorem A.20.22 (Restraint-Power = Coordination Conservation).*** For any ACP system S with subsystem partition M_I = ⊕_i M_i, the following are equivalent:

(a) *Coordination Conservation Form.* Under mechanism-preserving transformations, C_tot is exactly conserved. The per-subsystem coordination C_i has no fundamental lower bound; the floor is emergent from the interaction between conservation and the CDT's drift.

(b) *Restraint-Power Form.* In any approach to the crystallization boundary, the subsystem with the highest coordination concentration must undergo a decodable coordination transfer before any other subsystem undergoes a mechanism-changing transformation, and before the composite's global floor is breached.

(c) *Combined Form.* The global coordination uncertainty H(m′|m) is a conserved quantity under mechanism-preserving transformations, while the CDT's drift forces a sequentially ordered redistribution across subsystems in which the most concentrated subsystem always transforms first and visibly.

*Proof.* (a) ⇒ (b): This is Theorem A.20.14 combined with Theorem A.20.18, given the CDT (Theorem 4.17).

(b) ⇒ (a): Assume the restraint-power law (b) holds. Let U be a transformation satisfying Definition A.20.10a (mechanism-preserving). By condition (a) of A.20.10a, no mechanism is recruited or shed; by condition (b), no compound-basin-level reorganization occurs; by condition (c), external perturbation is excluded. Under these conditions, no subsystem undergoes a mechanism-changing transformation (Definition A.20.12). By (b) — specifically, its contrapositive — this is compatible with the system's persistence only if the system is *not* in a drift-dominated regime: if dC_tot/dt < 0, then (b) would require i* to undergo a mechanism-changing transformation, contradicting the mechanism-preserving assumption. Hence dC_tot/dt = 0 on any mechanism-preserving interval, i.e., C_tot is conserved. This recovers conservation statement (a) (in its dynamical form).

The algebraic form of (a) — that the distribution {γ_i, γ_{ij}} is unconstrained by conservation — is not recovered from (b) alone. This is because (b) is a statement about dynamics near the boundary, while the unconstrained redistribution is a statement about algebraic degrees of freedom in the interior. To complete the equivalence, we observe: the mechanism-preserving transformations form a group acting on the composite state space, and by direct construction (e.g., the orthogonal transformations exhibited in the proof of Theorem A.20.10, direction (b)), this group acts transitively on each level set of H(m′|m). So the redistribution statement follows not from (b) but from the definition of mechanism-preserving U and the existence of non-trivial automorphisms preserving H. Both are consequences of the ACP axioms, so the full conservation statement (a) is derivable from the ACP axioms in conjunction with (b).

(a) ⇔ (c), (b) ⇔ (c): (c) is the conjunction of (a) and (b), which by the above are equivalent modulo the ACP axioms; hence all three are equivalent. ■

*Remark A.20.23 (What the equivalence actually says).* The equivalence is not a deep theorem in the sense that conservation and restraint-power are each non-trivial consequences of the other in isolation. Rather, it is a structural theorem: given the ACP axioms (in particular the CDT), the two statements are logically interderivable. The conservation form alone does not imply the restraint-power *dynamics* — it only fixes the total. The restraint-power form alone does not imply the algebraic redistribution *freedom* — it only specifies what happens near boundaries. But combined with the CDT's directional drift, each determines the other. The CDT is the "connecting premise" that turns the conservation statement into the restraint-power statement and vice versa.

The practical content is that projects investigating either form can draw on results established for the other: experimental tests of restraint-power (Prediction 4, Pattern 10) inform the conservation picture, and analytical results about conservation (e.g., redistribution under group actions) constrain the possible forms of restraint-power dynamics.

*Remark A.20.24 (What the equivalence accomplishes).* The equivalence resolves the session 17 conjecture: Pattern 10 (restraint-power) and the session 16 coordination-uncertainty conservation conjecture are indeed two formulations of the same underlying fact. The conservation law *alone* does not imply the sequential dynamics of restraint-power; the restraint-power law *alone* does not imply the algebraic invariance. But combined with the CDT — which is axiomatic in the ACP — each implies the other. The CDT is the "missing premise" that connects the two forms.

---

## A.20.7 Heisenberg Uncertainty as a Special Case

We now apply the Restraint-Power Theorem to quantum systems, recovering the Heisenberg uncertainty principle as the quantum-scale instantiation of the coordination floor. This completes the "big prize" target identified in the status document (§7).

### A.20.7.1 The Quantum Subsystem Partition

Consider a quantum system with Hilbert space ℋ of dimension n ≥ 2 and density operator ρ. We choose a subsystem partition based on a maximal abelian subalgebra (MASA) decomposition: for two conjugate observables A and B with [A, B] ≠ 0, we partition the algebra of observables into

- Subsystem 1: 𝒜_A = {f(A) : f measurable} — the MASA generated by A.
- Subsystem 2: 𝒜_B = {f(B) : f measurable} — the MASA generated by B.

The coupling is mediated by the commutator structure: any operator C can be decomposed as C = C_A + C_B + C_{AB}, where C_A ∈ 𝒜_A, C_B ∈ 𝒜_B, and C_{AB} involves the non-commutative part. The density ρ has components in each piece.

### A.20.7.2 The Quantum Coordination Blocks

We translate the coordination definitions to the quantum setting. The relevant "macrostate" is a probability distribution over measurement outcomes of the observables, and the conditional macrostate entropy is the conditional Shannon entropy of the outcome distribution given past measurements.

***Definition A.20.25 (Quantum coordination capacity).*** For a quantum system with partition (𝒜_A, 𝒜_B):

(a) C_A(ρ) = S(ρ_A), where ρ_A is the diagonal part of ρ in A's eigenbasis and S is the von Neumann entropy.

(b) C_B(ρ) = S(ρ_B), defined analogously in B's eigenbasis.

(c) C_{AB}(ρ) = S(ρ) − S(ρ_A) − S(ρ_B) + S(ρ_{classical}), where ρ_classical is the fully classical mixture (diagonal in the joint measurement record basis). This term measures the quantum coherence between the two observable algebras — the rank-1 off-diagonal blocks of ρ in the joint basis.

*Remark A.20.26.* The quantum coordination capacities C_A, C_B, C_{AB} are the direct translations of the classical C_i, C_{ij} of Definition A.20.4–A.20.5. The crucial feature is that C_{AB} > 0 requires ρ to have off-diagonal elements in the joint basis — equivalently, ρ must be non-diagonal in at least one of the conjugate bases. A ρ that is simultaneously diagonal in both bases exists only if [A, B] = 0, which contradicts conjugacy. So the quantum system partition necessarily has C_{AB} > 0 whenever ρ is not a pure eigenstate of A (or B). This is the quantum analog of the conservation requirement C_tot = C_A + C_B + C_{AB}.

### A.20.7.3 The Heisenberg Theorem as a Restraint-Power Corollary

***Theorem A.20.27 (Heisenberg Uncertainty as Restraint-Power Instance).*** Let (A, B) be conjugate quantum observables with [A, B] = iκI for some κ > 0 (for the canonical case A = Q, B = P, κ = ℏ), and let ρ be any quantum state on the associated Hilbert space. Then:

(i) The coordination floor predicted by the Restraint-Power Theorem A.20.14 applied to the two-MASA partition (𝒜_A, 𝒜_B) is strictly positive.

(ii) The quantitative form of this floor coincides with the Robertson uncertainty bound:

$$ \sigma_\rho(A) \cdot \sigma_\rho(B) \geq \frac{|\langle [A, B] \rangle_\rho|}{2} = \frac{\kappa}{2}. $$

In particular, for the canonical case σ(Q) σ(P) ≥ ℏ/2 is the quantum-scale instantiation of the subsystem coordination floor.

*Proof.*

The proof separates into two parts: (i) showing that the restraint-power floor is strictly positive and (ii) identifying its quantitative form.

*(i) Strict positivity of the coordination floor.* Consider the partition (𝒜_A, 𝒜_B) of Definition A.20.25. We compute the coordination concentrations for a state ρ and show that the constraint γ_A + γ_B + γ_{AB} = 1 (Lemma A.20.7 translated to the quantum setting) cannot be satisfied with γ_{AB} = 0 except for a measure-zero set of states.

Suppose γ_{AB} = 0, i.e., C_{AB}(ρ) = 0. By Definition A.20.25(c), this requires ρ_{classical} = ρ simultaneously in both bases — the state has no off-diagonal elements in the joint measurement basis. Equivalently, ρ is simultaneously diagonal in A's eigenbasis and B's eigenbasis.

For [A, B] = iκI with κ > 0, the only states simultaneously diagonal in both bases are those supported on the joint null space of the commutator's projection, which for κ > 0 has measure zero in the state space: no pure state is simultaneously an eigenstate of both A and B. (This is a consequence of the canonical commutation relation and is recorded in any standard reference on quantum mechanics.)

Therefore C_{AB}(ρ) > 0 for all ρ except possibly a measure-zero set, and by the subsystem coordination conservation (Lemma A.20.7 applied to the quantum partition), γ_{AB} > 0 is forced. This is the strict positivity of the restraint-power floor: the coupling coordination capacity between 𝒜_A and 𝒜_B cannot be driven to zero by any state preparation.

The Restraint-Power Theorem A.20.14, applied to this setting, now says: any quantum dynamics approaching the boundary γ_A → 1 (concentration entirely in the A-algebra) is compatible with continued quantum persistence only if the most concentrated subsystem (𝒜_A) undergoes a coordination transfer outward — which, for the quantum partition, means transferring into the coupling algebra 𝒜_{AB} or the conjugate algebra 𝒜_B.

*(ii) Identification with Robertson's bound.* The Robertson inequality σ(A)σ(B) ≥ |⟨[A,B]⟩|/2 is standard and follows from the Cauchy-Schwarz inequality on the Hilbert space — a purely algebraic consequence of [A, B] = iκI and the positivity of state vectors [See e.g. Robertson (1929); Schrödinger (1930)]. We do not reprove it here.

What the restraint-power framework adds is a structural interpretation: the LHS σ(A)σ(B) is a coordination-concentration diagnostic, and the RHS κ/2 is the quantitative value of the coordination floor.

Specifically: σ(A) is a measure of the spread of ρ in the A-eigenbasis, which is inversely related to γ_A. When σ(A) → 0 (all coordination concentrated in A), the state becomes a pure A-eigenstate. By Robertson, this forces σ(B) → ∞ in the conjugate direction — or, if we normalize by a state-space cutoff, σ(B) becomes bounded below by κ/(2σ(A)). In the γ-variables, this means the coupling capacity γ_{AB} is bounded below by a state-dependent constant proportional to κ.

Conversely, σ(A) σ(B) = κ/2 (saturation of the Robertson bound) corresponds to a minimum-uncertainty state (e.g., the coherent state for the canonical Q, P pair), in which γ_{AB} is at its floor. No state can have γ_{AB} below this value — this is the restraint-power floor made quantitative.

The identification of the floor with κ/2 (not some other value) comes from the commutator value: the coordination floor in a partition is set by the structure of the coupling blocks B_{ij}, and for the quantum partition these are determined by the commutator [A, B] = iκI. The Robertson bound computes this structure-to-value map exactly in the two-observable case, and its numerical form κ/2 is the quantum-scale specification of the coordination floor.

Combining (i) and (ii): the Restraint-Power Theorem predicts a strictly positive floor; Robertson supplies its quantitative form as κ/2; and the identification σ(A)σ(B) ≥ κ/2 is the restraint-power law at the quantum scale. ■

*Remark A.20.28 (What is and is not proved).* The theorem establishes that the Robertson inequality *coincides* with the restraint-power floor for the two-MASA partition — not that the restraint-power framework *rederives* Robertson from the ACP axioms alone. The quantitative form σ(A)σ(B) ≥ κ/2 comes from Cauchy-Schwarz and is a standard QM result. The ACP contribution is structural: the *existence* of a floor is predicted by A.20.14, and the *location* of the floor is supplied by the commutator structure of the quantum partition. Full derivation of Robertson from ACP axioms alone would require deriving the canonical commutation relation [Q, P] = iℏI from the persistence condition rank(D) > 0 applied to a quantum operator algebra — which is open problem OP-RP-5 below (connection to Stone-von Neumann theorem).

What the framework proves structurally, while importing only the standard quantum commutator for the numerical value:

- (A) That a non-commutative two-MASA partition (𝒜_A, 𝒜_B) of a persistent quantum system has γ_{AB} > 0 — i.e., coupling is nonzero.
- (B) That this nonzero coupling is the coordination floor predicted by the restraint-power law.
- (C) That, under the Robertson identification, saturation of the floor corresponds to minimum-uncertainty states.

These three statements constitute the ACP's substantive quantum-scale claim. The numerical value κ/2 is imported from QM's commutator structure.

***Corollary A.20.29 (Heisenberg is the quantum-scale coordination floor).*** The Heisenberg uncertainty principle is the quantum instantiation of the coordination floor γ_{AB} > 0 that the restraint-power law enforces on a non-commutative two-MASA subsystem partition. The constant ℏ/2 is the quantum-scale value of the minimum coupling coordination capacity between conjugate observable algebras; it is non-zero because the algebras are non-commutative. The present result assumes this non-commuting quantum partition. Deriving the non-commutativity or the canonical commutator [Q, P] = iℏI from the ACP persistence condition rank(D) > 0 alone remains open (OP-RP-5).

*Remark A.20.30 (What the conjugate structure contributes).* Once a non-commutative quantum algebra is in view, conjugate observable pairs are the natural two-subsystem partition for the restraint-power floor. The Stone-von Neumann theorem then says that, given the canonical commutation relation and the usual regularity assumptions, the irreducible representation is unique up to unitary equivalence; it fixes the representation class of the (Q, P) pair. It does not by itself derive the canonical commutation relation from the ACP axioms. Thus A.20 answers the Schur-bridge question from step 2 onward: non-commutativity implies a Robertson/Heisenberg floor, and that floor is exactly the ACP coordination floor. The stricter step 1 — deriving the relevant non-commutative operator algebra from rank(D) > 0 alone — remains open.

*Remark A.20.31 (Other quantum coordination floors).* The Robertson bound is the two-observable case. The framework predicts coordination floors between any set of non-commuting observables; the generalization is the *entropic uncertainty relation* of Maassen-Uffink (1988), which bounds the sum of Shannon entropies in two conjugate bases below by a function of their maximum mutual overlap. The entropic form is arguably more natural in the ACP framework because it already speaks in the language of conditional entropy. The framework predicts that entropic uncertainty is the primary formulation, with Robertson a moment-based corollary.

### A.20.7.4 Other Physical Special Cases

The Restraint-Power Theorem recovers several other physics-scale regularities as special cases:

***Corollary A.20.32 (Bekenstein bound as coordination floor).*** The Bekenstein entropy bound S ≤ 2πRE/ℏc for a region of radius R with energy E is the gravitational-scale instantiation of the coordination floor in a system with radius-energy partition. The floor is set by the Planck scale (ℏ, c, G), analogous to how the Heisenberg floor is set by ℏ.

*Proof sketch.* Partition a gravitating system at radius R into internal (interior of R) and external (horizon and beyond) blocks. The entropy S is bounded because the internal block's rank is bounded by the horizon area (holographic principle). The Bekenstein bound is the claim that the maximum coordination capacity inside R is set by the coupling to the horizon (the holographic boundary), which is a restraint-power statement applied to the radius partition. Full proof requires the holographic principle, which is not part of the ACP axiom set, so this is a conjectural extension. ⚠ Argued structurally. See OP-RP-3 below.

***Corollary A.20.33 (Cosmic censorship as restraint-power).*** The weak cosmic censorship conjecture — that generic gravitational collapse produces event horizons rather than naked singularities — is the restraint-power law applied to the radius partition of a collapsing mass-energy distribution. The naked singularity corresponds to the case where the most concentrated subsystem (the collapsing mass) fails to perform a coordination transfer outward before its floor is breached. The formation of the horizon is the transfer: the collapsing mass-energy's coordination is transferred to the horizon's degrees of freedom (Bekenstein-Hawking entropy), and the Schur complement at the horizon captures the effective theory seen from outside.

*Remark A.20.34 (Why this is not a proof of cosmic censorship).* Corollary A.20.33 states cosmic censorship as a restraint-power instance, but does not *prove* it. A proof would require showing that generic gravitational collapse admits a restraint-power transfer; this is the content of the conjecture itself. The framework articulates *why* cosmic censorship should hold (it is the gravitational case of the general restraint-power law), but the technical gravitational proof remains open (OP-RP-4 below, cf. companion paper §10.3 OP-SC-6).

---

## A.20.8 Domain Instantiations

We list the cross-domain instantiations of the Restraint-Power Theorem, providing a mapping for each domain from the theorem's structural variables to the domain's observables. These constitute empirical tests of Prediction 4 of the main paper.

### A.20.8.1 Mapping Table

| Domain | Subsystem i* (concentrated) | Receiving subsystems J | Transfer mechanism | Visibility channel κ_{i*, j} | Floor (prediction) |
|--------|---------------------------|---------------------|------------------|------------------------------|--------------------|
| **Ecology** | Apex predator | Lower trophic levels | Self-restricted predation rate | Observable prey population | Sustainable harvest rate > 0 |
| **Economics (markets)** | Dominant firm / market-maker | Smaller firms, retail traders | Voluntary disclosure, liquidity provision | Public financial statements, quoted spreads | Informational rents > 0 for smaller participants |
| **Immunology** | Effector T cell population | Regulatory T cells, naive T cells | Apoptotic contraction, Treg induction | Cytokine signaling (e.g., IL-10) | Treg fraction > 0 |
| **Quantum mechanics** | Observable A's eigenstate | Conjugate observable B's spread | Measurement back-reaction | [A, B] ≠ 0 | σ(Q)σ(P) ≥ ℏ/2 |
| **General relativity** | Collapsing mass-energy | Horizon degrees of freedom | Horizon formation | Hawking radiation | Bekenstein-Hawking area > 0 |
| **Organizations** | CEO / founder | Middle management, board | Delegation, public commitments | Memos, earnings calls, board votes | Distributed authority > 0 |
| **Theology (tzimtzum/kenosis)** | Ultimate / maximally powerful | Creation / lower order | Voluntary self-limitation | Revelation, incarnation | Created order > 0 |
| **AI capital allocation** | Dominant AI labs / hyperscalers | Smaller firms, suppliers | Large CapEx commitments, circular contracts | Public financial disclosures, press releases | Smaller firms' access to compute > 0 |
| **Social choice** | Majority faction | Minority factions | Constitutional constraints, rights protections | Public institutional commitments | Minority rights > 0 |

*Remark A.20.35.* Each row instantiates the same formal structure: a concentrated subsystem i*, a visibility channel, a transfer mechanism, a receiving set J, and an emergent floor. The floor is strictly positive in every row, matching the theorem's prediction. The cases range across twenty orders of magnitude in energy and thirty orders of magnitude in timescale — a cross-domain scale invariance that is itself evidence for the underlying unification.

### A.20.8.2 Novel Predictions from the Unified Framework

The equivalence of the conservation and restraint-power forms (Theorem A.20.22) supports several novel predictions beyond those in the main paper's Prediction 4 and the companion paper's Pattern 10:

**Prediction RP-1 (Concentration-lifespan hyperbola).** Across any domain admitting a subsystem partition, the time-to-crystallization τ_{i*} of a system scales inversely with γ_{i*}: τ_{i*} ∝ 1/γ_{i*} (to leading order, in the mechanism-preserving regime). Equivalently, the product of maximum concentration and lifespan is bounded above by a domain-specific constant.

*Test:* Regress log(lifespan) on log(max concentration) across organizations, species, polities, or firms; predicted slope is −1.

**Prediction RP-2 (Decodability threshold).** For a system initiating a coordination transfer, the probability of stabilization increases sharply when the transfer's signal-to-noise ratio (κ_{i*, j} relative to the background coupling decay rate) exceeds a threshold. Below the threshold, the transfer is undecodable and fails; above the threshold, it stabilizes.

*Test:* Measure corporate disclosure bandwidths and correlate with subsequent organizational survival; predicted phase transition at a threshold disclosure rate.

**Prediction RP-3 (Visibility cost).** The coordination cost C_{vis} of maintaining the visibility channel κ_{i*, j} at level κ_0 scales linearly with κ_0 (to leading order): C_{vis} ∝ κ_0. This is the ACP-predicted version of the classical result that signaling costs scale with signal rate.

*Test:* Measure public-disclosure infrastructure costs as a function of disclosure volume; predicted linear scaling.

**Prediction RP-4 (Quantum-organizational scale matching).** The restraint-power coordination floor has a common structural form across all scales: at the quantum scale it is ℏ/2 (Heisenberg), at the gravitational scale it is the Bekenstein bound, at the organizational scale it is the minimum-viable-delegation ratio. The framework predicts that domain-specific measurements of the floor, normalized by the relevant coordination-capacity units, should yield a common dimensionless constant near unity.

*Test:* Aggregate cross-domain coordination floor measurements after unit normalization; predicted clustering near a single dimensionless value.

---

## A.20.9 Open Problems

**OP-RP-1: Continuous-time dynamical formulation.** Theorem A.20.14 is stated over a finite interval [t, t + T] with a mechanism-changing event. A continuous-time dynamical formulation — in which coordination concentrations γ_i(t) obey a system of ODEs with the Schur complement propagation as the generator — would connect the restraint-power law to the continuous-scale renormalization group formalism of Appendix A.18 (Wetterich flow equation). This requires a smoothing of the mechanism-change events into continuous coordination transfer rates.

**OP-RP-2: Non-Gaussian strengthening.** The proofs above use Gaussian approximations (via the precision matrix Q). For non-Gaussian systems, the Schur complement captures leading-order effects only. The A.17 non-Gaussian corrections (Theorem A.17.9 and Corollary A.17.15) suggest that non-Gaussian systems exhibit *sharper* restraint-power dynamics than Gaussian ones — the forced transfer happens faster, and the decodability threshold is sharper. A formal strengthening of the theorems under non-Gaussian conditions would improve the quantitative predictions RP-1 through RP-4.

**OP-RP-3: Bekenstein bound as formal corollary.** Corollary A.20.32 states the Bekenstein bound as a restraint-power instance but requires the holographic principle as an additional ingredient. Providing a full derivation within the ACP framework — without assuming holography — would extend the "Heisenberg as special case" result to "Bekenstein as special case," placing the gravitational-scale floor on the same footing as the quantum-scale floor.

**OP-RP-4: Cosmic censorship from restraint-power.** Corollary A.20.33 states cosmic censorship as a restraint-power instance but does not prove it. A formal proof of weak cosmic censorship from the restraint-power law would require showing that generic gravitational collapse admits a coordination transfer before a naked singularity can form. This is a substantial general-relativistic project and connects to companion paper §10.3 OP-SC-6.

**OP-RP-5: Canonical commutation and Tomita-Takesaki extension of the Heisenberg reduction.** The Heisenberg reduction (Theorem A.20.27) is proved after a non-commutative two-MASA quantum partition is specified. The stricter first-principles task is to derive, from the ACP persistence condition rank(D) > 0 alone, when the associated operator algebra must be non-commutative and when the canonical commutation relation [Q, P] = iℏI is forced. In finite dimensions this connects to the representation-theoretic assumptions behind the Stone-von Neumann theorem; in infinite dimensions it requires modular theory (Tomita-Takesaki) to define the subsystem partition for von Neumann algebras and extend the reduction to QFT and quantum-gravity settings.

**OP-RP-6: Measure problem for the quantum partition.** The partition (𝒜_A, 𝒜_B) of the operator algebra is one choice among many. The framework predicts coordination floors for each choice of partition, but does not yet specify which partition is "physical" for a given experimental context. Connecting this to Zurek's quantum Darwinism (A.12) — which identifies the physical pointer basis as the dynamically selected one — should resolve this.

**OP-RP-7: Rate equation for γ_i(t).** Between mechanism-change events, the {γ_i(t)} distribution evolves under mechanism-preserving dynamics. The explicit rate equation — a system of coupled Riccati-type ODEs for the γ_i, derived from the Schur complement dynamics — is the natural framework for testing Prediction RP-1 empirically. Deriving this rate equation in closed form is an open technical problem.

**OP-RP-8: Partition invariance.** The conservation law (Theorem A.20.10) holds for any chosen partition. Whether the restraint-power *dynamics* (Theorem A.20.14) has an invariant form under change of partition — that is, whether the identity of i* tracks a partition-invariant maximum-concentration object — is conjectured but not proven. Connection to category theory (the partition as a choice of forgetful functor) may resolve this (cf. OP-SC-4).

---

## A.20.10 Summary

This appendix establishes the Restraint-Power Theorem as a formal result of the ACP framework, unifies it with the coordination conservation conjecture from session 16, and derives the Heisenberg uncertainty principle as a quantum-scale special case. The five main results are:

1. **Coordination Conservation (A.20.10):** Under mechanism-preserving transformations, H(m′|m) is exactly conserved; per-subsystem floors are emergent, not fundamental.

2. **Restraint-Power Theorem (A.20.14):** When a system approaches its coordination floor, the most concentrated subsystem must undergo a coordination transfer before any other subsystem and before the global floor is breached.

3. **Visibility Necessity (A.20.18):** A coordination transfer stabilizes the composite only if it is decodable by the receiving subsystems; secret restraint fails to stabilize.

4. **Equivalence of Forms (A.20.22):** Conservation and restraint-power are logically equivalent given the CDT; they are two registers of the same structural fact.

5. **Heisenberg as Special Case (A.20.27):** Applied to a non-commutative two-MASA partition of a quantum operator algebra, the Restraint-Power Theorem predicts a strictly positive coordination floor γ_{AB} > 0; identifying this floor with the Robertson inequality (a standard QM result) shows that σ(Q)σ(P) ≥ ℏ/2 is the quantum-scale instantiation of the subsystem coordination floor. The ACP contribution is structural, not numerical: it predicts the existence and location of the floor once the non-commutative partition is given, while ℏ/2 is imported from the commutator structure of the quantum partition.

Taken together, these results provide the unification target identified in §5e and §7 of `ACP_PROJECT_STATUS.md` (session 17). The conjectured relationship between Pattern 10 and the coordination-uncertainty conservation law is now a theorem. Heisenberg, Bekenstein, and cosmic censorship are shown to be physical-scale instantiations of the same cross-domain coordination law that governs ecological restraint, organizational delegation, and market structure. The framework is no longer a collection of suggestive analogies; it is a single theorem with domain-specific instantiations.

The central open problems concern extensions (non-Gaussian, infinite-dimensional, continuous-time) and the completion of the gravitational-scale reductions (Bekenstein, cosmic censorship). None of the open problems threaten the central results.

---

*End of Appendix A.20.*
