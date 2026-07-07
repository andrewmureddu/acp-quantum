# STATUS

**Last updated:** 2026-07-07
**Active paper:** `paper/acp_main_v10.md` (internal masthead: "WORKING DRAFT — v0.9")
**Active ACP Quantum focus:** deriving quantum gravity from ACP: `bridges/quantum_gravity_derivation_program.md` + `proofs/semiclassical_collapse_failure.md` + `bridges/relational_observable_macrostate_kernel.md` + `bridges/cosmic_coordination_floor.md` + `bridges/singularity_inadmissibility.md` + `bridges/dark_constraint_quantum_gravity.md` + `bridges/quantum_gravity_convergence_map.md`
**Active QEC technical engine:** hardware-level adaptive syndrome alignment: `bridges/hardware_adaptive_alignment.md` + `simulations/hardware_adaptive_decoder/` (H0 grid scan + H1 trace replay + H2 circuit-level syndrome extraction / Pauli-frame logical-channel audit / schedule-phase audit) + `bridges/adaptive_syndrome_alignment.md` + `bridges/sacr_contraction_calibration.md`
**Active civil-systems bridge:** restraint ethics / conditional-leakage record channels: `bridges/restraint_ethics.md` + `simulations/restraint_ethics/`
**Active cross-domain QEC bridge:** otherness-preserving recovery: `bridges/otherness_preserving_recovery.md` + `simulations/otherness_preserving_recovery/`
**Active meta-theoretic bridge:** reality-reflective mathematics / admissible model-world coupling / uncertainty allocation: `bridges/reality_reflective_mathematics.md`
**Active self-limiting universality bridge:** protected forgetting / final-theory non-totalization: `bridges/self_limiting_universality.md` + `simulations/self_limiting_universality/`
**Active turbulence bridge:** scale-resolved turbulence productive interval / admissible closure / Kolmogorov cascade as uncertainty allocation: `bridges/turbulence_productive_interval.md`
**Active operational-time bridge:** operational-time relativity / proper productive intervals: `bridges/operational_time_relativity.md`
**Active special-cases catalog:** `special_cases/acp_special_cases_v03.md`
**Active integrity audit:** `audits/integrity_audit_v10.md`

---

## Current Research Focus

ACP Quantum is now organized around **deriving quantum gravity from ACP**. The project's working quantum-gravity thesis is:

> quantum gravity is the persistence-forced completion of classical spacetime: admissible gravitational dynamics must replace singular collapse with relational, finite-record, boundary-decodable quantum channels that preserve nonzero future entropy while protecting interior logical information until the appropriate decoding scale.

The current derivation program is anchored in
`bridges/quantum_gravity_derivation_program.md`. The honest status is:
ACP/Schur already proves that singular internal blocks are inadmissible for
persistent boundary laws; ACP structurally requires decodable redistribution
before a coordination floor is breached; the open physics task is proving that
the required microscopic completion is exactly quantum gravity, with the right
relational observable algebra, boundary records, and classical limit.

The Stage 2 theorem of the derivation ladder is now proven at the finite
relational-kernel level. `proofs/semiclassical_collapse_failure.md` derives
the failing subset of a trapped collapse macrocell from explicit focusing
assumptions (NEC, trapped bins, Penrose incompleteness, fixed description,
relational clock compatibility) instead of assuming it, quantifies the
normalization failure
(\(Z^{\mathrm{adm}}_{\ell,\Delta}(m)=1-\mu_m(\tau_{\mathrm{fail}}\leq\Delta)\),
vanishing at finite \(\Delta^*\) via the focusing bound
\(\lambda^*\leq 2/\alpha\)), and proves a no-go theorem: no kernel
constructible from the classical description alone — naked pushforward, hard
exclusion, or terminal absorption — satisfies normalization, record balance,
and the future-entropy floor simultaneously. Corollary 1 makes horizon
formation a deferral with a semiclassical evaporation deadline; Corollary 2
derives the forced-completion requirements (mechanism change before floor
breach, normalization, boundary decodability). Imported classical-GR inputs
and referee seams (relational clock F5, trapped bin design F2, pointwise NEC,
extendible MGHDs) are labeled explicitly. The numerical companion
`simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py` verifies
the focusing bound on 400 NEC-respecting samples (zero violations of
\(2/\alpha\) or the tighter \(2/|\theta_0|\)), the monotone mass-loss curve
with \(Z(\Delta^*)=0\), and the hard-exclusion entropy collapse (3.617 bits to
0.000). The kernel skeleton itself remains
`bridges/relational_observable_macrostate_kernel.md`, and the macrocell toy in
`simulations/cosmic_coordination_floor/` still compares naked collapse, hard
exclusion, horizon transfer, and a schematic quantum-completion policy. The
next hard step is the completion half: instantiate candidate quantum-gravity
mechanisms as completion kernels and audit them against the six
candidate-mechanism tests.

The working gravitational targets are:

$$ I(\mathrm{geometry\ sector};R_{\partial}) > 0 $$

while

$$ I(\mathrm{interior\ microstate};R_{\partial}^{\mathrm{early}}) \approx 0 $$

and

$$ H_{\ell,\Delta}(m)\geq H_{\mathrm{floor}}(m;\ell,\partial R)>0 . $$

Noise-tailored quantum persistence remains the technical engine and finite
laboratory for the derivation. The QEC prototype thesis is:

> quantum persistence can be improved by matching logical encodings, syndrome extraction, and mitigation protocols to the biased, correlated, or symmetry-constrained structure of the physical noise, while suppressing logical information leakage to the environment.

The static QEC reviewable anchor is `bridges/quantum_noise_as_signal.md`. It
proves, for a two-qubit dephasing channel, that a symmetry-adapted
decoherence-free encoding preserves true coherence under fully collective
dephasing while an unadapted encoding decoheres exponentially under the same
coupling. The active dynamic anchor is now
`bridges/hardware_adaptive_alignment.md` plus
`simulations/hardware_adaptive_decoder/`. The QEC subgoal is hardware-level
implementation: fixed logical encodings, noisy syndrome streams, online noise
estimation, decoder/gauge/schedule updates, overhead accounting, and
logical-channel audits. In the gravitational lift, error sectors become
geometry sectors, syndromes become boundary records, and logical states become
protected interior degrees of freedom.

The first Shannon upgrade is now in place: the former proxy environmental-signal score in `bridges/quantum_noise_as_signal.md` has been replaced by a classical Gaussian environment-fragment model with explicit mutual information quantities:

$$ I(Q;Y_c) $$

and

$$ I(L_A;Y_c,Y_1,Y_2) $$

plus the corresponding unaligned leakage \(I(L_U;Y_c,Y_1,Y_2)\).

The first logical-channel upgrade is also now in place. The same two-qubit
dephasing model is reduced to the induced logical dephasing channel on the
aligned and unaligned encodings, with entanglement fidelity
\(F_e=(1+C)/2\) and coherent information
\(I_c=1-H_2((1+C)/2)\) recorded in the simulation outputs. The remaining
OP-15 target is a microscopic Stinespring/environment-state model with
conditional reference-environment leakage \(I(R_L;E_{\mathrm{env}}\mid S)\)
plus a recoverability or active-decoding bound.

The first explicit civil-systems bridge is now in place:
`bridges/restraint_ethics.md` plus `simulations/restraint_ethics/`. It treats
restraint ethics as a record-channel problem: institutions should learn enough
about public error sectors to correct harm while suppressing excess leakage
about protected agency states. The toy model tests
\(I(E;R)>0\), \(I(L;R\mid E)\approx 0\), and bounded monitoring burden. This
bridge is not part of the core proof chain, but it feeds a useful diagnostic
back into ACP Quantum: raw logical-environment mutual information should be
distinguished from conditional/excess leakage after syndrome information.

The otherness-preserving recovery bridge is now in place:
`bridges/otherness_preserving_recovery.md` plus
`simulations/otherness_preserving_recovery/`. It treats creator/simulator/god
language as a neutral asymmetric-controller model and anchors the idea in the
Knill-Laflamme condition \(PE_a^\dagger E_bP=c_{ab}P\): the corrector may
learn the error sector while remaining blind to the protected logical state.
The first toy repetition-code scan compares absent, restrained, and
centralizing recovery, showing that a centralizing controller can preserve
classical bit fidelity while destroying logical coherence.

The newest SACR / shadow-geometry intake is now translated into an operational
channel-calibration target rather than a standalone geometry claim. The bridge
`bridges/sacr_contraction_calibration.md` defines \(q^*\), \(\eta^*\), and
\(\eta^*/(1-q^*)\) directly from a finite CPTP cycle map. The toy harness in
`simulations/sacr_contraction_calibration/` verifies the calibration geometry
for a two-sector map and marks the reported 99.1% floor as the target
\(\eta^*/(1-q^*)\lesssim 9\times 10^{-3}\). The next serious OP-16 step is to
compute these quantities for a real syndrome-extraction/recovery cycle.

The first hardware-facing scaffold is now in place. `bridges/hardware_adaptive_alignment.md`
defines the device-stack target: collect calibration/syndrome data, estimate
noise structure, update a decoder/gauge/schedule only when expected benefit
exceeds overhead, and audit the induced logical channel. The executable
benchmark `simulations/hardware_adaptive_decoder/` keeps a 3-qubit repetition
code fixed and adapts only decoder likelihoods under drifting non-identically
distributed data-qubit errors with noisy syndrome measurements. The first scan
is cautionary but useful: adaptive decoding wins only 8 of 625 grid points,
with maximum benefit `0.069` log10 units. This is now the correct hardware
discipline: adaptation must beat fixed and static-tailored baselines without
changing the logical channel.

