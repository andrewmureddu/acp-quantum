# SACR Contraction Calibration as a CPTP-Map Test

*Status: operational bridge from the shadow-geometry white paper to the
adaptive-syndrome-alignment program; toy simulation added, real protocol map
still open.*

## Abstract

The useful operational core of `shadow geometry paper.docx` is not the
terminology of a new geometry. It is the finite verification problem for an
active alignment cycle. Given an aligned sector \(P\), a misaligned/leakage
sector \(Q=I-P\), and one implemented cycle

$$
\Phi(\rho)=\sum_a K_a\rho K_a^\dagger ,
$$

compute the worst-case leakage retention

$$
q^*=\sup_{\rho:\operatorname{Tr}(Q\rho)=1}\operatorname{Tr}(Q\Phi(\rho))
$$

and the worst-case aligned-sector leakage

$$
\eta^*=\sup_{\rho:\operatorname{Tr}(Q\rho)=0}\operatorname{Tr}(Q\Phi(\rho)).
$$

If \(q^*<1\), then the alignment floor obeys

$$
V_\infty \leq \frac{\eta^*}{1-q^*},
\qquad
V(\rho)=\operatorname{Tr}(Q\rho).
$$

The paper's reported 99.1% coherence floor corresponds, in this sector
population model, to the calibration target

$$
\frac{\eta^*}{1-q^*}\lesssim 9\times 10^{-3}.
$$

This note records the channel-native version of that test and attaches it to
OP-16: adaptive syndrome-space alignment under drifting structured noise.

## 1. Intake Judgment

The source document repairs several informal shadow-geometry claims in a
mathematically productive direction:

- the "shadow projection" is a Stinespring complementary channel, not a
  literal Hilbert-space projection;
- alignment is equivalent to exact or approximate decoherence-free / QEC
  structure, expressed by scalar projected Lindblad or Knill-Laflamme
  conditions;
- the spectral-triple analogy is weakened to a finite real spectral structure
  without a generic first-order condition;
- the active SACR claim is reduced to a Lyapunov contraction inequality.

For ACP Quantum, the last item is the actionable one. It converts the protocol
claim into a finite calculation on the actual implemented cycle map. The
terminology "SACR" can remain archival, but the formal object should be called
an active alignment cycle or adaptive syndrome-alignment cycle.

## 2. Heisenberg-Picture Calibration Formula

Let \(P\) project onto the aligned logical sector and \(Q=I-P\) project onto
the misaligned/leakage sector. For a finite-dimensional CPTP cycle \(\Phi\),
define the Heisenberg-picture leakage effect

$$
E_Q=\Phi^\dagger(Q)=\sum_a K_a^\dagger Q K_a.
$$

Then the two contraction parameters are operator norms on the two sectors:

$$
q^*=\lambda_{\max}(Q E_Q Q|_{\operatorname{ran}Q}),
$$

and

$$
\eta^*=\lambda_{\max}(P E_Q P|_{\operatorname{ran}P}).
$$

The proof is just linear optimization over density matrices. For any state
supported in \(Q\),

$$
\operatorname{Tr}(Q\Phi(\rho))=\operatorname{Tr}(E_Q\rho),
$$

and the supremum over density matrices is achieved by the top eigenvector of
the restricted effect. The same argument gives \(\eta^*\) on \(P\).

If the cycle includes the pinching assumed in the source document, then every
state decomposes as

$$
\rho=(1-v)\rho_P+v\rho_Q,\qquad v=V(\rho).
$$

Linearity gives

$$
V(\Phi(\rho))
\leq
(1-v)\eta^*+v q^*
\leq
\eta^*+q^*v.
$$

Iterating the loose but convenient bound yields

$$
V(\rho_n)\leq (q^*)^nV(\rho_0)
+\eta^*\frac{1-(q^*)^n}{1-q^*},
$$

and therefore the asymptotic calibration bound above.

## 3. Relation to the Continuous Inequality

The source paper writes the active realignment condition as

$$
\kappa\alpha>\gamma,
$$

where \(\kappa\) is the cycle repetition rate, \(\alpha\) is contraction
efficiency, and \(\gamma\) is uncontrolled outward leakage. In a discrete
implementation the directly measurable condition is

$$
q^*<1
$$

together with a small floor

$$
\eta^*/(1-q^*)\ll 1.
$$

If one cycle has duration \(\tau\), the effective contraction rate is

$$
\lambda_{\mathrm{eff}}= -\frac{1}{\tau}\log q^*.
$$

The continuous inequality is useful for intuition. The finite CPTP-map
calibration is what should be reported for a real QEC or hardware protocol.

## 4. Toy Sector-Transfer Model

The accompanying simulation uses the smallest aligned/misaligned-sector
channel:

$$
\mathcal H=P\mathcal H\oplus Q\mathcal H,
\qquad
\dim P=\dim Q=2.
$$

With aligned basis \(|0_P\rangle,|1_P\rangle\) and leakage basis
\(|0_Q\rangle,|1_Q\rangle\), let \(W_{P\to Q}\) and \(W_{Q\to P}\) preserve
the logical label while moving between sectors. For leakage probability
\(\ell\) and recovery probability \(r\), use Kraus operators

$$
K_0=\sqrt{1-\ell}\,P,\qquad
K_1=\sqrt{\ell}\,W_{P\to Q},
$$

$$
K_2=\sqrt{r}\,W_{Q\to P},\qquad
K_3=\sqrt{1-r}\,Q.
$$

This channel is CPTP and gives

$$
q^*=1-r,\qquad \eta^*=\ell,\qquad
V_\infty\leq \ell/r.
$$

The calibration target is therefore

$$
\ell < 9\times 10^{-3}r.
$$

This is not evidence that a real SACR implementation works. It is a sanity
harness for the target inequality and a template for replacing the toy Kraus
operators by a real syndrome-extraction, feedback, and recovery map.

## 5. Connection to Adaptive Syndrome Alignment

In the adaptive-syndrome-alignment program, \(P\) should represent the logical
sector preserved by the current code/gauge/decoder configuration, while \(Q\)
collects misaligned or leakage sectors that destroy the target logical memory.
For each candidate adaptive cycle \(a_t\), the benchmark should compute

$$
q^*(a_t),\quad \eta^*(a_t),\quad
\frac{\eta^*(a_t)}{1-q^*(a_t)}
$$

from the implemented finite channel. The mature comparison is then not just
logical error rate versus drift, but:

- fixed and static-tailored protocols have low update overhead but may suffer
  large \(q^*\) under drift;
- adaptive protocols can reduce \(q^*\) by realigning the recovery map;
- overactive protocols increase \(\eta^*\) through measurement, switching, and
  characterization overhead.

The publishable target is a phase diagram where adaptive alignment wins only
when the reduction in \(q^*\) outweighs the induced increase in \(\eta^*\).

## 6. Current Limitation

The present simulation is a two-sector calibration toy. It does not instantiate
the full SACR cycle from the source document, nor does it validate the reported
99.1% floor. It does something narrower and necessary: it makes the paper's
finite verification problem executable for any future CPTP cycle map.

