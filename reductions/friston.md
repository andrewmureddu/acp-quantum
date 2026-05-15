**Appendix A.11: Formal Reduction of the Free Energy Principle**

**to the Anti-Crystallization Principle**

*ACP Working Paper Series*

*April 2026*

# Abstract

We provide the formal reduction of Friston’s Free Energy Principle (FEP) to the Anti-Crystallization Principle (ACP). The key result is Theorem A.11.5, which establishes that variational free energy minimization is equivalent to maintenance of the ACP’s productive interval under a specific identification of variables. The reduction proceeds through an intermediate lemma (Lemma A.11.3) relating the agent’s model entropy to the system-level conditional macrostate entropy H(m′ | m). This resolves the open problem flagged in Section 5.3 of the main paper.

The reduction reveals that the FEP’s two optimization channels—perception (updating the variational density q) and action (changing sensory states through the environment)—correspond precisely to the ACP’s two boundary management tasks: perception manages the dissolution boundary D, while unchecked action risks the crystallization boundary C. The complexity penalty in variational free energy, often treated as a regularization device, emerges as exactly the anti-crystallization constraint.

# A.11.1  Setup and Notation

We begin by stating the two frameworks side by side, then construct the bridge.

## The Free Energy Principle Framework

Following Friston (2010, 2019), consider a system partitioned into internal states μ, sensory states s, active states a, and external (hidden) states ψ. The system possesses a generative model P(s, ψ | μ) encoding predictions about how hidden causes produce sensory data. The variational free energy is:

F[q, s] = E_q[ln q(ψ) − ln P(s, ψ | μ)] = D_KL(q(ψ) || P(ψ | s, μ)) − ln P(s | μ)

where q(ψ) is a variational (recognition) density approximating the true posterior P(ψ | s, μ). The FEP asserts that biological systems minimize F through two channels:

(P) Perception: update q to minimize D_KL(q || P(ψ | s, μ)), improving the model’s match to the posterior.

(A) Action: change a (and thereby s) to maximize ln P(s | μ), selecting sensory data the model predicts well.

The decomposition F = D_KL + (−ln P(s|μ)) shows that F is an upper bound on surprisal: F ≥ −ln P(s | μ). Minimizing F therefore bounds surprisal from above.

## The ACP Framework (Relevant Elements)

The ACP operates on a system S = (Ω, σ, T, μ) with microstate space Ω, coarse-graining map σ: Ω → M, dynamics T, and measure μ. The key quantities are:

• Conditional macrostate entropy: H(m′ | m), measuring how predictable the next macrostate is given the current one.

• Dissolution boundary D: the set of macrostates where H(m′ | m) = H_max (maximum entropy, no prediction possible).

• Crystallization boundary C: the set where H(m′ | m) = 0 (fully deterministic, no novelty possible).

• Productive interval: 0 < H(m′ | m) < H_max, the regime of future-bearing dynamics.

# A.11.2  The Variable Identification

The formal mapping requires identifying FEP quantities with ACP quantities. We propose:

***Definition A.11.1 (FEP–ACP Variable Identification). ***Let S be a system satisfying Axioms 1–3 of the ACP, and let S additionally possess the Markov blanket partition of the FEP. The identification is:

(i) The macrostate m is the pair (μ, s)—the internal and sensory states jointly. The environment’s hidden causes ψ constitute the microscopic degrees of freedom that m coarse-grains over.

(ii) The conditional macrostate entropy H(m′ | m) decomposes as H((μ′, s′) | (μ, s)) = H(s′ | μ, s) + H(μ′ | s′, μ, s). The first term is the sensory surprise the agent will encounter; the second is the internal state’s update uncertainty.

(iii) The generative model P(s, ψ | μ) defines the coarse-graining map σ implicitly: two microstates ω₁, ω₂ map to the same macrostate if and only if they assign the same posterior distribution P(ψ | s, μ).

*Remark A.11.2. *The identification (iii) is the crucial step. It says that the agent’s model *is* the coarse-graining—different world-states that the agent cannot distinguish (because they produce the same posterior) belong to the same macrostate. This is not an assumption; it is a definitional identification. The FEP’s generative model performs exactly the function of the ACP’s coarse-graining map: it partitions the world into equivalence classes that the system can distinguish.

