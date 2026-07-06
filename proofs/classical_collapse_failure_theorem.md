# Classical Collapse Failure Theorem

*Status: proven at the finite relational-kernel level. The focusing assumptions
F1–F4 are stated as explicit hypotheses; their semiclassical justification is
physical, standard, and clearly flagged, but they are not yet derived from an
explicit general-relativistic pushforward. That derivation is the residual open
content of OP-19.*

Companion documents:

- `bridges/relational_observable_macrostate_kernel.md` (defines the kernel and
  contained the predecessor Proposition 2, which this theorem strengthens)
- `bridges/quantum_gravity_derivation_program.md` (Stage 2 of the derivation
  ladder, which this theorem discharges at the finite-kernel level)
- `bridges/singularity_inadmissibility.md` (the admissibility criterion used in
  case (a))
- `bridges/cosmic_coordination_floor.md` (the floor being breached in case (b))
- `simulations/cosmic_coordination_floor/` (finite instantiation of every
  quantity appearing below)

## 1. Purpose

Stage 2 of the quantum-gravity derivation program requires the following
theorem:

> For a finite-resolution relational collapse macrostate satisfying the
> classical focusing assumptions, the classical transition kernel either
> becomes undefined on admissible future macrostates or violates the positive
> future-entropy floor.

The previous formal object at this rung was Proposition 2 of
`bridges/relational_observable_macrostate_kernel.md`: qualitative, proved only
in sketch, and without quantitative content. This document replaces it with a
theorem that is:

1. **exhaustive** — every classical continuation lands in normalization
   failure, sub-floor crystallization, or mechanism change;
2. **quantitative** — the failure times carry explicit bounds in the drift,
   defect, and concentration parameters;
3. **record-aware** — the failure is shown to be record-free: the classical
   description cannot pay the coordination debt through its boundary channel,
   which is what forces the completion to be *decodable* rather than merely
   regular.

Everything in Sections 2–6 is exact finite mathematics. Section 7 states the
physical case that semiclassical gravitational collapse satisfies the
hypotheses; that case is standard but is *motivation*, not proof, and is
labeled accordingly.

## 2. Setting: Finite Relational Collapse Chain

Fix a resolution scale \(\ell\) and a verification interval \(\Delta\). Let
\(\mathcal M_\ell\) be the finite set of admissible relational macrocells of
`bridges/relational_observable_macrostate_kernel.md`, with the schematic split

$$
m=(G_\ell,B_\ell,L_\ell)
$$

into geometry sector, boundary-record sector, and unresolved protected interior
sector. Let

$$
c:\mathcal M_\ell\to\{c_0<c_1<\cdots<c_K\}\subset[0,1)
$$

be the binned relational compactness observable (areal-radius compactness
\(C_R=2GM_R/R_{\mathrm{areal}}\) in the minimal collapse macrocell).

**Definition 1 (classical collapse description).** A *classical collapse
description* at scale \((\ell,\Delta)\) is a sub-stochastic kernel

