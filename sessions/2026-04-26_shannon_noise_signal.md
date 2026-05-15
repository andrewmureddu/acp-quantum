# 2026-04-26 — Shannon Noise-as-Signal Upgrade

## Summary

Continued the structured-noise ACP Quantum front by upgrading
`bridges/quantum_noise_as_signal.md` and
`simulations/noise_as_signal/noise_as_signal_qiskit.py` from a hand-built
environmental-signal proxy to explicit Shannon mutual-information diagnostics.

## Changes

- Added a classical Gaussian environment-fragment readout coupled to the same
  collective and independent coordinates as the dephasing channel:
  \(Y_c=\sigma s q(x)+N_c\) and
  \(Y_k=\sigma(1-s)z_k(x)+N_k\).
- Added deterministic Gauss-Hermite quadrature for mutual information.
- Added CSV metrics:
  `structured_syndrome_mi_bits`,
  `aligned_logical_env_mi_bits`,
  `unaligned_logical_env_mi_bits`.
- Replaced the original proxy score with
  \(P_{\mathrm{MI}}=I(Q;Y_c)C_A(1-I(L_A;Y_c,Y_1,Y_2))\).
- Updated the bridge note with Proposition 2: in the fully collective limit,
  \(I(L_A;Y_c,Y_1,Y_2)=0\) while \(I(Q;Y_c)>0\) and the unaligned logical
  branch leaks to the same environment coordinate.

## Result

At \(\sigma=1.5\), the new diagnostics show the desired separation:

| structure \(s\) | \(I(Q;Y_c)\) | \(I(L_A;E)\) | \(C_A\) | \(P_{\mathrm{MI}}\) |
|---:|---:|---:|---:|---:|
| 0.00 | 0.000 | 0.934 | 0.105 | 0.000 |
| 0.50 | 0.541 | 0.525 | 0.570 | 0.146 |
| 0.90 | 1.067 | 0.032 | 0.978 | 1.010 |
| 1.00 | 1.164 | 0.000 | 1.000 | 1.164 |

The full scan's best score is \(P_{\mathrm{MI}}=1.4651\) at
\(\sigma=2.5, s=1.0\), as expected for the ideal DFS symmetry limit.

## Follow-Up

OP-15 is now partial rather than untouched. The next technical upgrade should
replace the classical fragment diagnostic with a full quantum-channel version:
explicit environment states / Stinespring dilation, entanglement fidelity or
coherent information, and then an active noise-adapted feedback protocol.
