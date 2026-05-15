# Generativity Criterion — the ACP applied to theory evolution

*Status: proposed bridge. Core reduction: **conjectured**, with the structural argument laid out below. Some sub-claims are **proven** as immediate consequences of results already in the paper; others are flagged **open** and migrated to `OPEN_PROBLEMS.md`.*

*Companion essay: `essays/the_incompleteness_quartet.md`.*

---

## 1. Motivation

The usual objection to totalizing theories — "if it explains everything, it explains nothing" — is a blunt instrument. A theory can explain a wide range of phenomena without being totalizing, and a theory can be narrow without being modest. What matters is not the *scope* of a theory but its *generativity*: does it open more inquiry than it closes?

This document formalizes that intuition and shows it is a direct application of the Anti-Crystallization Principle (ACP) to the object-level system consisting of *a theory and its inquiry-space*. The punchline is that the generativity criterion is not an aesthetic preference for theory-builders. It is the same structural law as the CDT, applied one level up: theories that are alive enough to persist as research programs are the theories that cannot crystallize on their own domains.

A corollary — which matters for the self-consistency of the ACP program itself — is that the ACP is subject to the rule it states. A correct unifying theory must remain generative. The four classical incompleteness results (Heisenberg, Gödel, Turing, Chaitin) are the structural guarantee that sufficiently-powerful theories can satisfy this.

## 2. Setup

Let $T$ be a theory — a representational system with formal content, an intended domain $D$, and a set of open questions $Q(T)$ regarded as well-posed *within* $T$'s vocabulary. Let $E(T)$ be the set of phenomena in $D$ for which $T$ provides (or is judged to provide) an adequate explanation.

At a given time $t$, define:

- $I_t(T)$ — the *inquiry-space* of $T$: the cardinality (or appropriate measure) of $Q(T)$ at time $t$.
- $U_t(T)$ — the *uncertainty-space* of $T$: a measure of what in $D$ remains unexplained, restricted to questions $T$ has the vocabulary to pose.

Under a research step $\Delta t$ (a new result, a new application, a new extension), the theory generates changes $\Delta I$ and $\Delta U$. By construction, answering a question drops it out of $Q(T)$; it contributes negatively to $\Delta I$ unless that answer opens new questions. An adequate explanation reduces $U$.

**Generativity ratio.**

$$G_t(T) \;=\; \frac{\max(0, \Delta I_t)}{\max(\varepsilon, -\Delta U_t)}$$

where the denominator is regularized by a small $\varepsilon > 0$ to avoid division by zero when the theory is not answering anything (in which case $G$ is undefined, which is correct — a theory that is not resolving uncertainty has no claim to be unifying).

**Generativity criterion.** $T$ is *generative* at time $t$ if $G_t(T) > 1$. $T$ is *unifying* (as opposed to *totalizing*) if it is generative persistently over research time.

## 3. Claim: generativity criterion $\Leftrightarrow$ nondegenerate-interval condition on $T$

The central claim is:

> **Claim 3.1 (structural correspondence).** A theory $T$ is generative at time $t$ iff the pair $(T, D)$ occupies the nondegenerate interval of the ACP, under the identification:
>
> - *dissolution* of $(T, D)$: $U_t(T) \to \sup U$, $I_t(T) \to 0$. The theory says nothing determinate; every question is open because the vocabulary is too weak to close any. (E.g. the null theory, or a theory whose predictions are indistinguishable from noise.)
> - *crystallization* of $(T, D)$: $U_t(T) \to 0$, $I_t(T) \to 0$. The theory's explanatory coverage is complete and its inquiry-space has collapsed. Every question the theory can pose, it has answered. There is no research program.

*Status: **conjectured**, with the following structural argument.*

### Structural argument

The ACP says a system retains future-bearing dynamics iff it occupies a nondegenerate interval between two absorbing states. Map the ACP ingredients onto the theory-evolution system as follows:

| ACP object | Theory-evolution object |
|---|---|
| System state | Pair $(T, D)$ at research-time $t$ |
| Macrostate entropy | Inquiry-space size $I_t(T)$ |
| Predictive structure | Explanatory coverage $E(T)$ |
| Dissolution boundary | $U_t \to \sup U$, $I_t \to 0$ — null theory |
| Crystallization boundary | $U_t \to 0$, $I_t \to 0$ — complete closed theory |
| Anti-coherent mechanisms | Research steps that answer questions without opening new ones |
| Coherent mechanisms | Research steps that open questions as they resolve others |

