**A Pattern Hiding in Plain Sight**

Evidence That Independent Research Programs Have Discovered

the Same Universal Persistence Principle

A Synthesis of Existing Results

March 2026  •  Working Draft

*“If you can measure it, consider it predicted.”*

— Peter Cotton

# **Abstract**

This paper assembles results from eight independent research programs—none of which cites the others on the relevant points—and argues that they have discovered the same structural principle. The principle: a dynamical system persists if and only if its information-processing capacity grows at least as fast as its complexity load. This condition appears as formal theorems in information theory (Shannon, 1948), cybernetics (Ashby, 1956), quantum error correction (Aharonov–Ben-Or, 1999), non-equilibrium thermodynamics (Prigogine, 1977), and as the covariant entropy bound in cosmology (Bousso, 1999). It appears as Nobel Prize–winning empirical frameworks in ecology (Holling, 1973) and institutional economics (Ostrom, 1990). It appears in sharpened form in quantum mechanics, where entropic uncertainty relations place a direct floor on Shannon entropy across incompatible observables (Maassen–Uffink, 1988). Recent thermodynamic work upgrades Ashby’s law from requisite variety to requisite complexity: efficient adaptive agents must carry internal structure rich enough to mirror the structure of their environment (Boyd, Mandal, and Crutchfield, 2017, 2018). Recent geometric work further suggests that quantum uncertainty, thermodynamic uncertainty, and finite dynamical speed are aspects of a single bound (Hasegawa, 2023). A single algebraic operation—the Schur complement—implements this condition across every domain where the correspondence has been checked, from Gaussian conditioning to renormalization group decimation to portfolio optimization (Cotton, 2024). Category theory confirms this is not coincidence: in the categories where open quadratic systems live, the Schur complement literally is composition (Stein, Zanasi, Piedeleu, Samuelson, 2025). Furthermore, the mathematical ingredients required to derive the uncertainty principle from pure persistence requirements already exist in the published literature—Tomita–Takesaki, Robertson, Maassen–Uffink, Stone–von Neumann, Groenewold–van Hove, Gromov, and Hasegawa—but no one has assembled the chain. This paper does not propose a new framework. It reads existing results side by side and asks what they say together that they have not yet said apart.

Keywords: persistence, Schur complement, uncertainty principle, entropic uncertainty, requisite complexity, Shannon capacity, dissipative structures, viability theory, convergent discovery, algebraic universality, microprediction

# **1. Introduction**

This paper makes one claim: that the existing scientific literature already contains a universal persistence principle, hiding in plain sight across disciplinary boundaries. No new framework is proposed. No new formalism is introduced. Every result cited belongs to someone else. The contribution is purely one of synthesis—reading established results side by side and noticing that they are structurally identical.

The principle can be stated in one sentence: *a system persists if and only if its capacity to process information meets or exceeds the rate at which complexity threatens to overwhelm it.* Call this the persistence threshold. It appears as C ≥ R in Shannon’s channel capacity theorem. As V(controller) ≥ V(system) in Ashby’s Law of Requisite Variety. As correction rate ≥ error rate in fault-tolerant quantum computation. As entropy export ≥ entropy production in Prigogine’s steady-state condition. As S ≤ A/4G in Bousso’s covariant entropy bound. As ΔQ·ΔP ≥ ħ/2 in the Heisenberg uncertainty principle. These are not analogies. Several are provably the same mathematical inequality in different notation.

The paper proceeds as follows. Section 2 documents the convergent discoveries. Section 3 identifies the single algebraic operation—the Schur complement—that implements the persistence threshold across all checked domains. Section 4 shows that the mathematical ingredients for a derivation of the uncertainty principle from pure persistence requirements already exist in the published literature. Section 5 surveys the inference-first physics programs that recast physical law as optimal prediction under constraints. Section 6 provides an honest accounting of what is established, what is suggestive, and what remains open. Section 7 asks what the conjunction implies.

# **2. The Convergent Discoveries**

What follows is a domain-by-domain accounting of where the persistence threshold lives in existing literature. The emphasis throughout is on results that are mathematically precise, not on vague analogies.

## **2.1 Shannon’s Channel Capacity (1948)**

Shannon proved that reliable communication over a noisy channel is possible if and only if the transmission rate R stays below the channel capacity C. Wolfowitz’s strong converse (1957) sharpened this to a knife-edge: C is a sharp threshold between perfectly reliable and completely unreliable communication. Reframed: the system’s information-processing capacity must meet or exceed the demands placed upon it, or the system fails catastrophically, not gradually. The Shannon–Hartley formula C = B·log₂(1 + S/N) embeds the persistence structure directly: bandwidth B acts as hard constraint, codebook design matched to channel statistics provides alignment, and error-correcting codes supply redundancy that lets the message survive noise. Rate-distortion theory (Shannon, 1959) formalizes the necessity of controlled information loss—proportional release—to keep encoding viable.

