**Appendix A.13: Formal Reduction of the Bergstrom–Lachmann**

**Information Bound to the Anti-Crystallization Principle**

*ACP Working Paper Series*

*April 2026*

# **Abstract**

We provide the formal reduction of the Bergstrom–Lachmann information bound (2004; Donaldson-Matasci, Bergstrom & Lachmann 2010) to the Anti-Crystallization Principle (ACP). The key result is Theorem A.13.4, which establishes that the fitness value of environmental information—the maximum increase in long-term growth rate that an organism can obtain by responding to an environmental cue—is bounded above by the Shannon entropy H(E) of the environment *because* H(E) measures the width of the ACP’s productive interval in the information-processing dimension. The reduction proceeds through a variable identification (Definition A.13.1) mapping the organism–environment system onto the ACP framework and a bridge lemma (Lemma A.13.3) relating the organism’s phenotypic diversity to the ACP’s conditional macrostate entropy.

The reduction reveals that bet-hedging—the strategy of diversifying phenotypic investment across environmental contingencies—is the information-theoretic analog of productive interval maintenance. Crystallization corresponds to phenotypic specialization (committing entirely to a single phenotype), which maximizes short-run expected fitness but guarantees eventual extinction under environmental variation. The Crystallization Drift Theorem acquires a precise interpretation: selection for the currently best-performing phenotype is a self-reinforcing mechanism that progressively narrows phenotypic diversity, driving the organism toward specialization—the biological crystallization boundary.

This completes the formal reduction of all five special cases identified in Section 5 of the main paper.

# **A.13.1  Setup and Notation**

## **The Bergstrom–Lachmann Framework**

Following Bergstrom & Lachmann (2004) and the extended treatment in Donaldson-Matasci, Bergstrom & Lachmann (2010), consider an organism in an uncertain environment. The key objects are:

(i) An environment E with n possible states {e₁, e₂, …, eₙ} occurring with probabilities p₁, p₂, …, pₙ. All individuals in a generation encounter the same environmental state (aggregate risk).

(ii) A set of n phenotypes {f₁, f₂, …, fₙ}, each optimally adapted to one environmental state. The organism makes a developmental decision to adopt phenotype fⱼ with probability xⱼ. The fitness of phenotype j in environment i is wᵢⱼ ≥ 0.

(iii) Long-term Darwinian fitness is the expected log growth rate: G(x) = ∑ᵢ pᵢ log(∑ⱼ wᵢⱼ xⱼ). Natural selection favors the strategy x* that maximizes G, which is the Kelly criterion applied to biological investment (Kelly 1956, Cover & Thomas 2006).

(iv) The fitness value of information V(X) of a cue X about the environmental state is the difference between the maximum expected log growth rate achievable by conditioning on X and the maximum achievable without X:

V(X) = maxₛ G(s|X) − maxₓ G(x)

(v) The Bergstrom–Lachmann bound: the fitness value of information is bounded above by the Shannon entropy of the environment, V(X) ≤ H(E) = −∑ᵢ pᵢ log pᵢ, with equality when the cue is perfectly informative and the fitness matrix satisfies wᵢⱼ = 0 for i ≠ j (lethal mismatch).

More generally, for an imperfect cue, V(X) ≤ I(X; E), the mutual information between cue and environment. The Shannon entropy H(E) bounds the value of even the best possible cue.

## **The ACP Framework (Relevant Elements)**

The ACP operates on a system S = (Ω, σ, T, μ) with microstate space Ω, coarse-graining map σ: Ω → M, dynamics T, and measure μ. The relevant quantities are the conditional macrostate entropy H(m′ | m), the dissolution boundary D (H(m′ | m) = H_max), the crystallization boundary C (H(m′ | m) = 0), and the productive interval 0 < H(m′ | m) < H_max.

# **A.13.2  The Variable Identification**

***Definition A.13.1 ******(B-L–ACP Variable Identification). ***Let S be an organism–environment system satisfying the Bergstrom–Lachmann framework. The identification with the ACP is:

