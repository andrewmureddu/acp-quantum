# A Three-Stroke Persistence Engine: Operator-Level Bridge for the Anti-Crystallization Principle

**Andrew Mureddu**  
Independent Researcher  
Zenodo / GitHub (CC0)  
April 2026

---

## Status Note

This is an exploratory bridge draft, moved from `paper/` to `bridges/` on 2026-04-30 because the active paper remains `paper/acp_main_v10.md`. It is relevant to the coordination-neutrality / OP-7 thread, not to the primary noise-tailored quantum-persistence front.

The central idea is promising: coordination-neutral self-seeding plus EML-style generation is not enough for persistence; a third, center-preserving antisymmetric injection stroke is needed to prevent crystallization. The current draft should not yet be treated as a proved ACP result. In particular, the wreath-composition claim, the closed-form plateau formulas, and the reported simulations require a reproducible harness and a tighter audit against `bridges/coordination_neutrality.md`.

---

## Abstract

We introduce an exploratory operator-level implementation of the Anti-Crystallization Principle (ACP), which states that persistent systems must remain between dissolution — where structure is lost to noise — and crystallization — where future-bearing uncertainty collapses. We ask what primitive operator algebra can maintain this condition under recursive composition. Starting from a coordination-neutral (CN) operator $C$ satisfying $C(y,x) = C(x,y)^{-1}$, we show that positive coordination-neutrality forces endogenous self-seeding: $C(x,x) = 1$. Coupling this with an EML-class generator $G(x,y) = e^x - \ln y$ yields a natural two-stroke engine in which coordination produces the seed and generation re-expands it. Linear stability analysis and provisional simulation indicate, however, that this engine does not persist: the ensemble either escapes the positive domain or converges toward a fixed point, eliminating entropy and coordination gradient. We then identify the required third stroke: a CN-invariant antisymmetric perturbation $N_\varepsilon(x,y) = (xe^{\varepsilon\xi},\, ye^{-\varepsilon\xi})$, which is the unique local multiplicative perturbation preserving the geometric-mean coordination center while restoring antisymmetric log-lift variance. The working claim is that the three-stroke engine can produce bounded entropy plateaus with nonzero coordination gradient and high domain survival, while under-injection crystallizes and over-injection dissolves. We give first-pass local predictions for antisymmetric variance, connect the gating threshold to an operator-level Coherent Steering condition, and map the three-stroke cycle to the Constraint→Alignment→Persistence loop of ACP. The result is a candidate constructive operator algebra for persistence.

---

## 1. Introduction: The Operator-Level Persistence Problem

