# 2026-04-28 — Formal Shadow Geometry Reproduction

## Prompt

Andrew asked:

> lets try to recreate the results from the shadow geometry paper. the formal one.

I interpreted this as a reproduction task for the formal
`shadow geometry paper.docx` source previously inspected at:

`/Users/andrewmureddu/Library/Mobile Documents/com~apple~CloudDocs/shadow geometry paper.docx`

## Work Completed

- Added `simulations/shadow_geometry_reproduction/README.md`.
- Added `simulations/shadow_geometry_reproduction/shadow_geometry_reproduction.py`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/reproduction_summary.csv`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/protection_factor.csv`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/decoherence_t2.csv`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/lindblad_dfs.csv`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/approximate_kl_defect.csv`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/lyapunov_floor.csv`.
- Generated:
  `simulations/shadow_geometry_reproduction/outputs/shadow_geometry_reproduction.png`.
- Added `audits/shadow_geometry_reproduction_audit.md`.
- Updated OP-16 in `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Reproduced Results

The suite recreated six claims that the paper specifies well enough to test:

| Claim | Result |
|---|---:|
| projection protection \(\beta(3)=2/3\) | pass |
| dark-state full-loop Berry phase \(\pi\) | pass |
| standard \(T_2\) dephasing law | pass |
| exact DFS Lindblad cancellation | pass |
| approximate Knill-Laflamme defect bound | pass |
| Lyapunov 99.1% calibration floor | pass |

Run output:

```text
PASS: projection protection beta(3) -> measured 0.665391482832 (2/3)
PASS: dark-state full-loop Berry phase -> measured 3.14159265359 (pi mod 2pi)
PASS: standard T2 dephasing law -> measured 0.135335283237 (exp(-2) at t=1)
PASS: exact DFS Lindblad cancellation -> measured 0 (aligned dissipator norm 0)
PASS: approximate Knill-Laflamme defect bound -> measured 0.746220604703 (defect <= perturbative bound)
PASS: 99.1% Lyapunov calibration floor -> measured 0.009 (eta*/(1-q*) = 0.009)
```

## Reproduction Boundary

The original SACR 99.1% simulation floor is **not independently reproduced**.
What is reproduced is the calibration equation:

$$
V_\infty=\frac{\eta^*}{1-q^*}=0.009,
$$

which corresponds to a 99.1% sector-population floor. To reproduce the actual
protocol claim, the project still needs the missing full cycle map:

1. protected state/code family;
2. syndrome or ancilla measurement circuit;
3. alignment-control operation;
4. constrain/release operation;
5. physical noise model and parameter values;
6. exact definition of "coherence floor."

## Takeaway

The repaired formal paper is usable as a collection of standard open-system and
QEC-calibration facts. It should not be used as evidence that SACR already
achieves the reported floor. It should be used as a specification for what a
future explicit active-alignment protocol must satisfy.

