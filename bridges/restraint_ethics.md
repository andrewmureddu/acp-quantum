# Restraint Ethics as an ACP Civilizational Bridge

*Status: proposed bridge; simulation-backed toy diagnostic; not part of the
core proof chain.*

*Companion simulation: `simulations/restraint_ethics/`.*

---

## Abstract

This note translates the ACP's restraint-power structure into a civilizational
ethics without claiming that physics proves a moral doctrine. The claim is more
limited and more useful: when a system contains persons, institutions, and
future-bearing capacities, the same structural failure modes become ethically
legible. Dissolution corresponds to abandonment, atomization, uncorrected harm,
or loss of shared memory. Crystallization corresponds to domination,
surveillance, monopoly closure, ideological finality, or algorithmic
overdetermination.

The civilizational target is therefore not maximal freedom and not maximal
order. It is legitimate restraint:

$$
I(\mathrm{error};\mathrm{record}) > 0
$$

while

$$
I(\mathrm{protected\ agency};\mathrm{record}\mid \mathrm{error}) \approx 0,
$$

with the future-bearing capacity of the person, community, or institution still
retaining memory of its own past. This is the civil analogue of the ACP Quantum
target: extract syndrome information without leaking the logical state.

The bridge also feeds back into the quantum program. Human systems make clear
that raw leakage can be the wrong audit when error sectors and protected states
are statistically entangled. The sharper diagnostic is excess leakage
conditioned on the syndrome/error sector. In quantum language, the future target
is a reference-system conditional mutual information such as

$$
I(R_L;E_{\mathrm{env}}\mid S)\approx 0,
$$

where \(R_L\) purifies the logical state, \(E_{\mathrm{env}}\) is the
environment fragment, and \(S\) is the extracted syndrome.

## 1. Why This Is Not a Naturalistic Fallacy

The bridge does not say:

> physics proves this morality.

It says:

> a formal theory of persistence identifies structural failure modes; when the
> system contains beings with agency, memory, vulnerability, and futures, those
> failure modes acquire ethical significance.

The ACP contributes a diagnostic grammar. It distinguishes between:

- constraints that preserve the productive interval;
- constraints that close the interval;
- freedoms that preserve future-bearing dynamics;
- freedoms that dissolve the conditions of freedom.

This is enough to make ethical questions sharper without pretending that a
mathematical theorem has directly derived a political program.

## 2. Civilizational Setup

Let a civil system be a coupled ACP system

$$
S_C=(\Omega,\sigma,T,\mu;\mathcal A,\mathcal P),
$$

