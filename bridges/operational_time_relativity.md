# Operational-Time Relativity for ACP

*Status: short formal bridge / candidate covariance principle.*

## 1. Starting point

The core ACP paper already treats time operationally. Section 8.1 defines
operational time \(\tau_{\mathrm{op}}\) as the cumulative count of
distinguishable macrostate transitions. Operational time halts at both
absorbing boundaries: at dissolution, because there is no coherent macroscopic
system whose transitions can be distinguished; at crystallization, because
\(H(m'|m)\to 0\) and the system no longer has nontrivial macroscopic futures.

The Schur bridge adds the local persistence inequality

$$
C(t)>L(t)\tau_v,
$$

where \(C\) is the remaining internal capacity, \(L\) is the rate at which
self-reinforcement consumes conditional macrostate entropy, and \(\tau_v\) is
the verification latency. The syndrome-coordination bridge gives the quantum
cycle version: syndrome capacity must exceed the disturbance load per cycle,
and the finite-cycle contraction quantities \(q^*\), \(\eta^*\), and
\(\eta^*/(1-q^*)\) should be reported for implemented protocols.

Thus ACP already contains a relativity of tempo: the relevant clock is not an
external parameter \(t\), but the system's own rate of distinguishable
verification.

## 2. Operational tempo

Let \(S=(\Omega_S,\sigma_S,K_S,\mu_S)\) be a coarse-grained dynamical system,
with macrostates \(M_S\) and transition kernel \(K_S\). Relative to an external
coordinate \(t\), define the operational clock

$$
\tau_S(t)=\int_0^t \nu_S(u)\,du,
$$

where

$$
\nu_S(t)=\frac{d\tau_S}{dt}
$$

is the operational tempo: the rate at which \(S\) executes distinguishable
macrostate-verification steps at the chosen coarse-graining.

For a local operational horizon \(\delta\), write

$$
H_S(\tau,\delta)
  =H(M_S(\tau+\delta)\mid M_S(\tau)).
$$

The normalized boundary coordinate is

$$
h_S(\tau,\delta)=\frac{H_S(\tau,\delta)}{H_{S,\max}}.
$$

The ACP boundaries are \(h_S=0\) and \(h_S=1\). A productive system is not a
system with a particular external speed; it is a system whose own operational
clock advances while remaining separated from both boundaries.

## 3. Candidate transformation laws

Let two operational coordinates be related by a smooth monotone
reparameterization

$$
\bar{\tau}=\phi(\tau),
\qquad
\phi'(\tau)>0.
$$

The ACP quantities split into scalars, rate densities, and operational
horizons.

**Scalar structural quantities.** Conditional entropy, normalized boundary
position, rank/capacity, mutual information per cycle, coherent information per
cycle, \(q^*\), and \(\eta^*/(1-q^*)\) are pulled back as scalars:

$$
\bar{H}(\bar{\tau})=H(\tau),
\qquad
\bar{h}(\bar{\tau})=h(\tau),
\qquad
\bar{C}(\bar{\tau})=C(\tau).
$$

In a finite QEC or feedback cycle, the implemented CPTP map is the operational
object. Changing the external duration of the cycle changes a rate such as
\(-\log q^*/t_{\mathrm{cycle}}\), but not \(q^*\) itself.

**Rate densities.** Quantities defined per unit operational time transform as
densities:

$$
\bar{L}(\bar{\tau})
  =\frac{d\tau}{d\bar{\tau}}L(\tau),
\qquad
\bar{\lambda}(\bar{\tau})
  =\frac{d\tau}{d\bar{\tau}}\lambda(\tau).
$$

Here \(L=-dH/d\tau\) is the crystallization load per operational step, and
\(\lambda\) may be any continuous contraction, leakage, or drift rate expressed
per operational step.

**Latencies and horizons.** Operational durations transform contravariantly:

$$
\bar{\delta}_v
  =\phi'(\tau)\delta_v.
$$

Therefore the load over one verification buffer is invariant:

$$
\bar{L}\,\bar{\delta}_v=L\,\delta_v.
$$

This is the basic covariance of the Schur persistence inequality:

$$
C>L\delta_v
\quad\Longleftrightarrow\quad
\bar{C}>\bar{L}\bar{\delta}_v.
$$

For two distinct systems \(A\) and \(B\), a stronger comparison requires more
than a change of parameter. Over intervals \(I_A,I_B\), call \(A\) and \(B\)
operationally conjugate if there is a monotone tempo map
\(\tau_B=\phi(\tau_A)\) and a macrostate isomorphism
\(\Psi:M_A\to M_B\) such that corresponding transition kernels satisfy

$$
K_B^{\phi(\tau_A+\delta)-\phi(\tau_A)}
  =\Psi_* K_A^\delta \Psi_*^{-1}.
$$

When this condition holds, boundary membership, normalized entropy trajectory,
capacity-load margin, and information balances are invariant descriptions of
the same operational process. When it does not hold, only weaker comparisons
between dimensionless diagnostics are justified.

## 4. Proper productive interval

A connected interval \(I=[\tau_0,\tau_1]\) in a system's own operational clock
is a **proper productive interval** when it has positive operational length and,
for every \(\tau\in I\), all of the following hold.

1. **Finite resolved clock.**
   The operational tempo is finite and nonzero:

   $$
   0<\nu_S<\infty.
   $$

   The system is neither an unresolved noise cloud nor a perfectly inert fixed
   structure.

2. **Two-boundary separation.**
   For the verification horizon \(\delta_v\),

   $$
   0<h_S(\tau,\delta_v)<1.
   $$

3. **Capacity-load margin.**
   In continuous form,

   $$
   C_S(\tau)>L_S(\tau)\delta_v(\tau).
   $$

   In a finite-cycle QEC or feedback implementation, the corresponding
   cycle-native condition is

   $$
   q^*<1,
   \qquad
   \eta^*/(1-q^*)<\epsilon_{\mathrm{floor}},
   $$

   for a domain-specified admissible floor.

4. **Memory with innovation.**
   The future is neither independent noise nor deterministic repetition:

   $$
   I(M_S(\tau);M_S(\tau+\delta_v))>0,
   \qquad
   H(M_S(\tau+\delta_v)\mid M_S(\tau))>0.
   $$

5. **Record selectivity, when a controller or environment is present.**
   Useful records must reveal the relevant error or disturbance sector without
   capturing the protected logical state:

   $$
   I(E;R)>0,
   \qquad
   I(L_{\mathrm{prot}};R\mid E)\leq\epsilon_L.
   $$

The proper duration of the productive interval is the internal amount of
verified continuation,

$$
\Delta\tau_{\mathrm{prod}}(S)
  =\int_{\tau_0}^{\tau_1}d\tau.
$$

This is the ACP analogue of proper time: it is measured along the system's own
trajectory of distinguishable transitions, not by a lab clock. A system may
look fast in external time while having a short proper productive interval, or
look slow while sustaining a long one.

For ACP Quantum, this distinction is useful. A perfectly isolated logical
state may retain coherence, but if there is no syndrome or noise-characterizing
record then it does not occupy the noise-tailored proper productive interval.
Conversely, a noisy device may run many hardware cycles per second, but its
proper productive interval is short if the syndrome stream leaks logical
information or if \(q^*\) approaches one. The invariant question is not "how
fast does it run?" but "how many protected, syndrome-informative verification
steps can it execute before reaching a boundary?"

## 5. Open theorem target

The reparameterization laws above are direct consequences of the chain rule.
The nontrivial theorem target is cross-system covariance:

**Operational-Time Covariance Problem.** Characterize the weakest conditions
under which two systems with different operational tempos, different
coarse-grainings, and possibly different record channels can be treated as
realizations of the same ACP productive interval.

The expected answer should include:

- an operational conjugacy or simulation relation between transition kernels;
- invariance of \(0<h<1\), \(C>L\delta_v\), and record-selectivity quantities;
- a rule for finite-cycle protocols, where \(q^*\) and
  \(\eta^*/(1-q^*)\) are cycle invariants while continuous rates are
  tempo-dependent;
- diagnostics for the non-conjugate case, where only normalized or
  dimensionless comparisons are legitimate.

Until that theorem is written, operational-time relativity should be treated
as a disciplined bridge: correct for reparameterizing a single process, a
candidate comparison principle across systems, and an open problem when the
systems' macrostate partitions are not already known to match.

## 6. First executable covariance probe

The braided quantum clock (`simulations/quantum_braiding_clock/`, Experiment
C; see `bridges/quantum_braiding_timekeeping.md` §12) now instantiates the
simplest nontrivial case of the covariance problem: a family of monitored
qubits with identical tick count, per-tick measurement strength, and
per-tick feedback, differing only in lab-time tick spacing. The result
matches section 3's classification. Tick-native scalars (memory retention,
record slack) are invariant across tempos unconditionally. Record-facing
diagnostics (phase lock, syndrome information) are invariant exactly when
the disturbance kernel commutes with the tempo map — detuning scaled to the
system's own tick — and fail completely when the disturbance keeps lab time,
in which case the slowed members leave the proper productive interval
altogether because record selectivity condition 5 fails. The failure mode is
sharp rather than gradual, which is encouraging for the theorem target: the
conjugate and non-conjugate cases are empirically distinguishable even in a
32-tick toy.