## 2.2 From Requisite Variety to Requisite Complexity

Ashby’s law—often called the First Law of Cybernetics—states: “Only variety can absorb variety.” A controller must possess at least as many response states as the system it regulates: V(controller) ≥ V(system). Conant and Ashby’s Good Regulator Theorem (1970) proved that any effective autonomous controller must contain an internal model of its environment. Later thermodynamic work sharpens the point. Boyd, Mandal, and Crutchfield showed first in Journal of Statistical Physics (2017) and then more generally in Physical Review X (2018) that adaptive information ratchets extract work efficiently only when their internal memory mirrors the temporal and structural complexity of the environment. The surviving requirement is therefore stronger than requisite variety alone: persistence demands requisite complexity.

## **2.3 Prigogine’s Dissipative Structures (1977)**

Prigogine demonstrated that systems far from equilibrium persist not despite continuous exchange with the environment but because of it. The steady-state condition requires entropy export to meet or exceed internal entropy production. Landauer’s principle (1961, experimentally verified by Bérut et al. in *Nature*, 2012) adds a thermodynamic floor: erasing one bit of information requires dissipating at least kBT ln 2 of energy. This makes release not merely useful but physically mandatory. Every irreversible computation demands proportional dissipation.

## **2.4 Holling’s Adaptive Cycle (1973)**

C. S. Holling’s adaptive cycle, formalized with Gunderson in *Panarchy* (2002), comes closest to anticipating the full persistence structure. The cycle has four phases: exploitation/growth (r), conservation (K), release (Ω), and reorganization (α). Holling stated explicitly that “processes of destruction and reorganization are often neglected in favor of growth and conservation”—release is the overlooked essential. The nested panarchy framework shows these cycles operating across scales, with cross-scale interactions maintaining system coherence.

## **2.5 Ostrom’s Design Principles (1990)**

Elinor Ostrom’s eight design principles for enduring institutions (Nobel Prize, 2009) map onto the persistence structure with striking fidelity. Clearly defined boundaries (Principle 1) must come first—no coordination is possible without knowing who is in and who is out. Proportional equivalence between costs and benefits (Principle 2) and collective-choice arrangements (Principle 3) provide coordination. Monitoring (Principle 4) and graduated sanctions (Principle 5) ensure continuation. The graduated nature of sanctions is particularly telling: not expulsion but calibrated response—proportional release. Ostrom studied institutions that survived for centuries and found these principles present in every case.

## **2.6 Quantum Error Correction Threshold (1999)**

Aharonov and Ben-Or’s threshold theorem for fault-tolerant quantum computation states: quantum computation succeeds if and only if the error correction rate exceeds the error generation rate. Measurement-induced phase transitions (MIPTs), first characterized by Skinner, Ruhman, and Nahum (2019), reveal the same threshold as a physical phase transition in quantum many-body systems. Below critical measurement rate pc, entanglement entropy scales as system volume—information keeps pace with complexity. Above pc, entanglement collapses to area-law scaling—information fails to keep pace and coherence is destroyed. Choi et al. (2020) proved this transition is equivalent to a quantum error correction threshold. Gullans and Huse (2020) showed the system projects into an optimal code achieving channel capacity.

## **2.7 The Heisenberg Uncertainty Principle (1927)**

The canonical commutation relation [Q, P] = iħ and the resulting Robertson inequality ΔQ·ΔP ≥ ħ/2 are conventionally treated as axioms of quantum mechanics. But the entropic uncertainty relation of Maassen and Uffink (1988) is the stronger fit for the present argument: it places a lower bound directly on the sum of Shannon entropies for incompatible observables. Read structurally, the point is not merely that conjugate variables have finite variances, but that a persistent system retains an irreducible floor of informational spread. As Section 4 argues, the mathematical ingredients for deriving that floor from persistence requirements alone already exist in the published literature. The uncertainty principle may not be an independent postulate. It may be the quantum-mechanical face of the same threshold that Shannon, Ashby, and Prigogine found in their own domains.

## **2.8 Bousso’s Covariant Entropy Bound (1999)**

For any light-sheet generated from a surface of area A, the entropy satisfies S ≤ A/4G. When this bound is violated—as near classical singularities—the spacetime becomes non-viable. Loop quantum cosmology (Ashtekar et al., 2008) showed that quantum geometry effects resolve singularities precisely by restoring respect for the Bousso bound. The Quantum Focusing Conjecture (Bousso et al., 2015) implies the Quantum Null Energy Condition, a proportionality between energy density and entropy change that must hold for spacetime viability.

## **2.9 The Pattern**

