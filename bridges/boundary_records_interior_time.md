# Boundary Records and Interior Time

*Status: bridge note lifting a proved finite result into the quantum-gravity
derivation program. The instrument-level propositions cited here are proved
in `bridges/clock_syndrome_record_splitting.md`; every gravitational
statement is a conjectural lift and is marked as such.*

## Abstract

Stage 6 of the derivation program requires boundary records that constrain
geometry without prematurely leaking the protected interior microstate:

$$
I(\mathrm{geometry\ sector};R_{\partial})>0,
\qquad
I(\mathrm{interior\ microstate};R_{\partial}^{\mathrm{early}})\approx0 .
$$

The clock-syndrome record-splitting results turn the second condition into
a censorship statement about *time*:

> boundary records transparent enough to protect the interior are provably
> blind to every interior relational clock. Whatever tempo the early
> boundary channel carries is geometry-sector tempo, not interior proper
> time; interior time becomes boundary-readable exactly when interior
> information does — at the decoding scale, not before.

This makes the record-splitting structure of Stage 6 forced rather than
stylistic, and it gives the OP-22 question — how boundary records become
time — a sharp negative half: they do not become *interior* time early, on
pain of violating the protection condition that makes the channel
admissible.

## 1. The finite results being lifted

For an exact protected sector with algebra \(\mathcal A_L\) and a clock
family generated inside \(\mathcal A_L\)
(`bridges/clock_syndrome_record_splitting.md`):

- **Proposition 1.** Instruments whose Kraus operators commute with
  \(\mathcal A_L\) on the protected sector produce records exactly
  independent of the clock phase, for arbitrary adaptive schedules.
- **Proposition 5.** \(\epsilon\)-transparent instruments produce records
  with \(I(\Theta;R)\le2\tau\log_2|\mathcal R|+h_2(2\tau)\),
  \(\tau=\sum_i(\epsilon_i+\epsilon_i^2/2)\).
- **Proposition 6.** The sharp criterion is algebraic: blindness for all
  schedules iff every code-compressed record POVM commutes with the clock
  rotation, with the filtered defect \(\zeta_n\) controlling total
  variation and the observed accumulation growing like \(\sqrt n\).
- **Lemma 3.** Reading a protected clock with total Fisher information
  \(J\) costs at least a factor \(e^{-J/2}\) of the conjugate protected
  coherence in the gentle limit.

## 2. The gravitational dictionary

| Finite object | Gravitational lift (conjectural) |
|---|---|
| code sector \(\mathcal C\) | protected interior microstate sector |
| logical algebra \(\mathcal A_L\) | interior relational observable algebra |
| stabilizer/syndrome records | early boundary records \(R_{\partial}^{\mathrm{early}}\) (null records, quasinormal spectra, exterior multipoles) |
| logical clock \(U_\theta=e^{-i\theta\bar G/2}\) | interior relational clock (proper-time-like observable of the protected interior) |
| transparency \([M,\mathcal A_L]P=0\) | interior privacy \(I(\mathrm{interior};R_{\partial}^{\mathrm{early}})\approx0\) |
| central clock channel | geometry-sector records with \(I(G_\ell;R_{\partial})>0\) |
| decoding scale (Stage 5 late decodability) | Page-time-like transition where interior information becomes boundary-recoverable |

⚠ The dictionary's left column is proved; the right column inherits the
theorems only insofar as the gravitational channel really is an instrument
family acting on a protected sector — which is precisely what Stages 4-7
posit but have not derived. There is also a real gap flagged here rather
than hidden: Stage 6's privacy condition is stated as small mutual
information, while the finite propositions assume small *commutators*;
Proposition 6 narrows this gap (the operative object is the compressed
record POVM, not the apparatus), but an information-to-algebra converse
for approximate sectors is exactly OP-30(a)'s remaining half.

## 3. Corollary G1 (conjectural lift): interior clock censorship

If the early boundary channel of an admissible gravitational mechanism is
implemented by instruments (\(\epsilon\)-)transparent with respect to the
protected interior algebra, then for any interior relational clock
observable:

$$
I(\Theta_{\mathrm{int}};R_{\partial}^{\mathrm{early}})
\ \le\ f(\epsilon)
\ \xrightarrow[\epsilon\to0]{}\ 0 ,
$$