Under this mapping, the Crystallization Drift Theorem (CDT) says the pair $(T, D)$ drifts toward crystallization unless the theory continues to open new inquiry at a rate that compensates for the rate at which its answers close the existing inquiry. That rate condition is exactly $G_t(T) > 1$.

The ACP's requirement of *coherent steering* (Appendix A.10) — that the system host mechanisms that prevent drift into either absorbing boundary — translates here into the requirement that research on $T$ be *structurally open*: the theory must be rich enough that its answers generate new questions. This is where the incompleteness quartet enters.

### Why the quartet underwrites this

A theory $T$ powerful enough to represent itself — powerful enough to pose self-referential questions, to encode its own syntax, to simulate its own inference procedures — is subject to the four structural incompleteness results described in `essays/the_incompleteness_quartet.md`. These collectively guarantee that no such theory can close over itself: there are always truths it cannot prove, procedures it cannot decide, observables it cannot jointly sharpen, descriptions it cannot compress.

Each such obstruction generates at least one new question that cannot be answered from inside $T$'s existing axiom base. The quartet is therefore a *source* of inquiry for any sufficiently-powerful $T$. This gives:

> **Sub-claim 3.2 (proven, modulo the quartet).** For any theory $T$ rich enough to (i) host a Turing-universal substrate, or (ii) encode elementary arithmetic, or (iii) admit a two-subsystem partition of its observable algebra, or (iv) describe strings of unbounded length, the inquiry-space $I_t(T)$ is bounded below by a positive constant for all $t$.

*This follows directly from the four theorems.* Each provides a lower bound on the open-question count: Gödel provides at least countably many unprovable truths; Turing provides uncountably many undecidable instances; Chaitin provides a constructive incompressibility lower bound; Heisenberg/A.20 provides a variance-product floor. The details of how each bound translates to "at least one open question" are straightforward but need to be written out; they are exactly the content of the quartet essay in formal register.

Combining 3.1 and 3.2: sufficiently-powerful theories cannot reach the crystallization boundary, which is the condition the ACP requires for the pair $(T, D)$ to retain research-bearing dynamics. **A sufficiently-powerful theory that is also productive — that actually closes some uncertainty per research step — is automatically generative.**

This is why "sufficiently powerful to be interesting" and "cannot be finished" are the same condition. The ACP makes the connection explicit: the first is what keeps the theory off the dissolution boundary, the second is what keeps it off the crystallization boundary.

## 4. Consequences

### 4.1 Self-application of the ACP

The ACP itself is a theory of this kind: it has formal content (the CDT, Coherent Steering, the reductions), an intended domain (dynamical systems generally), and it is powerful enough to represent itself (it describes conditions for persistence that apply to representational systems, of which the ACP is one).

**Corollary 4.1 (proven, conditional on 3.1).** If the ACP is correct, it is subject to the generativity criterion. Its continued persistence as a research program requires $G_t(\text{ACP}) > 1$. In particular, every result in the paper should open more well-posed questions than it closes.

This is an empirical check on the program: walk through the result inventory in `STATUS.md` and ask whether each result opened questions at a rate $> 1$. The existing `OPEN_PROBLEMS.md` tracker is the first-order audit of this. A healthy ACP program shows $|OPEN\_PROBLEMS.md|$ growing at least as fast as new results are added.

A less obvious corollary: the ACP is structurally forbidden from being finished. There is no version N of the paper that closes all open problems and admits no successors. If the theory is correct, version N+1 must always be possible. This is not a promissory note — it is a structural prediction of the theory itself.

### 4.2 Restraint as a structural obligation for dominant theories

Let $T$ be a theory whose compressive capacity on $D$ is high — it explains much of $D$, and downstream research in $D$ is conducted largely through $T$'s vocabulary. By Claim 3.1 and Sub-claim 3.2, $T$'s internal inquiry-space $I_t(T)$ remains positive. But the inquiry-spaces of downstream researchers, who think *through* $T$, are not protected by the quartet directly. They inherit whatever partition $T$ imposes on $D$.

