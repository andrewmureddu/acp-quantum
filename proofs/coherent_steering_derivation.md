**Coherent Steering from Stable Coexistence**

*Deriving the Coherent Steering Condition as a Necessary*

*Consequence of Dynamically Stable Self-Reinforcement*

*Appendix A.10 to the Compounding Lemma Proof*

*Working Draft — April 2026*

*Red markers (⚠) indicate open problems requiring further formalization.*

**A.10  The Dynamical Derivation of Coherent Steering**

**A.10.1  The Problem**

The interventional proof of Claim A.3 (Appendix A.8) establishes that the interaction information I(Xₑ; X₁; X₃) is non-negative under the **Coherent Steering Condition** (Definition A.8.3), and that Coherent Steering holds generically—its violation set has measure zero in kernel space (Proposition A.8.7). This is a strong result: it shows that the Crystallization Drift Theorem holds for “almost all” systems. But the argument is static. It treats the space of transition kernels as a fixed parameter space and shows that the bad set is small. It does not explain *why* a dynamical system that sustains two self-reinforcing mechanisms should find itself in the Coherent Steering region rather than the (measure-zero) antagonistic region.

This appendix provides the dynamical explanation. We prove that **stable coexistence of self-reinforcing mechanisms implies Coherent Steering**. The argument is not that antagonistic configurations are rare (the static result), but that they are *dynamically unstable*—a system that enters an antagonistic configuration rapidly exits it by shedding one of the mechanisms. Coherent Steering is therefore not merely generic in parameter space; it is the *unique stable regime* for coexisting self-reinforcing mechanisms.

This upgrades Coherent Steering from “generic assumption” to “theorem,” resolving Open Problem 1 from Section A.8.7.

**A.10.2  Dynamical Stability of Coexistence**

We begin by defining what it means for two self-reinforcing mechanisms to coexist stably. The intuition is straightforward: stable coexistence means that both mechanisms persist over time with reinforcement strengths bounded away from zero. A mechanism whose reinforcement strength decays to zero is being shed—it is no longer genuinely self-reinforcing in the system’s dynamics.

**Definition A.10.1 (Dynamically stable coexistence). **Two self-reinforcing mechanisms R₁, R₂ on a shared dynamical system S are in *dynamically stable coexistence* if there exist constants α₀ > 0 and T₀ > 0 such that for all t > T₀:

    (i)  α(R₁, t) ≥ α₀  and  α(R₂, t) ≥ α₀

    (ii)  R̅ = R₁ ∩ R₂ ≠ ∅, with P(m(t) ∈ R̅) > 0

Condition (i) requires both reinforcement strengths to be uniformly bounded below—neither mechanism is fading. Condition (ii) requires the compound basin to be occupied with positive probability—the mechanisms are genuinely co-active, not merely coexisting in disjoint regions of state space.

*Remark A.10.2. *This definition is the natural dynamical counterpart to the static assumption in Theorem A.8.9, which requires both mechanisms to be “simultaneously active” (m(t) ∈ R₁ ∩ R₂ ≠ ∅). The static version asks for a snapshot; the dynamical version asks for persistence. Any application of the Crystallization Drift Theorem to real systems implicitly assumes dynamical stability, because the theorem describes a drift that unfolds over time—it is meaningless if the mechanisms are transient.

**A.10.3  The Channel Erosion Lemma**

The core technical result is that violating Coherent Steering creates a feedback loop that erodes the weaker mechanism’s reinforcement strength. We call this **channel erosion**.

**Definition A.10.3 (Information channel of a mechanism). **For a self-reinforcing mechanism R₂ acting on variables X₃, the *information channel* of R₂ is the mutual information I(Xₑ; X₃)—the informativeness of the constrained variables about the system’s future. The information channel measures how much R₂’s constraint contributes to predicting the system’s next macrostate.

*Remark A.10.4. *The reinforcement strength α(R₂) and the information channel I(Xₑ; X₃) are related but distinct. The reinforcement strength measures the return probability advantage; the information channel measures how much the constraint informs the future. For the argument below, the crucial link is: **if the information channel degrades, the reinforcement strength must eventually follow**. A mechanism whose constrained variables carry no information about the future cannot maintain a return probability advantage, because the constraint is no longer functionally relevant to the transition dynamics.

