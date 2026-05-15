# Shadow Geometry Paper Reproduction Audit

**Date:** 2026-04-28
**Source:** `/Users/andrewmureddu/Library/Mobile Documents/com~apple~CloudDocs/shadow geometry paper.docx`
**Reproduction suite:** `simulations/shadow_geometry_reproduction/`

## Executive Judgment

The formal shadow-geometry paper contains several results that are exactly
reproducible from the text and one major result that is not independently
reproducible from the text alone.

The reproducible core is mathematical:

- projection geometry gives \(\beta(d)=1-1/d\);
- the aligned dark-state loop has Berry phase \(\pi\) modulo \(2\pi\);
- scalar Lindblad action on a code makes the dissipator vanish;
- diagonal dephasing gives the standard \(T_2\) coherence law;
- approximate Knill-Laflamme defects obey the stated perturbative bound;
- the Lyapunov calibration target \(V_\infty=\eta^*/(1-q^*)\approx 9\times
  10^{-3}\) corresponds to a 99.1% sector-population floor.

The non-reproducible core is the original SACR simulation claim. The paper
does not specify a full CPTP cycle map, circuit, hardware noise model, random
seed, or data file for the reported 99.1% coherence floor. Therefore the suite
can recreate the calibration target but cannot validate that an implemented
SACR protocol achieved it.

## Reproduction Results

The run produced:

- `simulations/shadow_geometry_reproduction/outputs/reproduction_summary.csv`
- `simulations/shadow_geometry_reproduction/outputs/protection_factor.csv`
- `simulations/shadow_geometry_reproduction/outputs/decoherence_t2.csv`
- `simulations/shadow_geometry_reproduction/outputs/lindblad_dfs.csv`
- `simulations/shadow_geometry_reproduction/outputs/approximate_kl_defect.csv`
- `simulations/shadow_geometry_reproduction/outputs/lyapunov_floor.csv`
- `simulations/shadow_geometry_reproduction/outputs/shadow_geometry_reproduction.png`

Summary:

| Claim | Status | Comment |
|---|---|---|
| \(\beta(3)=2/3\) | reproduced | Monte Carlo estimate agrees within tolerance. |
| full-loop Berry phase \(\pi\) | reproduced | Pancharatnam product gives \(\pi\) modulo \(2\pi\). |
| exact DFS Lindblad cancellation | reproduced | Aligned dissipator norm is numerically zero. |
| \(T_2\) dephasing law | reproduced | Misaligned coherence follows \(\exp(-2t)\) for eigenvalue gap 2. |
| approximate KL defect bound | reproduced | Both noncentered and centered cases are below the paper's bound. |
| 99.1% Lyapunov floor | calibration reproduced | \(q^*=0.9,\eta^*=9\times10^{-4}\) gives \(V_\infty=0.009\). |
| original SACR simulation floor | not independently reproduced | Full cycle map and noise model are absent. |

## Interpretation

The formal paper's repaired mathematics is mostly coherent as a collection of
standard open-system and QEC facts. The strongest reusable results for ACP
Quantum are:

1. exact alignment is decoherence-free / Knill-Laflamme structure;
2. approximate alignment has a perturbative defect scale;
3. active realignment should be tested by finite-cycle contraction parameters
   \(q^*\), \(\eta^*\), and \(\eta^*/(1-q^*)\).

The paper should not be cited internally as evidence that SACR already
achieves a 99.1% coherence floor. It can be cited as defining the calibration
target that a future explicit cycle map must satisfy.

## Next Reproduction Step

To move from calibration reproduction to protocol reproduction, recover or
construct the missing implemented cycle:

1. code / state family being protected;
2. syndrome or ancilla measurement circuit;
3. alignment-control operation;
4. constrain/release operation;
5. physical noise model and parameter values;
6. output metric definition for "coherence floor."

Once those are specified, compute the full logical channel and the contraction
diagnostics \(q^*\), \(\eta^*\), and \(\eta^*/(1-q^*)\).

