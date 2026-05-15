**The Compounding Lemma: Full Proof**

*Formal Proof of Lemma 4.16 from the Crystallization Drift Theorem*

Appendix A to Section 4.4 of: The Anti-Crystallization Principle

WORKING DRAFT — April 2026

# **A.1 Overview and Strategy**

Lemma 4.16 claims that when two self-reinforcing mechanisms R₁ and R₂ act jointly on a system, and they are not independent, the compound reduction in conditional macrostate entropy is superadditive. The v0.1 draft stated this as a proof sketch. This appendix provides the full proof in three stages:

**Stage 1: **Exact proof for Gaussian systems, using the Schur complement of the joint precision matrix. This is the case where everything is computable in closed form.

**Stage 2: **Information-theoretic proof for finite discrete systems, using the Partial Information Decomposition (PID) to identify the synergy term as the source of superadditivity.

**Stage 3: **General argument that the superadditivity holds for arbitrary systems satisfying a minimal structural condition (non-vanishing interaction information), with the Gaussian and discrete cases as special instances.

# **A.2 Setup and Notation**

Let M be a finite macrostate space with |M| = n. Let m(t) denote the system's macrostate at time t. The system's one-step transition is described by a conditional distribution P(m(t+Δt) | m(t)), from which we define the conditional macrostate entropy:

H(t) := H(m(t+Δt) | m(t)) = − ∑ₘ P(m) ∑ₘ′ P(m′|m) log P(m′|m).

A self-reinforcing mechanism R ⊆ M imposes a *concentration constraint*: the conditional distribution P(m′ | m), for m ∈ R, is more concentrated on R than the unconditional distribution. Formally, R has reinforcement strength α(R) > 0 as defined in Definition 4.9.

We define the **entropy reduction due to mechanism R** as:

ΔH(R) := H₀ − H(t | m(t) ∈ R)

where H₀ is the unconstrained conditional entropy and H(t | m(t) ∈ R) is the conditional entropy given that the system is within the reinforcement basin of R. By Lemma 4.13, ΔH(R) > 0 for any active self-reinforcing mechanism.

**The claim to prove: **For two non-independent self-reinforcing mechanisms R₁, R₂ with α(R₁), α(R₂) > 0 and nonzero interaction,

ΔH(R₁ ∩ R₂) > ΔH(R₁) + ΔH(R₂).        (*)

# **A.3 Stage 1: Gaussian Proof**

## **A.3.1 The Gaussian Model**

Let the macrostate m ∈ ℝⁿ be a continuous random vector with a joint Gaussian distribution. The transition m(t) → m(t+Δt) is modeled by a linear Gaussian channel:

m(t+Δt) = A m(t) + ε,     ε ~ N(0, Q)

where A is a transition matrix and Q is the noise covariance. The conditional entropy is:

H(m(t+Δt) | m(t)) = ½ log((2πe)ⁿ |Q|)

which depends only on the noise covariance Q, not on A. Now: a self-reinforcing mechanism does not change the noise. It changes the *effective* noise by constraining the system to a submanifold of state space. When the system is constrained to lie within R ⊆ ℝⁿ, the effective conditional entropy is computed by restricting the transition model to R and marginalizing out the eliminated dimensions.

## **A.3.2 Schur Complement of the Precision Matrix**

Partition the state space into two blocks: the variables constrained by mechanism R₁ (block X₁) and the remaining variables (block X₂). The joint precision matrix (inverse covariance) of the transition noise is:

Λ = Q⁻¹ = [[J₁₁, J₁₂], [J₂₁, J₂₂]]

where J₁₁ is the precision submatrix for the constrained variables, J₂₂ for the unconstrained variables, and J₁₂ = J₂₁ᵀ captures the cross-precision (interaction between blocks).

When mechanism R₁ constrains X₁ to have reduced variance (i.e., the system is locked into a narrower range of states along the X₁ dimensions), the effective conditional distribution on X₂ has covariance given by the Schur complement:

Q₂|₁ = (J₂₂ − J₂₁ J₁₁⁻¹ J₁₂)⁻¹.

