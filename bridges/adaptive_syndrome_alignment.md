# Adaptive Syndrome-Space Alignment Under Drifting Structured Noise

*Status: formal program note with first toy benchmarks; hardware-facing
adaptive-decoder scaffold added; not yet a fault-tolerant surface-code result.*

## Abstract

This note reformulates the archival SACR / shadow-geometry idea in standard
quantum-error-correction language. The mature claim is not that noise is
beneficial in general, nor that "shadow geometry" is a new QEC primitive. The
claim to test is narrower:

> adaptive code, gauge, syndrome, or decoder alignment can improve logical
> memory when physical noise is structured and drifting, but only when the
> logical-error penalty of remaining statically misaligned exceeds the overhead
> of characterizing and updating the alignment.

The first benchmark is intentionally small: a three-qubit repetition memory
whose orientation can be chosen to correct either \(X\)-dominated or
\(Z\)-dominated physical Pauli noise. The second benchmark is more
hardware-facing: the code is fixed, syndrome measurements are noisy, data-qubit
error rates are non-identical and drifting, and adaptation updates only the
decoder likelihood table. Both outputs are logical-channel quantities, not
branch population.

## 1. Why This Is the Mature Target

The two-qubit DFS model in `bridges/quantum_noise_as_signal.md` establishes the
static symmetry fact: an encoding matched to collective dephasing can preserve
logical coherence while the environment carries charge-sector information. That
is a useful lemma, but it is not yet a mature QEC contribution because DFS and
noise-tailored codes already exist.

The mature question is dynamic:

> When should a device spend resources learning and tracking the noise
> geometry, rather than use a fixed code or a static noise-tailored decoder?

This is the QEC-native version of the earlier SACR hypothesis. The word
"alignment" now means a controlled choice of code orientation, gauge, syndrome
extraction circuit, or decoder likelihoods relative to an estimated physical
noise model.

## 2. Setup

Let \(C_a\) be a code, gauge, or decoder configuration chosen from an alignment
family \(\mathcal A\). Let the physical noise at round \(t\) be
\(\mathcal N_t\), with estimated structure
\(\widehat \Sigma_t\). In a Pauli approximation, \(\Sigma_t\) may be the
covariance or probability vector over Pauli error components. More generally,
it may be a channel estimate, syndrome-event correlation model, or decoder
likelihood table.

For a memory experiment of \(T\) rounds, an alignment policy
\(\pi\) chooses

$$
a_t = \pi(\widehat \Sigma_{\leq t})
$$

and induces a logical channel

$$
\mathcal L_\pi(T)
=
\mathcal R_{a_T}\mathcal N_T
\cdots
\mathcal R_{a_1}\mathcal N_1,
$$

including the noisy syndrome extraction and recovery operations
\(\mathcal R_{a_t}\). The performance target is a logical-channel metric such
as logical error rate, entanglement fidelity \(F_e\), or the Pauli transfer
matrix of \(\mathcal L_\pi(T)\).

The alignment problem is:

$$
\pi^* =
\arg\max_\pi F_e(\mathcal L_\pi(T))
$$

subject to the cost of estimating \(\Sigma_t\), changing \(a_t\), and running
the corresponding syndrome extraction circuit.

## 3. Baselines

A credible domain benchmark must compare at least four policies.

1. **Fixed standard:** use a conventional code/gauge/decoder independent of
   \(\Sigma_t\).
2. **Static tailored:** estimate \(\Sigma_0\), choose the best initial
   alignment, and keep it fixed.
3. **Adaptive tailored:** periodically estimate \(\Sigma_t\) and update the
   alignment when the expected logical benefit exceeds update cost.
4. **Overactive adaptive:** update too frequently, paying characterization and
   switching overhead even when the noise is stationary or slowly varying.

Without the static tailored baseline, adaptive alignment can look artificially
good. Without the overactive baseline, the cost of adaptation is invisible.

## 4. Toy Repetition-Code Model

The first simulation lives at

`simulations/adaptive_syndrome_alignment/adaptive_alignment.py`.

It uses a three-qubit repetition memory with two orientations:

- \(a=x\): computational-basis repetition, correcting physical \(X\) errors;
- \(a=z\): Hadamard-rotated repetition, correcting physical \(Z\) errors.

The physical noise per round is independent biased Pauli noise with no \(Y\)
component:

$$
p_x(t)+p_z(t)=p,
$$

and

$$
b(t)=\chi \cos\left(2\pi \omega t/T\right),
$$

where \(\chi\in[0,1]\) is the anisotropy and \(\omega\) is the number of bias
drift cycles over the memory experiment. The probabilities are