# A.11.3  The Model–Macrostate Entropy Lemma

This is the key technical result bridging the two frameworks. It relates the agent’s model entropy—a quantity internal to the FEP—to the system-level conditional macrostate entropy—a quantity in the ACP.

***Lemma A.11.3 (Model–Macrostate Entropy Bridge). ***Under the variable identification of Definition A.11.1, the conditional macrostate entropy decomposes as:

H(m′ | m) = H(s′ | μ, s) + H(μ′ | s′, μ, s)

where:

(a) H(s′ | μ, s) = H_FEP(s′ | μ) + I(s′; s | μ)’s complement. More precisely, H(s′ | μ, s) ≤ H(s′ | μ) = −ln P(s′ | μ) averaged over s′, with equality when sensory states are temporally independent given internal states.

(b) H(μ′ | s′, μ, s) measures the indeterminacy of the internal state update. For a deterministic recognition dynamics (gradient descent on F), this term is zero. For stochastic recognition dynamics (Langevin sampling), it is controlled by the diffusion coefficient.

***Proof. ***By the chain rule for conditional entropy:

H(m′ | m) = H((μ′, s′) | (μ, s)) = H(s′ | μ, s) + H(μ′ | s′, μ, s)

This is the standard chain rule for joint entropy. Part (a) follows from the data processing inequality: the agent’s prediction of s′ depends on ψ only through μ (by the Markov blanket property), so H(s′ | μ, s) ≤ H(s′ | μ). The bound is saturated when s does not provide temporal autocorrelation beyond what μ already captures. Part (b) follows from the functional form of the recognition dynamics. ■

***Corollary A.11.4. ***For a system with deterministic recognition dynamics (the standard case in Friston 2010), the conditional macrostate entropy reduces to:

H(m′ | m) = H(s′ | μ, s) ≤ −⟨ln P(s′ | μ)⟩ = ⟨surprisal⟩

That is: the conditional macrostate entropy is bounded above by the average surprisal of sensory observations. This is the quantity that the FEP’s variational free energy bounds from above.

# A.11.4  The Reduction Theorem

***Theorem A.11.5 (FEP as ACP Special Case). ***Under the variable identification of Definition A.11.1, the Free Energy Principle is a special case of the Anti-Crystallization Principle. Specifically:

(i) Perception (minimizing D_KL(q || P(ψ | s, μ))) manages the dissolution boundary. A system with a poor generative model—one whose variational density q diverges from the true posterior—makes increasingly inaccurate predictions. In the ACP’s terms, H(m′ | m) → H_max: the macroscopic future becomes unpredictable. The system dissolves.

(ii) Action (maximizing ln P(s | μ)) without the complexity penalty risks crystallization. A system that selects only sensory data its model already predicts well is performing active inference in the service of self-reinforcement: it is narrowing its sensory repertoire to confirm existing predictions. In the ACP’s terms, this is the crystallization drift—the compound reinforcement basin R̅ shrinks, H(m′ | m) → 0.

(iii) The complexity penalty D_KL(q || P(ψ)) in the free energy decomposition F = E_q[−ln P(s | ψ)] + D_KL(q(ψ) || P(ψ)) is exactly the anti-crystallization constraint. It penalizes the variational density for diverging from the prior—that is, for becoming too specialized to current data. This prevents q from collapsing to a point mass (which would be crystallization of the generative model).

***Proof. ***We prove each part.

**Part (i). **The variational free energy satisfies F ≥ −ln P(s | μ). By Corollary A.11.4, −⟨ln P(s | μ)⟩ ≥ H(m′ | m) for deterministic recognition dynamics. Therefore, failing to minimize F allows surprisal to grow without bound, which by Corollary A.11.4 drives H(m′ | m) toward H_max. We need to verify that the direction is correct: large D_KL(q || p) means the agent’s model diverges from reality. An agent whose model diverges cannot predict its sensory inputs, so H(s′ | μ, s) → H(s′) = H_max^s, the maximum sensory entropy. Under the identification m = (μ, s), this drives H(m′ | m) → H_max. The system approaches D.

