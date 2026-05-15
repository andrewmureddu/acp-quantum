# Reality-Reflective Mathematics: An ACP Admissibility Criterion

*Status: exploratory bridge. Formal at the admissibility level; conjectural as
a general criterion for mathematical realism.*

Companion notes: `bridges/generativity_criterion.md`,
`bridges/singularity_inadmissibility.md`, `bridges/schur_complement.md`,
`bridges/restraint_ethics.md`, and `bridges/otherness_preserving_recovery.md`.

---

## 1. Thesis

The ACP program already contains an implicit criterion for when mathematics is
allowed to count as reality-reflective rather than merely internally valid.

The criterion is:

> A mathematical description is world-facing only when it can couple to finite
> records while preserving a nondegenerate interior capable of continued
> prediction.

Equivalently, reality-reflective mathematics must sit inside the ACP productive
interval as a description:

$$
0 < H_{\mathcal F}(m'|m) < H_{\max},
$$

with a finite record channel

$$
P_{\mathcal F}(R|s)
$$

that is informative about the intended target distinctions.

This does not say that pure mathematics is unreal, false, or useless. Pure
mathematics can be perfectly valid inside its own axioms. The ACP distinction is
different:

1. **formal validity:** the structure follows from its axioms;
2. **empirical admissibility:** the structure can be coupled to finite records
   without singularity, triviality, or total closure;
3. **reality reflection:** the structure continues to generate correct,
   perturbable, and non-totalizing predictions across admissible descriptions.

The implicit claim is that the world does not select mathematics by elegance
alone. It selects mathematics by admissible coupling.

## 2. What Was Already Present

This criterion was not absent from the project. It was distributed across
several bridges.

**Schur complement bridge.** The productive interval is the regime where the
internal block \(D\) is nondegenerate and the effective boundary law

$$
Q/D = A - BD^{-1}B^T
$$

is defined. When \(D\) is singular, the description cannot produce a legal
boundary theory. When \(D\) is trivial, the boundary sees no structured
interior.

**Singularity inadmissibility.** Singularities were already treated as failures
of the effective mathematics, not as physical endpoints. That note gives the
local version of the general rule: finite observables, normalizable record
channels, nondegenerate interiors, and finite continuation are admissibility
requirements for world-facing descriptions.

**Generativity criterion.** The ACP applied to theories says that a living
theory must open more inquiry than it closes. A closed theory with no remaining
questions is not a successful theory in the ACP sense; it is a crystallized
one.

**Empirical predictions.** The main paper's prediction appendix already treats
reality-coupling as falsifiability: a unification is not enough unless it
produces record-level consequences that can fail.

**QEC and conditional leakage.** The quantum program adds the sharpest
epistemic form: a good recovery apparatus learns error structure while remaining
blind to the protected logical state. In abstract terms, a good model should
learn the world's syndrome-bearing distinctions without pretending to exhaust
the world's protected interior.

These are the same criterion in different registers.

## 3. World-Facing Formal Descriptions

Let a candidate world-facing formal description be

$$
\mathcal F = (\mathcal S,\Phi,\sigma,\mathcal O,\mathcal R),
$$

where:

1. \(\mathcal S\) is a state space;
2. \(\Phi\) is an evolution law, constraint law, or admissible history class;
3. \(\sigma:\mathcal S\to\mathcal M\) is a coarse-graining map to macrostates;
4. \(\mathcal O=\{\mathcal O_i\}\) is a set of observables;
5. \(\mathcal R\) is a record channel \(P(R|s)\).

The formal description may also specify a target variable \(X\) whose
distinctions it is meant to track, and a residual or protected variable \(L\)
whose direct capture is not required for the model's intended function.

Examples:

| Domain | \(\mathcal S\) | \(X\) | \(R\) |
|---|---|---|---|
| Quantum error correction | physical code states | error sector | syndrome record |
| Gravity | geometries / histories | exterior charges, relational geometry | boundary/null records |
| Active inference | hidden causes and agent states | environmental causes | sensory observations |
| Population genetics | genotype frequencies | selection response | trait/fitness data |
| Theory evolution | theory-domain pair | unresolved explanatory structure | new predictions / open problems |

The same mathematical object can be formally valid without being
world-facing. It becomes world-facing only after the record channel and
coarse-graining are specified.

## 4. Admissibility Conditions

Call \(\mathcal F\) empirically admissible on a domain \(U\subseteq\mathcal S\)
when the following conditions hold.

**A1. Finite observables.**

The observables that give the description empirical content are finite at the
resolution scale of the description:

$$
|\mathcal O_i(s)| < \infty
\qquad
\text{for all required observables } \mathcal O_i .
$$

**A2. Normalizable record channel.**

The record channel is a genuine probability law:

$$
0\leq P(R|s)\leq 1,
\qquad
\sum_R P(R|s)=1,
$$

or the corresponding normalized measure in the continuum case.

**A3. Nondegenerate continuation.**

The induced macrostate transition kernel has nonzero but nonmaximal conditional
entropy:

$$
0 < H_{\mathcal F}(m'|m) < H_{\max}.
$$

In the Schur/Gaussian register, this means the relevant internal block is
defined and nontrivial:

$$
D^{-1}\ \text{exists on the retained support,}
\qquad
\kappa(D)<\infty,
$$

and \(D\) is not merely a structureless identity block.

**A4. Finite verification time.**

The law carries admissible states to admissible states over the verification
timescale \(\tau_v\):

$$
s\in U
\Rightarrow
\Phi_t(s)\in U
\qquad
0\leq t\leq \tau_v .
$$

**A5. Perturbable record coupling.**

The formal target distinctions change records under intervention. For target
states \(x,x'\), there must be some record variable \(R\) such that

$$
D_{\mathrm{KL}}\!\left(P(R|do(x))\,\|\,P(R|do(x'))\right) > 0,
$$

or, observationally when interventions are unavailable,

$$
I(X;R)>0.
$$

This is the minimal "the math touches the world" condition.

**A6. Non-totalizing remainder.**

When the description is meant to preserve or model a persistent object rather
than consume it, the record channel should not collapse all residual degrees of
freedom into the model's variables:

$$
H(L|R,X) > 0
$$

or, in the QEC/privacy form,

$$
I(L;R|X)\ \text{is bounded.}
$$

This condition is not required for every measuring apparatus. It is required
for descriptions that claim to model a persistent system while leaving the
system's own future-bearing interior intact. It is the abstract form of the
QEC rule: learn syndrome, not logical state.

**A7. Structured innovation floor.**

For dynamic, persistent, or generative descriptions, the future record stream
should not be completely determined by the current formal state, but its
surprises should also not be structureless. Let \(Z_t\) denote the description's
current internal state, including its variables, parameters, and record history.
For a future verification record \(R_{t+\Delta}\), define the record innovation

$$
N_t^{\mathcal F}
=
H(R_{t+\Delta}\mid Z_t),
$$

and its target-bearing part

$$
S_t^{\mathcal F}
=
I(X_{t+\Delta};R_{t+\Delta}\mid Z_t).
$$

The admissible innovation condition is

$$
0 < S_t^{\mathcal F}\leq N_t^{\mathcal F}<H(R_{t+\Delta}).
$$

If \(N_t^{\mathcal F}=0\), the description is crystallized relative to its
records: nothing can arrive as an empirical correction. If
\(S_t^{\mathcal F}=0\) while \(N_t^{\mathcal F}\) remains large, the record
stream is dissolved relative to the modeled target: surprises occur, but they
do not update the world distinction the model claims to track. Admissible
"noise" is therefore structured innovation, not bare randomness.

## 5. Necessary Criterion

**Proposition 1 (Admissibility is necessary for reality reflection).** If a
formal description \(\mathcal F\) fails A1, A2, A3, A4, or A5 on its intended
domain, then \(\mathcal F\) cannot be a reality-reflective description of that
domain.

**Proof.**

If A1 fails, at least one required empirical quantity is not finite, so the
description cannot assign bounded observable content at its own resolution.

If A2 fails, \(P(R|s)\) is not a probability law, so no finite observer can use
the description to predict records.

If A3 fails at the lower boundary, \(H_{\mathcal F}(m'|m)=0\), the description
has no remaining future-bearing alternatives. It may be a completed constraint
system, but it is no longer a persistent world-facing dynamics. In Schur
coordinates this is the singular-\(D\) case: the effective boundary law is
undefined without adding new support conditions. If A3 fails at the upper
boundary, \(H_{\mathcal F}(m'|m)=H_{\max}\), the description carries no
coherent predictive structure; its records are indistinguishable from noise.

If A4 fails, the description cannot carry its own admissible states through a
verification interval. It has no stable domain of application.

If A5 fails, the description has no informative coupling to the target
distinctions. Then its formal variables may be internally meaningful, but they
do not track the intended world variable. Hence it cannot be reality-reflective
on that target.

Therefore A1-A5 are necessary for reality reflection. \(\square\)

**Remark.** The proposition is only a necessary criterion. A description can
pass these tests and still be wrong, approximate, or incomplete. Reality still
has veto power through prediction and intervention.

## 6. The Selection Ladder

The ACP suggests the following ladder for mathematical structures.

| Level | Name | Criterion | Failure mode |
|---|---|---|---|
| L0 | Formal structure | Internal syntactic validity | Inconsistency |
| L1 | Effective description | A1-A4 admissibility | singularity or domain failure |
| L2 | Empirical model | A5 record coupling | empty interpretation |
| L3 | Persistent model | productive interval across time | dissolution or crystallization |
| L4 | Reality-reflective invariant | survives admissible changes of coordinates, scale, and coarse-graining | artifact of representation |
| L5 | Generative theory | produces new tests and open questions faster than it closes old ones | totalizing closure |

This ladder gives a clean answer to the question "does ACP distinguish math
that reflects reality?"

Yes, but only in stages.

ACP does not decide whether a theorem is formally true. It asks whether that
theorem can enter a finite, perturbable, nondegenerate record relation with the
world, and whether the structure persists under admissible changes of
description.

## 7. Uncertainty Allocation Across Scales

The stabilizing mechanisms of a description are also the mechanisms that can
rigidify it. A model gains power by suppressing irrelevant variation, but that
same suppression can eliminate the very record innovation that keeps the model
world-facing. ACP therefore predicts an admissible uncertainty allocation: not
zero uncertainty, not maximum uncertainty, but a structured distribution of
uncertainty across the distinctions, scales, and record channels where it keeps
the description correctable.

The scalar "noise floor" is only the one-mode special case. In a real
multi-scale system the optimized object is not a number \(n\), but a function
or spectrum

$$
\mathcal N_t:\mathcal A\to\mathbb R_{\geq 0},
$$

where \(\mathcal A\) may index spatial scales, Fourier modes, renormalization
levels, measurement channels, model layers, institutional record types, or
semantic partitions. For each \(\alpha\in\mathcal A\), write

$$
N_t(\alpha)
=
H(R_{\alpha,t+\Delta}\mid Z_t),
\qquad
S_t(\alpha)
=
I(X_{\alpha,t+\Delta};R_{\alpha,t+\Delta}\mid Z_t).
$$

The admissible allocation condition is pointwise:

$$
0<S_t(\alpha)\leq N_t(\alpha)<H(R_{\alpha,t+\Delta})
$$

on the active support of the description, together with a global continuation
constraint. Let

$$
h_t[\mathcal N]
=
\frac{H_{\mathcal F,\mathcal N}(m'|m,Z_t)}{H_{\max}}
$$

be the normalized continuation entropy induced by the whole allocation. A
schematic admissibility functional is

$$
\mathcal P_t[\mathcal N]
=
\frac{
\displaystyle
\int_{\mathcal A}
w_t(\alpha)\,
S_t(\alpha)\,
h_{t,\alpha}[\mathcal N]\,
\bigl(1-h_{t,\alpha}[\mathcal N]\bigr)\,
d\alpha
}{
1+\displaystyle\int_{\mathcal A}
w_t(\alpha)\,I(L_\alpha;R_{\alpha,t+\Delta}\mid X_\alpha,Z_t)\,d\alpha
+C[\mathcal N]
},
$$

with sums replacing integrals on discrete index sets. Here \(w_t(\alpha)\)
weights the relevance of each scale or channel, and \(C[\mathcal N]\) is the
cost, overhead, or singularity penalty introduced by the allocation.

The corresponding optimizer is a spectrum, not a scalar:

$$
\mathcal N_t^*
\in
\arg\max_{\mathcal N\in\mathfrak A_t}
\mathcal P_t[\mathcal N],
$$

where \(\mathfrak A_t\) is the admissible constraint class. The shape of
\(\mathcal N_t^*\), not merely its magnitude, is the content of the theory.

When some scales approach crystallization \((h_{t,\alpha}\to 0)\), the
allocation must admit more structured innovation, perturbability, or unresolved
slack there. When other scales approach dissolution \((h_{t,\alpha}\to 1)\),
the allocation must become more selective there: records must carry more target
information per unit surprise. The ACP criterion is therefore adaptive and
spectral. The right amount of mathematical looseness is a function over the
description's distances from both absorbing boundaries.

In a one-scale approximation, \(\mathcal A=\{\alpha_0\}\), this reduces to the
earlier scalar optimizer \(n^*(t)\). That scalar is useful for toy models, but
the general claim is variational:

> persistence selects uncertainty-allocation spectra under constraints.

This is the meta-mathematical version of the quantum condition:

$$
I(\mathrm{error};\mathrm{syndrome})>0,
\qquad
I(\mathrm{logical};\mathrm{record}\mid \mathrm{error})\approx 0.
$$

A world-facing theory should allocate uncertainty so that each scale remains
correctable by future records, and restrain record channels so they do not
confuse correction with total capture.

## 8. What This Makes Explicit

The project had several implicit claims that were not yet named.

**1. Singularity exclusion is not only a gravity principle.** It is the local
case of a general admissibility rule for mathematics. Singularities, divergent
observables, nonnormalizable measures, and undefined Schur complements all mean
the same thing: the formalism has left its legal domain.

**2. Falsifiability is anti-crystallization.** A theory that cannot be tested
has no record channel. A theory that cannot fail has a record channel only in a
degenerate sense: every record is already interpreted as confirmation. This is
the epistemic version of crystallization.

**3. Overfitting is mathematical crystallization.** A model that explains its
training domain by eliminating all residual uncertainty may become less
reality-reflective, not more. It has collapsed \(H(m'|m)\) relative to the
future records it still has to face.

**4. Pure math is a reservoir of possible state spaces.** Pure mathematics
need not be world-facing at birth. It supplies admissible and inadmissible
candidate structures. Physics, computation, biology, and cognition select from
that reservoir by record coupling and persistence.

**5. The environment is not just a source of data.** It is a boundary channel.
Good theories learn from the environment in the same way good QEC protocols
learn from syndrome streams: they extract error-relevant structure without
confusing the record with the whole logical state.

**6. Unification is stronger than analogy only when the same obstruction
appears in different coordinates.** The ACP reductions are strong because they
map domain variables to the same conditional-entropy / rank / record-channel
structure. This is the mathematical signature of a reality-reflective
invariant.

**7. Reality is what prevents total compression.** In ACP terms, a world-facing
theory persists only if the world continues to supply finite but nonzero
conditional entropy. The theory must be able to predict, but not finish, its
domain.

**8. Optimal uncertainty is spectral.** There is no universal best amount of
noise, regularization, or model slack. The admissible allocation depends on
which scales or record channels are currently failing by overconstraint and
which are failing by loss of decodable structure.

## 9. Relation to ACP Quantum

ACP Quantum is the concrete test bed for this meta-criterion.

In QEC language, the admissible record condition is:

$$
I(\mathrm{error};\mathrm{syndrome}) > 0,
$$

while the non-totalizing condition is:

$$
I(\mathrm{logical};\mathrm{record}\mid\mathrm{error}) \approx 0.
$$

The decoder should learn what happened to the protected information, not what
the protected information is.

The same structure applies to mathematics:

$$
I(\mathrm{world\ distinction};\mathrm{record}) > 0,
$$

while

$$
H(\mathrm{world\ remainder}\mid\mathrm{record},\mathrm{modeled\ distinction})>0.
$$

A reality-reflective theory should learn enough structure to predict and
correct its errors, but not so much that it mistakes its finite record channel
for the complete world.

Hardware adaptive syndrome alignment is therefore not merely an application of
ACP. It is the laboratory instance of the larger epistemic rule. A noise model
counts only if it improves the same logical channel under finite syndrome
records, explicit overhead, and leakage audit. That is exactly what a
world-facing mathematical model must do in any domain.

## 10. Conjectures

**Conjecture 1 (Reality-reflective invariant).** A mathematical structure is a
reality-reflective invariant of a domain only if it is preserved under
admissible changes of coarse-graining, coordinate system, and record channel
that leave the target distinction \(X\) empirically identifiable.

**Conjecture 2 (Generative admissibility).** Among empirically admissible
descriptions of the same domain, the descriptions that persist as research
programs are those that maximize record informativeness per unit of
crystallizing closure. A candidate schematic score is

$$
\mathcal A(\mathcal F)
=
\frac{
I(X;R)\,G(\mathcal F)\,\eta_{\mathrm{cont}}
}{
1 + I(L;R|X) + C_{\mathrm{sing}}
},
$$

where \(G(\mathcal F)\) is the generativity ratio,
\(\eta_{\mathrm{cont}}\) measures continuation inside the productive interval,
and \(C_{\mathrm{sing}}\) penalizes singular or near-singular domains.

This score is only a prompt for future formalization. The numerator says the
description must touch the world, remain generative, and continue. The
denominator says it must not over-capture its object or rely on singular
coordinates.

**Conjecture 3 (Mathematical naturalness as admissible recurrence).** The
reason certain mathematical structures recur across physics is not simply that
they are elegant or simple. They recur because many persistent systems share
the same admissibility obstructions: finite records, boundary/interior
partitions, nondegenerate kernels, and limited leakage.

**Conjecture 4 (Adaptive uncertainty allocation).** For any persistent
world-facing description with scale- or channel-indexed record degrees of
freedom, there is a nonempty admissible class of allocations
\(\mathfrak A_t\) on which \(\mathcal P_t[\mathcal N]>0\). If the
description's normalized continuation entropy drifts toward either absorbing
boundary on a subset of scales, the maximizing allocation \(\mathcal N_t^*\)
shifts locally away from that boundary by increasing target-bearing innovation
near crystallization and increasing selectivity near dissolution. The
observable signature of a domain is the shape of \(\mathcal N_t^*\), e.g. a
power-law exponent, cutoff profile, hierarchy of measurement rates, or
layer-wise regularization spectrum.

## 11. Open Targets

1. Define a category of admissible descriptions whose morphisms preserve record
   channels and productive intervals.
2. Prove that the Schur complement, conditional entropy, mutual information,
   and uncertainty floors are functorial or invariant objects in that category.
3. Turn A6 into a general "non-totalizing model" condition without importing
   the QEC protected-logical-state interpretation too literally.
4. Formalize A7 as a dynamic admissibility theorem over allocation functions
   \(\mathcal N_t(\alpha)\), and identify conditions under which
   \(\mathcal N_t^*\) exists, is unique, or must be replaced by an admissible
   family of spectra.
5. Build a small comparison table of historical mathematical structures:
   Euclidean geometry, Riemannian geometry, Hilbert spaces, probability theory,
   group theory, category theory, and singular GR solutions, classified along
   L0-L5.
6. Decide whether this bridge belongs as a short philosophical appendix, a
   companion essay, or a formal meta-theory note adjacent to
   `bridges/generativity_criterion.md`.

## 12. What This Does Not Claim

This note does not claim that ACP can decide mathematical truth. Formal truth
remains internal to axioms and proof systems.

It also does not claim that every reality-reflective theory must preserve a
private logical state in the literal QEC sense. The QEC form is the sharpest
available example of a more general requirement: a model should expose the
target distinctions needed for prediction without collapsing the modeled
object into its own record.

Finally, this is not a sufficient criterion for truth. It is a necessary
admissibility and generativity filter. A model can be admissible, measurable,
and generative while still failing against future records. That failure is not
a defect of the criterion; it is the point of keeping the record channel open.