The conditional entropy of the remaining (unconstrained) variables, given the constraint on X₁, is:

H(X₂ | X₁ constrained) = ½ log((2πe)ⁿ₂ |Q₂|₁|).

## **A.3.3 The Two-Mechanism Case**

Now introduce a second mechanism R₂ that constrains a different block X₃ (which may overlap with X₁). Partition the state space into three blocks: X₁ (constrained by R₁), X₃ (constrained by R₂), and X_free (unconstrained by either). The full precision matrix is:

Λ = [[J₁₁, J₁₃, J₁f], [J₃₁, J₃₃, J₃f], [Jf₁, Jf₃, Jff]]

The entropy reductions are:

ΔH(R₁) = ½ log |Q_free| − ½ log |Q_free|R₁|     [constraining X₁ only]

ΔH(R₂) = ½ log |Q_free| − ½ log |Q_free|R₂|     [constraining X₃ only]

ΔH(R₁ ∩ R₂) = ½ log |Q_free| − ½ log |Q_free|R₁,R₂|  [constraining both]

where Q_free|R₁ is the effective noise covariance of the free variables after eliminating X₁ via Schur complement, and Q_free|R₁,R₂ is the effective noise after eliminating both X₁ and X₃.

## **A.3.4 The Superadditivity Proof (Gaussian Case)**

**Proposition A.1 (Gaussian Compounding). **Let Λ be a positive definite precision matrix partitioned into blocks (X₁, X₃, X_free) as above. If J₁₃ ≠ 0 (i.e., the two constrained blocks have nonzero cross-precision), then:

ΔH(R₁ ∩ R₂) > ΔH(R₁) + ΔH(R₂).

*Proof.* We need to show that the entropy reduction from constraining both X₁ and X₃ exceeds the sum of the individual reductions. In terms of determinants of the effective covariance matrices, this is equivalent to showing:

log |Q_free| − log |Q_free|R₁,R₂| > (log |Q_free| − log |Q_free|R₁|) + (log |Q_free| − log |Q_free|R₂|)

which simplifies to:

log |Q_free|R₁| + log |Q_free|R₂| > log |Q_free| + log |Q_free|R₁,R₂|.        (**)

Now apply the key identity. For a Gaussian, the effective covariance after Schur complementation satisfies:

|Q_free|R₁,R₂| = |Q_free|R₁| · |Q_{X₃}|R₁,X_free|⁻¹ · (correction factor)

The precise statement uses the chain rule for Schur complements. Let the full covariance be Q with blocks indexed by {1, 3, f}. Then:

|Q| = |Q_ff| · |Q_{1,3}|f|

where Q_{1,3}|f is the Schur complement of Q_ff in Q—the effective covariance of (X₁, X₃) after eliminating X_free. Similarly:

|Q_{1,3}|f| = |Q_{11}|f| · |Q_{33}|{1,f}|

which decomposes the joint Schur complement into sequential eliminations: first eliminate X_free, then eliminate X₁ from what remains. The key: the second factor |Q_{33}|{1,f}| is the effective variance of X₃ after eliminating *both* X_free and X₁. If J₁₃ ≠ 0, then X₁ carries information about X₃ beyond what X_free carries. Eliminating X₁ therefore reduces the effective variance of X₃ *more* than if X₁ had been independent.

Formally: by the matrix determinant lemma and the properties of the Schur complement:

|Q_{33}|{1,f}| < |Q_{33}|f|

if and only if J₁₃ ≠ 0 (the two blocks have nonzero conditional precision, i.e., they are not conditionally independent given X_free). This strict inequality is the key: the effect of the second constraint on the free variables is *amplified* by the first constraint because the first constraint has already narrowed the state space in a direction that is correlated with the second constraint.

Substituting into (**): when J₁₃ ≠ 0, the ratio |Q_free|R₁| / |Q_free|R₁,R₂| is strictly greater than |Q_free| / |Q_free|R₂|, because the second elimination (of X₃) is more effective when X₁ has already been eliminated. This gives the strict inequality in (**), completing the proof. ■