with \(f\) as in Propositions 5-6. Early boundary records can carry
arbitrary amounts of *geometry-sector* tempo — ringdown frequencies,
horizon-area growth, null-record structure — while carrying essentially
none of the interior's own clock. In ACP operational-time language
(OP-29): the exterior can measure the geometry channel's operational tempo
\(\nu_{\mathrm{geom}}\), but the interior's proper productive interval is
not a boundary observable before decoding.

This is an ACP-native, mechanism-independent statement of a familiar
intuition — the exterior "does not see the interior clock" — but derived
from the admissibility condition itself rather than from any particular
horizon geometry: any mechanism satisfying Stage 6 privacy *must* exhibit
interior clock censorship, whether it is a horizon, a fuzzball, a bounce,
or an island prescription.

## 4. Corollary G2 (conjectural lift): time release equals information release

Stage 5 requires late decodability: redistributed coordination must become
boundary-recoverable within finite \(T_{\mathrm{dec}}\). By Proposition 6's
dichotomy, a channel becomes able to carry interior clock information
exactly when its compressed record elements stop commuting with the
interior algebra — i.e., exactly when it becomes an interior-information
channel. Therefore, within this framework:

> the transition at which the boundary can first read interior time and
> the transition at which it can first read interior information are the
> same transition.

There is no admissible regime in which the exterior learns the interior's
clock but not its state, or the state but not its clock; centrality is one
property, not two. In Page-curve language, interior proper time is a
post-Page observable. ⚠ Conjectural at the gravitational level; at the
finite level it is Proposition 6.1 read twice.

## 5. Consequences for the derivation ladder

1. **Stage 6 gains a forced substructure.** The admissible gravitational
   record channel is not merely "informative about geometry, quiet about
   the interior" — it is *split* in the Proposition-6 sense: a
   geometry-central channel (carrying exterior-usable tempo and
   coordination, Stage 5) and an interior-transparent channel, with no
   single channel able to serve both roles before decoding. The
   braided-clock ladder (Experiments A-G) is the finite laboratory where
   this split is exhibited end to end.
2. **Dark constraints are geometry-central records.** OP-17's null records
   \(R_0\) constrain geometry/path histories, \(I(G;R_0)>0\); the present
   note classifies them as the central channel, and predicts they are
   interior-blind — a checkable property of the mirror-room and
   wave-interference toys if an "interior" register is added to them.
3. **A falsifiable-in-the-toy prediction — now tested.** The interior
   clock register is implemented in
   `simulations/cosmic_coordination_floor/`: the interior microstate is a
   phase \(\theta\in\mathbb Z_8\) with uniform prior, advancing one bin
   per step, and the per-step diagnostic \(I(\Theta;R_{\partial})\) is
   computed on the joint distribution. The results match G1/G2 exactly:
   every admissible policy holds \(I(\Theta;R_{\partial})=0.000\) bits for
   the whole run while carrying `1.5`-`2.1` bits of geometry-record
   information; the clock first becomes boundary-readable through the
   late decodable channel at the transfer step (step 6 for the quantum
   completion, step 7 for horizon transfer), as the phase frozen at
   absorption. A deliberately inadmissible `leaky_completion` control that
   writes clock parity into its transfer record shows `0.210` bits of
   clock-record information with onset at exactly its trigger step and is
   flagged by the privacy audit — the censorship diagnostic has teeth.
   The toy also separates the two failure routes: naked collapse leaks
   the interior through lost singular mass with zero record-channel clock
   information, while the leaky channel leaks through the record itself.

## 6. What this does not claim

- No claim that horizons, islands, or any specific mechanism realize the
  instrument structure; only that *if* Stage 6 privacy holds
  instrument-wise, clock censorship follows.
- No claim about experienced interior time; every statement is about
  boundary-accessible information.
- No claim of novelty for the underlying complementarity intuition; the
  contribution is deriving it from the ACP admissibility condition via
  proved finite propositions, so that it holds for every admissible
  completion mechanism uniformly.

## 7. Pointers

`bridges/clock_syndrome_record_splitting.md` (Propositions 1, 5, 6, Lemma
3); `bridges/quantum_gravity_derivation_program.md` (Stages 5-7);
`bridges/quantum_braiding_timekeeping.md` §12-14;
`bridges/operational_time_relativity.md` §6;
`bridges/dark_constraint_quantum_gravity.md`;
`simulations/quantum_braiding_clock/`;
`simulations/cosmic_coordination_floor/`. Open problems: OP-17, OP-19,
OP-20, OP-22, OP-29, OP-30.
