# QEC Maturity Audit: From Toy DFS Model to Domain Contribution

**Date:** 2026-04-26
**Scope:** `bridges/quantum_noise_as_signal.md`,
`bridges/syndrome_coordination.md`, `simulations/noise_as_signal/`,
`simulations/qec_productive_interval/`, and
`references/shadow geometry vibe guide.docx`.

## Executive Judgment

The current ACP Quantum material is useful for domain experts as a technical
orientation package, but it is not yet a mature contribution to QEC theory or
hardware practice.

The useful core is real:

- the two-qubit DFS note gives a clean channel-level separation between
  syndrome-bearing noise structure and protected logical information;
- the simulation now records explicit Shannon quantities, entanglement
  fidelity, and coherent information for the induced logical channel;
- `bridges/syndrome_coordination.md` identifies the mature direction:
  syndrome-space alignment under structured, non-iid, and drifting noise.

The current blocking issue is also clear:

> The project must stop treating "shadow geometry" as the contribution and
> instead formulate a standard QEC problem: adaptive noise-tailored syndrome
> alignment under characterized, possibly drifting, non-iid noise.

In domain language, the candidate contribution is not "noise as signal" and
not "shadow geometry" as a new metaphysics. It is:

> A channel- and decoder-level framework for when adaptive code/gauge/syndrome
> alignment improves logical memory under structured noise, including the
> regime where active alignment is harmful because the noise is stationary and
> measurement/gate overhead dominates.

That is the path to a mature QEC contribution.

## What the Reference Guide Adds

The file `references/shadow geometry vibe guide.docx` contains an earlier SACR
protocol narrative:

- Sense noise geometry with ancilla measurements.
- Align qubits toward a common noise eigenstructure.
- Constrain entanglement when alignment is good.
- Release entropy periodically.

It also records important corrections:

- a Qiskit register-order parsing bug produced false all-zero diagnostics in an
  earlier version;
- the stronger original whitepaper numbers were reduced to an honest simulated
  coherence floor around 91%;
- degradation under gate-error sweeps was gradual rather than a sharp phase
  transition;
- the author-facing interpretation is explicitly "DFS plus active feedback,"
  not magic cancellation of decoherence.

For this workspace, the reference guide is best treated as a hypothesis source,
not as a validated QEC result. The strongest claims in it still need conversion
into standard QEC metrics:

- logical error rate per round;
- logical channel fidelity for arbitrary encoded states, not only branch
  population or GHZ-support fraction;
- syndrome extraction model with explicit measurement backaction;
- comparison against standard decoders and static noise-tailored baselines;
- no reset/reprepare step that silently discards the logical memory being
  tested.

## Current Expert-Useful Pieces

### 1. Minimal DFS theorem

`bridges/quantum_noise_as_signal.md` is clean. It proves that fully collective
dephasing preserves the aligned DFS coherence while destroying the unaligned
encoding. This is known physics, but the note makes the ACP-relevant
information separation explicit:

$$
I(\mathrm{error};\mathrm{syndrome})>0
$$

while

$$
I(\mathrm{logical};\mathrm{environment})\approx 0.
$$

This is useful as a lemma or pedagogical anchor, not as the main contribution.

### 2. Logical-channel diagnostics

The induced logical channel on each two-branch encoding is now explicit. If
\(C_X\) is the coherence multiplier, then

$$
F_e^X=\frac{1+C_X}{2},
$$

and

$$
I_c^X=1-H_2\left(\frac{1+C_X}{2}\right).
$$

That gives domain experts recognizable channel metrics. Good.

### 3. Syndrome-space alignment bridge

`bridges/syndrome_coordination.md` is closer to the mature contribution than
the two-qubit DFS note. Its important content is:

- the syndrome space is the reserved correction/coordination capacity;
- noise-aligned syndrome spaces should outperform noise-agnostic ones when
  noise is anisotropic;
- active ALIGN can hurt under stationary noise because it adds overhead;
- active ALIGN should only help when the noise structure drifts faster than a
  static tailored code can track.

That last point is the seed of a publishable comparison.

## What Would Not Survive Expert Review Yet

### 1. The SACR simulation is not yet a QEC benchmark

The reference guide's headline coherence numbers are not enough. GHZ branch
population, ancilla alignment frequency, or coherence-like scores do not prove
preservation of an arbitrary logical qubit. A QEC expert will ask for the
logical channel.

Required replacement:

- prepare a complete logical process basis or use entanglement fidelity;
- evolve through repeated noisy syndrome cycles;
- decode/recover;
- report logical \(X\), \(Y\), and \(Z\) failure probabilities or full logical
  Pauli transfer matrix.

### 2. Reset/reprepare can invalidate memory claims

The reference guide includes periodic full reset and GHZ reinitialization. That
may be useful as a calibration loop, but it cannot count as preserving a
stored unknown logical state. A memory benchmark must forbid resetting the data
qubits unless the logical state is teleported, recovered, or otherwise
preserved by a specified channel.

### 3. "Shadow geometry" is not acceptable as the primary formal register

The phrase can remain as internal intuition, but a domain paper must translate
it into:

- Stinespring complementary channels;
- noise covariance or Pauli error covariance;
- syndrome distinguishability;
- stabilizer/gauge selection;
- decoder likelihoods;
- logical-channel metrics.

### 4. The current theorem statements are too strong

`bridges/syndrome_coordination.md` contains theorem-shaped statements whose
proofs are still sketches. A domain expert will not accept, for example, a
general iff threshold condition or tight bound without precise definitions of
noise complexity, syndrome distinguishability, decoder class, and code family.

These should be downgraded or refactored into:

- definitions;
- propositions for finite Pauli channels;
- conjectures for general channels;
- simulation-backed predictions.

## Mature Contribution Target

The target should be:

# Adaptive Syndrome-Space Alignment for Drifting Structured Noise

Problem statement:

Given a stabilizer or subsystem code, a noisy syndrome-extraction circuit, and a
time-dependent physical noise model \(\mathcal N_t\) with estimated Pauli
covariance \(\Sigma(t)\), choose a code/gauge orientation or decoder update
\(A_t\) to minimize the logical error rate over memory time \(T\), accounting
for the overhead of estimating and applying \(A_t\).

The key comparison:

1. Standard fixed code + standard decoder.
2. Static noise-tailored code/decoder using \(\Sigma(0)\).
3. Adaptive noise-tailored code/decoder using online estimates
   \(\widehat{\Sigma}(t)\).
4. Overactive adaptive protocol where update overhead dominates.

The expected mature result:

There is a crossover drift rate. Below it, static tailoring wins because active
alignment overhead is unnecessary. Above it, adaptive alignment wins because
static tailoring becomes misaligned. Above a second threshold, no protocol wins
because the characterization/update loop cannot keep up with the drift.

This is a proper QEC/hardware-practice claim.

## Minimum Simulation Needed Next

The next simulation should not extend the two-qubit DFS model. It should build
a small but standard QEC benchmark:

- code: 3-qubit repetition first, then small surface-code patch if feasible;
- noise: biased/non-iid Pauli noise with controllable covariance
  \(\Sigma(t)\);
- drift: stationary, slow drift, fast drift, abrupt jump;
- protocols: fixed standard, fixed tailored, adaptive tailored, overactive
  adaptive;
- decoder: maximum-likelihood or matching where applicable;
- metrics: logical error per round, entanglement fidelity, logical Pauli
  transfer matrix, and overhead-adjusted memory time.

The first publishable figure should be a phase diagram:

$$
\text{alignment benefit}
=
\log p_L^{\mathrm{standard}}
-
\log p_L^{\mathrm{adaptive}}
$$

over noise anisotropy and drift rate.

## Immediate Edits Recommended

1. Create a new bridge note:
   `bridges/adaptive_syndrome_alignment.md`.

2. Recast SACR as an internal name only:
   "SACR" becomes "adaptive syndrome-space alignment" in formal text.

3. Split claims in `bridges/syndrome_coordination.md` by status:
   proven finite-channel identities, conjectures, and simulation-backed
   predictions.

4. Add a new simulation suite:
   `simulations/adaptive_syndrome_alignment/`.

5. Treat `references/shadow geometry vibe guide.docx` as archival motivation,
   not as evidence.

## Bottom Line

For domain experts, the project is now useful as a research program with a
clear toy model and a promising mature target. It is not yet useful as a
finished QEC result.

The most credible next move is to prove and simulate a narrower claim:

> Adaptive syndrome alignment helps exactly when noise anisotropy is real,
> noise drift is large enough to obsolete a static tailored code, and the
> characterization/update overhead is smaller than the logical-error penalty
> of remaining misaligned.

That claim is specific, falsifiable, QEC-native, and hardware-relevant.