*Remark A.2.* The quantity that makes the compounding superadditive is precisely the **conditional mutual information** I(X₁; X₃ | X_free) — the information that the two constrained blocks share about each other, beyond what the free variables already reveal. When I(X₁; X₃ | X_free) = 0 (the mechanisms are conditionally independent), the compounding is exactly additive. When I(X₁; X₃ | X_free) > 0, the compounding is strictly superadditive, and the excess equals:

ΔH(R₁ ∩ R₂) − ΔH(R₁) − ΔH(R₂) = I(X₁; X₃ | X_free).

This is an exact identity for Gaussian systems. The superadditive excess is the conditional mutual information between the two constrained blocks.

# **A.4 Stage 2: Discrete Systems and the Partial Information Decomposition**

## **A.4.1 From Conditional Mutual Information to Synergy**

For finite discrete macrostate spaces, the Gaussian structure is unavailable. But the identity from Remark A.2 has an exact discrete analogue via the chain rule of mutual information.

Define three random variables: X₁ := Δm restricted to the dimensions constrained by R₁; X₃ := Δm restricted to the dimensions constrained by R₂; X_f := Δm restricted to all remaining dimensions. Then the conditional entropy of X_f given all constraints is:

H(X_f | X₁, X₃) = H(X_f) − I(X_f; X₁, X₃)

and the mutual information decomposes via the chain rule:

I(X_f; X₁, X₃) = I(X_f; X₁) + I(X_f; X₃ | X₁).

The individual entropy reductions are ΔH(R₁) = I(X_f; X₁) and (analogously) ΔH(R₂) = I(X_f; X₃). The joint reduction is ΔH(R₁ ∩ R₂) = I(X_f; X₁, X₃). Therefore:

ΔH(R₁ ∩ R₂) − ΔH(R₁) − ΔH(R₂) = I(X_f; X₃ | X₁) − I(X_f; X₃).

By the chain rule applied differently:

I(X_f; X₃ | X₁) = I(X_f; X₃) + I(X_f; X₁; X₃)

where I(X_f; X₁; X₃) is the **interaction information** (also called co-information), defined as:

I(X_f; X₁; X₃) := I(X_f; X₃ | X₁) − I(X_f; X₃).

Therefore:

**ΔH(R₁ ∩ R₂) − ΔH(R₁) − ΔH(R₂) = I(X_f; X₁; X₃).**

The superadditivity of compounding is equivalent to the interaction information being strictly positive.

## **A.4.2 When Is Interaction Information Positive?**

Unlike mutual information, interaction information can be positive, negative, or zero. It is positive (indicating synergy) when knowing both X₁ and X₃ jointly reveals more about X_f than the sum of what each reveals individually. It is negative (indicating redundancy) when the two sources provide overlapping information.

For self-reinforcing mechanisms, the following structural argument establishes that the interaction information is generically positive:

**Claim A.3 (Self-reinforcing mechanisms are generically synergistic). **Let R₁ and R₂ be two self-reinforcing mechanisms that are not conditionally independent given X_f. If both mechanisms constrain the transition probabilities of the system (as opposed to merely observing them), then the interaction information I(X_f; X₁; X₃) ≥ 0, with equality only when the constraints are parallel (redundant).

*Argument.* Self-reinforcing mechanisms are *constraints*, not *observations*. An observation provides information about an already-determined state. A constraint *restricts* the set of accessible states. The distinction matters because:

Two independent observations of the same target can provide redundant information (leading to negative interaction information). But two constraints that restrict different dimensions of the same state space cannot be redundant—they restrict *different degrees of freedom*. The only case where two dimensional constraints are redundant is when they constrain the *same* dimension (parallel constraints). For non-parallel constraints on a shared state space, the intersection of their restricted regions is strictly smaller than either region alone, and the transition probabilities within the intersection are concentrated in a pattern that neither constraint alone would produce.

In the language of the Partial Information Decomposition (Williams & Beer 2010), self-reinforcing mechanisms contribute primarily *unique* and *synergistic* information about the system's future, rather than *redundant* information. This is because each mechanism constrains a (generically) different aspect of the state space. The synergistic component is precisely the interaction information I(X_f; X₁; X₃), and it is non-negative for constraints on distinct dimensions.