$$
K(m'|m)\geq 0,
\qquad
\sum_{m'\in\mathcal M_\ell}K(m'|m)=1-q(m),
\qquad
q(m)\in[0,1],
$$

where \(q(m)\) is the *singular defect*: the probability mass carried in one
verification step from cell \(m\) into inadmissible singular support
(geodesically incomplete, divergent, or otherwise outside
\(\mathcal S_{\mathrm{adm}}\)). This is exactly the object
\(K^{\mathrm{cl}}_{\ell,\Delta}\) of the kernel bridge, with
\(q(m)=1-Z^{\mathrm{adm}}_{\ell,\Delta}(m)\).

**Definition 2 (collapse basin and top band).** Fix thresholds
\(c_\dagger<c_{\mathrm{top}}\leq c_K\). The *collapse basin* is
\(\mathcal B=\{m:c(m)\geq c_\dagger\}\) (the trapped band) and the *top band*
is \(\mathcal T=\{m:c(m)\geq c_{\mathrm{top}}\}\) (the deeply collapsed band).

**Definition 3 (diagnostics).** For \(q(m)<1\), the conditional future entropy
of cell \(m\) is the entropy of the normalized forward law,

$$
H_{\ell,\Delta}(m)
=
-\sum_{m'}\hat K(m'|m)\log_2 \hat K(m'|m),
\qquad
\hat K(m'|m)=\frac{K(m'|m)}{1-q(m)} .
$$

For an initial admissible distribution \(\mu_0\) on \(\mathcal B\), the
*admissible mass* at step \(t\) is \(Z_t=\mu_t(\mathcal M_\ell)\) where
\(\mu_{t+1}=\mu_t K\). The *conditioned chain* \((m_t)\) is the Markov chain
with kernel \(\hat K\), i.e., the surviving histories reweighted on admissible
continuation.

## 3. Focusing Assumptions

The theorem consumes four hypotheses about \((K,\mathcal B)\). Each is stated
exactly here and physically justified in Section 7.

**F1 (focusing drift and band monotonicity).** There exists \(\delta>0\) such
that:

1. *(drift)* for every \(m\in\mathcal B\setminus\mathcal T\) with \(q(m)<1\),

$$
\mathbb E_{\hat K}\!\left[c(m')\,\middle|\,m\right]
\geq
c(m)+\delta ;
$$

2. *(monotonicity)* for every \(m\in\mathcal B\), \(K(m'|m)=0\) whenever
   \(c(m')<c_\dagger\); and for every \(m\in\mathcal T\), \(K(m'|m)=0\)
   whenever \(c(m')<c_{\mathrm{top}}\).

So the trapped band and the top band are absorbing for admissible
continuations, and compactness rises on average by at least \(\delta\) per step
until the top band is reached.

**F2 (semiclassical concentration).** There exist \(\varepsilon_{\mathrm{tail}}
\in[0,\tfrac12]\) and \(N_{\mathrm{top}}\in\mathbb N\) such that for every
\(m\in\mathcal T\) with \(q(m)<1\) there is a set
\(S(m)\subseteq\mathcal M_\ell\) with \(|S(m)|\leq N_{\mathrm{top}}\) and

$$
\sum_{m'\in S(m)}\hat K(m'|m)\geq 1-\varepsilon_{\mathrm{tail}} .
$$

Define the *terminal entropy scale*

$$
H_{\mathrm{top}}
=
H_2(\varepsilon_{\mathrm{tail}})
+\log_2 N_{\mathrm{top}}
+\varepsilon_{\mathrm{tail}}\log_2|\mathcal M_\ell| ,
$$

with \(H_2\) the binary entropy. The *deterministic-freeze idealization* is
\(\varepsilon_{\mathrm{tail}}=0\), \(N_{\mathrm{top}}=1\), giving
\(H_{\mathrm{top}}=0\).

**F3 (record rigidity / classical censorship).** On \(\mathcal B\), the
boundary-record sector is a fixed function of the geometry sector under \(K\):
\(B_\ell(m')=r(G_\ell(m'))\) for \(K\)-almost-all transitions. Moreover the
classical description supplies no channel from the unresolved interior sector
to the boundary record:

$$
I\!\left(L_\ell;B_\ell^{[t,\infty)}\right)=0 .
$$

No new record variables appear, and darkness behind the trapped band is not
decodable.

**F4 (mechanism rigidity).** The kernel \(K\) is a single fixed function of the
macrocell; there is no compactness-triggered change of transition mechanism, no
added variables, and no state-dependent switch of dynamical law.

Finally, the case split that drives the theorem:

**Definition 4 (defect regime).** The description is *leaking at* \(m\) if
\(q(m)>0\) and *conservative at* \(m\) if \(q(m)=0\). Because \(\mathcal T\) is
finite, if every \(m\in\mathcal T\) is leaking then
\(q_0=\min_{m\in\mathcal T}q(m)>0\).

## 4. Lemmas

**Lemma 1 (finite entry time).** Under F1, for the conditioned chain started at
any \(m_0\in\mathcal B\), the top-band entry time
\(\tau=\inf\{t:m_t\in\mathcal T\}\) satisfies

$$
\mathbb E[\tau]
\leq
\frac{c_K-c(m_0)}{\delta}
\leq
\frac{c_K-c_\dagger}{\delta}
=:\bar T .
$$

In particular \(\tau<\infty\) almost surely, and by Markov's inequality
\(\mathbb P(\tau>t)\leq \bar T/t\).

**Proof.** Let \(c_t=c(m_{t\wedge\tau})\). By F1.1,
\(\mathbb E[c_{t+1}\mid\mathcal F_t]\geq c_t+\delta\) on \(\{t<\tau\}\), and
\(c_{t+1}=c_t\) on \(\{t\geq\tau\}\), so
\(X_t=c_t-\delta(t\wedge\tau)\) is a submartingale. Taking expectations,

$$
c_K\;\geq\;\mathbb E[c_t]\;\geq\;c(m_0)+\delta\,\mathbb E[t\wedge\tau] ,
$$

so \(\mathbb E[t\wedge\tau]\leq (c_K-c(m_0))/\delta\) for every \(t\). Monotone
convergence gives \(\mathbb E[\tau]\leq(c_K-c(m_0))/\delta<\infty\).
\(\square\)

**Lemma 2 (geometric normalization failure).** Suppose F1 holds and every
\(m\in\mathcal T\) is leaking, with \(q_0=\min_{\mathcal T}q>0\). Then for
every \(0<s\leq t\),

$$
Z_t
\leq
\mathbb P(\tau>s)
+
(1-q_0)^{\,t-s}
\leq
\frac{\bar T}{s}+(1-q_0)^{\,t-s},
$$

and in particular \(Z_t\to 0\). For any \(\epsilon\in(0,1)\), the admissible
mass satisfies \(Z_t\leq\epsilon\) for all

$$
t\;\geq\;
t^*(\epsilon)
=
\frac{2\bar T}{\epsilon}
+
\frac{\log(\epsilon/2)}{\log(1-q_0)} .
$$

**Proof.** Every path weight under the defective kernel is dominated by its
weight under the conditioned kernel, since
\(K(m'|m)=(1-q(m))\hat K(m'|m)\leq\hat K(m'|m)\) factor by factor; hence the
defective path measure \(\mu\) of any path event is at most its conditioned
probability \(\mathbb P\). Decompose surviving mass at time \(t\) by whether
the history entered \(\mathcal T\) by time \(s\). Histories with \(\tau>s\)
contribute at most \(\mu(\tau>s)\leq\mathbb P(\tau>s)\). Histories with
\(\tau=u\leq s\) remain in \(\mathcal T\) for all later steps by F1.2, and each
step taken from \(\mathcal T\) multiplies their defective weight by at most
\(1-q_0\); since their conditioned measure totals at most 1, they contribute
at most \((1-q_0)^{t-u}\leq(1-q_0)^{t-s}\). Sum the two terms and apply
Lemma 1's tail bound. For the last claim take \(s=2\bar T/\epsilon\), so the
first term is \(\leq\epsilon/2\); for
\(t-s\geq\log(\epsilon/2)/\log(1-q_0)\) the second term is also
\(\leq\epsilon/2\). \(\square\)

**Lemma 3 (entropy ceiling in the top band).** Under F2, every conservative
\(m\in\mathcal T\) satisfies

$$
H_{\ell,\Delta}(m)\leq H_{\mathrm{top}} .
$$

**Proof.** Let \(\alpha=\hat K(S(m)^c|m)\leq\varepsilon_{\mathrm{tail}}
\leq\tfrac12\). The grouping bound gives

$$
H_{\ell,\Delta}(m)
\leq
H_2(\alpha)+(1-\alpha)\log_2|S(m)|+\alpha\log_2|\mathcal M_\ell| .
$$

Since \(H_2\) is nondecreasing on \([0,\tfrac12]\),
\(H_2(\alpha)\leq H_2(\varepsilon_{\mathrm{tail}})\); the middle term is at
most \(\log_2 N_{\mathrm{top}}\); the last is at most
\(\varepsilon_{\mathrm{tail}}\log_2|\mathcal M_\ell|\). \(\square\)

## 5. The Theorem

**Theorem 1 (classical collapse trichotomy).** Let \(K\) be a classical
collapse description satisfying F1–F4, started in the collapse basin
\(\mathcal B\) with admissible mass 1, and let
\(H_{\mathrm{floor}}>H_{\mathrm{top}}\) be any coordination floor. Then for
every \(\varepsilon\in(0,1)\) there is an explicit time

$$
T^*(\varepsilon)\leq\frac{\bar T}{\varepsilon}
=\frac{c_K-c_\dagger}{\delta\,\varepsilon}
$$

such that for all \(t\geq T^*(\varepsilon)\), with probability at least
\(1-\varepsilon\) over admissible continuations, the occupied cell
\(m_t\) lies in \(\mathcal T\) and satisfies **at least one** of:

**(a) normalization failure.** \(q(m_t)>0\): the forward channel from the
occupied cell is strictly sub-stochastic, so the description violates the
normalizable-record-channel condition of
`bridges/singularity_inadmissibility.md` §2 and is inadmissible on its original
state space;

**(b) sub-floor crystallization.** \(q(m_t)=0\) and

$$
H_{\ell,\Delta}(m_t)\leq H_{\mathrm{top}}<H_{\mathrm{floor}} :
$$

the forward channel from the occupied cell has crystallized below the floor;
in the deterministic-freeze idealization it sits at the CDT crystallization
boundary \(H(m'|m)=0\).

Moreover, by F3, neither outcome is accompanied by a decodable boundary record
of the lost or frozen coordination: in case (a) the defect mass leaves no
admissible record, and in case (b) the boundary record \(B_\ell=r(G_\ell)\)
freezes together with the geometry sector, while
\(I(L_\ell;B_\ell^{[t,\infty)})=0\) throughout.

Consequently the only continuations of gravitational collapse that remain
admissible with \(H_{\ell,\Delta}\geq H_{\mathrm{floor}}\) are those that
violate at least one of F1–F4 before \(T^*\) — that is, mechanism changes.

**Proof.** By Lemma 1 and Markov's inequality,
\(\mathbb P(\tau>T^*)\leq\bar T/T^*\leq\varepsilon\), so with probability at
least \(1-\varepsilon\) the conditioned chain has entered \(\mathcal T\) by
\(T^*\), and by F1.2 it remains there for all later \(t\). Fix such a history
and \(t\geq T^*\). The occupied cell \(m_t\in\mathcal T\) has either
\(q(m_t)>0\), which is case (a) — sub-stochasticity is immediate from
Definition 1, and inadmissibility follows because the record/evolution law
fails to be a probability law on the retained state space — or \(q(m_t)=0\),
in which case Lemma 3 gives case (b). The record statements are direct
consequences of F3: the defect flows to inadmissible support, which by
definition carries no admissible record; the record process is a deterministic
function of a geometry sector whose one-step law has entropy at most
\(H_{\mathrm{top}}\); and interior-to-boundary information is identically zero.
The final statement is the contrapositive: a continuation avoiding both (a)
and (b) with probability greater than \(\varepsilon\) for arbitrarily large
\(t\) contradicts the displayed dichotomy, so it must fail one of the
hypotheses F1–F4. \(\square\)

**Corollary 1 (uniformly naked collapse).** If additionally every top-band
cell is leaking, then admissible mass itself is exhausted:
\(Z_t\leq \bar T/s+(1-q_0)^{t-s}\) for all \(s\leq t\), with the explicit
threshold time \(t^*(\epsilon)\) of Lemma 2. The description does not merely
visit inadmissibility; it geometrically transfers essentially all of its
probability law outside the admissible state space.

**Corollary 2 (hard exclusion is record-free postselection).** If the singular
histories are instead excised and the kernel renormalized (\(q\equiv 0\) by
fiat), and F1–F2 hold for the renormalized kernel, then the surviving
description enters \(\mathcal T\) in mean time \(\leq\bar T\) and thereafter
runs permanently below any floor \(H_{\mathrm{floor}}>H_{\mathrm{top}}\)
(case (b) with probability \(1-\varepsilon\) for every \(\varepsilon\)). By F3
it retains no record of the deleted branch: the excision is a postselection
that discards coordination without a decodable transfer. It therefore defines
a different, non-equivalent theory that itself crystallizes.

**Corollary 3 (record starvation).** Under F1–F4, from any conservative
occupied cell \(m_t\in\mathcal T\) the boundary channel carries at most
\(H_{\mathrm{top}}\) bits per step about anything: for any random variable
\(X\),

$$
I\!\left(X;B_\ell(m_{t+1})\,\middle|\,m_t\right)
\leq
H\!\left(B_\ell(m_{t+1})\,\middle|\,m_t\right)
\leq
H_{\ell,\Delta}(m_t)
\leq
H_{\mathrm{top}},
$$

because \(B_\ell(m_{t+1})=r(G_\ell(m_{t+1}))\) is a function of the next
macrocell, whose conditional law has entropy \(H_{\ell,\Delta}(m_t)\). So the classical description cannot satisfy the Stage 5
decodability requirement

$$
I\!\left(X_R;Y_\partial^{[t,t+T_{\mathrm{dec}}]}\right)
\geq\eta\,\Delta C_R-\varepsilon'
$$

for any redistribution demand exceeding
\(T_{\mathrm{dec}}\,H_{\mathrm{top}}/\eta\); in the deterministic-freeze
idealization it cannot satisfy it at all. The coordination debt of collapse is
never repaid classically.

**Corollary 4 (forced completion).** Combining Theorem 1 with the CDT
two-boundary requirement and the singularity-inadmissibility criterion: any
gravitational law that keeps a collapsing relational macrostate channel
admissible with \(H_{\ell,\Delta}\geq H_{\mathrm{floor}}>H_{\mathrm{top}}\)
must, before \(T^*\), implement a transformation that (i) changes mechanism
(violates F4 or F1), or (ii) injects new macroscopic distinctions at
resolution \(\ell\) (violates F2), or (iii) opens a new boundary-record
channel (violates F3). By Stages 5–6 of the derivation program, the
persistence-compatible versions of these transformations are exactly the
finite, boundary-decodable, early-privacy-preserving redistributions — the
structural definition of the quantum-completion target. What remains open in
physics is *which* microscopic mechanism implements them; that they must be
implemented is now a theorem at this level.

## 6. Failure-Mode Table

| Continuation | Violated hypothesis | Theorem outcome | Toy policy |
|---|---|---|---|
| naked pushforward | none (leaking) | (a): geometric loss of normalization, unrecorded | `naked_collapse` |
| excise + renormalize | none (conservative) | (b): sub-floor crystallization, record-free postselection | `hard_exclusion` |
| horizon/boundary transfer | F4 (trigger), F3 (new records) | mechanism change; admissible if decodable | `horizon_transfer` |
| bounce-like redistribution | F1 (drift reversed) | mechanism change; admissible if decodable | part of `quantum_completion` |
| new interior variables | F2 (new distinctions) | mechanism change; admissible if decodable | part of `quantum_completion` |

## 7. Physical Justification of F1–F4 (Motivation, Not Proof)

The following is the standard semiclassical case that gravitational collapse
at fixed \((\ell,\Delta)\) instantiates the hypotheses. Each item is physics,
flagged as such; none of it is used in Sections 4–5.

**F1 from Raychaudhuri focusing.** For a hypersurface-orthogonal congruence
with tangent \(u^a\), the Raychaudhuri equation gives
\(d\theta/d\lambda=-\tfrac13\theta^2-\sigma_{ab}\sigma^{ab}
-R_{ab}u^au^b\); with the null/strong energy condition the curvature term is
nonpositive, so convergence is self-reinforcing. Inside the trapped band both
ingoing and outgoing congruences converge, and coarse compactness grows on
the verification timescale — the drift clause. The monotonicity clause is the
resolution-\(\ell\) reading of trapped-region monotonicity (the trapped region
does not spontaneously untrap in classical evolution; horizon area is
nondecreasing).

**Positive defect from Penrose incompleteness.** Given a closed trapped
surface, the null energy condition, and a noncompact Cauchy surface, classical
evolution is geodesically incomplete; deeply trapped configurations reach
inadmissible support within finite affine parameter. Read at fixed
\((\ell,\Delta)\), a positive-measure subset of each deeply collapsed cell
exits \(\mathcal S_{\mathrm{adm}}\) within \(\Delta\): \(q>0\) on
\(\mathcal T\).

**F2 from balding/no-hair shedding.** During late collapse the exterior sheds
distinguishing multipoles through quasinormal ringdown; classically distinct
interior data converge, at any fixed exterior resolution \(\ell\), toward the
same few-parameter (mass, spin, charge) coarse futures. The one-step forward
images of top-band cells therefore occupy a bounded, resolution-independent
number \(N_{\mathrm{top}}\) of cells, approaching the deterministic-freeze
idealization as collapse deepens.

**F3 from classical causal structure.** Behind the trapped band no causal
curve reaches the exterior record; the classical exterior record is determined
by the coarse exterior geometry (charges, area), which is the statement
\(B_\ell=r(G_\ell)\), and \(I(L_\ell;B_\ell)=0\) is classical censorship of
the interior. Classically there is no Hawking channel; that channel is
precisely a mechanism change.

**F4 from universality of the field equations.** Classical GR applies the same
local law at every compactness; nothing in the classical theory triggers a
change of mechanism at a threshold. This is exactly the hypothesis that a
quantum completion must violate.

**What a full derivation would require.** To discharge F1–F4 as theorems
rather than hypotheses one must fix an explicit family of collapse spacetimes
(Oppenheimer–Snyder, Vaidya, or numerical interior models), an explicit
relational coarse map \(\sigma_\ell\), and compute the induced pushforward
kernel, verifying the drift constant \(\delta\), the defect floor \(q_0\), and
the concentration pair \((N_{\mathrm{top}},\varepsilon_{\mathrm{tail}})\).
That computation is the concrete residual task of OP-19 at this rung.

## 8. Simulation Instantiation

`simulations/cosmic_coordination_floor/cosmic_coordination_floor.py` now
reports the theorem's quantities directly:

- `conditional_future_entropy_bits`: the mass-weighted per-cell
  \(H_{\ell,\Delta}(m)\) of Definition 3 — the quantity bounded by Lemma 3.
  Under `hard_exclusion` it decays toward the deterministic-freeze endpoint,
  which the marginal `future_entropy_bits` (a distribution-spread diagnostic)
  understates.
- `mean_forward_drift`: the mass-weighted \(\mathbb E[c(m')-c(m)]\) — the F1
  drift certificate \(\delta\).
- `forward_width`: the mass-weighted standard deviation of the forward
  compactness law — the F2 concentration certificate.
- `admissible_mass` and `singular_mass`: \(Z_t\) and the per-step defect flow
  of Lemma 2.
- summary columns `min_conditional_future_entropy_bits`,
  `first_conditional_floor_violation_step`, `final_mean_forward_drift`, and
  `final_forward_width` locate the theorem's failure times in the toy.

The toy's four policies realize the failure-mode table: the two classical
policies land in cases (a) and (b) respectively, and the two transfer policies
survive precisely by violating F3/F4 with a decodable record.

## 9. Honesty Boundary

**Proven here (exact, finite).** Lemmas 1–3, Theorem 1, Corollaries 1–4, for
any finite sub-stochastic kernel satisfying F1–F4. No gravitational input is
used in the proofs.

**Derived from ACP.** That case (a) is inadmissible (normalizable-record
failure), that case (b) is the crystallization boundary of CDT, and that an
admissible completion must be decodable and privacy-preserving (Stages 5–6).

**Physically motivated, not proven.** That semiclassical gravitational
collapse at fixed \((\ell,\Delta)\) satisfies F1–F4 with nontrivial constants
\((\delta,q_0,N_{\mathrm{top}},\varepsilon_{\mathrm{tail}})\). Section 7
gives the standard case; the explicit pushforward computation is open.

**Open in physics.** Which microscopic mechanism implements the forced
completion, and whether its kernel reproduces Einstein dynamics away from the
floor. This is Stages 4–8 of the derivation program and OP-19/OP-20.