Three features of this convergence deserve emphasis. First, the proportionality requirement is mathematically precise in at least four cases—Shannon, Ashby, QEC, Prigogine—where it can be shown to be the same mathematical inequality in different notation. Second, the constraint-first ordering (boundaries before coordination, constraint before expansion) is enforced across every domain, from Penrose’s Weyl Curvature Hypothesis to Ostrom’s Principle 1 to qubit initialisation requirements. Third, the necessity of release—dissipation, creative destruction, measurement, forgetting—is consistently present but consistently underemphasised. Landauer’s principle makes it physically mandatory. Holling argued it is neglected. Schumpeter called it essential. Apoptosis won a Nobel Prize. The pattern is hidden not because it is absent from the literature but because disciplinary boundaries prevent its recognition as universal.

# **3. The Algebraic Invariant: The Schur Complement**

If the persistence threshold is truly a single principle appearing in different domains, there should be a single mathematical operation that implements it. There is.

## **3.1 One Formula, Many Names**

The Schur complement of block D in a partitioned matrix M = [[A, B], [C, D]] is M/D := A − BD⁻¹C. This operation answers a universal question: given a system with internal and boundary degrees of freedom, what is the effective behavior on the boundary after the internal degrees of freedom have been eliminated? It appears under different names:

| **Domain** | **Name** | **Rigour** | **Reference** |
| --- | --- | --- | --- |
| Statistics | Gaussian conditioning Cov(X│Y) | Exact identity | Textbook |
| Networks | Kron reduction of Laplacian | Exact identity | Dörfler–Bullo (2013) |
| Quantum mechanics | Feshbach–Schur map | Formal theorem | Feshbach (1958) |
| Quantum field theory | Free-field RG decimation | Exact identity | Butera–Meineri (1995) |
| PDE theory | Dirichlet-to-Neumann map | Exact identity | Ingerman (2008) |
| Portfolio optimization | Schur complementary allocation | Exact identity | Cotton (2024) |
| Category theory | GQA composition | Complete theory | Stein et al. (2025) |
| Bayesian inference | Belief propagation messages | Exact identity | MIT 6.438 |
| Cosmological estimation | Marginalised Fisher information | Exact identity | Taylor–Kitching (2010) |

## **3.2 Cotton’s Schur Complementary Portfolios**

Cotton’s 2024 result deserves particular attention because it demonstrates the Schur complement operating as a prediction-optimization tool in a domain—financial markets—far removed from physics. His “Schur Complementary Allocation” paper shows that parameterizing the amount of Schur complement information included (via a parameter γ ∈ [0, 1]) smoothly interpolates between Hierarchical Risk Parity (γ = 0, ignoring off-diagonal covariance information) and full Markowitz optimization (γ → 1, using all available information). Gavidia-Calderón et al. (2025) subsequently provided a rigorous mathematical unification, proving the equivalence formally via Sierpiński graph structures.

The financial interpretation is structurally identical to the physical one. In physics, the Schur complement eliminates internal degrees of freedom to yield effective boundary behavior. In portfolio optimization, it eliminates intra-cluster asset correlations to yield effective inter-cluster risk allocation. In both cases, the operation answers the same question: what is the optimal prediction of boundary behavior given that internal structure has been compressed away? Cotton’s broader research program—microprediction (MIT Press, 2022)—makes this connection explicit. His dictum “if you can measure it, consider it predicted” treats prediction as ontologically primary, not as a tool applied to a pre-existing reality. Markets, in this view, are not prediction mechanisms applied *to* the world. They are the world’s prediction structure, compressed and made tradeable.

## **3.3 Categorical Confirmation**

Category theory confirms that the Schur complement’s universality is not coincidence but structural necessity.

To make the slogan precise, we pass to the semantic framework of Stein, Zanasi, Piedeleu, and Samuelson, where GQA axiomatizes quadratic relations and Gaussian processes compositionally; in that setting, the claim that “composition is Schur complementation” becomes an exact statement about composition in QuadRel.

**Proposition 3.1 (Composition as Schur elimination in QuadRel****reg****).**

Let QuadRelreg be the wide sub-PROP of QuadRel whose morphisms m → n are everywhere-finite quadratic forms

f(x,y) = ½ [x; y]ᵀ Q_f [x; y] + ℓ_fᵀ [x; y] + c_f,    with Q_f ∈ Sym_{m+n}(ℝ) positive semidefinite.

For composable morphisms f : m → k and g : k → n, write

Q_f = [A  B; Bᵀ  D_f],    Q_g = [D_g  C; Cᵀ  E],    ℓ_f = (a, d_f)ᵀ,    ℓ_g = (d_g, e)ᵀ.

Set D := D_f + D_g, and form the glued quadratic datum on ℝ^m ⊕ ℝ^k ⊕ ℝ^n:

K = [A  B  0; Bᵀ  D  C; 0  Cᵀ  E],    λ = (a, d_f + d_g, e)ᵀ.

