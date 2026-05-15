# Hardware-Level Adaptive Syndrome Alignment

*Status: implementation roadmap plus fixed-code adaptive-decoder, H1
trace-replay, and H2 circuit-level syndrome-extraction / Pauli-frame logical
audit / schedule-phase audit scaffolds; not yet a hardware demonstration.*

## Abstract

Hardware-level implementation is now the target of ACP Quantum. The useful
claim is not that structured noise is philosophically interesting, and not that
an encoding can be changed until a toy coherence metric improves. The target is
a device-facing control stack:

> use measured hardware noise structure to update syndrome interpretation,
> decoder likelihoods, gauge choices, or calibration schedules while preserving
> the same logical information and accounting for the overhead of adaptation.

The first executable step is
`simulations/hardware_adaptive_decoder/`. It keeps a 3-qubit repetition code
fixed and adapts only the decoder's likelihood table under drifting,
non-identically distributed data-qubit error rates. This is intentionally
smaller than a surface-code patch, but it has the right hardware grammar:
syndrome measurements, calibration lag, update overhead, logical-channel
output, and finite-cycle contraction diagnostics.

The first H1 replay interface now lives in the same directory as
`hardware_replay_decoder.py`. It accepts a per-round calibration/channel trace,
runs the same fixed/static/adaptive/overactive comparison, and writes replay
summary and timeseries outputs. The included trace is synthetic and seeded; its
purpose is to define the file interface that real backend logs can later
replace.

The first H2 circuit-level scaffold now lives at
`simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`. It
keeps the same 3-qubit logical memory but expands each round into explicit
ancilla preparation, CNOT-style parity extraction, idling, measurement,
leakage-like random records, correlated faults, crosstalk, and feedback error.
This is still a synthetic stress trace, not a backend result, but it is the
first scaffold with an explicit controller-record leakage audit.
It now also reconstructs the cumulative induced logical bit-flip channel from
the physical transition matrix, propagates a 64-state data Pauli frame to audit
the actual diagonal logical Pauli channel, averages terminal metrics over the
final calibration phase window, and replays all offsets of the calibration
schedule for generated H2 traces.

## 1. Hardware Thesis

A quantum processor should expose error-sector information without exposing the
logical state. In operational terms, the device should be engineered so that

$$
I(\mathrm{error};\mathrm{syndrome}) > 0
$$

while

$$
I(\mathrm{logical};\mathrm{environment}) \approx 0.
$$

At hardware level, this is not a single theorem. It is a closed-loop
implementation problem:

1. collect calibration and syndrome data;
2. estimate the current noise structure;
3. update a decoder, gauge, schedule, or local frame;
4. measure whether logical memory improves after update overhead;
5. verify that the update did not leak, measure, or reset the stored logical
   state.

The practical object is a memory experiment, not a state-preparation score.

## 2. Device Stack

A hardware implementation should separate five layers.

| Layer | Hardware object | ACP/QEC role |
|---|---|---|
| Physical noise stream | \(T_1\), \(T_2\), crosstalk, leakage, correlated Pauli events, drift | source of structured error information |
| Syndrome stream | repeated stabilizer or gauge measurements | observable error-sector channel |
| Estimator | online noise model \(\widehat\Sigma_t\) or decoder likelihoods | converts syndrome/calibration data into actionable structure |
| Policy | update rule for decoder, gauge, schedule, local Clifford frame, or feedback | decides when adaptation beats overhead |
| Logical audit | logical channel, \(F_e\), logical error per round, leakage and controller-record diagnostics | prevents false wins from reset, branch-population artifacts, or centralizing controller records |

The policy is only valuable if it beats both a standard fixed decoder and a
static noise-tailored decoder. It must also lose gracefully when the noise is
stationary, because unnecessary adaptation is hardware overhead.

## 3. Minimum Hardware Protocol

The first lab-grade experiment should be a memory benchmark with four
baselines:

1. **Fixed standard:** standard decoder and schedule.
2. **Static tailored:** calibrate once, then keep decoder/gauge/schedule fixed.
3. **Adaptive tailored:** recalibrate or infer drift online and update only when
   expected logical benefit exceeds overhead.