$$
p_x(t)=\frac{p}{2}(1+b(t)),
$$

and

$$
p_z(t)=\frac{p}{2}(1-b(t)).
$$

Positive \(b(t)\) means \(X\)-dominated noise; negative \(b(t)\) means
\(Z\)-dominated noise.

For the three-qubit repetition code, the logical failure probability for the
corrected Pauli component is the majority-failure probability

$$
f(p)=3p^2(1-p)+p^3,
$$

while the uncorrected component acts as a logical Pauli error whenever an odd
number of physical errors occurs:

$$
g(p)=\frac{1-(1-2p)^3}{2}.
$$

Thus, for \(a=x\),

$$
p_L^X=f(p_x),\qquad p_L^Z=g(p_z),
$$

and for \(a=z\),

$$
p_L^X=g(p_x),\qquad p_L^Z=f(p_z).
$$

The per-round logical Pauli transfer eigenvalues are

$$
\lambda_X=1-2p_L^Z,
$$

$$
\lambda_Z=1-2p_L^X,
$$

and

$$
\lambda_Y=(1-2p_L^X)(1-2p_L^Z).
$$

The memory channel is obtained by multiplying these transfer eigenvalues across
rounds, including characterization and switching overhead. The final
entanglement fidelity is

$$
F_e=\frac{1+\lambda_X+\lambda_Y+\lambda_Z}{4}.
$$

The current parameter choices are deliberately conservative:

$$
T=48,\qquad p=0.025,
$$

with adaptive updates every 12 rounds. Characterization and switching overhead
are included as additional small logical Pauli noise channels.

## 5. Alignment Criterion

Let \(e_t(a)\) be a per-round logical error proxy for alignment \(a\) under the
instantaneous noise \(\Sigma_t\), and let \(h_t(a_{t-1},a_t)\) be the overhead
from characterizing or changing alignment. A static alignment \(a_0\) beats an
adaptive policy \(a_t\) when

$$
\sum_{t=1}^T e_t(a_0)
\leq
\sum_{t=1}^T e_t(a_t)
+
\sum_{t=1}^T h_t(a_{t-1},a_t).
$$

Adaptive alignment can only win when

$$
\sum_{t=1}^T
\left[e_t(a_0)-e_t(a_t)\right]
>
\sum_{t=1}^T h_t(a_{t-1},a_t).
$$

This is the operational version of the SACR inequality
\(\kappa\alpha>\gamma\): the contraction gained by tracking the noise must
exceed the leakage and overhead introduced by the tracking operation.

The sharper finite-cycle diagnostic is recorded in
`bridges/sacr_contraction_calibration.md`. Given an implemented CPTP cycle
\(\Phi(\rho)=\sum_a K_a\rho K_a^\dagger\), aligned projector \(P\), and
misaligned/leakage projector \(Q=I-P\), define

$$
E_Q=\Phi^\dagger(Q)=\sum_a K_a^\dagger QK_a .
$$

Then

$$
q^*=\lambda_{\max}(QE_QQ|_{\operatorname{ran}Q}),
\qquad
\eta^*=\lambda_{\max}(PE_QP|_{\operatorname{ran}P}),
$$

and the active alignment floor obeys

$$
V_\infty\leq \frac{\eta^*}{1-q^*}.
$$

This turns the archival SACR realignment claim into a finite channel test: an
adaptive protocol should reduce \(q^*\) enough to compensate for the
measurement, switching, and characterization overhead that increases
\(\eta^*\).

## 6. First Benchmark Protocols

The simulation records:

- `fixed_x`: always correct physical \(X\) errors;
- `fixed_z`: always correct physical \(Z\) errors;
- `static_tailored`: choose the initially dominant axis and keep it;
- `adaptive_tailored`: update every 12 rounds and switch when the bias changes
  sign;
- `overactive_adaptive`: update every round, paying unnecessary
  characterization overhead.

Primary metrics:

- `entanglement_fidelity`;
- `logical_error = 1 - entanglement_fidelity`;
- Pauli-transfer eigenvalues `lambda_x`, `lambda_y`, `lambda_z`;
- `adaptive_benefit_log10`, defined as

$$
\log_{10}
\frac{
\min(e_{\mathrm{fixed\ x}},e_{\mathrm{fixed\ z}},e_{\mathrm{static}})
}{
e_{\mathrm{adaptive}}
};
$$

- `overactive_penalty_log10`.

Positive `adaptive_benefit_log10` means adaptive alignment beats the best
static baseline. Negative values mean static tailoring is better.

## 7. First Benchmark Result

The first scan is not a victory lap for naive adaptation. It gives the more
useful result:

> adaptive axis-switching helps only in a small crossover region, and the gain
> is modest.

With the current parameters, the maximum adaptive advantage is

$$
\log_{10}(e_{\mathrm{static}}/e_{\mathrm{adaptive}})=0.0276,
$$

at

$$
\chi=0.9,\qquad \omega=0.6.
$$

At that point the adaptive protocol has

$$
F_e=0.5324,\qquad e=0.4676,
$$

while the best static baseline has

$$
e=0.4982.
$$

Across the scanned grid, the best protocol counts are:

| protocol | grid points won |
|---|---:|
| `fixed_x` | 1041 |
| `fixed_z` | 818 |
| `adaptive_tailored` | 23 |
| `overactive_adaptive` | 4 |

This is exactly the caution expected from QEC: switching which Pauli component
a repetition code protects is not a general strategy for preserving an
arbitrary unknown logical qubit. It can help only when the noise drift creates
enough static misalignment and the update overhead is small enough. It is not a
replacement for a code or decoder that protects the full logical channel.

The implication for the mature program is sharp: the next adaptive benchmark
should update decoder likelihoods, gauge choices, or local Clifford tailoring
inside a code that continues to protect the same logical information. Naive
basis switching is at best a diagnostic toy.

## 8. Relation to Existing QEC Work

The recent hardware and code-design literature already supports the premise
that real QEC noise is not always iid depolarizing noise. Gicev, Hollenberg,
and Usman used heavy-hexagon syndrome measurements on IBM superconducting
devices and found data inconsistent with uniform depolarizing noise, including
biased, inhomogeneous, and temporally correlated structure. Tiurev, Derks,
Roffe, Eisert, and Reiner showed that surface codes tailored to known
non-independent and non-identically distributed noise can improve thresholds
and suppress logical failures relative to an untailored surface code.

Therefore the novelty target here cannot be "structured noise exists" or
"tailoring helps." The target must be the dynamic crossover:

> adaptive tailoring beats static tailoring only when noise drift is strong
> enough to matter and weak enough to track.

## 9. Limitations

1. The first benchmark is a repetition-code axis-choice model, not a
   fault-tolerant surface-code simulation.

2. The noise model has only independent \(X\) and \(Z\) components. Correlated
   multi-qubit errors, leakage, measurement error, crosstalk, and coherent
   miscalibration are not included.

3. The adaptive policy is deliberately simple: periodic sign tracking of the
   dominant Pauli component. A serious decoder-level implementation should use
   likelihood updates or Bayesian filtering of syndrome statistics.

4. The overhead model is phenomenological. It should be replaced by explicit
   characterization circuits, gate errors, measurement errors, and latency.

5. The bridge is currently a program note plus simulation, not a theorem about
   general stabilizer codes.

6. The new contraction calibration is only instantiated for a two-sector toy
   map. A serious OP-16 benchmark must compute \(q^*\), \(\eta^*\), and the
   floor bound for a real syndrome-extraction and recovery cycle.

## 10. Next Step

The next research-grade step is to move from axis choice in a repetition code
to a small stabilizer or subsystem-code benchmark where the alignment variable
is one of:

- decoder likelihoods;
- local Clifford tailoring;
- gauge choice;
- syndrome extraction schedule;
- active basis/gauge updates under measured noise drift.

The target figure should plot adaptive advantage over static tailoring as a
function of noise anisotropy and drift rate, with adaptation overhead included.
The matching channel-calibration figure should plot
\(\eta^*/(1-q^*)\) for the same policies, making visible when active updates
reduce leakage-sector retention and when their overhead raises the alignment
floor.

The hardware-level continuation is now recorded in
`bridges/hardware_adaptive_alignment.md` and
`simulations/hardware_adaptive_decoder/`. That scaffold keeps the logical code
fixed and adapts only decoder likelihoods under noisy syndrome measurements.
Its first result is again cautionary: adaptive decoding wins only in a small
drifting-anisotropic crossover region. This is the correct hardware standard.
Any future claim must beat strong fixed and static-tailored baselines without
changing the logical channel being protected.

## References

Gicev, S., Hollenberg, L.C.L., and Usman, M. (2024). Quantum computer error
structure probed by quantum error correction syndrome measurements. *Physical
Review Research* 6, 043249.

Tiurev, K., Derks, P.-J.H.S., Roffe, J., Eisert, J., and Reiner, J.-M. (2023).
Correcting non-independent and non-identically distributed errors with surface
codes. *Quantum* 7, 1123.

Nielsen, M.A. and Chuang, I.L. (2010). *Quantum Computation and Quantum
Information.* Cambridge University Press.