If D is invertible, then the composite g ∘ f in QuadRel is the quadratic form on ℝ^m ⊕ ℝ^n with

Q_{g ∘ f} = K / D,

ℓ_{g ∘ f} = (a, e)ᵀ − [B; Cᵀ] D⁻¹ (d_f + d_g),

c_{g ∘ f} = c_f + c_g − ½ (d_f + d_g)ᵀ D⁻¹ (d_f + d_g),

where K / D denotes the Schur complement of the internal block D in K. Hence sequential composition in QuadRelreg is exactly Schur complementation of the glued internal block.

*Proof. *By definition of composition in QuadRel,

(g ∘ f)(x,y) = inf_z { f(x,z) + g(z,y) }.

Set u := (x,y) and v := z. Then

f(x,z) + g(z,y) = ½ [u; v]ᵀ [P  R; Rᵀ  D] [u; v] + (p, d)ᵀ [u; v] + (c_f + c_g),

where

P = [A  0; 0  E],    R = [B; Cᵀ],    p = (a, e)ᵀ,    d = d_f + d_g.

Completing the square in v gives

inf_v { ½ vᵀ D v + (Rᵀ u + d)ᵀ v } = − ½ (Rᵀ u + d)ᵀ D⁻¹ (Rᵀ u + d).

Substituting back yields

(g ∘ f)(u) = ½ uᵀ (P − R D⁻¹ Rᵀ) u + (p − R D⁻¹ d)ᵀ u + c_f + c_g − ½ dᵀ D⁻¹ d.

Since P − R D⁻¹ Rᵀ = K / D, the Hessian of the composite is the Schur complement of D in K.

**Remark 3.2 (Partial case).**

Without the regularity assumption, composition in QuadRel uses the Moore–Penrose pseudoinverse D+, yielding the generalized Schur complement together with a support constraint:

(g ∘ f)(u) = ½ uᵀ (P − R D⁺ Rᵀ) u + (p − R D⁺ d)ᵀ u + c_f + c_g − ½ dᵀ D⁺ d + ι_{im(D)}(Rᵀ u + d).

Equivalently, sequential composition in QuadRel is elimination of the internal interface variable by infimal convolution; in quadratic coordinates, this elimination is generalized Schur complementation.

**Corollary 3.3 (Gaussian maps).**

Let L : Gauss → QuadRel be the faithful functor of Stein, Zanasi, Piedeleu, and Samuelson sending each Gaussian map to its negative conditional log-density. Then composition in Gauss becomes Schur complementation of the internal precision block after applying L. Thus the Schur complement governs Gaussian composition not in raw covariance coordinates, but in precision coordinates, where the categorical semantics are exact.

This exact identification sits within a wider categorical landscape. Baez and Fong’s compositional framework for passive linear networks (2018) defines a black-box functor from open circuits to Lagrangian linear relations. This functor “forgets internal structure and remembers only external behavior” and thereby computes the Kron reduction, which is the Schur complement. Fritz’s synthetic approach to Markov kernels (2020) axiomatizes conditioning within Markov categories; in Gaussian Markov categories, the concrete realisation of that categorical conditioning operation is again the Schur complement.

What the categorical results show, in precise form, is that elimination of internal degrees of freedom is not a domain-specific trick but the common operation by which effective behavior is computed across the programs surveyed here.

## **3.4 The Gaussian Boundary**

That common elimination picture has a clear boundary: its exact form is Gaussian, free, and quadratic. For interacting (non-Gaussian) theories, the Schur complement provides the zeroth-order structure around which perturbative corrections are organized. Koch-Janusz and Ringel (*Nature Physics*, 2018) showed that optimal RG coarse-graining maximizes real-space mutual information; for Gaussians, this reduces to Schur complementation. Whether a non-Gaussian generalization of the Schur complement can unify the program beyond the quadratic regime remains genuinely open. A 2025 preprint establishing the semigroup property of the smooth Feshbach–Schur map (Bach, Ballesteros, Fröhlich) suggests the program is advancing, but the complete non-Gaussian theory does not yet exist.

# **4. The Latent Derivation**

The most provocative claim of this paper is not about convergent discovery or algebraic invariance. It is this: *the mathematical ingredients required to derive the Heisenberg uncertainty principle from pure persistence requirements already exist in the published literature.* No one has assembled the chain. But every link is a proven theorem.

## **4.1 The Chain**

**Link 1: Nontrivial dynamics requires noncommutativity.** Tomita–Takesaki modular theory (1970) shows that for commutative von Neumann algebras, every faithful normal state is tracial, forcing the modular automorphism to be trivial. If physical time evolution is identified with or constrained by modular flow (Connes–Rovelli, 1994), commutativity forces trivial evolution. A system that *does something* must have a noncommutative observable algebra. Independently, the Heisenberg equation dO/dt = (i/ħ)[H, O] shows that commutativity makes all expectation values constant.

