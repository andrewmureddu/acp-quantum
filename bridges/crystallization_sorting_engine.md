# The Crystallization Sorting Engine

*Status: active component of the ACP quantum-gravity derivation program.
Theorems 1-5 are proven for classical record-retaining dynamics and Theorems
1-Q, 3-Q, 4-Q, 6, and 7 for quantum ones. The gravitational identification of
the contraction rate and the boundary capacity is imported, not derived, and is
marked ⚠ throughout.*

Companion notes:

- `bridges/quantum_gravity_derivation_program.md`
- `bridges/relational_observable_macrostate_kernel.md`
- `bridges/singularity_inadmissibility.md`
- `bridges/cosmic_coordination_floor.md`
- `bridges/otherness_preserving_recovery.md`
- `bridges/schur_complement.md`

Executable companions: `simulations/crystallization_sorting_engine/`
(classical ledger and quantum ledger) and
`simulations/hardware_adaptive_decoder/sorting_ledger_audit.py` (measurement on
the H2 QEC scaffold).

## 1. Thesis

Andrew's framing:

> singularity = where reality's sorting machine resides. You know how a change
> machine sorts coins? Something like that. The pressure from the
> crystallization is put to work to sort/process.

This note makes that precise, and the precise version turns out to be
load-bearing rather than decorative.

The existing derivation program treats contraction toward the crystallization
boundary as a hazard: a collapsing region narrows its own future channel and
must be stopped before the coordination floor is breached. That reading is
correct but incomplete. It says what contraction *costs* and never says what
contraction *buys*.

The claim of this note is:

> Contraction toward the crystallization boundary is the sole power source for
> boundary record formation. A region can export information about its interior
> only by reducing the distinguishability it retains. Collapse is therefore not
> merely a hazard to be averted; it is the engine stroke of a sorting machine
> whose output is the boundary record. What ACP forbids is not contraction but
> *wasted* contraction: distinctions merged before they were sorted.

The coin-sorter picture is exact in the following sense. A change machine has
(i) a pressure source, gravity pulling coins down the chute; (ii) a fixed set
of slots, which is a finite partition of the coins by denomination; (iii) an
output, coins filed into slots; and (iv) a blind spot, it never reads the mint
year or the serial number of any individual coin. Each of these has an exact
counterpart below: the crystallization drift, the record channel's finite slot
partition, the exported mutual information, and the Knill-Laflamme blindness
condition on the protected label.

## 2. Honesty Boundary

**Proven in this note.** Sections 3-6 are theorems about any finite
record-retaining Markov dynamics. They are elementary consequences of the chain
rule and the data processing inequality; the content is the identification of
the terms, not the difficulty of the proofs. Section 14 restates the same
ledger for a quantum record channel, where it becomes an exact three-way
conservation law and where the classical residual column is identified as
leakage to the unrecorded environment. All are verified numerically to machine
precision in the simulations.

**Derived as an ACP requirement.** Section 7 converts the bounds into a design
rule for admissible completions and a quantitative trigger-time statement. This
strengthens the existing "redistribute before the floor" requirement from a
qualitative ordering claim into an inequality between a contraction rate and a
channel capacity.

**⚠ Conjectural in physics.** Section 9 identifies the contraction rate with
gravitational focusing and the record capacity with a boundary-area bound.
Neither identification is derived here. They are imported from the Raychaudhuri
equation and the Bekenstein-Hawking area law respectively, and the resulting
"the completion scale is a bandwidth scale" conjecture is an open claim.

**Still open.** This note does not derive the microscopic throttle, does not
prove that gravitational focusing has the assumed relationship to macrocell
merging, and does not compute the boundary capacity from first principles.

## 3. The Distinguishability Ledger

Fix a finite-resolution relational region as in
`bridges/relational_observable_macrostate_kernel.md`. Let:

- \(S_0\) be the initial interior microstate label, a random variable on a
  finite admissible alphabet;
- \(M_k\) be the interior register at step \(k\), taking values in a finite set
  of coarse labels;
- \(R_{\leq k}=(R_1,\ldots,R_k)\) be the accumulated boundary record.

Assume two structural conditions, both of which hold for any physical channel
with a retained exterior record:

**(M) Markov update.** The pair \((M_{k+1},R_{\leq k+1})\) is produced from
\((M_k,R_{\leq k})\) by a channel that does not consult \(S_0\):

$$
S_0
\ \longrightarrow\
(M_k,R_{\leq k})
\ \longrightarrow\
(M_{k+1},R_{\leq k+1}).
$$

**(R) Record retention.** \(R_{\leq k}\) is a function of \(R_{\leq k+1}\);
records once written are not erased.

Define the three columns of the ledger:

$$
T_k=I(S_0;M_k,R_{\leq k}),
\qquad
E_k=I(S_0;R_{\leq k}),
\qquad
J_k=I(S_0;M_k\mid R_{\leq k}).
$$

\(T\) is the total surviving distinguishability of the initial interior state,
\(E\) is the column already exported to the boundary, and \(J\) is the column
still held privately inside — the *backlog*, the coins still in the hopper.

Define the per-step increments:

$$
\gamma_k=J_k-J_{k+1},
\qquad
\sigma_k=E_{k+1}-E_k,
\qquad
\delta_k=T_k-T_{k+1}.
$$

**Theorem 1 (ledger identity).** Under (M) and (R):

1. \(T_k=J_k+E_k\) for every \(k\);
2. \(\delta_k\geq 0\) and \(\sigma_k\geq 0\);
3. \(\gamma_k=\sigma_k+\delta_k\), so \(\gamma_k\geq 0\) and \(J\) is
   non-increasing;