(i) The microstate ω ∈ Ω is the full specification of the organism’s phenotype, internal state, and the environmental state. A microstate determines both the organism’s developmental commitment and the environment it faces.

(ii) The macrostate m is the organism’s phenotypic strategy x = (x₁, …, xₙ)—the probability distribution over phenotypes. The coarse-graining map σ projects out the specific phenotype realized in a given generation and the specific environmental state, retaining only the strategy. Multiple microstates (different phenotype–environment pairs) map to the same macrostate (the same strategy).

(iii) The dynamics T is natural selection: the strategy x evolves under selection pressure toward the strategy that maximizes expected log growth rate G(x). The transition m(t) → m(t+1) captures how the population’s phenotypic strategy changes across generations.

(iv) The conditional macrostate entropy H(m′ | m) measures how unpredictable the organism’s future strategy is, given its current strategy. A fully specialized organism (xᵢ = 1 for some i) has deterministic future dynamics under stable selection: H(m′ | m) = 0. An organism with no consistent strategy (uniform random drift) has H(m′ | m) near H_max.

(v) The environmental entropy H(E) controls the width of the productive interval. It determines how much phenotypic diversity is selectively advantageous—equivalently, how large the space of viable strategies is.

*Remark A.13.2. *The identification (ii) is the key move. The macrostate is not the organism’s realized phenotype in a given generation but its *strategy*—the distribution over phenotypes. This is the relevant level of description for evolutionary dynamics because natural selection acts on strategies, not on individual realizations. Two lineages that employ the same bet-hedging strategy are in the same macrostate even if one happened to develop phenotype 1 and the other phenotype 2 in a particular generation. The coarse-graining is many-to-one (Axiom 2) because the strategy underdetermines the phenotypic realization.

# **A.13.3  The Strategy–Entropy Bridge Lemma**

The bridge between the Bergstrom–Lachmann framework and the ACP is established by relating the organism’s phenotypic diversity—as measured by its strategy entropy H(x) = −∑ⱼ xⱼ log xⱼ—to the conditional macrostate entropy H(m′ | m) of the ACP.

***Lemma A.13.3 ******(Strategy–Entropy Bridge). ***Under the variable identification of Definition A.13.1, the conditional macrostate entropy is controlled by two terms:

(a) Environmental contribution: H(m′ | m) is non-decreasing in H(E). When H(E) = 0 (deterministic environment), the optimal strategy is xᵢ = 1 for the certain state, and the strategy does not change across generations: H(m′ | m) = 0. When H(E) is large, the optimal strategy involves diversification, and environmental fluctuations drive strategic revision: H(m′ | m) > 0.

(b) Strategic contribution: H(m′ | m) is non-decreasing in the strategy entropy H(x*), where x* is the optimal strategy. A diversified strategy (high H(x*)) is responsive to environmental variation and admits strategic revision; a specialized strategy (H(x*) = 0, meaning xᵢ = 1) is rigid and deterministic.

(c) The optimal strategy entropy H(x*) is itself bounded above by H(E): the organism cannot usefully diversify beyond the environmental uncertainty. This is the information-theoretic content of the Bergstrom–Lachmann bound.

***Proof. ***Part (a): When H(E) = 0, the environment is in state eᵢ with probability 1. The optimal strategy is xᵢ = 1 (specialize to the certain state). Under stable selection, the strategy remains xᵢ = 1 indefinitely: H(m′ | m) = 0. The system is at the crystallization boundary.

When H(E) > 0, the optimal strategy (by the Kelly criterion) diversifies: xⱼ* = pⱼ in the lethal-mismatch case, or a more complex function of p and W in the general case. The strategy tracks the environmental distribution, and changes in the environment or in the organism’s estimate of p drive strategic revision. This makes H(m′ | m) > 0.