Link 2: Noncommutativity implies uncertainty bounds. Robertson’s inequality (1929) is pure Hilbert space mathematics: for any noncommuting self-adjoint A, B and any state |ψ⟩, ΔA·ΔB ≥ ½|⟨ψ|[A,B]|ψ⟩|. No physics is required. Maassen and Uffink (1988) sharpened this in information-theoretic form, placing a lower bound directly on the sum of Shannon entropies for incompatible observables. Recent work by Hasegawa (2023) goes further still, showing that quantum speed limits, thermodynamic uncertainty relations, and Heisenberg-type bounds can be understood as aspects of a common geometric constraint via a bulk–boundary correspondence. That result does not complete the persistence derivation, but it places the missing bridge on the published map.

**Link 3: Persistence forces conjugate structure.** Stone–von Neumann uniqueness (1931) shows that Weyl relations have a unique irreducible representation. If the dynamics forces the existence of a canonical pair Q, P satisfying [Q, P] = iκI with κ ≠ 0, then the uncertainty relation ΔQ·ΔP ≥ κ/2 follows immediately from Link 2.

**Link 4: The noncommutativity is irremovable.** The Groenewold–van Hove theorem (1946) proves that no consistent quantisation map exists from Poisson brackets to commutators for polynomials of degree ≥ 4. The noncommutative structure cannot be deformed away. This is not a practical obstacle but a mathematical impossibility.

**Link 5: Symplectic rigidity.** Gromov’s non-squeezing theorem (1985)—sometimes called the “principle of the symplectic camel”—shows that symplectic capacity is preserved under Hamiltonian flow. De Gosson (2003, 2009) connected this to quantum mechanics: the covariance ellipsoid of a quantum state must have symplectic capacity ≥ ½ħ. States below this threshold do not exist. This is a geometric rigidity result that follows from the mathematics of symplectic manifolds, not from quantum postulates.

## **4.2 What Is Missing**

Each link above is a proven theorem. What is missing is the bridge between them—specifically, a proof that the three conditions (nontrivial dynamics, finite energy, state distinguishability) jointly force the existence of a canonical conjugate pair Q, P with [Q, P] = iκI. The mathematical tools exist: the Antonescu–Christensen construction of spectral triples on noncommutative algebras, the Bertozzini–Conti–Lewkeeratiyutkul reconstruction theorems, and the theory of symplectic leaves in noncommutative geometry. But the assembly—the explicit proof that these three *minimal* conditions force the full Heisenberg structure—has not appeared in the published literature as of this writing. The chain is latent. Its completion would constitute a derivation of the uncertainty principle from persistence alone.

## **4.3 The Thermodynamic Analogy**

If this derivation exists, it operates at the thermodynamic level—structural constraints on what kinds of systems can persist—rather than the statistical-mechanical level—microscopic mechanisms that generate quantum behavior. The analogy is precise: thermodynamics derives the form of PV = NkT from statistical considerations, while the value of Boltzmann’s constant k requires connecting temperature to energy via experiment. A persistence derivation would determine the *form* of the uncertainty principle (ΔQ·ΔP ≥ κ/2, κ > 0, irremovable) but not its *value* (κ = ħ). The value requires one empirical measurement. The structure follows from the requirement that something continues to exist.

# **5. The Inference-First Programs**

Independently of the convergent discoveries in Section 2 and the algebraic program in Section 3, a growing body of work recasts physical law itself as optimal prediction under constraints. These programs provide the conceptual bridge between the Schur complement as algebra and the persistence threshold as physics.

## **5.1 Caticha’s Entropic Dynamics**

Caticha’s program (2011–2018) derives Einstein’s vacuum field equations from information geometry. Physical space is modeled as a set of distinguishable points with finite resolution; its geometry is given by the Fisher information metric. The Hojman–Kuchař–Teitelboim deformation algebra—which encodes the embeddability constraints of spatial slices in spacetime—then forces Einstein’s equations. The Fisher information matrix of a marginal distribution (after eliminating hidden variables) is the Schur complement of the full Fisher matrix. If spacetime is a statistical manifold, then the effective spacetime metric after coarse-graining is the Schur complement of the microscopic Fisher metric. This connects directly to the algebraic program of Section 3.

## **5.2 Jacobson–Verlinde Thermodynamic Gravity**

Jacobson (1995) derived Einstein’s field equations from the proportionality of entropy to horizon area together with the Clausius relation δQ = T dS, applied to local Rindler horizons. Verlinde (2011) extended this to an entropic force framework. Padmanabhan developed the program further, showing gravitational field equations emerge as thermodynamic identities. A newer and more speculative arrival is Bianconi’s Gravity from Entropy (2025), which derives a gravitational action from the quantum relative entropy between the spacetime metric and the metric induced by matter fields, recovering Einstein’s equations in a low-coupling limit. Because that program is recent and not yet settled consensus, it should be read as convergent evidence rather than closure. In all these approaches, gravity is not a fundamental force but an effective description of how degrees of freedom organize when internal structure is eliminated—the physical counterpart of the Schur complement operation.

