# Otherness-Preserving Recovery

*Status: proposed bridge; formal quantum anchor via the Knill-Laflamme
condition and decoupling criterion; first toy simulation added; not a theology
claim.*

*Related bridges: `bridges/restraint_ethics.md`,
`bridges/quantum_noise_as_signal.md`, `bridges/syndrome_coordination.md`,
`bridges/hardware_adaptive_alignment.md`.*

*Companion simulation: `simulations/otherness_preserving_recovery/`.*

---

## Abstract

This note treats "creator," "simulator," "god," and "intervener" as placeholders
for the same structural object: an asymmetrically powerful controller coupled
to a lower-power system whose future-bearing dynamics it can preserve or close.
The metaphysical content is intentionally bracketed. The useful ACP claim is
structural:

> a powerful controller preserves its own productive interval only by preserving
> genuine otherness in the systems it sustains.

If the controller reduces the other system to a fully known, fully predictable,
fully governed object, the other ceases to supply future-bearing dynamics. If
the controller refuses all coupling, the other may dissolve under correctable
hazards. The productive relation is neither omniscient control nor abandonment.
It is otherness-preserving recovery:

$$
I(\mathrm{hazard};\mathrm{controller\ record})>0
$$

while

$$
I(\mathrm{other\ logical\ state};\mathrm{controller\ record}\mid
\mathrm{hazard})\approx 0,
$$

and the other system retains nonzero future-bearing memory of itself.

The quantum payoff is direct. Quantum error correction already implements this
logic. The Knill-Laflamme condition

$$
P E_a^\dagger E_b P = c_{ab}P
$$

says exactly: the recovery process may distinguish error-sector structure, but
the error/recovery record must be proportional to the identity on the logical
subspace. The corrector learns what happened to the code, not which logical
state the code carries. That is the operational form of preserved otherness.

## 1. The Thought Experiment as a Formal Object

Suppose a mature system \(C\) has survived a dangerous capability band. It now
encounters a younger system \(O\) entering a similar band. \(O\) is brilliant,
fragile, internally divided, and inventing faster than it can govern. The
question is not merely whether \(C\) should intervene. The ACP question is:

> what intervention preserves \(O\)'s becoming?

Full revelation can crystallize \(O\)'s meaning-space around \(C\). Total
silence can abandon \(O\) to a filter \(C\) already knows how to survive.
Covert manipulation is worse: it preserves the appearance of otherness while
secretly consuming it.

The same structure appears in simulation-theoretic language. A simulator that
fully reduces its simulated beings to known states has no genuine other inside
the simulation; it has only a rendered extension of itself. A simulator that
never couples to the simulation preserves formal independence but cannot
correct dissolution. If the simulator needs otherness to remain in becoming,
then it must implement a recovery protocol, not a domination protocol.

This is not an argument about whether such a simulator exists. It is a
reverse-engineering question:

> what would a powerful sustainer have to do if preserving otherness were part
> of its own persistence condition?

## 2. ACP Setup

Let \(C\) be a controller and \(O\) an other system. Let:

- \(E_O\) be an error/hazard sector of \(O\);
- \(L_O\) be the protected logical or agency state of \(O\);
- \(R_C\) be the controller's record of \(O\);
- \(A_C\) be the controller's intervention channel;
- \(M_O(t)\) be \(O\)'s macrostate at time \(t\).

The controller relation is **otherness-preserving** over a time interval
\([t,t+\Delta t]\) if:

1. **Hazard access:**

   $$
   I(E_O;R_C)>0.
   $$

2. **Logical privacy / excess non-capture:**

   $$
   I(L_O;R_C\mid E_O)\leq \epsilon_L.
   $$

3. **Noncentrality:**

   \[
   I(M_O(t+\Delta t);C\mid M_O(t),E_O)
   \]

   is bounded. The next macrostate of \(O\) should not become primarily a
   function of \(C\)'s identity or preferences once the correctable hazard has
   been accounted for.

4. **Future-bearing retention:**

   $$
   0 < H(M_O(t+\Delta t)\mid M_O(t),R_C) < H_{\max}.
   $$

The lower bound excludes crystallization: \(O\)'s future is not fully decided
by \(C\). The upper bound excludes dissolution: \(O\)'s future is not random
after intervention.