4. \(\sum_{k<n}\gamma_k=J_0-J_n\leq H(S_0)\).

**Proof.** (1) is the chain rule
\(I(S_0;M_k,R_{\leq k})=I(S_0;R_{\leq k})+I(S_0;M_k\mid R_{\leq k})\).
(2) \(\delta_k\geq0\) is the data processing inequality applied to (M);
\(\sigma_k\geq0\) holds because \(R_{\leq k}\) is a function of
\(R_{\leq k+1}\) by (R), so \(I(S_0;R_{\leq k+1})\geq I(S_0;R_{\leq k})\).
(3) substitute \(J=T-E\):
\(J_k-J_{k+1}=(T_k-T_{k+1})+(E_{k+1}-E_k)=\delta_k+\sigma_k\).
(4) telescoping, with \(J_0\leq H(S_0)\) and \(J_n\geq 0\). \(\square\)

Read as an engine: \(\gamma\) is the stroke, \(\sigma\) is the useful output,
\(\delta\) is the waste. Clause (4) says the fuel tank is finite. A collapsing
region has a bounded total quantity of interior distinguishability, and every
bit of it is spent exactly once, either into the boundary record or into
nothing.

**Definition (sorting efficiency).** For a window with
\(\sum\gamma_k>0\),

$$
\chi
=
\frac{\sum_k\sigma_k}{\sum_k\gamma_k}
=
\frac{E_n-E_0}{J_0-J_n}
\in[0,1].
$$

\(\chi=1\) is a lossless sort: everything the interior stopped holding, the
boundary started holding. \(\chi=0\) is pure crystallization drift: the
interior stopped holding it and nobody picked it up.

## 4. Contraction Is the Power Source

**Theorem 2 (no record without contraction).** Under (M) and (R),

$$
\sigma_k\leq\gamma_k,
\qquad\text{hence}\qquad
E_n-E_0\leq J_0-J_n .
$$

**Proof.** Immediate from Theorem 1(3) and \(\delta_k\geq0\). \(\square\)

Trivial to prove, but it is the formal content of Andrew's "the pressure is put
to work," and it has three consequences worth stating separately.

**Corollary 2.1 (silence of the uncontracted).** A region whose retained
interior distinguishability is constant, \(\gamma_k=0\), emits no information
about its own initial state: \(\sigma_k=0\). It may radiate, and its records may
have high entropy, but those records are uncorrelated with what is inside.