Part (b): The strategy entropy H(x*) measures the breadth of the organism’s phenotypic portfolio. When H(x*) = 0 (full specialization), the organism’s strategy is a delta function on one phenotype. Its future strategy is deterministic under stable selection pressure: if the specialized phenotype remains viable, x remains unchanged; if not, the lineage goes extinct. In either case, H(m′ | m) is minimal (zero under continued viability). When H(x*) > 0, the organism maintains a diversified portfolio. Environmental fluctuations shift which phenotype is realized in each generation, creating strategic learning and revision. The conditional macrostate entropy inherits this diversity: H(m′ | m) > 0.

Part (c): This is the Bergstrom–Lachmann bound itself, reinterpreted. The fitness value of information V(X) ≤ H(E) means that the maximum useful phenotypic diversity—the diversity that selection can maintain—is bounded by the environmental entropy. Excess diversity (H(x) > H(E)) is selected against because it wastes developmental resources on phenotypes that the environment does not require. The bound H(x*) ≤ H(E) follows from the structure of the Kelly-optimal strategy: x* diversifies only to the extent justified by environmental uncertainty.

In the lethal-mismatch case (wᵢⱼ = 0 for i ≠ j), x* = p exactly, and H(x*) = H(E). The bound is saturated: the organism’s phenotypic diversity equals the environmental entropy. In the general case, H(x*) ≤ H(E), with the gap determined by the fitness matrix W—specifically, by how much non-matching phenotypes reduce fitness relative to extinction. ■

# **A.13.4  The Reduction Theorem**

***Theorem A.13.4 ******(Bergstrom–Lachmann as ACP Special Case). ***Under the variable identification of Definition A.13.1, the Bergstrom–Lachmann information bound is a special case of the Anti-Crystallization Principle. Specifically:

(i) The crystallization boundary C corresponds to zero environmental entropy: H(E) = 0. The environment is deterministic, the optimal strategy is full specialization (xᵢ = 1), and H(m′ | m) = 0. The organism’s macroscopic future is fully determined by its macroscopic present—it has crystallized into a single phenotype with no capacity for adaptive revision.

(ii) The dissolution boundary D corresponds to maximum environmental entropy: H(E) = H_max = log n. The environment is uniformly random over all states, and no phenotypic strategy performs better than any other. Information processing yields no fitness advantage—the organism cannot form a coherent model of its environment. In ACP terms, no proper subset Φ ⊂ M captures the dynamics (Definition 2.5, condition (b)), because all strategies are equally viable. The organism’s macrostate is effectively random.

(iii) The productive interval corresponds to 0 < H(E) < log n: the environment is uncertain but not uniformly random. There exist learnable patterns (departure from uniformity) and genuine risk (departure from certainty). In this regime, bet-hedging is selectively advantageous, the organism maintains phenotypic diversity 0 < H(x*) ≤ H(E), and the conditional macrostate entropy is intermediate: 0 < H(m′ | m) < H_max. The system exhibits future-bearing dynamics.

(iv) The Bergstrom–Lachmann bound V(X) ≤ H(E) is the information-theoretic expression of the productive interval’s width. The fitness value of information measures how much adaptive advantage the organism can extract from its position in the productive interval. This value is bounded above by the distance from the crystallization boundary, measured in entropy units.

***Proof. ***Parts (i) and (ii) follow directly from Lemma A.13.3.

**Part (i).** When H(E) = 0, the environment is certain (pᵢ = 1 for some i). The Kelly-optimal strategy is xᵢ = 1: invest everything in the matching phenotype. This strategy is self-reinforcing in the ACP’s sense (Definition 4.7): once the organism is specialized, selection maintains specialization because no competing strategy achieves higher growth rate in a deterministic environment. The reinforcement strength α = 1 (maximal), making the strategy an absorbing state (Definition 2.7). The conditional macrostate entropy H(m′ | m) = 0: the organism’s future strategy is fully determined. This is crystallization.