**Lemma A.10.5 (Information channel bounds reinforcement strength). **Let R be a self-reinforcing mechanism on variables X with reinforcement strength α(R, t) > 0. If the information channel I(Xₑ; X) = 0 (the constrained variables carry no information about the future), then α(R, t) = 0.

*Proof. *If I(Xₑ; X) = 0, then X and Xₑ are independent: knowing that the system is in region R (a function of X) provides no information about the next macrostate Xₑ. Therefore P(m’ ∈ R | m ∈ R) = P(m’ ∈ R), and the reinforcement strength α(R) = P(m’ ∈ R | m ∈ R) − P(m’ ∈ R) = 0.  ■

More generally, the reinforcement strength is bounded by a function of the information channel:

**Proposition A.10.6 (Channel–reinforcement inequality). ***Let R be a self-reinforcing mechanism with reinforcement basin of measure μ(R) = P(m ∈ R). Then:*

    α(R, t) ≤ g(I(Xₑ; X), μ(R))

where g is a continuous, monotonically increasing function of I(Xₑ; X) with g(0, ·) = 0. For binary mechanisms (μ(R) bounded away from 0 and 1), g is linear in I(Xₑ; X) to leading order.

*Proof sketch. *The reinforcement strength α(R) measures the total variation distance between P(m’ | m ∈ R) and P(m’ | m ∉ R), restricted to the event {m’ ∈ R}. By Pinsker’s inequality, total variation distance is bounded by the square root of KL divergence, which is itself bounded by the mutual information I(Xₑ; X). The specific form of g depends on the geometry of R, but the key property—that g is continuous and vanishes at I = 0—follows from the continuity of mutual information and the data processing inequality.  ■

**A.10.4  The Channel Erosion Theorem**

We now state and prove the main result: violating Coherent Steering creates a self-amplifying erosion of the weaker mechanism.

**Theorem A.10.7 (Channel Erosion). ***Let R₁, R₂ be self-reinforcing mechanisms on variables X₁, X₃ of a shared dynamical system. Suppose the Coherent Steering Condition is violated:*

    I(Xₑ; X₃ | do(X₁ ∈ R₁)) < I(Xₑ; X₃)    —  (Anti-Coherence)

*Define the ***erosion deficit*** δ := I(Xₑ; X₃) − I(Xₑ; X₃ | do(X₁ ∈ R₁)) **>** 0. Then, under the joint dynamics where both mechanisms are active:*

*(a) The effective information channel of R₂ in the compound regime satisfies I**ᵉᶠᶠ**(Xₑ; X₃) ≤ I(Xₑ; X₃) − δ.*

*(b) By Proposition A.10.6, the effective reinforcement strength satisfies α**ᵉᶠᶠ**(R₂) ≤ g(I(Xₑ; X₃) − δ, μ(R₂)).*

*(c) The erosion is self-amplifying: as α(R₂) decreases, the compound basin R̅ shrinks, increasing the concentration of the system in directions favored by R₁, which (under anti-coherence) further degrades R₂’s channel.*

*Proof.*

**Part (a): **When both mechanisms are simultaneously active, the system occupies the compound basin R̅ = R₁ ∩ R₂. In this regime, R₁’s constraint is actively applied: the transition dynamics are those of do(X₁ ∈ R₁) (the mechanism *is* an intervention on X₁, as established in Section A.8.2). The informativeness of X₃ about Xₑ, in this regime, is therefore I(Xₑ; X₃ | do(X₁ ∈ R₁))—the interventional mutual information. By the anti-coherence condition, this is I(Xₑ; X₃) − δ, which is strictly less than R₂’s information channel in isolation.

The interpretation is direct: R₁’s constraint is *jamming* R₂’s channel. The intervention that R₁ performs on the shared substrate degrades, rather than clarifies, the information that X₃ carries about the future. R₁ is steering the system in a direction that makes R₂’s constraint less relevant.