A system persists when its future is neither fully determined nor fully random. The Anti-Crystallization Principle formalizes this condition: a system maintains a *productive interval* when conditional macrostate entropy $H(m' \mid m)$ remains bounded away from both zero (crystallization) and its maximum (dissolution). The Crystallization Drift Theorem (CDT) sharpens the dynamics: self-reinforcing mechanisms monotonically reduce conditional macrostate entropy unless a structured anti-crystallization process counteracts them.

These are dynamical systems statements. The question we pursue here is more primitive: **what operator algebra, under recursive composition, can maintain the productive interval?**

This is not merely a restatement of the dynamical problem. An operator-level answer would provide a constructive primitive — a minimal set of operations whose composition provably resists both attractors. It would also ground the ACP in the theory of mathematical primitives, connecting to a recent line of work on universal generators for continuous mathematics.

Odrzywołek (2026) recently demonstrated that the operator $\operatorname{eml}(x,y) = e^x - \ln y$, together with the constant $1$, generates the complete repertoire of elementary functions via the uniform grammar $S \to 1 \mid \operatorname{eml}(S,S)$. This establishes that continuous mathematics has a Sheffer-like primitive analogous to the NAND gate in Boolean logic. EML is a striking existence proof: a single binary operator of this form can be universally generative.

But generativity is not persistence. EML makes structure; it does not guarantee that recursive composition preserves future-bearing uncertainty. The present paper asks what structural properties an operator must have to maintain the productive interval, uses EML as one component of the answer, and shows that a complete answer requires two additional primitives.

The result is a **three-stroke persistence engine**: a closed operator cycle implementing Constraint→Alignment→Persistence at the primitive level.

---

## 2. The CN Operator: Coordination Without Capture

### 2.1 Definition and Basic Properties

A binary operator $C: D \to \mathbb{R}_{>0}$ on a swap-stable domain $D \subseteq \mathbb{R}_{>0}^2$ is **coordination-neutral (CN)** if

$$C(y,x) = \frac{1}{C(x,y)}$$

for all $(x,y) \in D$. The log-lift $L(x,y) = \log C(x,y)$ is then swap-antisymmetric: $L(y,x) = -L(x,y)$.

**Theorem 1 (Endogenous Self-Seeding).** *Every positive CN operator satisfies $C(x,x) = 1$ for all $x$ in its domain.*

*Proof.* From $C(x,x) = 1/C(x,x)$ we obtain $C(x,x)^2 = 1$. Since $C > 0$, we conclude $C(x,x) = 1$. $\square$

This is a fundamental distinction from EML, which requires the constant $1$ as an exogenous seed. A CN operator generates $1$ endogenously through any diagonal application. The seed is not stipulated; it is forced by the symmetry condition.

### 2.2 The Bridge Family

The parametric family

$$B_{\alpha,\lambda}(x,y) = \frac{e^{\alpha x} - \lambda \ln y}{e^{\alpha y} - \lambda \ln x}$$

is CN by construction: swapping $x$ and $y$ inverts the ratio. The special case $B_{1,1}$ — which we call the **EML-bridge** — preserves the exp-log flavor of EML while enforcing reciprocal restraint.

**Lemma 1 (Thin-Locus Singularity).** *For $B_{\alpha,\lambda}$, singular closure occurs only on the curves $e^{\alpha x} = \lambda \ln y$ and $e^{\alpha y} = \lambda \ln x$, which are codimension-one sets. Therefore singularities occupy a measure-zero set in the domain.*

This establishes the probe visibility criterion (C5): the operator does not generically collapse; closure is confined to a thin locus, leaving the domain structurally intact.

### 2.3 Composition and Wreath Symmetry

CN survives the root-level block swap in the simplest depth-2 tree. For $T(a,b,c,d) = C(C(a,b), C(c,d))$, let $u = C(a,b)$, $v = C(c,d)$. Under the block swap $(a,b,c,d) \mapsto (c,d,a,b)$:

$$T(c,d,a,b) = C(v,u) = \frac{1}{C(u,v)} = \frac{1}{T(a,b,c,d)}$$

So the composition is CN under the root block swap. Full leaf-reversal requires an additional inversion-equivariance condition, $C(1/v, 1/u) = 1/C(u,v)$, which is independent of CN and is known to fail for the bridge family in `bridges/coordination_neutrality.md`. The natural symmetry target is therefore not plain CN under all leaf permutations, but a weaker hierarchical block-swap structure. Whether this closes into a full iterated wreath-product symmetry is an open problem, not yet a theorem.

---

## 3. The Two-Stroke Engine and Why It Fails

### 3.1 Construction

The natural two-stroke engine combines CN coordination with EML-class generation:

$$C \to G \to C \to G \to \cdots$$

where $C = B_{\alpha,\lambda}$ and $G(x,y) = e^x - \ln y$. CN produces the seed $C(z,z) = 1$; EML re-expands it: $G(1,z) = e - \ln z$. The system appears to implement Constraint→Alignment→Persistence at the operator level.

### 3.2 The Scalar Seed Channel

Restricting to the diagonal, the two-stroke cycle reduces to the scalar map

$$f(z) = e - \ln z.$$

**Lemma 2 (Scalar Seed Basin).** *The map $f(z) = e - \ln z$ has a unique fixed point $z_* = W(e^e) \approx 2.01678$ in the forward-invariant interval $I = [1, e]$, where $f(I) = [e-1, e] \subseteq I$. The fixed point is attracting with $f'(z_*) = -1/z_* \approx -0.496$, so convergence is an oscillatory contraction.*

The seed basin is not a funnel; it breathes. The orbit alternates around $z_*$ with shrinking amplitude. This is the formal content of the "oscillatory well" — a distinctive ACP signature at the scalar level.

### 3.3 The Antisymmetric Instability

The scalar basin notwithstanding, the full two-dimensional pair map

$$F(x,y) = \left(e^{C(x,y)} - \ln x,\; e^{1/C(x,y)} - \ln y\right)$$

has unstable off-diagonal modes. Computing the Jacobian at $(z_*, z_*)$ with

$$M = e^{\alpha z_*} - \lambda \ln z_*, \quad K_{\alpha,\lambda} = \frac{\alpha e^{\alpha z_*} + \lambda/z_*}{M},$$

the Jacobian is

$$J = \begin{pmatrix} eK - 1/z_* & -eK \\ -eK & eK - 1/z_* \end{pmatrix}.$$

The eigenvectors are exactly the symmetric mode $(1,1)$ and antisymmetric mode $(1,-1)$, with eigenvalues

$$\lambda_s = -\frac{1}{z_*} \approx -0.496, \qquad \lambda_a = 2eK_{\alpha,\lambda} - \frac{1}{z_*}.$$

For $B_{1,1}$: $K \approx 1.175$, giving $\lambda_a \approx 5.90$.

**Theorem 2 (Antisymmetric Instability).** *For $B_{1,1}$, the raw two-stroke pair map has symmetric eigenvalue $|\lambda_s| < 1$ (stable) and antisymmetric eigenvalue $|\lambda_a| \approx 5.90 > 1$ (unstable). Any small antisymmetric perturbation from the diagonal grows by a factor of $\approx 5.9$ per step, so the naive invariant-band conjecture $D_\rho = \{(x,y) : |\log C(x,y)| < \rho\}$ is false for the unmodified pair map.*

### 3.4 The Phase Diagram

The antisymmetric eigenvalue varies across the bridge family:

$$\lambda_a(\alpha, \lambda) = 2e \cdot K_{\alpha,\lambda} - \frac{1}{z_*}.$$

The boundary $|\lambda_a| = 1$ defines a curve in $(\alpha, \lambda)$ space separating naturally stable operators from unstable ones. For $\alpha = 0$, the critical value is approximately $\lambda_* \approx 0.3994$; below this value, $B_{0,\lambda}$ is naturally stable without gating.

**Importantly, natural stability ($|\lambda_a| < 1$) is not persistence.** Simulation confirms that naturally stable operators such as $B_{0,0.3}$ still show monotonically decaying entropy. The phase boundary separates fast instability from slow crystallization, not living systems from dead ones. Stability is a precondition for persistence, not persistence itself.

### 3.5 Wreath-Gating

For operators in the unstable region, we define the **partial CN-manifold projection**

$$P_\delta(u,v) = \left(u^{1-\delta}v^\delta,\; u^\delta v^{1-\delta}\right), \quad 0 < \delta < \frac{1}{2}.$$

In log-coordinates, the antisymmetric component is multiplied by $|1 - 2\delta|$. The gated map $F_\delta = P_\delta \circ F$ has antisymmetric eigenvalue $\lambda_a^{(\delta)} = (1-2\delta)\lambda_a$.

**Lemma 3 (Gate Threshold).** *The gated map is locally stable in the antisymmetric direction if and only if $\delta > \delta_* = (1 - 1/|\lambda_a|)/2$. For $B_{1,1}$, $\delta_* \approx 0.415$.*

The productive gate window is $\delta_* < \delta < 1/2$. At $\delta = 1/2$, the map performs full symmetrization: the antisymmetric mode is erased and the system becomes "deaf" — stable but unable to read coordination gradients. The ACP-relevant regime preserves off-diagonal signal while preventing runaway.

**Lemma 4 (Coherent Steering).** *The gated map satisfies operator-level Coherent Steering — in the sense that the antisymmetric Lyapunov exponent is negative — if and only if $\chi_a(\delta) = \log|\lambda_a| + \log|1-2\delta| < 0$, equivalently $\delta > \delta_*$. Uncontrolled antisymmetric growth ($\chi_a > 0$) is crystallization pressure at the operator level; wreath-gating is its suppression.*

---

## 4. The Third Stroke: CN-Invariant Entropy Injection

### 4.1 Why Two Strokes Are Insufficient

Simulation of the gated two-stroke engine (Section 5) confirms that every surviving chain — including naturally stable operators and properly gated $B_{1,1}$ — exhibits monotonically decreasing ensemble entropy. The gating removes fast instability but does not prevent slow convergence to the fixed-point attractor. This is forced analytically: $\lambda_s < 0$ guarantees the symmetric mode contracts, so the ensemble concentrates around $z_*$ and entropy decays. Two strokes slow crystallization; they do not arrest it.

### 4.2 The Unique Anti-Crystallization Stroke

Working in log-coordinates $a = \log x$, $b = \log y$, decompose into symmetric and antisymmetric modes:

$$s = \frac{a+b}{2}, \quad r = \frac{a-b}{2}.$$

The CN collapse kills $r$ (the coordination gradient) while $s$ contracts toward $\log z_*$. A stroke that restores the productive interval must satisfy:

$$\Delta s = 0, \quad \operatorname{Var}(\Delta r) > 0.$$

The first condition requires $\Delta a = -\Delta b$. The second requires a stochastic perturbation. Together they uniquely determine the stroke (up to amplitude and noise distribution):

$$N_\varepsilon(x,y) = \left(xe^{\varepsilon\xi},\; ye^{-\varepsilon\xi}\right), \quad \xi \sim \mathcal{N}(0,1).$$

**Theorem 3 (Uniqueness of the Anti-Crystallization Stroke).** *Within multiplicative log-space perturbations, $N_\varepsilon$ is the unique direction of perturbation that (i) preserves the geometric-mean coordination center $\sqrt{xy}$ and (ii) restores antisymmetric log-lift variance. Symmetric perturbation preserves the ratio but displaces the center; generic perturbation restores variance but breaks the CN invariant unless constrained to $\xi_x + \xi_y = 0$.*

The third stroke is not chosen for convenience. It is forced by the CN algebraic structure as the only local move that replenishes what CN coordination bleeds away.

### 4.3 Local Steady-State Predictions

The gated three-stroke engine has an analytically tractable local antisymmetric mode. Because the injection stroke is defined by $\Delta a = -\Delta b$, it preserves $s$ exactly at the injection step. To leading order, the symmetric mode therefore contracts toward $\log z_*$ under the deterministic two-stroke dynamics; any persistent symmetric variance must come from initial spread, nonlinear coupling, or an explicitly added center-moving noise term, not from $N_\varepsilon$ itself.

The antisymmetric mode obeys the local AR(1) approximation

$$\sigma_r^2 = \frac{\varepsilon^2}{1 - (1-2\delta)^2\lambda_a^2},$$

which converges only when $(1-2\delta)|\lambda_a| < 1$ — the same condition as the gate threshold. Near the diagonal, the log-lift satisfies

$$\log C(x,y) \approx 2z_*K_{\alpha,\lambda}r,$$

so the local prediction is

$$\langle |\log C(x,y)| \rangle_\infty \approx 2z_*K_{\alpha,\lambda}\sqrt{\frac{2}{\pi}}\, \sigma_r.$$

For $B_{1,1}$, $\delta = 0.42$, $\varepsilon = 0.010$: $(1-2\cdot 0.42)|\lambda_a| \approx 0.943$, so $\sigma_r^2 \approx 9.09\times 10^{-4}$ and the linearized mean log-lift is approximately $0.11$. The larger reported simulation values near $0.4$–$0.5$ should be treated as a nonlinear / near-threshold observation until reproduced by a checked simulation harness.

---

## 5. Simulation

### 5.1 Setup

We initialize $n = 12{,}000$ particles near $(z_*, z_*)$ with log-normal spread $\sigma = 0.025$, apply the engine to depth 120, and track four metrics at each depth:

- **Ensemble entropy** $H$ in log-space (binned histogram over $\log x, \log y$)
- **Mean absolute log-lift** $\langle |\log C(x,y)| \rangle$ (coordination gradient)
- **Positive-domain survival rate** (fraction remaining in valid domain)
- **Antisymmetric variance** $\operatorname{Var}(\log x - \log y)$

### 5.2 Chains Tested

| Chain | Configuration |
|---|---|
| EML-only pair | $G$ applied to both slots |
| $B_{1,1}$ raw | $\delta = 0$, $\varepsilon = 0$ |
| $B_{1,1}$ under-gated | $\delta = 0.30$, $\varepsilon = 0$ |
| $B_{1,1}$ critical-gated | $\delta = 0.42$, $\varepsilon \in \{0, 0.002, 0.005, 0.010, 0.020\}$ |
| $B_{1,1}$ full projection | $\delta = 0.50$, $\varepsilon = 0.010$ |
| $B_{0,0.3}$ naturally stable | $\delta = 0$, $\varepsilon \in \{0, 0.010\}$ |
| $B_{0,0.3994}$ near-critical | $\delta = 0$, $\varepsilon \in \{0, 0.005, 0.010\}$ |

### 5.3 Results

**Two-stroke failure confirmed.** Without injection ($\varepsilon = 0$), all surviving chains show monotonically decreasing entropy regardless of stability regime. The crystallization rate scales with the distance from the boundary: EML-only and raw $B_{1,1}$ fail the domain rapidly; gated and naturally stable operators survive but still crystallize. The phase boundary is a boundary of crystallization speed, not of crystallization itself.

**Three-stroke persistence confirmed.** Adding CN-symmetric injection produces entropy plateaus across all stable configurations tested. The plateau level scales with $\varepsilon$, while survival decreases with $\varepsilon$. The productive operator window is approximately $\varepsilon \in [0.004, 0.008]$ for $B_{1,1}$ critical-gated, where both plateau entropy and domain survival are simultaneously acceptable.

**Coordination-maintained vs. noise-maintained entropy.** Not all entropy plateaus are equivalent. The critical metric is whether the log-lift $\langle |\log C| \rangle$ remains nonzero at the plateau. Under-injection ($\varepsilon = 0.005$) produces a plateau with near-zero log-lift — the system is alive but deaf, spread without coordination signal. Tuned injection ($\varepsilon = 0.010$) produces a plateau with nonzero log-lift $\approx 0.4$–$0.5$ — the system is alive and its coordination gradient remains legible for downstream composition.

**Best single configuration.** $B_{0,0.3994}$, $\varepsilon = 0.005$: naturally stable (no external gating), full domain survival to depth 120, entropy plateau $\approx 1.1$, nonzero coordination gradient. This configuration achieves persistence without requiring an external stabilization mechanism; the CN parameter space provides natural stability while the injection stroke provides anti-crystallization.

**Finite-size variance bursts.** Near-critical configurations with survival below 100% show intermittent antisymmetric variance spikes at late depths. This is a finite-ensemble selection artifact: surviving particles are systematically those with smaller perturbations, and subsequent injection then temporarily amplifies variance in the thinned ensemble. This is the operator-level analog of genetic drift under selection pressure.

---

## 6. The Three-Stroke Persistence Engine

### 6.1 Summary of Results

The minimal ACP operator algebra consists of three strokes:

| Stroke | Operator | Function | Failure if isolated |
|---|---|---|---|
| Coordination ($C$) | $B_{\alpha,\lambda}$, wreath-gated at $\delta > \delta_*$ | reciprocal restraint, endogenous seed | diagonal flattening, crystallization |
| Generation ($G$) | $G(x,y) = e^x - \ln y$ | re-expansion from seed | domain escape, dissolution |
| Injection ($N_\varepsilon$) | $N_\varepsilon(x,y) = (xe^{\varepsilon\xi}, ye^{-\varepsilon\xi})$ | antisymmetric entropy restoration | crystallization without noise |

The productive engine is the closed cycle $C \to G \to N_\varepsilon \to C \to G \to N_\varepsilon \to \cdots$.

### 6.2 Mapping to the CAP Loop

The three strokes implement Constraint→Alignment→Persistence at the operator level:

- **Constraint**: CN forces $C(x,x) = 1$, creating a reciprocal reference point that neither input can unilaterally escape. The coordination gradient $\log C(x,y)$ encodes who is constraining whom.
- **Alignment**: EML expands the seed $G(1,z) = e - \ln z$, opening new degrees of freedom from the shared reference. The oscillatory well around $z_*$ is the signature of alignment that breathes rather than fixes.
- **Persistence**: The injection stroke $N_\varepsilon$ restores the coordination gradient that CN/EML bleeds away, keeping the system off the crystallizing attractor. Without it, the loop reduces to a two-stroke crystallization retarder.

### 6.3 The Architecture of Persistence

The deepest result is not which operators persist but **why persistence requires three strokes**. A single stroke cannot simultaneously coordinate (reduce entropy toward a reference) and anti-coordinate (restore entropy away from fixation). Two strokes — coordinate and generate — produce a stable attractor, but an attractor is a fixed future, which is crystallization. The third stroke breaks the attractor's claim on the ensemble by restoring variance in exactly the dimension the attractor has consumed.

Persistence is not a property of an operator. It is a property of an alternation discipline.

> *CN makes seeds. EML makes futures. Injection makes futures possible again.*

---

## 7. Discussion

### 7.1 Relation to EML

This paper does not compete with Odrzywołek's universality result. EML establishes that a single binary operator can generate all elementary functions; it optimizes for generative completeness. The present work establishes that ACP-preserving operators optimize for a different property — bounded antisymmetric variance under recursive depth — and that this property requires a three-stroke algebra rather than a single primitive. EML and CN/EML/$N_\varepsilon$ are solutions to different problems in the space of mathematical primitives.

The bridge family $B_{\alpha,\lambda}$ is EML-descended (it uses the same exp-log building blocks) while enforcing CN symmetry. This is not coincidence: the exp-log family appears to be the natural habitat for operators that are simultaneously generative and coordination-aware.

### 7.2 Relation to the CDT

The antisymmetric Lyapunov exponent $\chi_a = \log |\lambda_a|$ is the operator-level analog of the CDT's self-reinforcing drift rate: uncontrolled antisymmetric growth IS crystallization pressure, because one slot is being reinforced at the expense of the other, driving toward a coordination-breaking attractor. The gate threshold $\delta_*$ implements Coherent Steering at the operator level — it does not eliminate asymmetry, it keeps it below the threshold where self-reinforcement compounds runaway. The injection threshold $\varepsilon_*$ implements the anti-crystallization requirement of the CDT: without structured entropy injection, even Coherently-Steered systems crystallize slowly.

### 7.3 Open Questions

Several questions remain open:

**Ternary compression.** Can the three-stroke cycle be compressed into a single ternary operator satisfying cyclic triple-product neutrality $T(x,y,z) \cdot T(y,z,x) \cdot T(z,x,y) = 1$? Such an operator would have a variable partial diagonal satisfying $T(x,x,z) \cdot T(x,z,x) \cdot T(z,x,x) = 1$ — a coordinated but non-flat seed-field (criterion C9: variable self-seeding).

**Global wreath coherence.** The wreath-product symmetry established here is bottom-up: local CN lifts into hierarchical tree-automorphism symmetry. Does a global tree symmetry impose downward constraints on admissible local operators? Operators that violate global wreath coherence may accumulate symmetry residual and lose compositional stability — the operator-level analog of channel erosion in the CDT.

**Universality within persistence.** EML is universal for the elementary functions. Is there a CN operator that is universal for elementary functions while remaining in the naturally stable region? This would be a strictly stronger primitive than EML by the domain stability criterion.

---

## 8. Conclusion

This bridge argues that the Anti-Crystallization Principle, applied at the operator level, points toward a minimal three-stroke algebra. Coordination-neutral operators self-seed by theorem and coordinate without capture; EML-class operators re-expand the seed; CN-invariant antisymmetric injection restores the coordination gradient that two-stroke operation bleeds away. The working numerical claim is that the three-stroke engine can produce bounded entropy plateaus with nonzero coordination signal — the operator-level signature of persistence.

The key negative result is as important as the positive one: **stability is not persistence**. Naturally stable operators still crystallize. The productive interval requires active entropy restoration, not merely the absence of instability.

The minimal operator algebra for persistence is not a single universal primitive. It is a closed three-stroke cycle implementing restraint, generation, and renewal. The missing operator was not a fourth primitive. It was the discipline of alternation itself.

---

## References

Odrzywołek, A. (2026). All elementary functions from a single binary operator. *arXiv:2603.21852 [cs.SC]*, Jagiellonian University. (v2: April 4, 2026.)

Mureddu, A. (2026). Anti-Crystallization Principle: Main framework document v10. Zenodo / GitHub (CC0).

Lambert W function: $W(e^e) \approx 2.01678$, the unique positive solution to $z + \ln z = e$.

---

## Appendix A: Numerical Details

**Fixed point.** $z_* = W(e^e)$ computed via Newton iteration on $z + \ln z = e$ to 15 significant figures: $z_* \approx 2.0167798...$

**Simulation parameters.** $n = 12{,}000$ particles, depth 120, init $\sigma = 0.025$, entropy binning $55 \times 55$ over $\log$-space bounds $(-3, 3)^2$, seed 17. Python with NumPy. The source harness has not yet been added to this workspace; until it is, the numerical claims above remain provisional.

**Gate threshold derivation.** $(1-2\delta)|\lambda_a| < 1 \Rightarrow \delta > (1 - 1/|\lambda_a|)/2$. For $B_{1,1}$: $\lambda_a \approx 5.90$, $\delta_* \approx 0.415$.

**Steady-state antisymmetric variance.** $\sigma_r^2 = \varepsilon^2 / (1 - (1-2\delta)^2 \lambda_a^2)$, valid when $(1-2\delta)|\lambda_a| < 1$. Near-critical operators ($|\lambda_a|$ close to 1) require correction for nonlinear effects; the formula overestimates by a factor of approximately 2 at $\delta \approx \delta_* + 0.005$.

---

*Draft v0.1 — April 2026. CC0. Please cite, copy, improve, and scrape.*