## **5.3 Friston’s Free Energy Principle**

Friston’s Free Energy Principle (FEP; 2010) identifies biological self-organization with variational free energy minimization on a Markov blanket. For Gaussian generative models, the FEP’s prediction errors are precision-weighted by inverting block submatrices of the joint precision matrix—algebraically, Schur complement operations. Predictive coding, the process theory of the FEP, is built on iterated Schur complementation of hierarchical precision matrices. Fields and Friston (2022) argued that the FEP extended to fundamental physics is asymptotically equivalent to unitarity. Addazi et al. (2021) derived gauge invariance and Poincaré symmetry from Markov blanket conditions, arriving at Einstein gravity. Friston acknowledges the FEP is “so simple that it is (almost) tautological”—but as he notes, this is true of any variational principle, including Hamilton’s principle of stationary action.

## **5.4 Cotton’s Microprediction**

Cotton’s *Microprediction* (MIT Press, 2022) approaches the same territory from the market side. Cotton argues that microprediction—repeated quantitative prediction tasks—is the fundamental operation underlying what is conventionally called AI, and that market-inspired mechanisms for distributing prediction are likely to outperform centralised approaches. His “Indispensable Markets Hypothesis” argues that prediction markets can be indispensable yet not perfectly efficient—structurally identical to the Grossman–Stiglitz paradox (1980), which proved that perfectly efficient markets are impossible because no one would have incentive to gather the information that makes markets efficient. The irreducible inefficiency is not a bug. It is required for the market to function. This is the economic instantiation of the uncertainty principle: the gap cannot be closed without destroying the system that requires it.

Cotton’s dictum—“if you can measure it, consider it predicted”—inverts the conventional relationship between measurement and prediction. Measurement does not precede prediction; prediction structure is what makes measurement possible. This is perhaps the most compressed expression of the principle this paper has assembled from eight independent sources: prediction is not what agents do before they look. It is what systems are before agents arrive.

## **5.5 QBism**

QBism (Fuchs, Schack) treats quantum mechanics as an agent’s optimal belief-update calculus—the normative rules for a Bayesian agent interacting with the world under irreducible uncertainty. The Born rule becomes a consistency requirement on betting probabilities. Measurement is not state collapse but belief revision. If the persistence threshold is real, QBism describes how an agent navigates a world structured by it: the rules of quantum mechanics are the rules for optimal prediction within the uncertainty floor that persistence requires.

# **6. Honest Accounting**

The following table catalogs what is established, what is suggestive, and what is open.

## **6.1 Established Beyond Dispute**

| **Claim** | **Source** |
| --- | --- |
| Shannon capacity is a sharp persistence threshold | Shannon (1948), Wolfowitz (1957) |
| V(controller) ≥ V(system) for viable regulation | Ashby (1956) |
| Erasure costs k₂T ln 2 per bit (dissipation mandatory) | Landauer (1961), Bérut (2012) |
| Commutative algebras have trivial modular flow | Tomita–Takesaki (1970) |
| ΔA·ΔB ≥ ½│⟨[A,B]⟩│ for noncommuting observables | Robertson (1929) |
| Entropic uncertainty places a lower bound on Shannon entropy for incompatible observables | Maassen–Uffink (1988) |
| Poisson → commutator map fails for deg ≥ 4 | Groenewold (1946) |
| Symplectic capacity ≥ ½ħ for quantum covariance | de Gosson (2003, 2009) |
| Symplectic capacity preserved under Hamiltonian flow | Gromov (1985) |
| Schur complement = Gaussian conditioning | Textbook |
| Schur complement = Kron reduction | Dörfler–Bullo (2013) |
| GQA composition = Schur complement | Stein et al. (2025) |
| Schur complement = portfolio interpolation parameter | Cotton (2024), Gavidia-Calderón (2025) |
| MIPT = QEC threshold | Choi et al. (2020) |
| Entropy → Einstein equations via Clausius relation | Jacobson (1995) |

## **6.2 Suggestive but Not Yet Proven**

| **Claim** | **Gap** |
| --- | --- |
| Eight domain-specific thresholds are one principle | No single proof; structural argument only |
| Thermodynamic Ashby strengthens requisite variety toward requisite complexity | Ratchet results are published and established; the full persistence-theorem generalization remains open |
| Heisenberg, TURs, and quantum speed limits may share a geometric bound | Published and real; the persistence-derivation reading is not yet mainstream |
| Schur complement extends to non-Gaussian theories | Exact for quadratic; perturbative otherwise |
| Persistence axioms force conjugate pairs | All links proven; assembly unpublished |
| FEP → gauge invariance → gravity | Small community (~10 researchers); not yet mainstream |
| Fisher metric = spacetime metric after coarse-graining | Caticha program established but little-known |
| Tensor network contraction = Schur complement | Exact for free theories; approximate for interacting |
| Prediction is ontologically prior to measurement | Philosophical claim; structurally motivated |

