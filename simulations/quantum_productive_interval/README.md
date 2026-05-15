# Quantum Productive Interval Simulation

This directory contains the first toy simulation for taking the ACP quantum.

The model is a monitored qubit represented by a Bloch vector. A scan over the
system-environment coupling strength `g` combines three effects:

- Hamiltonian rotation, which keeps internal futures open.
- Pointer-basis dephasing, which creates environmental records.
- Thermal relaxation, which erases memory at high coupling.

The simulation is intentionally dependency-free: it uses only the Python
standard library and writes both CSV data and an SVG plot.

## Run

```bash
python3 simulations/quantum_productive_interval/monitored_qubit.py
```

## Outputs

- `outputs/monitored_qubit_scan.csv`
- `outputs/monitored_qubit_scan.svg`

## Metrics

- `memory`: retained trace-distance distinguishability of antipodal initial
  states after the channel acts.
- `record`: proxy for usable environmental record formation. It rises with
  dephasing but is penalized by thermal relaxation.
- `coherence`: residual off-pointer coherence in the final states.
- `mixedness`: mean von Neumann entropy of final qubit states.
- `classical_score`: productive interval proxy for record-forming classicality.
- `quantum_score`: stricter proxy requiring record, memory, and residual
  off-pointer coherence.

Interpretation:

- Low `g`: crystallization. The qubit evolves almost unitarily but leaves no
  environmental record.
- Intermediate `g`: productive interval. The qubit keeps memory while exporting
  usable records.
- High `g`: dissolution. Thermal relaxation and strong monitoring erase memory.
