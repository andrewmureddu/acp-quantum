# 2026-04-26 — Logical-Channel Metrics for Noise-Tailored DFS Model

## Focus

Continued OP-15 by upgrading the `noise_as_signal` bridge from classical
environment-fragment mutual information alone to explicit logical-channel
memory diagnostics.

## Work Completed

- Added induced logical dephasing-channel quantities to
  `simulations/noise_as_signal/noise_as_signal_qiskit.py`.
- New simulation outputs:
  - `aligned_entanglement_fidelity`
  - `unaligned_entanglement_fidelity`
  - `aligned_coherent_information_bits`
  - `unaligned_coherent_information_bits`
- Regenerated:
  - `simulations/noise_as_signal/outputs/noise_as_signal_scan.csv`
  - `simulations/noise_as_signal/outputs/noise_as_signal_heatmap.png`
  - `simulations/noise_as_signal/outputs/noise_as_signal_curves.png`
- Updated `bridges/quantum_noise_as_signal.md` with the induced logical channel
  \(\mathcal N_X\), entanglement fidelity \(F_e=(1+C_X)/2\), coherent
  information \(I_c=1-H_2((1+C_X)/2)\), and Proposition 3.
- Updated `simulations/noise_as_signal/README.md`, `STATUS.md`, and
  `OPEN_PROBLEMS.md`.

## Result

For each encoding \(X\in\{U,A\}\), the physical two-qubit dephasing channel
induces a logical qubit dephasing channel with off-diagonal multiplier
\(\eta_X=C_X\). For the maximally mixed logical input,

$$
F_e^X=\frac{1+C_X}{2},
$$

and

$$
I_c^X=1-H_2\left(\frac{1+C_X}{2}\right).
$$

In the fully collective limit \(s=1\), the adapted DFS channel has

$$
F_e^A=1,\qquad I_c^A=1
$$

for all coupling strengths \(\sigma\). The unaligned channel has

$$
F_e^U=\frac{1+e^{-8\sigma^2}}{2},
$$

and \(I_c^U\to 0\) as \(\sigma\to\infty\).

This closes the coherent-information / entanglement-fidelity part of OP-15 for
the induced logical channel. The remaining OP-15 work is a microscopic
Stinespring/environment-state model and a recoverability or active-decoding
bound.

## Verification

Ran:

```bash
.venv/bin/python simulations/noise_as_signal/noise_as_signal_qiskit.py
```

The scan completed and rewrote the CSV and plots. The best
noise-tailored score remains \(1.4651\) at \(\sigma=2.5\), \(s=1.0\), matching
the ideal fully collective DFS limit.