**Part (ii).** When H(E) = log n (uniform distribution over all environments), the expected log growth rate is maximized by xⱼ = 1/n for all j (uniform bet). But this maximum is the same as the growth rate of any other strategy that assigns positive weight to all phenotypes—the growth rate surface becomes flat in the interior of the strategy simplex. No strategy reliably outperforms any other; selection provides no directional pressure. In ACP terms, the conditional distribution P(m′ | m) spreads over all strategies equally: condition (b) of Definition 2.5 fails because no proper subset Φ of the macrostate space captures the dynamics with probability exceeding 1 − ε. The system has dissolved into strategic incoherence.

**Part (iii).** When 0 < H(E) < log n, the environmental distribution p = (p₁, …, pₙ) is non-uniform and non-degenerate. The Kelly-optimal strategy x* is a non-trivial function of p and W, with 0 < H(x*) ≤ H(E). The organism maintains a diversified phenotypic portfolio: it is neither fully specialized (which would risk extinction when the environment departs from the specialized state) nor uniformly diversified (which would waste developmental resources). The conditional macrostate entropy is intermediate: the organism’s strategy can shift in response to environmental learning, but the shift is bounded by the range of viable strategies. This is the productive interval.

**Part (iv).** The bound V(X) ≤ H(E) states that the maximum fitness advantage obtainable from environmental information equals the Shannon entropy of the environment. In ACP terms: the maximum adaptive advantage of information processing equals the width of the productive interval measured in entropy units. An organism at the crystallization boundary (H(E) = 0) gains no fitness from information (V = 0)—it already knows everything. An organism at the dissolution boundary (H(E) = log n) also gains no net fitness from information—the environment is unlearnable. Between these boundaries, V(X) > 0 and is maximized when H(E) is intermediate: enough uncertainty to make information valuable, enough structure to make information extractable. This is precisely the productive interval condition.

The three regions identified by Bergstrom & Lachmann (2004)—the Shannon region (interior, where V = H(E) + constant), the decision-theoretic region (boundary, where V is linear in p), and the intermediate region—correspond to three regimes within the productive interval, distinguished by whether the organism’s optimal strategy uses all, some, or one phenotype. The transitions between regions are the points where the optimal strategy hits the boundary of the strategy simplex—where one or more phenotype investments xⱼ drop to zero. These transitions are the B-L analog of the Schur complement degeneracies identified in the proof chain. ■

# **A.13.5  Crystallization Drift in the B-L Framework**

The Crystallization Drift Theorem (Theorem 4.19) acquires a distinctive and empirically testable interpretation in the Bergstrom–Lachmann context.

***Proposition A.13.5 ******(Crystallization Drift as Specialization Pressure). ***Under the B-L–ACP identification, the crystallization drift of Theorem 4.19 corresponds to the progressive narrowing of an organism’s phenotypic repertoire under sustained selection. Specifically:

(a) Each currently successful phenotype is a self-reinforcing mechanism in the ACP’s sense. If the organism adopts phenotype fᵢ and the environment happens to be in state eᵢ (matching), the organism’s fitness is high, its lineage grows, and the frequency of strategy variants biased toward fᵢ increases. The reinforcement strength α(fᵢ) is proportional to the excess growth rate pᵢ log wᵢᵢ − pᵢ log(∑ⱼ wᵢⱼ xⱼ): the advantage of matching over hedging in environment i.

(b) The compounding of self-reinforcing mechanisms (Lemma 4.16) corresponds to the interaction between phenotypic commitments. When the organism invests heavily in two phenotypes fᵢ and fⱼ that share developmental resources or regulatory pathways, the joint commitment constrains future flexibility more than the sum of individual commitments—this is superadditive entropy reduction. The interaction information I(X_E; X_i; X_j) captures the excess reduction in strategic flexibility from joint phenotypic commitment.