**Corollary 2.2 (records are crystallization's exhaust).** The boundary's total
knowledge of the interior is bounded by the interior's total loss of self-
distinguishability. Perfect boundary reconstruction requires complete interior
contraction.

**Corollary 2.3 (the two ACP boundaries, in engine variables).** The productive
interval acquires a mechanical reading:

| ACP regime | Engine reading |
|---|---|
| dissolution | no contraction available, or record channel uncorrelated with the interior; \(\sigma\approx 0\) with \(J\) frozen |
| crystallization | contraction with \(\chi\to0\); the fuel is spent, nothing is filed |
| productive interval | contraction with \(\chi\) bounded away from \(0\); the machine sorts |

This is a strengthening of the CDT reading rather than a restatement of it. CDT
says a persistent system must sit strictly between the two absorbing
boundaries. The ledger says *why* the crystallization side cannot simply be
avoided by refusing to contract: refusing to contract is refusing to emit
records, and a system that emits no records about itself has no boundary
channel, no clock, and no decodable history. Persistence requires spending the
budget, and admissibility is a constraint on *how* it is spent.

## 5. Sort Before You Crush

**Theorem 3 (lossless sorting rule).** Suppose that at step \(k\) the merged
distinctions are already determined by the record: that is, there exists a
measurable \(\phi_k\) with

$$
(M_k,R_{\leq k})=\phi_k(M_{k+1},R_{\leq k+1})
\qquad\text{almost surely.}
$$

Then \(\delta_k=0\), and the step is a pure sort: \(\gamma_k=\sigma_k\).

**Proof.** By (M) and the data processing inequality,
\(T_{k+1}\leq T_k\). Conversely, \((M_{k+1},R_{\leq k+1})\mapsto
\phi_k(M_{k+1},R_{\leq k+1})=(M_k,R_{\leq k})\) is a deterministic map, so the
data processing inequality in the other direction gives
\(T_{k+1}=I(S_0;M_{k+1},R_{\leq k+1})\geq I(S_0;M_k,R_{\leq k})=T_k\). Hence
\(T_{k+1}=T_k\), i.e. \(\delta_k=0\). \(\square\)

**Proposition 3.1 (converse, sufficiency form).** \(\delta_k=0\) holds if and
only if \((M_{k+1},R_{\leq k+1})\) is a sufficient statistic for \(S_0\)
relative to \((M_k,R_{\leq k})\), equivalently if and only if there is a
recovery channel \(\mathcal R\) with
\(\mathcal R(M_{k+1},R_{\leq k+1})\overset{d}{=}(M_k,R_{\leq k})\) jointly with
\(S_0\). Deterministic recoverability is sufficient but not necessary; the
correct general condition is recoverability, in the Petz sense.

Theorem 3 is the design rule the whole note exists to produce:

> **Never merge a distinction you have not already exported.**

A change machine that crushes the coins before reading them is not a sorting
machine; it is a furnace. The difference between the two is not the pressure —
both use exactly the same pressure — but the ordering of read and crush.

This gives the ACP-admissible completion a positive characterization rather
than a prohibition. `bridges/singularity_inadmissibility.md` says what a
completion must *not* do: reach a singular endpoint. Theorem 3 says what it
must *do*: maintain the read-before-crush ordering on every distinction it
destroys.

## 6. Bandwidth

Theorem 3 states a rule. The next theorem states why the rule is not free.

Let \(\mathcal R_{k+1}\) be the alphabet of the record emitted at step
\(k+1\) and let

$$
C_k=\log_2|\mathcal R_{k+1}|
$$

be the per-step record capacity — the number of slots on the sorting machine.

**Theorem 4 (bandwidth-limited sorting).** Under (M) and (R),

$$
\sigma_k
\leq
H(R_{k+1}\mid R_{\leq k})
\leq
C_k,
$$

and therefore

$$
\boxed{\ \delta_k\ \geq\ \gamma_k-C_k\ }
$$

Cumulatively, \(\sum_{k<n}\delta_k\geq (J_0-J_n)-\sum_{k<n}C_k\).

**Proof.** \(\sigma_k=I(S_0;R_{k+1}\mid R_{\leq k})\leq H(R_{k+1}\mid
R_{\leq k})\leq\log_2|\mathcal R_{k+1}|\). Substitute into
\(\delta_k=\gamma_k-\sigma_k\). \(\square\)

**Corollary 4.1 (over-driven collapse must destroy).** If \(\gamma_k>C_k\) then
\(\delta_k>0\) strictly. Contraction faster than the boundary can export
necessarily annihilates information, regardless of how well designed the sorter
is. Lossless sorting is *unenforceable*, not merely unenforced, once the
contraction rate exceeds the channel capacity.

**Corollary 4.2 (resolution ceiling).** Capacity is not the only limit.
Let \(\Pi\) be the slot partition of the record channel. Distinctions inside a
single block of \(\Pi\) can never be exported, so

$$
E_\infty\leq H(\Pi(S_0)),
\qquad
\chi\leq\frac{H(\Pi(S_0))}{J_0-J_\infty}.
$$

A machine with unlimited throughput and one slot exports nothing. Bandwidth
without resolution is not sorting; it is a bell that rings at every coin.

Corollary 4.2 is the formal reason the classical collapse baseline fails even
when it radiates copiously. A record channel that reports only *that* collapse
occurred has positive capacity and zero sorting efficiency.

## 7. The ACP Completion Requirement

Combining Theorems 3 and 4 gives the operational form of the ACP requirement
for gravitational completions.

**Theorem 5 (trigger time).** Suppose a completion mechanism can be engaged at
step \(\tau\), and that from \(\tau\) onward the lossless rule of Theorem 3 is
enforced. Then the unavoidable destruction satisfies

$$
\sum_{k}\delta_k
\ \geq\
\sum_{k<\tau}\max\left(0,\ \gamma_k-C_k\right).
$$

In particular, if \(\gamma_k>C_k\) for any \(k<\tau\), the completion cannot
recover a lossless history no matter how perfect it is after \(\tau\).

**Proof.** Destruction before \(\tau\) is bounded below termwise by
Corollary 4.1, and destruction is non-negative after \(\tau\). \(\square\)

This is the quantitative version of a claim the derivation program previously
made only qualitatively — that redistribution must occur *before* the floor is
reached. The sharpened statement is:

> The completion must engage before the contraction rate first exceeds the
> boundary record capacity, not merely before the coordination floor is
> reached. Waiting until the floor is imminent guarantees a positive
> information debt that no subsequent mechanism can repay.

**Corollary 5.1 (contraction throttle).** A completion that achieves
\(\delta_k=0\) for all \(k\) must satisfy \(\gamma_k\leq C_k\) at every step.
Since \(C_k\) is a property of the boundary channel, and \(\gamma_k\) is a
property of the interior dynamics, an admissible completion must modify the
*dynamics* so that contraction never outruns export. ACP does not permit an
arbitrarily fast collapse coupled to an arbitrarily good decoder.

There are exactly three ways to satisfy \(\gamma_k\leq C_k\), and they exhaust
the strategy space:

1. **Throttle.** Reduce \(\gamma_k\): slow, halt, or reverse the contraction.
   This is the strategy of bounces, regular-black-hole cores, effective
   repulsive terms, and asymptotic-safety interiors.
2. **Widen.** Increase \(C_k\): grow the boundary channel. This is the strategy
   of horizon area growth and of any mechanism that adds record modes.
3. **Buffer.** Hold the backlog: refuse to merge unexported distinctions and
   carry \(J>0\) until capacity becomes available. This is the strategy of
   remnants, islands, and protected interior subspaces.

The three are not competing intuitions about black holes; they are the three
degrees of freedom in one inequality. A viable completion picks a schedule over
them.

## 8. Efficiency Is Not Legitimacy

The ledger scores a machine on whether it wastes. It says nothing about whether
the machine is entitled to read what it reads. These are independent axes, and
conflating them is the main trap this framework creates.

Split the interior label as \(S_0=(G,L)\), with \(G\) the sector label
(geometry sector, error sector) and \(L\) the protected label (interior
microstate, logical state). The selectivity conditions from
`bridges/relational_observable_macrostate_kernel.md` and
`bridges/otherness_preserving_recovery.md` are:

$$
I(G;R_{\leq k})>0
\quad\text{early},
\qquad
I(L;R_{\leq k}\mid G)\leq\epsilon_L
\quad\text{early},
$$

with late release \(I(L;R_{\leq k}\mid G)\to H(L\mid G)\) after the decoding
scale \(T_{\mathrm{dec}}\).

A sorter reading the singleton partition — one slot per microstate — achieves
\(\chi=1\) exactly, wastes nothing, and is inadmissible, because it files coins
by serial number. The Knill-Laflamme condition
\(PE_a^\dagger E_bP=c_{ab}P\) is precisely the statement that the machine's
slots resolve error sectors and are degenerate on the protected label: a
denomination sorter, not an identity sorter.

**Acceptance criterion.** An admissible sorting engine must satisfy both:

$$
\chi\approx 1
\qquad\text{and}\qquad
I(L;R^{\mathrm{early}}_{\leq k}\mid G)\leq\epsilon_L .
$$

Neither implies the other, and the simulation exhibits a policy that passes
each while failing the other.

## 9. The Three Exits

Theorem 1(4) says the budget is finite; the ledger says where it can go. A
collapse history therefore has exactly three asymptotic outcomes, distinguished
by \((\chi,J_\infty)\):

| Exit | Signature | Reading |
|---|---|---|
| destruction | \(\chi<1\) | information annihilated; the singular endpoint; classical collapse |
| permanent backlog | \(\chi=1\), \(J_\infty>0\) | remnant or eternally protected interior; lossless but never released |
| complete export | \(\chi=1\), \(J_\infty=0\) | the full budget reaches the boundary |

The third exit produces a two-phase export curve: an early phase in which only
the sector column rises, and a late phase after the release channel opens in
which the protected column is transferred. ⚠ This is Page-like in shape and in
the role of the decoding scale, but the toy is a classical finite record model
and the resemblance should not be read as a derivation of the Page curve.

The second exit deserves a warning that this framework makes newly precise. A
permanent backlog is *not* an information paradox — nothing was destroyed — but
it is an ACP problem of a different kind: the region continues to hold
distinguishability it can never spend, which is a frozen rather than a burnt
budget. `bridges/self_limiting_universality.md` treats the deliberate version
of this as protected forgetting; the involuntary version is a remnant.

## 10. Gravitational Reading (⚠ conjectural)

The identifications below are imported, not derived. They are what would have
to be true for the theorems above to constrain gravity.

**Contraction rate.** \(\gamma_k\) should be controlled by focusing. The
Raychaudhuri equation

$$
\frac{d\theta}{d\lambda}
=
-\frac{\theta^2}{3}
-\sigma_{ab}\sigma^{ab}
+\omega_{ab}\omega^{ab}
-R_{ab}k^ak^b
$$

drives \(\theta\to-\infty\) in finite affine parameter under the standard
convergence and no-rotation assumptions. Neighboring relational macrocells
merge, and the merging accelerates. ⚠ The step from "geodesic congruences
focus" to "the macrocell kernel loses \(\gamma_k\) bits per step" is a
coarse-graining claim this note does not prove.

**Capacity.** \(C_k\) should be controlled by the boundary. The
Bekenstein-Hawking relation \(S_{\mathrm{BH}}=A/4G\hbar\) bounds the record
capacity supported on a boundary of area \(A\), and the per-step exportable
information is bounded by the emission rate through that boundary. ⚠ Using the
area law as a channel capacity is standard practice in the holographic
literature but is an import here, not a derivation.

**The over-drive claim.** Granting both identifications, classical collapse has
\(\gamma_k\) growing without bound while the interior's own boundary capacity
is bounded. Corollary 4.1 then forces \(\delta_k>0\): classical collapse
destroys information not because of curvature divergence per se, but because it
contracts faster than any finite boundary can file the results. The singularity
is the point at which the sorting machine's hopper empties into nothing.

**Conjecture SE-1 (the completion scale is a bandwidth scale).** The scale at
which quantum gravity must modify classical collapse is set by where the
focusing-induced contraction rate first exceeds the boundary export capacity,
\(\gamma=C\), rather than by a fixed curvature threshold alone. Two collapses
reaching the same curvature with different boundary capacities should require
the completion to engage at different curvatures.

**Conjecture SE-2 (throttle-capacity complementarity).** Every admissible
completion mechanism implements some schedule over throttle, widening, and
buffering (Section 7), and mechanisms that appear physically unrelated —
bounces, horizon growth, islands, remnants — should be classifiable by which
term they use and when.

Conjecture SE-1 is the more interesting of the two because it is
differential: it predicts a *relationship* between completion onset and
boundary capacity rather than a single number, and it is in principle
falsifiable inside any candidate theory that supplies both quantities.

## 11. QEC Reading

The QEC laboratory instantiates every term concretely, which is why the program
keeps it as the technical engine.

| Engine term | QEC | Gravity (⚠) |
|---|---|---|
| interior register \(M_k\) | physical data qubits | interior relational macrocell |
| backlog \(J_k\) | unextracted error/state information | interior distinguishability not yet on the boundary |
| record \(R_{\leq k}\) | syndrome history | boundary/null records \(R_\partial\) |
| slot partition \(\Pi\) | stabilizer group / syndrome map | finite boundary observable partition |
| capacity \(C_k\) | syndrome bits per cycle | area-bounded export per step |
| contraction \(\gamma_k\) | decoherence, leakage, merging of code states | focusing |
| destruction \(\delta_k\) | uncorrectable logical error | information loss at the singular endpoint |
| efficiency \(\chi\) | fraction of decoherence that shows up as syndrome | fraction of collapse that shows up as boundary record |
| selectivity | Knill-Laflamme degeneracy on the logical label | early interior privacy |

The QEC translation of Theorem 2 is worth stating on its own, because it is
usually described the other way round: *syndrome information is paid for out of
the code's own coherence budget.* A syndrome extraction that learns nothing has
disturbed nothing, and one that learns everything about the error sector has
consumed exactly that much of the code's retained distinguishability. The
existing `simulations/risky_qec_claims/` result — that a noisy channel can
carry syndrome information while a clean one carries none — is the resolution
ceiling of Corollary 4.2 in a different vocabulary.

## 12. Simulation

`simulations/crystallization_sorting_engine/sorting_engine.py` propagates the
exact joint distribution over \((S_0,M_k,R_{\leq k})\) for a nine-microstate
interior with \(H(S_0)=\log_2 9=3.169925\) bits, factored as a
three-valued sector label \(G\) and a three-valued protected label \(L\). No
sampling is used; record branches with equal posteriors are merged, which is
exact because every reported quantity is a weighted function of the branch
posterior alone.

Six policies share one boundary-channel schedule and differ only in what they
read and when they contract. Default seeded run, 24 steps:

| Policy | \(\chi\) | exported (bits) | backlog (bits) | early \(I(L;R\mid G)\) | BW-limited steps | verdict |
|---|---:|---:|---:|---:|---:|---|
| classical_collapse | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | destructive: crushes without sorting |
| over_driven_sorter | 0.443299 | 1.405225 | 0.000000 | 0.000000 | 0 | destructive: contraction outruns export |
| late_completion | 0.500003 | 1.584972 | 0.000000 | 0.000000 | 1 | destructive: contraction outran capacity |
| stalled_remnant | 1.000000 | 1.584963 | 1.584963 | 0.000000 | 0 | lossless but permanent backlog |
| centralizing_sorter | 1.000000 | 3.169925 | 0.000000 | 1.540191 | 0 | lossless but centralizing |
| sort_then_contract | 1.000000 | 3.169925 | 0.000000 | 0.000000 | 0 | admissible |

Numerical validation across all six policies: maximum ledger-identity residual
\(|\gamma-\sigma-\delta|\) is \(2.2\times10^{-15}\) bits, the Theorem 2 bound
\(\sigma\leq\gamma\) is never violated by more than \(1.1\times10^{-15}\) bits,
and the Theorem 4 bound \(\delta\geq\gamma-C\) is never violated.

Four results are worth extracting.

**The classical baseline fails on resolution, not bandwidth.**
`classical_collapse` has a record channel with positive capacity (one bit per
step) and exports exactly zero. It reports *that* collapse is occurring and
nothing about *what* is collapsing. \(\chi=0\), the entire 3.170-bit budget
destroyed. This is Corollary 4.2, and it is the precise sense in which a
radiating classical singularity is not a sorting machine.

**Trigger time is decisive and cheap to get wrong.** `sort_then_contract` and
`late_completion` implement the same read-then-crush idea with the same slots.
The first engages from step 0 and achieves \(\chi=1\) with the whole budget
exported. The second waits until step 14 and then crushes at rate 0.95 in a
single step: contraction of 3.01 bits against a 2-bit channel, one
bandwidth-limited step, and \(\chi=0.500\) — exactly half the budget burned,
with the sector column surviving and the protected column annihilated. Theorem
5 in one line of output.

**Efficiency and legitimacy are orthogonal.** `centralizing_sorter` is a
perfect engine: \(\chi=1\), full export, zero waste. It is also inadmissible,
reading 1.540 bits of protected label before the decoding scale.
`sort_then_contract` achieves the identical ledger with 0.000 bits of early
leakage. Nothing in Theorems 1-5 distinguishes them; only Section 8 does.

**A lossless machine can still fail by never finishing.** `stalled_remnant`
never opens a protected-release channel. It wastes nothing, \(\chi=1\), and
ends holding \(\log_2 3=1.585\) bits it can never spend.

The throughput scan (`outputs/sorting_engine_throughput_scan.csv`,
`outputs/sorting_engine_throughput_frontier.svg`) sweeps contraction rate,
emission throughput, and slot resolution over 108 ungated configurations. It
shows the frontier the theorems predict:

- \(\chi\) falls monotonically with contraction rate at fixed channel, from
  0.738 to 0.105 for the full-resolution channel at emission probability 0.1;
- \(\chi=1.000000\) at *every* contraction rate when resolution and throughput
  are both maximal, confirming Corollary 4.1's reading that destruction is
  caused by the channel's inability to keep up, not by the pressure itself;
- \(\chi=0\) at every rate for the single-slot channel regardless of throughput,
  which is Corollary 4.2;
- sector-resolution channels with full throughput sit at exactly
  \(\chi=0.500000\) for every contraction rate at which the run completes its
  contraction, matching Corollary 4.2's ceiling
  \(H(\Pi(S_0))/(J_0-J_\infty)=\log_23/\log_29\). At the slowest rate the same
  channel scores 0.585 only because the 24-step window ends with 0.463 bits of
  backlog still unspent, so the denominator is not yet the full budget.

## 13. Measurement on the H2 QEC Scaffold

The ledger has now been measured on real project hardware-facing code rather
than only on its own toy. `simulations/hardware_adaptive_decoder/sorting_ledger_audit.py`
imports the H2 circuit-level primitives unchanged — same fault model, same
parity-extraction circuit, same decoder policies, same drift and calibration
schedule already audited for logical error in
`bridges/hardware_adaptive_alignment.md`.

**Probe.** At the start of a measurement window the data register is placed in
an unknown error configuration \(S_0\), uniform over the eight three-qubit
states, and the window then runs ordinary H2 rounds with the protocol's real
decoder state carried forward from round 0. The joint over
\((S_0,D_k,R_{\leq k})\) is propagated exactly: all \(4^8\) syndrome histories
are retained, with no sampling, no pruning, and no branch merging.

**The stabilizer group is the slot partition.** This is not an analogy. For the
[[3,1]] repetition memory the syndrome map resolves \(\log_24=2\) bits against
a \(\log_28=3\)-bit error space, so Corollary 4.2's ceiling is
\((n-k)/n=2/3\) asymptotically, and the missing third is the logical label the
code is *designed* to be blind to. Over a finite window the correct ceiling is
\(2/(J_0-J_\infty)\), which is reported alongside \(\chi\).

**Results** (uniform decoder; windows of 8 rounds inside the 96-round default
trace):

| Window start | \(\gamma\) | \(\sigma\) | \(\delta\) | \(\chi\) | window ceiling | \(\chi_G\) | \(I(L_0;R\mid G_0)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.00195 | 1.92876 | 0.07319 | 0.963442 | 0.99903 | 0.96438 | 0 |
| 44 | 2.29867 | 1.52677 | 0.77189 | 0.664199 | 0.87007 | 0.76339 | 0 |
| 52 | 2.39818 | 1.34780 | 1.05038 | 0.562009 | 0.83396 | 0.67390 | 0 |
| 60 | 2.28404 | 1.37541 | 0.90863 | 0.602184 | 0.87564 | 0.68771 | 0 |
| 72 | 2.04528 | 1.70805 | 0.33723 | 0.835116 | 0.97786 | 0.85402 | 0 |
| 88 | 2.00277 | 1.92233 | 0.08045 | 0.959833 | 0.99862 | 0.96117 | 0 |

Validation across all thirty protocol-window pairs: the ledger identity holds
to `0.000e+00`, \(\sigma\leq\gamma\) is never violated, \(\sigma\leq
H(R_{k+1}\mid R_{\leq k})\) is never violated, and there are zero
bandwidth-limited steps.

Six findings.

**1. \(\chi\) is a property of the extraction circuit, not of the decoder.**
Across the five decoder policies the spread in \(\chi\) is `0.00479` at
window 0 and `0.00215` at window 52. Across windows of the same trace it is
`0.401`. Holding the data-qubit noise fixed and scaling only the
ancilla/readout fault rates moves it by `0.142` at window 44 (`0.70558` at
quarter rates, `0.56349` at quadruple rates). The decoder cannot raise the
sorting efficiency; it can only spend what was already sorted. This is a
concrete hardware directive and it sits well with the H2 headline that adaptive
decoding buys only marginal logical-error improvement: the bottleneck is
upstream of the thing being adapted.

**2. Adaptation overhead is a measurable charge against \(\chi\).**
`overactive_decoder` recalibrates every round and pays for it in sorting
efficiency: `0.95939` against `0.96418` at window 0, and `0.95486` against
`0.96100` at window 88. Small, consistently signed, and in the predicted
direction — characterization faults are contraction that produces no record.

**3. The H2 sorter is perfectly selective.** \(I(L_0;R\mid G_0)=0\) exactly, in
every window and for every policy. The parity checks resolve the error sector
and are exactly degenerate on the logical label, which is Knill-Laflamme
holding numerically rather than by assertion. In the vocabulary of Section 8,
the scaffold is nothing like `centralizing_sorter`; the only open question
about it was ever efficiency.

**4. What stays inside is exactly the protected label.** After eight rounds the
retained column equals the protected column to five decimals — `0.99805` and
`0.99805` at window 0, `0.60182` and `0.60182` at window 52. The sector column
has been fully drained to the boundary and the logical component is all that
remains in the register. Real syndrome extraction exhibits the
`sort_then_contract` structure of Section 12 without being designed to.

**5. Bandwidth is not the binding constraint here; noise is.** Peak
\(\gamma_k/C_k\) runs `0.876` to `0.951` across windows and never exceeds 1, so
Theorem 4's alphabet bound is close but never active. The tighter bound is the
informative one: \(\sigma_k\) falls short of the realized record entropy
\(H(R_{k+1}\mid R_{\leq k})\) by up to `0.278` bits at window 0 and `0.740`
bits at window 52. The syndrome register carries roughly two bits per
extraction round, of which up to three quarters of a bit is readout noise
rather than error information. That gap is the sorter misfiling coins, and it
is where the losses live.

**6. Drift costs sorting efficiency, not just decoder accuracy.** \(\chi\)
tracks the trace's noise schedule, falling from `0.963` in the clean early
window to `0.562` at the drift peak near round 52, where \(\chi_G=0.674\)
against a ceiling of 1 — a third of the error-sector information never reaches
the decoder at all. The adaptive-alignment program has so far measured drift's
effect on the decoder's estimate; this says drift also degrades the record
channel that the estimate is computed from.

**Caveats.** The eight-round window is forced by exact enumeration of \(4^8\)
histories; longer windows would need pruning and are not reported. The probe is
an injected uniform error, not the memory's stationary state, so \(\chi\) here
answers "how much of a fresh unknown error gets sorted" rather than "what is
the steady-state efficiency of the memory." And the [[3,1]] repetition scaffold
remains, as the existing H2 Pauli-frame audit already records, a diagnostic
rung rather than a full logical-qubit memory.

## 14. Coherent-Information Restatement

Sections 3-7 use a classical reference and a classical record, and call the
residual column *destroyed*. That word is an artifact of the classical setting.
Quantum mechanically the global evolution is an isometry, nothing is destroyed,
and the ledger becomes a conservation law rather than a chain of inequalities.

**Setup.** Let \(R\) be a reference system, initially maximally entangled with
the interior \(A_0\). Let each step act by a Stinespring isometry

$$
V_k:\ A_k\ \longrightarrow\ A_{k+1}\otimes B_{k+1}\otimes E_{k+1},
$$

where \(B\) accumulates the boundary record and \(E\) accumulates the
unrecorded environment. The global state on \(RABE\) stays pure. Define the
columns exactly as before, now with quantum mutual information:

$$
T_k=I(R;A_kB_{\leq k}),
\qquad
E_k=I(R;B_{\leq k}),
\qquad
J_k=I(R;A_k\mid B_{\leq k}),
$$

and additionally the leakage column

$$
L_k=I(R;E_{\leq k}).
$$

**Theorem 1-Q.** Theorem 1 holds verbatim. \(T_k=J_k+E_k\) is the quantum chain
rule for mutual information, an identity for von Neumann entropies.
\(\delta_k\geq0\) is the data processing inequality for quantum channels.
\(\sigma_k\geq0\) is monotonicity under partial trace. And \(J_k\geq 0\), which
was trivial classically, is now exactly **strong subadditivity**.

**The two languages are the same ledger.** For a purification,

$$
I_c(R\rangle X)=I(R;X)-H(R),
$$

and \(H(R)\) is constant in \(k\). The increments therefore do not care which
language is used:

$$
\gamma_k,\ \sigma_k,\ \delta_k,\ \chi
\quad\text{are identical whether computed from } I \text{ or from } I_c .
$$

Only the absolute columns shift, and the identity survives the shift as
\(T^c_k=E^c_k+J_k\), with \(J\) unshifted because it is a *conditional* mutual
information. Sorting efficiency was already a coherent-information quantity;
the classical presentation merely hid it.

**Theorem 6 (three-way conservation).** For the pure global state,

$$
\boxed{\ I(R;B_{\leq k})+I(R;A_k\mid B_{\leq k})+I(R;E_{\leq k})=2H(R)\ }
$$

at every step, and consequently

$$
\delta_k=L_{k+1}-L_k .
$$

**Proof.** For pure \(RABE\), \(H(AB)=H(RE)\) and \(H(RAB)=H(E)\), so
\(I(R;AB)=H(R)+H(RE)-H(E)\) and \(I(R;E)=H(R)+H(E)-H(RE)\); adding gives
\(I(R;AB)+I(R;E)=2H(R)\). Apply the chain rule
\(I(R;AB)=I(R;B)+I(R;A\mid B)\). The increment statement follows by
differencing, since \(T_k=2H(R)-L_k\). \(\square\)

This is the sharpest form of the whole framework. The classical ledger had two
columns and a leak to nowhere; the quantum ledger has three columns and no
leak. Contraction is a **routing decision**: every bit leaving the interior
arrives either in the boundary record or in the environment, and

$$
\gamma_k
=
\underbrace{\sigma_k}_{\text{filed in a slot}}
+
\underbrace{\delta_k}_{\text{on the floor}} .
$$

"Destruction" in Sections 3-7 is not annihilation. It is leakage to a party
whose records nobody reads. Whether that distinction matters operationally
depends entirely on whether \(E\) is ever recoverable — which is precisely the
black-hole information question, now stated as a bookkeeping question about
which column the contraction was routed into.

Two immediate consequences.

**Corollary 6.1 (the budget doubles).** \(J_0=I(R;A_0)=2H(R)\), twice the
classical maximum. The extra \(H(R)\) is the coherence of the interior with its
reference. A quantum interior carries twice the distinguishability budget of a
classical one of the same dimension, and the second half exists only as
correlation.

**Corollary 6.2 (the sorter and the floor compete).** Because the three columns
sum to a constant, any increase in \(I(R;B)\) is exactly an decrease in
\(I(R;A\mid B)+I(R;E)\). Making the record more informative necessarily makes
the environment less so. Monogamy is not an extra principle here; it is the
conservation law read sideways.

**Theorem 7 (classical-record cap).** If the boundary record is classical —
that is, if \(B\) is decohered, so that \(\rho_{RB}=\sum_b p_b\,\rho_R^b\otimes
|b\rangle\langle b|\) — then

$$
I(R;B_{\leq k})=H(R)-\sum_b p_b H(\rho_R^b)\leq H(R),
$$

so a fully drained interior gives

$$
\chi\leq\tfrac12 .
$$

Equivalently, in coherent-information form, a classical record satisfies
\(I_c(R\rangle B)\leq 0\): it sits at or below the threshold beneath which no
quantum information is recoverable at all.

**Proof.** For a cq state, \(H(RB)=H(\{p_b\})+\sum_bp_bH(\rho^b_R)\) and
\(H(B)=H(\{p_b\})\), so \(I(R;B)=H(R)-\sum_bp_bH(\rho_R^b)\), which is the
Holevo quantity and is bounded by \(H(R)\). With \(J_0-J_\infty=2H(R)\),
\(\chi=\sigma_{\mathrm{tot}}/\gamma_{\mathrm{tot}}\leq H(R)/2H(R)\).
\(\square\)

This is Corollary 4.2's resolution ceiling reappearing in quantum form.
Classicality of the record *is* a slot-resolution limit: a machine that files
coins by reading a classical label can capture at most half of what a quantum
interior distinguishes, no matter how many slots it has or how fast it runs.

**Theorem 3-Q (lossless rule as decoupling).** \(\delta_k=0\) if and only if
\(L_{k+1}=L_k\), i.e. the environment learns nothing new about the reference.
This is the decoupling condition, and it is equivalent to correctability: there
exists a recovery channel on \(A_{k+1}B_{\leq k+1}\) restoring the reference
correlations, which in Kraus form is the Knill-Laflamme condition
\(PE_a^\dagger E_bP=c_{ab}P\) for the discarded part. Section 5's "never merge
a distinction you have not already exported" becomes **never let the
environment learn something the record has not already learned**, which is the
same rule stated from the other side of the ledger.

**Theorem 4-Q (quantum bandwidth).** \(\sigma_k=I(R;B_{k+1}\mid B_{\leq k})
\leq 2\log_2 d_{B_{k+1}}\), so \(\delta_k\geq\gamma_k-2\log_2 d_{B_{k+1}}\).
The factor of two relative to the classical alphabet bound is the same factor
of two as in Corollary 6.1 and Theorem 7, and coherent transfer of one record
qubit saturates it exactly.

### Consequence for the derivation program

Stage 7 of `bridges/quantum_gravity_derivation_program.md` currently treats
holographic QEC as *evidence* for the structure ACP expects. Theorem 7 upgrades
that. If an admissible completion must achieve \(\chi\to1\) — which it must,
because \(\delta>0\) is exactly information routed to a party the exterior
cannot read — then the boundary record channel **cannot be classical**. A
horizon that emits only decohered outcomes caps sorting at one half and
necessarily strands half the interior budget in the environment. The boundary
channel has to carry quantum correlation with the interior, which is the
code-like structure Stage 7 was arguing toward. ⚠ The step from "the record
must be quantum" to "the boundary theory is a specific holographic code"
remains unbridged; what is now forced is only the classicality exclusion.

### Simulation

`simulations/crystallization_sorting_engine/quantum_sorting_ledger.py`
propagates the exact pure state on \(RABE\) — two reference qubits maximally
entangled with a two-qubit interior, plus one record and one environment qubit
per step, sixteen qubits total — and computes every von Neumann entropy from
the state vector. Budget \(2H(R)=4\) bits.

| Policy | \(\gamma\) | \(\sigma\) | \(\delta\) | \(\chi\) | \(I(R;B)\) | \(I(R;E)\) | \(I_c(R\rangle B)\) | early protected |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| coherent_sort | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 2.0000 |
| classical_sort | 4.0000 | 2.0000 | 2.0000 | 0.50000 | 2.0000 | 2.0000 | 0.0000 | 1.0000 |
| leaky_sort | 4.0000 | 2.7982 | 1.2018 | 0.69956 | 2.7982 | 1.2018 | +0.7982 | 1.3991 |
| crush | 4.0000 | 0.0000 | 4.0000 | 0.00000 | 0.0000 | 4.0000 | −2.0000 | 0.0000 |
| sector_then_protected | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 0.0000 |
| centralizing_sort | 4.0000 | 4.0000 | 0.0000 | 1.00000 | 4.0000 | 0.0000 | +2.0000 | 2.0000 |

Validation, all six policies, all steps: the conservation law of Theorem 6
holds to `0.000e+00`; the backlog never goes negative, so strong subadditivity
is saturated but never violated; \(\sigma\leq\gamma\) and
\(\sigma\leq2\log_2d_B\) are never violated; and
\(|\delta_k-(L_{k+1}-L_k)|=\) `0.000e+00`, confirming that destruction is
leakage exactly and not merely in bound.

`classical_sort` lands on \(\chi=0.5\) and \(I_c(R\rangle B)=0.0000\)
simultaneously, which is Theorem 7 with both of its equivalent statements
visible at once. `crush` reaches \(I_c=-2.0000=-H(R)\), the floor.

The dephasing scan turns the classicality of the record into a continuous knob.
Sweeping the record-environment coupling angle \(\theta\) from 0 to \(\pi\)
moves \(\chi\) from `1.000000` to `0.500000` along

$$
\chi(\theta)=1-\tfrac12 h_2\!\left(\tfrac{1+\cos(\theta/2)}{2}\right),
$$

and the simulated values match that closed form to `0.00e+00` at all thirteen
sample points. There is no sharp classical/quantum transition in sorting
efficiency: partial decoherence of the record costs partial efficiency, and the
classical limit is the endpoint of a smooth curve rather than a different
regime.

## 15. What This Does Not Claim

This note does not prove that gravitational focusing merges relational
macrocells at the rate assumed in Section 10, does not derive the boundary
capacity from a gravitational theory, does not derive the Page curve, and does
not exhibit a microscopic throttle mechanism. It does not claim that black
holes are literally coin sorters, and it does not claim the toy simulation is a
gravitational calculation.

What it does claim is that the sorting reading of collapse is not a metaphor
awaiting formalization. It is a ledger identity plus two capacity bounds, and
the ACP admissibility condition has an exact expression in those terms:

$$
\chi\approx1
\quad\text{with}\quad
\gamma_k\leq C_k
\quad\text{and}\quad
I(L;R^{\mathrm{early}}\mid G)\leq\epsilon_L .
$$

## 16. Next Targets

1. Compute \(\gamma_k\) for the macrocell kernel of
   `simulations/cosmic_coordination_floor/` and compare it against an
   area-derived \(C_k\), turning Conjecture SE-1 into a number inside the
   existing collapse toy.
2. *(Done — Section 14.)* The remaining quantum work is approximate rather
   than exact: replace the sharp decoupling condition of Theorem 3-Q with an
   \(\epsilon\)-approximate version and carry the error through Theorem 5, so
   the trigger-time bound survives when the completion is only approximately
   correctable.
3. *(Done — Section 13.)* Extend the H2 audit beyond the eight-round exact
   window to a steady-state per-cycle \(\chi\), and to a phase-protecting
   stabilizer or subsystem code where the sector/protected split is not just
   the repetition code's coset structure.
4. Test finding 1 of Section 13 — that \(\chi\) is set by the extraction
   circuit rather than the decoder — on a code where the decoder can change the
   *slot partition* rather than only the likelihoods. Corollary 4.2 predicts
   that gauge or check-schedule adaptation should move \(\chi\) where
   likelihood adaptation cannot.
5. Score the candidate completions of
   `bridges/relational_observable_macrostate_kernel.md` §10 by which of the
   three strategies of Section 7 they use.
6. Test whether Corollary 5.1's throttle requirement can be strengthened into a
   bound on the effective stress-energy correction needed near the completion
   scale.