4. **Overactive adaptive:** update too often, exposing the cost of control
   traffic, latency, measurement, and extra idle time.

The data qubits must not be reset or reinitialized during the memory
experiment. If calibration happens on the same logical memory, the elapsed time
and extra operations count as overhead. If calibration happens on parallel
calibration qubits, the experiment must report that architectural assumption.

Required outputs:

- logical error per round or memory-time fit;
- entanglement fidelity or logical Pauli transfer matrix;
- update count and update latency;
- characterization overhead;
- syndrome-event correlation or decoder-likelihood history;
- \(q^*\), \(\eta^*\), and \(\eta^*/(1-q^*)\) for the implemented cycle when a
  finite cycle map can be reconstructed.

## 4. First Fixed-Code Benchmark

The new benchmark at `simulations/hardware_adaptive_decoder/` is deliberately
minimal. It uses a 3-qubit repetition memory with noisy parity checks. The
physical code is never reoriented. Instead, the decoder changes its likelihood
weights for the three data qubits as the hardware error rates drift.

This matters because it preserves the same logical channel. The older
axis-switching toy asked whether the system should correct \(X\)-dominated or
\(Z\)-dominated noise. That was useful as a cautionary first scan, but it is
not the hardware endpoint. A hardware controller should first be judged on a
stricter question:

> can adaptive likelihood updates improve the same stored logical bit/qubit
> relative to the best fixed and static-tailored decoder?

The simulator propagates the exact 8-state diagonal Pauli channel. The
correctable sector \(P\) is the Hamming-weight 0 or 1 sector; the logical
failure sector \(Q\) is Hamming-weight 2 or 3. For each implemented correction
round it computes the classical diagonal analogues of

$$
q^*=\lambda_{\max}(QE_QQ|_{\operatorname{ran}Q}),
$$

and

$$
\eta^*=\lambda_{\max}(PE_QP|_{\operatorname{ran}P}),
$$

then reports the worst observed alignment floor

$$
\frac{\eta^*}{1-q^*}.
$$

This does not prove a hardware advantage. It gives the project a clean first
cycle-map scaffold that can be replaced by real calibration data or a real
syndrome-extraction circuit.

The first default scan is deliberately cautionary. On a 25 by 25 grid over
hardware anisotropy and drift rate, adaptive decoding wins only 8 grid points.
The maximum adaptive improvement is

$$
\log_{10}(e_{\mathrm{static}}/e_{\mathrm{adaptive}})=0.069
$$

at anisotropy \(1.800\) and drift \(0.667\). The uniform fixed decoder wins 600
grid points, and the static-tailored decoder wins 17. This is not a failure of
the hardware program; it is the correct discipline. Adaptation is only valuable
where the cost of stale calibration exceeds the cost of updating.

The contraction diagnostic is also intentionally severe in this first model:
with \(Q\) defined as the majority-failure sector, the worst-round \(q^*\) can
sit close to one. That means the current 3-bit memory is not an active
contraction protocol for already-failed logical sectors. The next hardware
model should either compute the cycle map on a proper leakage/alignment sector
or move to a code/decoder where recovery genuinely contracts the relevant
misalignment subspace.

### 4.1 H1 Replay Scaffold

The first hardware-data replay scaffold is now in place:
`simulations/hardware_adaptive_decoder/hardware_replay_decoder.py`. The input
trace has one row per correction round. The reconstructed physical channel is
recorded as

$$
(p_0(t),p_1(t),p_2(t),p_m(t)),
$$

while the controller-visible calibration record is recorded separately as

$$
(\hat p_0(t),\hat p_1(t),\hat p_2(t),\hat p_m(t)).
$$

This separation matters. Offline replay may use the best reconstructed channel
to audit the logical map, but the adaptive policy is only allowed to see the
calibration/syndrome record. The policy therefore cannot win by reading the
hidden physical truth.

The default seeded replay is cautionary but useful. Over 96 rounds, the fixed
uniform decoder remains best with logical error `0.15504`; stale static
tailoring fails under drift with logical error `0.38631`; gated adaptive replay
updates 4 times and improves the stale tailored decoder to `0.17826`; and the
overactive decoder updates every round and falls to `0.21512`. The average
single-round syndrome information in the trace is
\(I(E;S)=0.22624\) bits.