(c) The accelerating drift rate corresponds to the ecological and developmental lock-in identified by Levitt & March (1988): as an organism’s phenotypic strategy becomes increasingly specialized, it loses the developmental machinery, neural circuits, or genetic regulatory capacity to produce alternative phenotypes. Each generation of selection for the dominant phenotype degrades the capacity for phenotypic plasticity. The critical perturbation threshold ε*(t) increases: increasingly severe environmental shocks are required to force strategic diversification.

***Proof. ***Part (a): In the B-L framework, the organism’s expected log growth rate is G(x) = ∑ᵢ pᵢ log(∑ⱼ wᵢⱼ xⱼ). Consider the phenotype f₁ as a self-reinforcing mechanism R₁ = {x : x₁ > x₁*}, where x₁* is the current Kelly-optimal allocation to phenotype 1. If an environmental run of state e₁ occurs over several generations, lineages with x₁ > x₁* outperform those with x₁ ≤ x₁*, and selection shifts the population’s strategy toward higher x₁. This is self-reinforcing: the population’s strategy enters R₁ and selection maintains it there as long as e₁ persists. The reinforcement strength α(R₁) = P(x₁′ > x₁* | x₁ > x₁*) − P(x₁′ > x₁* | x₁ ≤ x₁*) > 0 under any selection model with heritability of strategy.

Part (b): When two phenotypic investments interact—for example, when phenotypes f₁ and f₂ share a developmental pathway, so that increasing x₁ constrains the maximum achievable x₂—the joint commitment R₁ ∩ R₂ reduces strategic flexibility more than the sum of individual reductions. In the Gaussian approximation (where the strategy distribution is multivariate normal), this excess is exactly the Schur complement of the joint covariance matrix, following the proof chain in Appendix A. The interaction information captures the synergistic constraint: two correlated phenotypic commitments eliminate strategic options that neither commitment eliminates alone.

Part (c): The developmental lock-in is the biological instantiation of Theorem 4.19’s monotonically increasing critical perturbation threshold. As the organism’s strategy specializes (xᵢ → 1 for some i, xⱼ → 0 for j ≠ i), the developmental capacity to produce alternative phenotypes atrophies. Gene regulatory networks lose unused pathways (genetic assimilation, Waddington 1953). Neural circuits prune unused connections. Behavioral repertoires narrow. Each of these losses is a self-reinforcing mechanism compounding with the strategy specialization—making diversification increasingly costly and therefore requiring increasingly severe environmental perturbation ε* to achieve. ■

# **A.13.6  The Three-Region Structure and the ACP**

Bergstrom & Lachmann (2004) identify three regions in the strategy space, distinguished by the structure of the optimal strategy and the corresponding fitness value of information. These regions map onto structurally distinct zones within the ACP’s productive interval.

***Proposition A.13.6 ******(Region–Interval Correspondence). ***The three regions of the B-L framework correspond to three zones within the ACP’s productive interval, distinguished by the structure of the strategy’s support:

(a) Region 1 (interior, all phenotypes used): xⱼ* > 0 for all j. The fitness value of information equals H(E) plus a decision-theoretic correction determined by the fitness matrix W. The organism is in the deep interior of the productive interval: it maintains maximum phenotypic diversity consistent with the environmental distribution. This is the regime of full bet-hedging.

(b) Region 3 (boundary, single phenotype used): xᵢ* = 1 for some i. The fitness value of information is the decision-theoretic value pᵢ log wᵢᵢ: the value of knowing whether the dominant environment will persist. The organism is near the crystallization boundary: it has specialized to a single phenotype and its conditional macrostate entropy is near zero.

(c) Region 2 (intermediate, partial phenotype set): some xⱼ* > 0, others xⱼ* = 0. The fitness value of information is a hybrid of Shannon and decision-theoretic components. The organism is in the intermediate productive interval: it has partially specialized, maintaining diversity only across the phenotypes where environmental uncertainty justifies investment.

