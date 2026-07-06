# The Cadence Control Law: Optimal Record Tempo in the Productive Interval

*Status: exploratory bridge note; the general interior-optimum proposition and
its two instances (correction cadence, adaptation cadence) are **proved** at
the toy-model level, verified exactly by `simulations/cadence_control_law/`,
and shown to retrodict the previously unexplained optimum of the
`simulations/risky_qec_claims/` monitoring scan (interval 4 at backaction
0.012; interval 1 at zero backaction). The component mathematics is standard
(Zeno/anti-Zeno crossovers, QEC cycle-time optimization, bias-variance window
selection); the contribution claimed here is recognition — that these are one
two-boundary tempo law with a derivable exponent classification — plus the
ACP reading and the operational-time covariance conjecture. Tracked as
OP-30.*

## 1. Thesis

Question (Andrew): is there a cadence control law to be discovered or
recognized?

Answer: recognized. The law was already present, quantitatively, in this
project's own simulation data. The general statement:

> **Cadence control law.** Let a monitored persistent system pay a cost
> \(c>0\) per record event (backaction, overhead, leakage), and let
> unrecorded drift contribute an accumulated per-unit-time cost
> \(\alpha T^{s}\) that grows with the inter-record interval \(T\) with order
> \(s>0\), because each record event resets the accumulation. Then the
> persistence cost rate
>
> $$ J(T)=\alpha T^{s}+\frac{c}{T} $$
>
> has a unique interior optimum
>
> $$ T^{*}=\Big(\frac{c}{s\,\alpha}\Big)^{\frac{1}{s+1}},
> \qquad
> J(T^{*})=(s+1)\,s^{-\frac{s}{s+1}}\,\alpha^{\frac{1}{s+1}}\,
> c^{\frac{s}{s+1}} , $$
>
> so the **cadence exponent** — the sensitivity of the optimal record tempo
> to the record cost — is \(1/(s+1)\), fixed by the accumulation order alone.

The two boundaries of the tempo axis are the two ACP boundaries:

- \(T\to 0\) (continuous monitoring): the record channel dominates the
  dynamics — backaction, burden, and Zeno-like pinning. This is the
  crystallization-*side* cost, with the caution of
  `simulations/risky_qec_claims/` kept in force: over-monitoring carries
  crystallization-type costs in these toys; the identification of syndrome
  measurement *as* crystallization remains an overstrong claim.
- \(T\to\infty\) (no monitoring): drift accumulates past decodability —
  dissolution.

The productive interval reappears on the tempo axis, and the cadence law is
its interior optimum: uncertainty allocation across *times*, the temporal
sibling of the spectral allocation \(N(k)\) across scales in
`bridges/reality_reflective_mathematics.md` and
`bridges/turbulence_productive_interval.md`.

## 2. General Proposition

### Proposition 2.1 (Interior optimum and comparative statics)

For \(\alpha,c>0\) and \(s>0\), the function
\(J(T)=\alpha T^{s}+c/T\) on \(T\in(0,\infty)\) has a unique critical point

$$
T^{*}=\Big(\frac{c}{s\alpha}\Big)^{\frac{1}{s+1}},
$$

which is the global minimum, with minimum value
\(J(T^{*})=(s+1)s^{-s/(s+1)}\alpha^{1/(s+1)}c^{s/(s+1)}\). Moreover
\(T^{*}\) is strictly increasing in \(c\) with log-log slope \(1/(s+1)\) and
strictly decreasing in \(\alpha\) with log-log slope \(-1/(s+1)\).