where \(\mathcal A\) is a set of institutions or power-bearing actors and
\(\mathcal P\) is a set of persons, communities, or protected plural forms of
life. The ACP macrostate entropy \(H(m'|m)\) is interpreted here as the system's
remaining future-bearing civil capacity: the next state is neither random nor
already decided.

For a power-bearing institution \(A\), let:

- \(E\) denote a public error sector: harm, fraud, violence, corruption,
  coordination failure, ecological damage, or another correctable public
  failure mode.
- \(L\) denote a protected agency/logical state: the private, developmental,
  political, creative, or communal state that must remain open for the system
  to be ethically future-bearing.
- \(R\) denote the institutional record: surveillance data, audit trail,
  legal record, educational assessment, market signal, scientific measurement,
  or AI-governance telemetry.
- \(C(R)\) denote the burden of producing and acting on the record: cost,
  latency, coercion, administrative drag, chilling effects, or control traffic.

The civil analogue of syndrome extraction is not "learn everything." It is:

$$
I(E;R)>0.
$$

The civil analogue of logical privacy is not "the institution knows nothing."
It is:

$$
\Lambda_{\mathrm{exc}}=I(L;R\mid E)\approx 0.
$$

That is, once the correctable public error is known, the record should reveal as
little as possible about the protected agency state.

## 3. Definition: Restraint-Legitimate Record Channel

**Definition 1 (restraint-legitimate record channel).** A record channel
\(R\) is restraint-legitimate for a civil system \(S_C\) at time \(t\) if:

1. **Correctability:** \(I(E;R)\geq \epsilon_E>0\).
2. **Excess non-capture:** \(I(L;R\mid E)\leq \epsilon_L\).
3. **Bounded burden:** \(C(R)\leq C_{\max}\).
4. **Future-bearing retention:** the protected state retains nonzero memory,
   for example \(I(L_t;L_{t+\Delta t})>0\) under the induced civil channel.

Condition 1 excludes abandonment. Conditions 2 and 3 exclude surveillance,
over-administration, and control-by-exhaustion. Condition 4 excludes "fixes"
that solve the public error only by erasing the agency or continuity of the
protected system.

The associated diagnostic score is

$$
\mathcal R(R)
=
I(E;R)\,
\left(1-I(L;R\mid E)\right)\,
\exp[-\alpha C(R)].
$$

This score is not a moral scalar. It is a test statistic for the bridge: it is
low when there is no usable record, low when the record captures the protected
state, and low when record production itself becomes excessive.

## 4. Civil Productive Interval

Under this bridge, the two ACP boundaries become:

**Dissolution / abandonment.**

$$
I(E;R)\to 0.
$$

The institution cannot detect or correct public failure modes. Harm diffuses,
trust collapses, and the system loses shared memory.

**Crystallization / capture.**

$$
I(L;R\mid E)\to H(L)
$$

or

$$
C(R)\to C_{\max}.
$$

The institution does detect the system, but it detects too much or acts too
heavily. The protected agency state becomes administratively legible, socially
frozen, or strategically optimized away.

**Restraint regime.**

$$
0<I(E;R),\qquad I(L;R\mid E)\approx 0,\qquad C(R)\ \mathrm{bounded}.
$$

The system learns enough to correct harms while refusing to learn or control so
much that it closes the futures it governs.

This is the civil form of "preserving the gap."

## 5. Relation to A.20 Restraint-Power

A.20 proves the restraint-power theorem inside the ACP formalism: when a system
approaches its coordination floor, the most concentrated subsystem must perform
the first outward mechanism-changing transformation if the composite is to
persist.

In civil systems, high coordination concentration appears as concentrated
state power, capital power, platform power, military power, scientific
authority, institutional authority, or model-mediated cognitive power. Let
\(\gamma_A\) be the A.20 coordination concentration of actor \(A\). If

$$
\gamma_A = \max_i \gamma_i,
$$

and \(A\) has the capacity to close the productive interval of lower-power
subsystems, then A.20 gives the structural reading:

> the strongest actor must visibly self-limit first.

The ethical content comes from the nature of the affected subsystems. If those
subsystems are persons or communities, interval collapse is not merely a loss of
systemic persistence. It is domination, abandonment, or loss of agency.

## 6. Market-Authoritarian Boundary

The bridge gives a precise way to state a politically sensitive claim without
collapsing nuance:

> capitalism is not identical with authoritarianism, but unrestrained capital
> accumulation can create dissolution pressures that make authoritarian
> crystallization attractive.

In ACP terms:

1. Competitive markets can be anti-crystallizing: they distribute information,
   break inherited closure, and permit local experiment.
2. Unrestrained accumulation can dissolve intermediate structures: labor
   futurity, public goods, ecological continuity, civic trust, institutional
   independence, and epistemic commons.
3. Authoritarian systems can then appear as crystallization responses: forced
   unity, hierarchy, surveillance, mythic coherence, suppression of dissent,
   and state-capital coordination.

The proposed test is not "markets bad" or "planning good." It is:

$$
\text{Does the economic record channel preserve agency while correcting public
failure modes?}
$$

Markets lose legitimacy when the largest actors convert price, data, law,
labor, ecology, and governance into channels that reveal and constrain
protected agency while externalizing the public error sector.

## 7. AI Governance Form

AI intensifies the bridge because model-mediated systems can observe, predict,
rank, personalize, discipline, and optimize at civilizational scale. The ACP
question is not only whether AI systems are safe in the narrow sense. It is:

> what human intervals do these systems close before anyone notices?

For AI governance, a restraint-legitimate channel must satisfy:

$$
I(\mathrm{harm};\mathrm{audit})>0
$$

while

$$
I(\mathrm{person};\mathrm{audit}\mid \mathrm{harm})\approx 0,
$$

with a real right of appeal, deletion, contestation, plural governance, and
non-automated recovery paths. Otherwise the audit system itself becomes a
crystallization machine.

This is why current geopolitical conditions are a relevant stress test rather
than evidence for the theory. Recent public reports describe continued global
democratic decline, intensifying geopolitical confrontation, misinformation and
polarization risks, and AI capability growth with governance lag. Those are
exactly the background conditions under which record channels tend to be
expanded quickly and restrained slowly.

## 8. Delivery: How to Give the Theory Away

The communication problem is itself ACP-shaped. A theory of restraint must not
be delivered as a totalizing closure.

The public method should therefore be:

1. **Recognition before proof.** Start from cases people already understand:
   parents, teachers, courts, markets, science, medicine, AI systems.
2. **Two failure modes every time.** Never say only "too much control is bad."
   Also show how abandonment dissolves the conditions of freedom.
3. **Give the reader the gap.** The rhetoric should make the reader feel the
   interval, not merely submit to a thesis.
4. **Refuse final ideology.** The theory must preserve the inquiry-space of its
   downstream readers, as required by `bridges/generativity_criterion.md`.

In a Lewis register, the message is that cleverness without trained restraint
turns persons into material. In a Jung register, the warning is that a
civilization that cannot recognize its shadow will call its crystallization
salvation. In an Einstein register, the public demand is simple: when knowledge
becomes world-power, restraint becomes part of knowledge.

These are not appeals to authority. They are delivery modes for the same
formal point: power is legitimate only when it preserves the interval of
becoming for those subject to it.

## 9. Feedback to the Quantum Formalism

The civil bridge suggests a refinement of the existing ACP Quantum target.
`bridges/quantum_noise_as_signal.md` currently tracks raw logical-environment
mutual information:

$$
I(L;Y_{\mathrm{env}}).
$$

In ideal DFS examples, raw leakage and excess leakage coincide because the
logical branch and error sector are cleanly separated. In more realistic
settings, they need not. Error sectors, syndromes, and logical labels can be
statistically or dynamically coupled by imperfect encodings, biased priors,
decoder histories, or feedback policies.

The civil analogy exposes the audit problem: a record can appear to leak
private information simply because the private state is correlated with a
public error, even when the record carries no private information beyond that
error. Conversely, a record can correct errors while silently carrying extra
protected-state information.

The sharper quantum target is therefore:

$$
I(\mathrm{error};S)>0,
$$

while

$$
I(R_L;E_{\mathrm{env}}\mid S)\approx 0,
$$

and

$$
I_c(R_L\rangle B S)>0,
$$

where \(R_L\) is a reference purifying the logical input, \(S\) is the syndrome
or error-sector register, \(E_{\mathrm{env}}\) is the environment fragment, and
\(B\) is the retained system. This conditional leakage target should be added
to OP-15 as the next microscopic upgrade.

## 10. Testable Predictions

The bridge yields empirical and simulation-level predictions:

1. Record channels with moderate \(I(E;R)\), low \(I(L;R\mid E)\), and bounded
   burden will outperform both no-record and high-leakage regimes on
   persistence measures.
2. Systems with high raw \(I(L;R)\) but low conditional \(I(L;R\mid E)\) will be
   misclassified by privacy metrics that ignore the public error sector.
3. Dominant actors that visibly self-limit before crisis should stabilize
   composite systems better than actors that wait for imposed correction.
4. AI governance systems without conditional-leakage audits will overfit to
   legibility: they will appear effective on harm detection while narrowing
   human agency.
5. The quantum analogue should be measurable: conditional reference-environment
   leakage after syndrome extraction should predict recoverability better than
   raw environment mutual information in settings with correlated errors.

## 11. Simulation Summary

The companion simulation `simulations/restraint_ethics/` tests the first two
predictions in a binary Gaussian record model. It scans monitoring strength and
leakage fraction. The output has the expected ACP shape:

- low monitoring gives no usable error record;
- high leakage or high record burden gives capture;
- an intermediate region gives positive syndrome information with low excess
  leakage.

It also includes a context-correlation audit showing why conditional leakage
matters. When the protected variable \(L\) is correlated with the public error
sector \(E\), raw \(I(L;R)\) can be high even for an error-only record, while
\(I(L;R\mid E)\) stays near zero. This is the civil diagnostic that motivates
the quantum upgrade in Section 9.

## 12. Claim Boundary

This bridge is not a derivation of ethics from physics. It is a proposed
translation layer:

- **proved upstream:** ACP/CDT and A.20 inside their stated assumptions;
- **defined here:** restraint-legitimate civil record channels;
- **simulation-backed here:** a toy record-channel productive interval;
- **conjectured:** that real civil systems preserving agency satisfy the same
  interval condition in measurable institutional data;
- **open:** the quantum conditional-leakage upgrade with microscopic
  Stinespring environment states and recoverability bounds.

## References

Freedom House. "Global Freedom Declined for 20th Consecutive Year in 2025."
2026. https://freedomhouse.org/article/new-report-global-freedom-declined-20th-consecutive-year-2025

World Economic Forum. "Global Risks Report 2026." 2026.
https://www.weforum.org/press/2026/01/global-risks-report-2026-geopolitical-and-economic-risks-rise-in-new-age-of-competition/

Stanford HAI. "AI Index Report 2026." 2026.
https://hai.stanford.edu/ai-index/2026-ai-index-report

Lewis, C.S. *The Abolition of Man.* 1943.

Jung, C.G. *The Undiscovered Self.* 1957.

Russell, B. and Einstein, A. "The Russell-Einstein Manifesto." 1955.
https://ahf.nuclearmuseum.org/ahf/key-documents/russell-einstein-manifesto/