The first H1 replay interface is now also in place:
`simulations/hardware_adaptive_decoder/hardware_replay_decoder.py`. It defines
a per-round trace format separating reconstructed channel columns from
controller-visible calibration/syndrome columns, then replays fixed, static,
gated adaptive, overactive, and instant-rate decoder policies on the same
logical memory. The default seeded synthetic trace is again cautionary:
adaptive replay updates 4 times and improves stale static tailoring
(`0.38631` logical error) to `0.17826`, but the fixed uniform decoder remains
best at `0.15504`; overactive updating every round falls to `0.21512`. Average
single-round syndrome information in the trace is `0.22624` bits.

The first H2 circuit-level syndrome-extraction scaffold is now also in place:
`simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`. It
keeps the same 3-qubit repetition memory but expands each round into explicit
ancilla preparation, CNOT-style parity checks, idling, gate faults, measurement
error, phase faults, leakage-like random records, correlated faults, crosstalk,
and feedback error. The default seeded stress trace is again modest rather than
triumphal:
adaptive decoding updates 4 times and improves the best fixed/static baseline
from `0.46772` logical error to `0.45452`, while overactive updating every
round falls to `0.46064`. The circuit-level record audit reports
`0.11486` bits of average \(I(\mathrm{error};\mathrm{syndrome})\) and
approximately zero conditional controller leakage,
`2.7e-17` bits of \(I(\mathrm{logical};\mathrm{record}\mid\mathrm{error})\).
The H2 output now also reconstructs the cumulative induced logical bit-flip
process and propagates a 64-state data Pauli frame. The adaptive run has
symmetric logical transition rates `p01=p10=0.45452`, bit-flip PTM entries
`XX=1.00000` and `YY=ZZ=0.09096`, coherent information `0.00598` bits, and a
four-round terminal phase-window logical error of `0.45411`. The stricter
Pauli-frame audit reports
`(pI,pX,pY,pZ)=(0.27373,0.22809,0.22643,0.27174)`, actual diagonal PTM
`(XX,YY,ZZ)=(0.00365,0.00033,0.09096)`, entanglement fidelity `0.27373`, and
coherent information `-0.99401` bits. Thus the current repetition scaffold
shows an adaptive bit-flip gain while failing as a full logical-qubit memory.
The calibration schedule-phase audit replays all four offsets of the
calibration period; the adaptive mean logical error is `0.45761`, with span
`0.00867` and mean adaptive benefit `0.010` log10, while the Pauli-frame
schedule mean is `0.72781` logical-Pauli error and `-0.99476` bits of coherent
information.

A new risk-audit harness now lives at `simulations/risky_qec_claims/`. It
stress-tests four overstrong interpretations of the program: generic positive
logical/noise/environment synergy, "syndrome measurement is crystallization,"
"QEC is crystallization" without a monitoring-cost model, and "start
computation on the noisiest qubit." The result is clarifying: positive logical
synergy can be pure leakage; clean syndrome information can have zero logical
synergy; ideal syndrome recovery preserves coherence in the repetition-code
toy; and noisiest subsystems should be prioritized for calibration/decoder
attention, not for bare logical storage.

A second pass over the same output added an important methodological
refinement: single-state coherence probes can hide logical-channel errors. In
the repetition-code audit, ideal syndrome recovery leaves \(|+_L\rangle\)
coherence at `1.000000`, but the recovered identity-channel entanglement
fidelity is `0.981824` because logical bit-flip failures remain. The hardware
bridge now requires process metrics such as a logical PTM, entanglement
fidelity, coherent information, or small process reconstruction, and asks
future schedule scans to avoid terminal-time divisibility artifacts by using
phase-averaged or steady-state cycle metrics.

## Where the Parent Paper Stands

v10 includes, relative to what `memory.md` (legacy) describes as the v09 state:

- **A.20 Restraint-Power Theorem** + **Heisenberg uncertainty principle as the quantum-scale instantiation** of the coordination floor for a two-MASA operator-algebra partition. This is a substantial new result not reflected in the legacy memory file.
- The Price / Fisher reduction (A.19) is fully integrated.
- Ten testable predictions are stated with experimental protocols and falsification criteria (Section 6 + Appendix A.16).
- Quantitative lower bounds on the drift rate for non-Gaussian systems (A.17).

The full result inventory, as of v10:

