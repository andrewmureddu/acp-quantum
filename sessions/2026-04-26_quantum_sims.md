# 2026-04-26 — Quantum Productive-Interval Sims

## Summary

Andrew redirected the project from submission-readiness toward playful expansion and asked to start simulations for the quantum version of the ACP.

Built the first toy simulation:

- `simulations/quantum_productive_interval/monitored_qubit.py`
- `simulations/quantum_productive_interval/README.md`

The simulation is dependency-free and scans a monitored qubit over system-environment coupling strength `g`. The model combines:

- Hamiltonian rotation around x, representing internally open futures.
- Pointer-basis dephasing along z, representing environmental record formation.
- Thermal relaxation toward the maximally mixed state, representing memory-erasing dissolution.

Outputs:

- `simulations/quantum_productive_interval/outputs/monitored_qubit_scan.csv`
- `simulations/quantum_productive_interval/outputs/monitored_qubit_scan.svg`

## First Result

The scan produces an ACP-like productive interval:

- low coupling: crystallization/no environmental record;
- intermediate coupling: memory plus usable records;
- high coupling: dissolution via memory loss/mixedness.

With the current parameters:

- productive band: `g=0.033..0.400`;
- peak classical/productive score: `g≈0.167`;
- peak quantum/coherence-preserving score: `g≈0.100`.

The split is conceptually useful: objectified classicality tolerates stronger monitoring than residual quantum coherence.

## Follow-Up

Added OP-14: replace qualitative proxy metrics with channel-native quantities such as trace-distance contraction, coherent information, mutual information to explicit environment fragments, entanglement-breaking thresholds, and measurement-induced phase transition diagnostics.

## QEC Extension

Installed Qiskit locally in `.venv`:

- `qiskit 2.4.1`
- `qiskit-aer 0.17.2`
- `numpy 2.4.4`
- `matplotlib 3.10.9`

Built the first QEC version:

- `simulations/qec_productive_interval/repetition_code_acp.py`
- `simulations/qec_productive_interval/README.md`

The simulation uses a 3-qubit bit-flip repetition code and scans:

- physical bit-flip probability per tick, `p_noise`;
- syndrome-recovery interval.

It probes both `|0_L>` and `|+_L>` so the model can see both logical-bit survival and logical coherence survival. A small logical dephasing cost per recovery models imperfect, costly monitoring. This produces the ACP double-boundary:

- too-frequent recovery: crystallization of logical phase;
- too-infrequent recovery: dissolution of logical bit memory;
- middle recovery intervals: productive QEC band.

Current outputs:

- `simulations/qec_productive_interval/outputs/repetition_code_scan.csv`
- `simulations/qec_productive_interval/outputs/repetition_code_acp_heatmap.png`
- `simulations/qec_productive_interval/outputs/repetition_code_acp_curves.png`

Representative ridge:

- `p=0.005`: best interval `18`;
- `p=0.010`: best interval `9`;
- `p=0.015`: best interval `6`;
- `p=0.020`: best interval `4`;
- `p=0.030`: best interval `3`.

The best interval shortens as noise increases, as expected for an ACP-managed correction schedule.

## Noise as Signal

Built a focused Qiskit simulation for Andrew's intuition that not all noise is noise:

- `simulations/noise_as_signal/noise_as_signal_qiskit.py`
- `simulations/noise_as_signal/README.md`

The sim compares two encodings under phase noise:

- unaligned: `( |00> + |11> ) / sqrt(2)`;
- aligned/DFS: `( |01> + |10> ) / sqrt(2)`.

The scan varies total coupling/noise strength and the fraction of the noise that is collective/structured. Collective dephasing destroys the unaligned encoding but leaves the aligned DFS encoding coherent. Independent dephasing destroys both.

Outputs:

- `simulations/noise_as_signal/outputs/noise_as_signal_scan.csv`
- `simulations/noise_as_signal/outputs/noise_as_signal_heatmap.png`
- `simulations/noise_as_signal/outputs/noise_as_signal_curves.png`

Representative fixed-noise result at `noise_strength≈1.5`:

- structure `0.00`: signal `0.000`, unaligned coherence `0.105`, aligned coherence `0.105`;
- structure `0.50`: signal `0.447`, unaligned coherence `0.006`, aligned coherence `0.570`;
- structure `0.90`: signal `0.805`, unaligned coherence `0.000`, aligned coherence `0.978`;
- structure `1.00`: signal `0.895`, unaligned coherence `0.000`, aligned coherence `1.000`.

ACP reading: zero coupling is crystallization/no interface; unstructured coupling is dissolution; structured coupling is decodable environmental geometry that an aligned encoding can use as signal.

## Technical Write-Up

Added `bridges/quantum_noise_as_signal.md` as a journal-readable bridge note.
It formalizes the two-qubit model as a Gaussian dephasing channel with total
coupling strength `sigma` and structure fraction `s`. The central analytic
result:

- unaligned coherence:
  `C_U(sigma,s)=exp(-8 sigma^2 s^2 - sigma^2(1-s)^2)`;
- aligned DFS coherence:
  `C_A(sigma,s)=exp(-sigma^2(1-s)^2)`.

Thus, under fully collective dephasing (`s=1`), `C_A=1` for all coupling
strengths while `C_U=exp(-8 sigma^2)`. The note also derives the productive
score optimum for partially structured noise and states limitations explicitly.

## Project Refocus

Andrew asked whether this should become the focus of ACP Quantum. Answer: yes.

Updated:

- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `STATUS.md`
- `OPEN_PROBLEMS.md`

New orientation: ACP Quantum is centered on structured noise as signal. The parent ACP v10 paper remains the theoretical base, but next-step selection now prioritizes quantum-information work: channel definitions, DFS alignment, syndrome/environment mutual information, active feedback, and QEC boundary management.

Added OP-15 to replace the proxy environmental signal in `bridges/quantum_noise_as_signal.md` with explicit Shannon quantities:

- `I(error; syndrome)`;
- `I(logical state; environment)`;
- logical memory / coherent information / entanglement fidelity.