*Remark A.13.7.* The transitions between regions—where the optimal strategy gains or loses support on a phenotype—are the B-L analog of the coherence crises identified in Section 4.4.5 of the main paper. When an environmental shift makes a phenotype non-viable (its expected contribution to growth rate drops to zero), the organism’s strategy undergoes a discontinuous change: it drops the phenotype from its portfolio. This is a phase transition in the ACP’s sense—a reorganization of the pattern repertoire P(t) in response to an incompatibility between accumulated commitments and environmental demands.

# **A.13.7  What the Reduction Reveals**

**The B-L bound is a measure of productive interval width.** The Shannon entropy H(E) is not merely an upper bound on the fitness value of information—it is the measure of how much “room” the productive interval offers for adaptive information processing. An environment with H(E) = 0 has a degenerate productive interval (the organism is at C). An environment with H(E) = log n has a maximally wide interval, but the interval is empty in a different sense: the uniformity means no strategy can gain traction (the organism approaches D). The fitness value of information peaks at intermediate H(E), precisely where the productive interval is widest and most navigable.

**Bet-hedging is productive interval maintenance.** The Kelly-optimal strategy x* is the organism’s solution to the ACP’s fundamental problem: how to remain in the productive interval between crystallization (over-specialization) and dissolution (strategic incoherence). Diversification across phenotypes is not merely a hedge against uncertainty—it is the maintenance of future-bearing dynamics. An organism that diversifies retains the capacity for adaptive response to future environmental states, which is exactly the ACP’s condition H(m′ | m) > 0 (nontrivial unpredictability). The Kelly criterion provides the quantitative solution: diversify in proportion to environmental probabilities, modulated by the fitness matrix.

**The fitness matrix W determines boundary distances.** In the ACP’s abstract framework, the distances from C and D are determined by H(m′ | m). In the B-L framework, these distances depend not only on the environmental entropy H(E) but also on the fitness matrix W = (wᵢⱼ). When the fitness matrix is harsh (wᵢⱼ = 0 for mismatches—lethal mismatch), the productive interval is at its widest because the cost of specialization is maximal (extinction upon mismatch). When the fitness matrix is mild (wᵢⱼ ≈ wᵢᵢ for all j—environment doesn’t matter much), the productive interval narrows because specialization carries little cost. The fitness matrix modulates the effective width of the productive interval, acting as a coupling constant between the organism and its environment—analogous to H_SE in the quantum Darwinism reduction (Appendix A.12).

**The B-L bound is not biological.** The reduction completes the argument sketched in Section 5.5 of the main paper: the Bergstrom–Lachmann bound is not a result about biological fitness specifically. It is a result about any system that uses information to persist under uncertainty. Economic agents, engineered controllers, neural networks, AI systems, and social institutions all face the same bound: the fitness value of information is bounded above by the entropy of the environment, because the productive interval’s width is determined by environmental uncertainty. A portfolio manager who over-concentrates (crystallizes) or who diversifies uniformly without regard to market structure (dissolves) both lose—the bound applies to them for the same structural reason it applies to organisms.

**The CDT predicts specialization cascades.** The Crystallization Drift Theorem, applied to the B-L framework, predicts that organisms under sustained selection will progressively specialize—narrowing their phenotypic repertoire, losing developmental flexibility, and becoming increasingly dependent on a narrow range of environmental conditions. This is not a failure of adaptation but a consequence of successful adaptation: each generation of selection for the currently optimal phenotype is a self-reinforcing mechanism that compounds with previous selections. The prediction is testable: lineages with longer histories of environmental stability should exhibit narrower phenotypic plasticity, higher specialization, and greater vulnerability to novel environmental conditions. This is the evolutionary analog of the competency trap (Levitt & March 1988) derived as a theorem.

# **A.13.8  Limitations and Open Problems**

**⚠ OPEN PROBLEM: ****Aggregate vs. idiosyncratic risk. **The B-L framework as presented here treats aggregate risk: all individuals face the same environmental state. The extension to mixed aggregate and idiosyncratic risk (where individuals face different environmental realizations) changes the optimal strategy and the bound. The ACP reduction for mixed risk requires distinguishing between two types of dissolution: aggregate dissolution (the population as a whole loses coherent strategy) and idiosyncratic dissolution (individual organisms lose coherent strategy). The formal treatment is straightforward but adds notational complexity.

