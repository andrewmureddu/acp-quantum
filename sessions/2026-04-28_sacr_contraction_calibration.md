# 2026-04-28 — SACR Contraction Calibration

## Prompt

Andrew pointed to:

`/Users/andrewmureddu/Library/Mobile Documents/com~apple~CloudDocs/shadow geometry paper.docx`

and said:

> let's run this

I treated that as an instruction to run the document through the ACP Quantum
research filter: extract the operational content, discard unsupported
terminology, and turn the finite claim into an executable object.

## Source Intake

The document is a repaired shadow-geometry white paper. Its most useful claims
are:

- the shadow sector is a Stinespring complementary channel;
- exact alignment is decoherence-free / Knill-Laflamme structure;
- approximate alignment gives defect bounds;
- the spectral-triple analogy is weakened to finite spectral geometry without
  a generic first-order condition;
- the active SACR claim reduces to a Lyapunov contraction condition.

For this workspace, the decisive object is the discrete-cycle calibration:

$$
q^*=\sup_{\rho:\operatorname{Tr}(Q\rho)=1}\operatorname{Tr}(Q\Phi(\rho)),
$$

$$
\eta^*=\sup_{\rho:\operatorname{Tr}(Q\rho)=0}\operatorname{Tr}(Q\Phi(\rho)),
$$

with alignment floor

$$
V_\infty\leq \frac{\eta^*}{1-q^*}.
$$

The reported 99.1% coherence floor becomes the target

$$
\eta^*/(1-q^*)\lesssim 9\times 10^{-3}.
$$

## Work Completed

- Added `bridges/sacr_contraction_calibration.md`.
- Added `simulations/sacr_contraction_calibration/README.md`.
- Added `simulations/sacr_contraction_calibration/sacr_contraction_calibration.py`.
- Regenerated:
  `simulations/sacr_contraction_calibration/outputs/sacr_contraction_scan.csv`.
- Regenerated:
  `simulations/sacr_contraction_calibration/outputs/sacr_contraction_heatmap.png`.
- Updated `bridges/adaptive_syndrome_alignment.md`.
- Updated OP-16 in `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Main Formal Move

For a finite CPTP cycle

$$
\Phi(\rho)=\sum_a K_a\rho K_a^\dagger,
$$

define the Heisenberg-picture leakage effect

$$
E_Q=\Phi^\dagger(Q)=\sum_a K_a^\dagger QK_a.
$$

Then:

$$
q^*=\lambda_{\max}(QE_QQ|_{\operatorname{ran}Q}),
$$

and

$$
\eta^*=\lambda_{\max}(PE_QP|_{\operatorname{ran}P}).
$$

This makes the SACR validation target finite and channel-native. A future
protocol does not need a vague alignment score; it needs a Kraus map or
superoperator for the actual cycle, plus projectors \(P,Q\).

## Toy Simulation Result

The toy model has a two-dimensional aligned sector and a two-dimensional
leakage sector. With leakage probability \(\ell\) and recovery probability
\(r\):

$$
q^*=1-r,\qquad \eta^*=\ell,\qquad
V_\infty\leq \ell/r.
$$

The scan confirms the target wedge:

$$
\ell/r\leq 9\times 10^{-3}.
$$

Run output:

```text
wrote simulations/sacr_contraction_calibration/outputs/sacr_contraction_scan.csv
wrote simulations/sacr_contraction_calibration/outputs/sacr_contraction_heatmap.png
best floor bound: 0.000000 at leakage=0.00000, recovery=0.010
grid points passing 99.1% target: 1867 / 8100
largest passing leakage in scan: 0.00875
weakest passing recovery in scan: 0.010
```

## Program Status

OP-16 is now partial+ rather than merely partial. The project has:

1. a QEC-native adaptive-alignment problem statement;
2. a toy repetition-code drift benchmark;
3. a finite-cycle contraction calibration formula;
4. a toy calibration harness.

The next serious step is not another shadow-geometry document. It is a real
small-code adaptive cycle where the Kraus/superoperator map includes syndrome
extraction, feedback, recovery, characterization overhead, and switching
overhead, so \(q^*\), \(\eta^*\), logical error rate, and entanglement fidelity
can be reported together.

