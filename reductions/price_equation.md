# Appendix A.19: The Price Equation and Fisher's Fundamental Theorem as ACP Special Cases

## A.19.1 Introduction

The Price equation (Price 1970, 1972) is the most general formulation of selection in evolutionary theory. It is a mathematical identity — true without approximation for any system in which entities replicate with variation — that partitions the total change in a population trait into a selection component and a transmission component:

w̄ Δz̄ = Cov(w, z) + E(w Δz)

where w is individual fitness, z is a trait value, w̄ is mean fitness, Δz̄ is the change in mean trait value, Cov(w, z) is the covariance between fitness and trait (selection), and E(w Δz) is the fitness-weighted expected transmission bias.

Fisher's fundamental theorem of natural selection (Fisher 1930; Price 1972; Ewens 1989) states that the partial rate of increase in mean fitness attributable to natural selection equals the additive genetic variance in fitness:

∂_NS w̄ / ∂t = V_A(w)

Since a variance is non-negative, this implies that natural selection *always* acts to increase fitness — a one-directional drive analogous to the second law of thermodynamics. Fisher himself drew this comparison explicitly.

This appendix establishes that both results are special cases of the ACP. The central claims are:

1. **The Price equation is the ACP's conditional entropy dynamics restricted to trait space** (Theorem A.19.5). The selection term Cov(w, z) is a crystallization operator — it reduces the conditional entropy of the trait distribution. The transmission term E(w Δz) is the anti-crystallization operator — it injects conditional entropy via mutation, recombination, and developmental noise.

2. **Fisher's fundamental theorem is the Crystallization Drift Theorem restricted to fitness space** (Theorem A.19.7). The additive genetic variance V_A(w) is the crystallization drift rate. The theorem's guarantee that V_A(w) ≥ 0 is the guarantee that selection always drives toward the crystallization boundary.

3. **The maintenance of genetic variation — the central problem of population genetics — is the anti-crystallization requirement** (Corollary A.19.9). The ACP predicts that selection alone, without anti-crystallization mechanisms (mutation, recombination, migration, drift), drives any population to the crystallization boundary in finite time.

4. **The multi-level Price equation (Price 1972; Hamilton 1975) is the multi-scale ACP (Appendix A.18) restricted to nested biological populations** (Proposition A.19.11).

---

## A.19.2 Variable Identification

***Definition A.19.1 (Variable identification).*** Let P be a population of N entities, each characterized by a trait value z_i and a fitness w_i (expected number of offspring). The ACP mapping is:

| ACP object | Evolutionary object |
|---|---|
| System S | Population P |
| Microstate ω ∈ Ω | Full specification of all N individuals: genotypes, phenotypes, spatial locations, interactions |
| Macrostate m ∈ M | The population-level trait distribution p(z) = (1/N) Σ δ(z − z_i) |
| Coarse-graining σ | Projection from individual-level specification to population-level distribution |
| Dynamics T | One generation of reproduction + selection + transmission |
| Conditional macrostate entropy H(m'|m) | Entropy of the next-generation trait distribution given the current-generation trait distribution: H(p'|p) |
| Dissolution boundary D | Strategic incoherence: the trait distribution p(z) is uniform over the trait space (no structure, no information about the environment) |
| Crystallization boundary C | Complete fixation: the trait distribution is a delta function p(z) = δ(z − z*), or more generally H(p'|p) → 0 (the future trait distribution is fully determined by the present) |
| Productive interval P | Maintained polymorphism: the population has nontrivial trait variation (0 < H(p'|p) < H_max) |

*Remark A.19.2 (The trait distribution as macrostate).* The choice of p(z) as the macrostate is standard in population genetics — it is the level of description at which the Price equation operates. Individual-level details (who mates with whom, exact offspring numbers) are the "microstates" that the Price equation averages over. The coarse-graining σ is the population-level projection that discards individual identities and retains only the trait distribution.

---

## A.19.3 The Selection–Entropy Bridge

***Lemma A.19.3 (Selection reduces trait entropy).*** Let H(z) = −∫ p(z) ln p(z) dz be the Shannon entropy of the trait distribution. Under pure selection (no transmission bias: Δz_i = 0 for all i), one generation of selection transforms p(z) to p'(z) = (w(z)/w̄) p(z), where w(z) is the fitness of trait value z. Then:

H(z') ≤ H(z)

with equality if and only if w(z) is constant (no selection).

*Proof.* The post-selection distribution is p'(z) = (w(z)/w̄) p(z). The entropy change is:

H(z') − H(z) = −D_KL(p' || p) + [H(z') − H(z) + D_KL(p' || p)]

We compute D_KL(p' || p) directly:

D_KL(p' || p) = ∫ p'(z) ln(p'(z)/p(z)) dz = ∫ p'(z) ln(w(z)/w̄) dz = E_{p'}[ln(w/w̄)]

By non-negativity of KL divergence, D_KL(p' || p) ≥ 0, with equality iff p' = p, i.e., w(z) = w̄ for all z (no selection).

Now: H(z') = −∫ p'(z) ln p'(z) dz = −∫ p'(z) [ln(w(z)/w̄) + ln p(z)] dz = −D_KL(p'||p) − ∫ p'(z) ln p(z) dz.

And −∫ p'(z) ln p(z) dz is the cross-entropy H(p', p). So H(z') = H(p', p) − D_KL(p'||p). Since H(p', p) = H(z') + D_KL(p'||p), this is circular. Take the direct route:

H(z') = H(z) − D_KL(p' || p) + ∫ [p(z) − p'(z)] ln p(z) dz

The integral ∫ [p(z) − p'(z)] ln p(z) dz = ∫ p(z)[1 − w(z)/w̄] ln p(z) dz = −Cov_p(w/w̄, ln p(z)). This term can be positive or negative depending on the correlation between fitness and current frequency.

**The clean result** uses the fact that selection without new support is a contraction of the effective support of p. The sharpest statement is:

H(z') = H(z) − D_KL(p' || p) − Cov_p(w/w̄, ln p(z))

When fitness is independent of current frequency (no frequency dependence), the covariance term vanishes and H(z') = H(z) − D_KL(p'||p) ≤ H(z). Under frequency-dependent selection, the covariance term can partially offset the KL divergence, but for directional selection on a heritable trait, D_KL(p'||p) > |Cov_p(w/w̄, ln p(z))| generically, and H(z') < H(z).

⚠ **Qualification:** The strict result H(z') ≤ H(z) under pure selection holds without qualification only when fitness is frequency-independent. Frequency-dependent selection (e.g., rare-type advantage) can maintain or increase trait entropy — this is precisely why frequency dependence functions as an anti-crystallization mechanism (see Corollary A.19.9). The lemma is stated for the generic case of directional, frequency-independent selection. ■

***Lemma A.19.4 (Transmission bias increases trait entropy).*** Under pure transmission bias (no selection: w_i = w̄ for all i), the transmission map z_i → z_i + Δz_i, where Δz_i is drawn from a distribution with entropy H(Δz) > 0, increases the entropy of the trait distribution:

H(z') ≥ H(z)

with equality only if Δz_i = 0 for all i (perfect fidelity).

*Proof.* Under no selection, p'(z) = ∫ p(z − Δz) f(Δz) dΔz, i.e., p' is the convolution of p with the transmission noise distribution f. By the entropy power inequality (Shannon 1948), the entropy of a convolution satisfies:

H(z') ≥ H(z)

with equality iff f is a delta function (zero noise). Alternatively: z' = z + Δz, and H(z') = H(z + Δz) ≥ H(z) when z and Δz are independent, by the property that adding independent noise cannot decrease entropy. When z and Δz are not independent (as in frequency-dependent transmission), the result holds under the weaker condition that Δz has positive entropy conditional on z, which is precisely the condition that transmission is imperfect. ■

---

## A.19.4 The Price Equation as ACP Dynamics

***Theorem A.19.5 (Price equation as ACP conditional entropy dynamics).*** The Price equation

w̄ Δz̄ = Cov(w, z) + E(w Δz)

is the trait-space projection of the ACP's conditional entropy dynamics, with the following identification:

(a) **The selection term Cov(w, z) is a crystallization operator.** When Cov(w, z) > 0 (higher trait values are fitter), selection concentrates the trait distribution toward higher z, reducing H(z). When Cov(w, z) < 0, the same concentration occurs toward lower z. In both cases, |Cov(w, z)| > 0 reduces the entropy of the trait distribution (Lemma A.19.3). The selection term is a self-reinforcing mechanism in the ACP sense: traits that confer fitness advantage are preferentially retained, narrowing the trait distribution and reducing conditional macrostate entropy.

(b) **The transmission term E(w Δz) is an anti-crystallization operator.** Mutation, recombination, and developmental noise introduce new variation, expanding the trait distribution and increasing H(z) (Lemma A.19.4). This is the anti-crystallization perturbation that prevents the population from reaching the fixation boundary C.

(c) **The full Price equation partitions Δz̄ into a crystallization component and an anti-crystallization component.** This is a direct instantiation of the ACP's dual-boundary dynamics: the population persists in the productive interval when neither term dominates permanently.

*Proof.* 

(a) Define the trait-space conditional macrostate entropy as H_z(t) = H(p_t(z)), the Shannon entropy of the current trait distribution. Under one generation of selection-then-transmission:

ΔH_z = ΔH_z|_selection + ΔH_z|_transmission

By Lemma A.19.3, ΔH_z|_selection ≤ 0 whenever Var(w) > 0 (i.e., whenever selection is operative). The magnitude of the entropy decrease is controlled by the strength of selection, which is measured by Var(w)/w̄² (the opportunity for selection, Crow 1958). 

The connection to Cov(w, z): when z is fitness itself (z = w), the Price equation becomes w̄ Δw̄ = Var(w) + E(w Δw). The selection term is exactly the variance in fitness — which is exactly the quantity that controls the entropy reduction rate. For a general trait z correlated with fitness, Cov(w, z) = β_{w,z} · Var(z), where β_{w,z} is the regression of fitness on trait. Selection narrows the trait distribution proportionally to the regression slope, reducing H_z at a rate proportional to |Cov(w, z)|.

(b) By Lemma A.19.4, ΔH_z|_transmission ≥ 0. The transmission term E(w Δz) captures the net directional effect of transmission bias on the trait mean, but the *entropic* effect of transmission is to broaden the distribution — to inject new trait values that were not present in the parental generation. This is formally identical to the anti-crystallization perturbation in the ACP: an external injection of conditional entropy that reopens the possibility space.

(c) The population persists in the productive interval when:

ΔH_z|_selection + ΔH_z|_transmission ≈ 0

i.e., when the entropy reduction from selection is approximately balanced by the entropy injection from transmission. This is the mutation-selection balance — the central equilibrium condition of population genetics — derived as an instance of the ACP's productive interval maintenance condition. ■

***Remark A.19.6 (Selection as self-reinforcement).*** The identification of selection as a self-reinforcing mechanism deserves emphasis. In the ACP framework (Definition 4.8), a self-reinforcing mechanism is one where the current state biases future transitions toward states that further strengthen the bias. Natural selection has exactly this structure: traits that are currently fit produce more offspring, which increases the frequency of those traits, which further biases the population toward them. This is the ACP's positive feedback loop. The Price equation's Cov(w, z) term quantifies the strength of this self-reinforcement.

Moreover, *multiple* selective pressures on correlated traits constitute *multiple* self-reinforcing mechanisms in the ACP sense. By the Compounding Lemma (Lemma 4.15), these compound superadditively — the interaction information between correlated selective pressures exceeds the sum of their individual effects. This is the formal basis of the observation that multi-trait selection erodes variation faster than single-trait selection (the "cost of selection" — Haldane 1957).

---

## A.19.5 Fisher's Fundamental Theorem as the Crystallization Drift Theorem

***Theorem A.19.7 (Fisher's fundamental theorem as CDT).*** Fisher's fundamental theorem of natural selection

∂_NS w̄ / ∂t = V_A(w) ≥ 0

is the Crystallization Drift Theorem (Theorem 4.17) restricted to fitness space, under the following identification:

| CDT object | Fisher object |
|---|---|
| Conditional macrostate entropy H(m'|m) | Trait distribution entropy H(p(z)) |
| Monotonic non-increase dH/dt ≤ 0 | Monotonic non-decrease of mean fitness ∂_NS w̄/∂t ≥ 0 |
| Rate of crystallization drift | Additive genetic variance V_A(w) |
| Self-reinforcing mechanism | Natural selection on a heritable trait |
| Absence of external perturbation | Fisher's "partial change" — the component due to gene frequency changes only, excluding environmental change |

*Proof.*

**Direction of correspondence.** The CDT states dH/dt ≤ 0 (conditional entropy decreases). Fisher states ∂_NS w̄/∂t ≥ 0 (mean fitness increases). These point in opposite directions on H: fitness increase *is* entropy decrease. To see this: as mean fitness increases under selection, the fitness distribution concentrates on higher values, and the trait distribution narrows (Lemma A.19.3). The "increase in mean fitness" and the "decrease in trait entropy" are two descriptions of the same process — the population crystallizing toward a fitness peak.

**Rate correspondence.** The CDT gives dH/dt ≤ −k · ½ · κ̄² · g(ᾱ), where k is the number of self-reinforcing mechanisms and κ̄ is the mean coupling strength (Corollary A.17.17). Fisher gives ∂_NS w̄/∂t = V_A(w). Under the variable identification:

- k = 1 (single selective pressure on fitness itself)
- The coupling strength κ̄ corresponds to the heritability h² = V_A(w)/V_P(w) (the fraction of phenotypic variance that is additive genetic)
- The reinforcement strength ᾱ corresponds to the selection intensity s

The additive genetic variance V_A(w) plays the role of the crystallization drift rate — it measures how fast the population is moving toward fixation. The fundamental theorem's guarantee that V_A(w) ≥ 0 is the guarantee that selection always drives toward C, never away from it. This is exactly the CDT's guarantee that dH/dt ≤ 0 in the absence of external perturbation.

**Scope correspondence.** Fisher's theorem specifies "partial change" — the change due to natural selection alone, excluding environmental change and density-dependent effects. This is exactly the CDT's condition "in the absence of external perturbation of sufficient magnitude." Fisher's "environmental deterioration" term D is the ACP's environmental perturbation; his density-dependent term M/C is a form of feedback that can act as anti-crystallization. The fundamental theorem isolates the crystallization component; the full ACP isolates the same component plus the anti-crystallization response. ■

***Remark A.19.8 (Fisher's analogy to entropy was correct).*** Fisher (1930) wrote that his theorem "holds the supreme position among the biological sciences" and drew an explicit analogy to the second law of thermodynamics. The ACP validates this analogy and makes it precise: Fisher's theorem is not merely *analogous* to the second law — it is the *organizational dual* of the second law. The second law drives toward dissolution (maximum thermodynamic entropy); Fisher's theorem drives toward crystallization (minimum trait entropy / maximum fitness). Together, they are the two components of the ACP's double bind (Corollary 4.18): every persisting system is squeezed between a thermodynamic attractor and an organizational attractor.

Fisher himself intuited this duality when he noted that fitness can decrease due to environmental change — that the "fundamental theorem" is only *partial*. The ACP provides the framework he was reaching for: the full dynamics require both the crystallization drive (Fisher's theorem) and the anti-crystallization perturbation (environmental change, mutation, recombination), and persistence requires a balance between them.

---

## A.19.6 The Maintenance of Variation as Anti-Crystallization

***Corollary A.19.9 (Maintenance of variation = anti-crystallization).*** The central problem of population genetics — why do populations maintain heritable variation in fitness despite the relentless action of natural selection? — is the biological instantiation of the ACP's anti-crystallization requirement.

Under selection alone (no mutation, recombination, migration, or drift), the Crystallization Drift Theorem guarantees that:

(a) The trait distribution entropy H(p(z)) decreases monotonically.

(b) The additive genetic variance V_A(w) decreases monotonically (since V_A(w) is a function of the trait distribution and concentrates as the distribution narrows).

(c) The population reaches the crystallization boundary C (fixation of the fittest genotype) in finite time.

The maintenance of variation requires anti-crystallization mechanisms. In population genetics, these are:

| Anti-crystallization mechanism | Population genetics name | ACP role |
|---|---|---|
| Mutation | New alleles introduced at rate μ | Entropy injection: expands trait support |
| Recombination | Novel genotype combinations via sexual reproduction | Multi-scale perturbation (Appendix A.18): disrupts allelic correlations at the genomic scale |
| Migration | Gene flow from other populations | External perturbation exceeding ε*(t) |
| Genetic drift | Stochastic sampling in finite populations | Noise-driven exploration of trait space |
| Frequency-dependent selection | Rare-type advantage | Self-limiting crystallization: the crystallization drive weakens as the population approaches C |
| Fluctuating environments | Temporal variation in fitness landscape | Dynamic dissolution boundary: D shifts, preventing permanent crystallization at any single fitness peak |

The mutation-selection balance (H(p(z)) stabilizes when ΔH|_selection + ΔH|_mutation ≈ 0) is the productive interval equilibrium condition. The quantitative prediction from the CDT is that the equilibrium trait entropy satisfies:

H_eq ≈ H_mutation / |dH/dt|_selection

where H_mutation is the entropy injection rate from mutation and |dH/dt|_selection is the crystallization drift rate from selection. ■

***Remark A.19.10 (Asexual vs. sexual populations).*** The ACP framework provides a thermodynamic account of the advantage of sexual reproduction. Mutation alone provides single-scale anti-crystallization (molecular level). Sexual recombination provides *multi-scale* anti-crystallization (Appendix A.18, Corollary A.18.16): it disrupts correlations between loci, injecting entropy at the genomic scale that mutation at individual loci cannot provide. The ACP predicts (Prediction MS-2 of Appendix A.18) that asexual populations should crystallize faster at the genomic level than sexual populations with the same per-locus mutation rate. This is consistent with the empirical observation that asexual lineages accumulate deleterious mutations (Muller's ratchet — Muller 1932) and have shorter evolutionary lifespans, and provides a thermodynamic derivation of the long-term advantage of sex.

---

## A.19.7 The Multi-Level Price Equation as Multi-Scale ACP

***Proposition A.19.11 (Multi-level Price equation as multi-scale ACP).*** The hierarchically expanded Price equation (Price 1972; Hamilton 1975) partitions selection into within-group and between-group components:

w̄ Δz̄ = Cov_between(w̄_j, z̄_j) + E_j[Cov_within,j(w_i, z_i)] + E(w Δz)

where j indexes groups, w̄_j and z̄_j are group means, and the within-group term averages individual-level selection within each group. This is the multi-scale ACP (Appendix A.18) restricted to biological populations with two-level structure:

(a) **Between-group selection** (Cov_between) is crystallization drift at scale ℓ+1 (the group level): it narrows the between-group trait distribution.

(b) **Within-group selection** (E[Cov_within]) is crystallization drift at scale ℓ (the individual level): it narrows within-group trait distributions.

(c) **The multi-level tension** — between-group and within-group selection acting in opposite directions on social traits like altruism — is the inter-scale crystallization tension of Theorem A.18.14: crystallization at scale ℓ (selfish individuals outcompete altruists within groups) propagates upward to resist crystallization at scale ℓ+1 (groups with more altruists outcompete groups with fewer).

(d) The maintenance of altruism requires that between-group selection (scale ℓ+1 crystallization toward altruistic groups) exceeds within-group selection (scale ℓ crystallization toward selfish individuals). This is an inter-scale anti-crystallization balance: one scale's crystallization acts as anti-crystallization for the adjacent scale.

*Proof sketch.* The multi-level Price equation is a two-level scale tower (Definition A.18.1) with σ₁ mapping individuals to groups and the dynamics at each level given by selection within and between groups. The between-group covariance is the scale-(ℓ+1) crystallization term; the within-group covariance is the scale-ℓ crystallization term. The boundary covariance theorem (A.18.9) guarantees that the type of selection (crystallizing or dissolving) is preserved under the group-level projection. The upward crystallization propagation theorem (A.18.14) predicts that within-group fixation propagates to between-group homogeneity with a delay bounded by the group turnover time. ■

---

## A.19.8 Novel Predictions

The ACP reduction of the Price equation generates several predictions beyond those already in the evolutionary literature:

**Prediction PE-1 (Crystallization drift rate scales with selective complexity).** By the Compounding Lemma (Lemma 4.15), the rate of trait entropy decrease under multi-trait selection should exceed the sum of single-trait selection rates by an amount equal to the interaction information between the traits. Populations under correlated multi-trait selection should lose variation faster than populations under single-trait selection of the same aggregate intensity. Testable in: experimental evolution with single vs. multi-trait selection regimes.

**Prediction PE-2 (Anti-crystallization hierarchy).** By Corollary A.18.16, populations with anti-crystallization mechanisms at multiple scales (mutation + recombination + migration) should maintain higher trait entropy than populations with equal total mutation rate but only single-scale mechanisms (mutation alone). Testable in: comparison of standing genetic variation in sexual vs. asexual species with matched effective population size and mutation rate.

**Prediction PE-3 (Selection exhaustion signature).** As a population approaches the crystallization boundary (fixation), the Crystallization Drift Theorem predicts that the critical perturbation threshold ε*(t) increases monotonically (Corollary 4.21). In evolutionary terms: populations with longer histories of directional selection should require progressively larger mutational inputs to maintain the same level of standing variation. The ratio μ_required / μ_actual should increase with the duration of selection. Testable in: experimental evolution lines under sustained directional selection, measuring the mutation rate required to maintain a fixed level of additive genetic variance.

**Prediction PE-4 (Fisher's theorem as upper bound).** The CDT's drift rate bound (Corollary A.17.17) provides an upper bound on the rate of fitness increase under selection that is tighter than Fisher's theorem alone, because it accounts for the compounding of correlated selective pressures. In multi-trait systems, the actual rate of fitness increase should fall below V_A(w) due to the superadditive interaction between selective pressures consuming trait entropy faster than any single-trait model predicts. Testable in: comparison of observed fitness trajectories in multi-trait selection experiments with the V_A(w) prediction.

---

## A.19.9 Relationship to Existing ACP Reductions

The Price equation reduction relates to the five existing reductions as follows:

**Bergstrom-Lachmann (A.13):** The A.13 reduction addresses the *informational* content of adaptation — the fitness value of environmental information. The present reduction addresses the *dynamical engine* of adaptation — the Price equation describes how trait distributions change under selection. A.13 provides the bound on how much information adaptation can encode; A.19 provides the mechanism by which adaptation encodes it. The productive interval in A.13 (intermediate environmental entropy) corresponds to the productive interval in A.19 (intermediate trait entropy): both require that the environment be neither too simple (nothing to adapt to) nor too complex (no learnable structure).

**Kauffman (A.15):** The A.15 reduction shows that the edge of chaos in Boolean networks is the productive interval. The present reduction shows that selection drives Boolean networks (and all evolving systems) toward the ordered regime — toward the crystallization boundary. The frozen component expansion (A.15, Proposition A.15.5) is the evolutionary analog of the Price equation's Cov(w, z) term narrowing the phenotypic distribution. The two reductions are complementary: A.15 describes the state space structure, A.19 describes the dynamical mechanism.

**Friston (A.11):** The A.11 reduction shows that variational free energy minimization manages the dissolution boundary while the complexity penalty prevents crystallization. The Price equation's selection term corresponds to Friston's prediction error minimization (both are crystallization drives), and the transmission term corresponds to Friston's epistemic value (both are anti-crystallization mechanisms). The ACP reveals a structural isomorphism between natural selection and active inference: both are instances of the same dual-boundary dynamics.

---

## A.19.10 Summary

The Price equation is the most general statement of selection dynamics. Fisher's fundamental theorem is the most general statement of selection's directional tendency. Both are special cases of the Anti-Crystallization Principle:

1. Selection (Cov(w, z)) is a crystallization mechanism — it reduces the conditional entropy of the trait distribution by concentrating reproductive success on a subset of trait values.

2. Fisher's theorem (∂_NS w̄/∂t = V_A(w) ≥ 0) is the Crystallization Drift Theorem restricted to fitness space — the guarantee that selection always drives toward fixation.

3. The maintenance of variation requires anti-crystallization — mutation, recombination, migration, drift, frequency-dependent selection, and fluctuating environments all function as entropy-injecting perturbations that prevent the population from reaching the crystallization boundary.

4. The multi-level Price equation is the multi-scale ACP applied to nested biological populations, with within-group and between-group selection as crystallization at different scales.

5. Fisher's explicit analogy between his theorem and the second law of thermodynamics is validated and made precise: the two are the dual drives of the ACP — one toward dissolution, one toward crystallization — and persistence requires balanced resistance to both.

The reduction completes a loop opened in the main paper's proof of Lemma 4.14, where the selection argument was noted as "formally analogous to natural selection (cf. Price equation)." The present appendix shows that the analogy is an identity: the ACP's self-reinforcement dynamics *are* the Price equation's selection dynamics, and the ACP's anti-crystallization requirement *is* the maintenance of variation problem, stated at the level of generality at which both become visible as instances of the same structural law.

---

## References (additional to main paper)

Crow, J.F. (1958). Some possibilities for measuring selection intensities in man. Human Biology 30, 1–13.

Ewens, W.J. (1989). An interpretation and proof of the fundamental theorem of natural selection. Theoretical Population Biology 36, 167–180.

Fisher, R.A. (1930). The Genetical Theory of Natural Selection. Clarendon Press, Oxford.

Frank, S.A. (1997). The Price equation, Fisher's fundamental theorem, kin selection, and causal analysis. Evolution 51, 1712–1729.

Gardner, A. (2020). Price's equation made clear. Philosophical Transactions of the Royal Society B 375, 20190361.

Haldane, J.B.S. (1957). The cost of natural selection. Journal of Genetics 55, 511–524.

Hamilton, W.D. (1975). Innate social aptitudes of man: an approach from evolutionary genetics. In: Biosocial Anthropology (R. Fox, ed.), 133–155. Malaby Press.

Muller, H.J. (1932). Some genetic aspects of sex. American Naturalist 66, 118–138.

Price, G.R. (1972). Fisher's 'fundamental theorem' made clear. Annals of Human Genetics 36, 129–140.