This does not establish an adaptive advantage, because adaptive replay still
loses to the fixed uniform decoder on the example trace. Its value is stricter:
real hardware logs can now be replayed through the same acceptance test without
changing the protected logical channel.

### 4.2 H2 Circuit-Level Syndrome Extraction

The first circuit-level scaffold is now in place:
`simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`. It
still protects the same 3-qubit repetition logical memory, but it no longer
treats each round as a single diagonal data-error layer. Each round explicitly
models two ancilla parity checks,

$$
d_0d_1,\qquad d_1d_2,
$$

with preparation error, data idling, data idle phase faults, data-gate flips,
data-gate phase faults, ancilla-gate flips, correlated data-ancilla faults,
correlated phase faults, crosstalk on the nonparticipating data qubit,
measurement error, leakage-like random measurement records, correction failure,
and correction-induced phase faults. The decoder receives only compressed
calibration likelihoods. The expanded circuit fault columns are reserved for
offline logical-channel and record audits.

The default H2 trace is a seeded circuit-level stress test. It is deliberately
not a hardware claim. Over 96 rounds, the gated adaptive decoder updates 4
times and achieves logical error `0.45452`; the fixed uniform decoder gives
`0.46772`; stale static tailoring gives `0.47317`; and overactive every-round
updating gives `0.46064`. The adaptive improvement over the best fixed/static
baseline is modest:

$$
\log_{10}(e_{\mathrm{static}}/e_{\mathrm{adaptive}})=0.012.
$$

The process audit now confirms that this is a logical-channel statement rather
than a single-state probe. For the adaptive run, the induced logical
codeword-transition rates are symmetric to numerical precision:

$$
p_{0\to 1}=p_{1\to 0}=0.45452,
$$

with asymmetry zero to reported precision. The corresponding bit-flip-channel PTM
has

$$
R_{XX}=1,\qquad R_{YY}=R_{ZZ}=0.09096,
$$

and terminal coherent information \(I_c=0.00598\) bits. Averaging over the
final four-round calibration phase window gives logical error `0.45411` and
coherent information `0.00609` bits.

The Pauli-frame audit is stricter. The same adaptive run has logical Pauli
probabilities

$$
(p_I,p_X,p_Y,p_Z)=(0.27373,0.22809,0.22643,0.27174),
$$

so the actual diagonal logical PTM is

$$
R_{XX}=0.00365,\qquad R_{YY}=0.00033,\qquad R_{ZZ}=0.09096,
$$

with Pauli-channel entanglement fidelity `0.27373` and coherent information
\(I_c=-0.99401\) bits. The bit-flip consistency error is numerical
(`4.4e-16`), meaning the old bit-flip metric was internally correct but
incomplete. The repetition scaffold can therefore demonstrate adaptive
syndrome interpretation in one component while failing as a full qubit memory.

The new schedule-phase audit is stricter than the terminal phase-window check.
For generated H2 traces, the script replays all four calibration-period
offsets while holding the physical noise trajectory fixed. The adaptive mean
logical error across offsets is `0.45761`, with a phase span of `0.00867` and
mean adaptive benefit `0.010` log10. Thus the default adaptive win is not only
a final-tick artifact, but it is still schedule-sensitive and should be treated
as a modest stress-test result rather than a robust hardware claim. In the
Pauli-frame schedule scan, the adaptive mean logical-Pauli error is `0.72781`
and the mean Pauli coherent information is `-0.99476` bits, again marking the
current repetition scaffold as a diagnostic ladder rung rather than an
adequate full logical-qubit architecture.

The record audit is more important than the small advantage. The average
circuit-level syndrome information is

$$
I(\mathrm{error};\mathrm{syndrome})=0.11486\ \mathrm{bits},
$$

while the conditional controller-record leakage is numerically zero,

$$
I(\mathrm{logical};\mathrm{record}\mid \mathrm{error})
  \approx 2.7\times 10^{-17}\ \mathrm{bits}.
$$

This is the first executable instance of the hardware acceptance condition in
which adaptation is tested after overhead and the controller record is checked
for logical noncentrality.

## 5. Hardware Acceptance Criteria