**Conjecture 4.2 (open).** For a dominant theory $T$ with compressive ratio $\rho$, the collective semantic field $S$ of downstream researchers has an effective inquiry-space $I_t(S) \leq f(\rho) \cdot I_t(T)$ for some decreasing $f$. As $\rho \to 1$ (monopoly framing), $I_t(S)$ can approach zero even while $I_t(T)$ remains positive.

If 4.2 holds, the restraint obligation on a dominant theory is structural, not ethical: unless $T$ actively flags its own gaps and refuses to project closure onto its downstream, the semantic field crystallizes around it. This is the formal statement of what the accompanying essay calls "structural hygiene."

*Relation to A.20 (Restraint-Power Theorem).* The conjecture generalizes A.20 from operator-algebra partitions to theory-domain compositions. A.20 bounds the coordination-floor for a two-MASA partition; 4.2 bounds the coordination-floor for a (theory, downstream) partition. Whether the A.20 machinery extends literally is open — it likely requires a notion of "compressive partition" analogous to MASAs.

### 4.3 Meaning-space as a measure-theoretic object

A measure-theoretic treatment of the meaning-space would formalize 4.2. Given observers $\{O_i\}$ with conditional distributions $p_i$ over world-states, define the meaning-space measure $\mu$ as the union (or join in the partition lattice) of the distinguishable partitions induced by $\{p_i\}$. A dominant frame $T$ acts by inducing a coarsening $\kappa_T$ on each $p_i$.

Under this setup, *semantic crystallization* is the fixed point where $\kappa_T \circ p_i = \kappa_T \circ p_j$ for all $i, j$ — all observers share the same coarsening, and conditional entropy over interpretations, taken across observers, is zero. *Semantic dissolution* is the opposite extreme: no two $p_i$'s induce compatible partitions, and joint distinguishability is noise. The nondegenerate interval lies between.

*Status: setup only. Whether this induces the ACP's interval structure formally, and whether the CDT applies in the semantic register, is **open**. See OP-10 below.*

## 5. What this does and does not claim

**Proven** (modulo the quartet's standard statements):
- Sub-claim 3.2: sufficiently-powerful theories have inquiry-spaces bounded below by a positive constant.

**Conjectured**:
- Claim 3.1: the generativity criterion corresponds to the ACP's nondegenerate-interval condition for the theory-evolution system.
- Corollary 4.1: the ACP is subject to the generativity criterion. (Follows from 3.1 if 3.1 holds.)

**Open**:
- Conjecture 4.2: downstream semantic inquiry-space is bounded by the dominant theory's compressive ratio. (New open problem — see OP-10.)
- The measure-theoretic treatment of meaning-space and its ACP structure. (New open problem — see OP-11.)
- Whether the generativity criterion admits a sharp quantitative bound (analogous to A.17's non-Gaussian bounds) rather than the threshold condition $G > 1$. (See OP-12.)

## 6. What this is not

This document does not claim that Gödel, Turing, Heisenberg, and Chaitin are four statements of the *same* theorem. They are four theorems in four domains with four different proofs. The claim is that they share a *structural signature* — the impossibility of a sufficiently-powerful representational system closing over itself — and that this signature is exactly what the ACP identifies as the crystallization boundary being unreachable.

Nor does this document propose to replace domain-specific criteria for theory evaluation. The generativity criterion $G > 1$ is a *necessary* condition for a theory to count as unifying rather than totalizing, not a sufficient one. A theory can be generative and wrong. Empirical adequacy, internal consistency, and the usual scientific virtues still apply.

## 7. New open problems

These are propagated into `OPEN_PROBLEMS.md`.

- **OP-10** (from Conjecture 4.2): downstream-inquiry-space bound under theory dominance.
- **OP-11** (from §4.3): measure-theoretic meaning-space and its ACP structure.
- **OP-12** (from §5): quantitative form of the generativity criterion.
- **OP-13** (methodological): formalize the quartet → ACP-boundary reduction as a single theorem in the main paper appendix on meta-theoretic coherence, or leave as four parallel arguments.

---

*This document is a bridge, not part of the proof chain. The claim that $G > 1$ is the ACP's crystallization-avoidance condition applied to theories is structural; it does not affect the status of the CDT or A.20 but, if it goes through, supplies the self-consistency argument that the ACP program must itself satisfy.*