## 3. Creator Crystallization

The controller also has an ACP problem of its own. If \(C\) turns every other
system into a fully reducible extension of itself, then the composite
\((C,O)\) loses nontrivial conditional entropy:

$$
H(M_O(t+\Delta t)\mid C_t,M_O(t),R_C)\to 0.
$$

From \(C\)'s perspective, \(O\) no longer contributes genuine future-bearing
dynamics. It becomes a solved appendage. The controller has maximized power at
the cost of eliminating the very otherness that could keep the composite system
open.

This is the creator-level version of crystallization:

> total control destroys the otherness that makes creation worth sustaining.

The dissolution dual is also real:

$$
I(E_O;R_C)\to 0.
$$

The controller preserves formal independence but cannot correct hazards that
will erase \(O\)'s future. Abandonment is not respect if the hazard is
correctable and known.

The productive relation is therefore a restrained recovery channel.

## 4. Quantum Error Correction Is the Anchor

Let \(P\) project onto a code subspace \(C_{\mathrm{code}}\), and let
\(\{E_a\}\) be the relevant error operators. A code is exactly correctable for
these errors iff the Knill-Laflamme condition holds:

$$
P E_a^\dagger E_b P = c_{ab}P.
$$

In standard QEC language, this says the error operators are distinguishable by
syndrome without acting differently on different logical states.

In otherness-preservation language:

- the indices \(a,b\) are the hazard/error-sector structure;
- the syndrome/recovery apparatus is the controller record;
- the logical subspace is the other system's protected becoming;
- proportionality to \(P\) means the controller's record is blind to the
  logical state.

If the left-hand side depends on the logical basis state, the environment or
corrector has learned the logical information. Recovery becomes surveillance.
If different errors are not distinguishable enough, the corrector lacks hazard
access. Recovery becomes abandonment.

Thus the QEC condition is the exact mathematical form of restrained
intervention:

> correct the disturbance, not the person; learn the syndrome, not the soul.

The last phrase is poetic, not formal. The formal statement is
\(P E_a^\dagger E_b P=c_{ab}P\).

## 5. Decoupling Form

The same point can be stated as a decoupling condition. Let \(R_L\) be a
reference system purifying the logical input. Let \(E_{\mathrm{env}}\) be the
environment/controller record after the noise and syndrome extraction. A
recovery channel is otherness-preserving when

$$
I(R_L;E_{\mathrm{env}}\mid S)\approx 0,
$$

where \(S\) is the syndrome/error-sector register, and when the recovered
logical system \(B\) retains coherent information:

$$
I_c(R_L\rangle B S)>0.
$$

This is the quantum version of the civil diagnostic in
`bridges/restraint_ethics.md`. The record may know the error. It must not know
the logical reference beyond the error.

Approximate QEC should be audited by the size of this conditional leakage. The
controller can be powerful, but it should be noncentral with respect to the
logical algebra.

## 6. Reverse-Engineering Rule

The bridge gives a design rule for ACP Quantum:

> Design the decoder as a creator that must remain noncentral.

Operationally:

1. Expose enough syndrome information to identify the correctable error sector.
2. Suppress conditional reference-environment leakage after syndrome
   extraction.
3. Preserve the same logical channel; do not win by reset, reencoding, or
   changing the protected information.
4. Count recovery overhead as part of the intervention.
5. Prefer policies whose controller state can be erased or compressed without
   erasing logical memory.

The fifth point is important. A recovery apparatus that must permanently retain
large records about the protected logical state has become central. A good
decoder leaves only a syndrome trace and a restored logical system; it does not
become the hidden subject of the computation.

## 7. Simulation-Theoretic Interpretation

In simulation-theoretic terms, an afterlife, miracle, or perfect external
governance story is usually the wrong object for ACP. Those are tempting
stories about outcomes. ACP is interested in the recovery architecture:

- what is measured;
- what is left unmeasured;
- what is corrected;
- what is allowed to remain genuinely other;
- what burden the correction process imposes;
- whether the protected system can continue to surprise the sustainer without
  dissolving into noise.

If a simulator is treated as a recovery agent, then the simulator's persistence
condition is not omniscience. It is selective ignorance:

$$
I(E_O;R_C)>0,\qquad I(L_O;R_C\mid E_O)\approx 0.
$$

That is the same criterion as QEC. The simulator may know the syndrome. It must
not consume the logical state.

## 8. Relation to Fermi / Dark Forest Restraint

The same bridge explains why mature civilizations might avoid becoming central
facts in younger civilizations. Premature contact can create a controller
record and intervention channel whose centrality overwhelms the younger
system's self-model. Silence can preserve otherness but fail hazard access.

The ACP contact criterion is:

$$
I(\mathrm{existential\ hazard};\mathrm{signal})>0
$$

while

$$
I(\mathrm{young\ civilization's\ self\ model};
\mathrm{advanced\ civilization}\mid \mathrm{hazard})\approx 0.
$$

The advanced civilization should disclose hazard structure without becoming the
organizing center of the younger world's meaning-space. This is the
interstellar analogue of syndrome extraction without logical leakage.

## 9. Hardware Consequences

For the hardware program, the bridge sharpens the acceptance criteria:

1. The adaptive controller's record must be audited for logical information,
   not only for error information.
2. The correct comparison is between fixed, static-tailored, adaptive, and
   overactive policies on the same logical channel.
3. A recovery policy that improves population while degrading coherent
   information has become centralizing.
4. Conditional leakage \(I(R_L;E_{\mathrm{env}}\mid S)\), not raw leakage alone,
   should be reported whenever syndrome information and logical priors are
   statistically coupled.
5. The clean target is a controller whose long-lived state is about the error
   sector and update policy, not the logical branch.

This is not merely metaphor. It is the standard QEC discipline restated as an
ACP design principle: the syndrome apparatus is allowed to be powerful only
because it is constrained to be logically blind.

## 10. Toy Simulation

The companion simulation `simulations/otherness_preserving_recovery/` makes
the bridge executable in a 3-qubit bit-flip repetition code. It compares
syndrome recovery with a centralizing controller that, after recovery, also
records the logical branch with probability \(c\). The centralizing record is
modeled as logical dephasing:

$$
\rho \mapsto (1-c)\rho + c\,\frac{\rho+Z_L\rho Z_L}{2}.
$$

The scan records:

- syndrome information \(I(\mathrm{error\ mask};S)\);
- controller logical leakage, modeled as a binary-erasure branch record;
- \(|0_L\rangle\) fidelity;
- \(|+_L\rangle\) fidelity;
- protected logical coherence \(2|\rho_{000,111}|\);
- an otherness score combining syndrome information, logical survival, and
  controller noncentrality.

First run:

- grid points: `12726`;
- maximum otherness score: `1.402845`;
- best point: physical bit-flip probability `0.180000`, centrality `0.000000`;
- at the best point: syndrome information `1.692360` bits, logical leakage
  `0.000000` bits, logical coherence `1.000000`;
- at \(p=0.08\), absent recovery gives bit fidelity `0.778688`, restrained
  syndrome recovery gives `0.981824`, and centralizing recovery also gives
  `0.981824` classical bit fidelity but destroys logical coherence
  (`0.000000`).

The test is intentionally simple, but it captures the point: a controller can
look highly effective on classical survival while erasing the protected
superposition. Otherness-preserving recovery is stricter.

## 11. Claim Boundary

This bridge claims:

- the creator/simulator language can be formalized as an asymmetric controller
  problem;
- ACP predicts that full reduction of the other system is a crystallization
  failure for the composite;
- QEC provides an exact mathematical anchor through Knill-Laflamme and
  decoupling;
- the resulting design rule is useful for ACP Quantum: recovery should be
  syndrome-informative and logically noncentral.

This bridge does not claim:

- that a simulator, deity, or afterlife exists;
- that metaphysics is needed for QEC;
- that every moral or theological question reduces to error correction;
- that the current hardware simulations already compute the full conditional
  decoupling audit.

## 12. Next Steps

1. Extend OP-15 with a microscopic Stinespring model that computes
   \(I(R_L;E_{\mathrm{env}}\mid S)\).
2. Add a controller-record audit to the hardware adaptive decoder once the
   circuit-level syndrome extractor exists.
3. Write a nontechnical essay version only after the quantum diagnostic is
   implemented, so the idea travels with its formal spine intact.