A result becomes hardware-relevant only if it passes all of the following
checks.

1. The adaptive protocol is compared against fixed, static-tailored, and
   overactive baselines.
2. The logical channel is fixed; the protocol does not win by changing what
   information is being protected.
3. The improvement is reported after update overhead, latency, measurement
   error, and extra idle exposure.
4. The result is stated as a logical-channel improvement, not as branch
   population, GHZ support, or state-preparation survival.
5. The adaptive policy does not improve stationary noise beyond statistical
   noise; otherwise the baseline is unfair or overhead is missing.
6. A contraction diagnostic is computed for the implemented cycle whenever a
   finite channel map is available.
7. The controller/syndrome record is audited for logical-state information
   whenever the implemented cycle exposes such a record; the recovery should be
   syndrome-informative and logically noncentral.

The risk-audit harness in `simulations/risky_qec_claims/` adds four refinements
to these criteria.

First, do not use generic positive logical/noise/environment interaction
information as a resource criterion. It can be pure logical leakage. The safe
audit separates syndrome information from logical privacy:

$$
I(E;S)>0,\qquad I(R_L;E_{\mathrm{env}}\mid S)\approx 0.
$$

Second, single-state probes are insufficient. In the repetition-code toy,
logical bit-flip failures leave \(|+_L\rangle\) invariant, so a branch-coherence
score can look perfect while the identity logical channel is not. Hardware
reports should include a logical process metric such as a logical Pauli
transfer matrix, entanglement fidelity, coherent information, or a small
tomographic reconstruction.

Third, correction-schedule scans should be robust to terminal-time artifacts.
If a correction interval lands exactly on the final measurement tick, it can
look artificially good relative to a neighboring interval. Report either a
phase-averaged stopping time, a steady-state per-cycle channel, or both.

Fourth, highly coupled or noisy subsystems are calibration/decoder/gauge
priorities, not automatically good places to store or start logical
computation. The policy question is whether their syndrome information is
trackable and useful after overhead, not whether noise alone is high.

## 6. Roadmap

**H0: fixed-code adaptive decoder.** Complete the current repetition-code
likelihood-update benchmark and use it to identify the drift/anisotropy region
where adaptive decoding beats static tailoring.

**H1: hardware-data replay.** Initial trace format and seeded replay harness
exist. The remaining H1 step is to replace the synthetic trace with measured
syndrome-event or calibration logs from a real backend. The protocol remains
offline at this stage: replay the data through fixed, static, adaptive, and
overactive policies.

**H2: circuit-level simulator.** First scaffold exists. It adds explicit
ancilla preparation, CNOT-style parity extraction, measurement error,
leakage-like random records, idle errors, crosstalk, correlated faults, and
feedback error. It now computes the cumulative induced logical bit-flip
process, a Pauli-frame logical-channel audit, coherent information, and a
terminal phase-window average plus a calibration schedule-phase replay audit.
The remaining H2 upgrade is to move from this repetition-code Pauli-frame audit
to a phase-protecting stabilizer/subsystem-code circuit and then compute true
steady-state per-cycle maps.

**H3: small patch.** Move from a repetition memory to a small surface-code,
heavy-hex, Bacon-Shor, or subsystem-code patch where adaptation updates decoder
likelihoods, gauge choice, schedule, or local Clifford frame while preserving
the same logical channel.

**H4: live hardware loop.** Run the policy online: estimate, update, and decode
inside the same experimental campaign. The publication-grade claim is an
adaptive crossover curve: static tailoring wins when drift is negligible,
adaptive tailoring wins when drift is trackable, and overactive adaptation
fails when overhead dominates.

## 7. Claim Boundary

This bridge changes the QEC subgoal and supplies the technical laboratory for
the ACP quantum-gravity derivation, but it does not lower the evidential
standard. The current state is a hardware-facing scaffold, not a hardware
result. The next valid QEC claim must be phrased as:

> under a specified drifting hardware-noise model or measured syndrome stream,
> adaptive decoder/gauge/schedule updates improve the induced logical channel
> over fixed and static-tailored baselines after overhead.

Anything stronger belongs in the open-problem column until the corresponding
cycle map or hardware data exists.