## **6.3 Known Limitations**

**The tautology objection.** If “persistence” is defined as “continued existence,” then “persistence requires the persistence conditions” is circular. The defense: the conditions (nontrivial dynamics, finite energy, state distinguishability) are independently specifiable physical properties. The *content* is that these three seemingly innocuous conditions jointly force the entire structure of quantum mechanics. The logical distance between “the system does something with finite energy while distinguishing states” and “the system must satisfy ΔQ·ΔP ≥ κ/2 with κ structurally irremovable” is the content.

**The selection bias objection.** Perhaps we have cherry-picked results that fit the pattern and ignored those that do not. The defense: the results cited include Nobel Prize–winning research (Ostrom, Prigogine, apoptosis), Fields Medal–adjacent mathematics (Gromov, Connes), and foundational theorems of information theory, quantum mechanics, and statistical physics. These are not obscure results selected for their resemblance to a preconceived pattern. They are central results of their respective disciplines. The question is not whether the results exist but whether anyone has read them together.

**The disciplinary boundary objection.** Unifying results across eight domains risks superficiality in each. The defense: this paper makes no claim that any domain-specific result is novel. Every result cited is well-established in its home discipline. The novelty is exclusively in the synthesis—noticing that established results, when read side by side, say something they have not yet said apart.

# **7. What the Conjunction Implies**

Consider the alternative hypothesis: Shannon’s capacity theorem, Ashby’s requisite variety, Prigogine’s dissipative structures, Holling’s adaptive cycle, Ostrom’s design principles, the QEC threshold, the Heisenberg uncertainty principle, and Bousso’s entropy bound are all unrelated phenomena that happen to share formal structure. On this hypothesis, we would need to explain: why they enforce the same mathematical inequality; why a single algebraic operation (the Schur complement) implements the threshold in every domain checked; why the same constraint-first ordering appears at every scale; and why the necessity of release is independently discovered in every field. Each coincidence is individually possible. The conjunction is strained.

The more parsimonious explanation: there exists a structural requirement that any dynamical system must satisfy in order to continue existing, and independent researchers in independent disciplines have been discovering different faces of it for a century. Shannon found the information-theoretic face. Ashby found the cybernetic face. Prigogine found the thermodynamic face. Heisenberg found the quantum face. Ostrom found the institutional face. The Schur complement is the algebraic face. Cotton’s microprediction program is the market face. They are not competing descriptions. They are translations. The underlying text is the same.

If this reading is correct, the uncertainty principle is not an axiom of quantum mechanics. It is a structural requirement for the existence of any dynamical system, which quantum mechanics happens to make visible. The ħ in ΔQ·ΔP ≥ ħ/2 is the scale at which the universe resolves the persistence threshold—the specific value of the general constant κ that the thermodynamic-level argument forces to be positive but cannot numerically fix. The speed of light, Boltzmann’s constant, and Planck’s constant may all be conversion factors between different descriptions of the same underlying persistence requirement.

And if Cotton is right that “if you can measure it, consider it predicted,” then the deepest implication is ontological: prediction structure is not something agents impose on the world. It is what the world is. The laws of physics are the persistence conditions of a universe that predicts itself into existence at every scale, and the mathematics already knows this. We simply have not yet read it in a single sitting.

*The pattern is real. The unified theorem remains to be written.*

# **References**

[1] Aharonov, D. and Ben-Or, M. (1999). Fault-tolerant quantum computation with constant error rate. SIAM J. Comput. 38(4): 1207–1282.

[2] Ashby, W. R. (1956). An Introduction to Cybernetics. Chapman & Hall.

[3] Aubin, J.-P. (1991). Viability Theory. Birkhäuser.

[4] Bach, V., Ballesteros, M., and Fröhlich, J. (2013, 2025). Continuous renormalization group analysis via the Feshbach–Schur map.

[5] Baez, J. and Fong, B. (2018). A Compositional Framework for Passive Linear Networks. Theory Appl. Categories 33: 1158–1222.

[6] Bianconi, G. (2025). Gravity from entropy. Physical Review D 111: 066001.

[7] Bousso, R. (1999). A covariant entropy conjecture. JHEP 07: 004.

[8] Boyd, A. B., Mandal, D., and Crutchfield, J. P. (2017). Leveraging Environmental Correlations: The Thermodynamics of Requisite Variety. Journal of Statistical Physics 167.