| # | Result | Where |
|---|---|---|
| 1–5 | Core proof chain (ACP statement, CDT, compounding lemma, Claim A.3 interventional, induction to k mechanisms) | `paper/` + `proofs/` |
| 6–10 | A.11–A.15: five reductions (Friston, Zurek, Bergstrom–Lachmann, Prigogine, Kauffman) | `reductions/` |
| 11 | A.16 empirical predictions (10 predictions, 3 novel from unification) | `bridges/empirical_predictions.md` |
| 12 | A.17 non-Gaussian bounds (non-Gaussian systems crystallize *faster* than Gaussian — Gaussian is the conservative lower bound) | `bridges/non_gaussian_bounds.md` |
| 13 | A.18 multiscale RG (C/D asymmetry, productive interval as RG-invariant subset) | `reductions/multiscale_rg.md` |
| 14 | A.19 Price / Fisher (selection = crystallization drift; Fisher's theorem = CDT applied to fitness space) | `reductions/price_equation.md` |
| 15 | A.20 Restraint-Power + Coordination Conservation; Heisenberg as special case | `bridges/restraint_power.md` + `bridges/syndrome_coordination.md` + `bridges/coordination_neutrality.md` |
| 16 | Schur complement bridge — four identifications unifying thermodynamic (ACP) and algebraic (Schur) registers; Heisenberg connection reconciled with A.20 as a reduction for non-commutative two-MASA partitions | `bridges/schur_complement.md` |
| 17 | Quantum noise-tailoring bridge — correlated dephasing as exploitable channel structure; DFS coherence invariant under collective noise | `bridges/quantum_noise_as_signal.md` + `simulations/noise_as_signal/` |
| 18 | Hardware adaptive-alignment bridge — fixed-code adaptive decoder scaffold with noisy syndrome measurements, overhead, logical-channel output, contraction diagnostics, and H2 Pauli-frame logical-process / schedule-phase audits | `bridges/hardware_adaptive_alignment.md` + `simulations/hardware_adaptive_decoder/` |

## Active fronts

**1. ACP quantum-gravity derivation program.** This is now the primary ACP Quantum front. The target is explicit: derive quantum gravity as the persistence-forced completion of classical spacetime. The roadmap is `bridges/quantum_gravity_derivation_program.md`, supported by `bridges/relational_observable_macrostate_kernel.md`, `bridges/cosmic_coordination_floor.md`, `bridges/singularity_inadmissibility.md`, `bridges/dark_constraint_quantum_gravity.md`, and `bridges/quantum_gravity_convergence_map.md`. The Stage 2 collapse failure theorem is now proven: `proofs/semiclassical_collapse_failure.md` (no-go over classical kernel constructions, horizon-deferral deadline, forced-completion corollary), with numerical verification in `simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py`. The next serious step is instantiating candidate completion kernels (holographic/QEC, loop/effective bounce, asymptotic-safety, fuzzball) and auditing them against the six candidate-mechanism tests; theorem refinements (averaged/quantum focusing conditions, OP-29 clock covariance) are secondary. *(Priority: highest.)*

**2. Hardware-level adaptive syndrome alignment as QEC laboratory.** The QEC program remains the technical engine for the quantum-gravity derivation. The device-facing target is a fixed logical memory, noisy syndrome stream, online noise estimation, decoder/gauge/schedule updates, explicit overhead, and logical-channel audits. The current scaffold is `bridges/hardware_adaptive_alignment.md` plus `simulations/hardware_adaptive_decoder/`; H0, H1, and an H2 circuit-level syndrome-extraction scaffold with bit-flip logical-PTM, Pauli-frame logical-channel metrics, terminal phase-window metrics, and calibration schedule-phase replay are in place. The next step is measured backend-log replay or moving H2 from the repetition-code Pauli audit to a phase-protecting stabilizer/subsystem-code circuit with true steady-state per-cycle maps. *(Priority: high.)*

**3. Active noise-adapted feedback model.** The current `noise_as_signal` note is static channel geometry: DFS-adapted versus unadapted encoding. Next step is an active protocol that characterizes correlated noise, selects or rotates into the corresponding encoding/gauge, and checks true coherence rather than branch population. This feeds the gravitational lift from error/syndrome/logical separation to geometry-record/interior separation. *(Priority: high.)*

**4. QEC productive interval.** Continue the 3-qubit repetition-code work by comparing ideal syndrome extraction, costly syndrome extraction, and structured-noise alignment. Goal: formalize when correction prevents dissolution and when monitoring induces crystallization. *(Priority: high.)*

**5. Parent-paper maintenance.** The v10 integrity audit is complete. Remaining cleanup before any hypothetical submission: remove working-draft masthead/version notes, convert internal open-problem prose into submission-style limitations, and decide how much conjectural A.20 physical outlook belongs in the main draft versus companion notes. *(Priority: medium.)*

**6. Heisenberg / A.20 consequences.** A.20 recovers Heisenberg as a special case of the coordination floor once a non-commutative two-MASA partition is specified. This remains important because a stronger operator-algebraic version may connect the quantum-kinematics and quantum-gravity derivation tracks. *(Priority: exploratory.)*

**7. Quantum foundations from ACP.** `bridges/born_rule_from_acp.md`, `bridges/unitary_evolution_from_acp.md`, `bridges/tensor_product_from_acp.md`, and `bridges/measurement_formalism_from_acp.md` now prove the conditional local quantum-kinematics package given Hilbert structure. The remaining task is to derive the Hilbert branch geometry itself and reconnect it to relational gravitational observables. *(Priority: exploratory but strategically important.)*

**8. Collapse/timekeeping bridge: quantum braiding.** `bridges/quantum_braiding_timekeeping.md` treats collapse operationally as a clocking event in a quantum instrument/feedback process. This remains adjacent to OP-21/OP-22 and may help state how boundary records become time in the quantum-gravity derivation. *(Priority: exploratory.)*

**9. Meta-theoretic coherence / admissible mathematics.** `bridges/reality_reflective_mathematics.md` now matters directly to quantum gravity because admissible mathematical descriptions must have finite observables, normalizable record channels, nondegenerate continuation, and structured uncertainty allocation. This is the meta-theoretic shell of the derivation program. *(Priority: supporting.)*

**10. Operator-level CN / three-stroke persistence engine.** `bridges/three_stroke_persistence_engine.md` remains an exploratory companion to `bridges/coordination_neutrality.md`, relevant to OP-7 but not on the critical path until the relational macrostate kernel is defined. *(Priority: lower.)*

**11. Restraint ethics / civil record channels.** `bridges/restraint_ethics.md`
formalizes Andrew's "self-restraint as load-bearing structure" insight as a
civilizational bridge. The central diagnostic is syndrome-selective governance:
\(I(E;R)>0\) for public error correction while
\(I(L;R\mid E)\approx 0\) for protected agency/logical-state privacy, with
bounded record burden. `simulations/restraint_ethics/` gives the first toy
test and shows the expected interval between no-record abandonment and
high-leakage/high-burden capture. This front is exploratory but strategically
important because it feeds a conditional-leakage diagnostic back into OP-15.
*(Priority: exploratory, cross-domain.)*

**12. Otherness-preserving recovery.** `bridges/otherness_preserving_recovery.md`
formalizes the simulation/creator thought experiment as an asymmetric
controller problem. The key quantum anchor is Knill-Laflamme: a recovery
apparatus is legitimate precisely when it learns syndrome/error structure but
not the logical state. `simulations/otherness_preserving_recovery/` gives a
first repetition-code toy where restrained syndrome recovery preserves
coherence, while centralizing logical-branch measurement preserves classical
bit fidelity but collapses the protected superposition. This is now the bridge
between the ethics work and the hardware QEC audit. *(Priority: exploratory,
but directly useful for OP-15/OP-23.)*

**13. Turbulence as admissible closure.** `bridges/turbulence_productive_interval.md`
upgrades the old Navier-Stokes special-case mapping using the new
reality-reflective-mathematics criterion. The key correction is scale-resolved:
fully developed turbulence is not automatically dissolution; inertial-range
turbulence remains productive when finite records decode energy flux and
coherent structures. The newest refinement treats the scale-local Reynolds
number and Kolmogorov cascade as the fluid example of uncertainty allocation
across scales: the optimized object is \(N(k)\), not a scalar noise level, and
the slope of the spectrum is the fingerprint of the persistence-maximizing
solution under the domain's constraints. The next target is a DNS or shell-model
diagnostic for \(H_\ell\), \(I(\Pi_\ell;R_\ell)\), structured innovation
\(N_\ell,S_\ell^{\mathrm{innov}}\), the spectrum \(N(k)\), future predictive
information, and interaction-information excess. *(Priority: exploratory,
OP-27.)*

**14. Operational-time relativity.** `bridges/operational_time_relativity.md`
formalizes a bridge that was implicit in the core theorem chain: ACP quantities
must be stated in the system's own clock of distinguishable verification steps,
not in an arbitrary external tempo. The bridge defines candidate
reparameterization laws, identifies invariants such as boundary membership,
\(C>L\delta_v\), per-cycle information balances, \(q^*\), and
\(\eta^*/(1-q^*)\), and defines a proper productive interval as a connected
segment of operational time with finite tempo, two-boundary separation,
capacity-load margin, memory with innovation, and record selectivity where a
controller/environment is present. This creates a real new formal target:
cross-system covariance when two systems have different operational tempos and
non-identical macrostate partitions. *(Priority: exploratory, OP-29.)*

## Open problems

Canonical tracker: `OPEN_PROBLEMS.md`. Headline items:

- **OP-1: Quantitative erosion constant** (named "OP-new-2" in legacy memory). Channel Erosion (A.10) gives the rate is positive; we don't have a sharp numerical bound in general.
- **OP-2: Coherence crisis transient dynamics.** What happens *during* the regime change when one mechanism erodes another?
- **OP-3 through OP-5: Schur complement bridge open problems.** Three listed at the bottom of `bridges/schur_complement.md`: precision-matrix regularity, rank-reduction dynamics, and anti-crystallization as rank restoration. The Heisenberg reconciliation formerly tracked as OP-6 is resolved; the residual first-principles quantum-kinematics problem is tracked as OP-RP-5 in `bridges/restraint_power.md`.
- **OP-7: Coordination neutrality under tree composition.** Named in `bridges/coordination_neutrality.md`. The bridge family (exp / log operators — cf. Odrzywolek's eml in `references/`) is CN pairwise but may fail joint-inversion invariance under composition. `bridges/three_stroke_persistence_engine.md` is an OP-7-adjacent exploratory draft; its composition and simulation claims remain provisional.
- **OP-14: Quantum productive-interval simulation calibration.** First toy sim exists; next step is replacing proxy scores with channel-native quantities (trace-distance contraction, coherent information, mutual information to environment fragments, entanglement-breaking threshold, measurement-induced transition diagnostics).
- **OP-15: Shannon form of noise-as-signal.** Partially upgraded: `bridges/quantum_noise_as_signal.md` now uses explicit classical environment-fragment mutual information and induced logical-channel entanglement fidelity / coherent information. Remaining work is the full microscopic environment-state version and recoverability / active decoding.
- **OP-16: Adaptive syndrome-space alignment under drifting structured noise.** Partial+++: first bridge, axis-switching toy, fixed-code adaptive-decoder scaffold, H1 trace replay harness, H2 circuit-level syndrome-extraction scaffold with bit-flip logical-PTM / Pauli-frame logical-channel / phase-window / schedule-phase metrics, and finite-cycle contraction calibration harness exist. Next step is improving the hardware scaffold toward measured backend replay or decoder-likelihood, gauge, or schedule adaptation inside a phase-protecting stabilizer/subsystem-code circuit while computing \(q^*\), \(\eta^*\), and the alignment floor for a real syndrome-extraction/recovery map.
- **OP-17: Dark constraints as quantum-gravity syndrome information.** Partial+: bridge seed, ray-count mirror-room simulation, and wave-interference dark-fringe simulation exist; next step is a weak-metric/lensing null-record upgrade that feeds the derivation program's boundary-record stage.
- **OP-18: Singularity inadmissibility and horizon regularization.** Partial++: ACP/Schur criterion, gravitational bridge note, finite macrocell collapse toy, OP-20 kernel skeleton, and now the proven semiclassical collapse failure theorem (`proofs/semiclassical_collapse_failure.md`); next steps are averaged/quantum focusing conditions and the OP-29 clock transformation.
- **OP-19: ACP derivation of quantum gravity / cosmic coordination floor.** Partial+++: derivation roadmap, program bridge, macrocell-vector toy model, relational macrostate-kernel skeleton, and the Stage 2 theorem (quantitative normalization failure, no-go over classical kernels, horizon deadline, forced completion) now exist; next step is candidate completion kernels.
- **OP-20: Relational observable macrostate kernel.** Partial++: `bridges/relational_observable_macrostate_kernel.md` defines the finite relational observable algebra, macrocell partition, quantum/channel kernel, classical pushforward kernel, Schur-block reading, and boundary-information diagnostics; the classical-collapse failure proposition is superseded by the proven theorem; `simulations/cosmic_coordination_floor/` instantiates the toy macrocell vector, the candidate policy comparison, and the theorem's numerical checks. Next step is candidate-mechanism audit beyond the schematic toy.
- **OP-21: First-principles Hilbert branch structure / quantum kinematics from ACP.** Partial+++: the conditional local package now includes branch weights, closed unitary flow, tensor-product independent composition, and POVM/projective measurement structure; the remaining task is to derive that kinematics from ACP alone.
- **OP-22: Quantum braiding and collapse as internal timekeeping.** Partial: seed bridge note exists; next step is a monitored-qubit feedback simulation with record entropy, memory, leakage, and clock-regularity diagnostics.
- **OP-23: Hardware implementation ladder for adaptive syndrome alignment.** Open/partial: roadmap, first fixed-code adaptive decoder scaffold, H1 trace replay interface, and H2 circuit-level syndrome-extraction interface with bit-flip logical-process, Pauli-frame logical-channel, and schedule-phase audits exist; next step is measured hardware-data replay, a phase-protecting stabilizer/subsystem patch, steady-state cycle maps, and live hardware loop.
- **OP-24: Restraint ethics and conditional-leakage civil systems.** Open/partial: first bridge and binary Gaussian record-channel simulation exist; next step is domain-native observables and empirical/agent-based institutional models.
- **OP-25: Otherness-preserving recovery and controller noncentrality.** Open/partial: first bridge and repetition-code centrality simulation exist; next step is a microscopic Stinespring/decoupling audit and controller-record metrics for circuit-level QEC.
- **OP-26: Reality-reflective mathematics and admissible model-world coupling.** Open/partial: first bridge note exists and now includes structured innovation quantities plus an uncertainty-allocation functional \(\mathcal P_t[\mathcal N]\); next step is categorical/invariant formalization of admissible descriptions and quantitative conditions for \(\mathcal N_t^*\).
- **OP-27: Turbulence productive interval and admissible closure.** Open/partial: first bridge note exists and now includes scale-local Reynolds / Kolmogorov-cascade uncertainty allocation plus spectral-allocation Conjecture T-2; next step is a DNS or shell-model scale diagnostic for inertial-range productive scores, spectra, and closure failure modes.
- **OP-28: Self-limiting universality and protected forgetting.** Open/partial+: first bridge note and first finite record-channel toy simulation exist; next step is formalizing protected forgetting as a bounded-leakage morphism and deriving a downstream semantic-field bound for final-scope theories.
- **OP-29: Operational-time relativity and proper productive intervals.** Open/partial: first bridge note exists; next step is proving the operational-time covariance theorem for systems with different tempos, coarse-grainings, and record channels.

## Changelog

### 2026-07-07 — semiclassical collapse failure theorem
- Added `proofs/semiclassical_collapse_failure.md`, the Stage 2 theorem of the
  quantum-gravity derivation ladder. It strengthens Proposition 2 of the OP-20
  kernel bridge in four ways: the failing subset of a trapped collapse
  macrocell is derived from explicit focusing assumptions (F1–F6: NEC,
  trapped bins, Penrose causality inputs, fixed description, relational clock
  compatibility, nondegenerate cell measure) instead of assumed; the
  normalization failure is quantitative, with retained mass
  \(Z^{\mathrm{adm}}_{\ell,\Delta}(m)=1-\mu_m(\tau_{\mathrm{fail}}\leq\Delta)\)
  vanishing at finite \(\Delta^*\) controlled by the focusing bound
  \(\lambda^*\leq 2/\alpha\); hard exclusion is shown to violate record
  balance with divergent discarded coordination \(-\log Z\); and an
  exhaustiveness lemma upgrades the trichotomy to a no-go theorem over every
  kernel constructible from the classical description.
- Corollary 1 formalizes horizon deferral: an admissible exterior
  regularization whose permanent-horizon idealization is removed by
  semiclassical evaporation, so the trichotomy reappears in the exterior
  algebra at the decoding scale. Corollary 2 derives the forced-completion
  requirements (mechanism change before floor breach, normalization,
  boundary decodability) from the theorem plus the floor and record-balance
  axioms.
- Imported classical-GR inputs (Raychaudhuri comparison, Penrose theorem,
  trapped-surface existence/stability) and referee seams (F5 clock, F2 bin
  design, pointwise NEC, extendible MGHDs) are labeled explicitly.
- Added `simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py`:
  400 NEC-respecting Raychaudhuri integrations with zero violations of the
  \(2/\alpha\) bound (or the tighter \(2/|\theta_0|\)), a monotone mass-loss
  curve with \(Z(\Delta^*)=0\), and hard-exclusion entropy collapse from
  3.617 bits to 0.000; the absorption channel has exactly zero future entropy.
- Updated `bridges/relational_observable_macrostate_kernel.md`,
  `bridges/quantum_gravity_derivation_program.md`,
  `bridges/cosmic_coordination_floor.md`,
  `bridges/singularity_inadmissibility.md`, the simulation README, and
  OP-18/OP-19/OP-20.
- Session log: `sessions/2026-07-07_semiclassical_collapse_failure.md`.

### 2026-05-15 — CC0 license added
- Added root `LICENSE` with the CC0 1.0 Universal legal code.
- Updated `README.md` to identify the repository license as CC0 1.0
  Universal.
- Session log: `sessions/2026-05-15_cc0_license.md`.

### 2026-05-15 — GitHub repository bootstrap
- Initialized this workspace as a git repository on `main`.
- Added `.gitignore` to exclude local runtime clutter: `.venv/`, macOS metadata,
  Python caches, Matplotlib font caches, scratch files, and local Cowork
  `metadata.json`.
- Created the private GitHub repository `andrewmureddu/acp-quantum` and pushed
  the initial ACP Quantum snapshot.
- Session log: `sessions/2026-05-15_github_repository_bootstrap.md`.

### 2026-05-14 — macrocell collapse kernel toy
- Upgraded `simulations/cosmic_coordination_floor/cosmic_coordination_floor.py`
  from a one-coordinate collapse toy to a finite relational macrocell model
  with bins for boundary mass/spin/charge, compactness, expansion, curvature,
  boundary area, structured null records, and outgoing radiation records.
- Added the fourth policy required by the OP-20 bridge: `quantum_completion`,
  a schematic candidate completion that triggers before the hard floor,
  preserves normalization, emits geometry-sector records, bounds early
  protected-interior leakage, and releases late decodable information.
- Regenerated `outputs/cosmic_coordination_floor_timeseries.csv`,
  `outputs/cosmic_coordination_floor_summary.csv`, and
  `outputs/cosmic_coordination_floor.svg`. The default summary now separates
  naked collapse (mass/privacy failure), hard exclusion (future-entropy
  crystallization with no late decoding), horizon transfer, and quantum
  completion.
- Updated `bridges/relational_observable_macrostate_kernel.md`,
  `bridges/cosmic_coordination_floor.md`,
  `bridges/quantum_gravity_derivation_program.md`, the simulation README, and
  OP-18 through OP-20.
- Session log: `sessions/2026-05-14_macrocell_collapse_kernel.md`.

### 2026-05-13 — relational observable macrostate kernel
- Added `bridges/relational_observable_macrostate_kernel.md`, closing the first
  OP-20 gap at the formal-object level.
- Defined finite relational observable algebras, macrocells
  \(m\in\mathcal M_\ell\), quantum/channel and classical-pushforward forms of
  \(P_{\ell,\Delta}(m'|m)\), and the diagnostics
  \(H_{\ell,\Delta}(m)\), \(I(G_\ell;R_{\partial})\),
  \(I(L_R;R_{\partial}^{\mathrm{early}}\mid G_\ell)\), and late
  boundary decodability.
- Added a modest classical-collapse failure proposition: classical collapse
  either loses normalization to inadmissible singular support, becomes a
  postselected hard-exclusion theory, or concentrates toward the zero-entropy
  floor.
- Updated `bridges/quantum_gravity_derivation_program.md`,
  `bridges/cosmic_coordination_floor.md`, `README.md`, `AGENTS.md`,
  `CLAUDE.md`, and OP-18 through OP-20.
- Session log: `sessions/2026-05-13_relational_macrostate_kernel.md`.

### 2026-05-10 — quantum-gravity derivation program promoted
- Promoted ACP Quantum's project focus from QEC-centered noise-tailored persistence
  to the explicit goal of deriving quantum gravity from ACP.
- Added `bridges/quantum_gravity_derivation_program.md`, stating the derivation
  ladder: admissibility, classical GR failure, required completion, relational
  observables, boundary decodability, protected interior information,
  holographic/QEC structure, and classical limit.
- Updated `AGENTS.md`, `CLAUDE.md`, and `README.md` so QEC is now framed as the
  technical engine/laboratory for the quantum-gravity derivation.
- Updated this status file and OP-17 through OP-20 to make the relational
  observable macrostate kernel the next highest-priority formal object.
- Session log: `sessions/2026-05-10_quantum_gravity_derivation_program.md`.

### 2026-05-10 — H2 Pauli-frame logical-channel audit
- Upgraded `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`
  so the H2 circuit-level scaffold propagates a 64-state data Pauli frame in
  parallel with the existing exact bit-flip process.
- Added generated trace columns for phase faults (`data_idle_z_*`,
  `data_gate_z_*`, `correlated_phase`, `data_crosstalk_z`, and
  `correction_phase_error`) and output columns for logical Pauli probabilities,
  actual diagonal PTM entries, Pauli-channel entanglement fidelity, Pauli
  coherent information, and bit-flip consistency.
- Regenerated the seeded H2 outputs. The adaptive bit-flip result is unchanged:
  logical error `0.45452`, bit-flip PTM `XX=1.00000`, `YY=ZZ=0.09096`, and
  adaptive benefit `0.012` log10.
- The new Pauli-frame audit is deliberately harsher:
  `(pI,pX,pY,pZ)=(0.27373,0.22809,0.22643,0.27174)`, actual PTM
  `(XX,YY,ZZ)=(0.00365,0.00033,0.09096)`, entanglement fidelity `0.27373`,
  and coherent information `-0.99401` bits. The bit-flip consistency error is
  numerical (`4.4e-16`), so the earlier bit-flip audit was correct but
  incomplete.
- Updated `bridges/hardware_adaptive_alignment.md`,
  `simulations/hardware_adaptive_decoder/README.md`, and OP-16/OP-23 to mark
  the current repetition scaffold as a diagnostic ladder rung, not a full
  logical-qubit memory.
- Session log: `sessions/2026-05-10_h2_pauli_frame_audit.md`.

### 2026-05-10 — operational-time relativity bridge
- Added `bridges/operational_time_relativity.md`, starting from the core
  paper's operational-time section and the Schur/QEC persistence inequalities.
- Defined operational tempo \(\nu_S=d\tau_S/dt\), candidate
  reparameterization laws for scalar quantities, rate densities, and
  verification horizons, and the invariant product \(L\delta_v\).
- Clarified the proper productive interval as an intrinsic interval of
  operational time with finite tempo, boundary separation, capacity-load
  margin, memory with innovation, and controller/environment record selectivity
  where applicable.
- Added OP-29 for the real theorem-level gap: cross-system covariance under
  different tempos, coarse-grainings, and record channels.
- Session log: `sessions/2026-05-10_operational_time_relativity.md`.

### 2026-05-09 — H2 schedule-phase audit
- Upgraded `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`
  so generated H2 traces can replay all offsets of the calibration schedule.
- Added `outputs/circuit_level_phase_scan_summary.csv` plus summary columns
  for schedule-phase mean, span, and adaptive-benefit robustness.
- Regenerated the seeded H2 outputs. The default adaptive run updates `4`
  times and has logical error `0.45452`, PTM `XX=1.00000`,
  `YY=ZZ=0.09096`, coherent information `0.00598` bits, and four-round
  phase-window logical error `0.45411`.
- The four-offset schedule-phase audit reports adaptive mean logical error
  `0.45761`, phase span `0.00867`, and mean adaptive benefit `0.010` log10.
- Updated `bridges/hardware_adaptive_alignment.md`,
  `simulations/hardware_adaptive_decoder/README.md`, and OP-16/OP-23 to
  record the new audit while keeping measured backend replay and full
  Pauli-frame/stabilizer PTM as the next hardware steps.
- Session log: `sessions/2026-05-09_h2_schedule_phase_audit.md`.

### 2026-05-06 — uncertainty allocation spectra
- Refined `bridges/reality_reflective_mathematics.md` from scalar "noise
  floor" language to uncertainty allocation across scales or record channels.
  The optimized object is now a function \(\mathcal N_t:\mathcal A\to
  \mathbb R_{\geq 0}\), with scalar \(n^*(t)\) retained only as the one-scale
  special case.
- Added the variational functional \(\mathcal P_t[\mathcal N]\), making the
  shape of the uncertainty spectrum the theory-bearing object.
- Refined `bridges/turbulence_productive_interval.md` so the Kolmogorov cascade
  is treated as uncertainty allocation \(N(k)\), not a scalar turbulence
  level. The K41 \(-5/3\) slope is framed as a constraint-specific fingerprint
  of the persistence-maximizing allocation.
- Added Conjecture T-2, the spectral allocation fingerprint: cascade-like
  persistent systems should exhibit spectra generated by the same variational
  form under different domain constraints, not a single universal exponent.
- Updated OP-26 and OP-27 accordingly.
- Session log: `sessions/2026-05-06_uncertainty_allocation_spectra.md`.

### 2026-05-06 — self-limiting universality
- Added `bridges/self_limiting_universality.md`, synthesizing generativity,
  reality-reflective admissibility, otherness-preserving recovery, and
  restraint-power into a final-theory constraint.
- Formalized "protected forgetting" as structural non-capture:
  \(I(X;R_C)>0\) while \(I(L;R_C\mid X)\leq\epsilon_L\), with structured
  innovation and nondegenerate continuation retained.
- Stated Conjecture 1, self-limiting universality: any final-scope theory that
  contains its own knowers must preserve a protected remainder in the
  downstream semantic partition.
- Stated Conjecture 2, maximal-compressor restraint: the strongest compressor
  or most concentrated subsystem must be first to reduce centrality by a
  decodable transfer or protected-forgetting operation.
- Added OP-28 for protected forgetting, downstream semantic-field bounds, and
  a categorical bounded-leakage formulation.
- Added `simulations/self_limiting_universality/`, a discrete record-channel
  toy with binary needed distinction \(X\), protected interior \(L\), and
  compressor record \(R_C\). The seeded run reports protected forgetting with
  \(I(X;R_C)=0.820\), \(I(L;R_C\mid X)=0.000\), internal score `0.399800`;
  total possession and noisy dissolution both score `0.000000`; pretended
  forgetting scores `0.399800` publicly but `0.000000` internally.
- Session log: `sessions/2026-05-06_self_limiting_universality.md`.

### 2026-05-06 — structured innovation floor
- Extended `bridges/reality_reflective_mathematics.md` with A7, a structured
  innovation floor for persistent/generative descriptions. The new quantities
  are \(N_t^{\mathcal F}=H(R_{t+\Delta}\mid Z_t)\) and
  \(S_t^{\mathcal F}=I(X_{t+\Delta};R_{t+\Delta}\mid Z_t)\), with the
  admissible condition
  \(0<S_t^{\mathcal F}\leq N_t^{\mathcal F}<H(R_{t+\Delta})\).
- Added an adaptive admissibility-floor score \(\mathcal P_t(n)\) and
  conjectural optimizer \(n^*(t)\), making explicit that the optimal noise or
  slack floor depends on distance from crystallization and dissolution.
- Extended `bridges/turbulence_productive_interval.md` with a Kolmogorov
  cascade / scale-local Reynolds reading: the cascade is a structured
  innovation channel, not mere waste or mere chaos.
- Updated `special_cases/acp_special_cases_v03.md` §5.3 so Richardson's cascade
  is described as crystallizing vortex concentration plus anti-crystallizing
  scale transfer and dissipation.
- Updated OP-26 and OP-27 with the new structured-innovation diagnostics.
- Session log: `sessions/2026-05-06_structured_innovation_floor.md`.

### 2026-05-06 — H2 logical-process audit
- Upgraded `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`
  so the H2 circuit-level scaffold reconstructs the cumulative induced
  logical bit-flip channel from the physical transition matrix.
- Added output columns for logical codeword transition rates, bit-flip
  asymmetry, symmetrized logical PTM entries, coherent information, and
  terminal phase-window averages.
- Regenerated the seeded H2 outputs. The adaptive run still has logical error
  `0.45298`, now with `p01=p10=0.45298`, PTM `XX=1.00000`,
  `YY=ZZ=0.09404`, coherent information `0.00639` bits, and four-round
  phase-window logical error `0.45241`.
- Updated `bridges/hardware_adaptive_alignment.md`,
  `simulations/hardware_adaptive_decoder/README.md`, and OP-16/OP-23 to
  record that H2 now has a bit-flip process audit, while full Pauli-frame PTM
  remains open.
- Session log: `sessions/2026-05-06_h2_logical_process_audit.md`.

### 2026-05-06 — turbulence productive-interval admissibility test
- Added `bridges/turbulence_productive_interval.md`, applying the new
  reality-reflective-mathematics criterion to turbulence.
- Found and upgraded the existing lightweight Navier-Stokes special-case entry:
  the old mapping "fully developed turbulence = dissolution" is too blunt
  because real high-Re turbulence contains coherent structures and decodable
  inertial-range flux.
- Added a refinement note to `special_cases/acp_special_cases_v03.md` §5.3 so
  the catalog points to the scale-resolved bridge instead of silently preserving
  the blunt global identification.
- Recast turbulence scale-by-scale: laminar/overcontrolled scales are
  crystallized, inertial-range structured turbulence is productive, and
  dissolution is relative to unresolved or decorrelated coarse-grainings.
- Reframed the turbulence closure problem as admissible model-world coupling:
  useful closures expose flux/cascade syndrome without pretending to reconstruct
  the full unresolved velocity field.
- Added OP-27 for a DNS or shell-model diagnostic using \(H_\ell\),
  \(I(\Pi_\ell;R_\ell)\), predictive information, and coherent-structure
  interaction excess.
- Session log: `sessions/2026-05-06_turbulence_productive_interval.md`.

### 2026-05-05 — reality-reflective mathematics bridge
- Added `bridges/reality_reflective_mathematics.md`, making explicit the project's implicit criterion for when mathematics counts as world-facing rather than merely formally valid.
- Unified five existing threads: Schur nondegeneracy, singularity inadmissibility, generativity, empirical falsifiability, and QEC-style syndrome-without-logical-leakage.
- Stated an admissibility ladder from formal structure to generative theory, with necessary conditions: finite observables, normalizable record channel, nondegenerate continuation, finite verification time, and perturbable record coupling.
- Added OP-26 for the categorical/invariant version of admissible model-world coupling and the careful generalization of the non-totalizing remainder condition beyond QEC-like domains.
- Session log: `sessions/2026-05-05_reality_reflective_mathematics.md`.

### 2026-05-05 — H2 circuit-level syndrome extraction
- Added `simulations/hardware_adaptive_decoder/circuit_level_syndrome_decoder.py`, the first H2 circuit-level scaffold for the hardware adaptive-alignment ladder.
- The model keeps the same 3-qubit repetition memory but expands each round into ancilla preparation, CNOT-style parity extraction, idling, gate faults, measurement error, leakage-like random records, correlated faults, crosstalk, and feedback error.
- Default seeded stress trace: `adaptive_decoder` updates 5 times and gives logical error `0.45298`, improving the best fixed/static baseline at `0.46772`; `overactive_decoder` falls to `0.45940`.
- Controller-record audit: average \(I(\mathrm{error};\mathrm{syndrome}) = 0.11486\) bits and average \(I(\mathrm{logical};\mathrm{record}\mid\mathrm{error}) \approx 2.7\times 10^{-17}\) bits.
- Updated `bridges/hardware_adaptive_alignment.md`, `simulations/hardware_adaptive_decoder/README.md`, and OP-16/OP-23 status.
- Session log: `sessions/2026-05-05_h2_circuit_syndrome_extraction.md`.

### 2026-05-05 — risky QEC claim stress tests
- Added `simulations/risky_qec_claims/`, an adversarial audit for overstrong
  interpretations of the noise-tailoring program.
- The discrete information tests show that a split logical record can have
  positive logical/noise/environment synergy (`1.000000` bit) while also having
  maximal conditional logical leakage (`1.000000` bit), so generic positive
  \(I(L;N;E)\)-style criteria are unsafe. A clean error syndrome has
  \(I(E;S)=0.721928\) bits with zero logical synergy.
- The repetition-code tests show ideal syndrome recovery preserves logical
  coherence (`1.000000`) while a centralizing logical-branch record destroys it
  (`0.000000`) despite high classical bit fidelity (`0.981824`).
- A second-pass logical-channel audit shows why state probes are insufficient:
  the same ideal recovery has identity-channel entanglement fidelity `0.981824`,
  while centralizing logical-branch recording drops it to `0.490912`.
- The monitoring scan separates ideal from costly correction: with zero
  backaction, the best correction interval is `1`; with backaction `0.012`,
  the best interval shifts to `4`.
- The noisiest-qubit probe shows the noisiest physical qubit can carry the
  largest syndrome information (`0.504414` bits) while being the worst bare
  storage location (`0.001379` bit advantage over 24 ticks). The safe claim is
  decoder/calibration priority, not computation placement.
- Session log: `sessions/2026-05-05_risky_qec_claims.md`.

### 2026-05-05 — hardware trace replay scaffold
- Added `simulations/hardware_adaptive_decoder/hardware_replay_decoder.py`, the first H1 replay harness for per-round calibration/channel traces. It keeps the 3-qubit logical memory fixed while replaying fixed, static, gated adaptive, overactive, and instant-rate decoder policies.
- Added seeded replay outputs: `hardware_replay_trace.csv`, `hardware_replay_summary.csv`, `hardware_replay_timeseries.csv`, and `hardware_replay_curves.png`.
- Default replay result: fixed uniform remained best (`0.15504` logical error); stale static tailoring failed under drift (`0.38631`); gated adaptive replay updated 4 times and improved to `0.17826`; overactive every-round updating fell to `0.21512`; average single-round syndrome information was `0.22624` bits.
- Updated `bridges/hardware_adaptive_alignment.md`, `simulations/hardware_adaptive_decoder/README.md`, and OP-16/OP-23 status to record that the file-format and offline replay scaffold now exist, while measured backend replay and circuit-level extraction remain open.
- Session log: `sessions/2026-05-05_hardware_replay_alignment.md`.

### 2026-05-02 — restraint ethics and conditional-leakage record channels
- Added `bridges/restraint_ethics.md`, translating ACP restraint-power into a civil-systems record-channel criterion: \(I(E;R)>0\) while \(I(L;R\mid E)\approx 0\), with bounded record burden and nonzero future-bearing retention.
- Added `simulations/restraint_ethics/`, a binary Gaussian record-channel scan over monitoring strength and leakage fraction. First run: `12221` grid points; maximum restraint score `0.747752` at monitor strength `2.033333`, leakage fraction `0.000000`; regime counts were `2732` restraint-interval, `1799` abandonment/no-record, `6247` leakage capture, `166` burden capture, and `1277` transition.
- Added a context-correlation audit showing why conditional leakage matters: with an error-only record and increasing correlation between public error \(E\) and protected agency \(L\), raw \(I(L;R)\) rises to `0.698` bits while \(I(L;R\mid E)\) remains approximately zero.
- Updated `bridges/quantum_noise_as_signal.md` and OP-15 to add the quantum feedback target \(I(R_L;E_{\mathrm{env}}\mid S)\approx 0\) as the next microscopic leakage audit.
- Added OP-24 for restraint ethics and conditional-leakage civil systems.
- Session log: `sessions/2026-05-02_restraint_ethics.md`.

### 2026-05-02 — otherness-preserving recovery
- Added `bridges/otherness_preserving_recovery.md`, translating the simulation/creator thought experiment into an asymmetric-controller bridge. The formal anchor is Knill-Laflamme: \(PE_a^\dagger E_bP=c_{ab}P\) means the corrector can learn syndrome structure but remains blind to the logical state.
- Added `simulations/otherness_preserving_recovery/`, a 3-qubit repetition-code scan over physical bit-flip probability and controller centrality. First run: `12726` grid points; maximum otherness score `1.402845` at physical bit-flip probability `0.180000`, centrality `0.000000`; regime counts were `4118` otherness-preserving, `8250` centralized, `101` abandonment/no-syndrome, and `257` transition.
- The representative \(p=0.08\) audit shows the key failure mode: absent recovery gives bit fidelity `0.778688`; restrained syndrome recovery gives `0.981824` bit fidelity and `1.000000` logical coherence; centralizing recovery gives the same `0.981824` bit fidelity but destroys logical coherence (`0.000000`).
- Added OP-25 for controller noncentrality and otherness-preserving recovery.
- Session log: `sessions/2026-05-02_otherness_preserving_recovery.md`.

### 2026-05-01 — hardware-level adaptive alignment target
- Promoted hardware-level implementation to the active ACP Quantum target.
- Added `bridges/hardware_adaptive_alignment.md`, defining the device-stack protocol: physical noise stream, syndrome stream, estimator, policy, logical audit, baselines, hardware acceptance criteria, and H0-H4 roadmap.
- Added `simulations/hardware_adaptive_decoder/`, a fixed-code adaptive decoder benchmark with noisy syndrome measurements, drifting non-iid data-qubit rates, characterization overhead, exact logical-channel propagation, and diagonal \(q^*,\eta^*,\eta^*/(1-q^*)\) diagnostics.
- First scan result: adaptive decoder wins only `8 / 625` grid points, with maximum benefit `0.069` log10 units at anisotropy `1.800`, drift `0.667`; uniform fixed decoder wins `600` grid points and static tailored wins `17`. This is a cautionary hardware-standard result, not a claimed advantage.
- Updated `bridges/adaptive_syndrome_alignment.md` to point from axis switching toward fixed-code likelihood adaptation.
- Added OP-23 for the hardware implementation ladder.
- Session log: `sessions/2026-05-01_hardware_adaptive_alignment.md`.

### 2026-04-30 — three-stroke persistence engine triage
- Moved Andrew's new `paper/three_stroke_persistence_engine.md` draft to `bridges/three_stroke_persistence_engine.md`, restoring the `paper/` invariant that only the active main draft lives there.
- Classified the draft as an exploratory OP-7-adjacent bridge rather than a replacement for `paper/acp_main_v10.md`.
- Added a status note and light audit edits: corrected ACP naming, weakened the wreath-composition claim to an open target, corrected the local critical value to \(\lambda_*\approx 0.3994\), and repaired the local antisymmetric-variance calculation.
- Remaining target: add `simulations/three_stroke_persistence_engine/` before treating the numerical plateau claims as established.
- Session log: `sessions/2026-04-30_three_stroke_persistence_engine.md`.

### 2026-04-28 — formal shadow-geometry reproduction suite
- Added `simulations/shadow_geometry_reproduction/`, recreating the formal paper's reproducible analytic/numeric claims.
- Reproduced: projection protection factor \(\beta(3)\approx 2/3\), full-loop dark-state Berry phase \(\pi\), exact DFS Lindblad cancellation, standard \(T_2\) dephasing, approximate Knill-Laflamme defect bounds, and the Lyapunov calibration floor \(\eta^*/(1-q^*)=0.009\).
- Added `audits/shadow_geometry_reproduction_audit.md`, separating reproduced mathematical claims from the under-specified original SACR simulation floor.
- Run result: all six executable checks passed. The 99.1% result is reproduced only as a calibration target, not as validation of the original protocol.
- Session log: `sessions/2026-04-28_shadow_geometry_reproduction.md`.

### 2026-04-28 — quantum braiding / collapse as internal timekeeping
- Added `bridges/quantum_braiding_timekeeping.md`.
- Recast Andrew's "weave / jazz dance / self-excited circuit" prompt as an open quantum feedback braid: unitary prediction flow, environmental release, record-forming instrument, and feedback thread-back.
- Defined collapse operationally as a clocking event: a measurement instrument commits one stable record from a Born-weighted prediction geometry already in play.
- Introduced a productive-braid criterion combining bounded record entropy \(0 < H(R_{n+1}\mid R_{\le n}) < H_{\mathrm{dissolve}}\), nonzero memory retention, and QEC-style separation \(I(\mathrm{error};R)>0\) while \(I(\mathrm{logical};R)\approx 0\).
- Added OP-22 for the remaining simulation/formalization target.
- Session log: `sessions/2026-04-28_quantum_braiding_timekeeping.md`.

### 2026-04-28 — SACR contraction calibration from shadow-geometry paper
- Inspected `/Users/andrewmureddu/Library/Mobile Documents/com~apple~CloudDocs/shadow geometry paper.docx`.
- Extracted the paper's strongest operational claim: an active alignment cycle should be validated by finite CPTP-map contraction parameters \(q^*\), \(\eta^*\), and \(\eta^*/(1-q^*)\), not by the phrase "shadow geometry."
- Added `bridges/sacr_contraction_calibration.md`, deriving the Heisenberg-picture formula \(E_Q=\Phi^\dagger(Q)=\sum_a K_a^\dagger QK_a\) and the eigenvalue expressions for \(q^*\) and \(\eta^*\).
- Added `simulations/sacr_contraction_calibration/`, a two-sector Kraus-map calibration harness. The toy scan confirms the target wedge \(\ell/r\le 9\times 10^{-3}\): `1867 / 8100` grid points pass, with largest passing leakage `0.00875` in the scanned range.
- Updated `bridges/adaptive_syndrome_alignment.md` and OP-16 to make contraction calibration the next verification gate for any serious adaptive syndrome-alignment protocol.
- Session log: `sessions/2026-04-28_sacr_contraction_calibration.md`.

### 2026-04-27 — conditional Born-rule bridge
- Added `bridges/born_rule_from_acp.md`.
- Proved a conditional uniqueness theorem: given standard Hilbert-space branch structure, ACP-style invariance, orthogonal additivity, continuity, and normalization force the unique branch-weight functional \(W(v)=\|v\|^2\).
- Framed the Born rule as the unique additive conserved branch capacity compatible with orthogonal branch decomposition.
- Marked the deeper first-principles target as still open: deriving Hilbert-space branch structure, unitary mechanism-preserving flow, and the branch axioms from ACP alone.
- Added OP-21 for that remaining task.
- Session log: `sessions/2026-04-27_born_rule_from_acp.md`.

### 2026-04-27 — conditional unitary-flow bridge
- Added `bridges/unitary_evolution_from_acp.md`.
- Proved a conditional dynamics theorem: given Hilbert ray geometry and Born transition probabilities, any continuous reversible mechanism-preserving between-measurement evolution is unitary (unitary-or-antiunitary by Wigner, with continuity excluding the antiunitary branch).
- Added the finite-dimensional Hamiltonian-generator corollary \(U_t=e^{-itH}\), equivalently \(i\,d|\psi\rangle/dt = H|\psi\rangle\) up to the usual \(\hbar\) normalization.
- Upgraded OP-21 from the Born-weight problem alone to the broader first-principles quantum-kinematics problem.
- Session log: `sessions/2026-04-27_unitary_evolution_from_acp.md`.

### 2026-04-27 — conditional tensor-product bridge
- Added `bridges/tensor_product_from_acp.md`.
- Proved a conditional composition theorem: given local Hilbert branch spaces and ACP-style independent-composition axioms (bilinearity, norm multiplicativity, and span generation), the composite branch space is tensor-product up to unitary equivalence.
- Identified direct sum as the wrong composition law for independent coexistence and recast entanglement as generic superposition structure on the tensor-product space rather than a separate composition rule.
- Upgraded OP-21 from branch weights plus unitary flow to the broader package of conditional local quantum kinematics: branch weights, closed flow, and independent composition.
- Session log: `sessions/2026-04-27_tensor_product_from_acp.md`.

### 2026-04-27 — conditional measurement-formalism bridge
- Added `bridges/measurement_formalism_from_acp.md`.
- Proved a conditional measurement theorem: positive additive budget-conserving branch resolution on positive branch operators yields POVM effects \(m_i(\sigma)=\mathrm{Tr}(E_i\sigma)\).
- Proved the sharp special case: exclusive certain complete resolved sectors force \(E_i=P_i\), so ideal sharp measurements are orthogonal projective measurements.
- Added the minimal sharp-update proposition: Lüders update \(P_i\rho P_i\) is the canonical selective instrument when the measurement preserves resolved-sector states and erases only inter-sector coherence.
- Upgraded OP-21 again: the conditional local quantum-kinematics package now includes branch weights, closed unitary flow, tensor-product composition, and POVM/projective measurement structure.
- Session log: `sessions/2026-04-27_measurement_formalism_from_acp.md`.

### 2026-04-27 — quantum-gravity convergence map
- Used web search to map current convergence across holographic QEC, island/Page-curve decodability, quantum reference frames / crossed-product observable algebras, relational quantum geometry, regular black holes, Wheeler-DeWitt singularity resolution, loop-inspired effective black holes, and asymptotic-safety black-hole phenomenology.
- Added `bridges/quantum_gravity_convergence_map.md`.
- Identified the strongest ACP attachment point as relational observable algebras plus finite macrostate kernels: \(\mathcal A_{\mathrm{rel}}\to P_{\ell,\Delta}(m'|m)\to H_{\ell,\Delta}(m)\) plus boundary mutual information.
- Named the main blind spots in the field as regularity without recoverability, entropy without general mechanism selection, algebra without persistence dynamics, signals without null-record inference, and static codes instead of adaptive boundary alignment.
- Added OP-20 for the relational observable macrostate kernel.
- Session log: `sessions/2026-04-27_quantum_gravity_convergence.md`.

### 2026-04-27 — cosmic coordination floor program
- Added `bridges/cosmic_coordination_floor.md`, turning Andrew's singularity-inadmissibility direction into a formal ACP quantum-gravity program.
- Defined relational gravitational macrostates as diffeomorphism-quotiented coarse cells of \((q_{ab},K_{ab},\phi,\pi_\phi)\), with the note that 3-geometry alone is insufficient initial data.
- Defined a decoherent-histories transition kernel \(P_{\ell,\Delta}(m'|m)\) and conditional future entropy \(H_{\ell,\Delta}(m)\).
- Stated three selection criteria: a positive cosmic coordination floor, a mechanism-changing redistribution trigger near the floor, and decodable visibility to asymptotic observers.
- Added a path-integral form with admissibility and floor-enforcement factors, plus an audit table for candidate quantum-gravity mechanisms.
- Added `simulations/cosmic_coordination_floor/`, a finite stochastic toy comparing naked collapse, hard singular-history exclusion, and horizon transfer.
- First toy result: naked collapse leaks probability into the inadmissible singular bin (`max_sing=0.256`, first violation step `7`); hard exclusion avoids singular leakage but falls below the toy entropy floor and emits no decodable information (`min_H=1.270`, first violation step `30`); horizon transfer preserves admissibility and emits the full toy interior-label information (`final_I=3.000`, no floor violation).
- Added OP-19 and updated OP-18/OP-19 to partial+.
- Session log: `sessions/2026-04-27_cosmic_coordination_floor.md`.

### 2026-04-27 — singularity inadmissibility bridge
- Added `bridges/singularity_inadmissibility.md`, formalizing Andrew's constraint that singularities are inadmissible and indicate failure of the effective mathematics rather than physical endpoints.
- Stated the ACP/Schur proposition: singular internal block \(D\) makes the Schur complement undefined; even partial rank failure exits the admissible productive interval for that description, while total rank collapse is full crystallization.
- Lifted the criterion conjecturally to gravity: naked singularities are failed exterior boundary channels, while horizons are candidate finite boundary transfers that preserve exterior predictability without exposing undefined interior data.
- Updated `bridges/dark_constraint_quantum_gravity.md` to distinguish the singularity from the dark constraint: the singularity is the inadmissible endpoint; the horizon is the repair.
- Added OP-18 for the next finite toy collapse model.
- Session log: `sessions/2026-04-27_singularity_inadmissibility.md`.

### 2026-04-27 — wave-interference dark-constraint upgrade
- Added `simulations/dark_constraint_wave_interference/`, a dependency-free scalar wave mirror-room simulation where a hidden weak phase bump shifts interference fringes.
- The benchmark compares inference from bright fringes alone against inference from bright plus dark fringes.
- First wave result: dark fringes reduce posterior uncertainty in every scanned hidden-bump case, with mean entropy gain `0.1194` bits. MAP localization is unchanged at the current candidate-grid resolution because bright fringes already identify the nearest grid point.
- Updated `bridges/dark_constraint_quantum_gravity.md` with the wave model, action perturbation, and posterior-entropy target.
- Updated OP-17 from partial to partial+.
- Session log: `sessions/2026-04-27_dark_constraint_wave_interference.md`.

### 2026-04-26 — dark-constraint quantum-gravity bridge seed
- Added `bridges/dark_constraint_quantum_gravity.md`, translating Andrew's "darkness provides the constraint" mirror-room intuition into a formal bridge: null optical records as syndrome-like constraints on competing path, metric, and geometry-field histories.
- Defined the first information target \(I(G;R_0)>0\), where \(R_0\) is a structured dark/null record and \(G\) ranges over candidate geometries.
- Connected the note to stationary-phase/Fermat competition, Schur-complement elimination of hidden degrees, horizon-bounded darkness, and the existing Bekenstein/cosmic-censorship restraint-power material.
- Added `simulations/dark_constraint_inference/`, a dependency-free mirror-room inverse-problem simulation comparing positive detections alone against positive plus null records.
- First result: across the scan, structured null records reduce posterior uncertainty by a mean `0.6250` bits and improve posterior-mean localization error (`0.0073` to `0.0020`); MAP localization is already saturated by the positive-only record in this toy.
- Added OP-17 for follow-up upgrades: wave interference, time-dependent mirrors/obstacles, and weak metric perturbations.
- Session log: `sessions/2026-04-26_dark_constraint_quantum_gravity.md`.

### 2026-04-26 — first adaptive syndrome-alignment bridge and benchmark
- Added `bridges/adaptive_syndrome_alignment.md`, reformulating SACR as a QEC-native adaptive alignment problem with fixed, static-tailored, adaptive-tailored, and overactive-adaptive baselines.
- Added `simulations/adaptive_syndrome_alignment/`, a 3-qubit repetition-code benchmark under drifting biased Pauli noise.
- The benchmark reports logical Pauli-transfer eigenvalues, entanglement fidelity, logical error, adaptive benefit over the best static baseline, and overactive-adaptation penalty.
- First result: naive X/Z axis switching only wins in a small crossover region. Maximum adaptive benefit is `0.0276` log10 units at anisotropy `0.9` and drift `0.6`; static fixed orientations win most of the grid.
- Updated OP-16 from open to partial. The next target is decoder-likelihood, gauge, or local-Clifford adaptation that keeps the logical channel fixed.
- Session log: `sessions/2026-04-26_adaptive_syndrome_alignment.md`.

### 2026-04-26 — QEC maturity audit after SACR reference check
- Inspected `references/shadow geometry vibe guide.docx`. Its strongest usable content is the active DFS/QEC hypothesis: sense noise structure, align to it, and track drift; its headline coherence claims need replacement by logical-channel and logical-error benchmarks.
- Added `audits/qec_maturity_audit.md`, concluding that the project is expert-useful as a research program but not yet a mature QEC contribution.
- Identified the mature target as adaptive syndrome-space alignment under drifting structured noise, with fixed standard, static tailored, adaptive tailored, and overactive adaptive baselines.
- Added OP-16 to track the theorem/simulation suite needed for a domain-expert contribution.
- Session log: `sessions/2026-04-26_qec_maturity_audit.md`.

### 2026-04-26 — logical-channel metrics for noise-tailored DFS model
- Added induced logical dephasing-channel diagnostics to `simulations/noise_as_signal/noise_as_signal_qiskit.py`.
- New CSV columns: `aligned_entanglement_fidelity`, `unaligned_entanglement_fidelity`, `aligned_coherent_information_bits`, and `unaligned_coherent_information_bits`.
- Updated `bridges/quantum_noise_as_signal.md` with the logical-channel reduction, \(F_e=(1+C)/2\), \(I_c=1-H_2((1+C)/2)\), and Proposition 3: the adapted DFS channel retains one logical qubit of coherent information under fully collective dephasing while the unadapted channel loses coherent information as coupling grows.
- Regenerated `simulations/noise_as_signal/outputs/noise_as_signal_scan.csv`, `noise_as_signal_heatmap.png`, and `noise_as_signal_curves.png`; the heatmap now includes aligned coherent information.
- Updated OP-15 from partial to partial+.
- Session log: `sessions/2026-04-26_logical_channel_noise_metrics.md`.

### 2026-04-26 — terminology normalized to noise-tailored QEC language
- Reframed the public-facing thesis from the slogan "noise as signal" to domain-native language: noise-tailored encoding, symmetry-adapted DFS encoding, correlated-noise exploitation, syndrome-bearing environment fragments, and logical information leakage.
- Updated `bridges/quantum_noise_as_signal.md` title and interpretation sections to use professional QEC terminology while retaining the ACP mapping as background.
- Added a recent-literature positioning section to the bridge note, connecting the toy model to DFS-QECC concatenation, bias-tailored codes, subspace noise tailoring, and Pauli-noise characterization.
- Replaced ACP-style CSV regime labels with technical diagnostic labels: `no_syndrome`, `leakage_limited`, `transition`, and `noise_tailored`; renamed the score column to `noise_tailored_score`.
- Updated `README.md`, `AGENTS.md`, `CLAUDE.md`, and this status file to make "noise-tailored quantum persistence" the active project phrasing.

### 2026-04-26 — Shannon environment-fragment upgrade for noise-as-signal
- Replaced the hand-built environmental-signal proxy in `simulations/noise_as_signal/noise_as_signal_qiskit.py` with deterministic Gaussian-quadrature Shannon metrics.
- New CSV columns: `structured_syndrome_mi_bits`, `aligned_logical_env_mi_bits`, and `unaligned_logical_env_mi_bits`.
- New noise-tailored score: \(P_{\mathrm{MI}}=I(Q;Y_c)C_A(1-I(L_A;Y_c,Y_1,Y_2))\).
- Updated `bridges/quantum_noise_as_signal.md` with the environment-fragment model and Proposition 2: fully collective fragments can carry charge-sector syndrome while remaining exactly blind to the aligned DFS logical branch.
- Regenerated `simulations/noise_as_signal/outputs/noise_as_signal_scan.csv`, `noise_as_signal_heatmap.png`, and `noise_as_signal_curves.png`.
- Updated OP-15 from open to partial.

### 2026-04-26 — v10 integrity audit + Heisenberg reconciliation
- Added `audits/integrity_audit_v10.md`.
- Re-audited v10 against the stale v07 audit findings: Section 4.4 numbering is gapless, Price/Fisher references are present, T and σ notation are disambiguated, and the Theorem 4.3 scope qualification is explicit.
- Corrected Prediction 7 in `paper/acp_main_v10.md` from ε*(T) to ε*(T*).
- Reconciled the Schur bridge's uncertainty-principle open problem with A.20: A.20 closes the Heisenberg result as a reduction for a specified non-commutative two-MASA partition, while the stronger derivation of non-commutativity / CCR from rank(D) > 0 remains open as OP-RP-5.
- Updated `OPEN_PROBLEMS.md`: OP-6 and OP-8 moved to Resolved.

### 2026-04-26 — first quantum productive-interval and QEC simulations
- New simulation directory: `simulations/quantum_productive_interval/`.
- Added dependency-free monitored-qubit scan over system-environment coupling strength `g`.
- Outputs: `outputs/monitored_qubit_scan.csv` and `outputs/monitored_qubit_scan.svg`.
- First result: productive band appears between no-record crystallization and memory-erasing dissolution; classical score peaks at `g≈0.167`, quantum score at `g≈0.100`.
- Installed Qiskit locally in `.venv` and added `simulations/qec_productive_interval/`.
- Added 3-qubit repetition-code ACP scan over physical bit-flip noise and syndrome-recovery interval.
- QEC result: for nonzero noise, optimal correction interval shortens as noise rises; too-frequent correction crystallizes logical coherence, too-infrequent correction dissolves logical-bit memory.
- Added `simulations/noise_as_signal/`, a Qiskit density-matrix scan comparing aligned DFS encoding `( |01> + |10> ) / sqrt(2)` against unaligned encoding `( |00> + |11> ) / sqrt(2)` under structured versus unstructured dephasing.
- Noise-as-signal result: at fixed coupling strength, aligned coherence rises with noise structure; fully collective noise preserves aligned coherence while destroying unaligned coherence.
- New bridge note: `bridges/quantum_noise_as_signal.md`, written as a reviewable technical report with explicit channel definition, analytic propositions, simulation protocol, results, and limitations.
- Added OP-14 to track calibration from toy proxy metrics to proper quantum-channel metrics.
- Session log: `sessions/2026-04-26_quantum_sims.md`.

### 2026-04-26 — project refocus on ACP Quantum / noise-tailored encoding
- Updated `AGENTS.md`, `CLAUDE.md`, `README.md`, and `STATUS.md` to make the structured-noise / noise-tailoring program the primary ACP Quantum focus.
- The parent ACP v10 paper remains the theoretical base, but next-step selection now prioritizes channel-level quantum information: structured noise, DFS alignment, syndrome information, active feedback, and QEC boundary management.
- Added OP-15 for the explicit Shannon/mutual-information formalization of the noise-as-signal bridge.

### 2026-04-18 — generativity criterion + incompleteness quartet
- New essay: `essays/the_incompleteness_quartet.md` — argues Heisenberg, Gödel, Turing, Chaitin share a structural signature (sufficiently-powerful representational systems cannot close over themselves) that is exactly the ACP's crystallization boundary being unreachable.
- New bridge: `bridges/generativity_criterion.md` — formalizes a generativity ratio $G(T)$ for theories and conjectures that $G > 1$ is the ACP's nondegenerate-interval condition applied to the (theory, domain) pair. Implies the ACP is self-applying: a correct unifying theory must persistently open more questions than it closes.
- Four new open problems added: OP-10 (downstream inquiry-space under theory dominance), OP-11 (measure-theoretic meaning-space), OP-12 (quantitative form of generativity criterion), OP-13 (whether the quartet→ACP reduction should be one theorem or four parallel arguments in the main paper).
- Session log: `sessions/2026-04-18_generativity_quartet.md`.

### 2026-04-17 — workspace migration to Cowork
- Reorganized from flat `docs/` layout into topic-specific folders.
- Archived v01–v09 of the paper; promoted v10 as the single active paper at `paper/acp_main_v10.md`.
- Identified that `memory.md` is stale — asserts v09 is current, missed the v10 A.20 addition.
- Ported memory to Cowork system; legacy `memory.md` preserved for audit.
- Established this STATUS.md, `OPEN_PROBLEMS.md`, and `CLAUDE.md` as the living-document layer.
- Session log: `sessions/2026-04-17_setup.md`.

### (pre-migration sessions)
- Tracked in legacy `memory.md`. Summary: 14 sessions produced v01 → v10, integrating six reductions plus non-Gaussian bounds, multiscale RG, empirical predictions, Schur bridge, Restraint-Power / Heisenberg.