*Proof.* \(J'(T)=s\alpha T^{s-1}-c/T^{2}\) vanishes iff
\(T^{s+1}=c/(s\alpha)\); \(J''(T)=s(s-1)\alpha T^{s-2}+2c/T^{3}>0\) at the
critical point (directly for \(s\ge1\); for \(0<s<1\) substitute
\(c=s\alpha (T^{*})^{s+1}\) to get
\(J''(T^{*})=s(s+1)\alpha (T^{*})^{s-2}>0\)). Limits
\(J(0^{+})=J(\infty)=\infty\) make it global. The value and the exact
power-law comparative statics follow by substitution. \(\square\)

### Remark 2.2 (Existence condition: records must be restorative and costly)

The interior optimum exists precisely when both structural features hold:

- \(c>0\): records cost something. If \(c=0\), \(T^{*}\to0\) — monitor
  continuously; the Zeno boundary is reached and the tempo interval closes
  from the crystallization side.
- \(s>0\): records reset accumulation, so that the drift cost *rate* grows
  with the interval. If drift contributes only a constant rate that records
  cannot reset (\(s=0\)), then \(J(T)=\alpha+c/T\) is strictly decreasing —
  never monitor; cadence is not a control variable at all.

So a cadence control law exists exactly for systems whose record channel is
*restorative* (correction, recalibration, re-estimation) and *costly*
(backaction, overhead, leakage). That is precisely the class of systems the
noise-tailored QEC program studies.

## 3. Instance A: Correction Cadence (Square-Root Law)

Model (matching `simulations/risky_qec_claims/` and
`simulations/cadence_control_law/`): a 3-qubit repetition memory with
per-tick bit-flip probability \(p\) per qubit; majority-vote correction every
\(T\) ticks; each correction event applies logical dephasing backaction
\(b\), i.e. a per-event coherence cost \(\gamma_b=-\ln(1-b)\).

Exactly, a qubit is flipped after \(T\) ticks with probability
\(q(T)=\tfrac12(1-(1-2p)^{T})\), the per-cycle miscorrection probability is
\(P_{\mathrm{cyc}}(T)=3q^{2}(1-q)+q^{3}\), logical flips compose across
cycles by XOR, and the exact per-tick cost rate is

$$
J(T)=\frac{-\tfrac12\ln\!\big(1-2P_{\mathrm{cyc}}(T)\big)+\gamma_b}{T}.
$$

For \(pT\ll1\), \(P_{\mathrm{cyc}}\approx3(pT)^{2}\), so
\(J(T)\approx 3p^{2}T+\gamma_b/T\): Proposition 2.1 with \(s=1\),
\(\alpha=3p^{2}\), \(c=\gamma_b\), giving the **square-root law**

$$
T^{*}\approx\frac{1}{p}\sqrt{\frac{\gamma_b}{3}} .
$$

For a code correcting \(t\) errors, \(P_{\mathrm{cyc}}\sim C(pT)^{t+1}\)
gives \(s=t\) and

$$
T^{*}=\frac{1}{p}\Big(\frac{\gamma_b}{t\,C}\Big)^{\frac{1}{t+1}} ,
$$

with two structural readings:

- **Fill fraction.** The dimensionless optimal load
  \(pT^{*}=(\gamma_b/(tC))^{1/(t+1)}\) is the expected fraction of the
  code's correction capacity consumed per cycle — the invariant form of the
  law, independent of the clock used to state \(p\) and \(T\).
- **Protection flattens cadence.** Larger \(t\) gives exponent
  \(1/(t+1)\to0\): better codes make the optimal cadence insensitive to the
  record cost.

## 4. Instance B: Adaptation Cadence (Cube-Root Law)

Model: a controller tracks a parameter drifting at rate \(a\) per round
(e.g., a physical error rate under drift, as in
`simulations/hardware_adaptive_decoder/`) through observations with noise
variance \(\sigma^{2}\), estimating by a moving average over the last \(W\)
rounds. Exactly,

$$
M(W)=\underbrace{\frac{\sigma^{2}}{W}}_{\text{estimation noise}}
+\underbrace{\frac{a^{2}(W-1)^{2}}{4}}_{\text{staleness bias}} ,
$$

Proposition 2.1 with \(s=2\) (large \(W\)), \(\alpha=a^{2}/4\),
\(c=\sigma^{2}\), giving the **cube-root law**

$$
W^{*}\approx\Big(\frac{2\sigma^{2}}{a^{2}}\Big)^{\frac{1}{3}} .
$$

This is the quantitative content behind the qualitative H1/H2 finding that
gated adaptation beats overactive updating: updating every round sets
\(W\approx1\), maximizing estimation noise; never updating sets
\(W\to\infty\), maximizing staleness. The law is stated for the
moving-average controller class; other estimators shift the constants but
polynomial bias-variance tradeoffs stay inside the exponent classification
of Proposition 2.1.

## 5. Verification and Retrodiction

`simulations/cadence_control_law/cadence_control_law.py` computes the exact
objectives (no Monte Carlo), takes integer argmins, and fits log-log
exponents:

| Check | Fitted | Predicted |
|---|---|---|
| \(T^{*}\) vs backaction \(b\) (at \(p=0.002\)) | `0.5515` | \(1/2\) |
| \(T^{*}\) vs drift \(p\) (at \(b=0.012\)) | `-0.9942` | \(-1\) |
| \(W^{*}\) vs drift \(a\) (at \(\sigma^{2}=1\)) | `-0.6571` | \(-2/3\) |

The residual deviation in the first row is finite-\(b\) curvature (the
\((1-q)\) factor in \(P_{\mathrm{cyc}}\) and the convexity of
\(\gamma_b=-\ln(1-b)\)); the slope approaches \(1/2\) as \(b\to0\).

**Retrodiction.** At the operating point of the prior monitoring scan
(\(p=0.02\), \(b=0.012\)), the exact objective's integer optimum is
\(T^{*}=4\) (continuum prediction \(3.17\)) — exactly the best interval
found empirically by `simulations/risky_qec_claims/` with its independent
composite productive score; and at \(b=0\) the optimum is \(1\), again
matching. The interval-4 result, previously reported as a bare scan outcome,
is the square-root law evaluated at that operating point.

## 6. ACP Reading

### 6.1 The tempo productive interval

The CDT's two absorbing boundaries reappear as the two divergences of
\(J(T)\): record-dominated dynamics at \(T\to0\), drift-dominated dynamics at
\(T\to\infty\). The optimal cadence is not a compromise between two
inconveniences; it is the same structural statement as the productive
interval itself, projected onto the tempo axis. Remark 2.2 gives the
boundary-collapse conditions: costless records close the interval from one
side, non-restorative records from the other.

### 6.2 Records as clock ticks

`bridges/quantum_braiding_timekeeping.md` treats collapse-like record events
as the ticks of an internal clock. The cadence law fixes the *rate* of that
clock: a persistent monitored system should tick at
\(1/T^{*}\propto p\,(t C/\gamma_b)^{1/(t+1)}\) — faster under stronger
drift, slower under costlier records, with the sensitivity set by how much
protection the code affords. This is a candidate answer to OP-22's
clock-regularity question.

### 6.3 Operational-time covariance (conjectural)

The law as stated uses lab ticks. `bridges/operational_time_relativity.md`
requires ACP-lawful statements to be covariant under tempo
reparameterization. Conjecture C-1 (OP-30): under a change of operational
tempo, \(p\), \(1/T^{*}\), and \(a\) transform as rate densities while the
fill fraction \(pT^{*}\) and the optimal cost ratio — record-cost share
\(\tfrac{c/T^{*}}{J(T^{*})}=\tfrac{s}{s+1}\), drift share
\(\tfrac{1}{s+1}\) — are invariants. Note the second: **at the optimum, the
fraction of persistence cost spent on records is \(s/(s+1)\)** — one half
for single-error correction, two thirds for tracking — a dimensionless,
clock-free signature that could be checked in any system suspected of
running at its cadence optimum.

### 6.4 Institutional cadence

`bridges/restraint_ethics.md` bounds monitoring burden; the cadence law
suggests its dynamic form: audit/oversight frequency in an institution with
restorative, costly review should sit at an interior optimum with the same
exponent structure — under-auditing accumulates undecoded drift,
over-auditing pays burden and induces the capture-like pathologies the
restraint bridge models. This is a reading, not a result; domain-native
observables are OP-24 work.

## 7. Prior Art (External Inputs)

None of the component mathematics is new. Zeno and anti-Zeno crossovers
identify nonmonotonic dependence of decay on measurement frequency; optimal
QEC cycle length under noisy syndrome extraction is folklore in the
fault-tolerance literature; window/forgetting-factor selection by
bias-variance tradeoff is classical estimation theory; and Proposition 2.1
is elementary. What this note claims is the recognition that these are one
law with a derivable exponent classification \(1/(s+1)\), its two-boundary
ACP reading, the invariant fill-fraction/cost-share forms, and the exact
retrodiction of this project's own prior scan.

## 8. Relation to Existing ACP Quantum Material

- `simulations/risky_qec_claims/`: its monitoring-interval scan is the
  empirical anchor; the law explains its optimum quantitatively.
- `bridges/hardware_adaptive_alignment.md` +
  `simulations/hardware_adaptive_decoder/`: the update gate ("adapt only
  when expected benefit exceeds overhead") is the policy form of Instance B;
  the next hardware step can estimate \(s\), \(\alpha\), \(c\) from H1/H2
  traces and *predict* the update cadence instead of gating heuristically.
- `bridges/sacr_contraction_calibration.md`: per-cycle contraction \(q^*\)
  and leakage \(\eta^*\) are natural inputs for measuring \(\alpha\) and
  \(c\) on a real syndrome-extraction cycle.
- `bridges/operational_time_relativity.md` (OP-29) and
  `bridges/quantum_braiding_timekeeping.md` (OP-22): §6.2–6.3 give both
  bridges a concrete quantitative target.
- `bridges/reality_reflective_mathematics.md` /
  `bridges/turbulence_productive_interval.md`: allocation across times as
  the sibling of allocation across scales; the cost-share invariant
  \(s/(s+1)\) plays the role of a spectral slope.

## 9. What This Does Not Yet Do

- **Toy scope.** Both instances assume Markovian, uncorrelated drift and a
  fixed controller class; correlated or adversarial drift, non-Markovian
  noise, and optimal (rather than moving-average) estimators may shift
  constants and could break the clean power-law classification — checking
  whether \(1/(s+1)\) survives is open.
- **The crystallization identification is structural, not literal.** The
  \(T\to0\) divergence is a cost statement in these toys; per the risk
  audit, "measurement is crystallization" is not claimed.
- **Covariance is conjectural.** C-1 (fill-fraction and cost-share
  invariance under tempo reparameterization) is stated, not proved; it is
  the natural first OP-29 theorem target.
- **No measured-hardware confirmation.** The H1/H2 replay traces exist; the
  law's constants have not yet been estimated from them.

## 10. Open Direction (OP-30)

1. **Prove Conjecture C-1** (operational-time covariance of the cadence
   law): transform laws for \(p\), \(a\), \(1/T^{*}\) as rate densities;
   invariance of \(pT^{*}\) and of the cost shares \(s/(s+1)\), \(1/(s+1)\).
2. **Estimate the law from H1/H2 traces:** fit \(\alpha\), \(c\), \(s\)
   from `simulations/hardware_adaptive_decoder/` replay data and compare the
   predicted update cadence with the gated policy's empirical update times.
3. **Robustness of the exponent classification** under correlated drift,
   non-Markovian noise, and optimal estimation.
4. **Gravitational and institutional instances:** boundary-record cadence in
   the macrocell collapse toy (does the quantum-completion policy's trigger
   scale sit at a cadence optimum?); audit-frequency form for OP-24.