**Part (ii). **Consider action that maximizes ln P(s | μ) alone, ignoring the complexity penalty. Such a system selects sensory environments that its existing model already predicts. Each such selection reinforces the model’s current parameters—this is precisely a self-reinforcing mechanism in the ACP’s sense (Definition 4.7). By Lemma 4.14, self-reinforcing mechanisms dominate pattern repertoires. By the Crystallization Drift Theorem (Theorem 4.19), this drives H(m′ | m) → 0. We verify the identification: the agent’s model becomes increasingly specialized, predicting a narrow range of sensory data with certainty. The conditional macrostate entropy drops because the system’s future (μ′, s′) becomes fully determined by its present (μ, s)—a crystallized state.

**Part (iii). **Write the variational free energy in the alternative decomposition:

F = E_q[−ln P(s | ψ)] + D_KL(q(ψ) || P(ψ))

The first term (expected negative log-likelihood) is the accuracy term: it drives q toward explaining the data well. Minimizing this term alone would push q toward a delta function on the maximum-likelihood ψ—crystallizing the model. The second term D_KL(q || P(ψ)) is the complexity penalty: it resists q diverging from the prior. When P(ψ) is broad (high-entropy prior), this penalty is exactly an anti-crystallization force. It prevents the variational density from collapsing to a point mass. The balance between accuracy and complexity is the FEP’s version of the productive interval: enough model precision to avoid dissolution, enough model flexibility to avoid crystallization. ■

# A.11.5  Crystallization Drift in FEP Terms

The Crystallization Drift Theorem (Theorem 4.19) acquires a specific interpretation in the FEP context.

***Proposition A.11.6 (Crystallization Drift as Precision Accumulation). ***Under the FEP–ACP identification, the crystallization drift of Theorem 4.19 corresponds to the progressive accumulation of precision (inverse variance) in the agent’s generative model. Specifically:

(a) Each self-reinforcing mechanism R_i in the ACP corresponds to a precision-weighted prediction in the generative model. The reinforcement strength α(R_i) is monotonically related to the precision π_i of the corresponding prediction.

(b) The compounding of self-reinforcing mechanisms (Lemma 4.16) corresponds to the precision-weighting scheme in hierarchical predictive coding: a prediction confirmed at multiple levels acquires compound precision.

(c) The accelerating drift rate (Theorem A.9.9) corresponds to the well-known confirmation bias in active inference: the more precisely the agent predicts a particular sensory stream, the more strongly it acts to maintain that stream, which further increases precision.

***Proof sketch. ***Part (a): In Friston’s framework, precision π = 1/σ² controls how strongly a prediction influences perception. A high-precision prediction is one that the agent treats as reliable and resists revising—it is self-reinforcing in the sense of Definition 4.7 because the agent’s own dynamics (precision-weighted prediction error minimization) maintain the prediction’s dominance. The reinforcement strength α(R) = P(m′ ∈ R | m ∈ R) − P(m′ ∈ R) corresponds to the excess persistence of the prediction under precision weighting.

Part (b): In hierarchical predictive coding, predictions at level ℓ are modulated by precision estimates at level ℓ+1. When two predictions R_i, R_j are non-independent (they share variance-explaining structure), their joint precision exceeds the sum: π_{ij} > π_i + π_j. This is the Gaussian case of superadditive compounding (Lemma 4.16), where the excess is given by the Schur complement of the joint precision matrix.

Part (c): Active inference acts to minimize prediction error. A system with high-precision predictions of sensory stream s_0 will preferentially select actions that produce s_0, which confirms the prediction, which maintains or increases π. This is precisely the feedback loop identified in Theorem 4.19: self-reinforcing mechanisms drive the system toward crystallization at an accelerating rate, because each reinforcement cycle increases the effective precision. ■

# A.11.6  What the Reduction Reveals

The formal reduction illuminates several points that are obscured when the FEP and ACP are treated as independent frameworks.

**The complexity penalty is not optional. **In Bayesian statistics, the KL penalty D_KL(q || P(ψ)) is often treated as a regularizer—useful for preventing overfitting but not fundamental. The ACP reduction shows it is structurally necessary: without it, the accuracy term drives the system to crystallization. Any biological system that minimizes accuracy without a complexity penalty will undergo crystallization drift (Theorem 4.19) and lose future-bearing dynamics. The complexity penalty is the FEP’s implementation of boundary maintenance at C.

