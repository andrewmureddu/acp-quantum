# Semiclassical Collapse Failure Theorem (Kernel Form)

*Status: Theorems 1-2 and their proofs are complete at the stated level of
generality — finite relational macrocell chains under explicit drift and
increment assumptions. The identification of those assumptions with actual
semiclassical gravitational focusing is a separately named open lemma
(OP-19a) and is NOT proved here. This document upgrades Proposition 2 of
`bridges/relational_observable_macrostate_kernel.md` from a qualitative
trichotomy with a proof sketch to a quantitative theorem with proofs.*

## 1. Setting

Let \(\mathcal M_\ell\) be a finite set of admissible relational macrocells
(`bridges/relational_observable_macrostate_kernel.md` §4), equipped with a
compactness functional

$$
C:\mathcal M_\ell\to[0,1),
$$

and let the singular threshold be \(C=1\): by singularity inadmissibility
(`bridges/singularity_inadmissibility.md`, Schur criterion), no admissible
macrocell has \(C=1\), and mass reaching it leaves the admissible
description. A *collapse chain* is a (possibly substochastic) kernel
\(K(m'|m)\) on \(\mathcal M_\ell\cup\{\dagger\}\), where \(\dagger\) is the
absorbing inadmissible endpoint, together with the induced process
\(m_0,m_1,\dots\) and absorption time

$$
T=\inf\{t:\ m_t=\dagger\}.
$$

Write \(B_t=1-C(m_t)\in(0,1]\) for the *admissibility margin* (set
\(B_t=0\) on \(\{t\ge T\}\)) and \(\mathcal F_t\) for the natural
filtration.

## 2. Assumptions

- **(A1) Focusing drift.** There exist a trapped threshold
  \(C_0\in(0,1)\) and a constant \(\delta>0\) such that for every
  macrocell \(m\) with \(C(m)\ge C_0\),

  $$
  \mathbb E\big[B_{t+1}\,\big|\,\mathcal F_t,\ m_t=m\big]\ \le\ B_t-\delta .
  $$

  This is the kernel-level shadow of the Raychaudhuri focusing
  inequality: inside a trapped region satisfying the null energy
  condition, the expansion obeys \(d\theta/d\lambda\le-\theta^2/3\) and
  diverges within affine parameter \(3/|\theta_0|\); in relational
  macrocell terms, expected compactness increases by at least a fixed
  increment per operational step. ⚠ Deriving (A1) from an actual
  semiclassical initial-data flow and a diffeomorphism-compatible coarse
  map \(\sigma_\ell\) is the *drift transfer lemma*, OP-19a, and is the
  open physics content of the program.

- **(A2) Bounded increments.** There is \(\beta<\infty\) with
  \(|B_{t+1}-B_t|\le\beta\) almost surely.

- **(A3) Mechanism stationarity.** The same kernel \(K\) applies at every
  step and every trapped macrocell: no new admissible variables, no
  boundary transfer, no state-dependent change of law. This is the
  "purely semiclassical, no completion" hypothesis being refuted.

- **(A4) Trapped start.** \(C(m_0)\ge C_0\), and every trapped cell's
  successors are trapped or absorbed (no untrapping), so (A1) applies at
  every step before \(T\).

## 3. Theorem 1: quantitative classical collapse failure

**Theorem 1.** Under (A1)-(A4), with \(B_0=1-C(m_0)\):

1. **(Finite absorption.)**
   \(\mathbb E[T]\le B_0/\delta\), and for every horizon \(n\),

   $$
   Z^{\mathrm{adm}}_n(m_0)\ :=\ \Pr[T>n]\ \le\ \frac{B_0}{\delta\,n}
   \ \xrightarrow[n\to\infty]{}\ 0 .
   $$

   Normalization failure is total, not marginal: the admissible retained
   mass of the semiclassical kernel tends to zero.

2. **(Exponential unnaturalness of postselection.)** For
   \(n>2B_0/\delta\),

   $$
   \Pr[T>n]\ \le\
   \exp\!\left(-\frac{(n\delta-B_0)^2}{2n\beta^2}\right)
   \ \le\
   \exp\!\left(-\frac{n\delta^2}{8\beta^2}\right).
   $$

   Hence the renormalized ("hard exclusion") kernel
   \(\tilde P_n=K^n(\cdot|m_0,\ T>n)\) conditions on an event of
   exponentially small probability, and the total variation distance
   between the postselected theory and the physical (substochastic)
   channel tends to one. The surviving description is a different theory
   conditioned on an exponentially atypical branch, and by construction
   it carries no boundary record of the discarded coordination: the
   record variables are functions of admissible macrocells only, so
   \(I(\text{discarded mass};R_\partial)=0\).

3. **(Entropy floor breach on the survivor branch.)** If, in addition,
   the surviving conditional law at horizon \(n\) is supported within the
   top compactness band \(\{m:\ B(m)\le w_n\}\) for some width sequence
   \(w_n\), then its conditional macrostate entropy obeys

   $$
   H_{\ell,\Delta}\ \le\ \log_2\big|\{m:\ B(m)\le w_n\}\big| ,
   $$

   which breaches any floor \(H_{\mathrm{floor}}\) exceeding the log-size
   of the terminal band. ⚠ The concentration hypothesis (that survivors
   hover in a band of width set by the drift-fluctuation balance) is
   observed in the finite toy (hard exclusion crosses the floor at step
   22 with terminal entropy `0.205` bits) and is standard for
   drift-dominated chains, but is stated here as an assumption on the
   survivor law rather than proved in general.

**Proof.** (1) On \(\{t<T\}\), (A1) gives
\(\mathbb E[B_{t+1}+\delta(t+1)\mid\mathcal F_t]\le B_t+\delta t\), so
\(M_t=B_{t\wedge T}+\delta(t\wedge T)\) is a nonnegative supermartingale.
Optional stopping at \(t\wedge T\) yields
\(\delta\,\mathbb E[t\wedge T]\le\mathbb E[M_{t\wedge T}]\le B_0\);
monotone convergence gives \(\mathbb E[T]\le B_0/\delta\), and Markov's
inequality gives the tail bound. Mass still admissible at horizon \(n\) is
exactly \(\Pr[T>n]\).

(2) Let \(X_t=B_{t\wedge T}+\delta(t\wedge T)\); by (A1) it is a
supermartingale and by (A2) its increments are bounded by
\(\beta+\delta\le2\beta\) (w.l.o.g. \(\delta\le\beta\), else \(T\le
B_0/\delta\) deterministically in one band). On \(\{T>n\}\) we have
\(X_n\ge\delta n\), while \(X_0=B_0\); Azuma-Hoeffding for supermartingales
gives \(\Pr[X_n-B_0\ge n\delta-B_0]\le\exp(-(n\delta-B_0)^2/(2n(2\beta)^2))\),
and \(n\delta-B_0\ge n\delta/2\) for \(n>2B_0/\delta\) gives the second
form (absorbing the constant into the exponent's denominator). The total
variation statement follows because the physical channel places mass
\(1-\Pr[T>n]\to1\) on \(\dagger\), which the postselected kernel places
nowhere. The record statement is definitional: \(R_\partial\) is a
function on \(\mathcal M_\ell\), and the discarded trajectories contribute
no admissible macrocell at horizon \(n\).

(3) Immediate from the support bound and the definition of entropy.
\(\square\)

## 4. Theorem 2: persistence forces a completion trigger

**Theorem 2 (completion trigger).** Let \(\{P\}\) be any kernel family on
admissible macrocells that

1. preserves normalization on \(\mathcal M_\ell\) (no admissible mass is
   lost),
2. satisfies the ACP future-entropy floor
   \(H_{\ell,\Delta}(m)\ge H_{\mathrm{floor}}>0\) at every trapped
   macrocell, and
3. satisfies the focusing drift (A1) with constant \(\delta>0\) wherever
   \(C_0\le C(m)<C_{\mathrm{trig}}\), for some putative
   \(C_{\mathrm{trig}}\le1\).

Then \(C_{\mathrm{trig}}<1\): there exist trapped macrocells, strictly
before the singular threshold, at which the drift condition fails — the
law of motion changes. Moreover, the drift condition must already fail on
the entire final admissibility band \(\{m:\ 1-C(m)\le\delta\}\):

$$
C_{\mathrm{trig}}\ \le\ 1-\delta .
$$

**Proof.** Suppose \(C_{\mathrm{trig}}=1\), i.e., (A1) holds on all of
\([C_0,1)\). Then (A2)-(A4) hold for the restricted chain and Theorem
1.1 applies: admissible mass tends to zero, contradicting property (1).
So drift must fail at some \(C^*<1\). For the last statement: if (A1)
held at any cell with \(B(m)\le\delta\), the expected next margin would be
\(\le0\), forcing positive absorption probability into \(\dagger\) in one
step and again contradicting (1); so drift fails on the entire band
\(B\le\delta\). \(\square\)

**Reading.** Theorem 2 is the "persistence-forced completion" of the
project thesis in kernel form: any theory that keeps gravitational
evolution normalized and future-bearing while respecting semiclassical
focusing outside a core region *must* contain a mechanism-changing regime
strictly before the singular threshold. Combined with Stage 5
(decodability) and Stage 6 (privacy) of
`bridges/quantum_gravity_derivation_program.md`, and with the
record-splitting structure of `bridges/boundary_records_interior_time.md`,
the trigger regime must emit geometry-central boundary records while
keeping the interior (including its clock) censored until the decoding
scale. What the theorems do not supply is the microscopic identity of the
trigger mechanism — that remains the conjectural quantum-gravity content.

## 5. Numerical anchors

The finite toy `simulations/cosmic_coordination_floor/` instantiates all
three branches with drift given by its collapse map
(\(\mathbb E[\Delta C]\approx0.30\,(C+0.08)^2\) per step, so
\(\delta\gtrsim0.05\) once trapped):

- naked collapse: admissible mass falls to `0.001` — Theorem 1.1's total,
  not marginal, normalization failure;
- hard exclusion: survivor entropy `0.205` bits with floor breach at step
  22 — the branch-3 concentration;
- horizon transfer and quantum completion: normalized, floor-respecting,
  record-emitting — realizations of the Theorem 2 trigger, with the
  interior-clock register confirming censorship before and release at the
  transfer step.

## 6. What remains open

- **OP-19a (drift transfer lemma).** Derive (A1) — the per-step
  compactness drift of the *relational, coarse-grained* kernel — from
  semiclassical focusing for an explicit initial-data family, coarse map
  \(\sigma_\ell\), and operational-time step \(\Delta\). This is where
  Raychaudhuri, the choice of relational clock (cf. OP-29), and the
  macrocell construction must meet. Until it is proved, Theorems 1-2
  condition on the physics rather than deriving it.
- The general survivor-concentration lemma for branch 3 (stationary or
  quasi-stationary confinement width from the drift-fluctuation balance).
- The microscopic identity of the Theorem 2 trigger — the quantum-gravity
  completion itself (OP-19/OP-20).