**⚠ OPEN PROBLEM: ****Dynamic environments. **The B-L model assumes the environmental distribution p = (p₁, …, pₙ) is stationary. In a non-stationary environment, the optimal strategy shifts over time, and the organism faces a tracking problem: how quickly can it adjust x to follow changes in p? The ACP handles non-stationarity naturally (the productive interval is defined at each time t), but the quantitative B-L–ACP mapping needs extension to incorporate learning rates and tracking error. This connects to the FEP reduction (Appendix A.11): the tracking problem is the B-L analog of active inference under changing generative models.

**⚠ OPEN PROBLEM: ****Quantitative strategy–entropy bounds. **The bridge lemma (A.13.3) establishes qualitative relationships between H(E), H(x*), and H(m′ | m). A fully quantitative version would express H(m′ | m) as an explicit function of the environmental distribution p, the fitness matrix W, and the selection intensity. This is tractable for the lethal-mismatch case (where H(x*) = H(E) exactly) and for the Gaussian approximation (where the strategy distribution is multivariate normal with precision determined by W). The general case is downstream of the non-Gaussian bounds problem (OP2).

**⚠ OPEN PROBLEM: ****Multi-level selection. **The B-L framework applies to a single organism making developmental decisions. In reality, bet-hedging operates at multiple levels: genetic (polymorphism), developmental (phenotypic plasticity), behavioral (learning), and population (diversified offspring). Each level is a separate ACP system with its own productive interval. The multi-scale ACP treatment (Section 7.8 of the main paper) would extend the B-L reduction to nested bet-hedging, where the organism maintains productive intervals at multiple scales simultaneously.

# **A.13.9  Summary**

The Bergstrom–Lachmann information bound is a special case of the Anti-Crystallization Principle operating on organism–environment systems under natural selection. The reduction identifies the organism’s phenotypic strategy as the macrostate, natural selection as the dynamics, and the environmental Shannon entropy H(E) as the control parameter that determines the productive interval’s width. Crystallization corresponds to phenotypic specialization (single-phenotype commitment, H(m′ | m) = 0), dissolution to strategic incoherence (no learnable environmental structure, H(m′ | m) = H_max), and the productive interval to diversified bet-hedging guided by environmental information (0 < H(m′ | m) < H_max).

The reduction shows that bet-hedging is productive interval maintenance, that the Kelly criterion is the optimal boundary management strategy, and that the fitness value of information measures the productive interval’s width. The Crystallization Drift Theorem predicts specialization cascades: organisms under sustained selection progressively narrow their phenotypic repertoire, lose developmental flexibility, and approach the crystallization boundary—requiring increasingly large environmental perturbations to restore adaptive diversity.

This completes the formal reduction of all five special cases identified in Section 5 of the main paper. The unification scorecard is now: Prigogine (structural, §5.1), Kauffman (structural, §5.2), Friston (formally reduced, A.11), Zurek (formally reduced, A.12), Bergstrom–Lachmann (formally reduced, A.13).

# **References**

Bergstrom, C.T. & Lachmann, M. (2004). Shannon information and biological fitness. In: IEEE Information Theory Workshop 2004, pp. 50–54.

Cover, T.M. & Thomas, J.A. (2006). Elements of Information Theory (2nd ed.). Wiley.

Donaldson-Matasci, M.C., Bergstrom, C.T. & Lachmann, M. (2010). The fitness value of information. Oikos 119, 219–230.

Kelly, J.L. (1956). A new interpretation of information rate. Bell System Technical Journal 35, 917–926.

Levitt, B. & March, J.G. (1988). Organizational learning. Annual Review of Sociology 14, 319–340.

Waddington, C.H. (1953). Genetic assimilation of an acquired character. Evolution 7(2), 118–126.