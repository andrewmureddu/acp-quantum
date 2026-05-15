# 2026-04-26 — Adaptive Syndrome-Alignment Bridge and First Benchmark

## Focus

Continued OP-16 by moving from the maturity audit to a concrete bridge note and
simulation benchmark.

## Work Completed

- Added `bridges/adaptive_syndrome_alignment.md`.
- Added `simulations/adaptive_syndrome_alignment/adaptive_alignment.py`.
- Added `simulations/adaptive_syndrome_alignment/README.md`.
- Generated:
  - `simulations/adaptive_syndrome_alignment/outputs/adaptive_alignment_scan.csv`
  - `simulations/adaptive_syndrome_alignment/outputs/adaptive_alignment_heatmap.png`
  - `simulations/adaptive_syndrome_alignment/outputs/adaptive_alignment_curves.png`
- Updated `STATUS.md` and `OPEN_PROBLEMS.md`.

## Benchmark

The benchmark uses a three-qubit repetition memory with two orientations:

- `x`: computational-basis repetition, correcting physical \(X\) errors.
- `z`: Hadamard-rotated repetition, correcting physical \(Z\) errors.

Physical noise is biased Pauli noise with drifting X/Z bias:

$$
b(t)=\chi\cos(2\pi\omega t/T).
$$

The simulation compares:

1. `fixed_x`
2. `fixed_z`
3. `static_tailored`
4. `adaptive_tailored`
5. `overactive_adaptive`

The primary metric is the entanglement fidelity of the induced logical Pauli
channel after the memory experiment.

## Result

The first result is cautionary and useful:

> naive X/Z repetition-code axis switching only wins in a small crossover
> region.

Maximum adaptive benefit:

$$
\log_{10}(e_{\mathrm{static}}/e_{\mathrm{adaptive}})=0.0276
$$

at anisotropy \(\chi=0.9\) and drift \(\omega=0.6\).

At that point:

$$
F_e=0.5324,\qquad e=0.4676,
$$

while the best static baseline has \(e=0.4982\).

Grid winners:

| protocol | grid points won |
|---|---:|
| `fixed_x` | 1041 |
| `fixed_z` | 818 |
| `adaptive_tailored` | 23 |
| `overactive_adaptive` | 4 |

## Interpretation

This result pushes the mature program in the right direction. Switching which
Pauli component a repetition code protects is not a general strategy for
preserving an arbitrary unknown logical qubit. A serious adaptive-alignment
protocol should instead update decoder likelihoods, gauge choices, syndrome
extraction schedules, or local Clifford tailoring while preserving the same
logical channel.

## Verification

Ran:

```bash
.venv/bin/python simulations/adaptive_syndrome_alignment/adaptive_alignment.py
.venv/bin/python -m py_compile simulations/adaptive_syndrome_alignment/adaptive_alignment.py
```