**Part (b): **Immediate from Proposition A.10.6. The reinforcement strength of R₂ in the compound regime is bounded by g(I(Xₑ; X₃) − δ, μ(R₂)). Since g is monotonically increasing and δ > 0, this is strictly less than the reinforcement strength R₂ would have in isolation: αᵉᶠᶠ(R₂) < α(R₂).

**Part (c): **The self-amplification arises from the coupling between reinforcement strength and basin dynamics. As α(R₂) decreases:

Step 1. The compound basin R̅ = R₁ ∩ R₂ becomes less stable: the probability of remaining in R̅ depends on both α(R₁) and α(R₂), so weakening either mechanism reduces the return probability to the intersection.

Step 2. The system spends more time in R₁ \ R̅ (in R₁ but not R₂), where R₁’s constraint is active but R₂’s is not. In this region, the transition dynamics are governed entirely by R₁’s steering, which (by anti-coherence) further degrades the substrate conditions that support R₂.

Step 3. The degraded substrate reduces P(m’ ∈ R₂ | m ∉ R₂)—the probability of *re-entering* R₂ from outside—because the variables X₃ have been steered away from R₂’s basin by R₁’s constraint.

Step 4. With reduced return probability and reduced re-entry probability, α(R₂) decreases further, completing the feedback loop.

Formally, let α₂(t) := α(R₂, t) denote the time-dependent reinforcement strength. The feedback loop yields the differential inequality:

    dα₂/dt ≤ −c · δ · α₁(t) · α₂(t)

where c > 0 is a constant depending on the coupling structure and the geometry of the basins. The key factor is the product δ · α₁(t): the erosion rate is proportional to both the severity of the anti-coherence (δ) and the strength of the antagonistic mechanism (α₁). If R₁ is strongly self-reinforcing and the anti-coherence is severe, R₂ erodes quickly.

If α₁(t) is bounded below by α₁₀ > 0 (R₁ remains strong), the differential inequality gives:

    α₂(t) ≤ α₂(0) · exp(−c · δ · α₁₀ · t)

which decays exponentially to zero. The time constant for decay is τ = 1/(c · δ · α₁₀): stronger anti-coherence and stronger R₁ give faster erosion.  ■

*Remark A.10.8. *The asymmetry in the argument is important. The anti-coherence condition is not symmetric: it says R₁ degrades R₂’s channel, not necessarily the reverse. The mechanism that “wins” is the one whose steering direction is less dependent on the other’s channel. In general, one of two things happens: (i) the weaker mechanism is shed (R₂ decays to α = 0), and the system retains only R₁; or (ii) both mechanisms degrade each other’s channels (mutual anti-coherence), in which case both reinforcement strengths decay and the system enters a full *coherence crisis* (Remark 4.12), shedding mechanisms until a coherent subset remains.

**A.10.5  The Main Theorem**

We can now state the main result.

**Theorem A.10.9 (Stable Coexistence Implies Coherent Steering). ***Let R₁ and R₂ be self-reinforcing mechanisms on variables X₁, X₃ of a shared dynamical system with shared substrate coupling (Definition A.8.6). If R₁ and R₂ are in dynamically stable coexistence (Definition A.10.1), then they satisfy the Coherent Steering Condition (Definition A.8.3):*

*    I(Xₑ; X₃ | do(X₁ ∈ R₁)) ≥ I(Xₑ; X₃)*

*Proof. *By contraposition. Suppose the Coherent Steering Condition is violated, so the anti-coherence condition holds with deficit δ > 0. By Theorem A.10.7 (Channel Erosion), the reinforcement strength α₂(t) satisfies:

    α₂(t) ≤ α₂(0) · exp(−c · δ · α₁₀ · t)

where α₁₀ is a lower bound on R₁’s reinforcement strength. This decays to zero exponentially. Therefore, for any α₀ > 0, there exists T such that α₂(t) < α₀ for all t > T. This violates condition (i) of Definition A.10.1 (dynamically stable coexistence).

Hence: violation of Coherent Steering ⇒ violation of dynamically stable coexistence. Equivalently: dynamically stable coexistence ⇒ Coherent Steering.  ■