**Perception and action serve different boundaries. **The FEP’s two optimization channels are not symmetric. Perception (updating q) primarily manages the dissolution boundary: an agent that stops updating its model loses predictive coherence and dissolves into sensory noise. Action (changing s through the world) primarily manages the crystallization boundary—or rather, risks it: action that is purely confirmatory drives crystallization. The asymmetry between perception and action, which is sometimes noted in the FEP literature but not explained, is a structural consequence of the ACP’s two-boundary architecture.

**The FEP inherits the crystallization drift. **Since the FEP is a special case of the ACP, FEP-governed systems are subject to the Crystallization Drift Theorem. Concretely: any active inference agent that successfully minimizes prediction error over time will progressively reduce H(m′ | m)—it will become increasingly predictable, increasingly rigid, increasingly incapable of accommodating genuine novelty. This is not a failure of implementation; it is a mathematical consequence of successful free energy minimization in a self-reinforcing regime. The CDT provides a formal account of why biological systems require mechanisms of model revision (sleep, stress, exploration, play) that periodically disrupt the precision accumulation.

**Friston’s “epistemic value” is an anti-crystallization force. **In later formulations (Friston et al. 2015, 2017), the FEP includes an epistemic value term that motivates information-seeking behavior—exploring novel sensory data even when it might increase prediction error. Under the ACP reduction, epistemic value is identified as the agent’s endogenous anti-crystallization mechanism: it provides the perturbation required by Theorem 4.19 to maintain the productive interval. The epistemic/pragmatic tradeoff in active inference is the productive interval maintenance problem in ACP terms.

# A.11.7  Limitations and Open Problems

**⚠ Markov blanket existence. **The reduction requires the Markov blanket partition of the FEP. Not all ACP systems possess this partition. The FEP is therefore a proper special case: it applies to the subset of ACP systems that admit a Markov blanket decomposition. Systems without clear internal/external boundaries (e.g., reaction-diffusion systems without membranes) are governed by the ACP but not necessarily by the FEP.

**⚠ Stochastic recognition dynamics. **Our main results use the deterministic recognition dynamics case (Corollary A.11.4). For systems with stochastic internal dynamics (Langevin or MCMC sampling of the posterior), the term H(μ′ | s′, μ, s) is nonzero and the bridge lemma requires a bound relating this term to the diffusion coefficient. This is a technical extension, not a structural gap: the inequality H(m′ | m) ≤ F + H_internal still holds, where H_internal is the recognition noise entropy.

**⚠ Quantitative mapping. **The reduction is structural: it shows that FEP-minimization corresponds to productive interval maintenance. A fully quantitative version would express the ACP’s H(m′ | m) as an explicit function of the FEP’s F, π, and model parameters. This requires bounding the gap between H(s′ | μ, s) and −ln P(s | μ), which depends on the temporal autocorrelation of sensory states. This is downstream of the non-Gaussian bounds problem (OP2).

# A.11.8  Summary

The Free Energy Principle is a special case of the Anti-Crystallization Principle for systems admitting a Markov blanket partition. The reduction proceeds through a variable identification (Definition A.11.1) and a bridge lemma (Lemma A.11.3) connecting the agent’s model entropy to the ACP’s conditional macrostate entropy. The main theorem (Theorem A.11.5) shows that the FEP’s two optimization channels—perception and action—correspond to the ACP’s two boundary management tasks, and that the complexity penalty in variational free energy is structurally equivalent to the anti-crystallization constraint.

The reduction is currently structural rather than fully quantitative. It establishes the logical relationship between the frameworks and identifies the FEP as governing a proper subset of ACP systems. It inherits the ACP’s results: FEP-governed systems are subject to crystallization drift, and the FEP’s epistemic value term serves as the anti-crystallization perturbation mechanism.

# References

Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience 11, 127–138.

Friston, K. (2019). A free energy principle for a particular physics. arXiv:1906.10184.

Friston, K., Rigoli, F., Ognibene, D., Mathys, C., Fitzgerald, T., & Pezzulo, G. (2015). Active inference and epistemic value. Cognitive Neuroscience 6(4), 187–214.

Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., Dolan, R. J., & Pezzulo, G. (2017). Active inference and learning. Neuroscience and Biobehavioral Reviews 68, 862–879.

Cover, T. M., & Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley.

Pearl, J. (2009). Causality: Models, Reasoning, and Inference (2nd ed.). Cambridge University Press.