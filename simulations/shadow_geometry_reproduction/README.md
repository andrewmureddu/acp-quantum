# Shadow Geometry Paper Reproduction Suite

This suite recreates the numerically reproducible results from the formal
`shadow geometry paper.docx` source.

It does **not** validate the original reported SACR hardware/coherence-floor
simulation, because the paper does not specify the full cycle map, circuit,
noise model, or code needed to reproduce that run. Instead, it recreates the
paper's analytic/numeric claims where enough information is present.

## Reproduced Claims

- Projection protection factor:
  `beta(d) = 1 - 1/d`, with Monte Carlo confirmation and `beta(3) = 2/3`.
- Aligned dark-state Berry phase:
  the full loop for `(|0> + exp(i phi)|1>)/sqrt(2)` gives phase `pi mod 2pi`.
- Exact decoherence-free aligned code:
  scalar Lindblad action on the code gives zero dissipator.
- Standard dephasing `T2` law:
  off-diagonal coherence follows `exp(-t/T2)` with
  `1/T2 = 0.5 * sum_mu |ell_mu,i - ell_mu,j|^2`.
- Approximate Knill-Laflamme defect:
  the simulated defect stays below the paper's perturbative bound, including
  the centered second-order case.
- Lyapunov/SACR calibration:
  a discrete affine contraction with `q* = 0.9` and `eta* = 9e-4` has
  asymptotic misalignment `eta*/(1-q*) = 0.009`, equivalent to a `99.1%`
  sector-population floor.

## Run

```bash
.venv/bin/python simulations/shadow_geometry_reproduction/shadow_geometry_reproduction.py
```

## Outputs

- `outputs/reproduction_summary.csv`
- `outputs/protection_factor.csv`
- `outputs/decoherence_t2.csv`
- `outputs/lindblad_dfs.csv`
- `outputs/approximate_kl_defect.csv`
- `outputs/lyapunov_floor.csv`
- `outputs/shadow_geometry_reproduction.png`