*Remark A.10.10 (The contrapositive is the natural direction). *The theorem is most naturally read as: anti-coherence destroys coexistence. The dynamical mechanism is channel erosion: R₁’s constraint jams R₂’s information channel, which degrades R₂’s reinforcement strength, which causes R₂ to be shed from the pattern repertoire. The system then continues with R₁ alone (or whatever coherent subset of mechanisms survives the selection process). This is exactly the coherence crisis described informally in Remark 4.12 and Section 4.4.5, now given a formal dynamical mechanism.

**A.10.6  The Symmetric Case and Mutual Anti-Coherence**

Theorem A.10.9 handles the asymmetric case where R₁ jams R₂ but R₂ does not (necessarily) jam R₁. The symmetric case—where both mechanisms degrade each other’s channels—deserves separate treatment because it leads to a stronger conclusion.

**Corollary A.10.11 (Mutual anti-coherence is maximally unstable). ***If both*

*    I(Xₑ; X₃ | do(X₁ ∈ R₁)) **<** I(Xₑ; X₃)    and    I(Xₑ; X₁ | do(X₃ ∈ R₂)) **<** I(Xₑ; X₁)*

*then both reinforcement strengths decay exponentially, and the system enters a coherence crisis with characteristic time τ = 1/(c · min(δ₁, δ₂) · max(α₁₀, α₂₀)).*

*Proof. *Apply Theorem A.10.7 to both directions. R₁’s constraint erodes R₂ with deficit δ₁; simultaneously, R₂’s constraint erodes R₁ with deficit δ₂. The coupled system of differential inequalities is:

    dα₁/dt ≤ −c · δ₂ · α₂ · α₁

    dα₂/dt ≤ −c · δ₁ · α₁ · α₂

Adding: d(α₁ + α₂)/dt ≤ −c · min(δ₁, δ₂) · α₁ · α₂ ≤ 0. Both strengths are non-increasing, and the product α₁ · α₂ provides the feedback that drives both to zero. The decay is at least as fast as the exponential bound from either inequality alone, and the mutual reinforcement of the two decay processes makes the crisis maximally severe.  ■

*Remark A.10.12. *Mutual anti-coherence corresponds to mechanisms that steer the system in *incompatible directions* on the shared substrate. Each mechanism’s constraint actively interferes with the other’s ability to predict and control the system’s future. This is the dynamical content of a coherence crisis: not merely that the mechanisms’ basins don’t overlap (which is the static condition R̅ = ∅), but that the mechanisms’ *causal effects* on the shared substrate are mutually destructive. The system must shed mechanisms until the remaining set is coherent.

**A.10.7  Extension to k Mechanisms**

The two-mechanism result extends to k mechanisms by the same inductive strategy as Appendix A.9.

**Theorem A.10.13 (Stable coexistence implies Coherent Steering, k mechanisms). ***Let R₁, …, Rₖ be self-reinforcing mechanisms in dynamically stable coexistence (all pairwise reinforcement strengths bounded below, compound basin occupied with positive probability). Then for each pair (R̅ⱼ, Rⱼ₊₁), the Coherent Steering Condition holds.*

*Proof sketch. *Fix any j and consider the compound R̅ⱼ = R₁ ∩ … ∩ Rⱼ and the new mechanism Rⱼ₊₁. By Lemma A.9.1, R̅ⱼ is self-reinforcing. By stable coexistence, α(R̅ⱼ) and α(Rⱼ₊₁) are bounded below. Apply Theorem A.10.9 to the pair (R̅ⱼ, Rⱼ₊₁): if Coherent Steering fails for this pair, channel erosion decays the weaker mechanism’s reinforcement strength to zero, violating stable coexistence.  ■

**A.10.8  Relationship to the Genericity Argument**

Theorem A.10.9 and Proposition A.8.7 (the static genericity result) are complementary, not redundant. They answer different questions:

**Proposition A.8.7 **(static): The set of transition kernels violating Coherent Steering has measure zero. This is a statement about the parameter space of possible systems. It says: if you pick a system at random, it almost surely satisfies Coherent Steering.