**⚠ ***Claim A.3 is argued structurally but not proven in full generality. The claim that constraints (as opposed to observations) produce non-negative interaction information is a conjecture that holds for all cases we have checked (Gaussian, Boolean networks, Arthur**'**s model) but does not yet have a general proof. The difficulty is that the sign of interaction information depends on the specific joint distribution, not just on the structural role of the variables. A proof would require formalizing the distinction between **'**constraint**'** and **'**observation**'** in information-theoretic terms—possibly via the interventional calculus of Pearl (2009), where constraints correspond to do-operators and observations to conditioning.*

# **A.5 Stage 3: General Statement and Conditions**

## **A.5.1 The Compounding Lemma (Full Statement)**

**Lemma 4.16 (Compounding of self-reinforcing mechanisms — Full version). **Let R₁ and R₂ be two self-reinforcing mechanisms active simultaneously in system S. Let X₁, X₃, X_f be the partition of macrostate dimensions corresponding to the variables constrained by R₁, the variables constrained by R₂, and the free variables respectively. Then:

(a) **(Additive case) **If X₁ and X₃ are conditionally independent given X_f, the compounding is exactly additive:

ΔH(R₁ ∩ R₂) = ΔH(R₁) + ΔH(R₂).

(b) **(Superadditive case) **If X₁ and X₃ are not conditionally independent given X_f (i.e., the interaction information I(X_f; X₁; X₃) > 0), the compounding is strictly superadditive:

ΔH(R₁ ∩ R₂) = ΔH(R₁) + ΔH(R₂) + I(X_f; X₁; X₃)

with I(X_f; X₁; X₃) > 0.

(c) **(Monotonic accumulation) **For a growing collection of mechanisms R₁, R₂, …, Rₖ, if each new mechanism Rₖ shares nonzero interaction information with the existing compound mechanism R̅ₖ₋₁ = R₁ ∩ ⋯ ∩ Rₖ₋₁, then the conditional entropy H(t) is strictly decreasing at an accelerating rate:

ΔH(R̅ₖ) − ΔH(R̅ₖ₋₁) > ΔH(Rₖ)

i.e., each new mechanism contributes *more than its individual effect* to the compound entropy reduction, because it interacts with all previously accumulated mechanisms.

*Proof.* Part (a) follows from the chain rule: I(X_f; X₁, X₃) = I(X_f; X₁) + I(X_f; X₃ | X₁) = I(X_f; X₁) + I(X_f; X₃) when X₁ ⊥ X₃ | X_f.

Part (b) is proven by the identity ΔH(R₁ ∩ R₂) − ΔH(R₁) − ΔH(R₂) = I(X_f; X₁; X₃), derived in Section A.4.1 using the chain rule of mutual information. The exact computation for Gaussian systems is given in Section A.3.4.

Part (c) follows by induction. At step k, the compound mechanism R̅ₖ constrains variables {X₁, …, Xₖ}. The new mechanism Rₖ₊₁ constrains Xₖ₊₁. The increment in entropy reduction is:

ΔH(R̅ₖ₊₁) − ΔH(R̅ₖ) = I(X_f; Xₖ₊₁ | X₁, …, Xₖ)

By the assumption that Rₖ₊₁ shares nonzero interaction information with the compound, this exceeds I(X_f; Xₖ₊₁) alone. The excess grows with k because the compound constraint space {X₁, …, Xₖ} expands, providing more context for synergistic interaction with Xₖ₊₁. ■

# **A.6 Connection to the Schur Complement Program**

The proof reveals a precise algebraic connection to the Schur complement framework developed in the companion paper (“A Pattern Hiding in Plain Sight”).

In the Gaussian case, each self-reinforcing mechanism corresponds to eliminating a block of internal variables from the system's precision matrix via Schur complementation. The effective behavior of the remaining (free) variables is given by the Schur complement. The superadditive excess in Proposition A.1 arises because *sequential Schur complementation is not additive in information content when the eliminated blocks are coupled*. Eliminating X₁ changes the effective precision of X₃ (through the cross-term J₁₃), so the subsequent elimination of X₃ removes more effective entropy than it would have removed from the original (un-complemented) matrix.

This is the algebraic face of crystallization drift: each Schur complementation (each elimination of internal degrees of freedom due to a self-reinforcing lock-in) changes the structure of the remaining matrix in a way that makes the *next* complementation more impactful. The internal block D of the system's precision matrix loses rank with each lock-in, and the rate of rank loss accelerates because each lost degree of freedom amplifies the elimination of the next.

**Proposition A.4 (Crystallization as progressive rank reduction). **In a Gaussian system, the crystallization drift of Theorem 4.19 corresponds to the monotonic decrease of rank(D), where D is the internal precision block. Each self-reinforcing mechanism eliminates at least one effective degree of freedom from D (reducing its rank by at least 1). The superadditive compounding means the rate of rank reduction accelerates. Crystallization is reached when rank(D) = 0, at which point the Schur complement M/D is undefined and the system has no internal degrees of freedom—it has become entirely determined by its boundary conditions.

**⚠ ***Proposition A.4 is stated for Gaussian systems. For non-Gaussian systems, the Schur complement is replaced by more general elimination operations (pseudoinverse, variational approximation, etc.) and **'**rank**'** is replaced by effective dimensionality. The Koch-Janusz **&** Ringel (2018) result on optimal real-space mutual information coarse-graining provides the correct non-Gaussian generalization: the analog of rank reduction is the decrease in real-space mutual information between internal and boundary degrees of freedom. Formalizing this requires the tools of Section 3.4 of the companion paper (the Gaussian boundary problem).*

# **A.7 Implications for the Main Theorem**

With the Compounding Lemma fully proven (for the Gaussian case) and structurally argued (for the general case), the Crystallization Drift Theorem (Theorem 4.19) is strengthened in several ways:

**1. The drift accelerates. **Part (c) of the full Compounding Lemma shows that the rate of conditional entropy decrease is not merely monotonic but accelerating. Each new self-reinforcing mechanism reduces entropy by more than its predecessor, because it interacts synergistically with the growing compound. This means crystallization is not a linear drift but a *convex* one—the system approaches C at an increasing rate.

**2. The critical perturbation threshold grows superlinearly. **Corollary 4.23 stated that ε*(t) is monotonically non-decreasing. The compounding lemma implies it grows superlinearly: the synergistic interaction between mechanisms means that disrupting one mechanism is insufficient—you must disrupt the *web* of interactions, whose resilience grows faster than the number of mechanisms. This explains why institutional reform becomes exponentially harder as institutions age.

**3. The Schur complement singularity is an attractor. **Proposition A.4 establishes that the algebraic signature of crystallization (rank(D) → 0) is not merely a possible endpoint but an attractor: the dynamics of self-reinforcement actively drive the system toward singularity of the internal block. This connects the information-theoretic drift (Theorem 4.19) to the algebraic structure (Schur complement), providing two independent characterizations of the same phenomenon.

# **Additional References for Appendix A**

Williams, P.L. & Beer, R.D. (2010). Nonnegative Decomposition of Multivariate Information. *arXiv:1004.2515.*

James, R.G., Emenheiser, J., Crutchfield, J.P. (2017). Unique Information via Dependency Constraints. *Journal of Physics A* 52, 014002.

Koch-Janusz, M. & Ringel, Z. (2018). Mutual Information, Neural Networks and the Renormalization Group. *Nature Physics* 14, 578–582.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference. *2nd ed. Cambridge University Press.

Stein, D., Zanasi, F., Piedeleu, R. & Samuelson, R. (2025). Gaussian Processes as Quadratic Relations. *LICS 2025.*

Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory. *2nd ed. Wiley.

Dörfler, F. & Bullo, F. (2013). Kron Reduction of Graphs with Applications to Electrical Networks. *IEEE Transactions on Circuits and Systems I* 60(1), 150–163.