[9] Boyd, A. B., Mandal, D., and Crutchfield, J. P. (2018). Identifying Functional Thermodynamics in Autonomous Maxwellian Ratchets. Physical Review X 8.

[10] Bény, C. and Osborne, T. (2015). Information-geometric approach to the renormalization group. Phys. Rev. A 92: 022330.

[11] Bérut, A. et al. (2012). Experimental verification of Landauer’s principle. Nature 483: 187–189.

[12] Caticha, A. (2018). The Entropic Dynamics approach to Quantum Mechanics. Entropy 21(10): 943.

[13] Choi, S. et al. (2020). Quantum error correction in scrambling dynamics and MIPT. Phys. Rev. Lett. 125: 030505.

[14] Conant, R. and Ashby, W. R. (1970). Every Good Regulator of a System Must Be a Model of That System. Int. J. Systems Sci. 1(2): 89–97.

[15] Connes, A. (1994). Noncommutative Geometry. Academic Press.

[16] Connes, A. and Rovelli, C. (1994). Von Neumann algebra automorphisms and time–thermodynamics relation. Class. Quantum Grav. 11: 2899.

[17] Cotton, P. (2022). Microprediction: Building an Open AI Network. MIT Press.

[18] Cotton, P. (2024). Schur Complementary Allocation: A Unification of HRP and Minimum Variance Portfolios. arXiv:2411.05807.

[19] de Gosson, M. (2003). Phase space quantization and the uncertainty principle. Phys. Lett. A 317: 365–369.

[20] Dörfler, F. and Bullo, F. (2013). Kron reduction of graphs with applications to electrical networks. IEEE Trans. Circuits Syst. I 60(1): 150–163.

[21] Fields, C. and Friston, K. (2022). A free energy principle for generic quantum systems. Progress in Biophysics and Molecular Biology 173: 36–59.

[22] Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Rev. Neurosci. 11: 127–138.

[23] Fritz, T. (2020). A synthetic approach to Markov kernels. Adv. Math. 370: 107239.

[24] Gavidia-Calderón, C. et al. (2025). Hierarchical Minimum Variance Portfolios. arXiv:2503.12328.

[25] Groenewold, H. J. (1946). On the principles of elementary quantum mechanics. Physica 12(7): 405–460.

[26] Gromov, M. (1985). Pseudo holomorphic curves in symplectic manifolds. Invent. Math. 82: 307–347.

[27] Grossman, S. and Stiglitz, J. (1980). On the impossibility of informationally efficient markets. Am. Econ. Rev. 70(3): 393–408.

[28] Gullans, M. and Huse, D. (2020). Dynamical purification phase transition induced by quantum measurements. Phys. Rev. X 10: 041020.

[29] Hasegawa, Y. (2023). Thermodynamic uncertainty relation for quantum first-passage processes. Nature Communications 14: 2828.

[30] Holling, C. S. (1973). Resilience and stability of ecological systems. Annu. Rev. Ecol. Syst. 4: 1–23.

[31] Jacobson, T. (1995). Thermodynamics of spacetime: the Einstein equation of state. Phys. Rev. Lett. 75: 1260–1263.

[32] Koch-Janusz, M. and Ringel, Z. (2018). Mutual information, neural networks and the renormalization group. Nature Physics 14: 578–582.

[33] Landauer, R. (1961). Irreversibility and heat generation in the computing process. IBM J. Res. Dev. 5(3): 183–191.

[34] Lee, S.-S. (2014). Quantum renormalization group and holography. JHEP 01: 076.

[35] Maassen, H. and Uffink, J. B. M. (1988). Generalized entropic uncertainty relations. Physical Review Letters 60(12): 1103–1106.

[36] Ostrom, E. (1990). Governing the Commons. Cambridge University Press.

[37] Prigogine, I. (1977). Self-organization in nonequilibrium systems. Wiley.

[38] Robertson, H. P. (1929). The uncertainty principle. Physical Review 34(1): 163–164.

[39] Shannon, C. E. (1948). A mathematical theory of communication. Bell Syst. Tech. J. 27(3): 379–423.

[40] Skinner, B. et al. (2019). Measurement-induced phase transitions in entanglement dynamics. Phys. Rev. X 9: 031009.

[41] Stein, D. et al. (2025). Graphical Quadratic Algebra. ICTAC 2025.

[42] Stone, M. H. (1930). Linear transformations in Hilbert space. Proc. Natl. Acad. Sci. 16(2): 172–175.

[43] Taylor, A. and Kitching, T. (2010). Analytic methods for cosmological likelihoods. MNRAS 408: 865–875.

[44] Verlinde, E. (2011). On the origin of gravity and the laws of Newton. JHEP 04: 029.

[45] Wolfowitz, J. (1957). The coding of messages subject to chance errors. Illinois J. Math. 1(4): 591–606.

[46] Zhang, F. (2005). The Schur Complement and Its Applications. Springer.