**Theorem A.10.9 **(dynamical): Any system that stably maintains two self-reinforcing mechanisms satisfies Coherent Steering. This is a statement about the dynamics of actual systems. It says: *even if* a system starts in the measure-zero antagonistic region, it will not remain there—the antagonism will resolve by shedding a mechanism.

Together, the results provide a two-level justification for Coherent Steering: it holds almost everywhere (static), and the rare exceptions are dynamically unstable (dynamical). The Coherent Steering Condition is therefore not merely a technical assumption but a *structural consequence of what it means for self-reinforcing mechanisms to coexist*.

This has important consequences for the Crystallization Drift Theorem. The original statement of Theorem 4.19 relies on Coherent Steering to establish superadditivity (via Claim A.3). The dynamical derivation shows that this reliance is not an additional assumption—it is implied by the theorem’s own premise that the system maintains multiple self-reinforcing mechanisms over time. The Crystallization Drift Theorem is therefore *self-grounding*: the conditions it describes (accumulation of self-reinforcing mechanisms) automatically produce the conditions it requires (Coherent Steering).

**A.10.9  The Gaussian Case: Explicit Bounds**

For Gaussian systems, the channel erosion theorem yields quantitative bounds that illustrate the general argument.

**Proposition A.10.14 (Gaussian erosion rate). ***Let Q be the precision matrix of a joint Gaussian transition kernel for (X₁, X₃, Xₑ). Define the antagonism parameter:*

    δₓ := ½ log(|Q₃₃| · |Qₑₑ|/|Q₃ₑ,ₑ₃|) − ½ log(|Q₃₃ᵈᵒ| · |Qₑₑᵈᵒ|/|Q₃ₑ,ₑ₃ᵈᵒ|)

*where the superscript “do” denotes evaluation after the Schur complement elimination of X₁. If δₓ **>** 0 (anti-coherence), the reinforcement strength of R₂ decays with time constant:*

    τ = (c · δₓ · α₁₀)⁻¹

*where c depends on the basin measure μ(R₂) and the Gaussian geometry.*

*Proof. *Direct application of Theorem A.10.7 with the Gaussian mutual information formula. The erosion deficit δ equals δₓ by the computation of Section A.8.5 Part (i). The channel–reinforcement inequality (Proposition A.10.6) takes the explicit Gaussian form: α(R) ≤ √(2 I(Xₑ; X) / μ(R)(1 − μ(R))) via Pinsker’s inequality applied to the Gaussian distribution.  ■

*Remark A.10.15. *In the Gaussian case, the anti-coherence condition δₓ > 0 has a clean algebraic interpretation. The Schur complement elimination of X₁ from the precision matrix changes the effective covariance of (X₃, Xₑ). Anti-coherence means that this change *increases* the noise in the X₃–Xₑ channel—the eliminated degree of freedom was carrying signal, not noise, and removing it degrades the channel. This happens precisely when the coupling structure Q₁₃ and Q₁ₑ are such that X₁ mediates a path between X₃ and Xₑ that constructively interferes with the direct path. Eliminating X₁ removes this constructive interference, reducing the channel capacity.

The Gaussian case makes clear why anti-coherence is non-generic: it requires the eliminated variable to be carrying signal along the channel it destroys. Generically, the eliminated variable carries a mix of signal and noise, and removing it on net *improves* the channel (denoising). Anti-coherence is the special case where the variable is pure signal—a fine-tuned condition.

**A.10.10  What This Resolves and What Remains**

**Resolved. **Open Problem 1 from Section A.8.7 is resolved. Coherent Steering is not merely a generic condition (measure-zero complement) but a *necessary consequence of dynamically stable coexistence* of self-reinforcing mechanisms. The derivation provides a causal mechanism (channel erosion), a quantitative bound (exponential decay of the weaker mechanism under anti-coherence), and a clean interpretation (anti-coherence = channel jamming, which is dynamically self-resolving).

**Strengthened. **The Crystallization Drift Theorem is now fully self-grounding. Its premise (multiple self-reinforcing mechanisms coexisting over time) implies its technical requirement (Coherent Steering) without additional assumptions. The theorem’s logical structure is tighter: it does not assume Coherent Steering and then show it is generic; it derives Coherent Steering from the very conditions the theorem describes.

**Connection to coherence crisis. **The channel erosion theorem provides the missing dynamical mechanism for the coherence crisis described informally in Remark 4.12 and Section 4.4.5. When mechanisms violate Coherent Steering, the violated mechanism’s reinforcement strength decays exponentially, and the system sheds it. This is the formal content of “coherence crisis followed by reorganization”—the crisis is channel erosion, and the reorganization is the shedding of anti-coherent mechanisms until the surviving set is coherent.

⚠ **Open Problem (quantitative erosion constant). **The erosion rate constant c in Theorem A.10.7 depends on the coupling structure and basin geometry. The Gaussian case (Proposition A.10.14) gives an explicit form, but the general case requires bounding the derivative of mutual information with respect to coupling parameters. This is downstream of Open Problem 2 (quantitative non-Gaussian bounds) and would benefit from the same tools (Koch-Janusz & Ringel 2018, information geometry). The *existence* of c > 0 is established; its *magnitude* remains to be characterized in full generality.

⚠ **Open Problem (rate of coherence crisis resolution). **Theorem A.10.7 gives the time scale for shedding an anti-coherent mechanism (τ = 1/(cδα₁₀)). But the full coherence crisis dynamics—in which the system may shed multiple mechanisms and reorganize—require a multi-mechanism version of the erosion ODEs. The k-mechanism extension (Theorem A.10.13) shows that stability implies coherence for each pair, but the *transient* dynamics of how a system with multiple anti-coherent mechanisms resolves to a coherent subset remain to be characterized. This is a problem in dynamical selection theory and may connect to the phase transition structure discussed in Section 4.4.8.

**A.10.11  Connection to the Broader Program**

**1. Coherent Steering as natural selection for compatibility. **The channel erosion theorem shows that the mechanism landscape undergoes a selection process: anti-coherent mechanisms are selected *against* because they degrade each other’s functional channels. Coherent mechanisms are selected *for* because they enhance each other’s channels (by the Coherent Steering condition, intervention denoises rather than jams). This is a second layer of selection beyond Lemma 4.14 (survivorship selection for self-reinforcement). The first layer selects for self-reinforcing mechanisms; the second layer selects for coherent self-reinforcing mechanisms. The combination drives the system toward an increasingly coherent and increasingly rigid pattern repertoire—the crystallization drift.

**2. Two selection pressures, one drift. **The proof chain now contains two selection arguments that work in tandem: (i) Lemma 4.14 selects for self-reinforcement (α > 0); (ii) Theorem A.10.9 selects for coherence (δ ≤ 0). Both selections drive the system toward crystallization, but through different mechanisms. Selection (i) eliminates weak patterns (those without return-probability advantage). Selection (ii) eliminates incompatible patterns (those whose constraints jam each other’s channels). Together they produce the monotonic accumulation of strong, mutually compatible constraints that is the Crystallization Drift Theorem.

**3. The faith interval as the coherent regime. **In the theological extension (*The Architecture of Becoming*), the productive interval is interpreted as the “faith interval”—the space where genuine agency and exploration are possible. The dynamical derivation of Coherent Steering adds a layer to this interpretation: the faith interval is not merely the region between dissolution and crystallization, but specifically the region where the system’s constraints are *mutually coherent*. Incoherent constraints produce crises that either resolve (returning to the faith interval) or destroy the system (pushing it to a boundary). Coherent constraints produce drift that eventually closes the interval. The challenge of persistence is to maintain coherence while resisting the drift that coherence itself produces—a structural tension that the ACP identifies as fundamental.

**Additional References for Appendix A.10**

Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory. *2nd ed. Wiley.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference. *2nd ed. Cambridge University Press.

Pinsker, M.S. (1964). *Information and Information Stability of Random Variables and Processes. *Holden-Day.

Tsybakov, A.B. (2009). *Introduction to Nonparametric Estimation. *Springer.

Koch-Janusz, M. & Ringel, Z. (2018). Mutual Information, Neural Networks and the Renormalization Group. *Nature Physics* 14, 578–582.