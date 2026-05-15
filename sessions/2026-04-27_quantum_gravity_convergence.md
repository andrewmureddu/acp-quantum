# 2026-04-27 — Quantum-Gravity Convergence Map

## Prompt

Andrew asked to continue building out quantum gravity using web search to find
convergence: map what people are doing, identify what they are not doing quite
right, and look for existing work that ACP can build on.

## Work Done

- Read `STATUS.md` and `OPEN_PROBLEMS.md`.
- Searched current quantum-gravity work across:
  - holographic quantum error correction and tensor-network codes;
  - islands, Page curves, quantum extremal surfaces, and Hawking-radiation
    entropy;
  - quantum reference frames, crossed-product observable algebras, and
    relational quantum geometry;
  - regular black holes, Wheeler-DeWitt singularity resolution, loop-inspired
    effective black holes, and asymptotic-safety black-hole phenomenology.
- Added `bridges/quantum_gravity_convergence_map.md`.
- Updated `STATUS.md`.
- Added OP-20 to `OPEN_PROBLEMS.md`.

## Main Result

The convergence is real. The field is already moving toward an ACP-shaped
constraint:

- holography: bulk information behaves like logical data encoded in boundary
  degrees of freedom;
- islands/Page curves: black-hole evaporation is becoming a decodability
  problem;
- relational observable algebra: physical access is defined by
  system-plus-reference-frame invariant observables;
- regular black holes: singular endpoints are increasingly treated as failures
  to be replaced by finite quantum-corrected structure.

The ACP addition is a cross-mechanism admissibility filter:

$$
\mathcal A_{\mathrm{rel}}
\to
P_{\ell,\Delta}(m'|m)
\to
H_{\ell,\Delta}(m)
$$

with boundary mutual-information diagnostics:

$$
I(G;R_+,R_0)>0,
\qquad
I(X_R;Y_{\partial})>0
$$

and early logical privacy:

$$
I(\mathrm{interior\ microstate};R_{\partial}^{\mathrm{early}})
\approx 0.
$$

## Field Blind Spots Identified

1. Regularity without recoverability.
2. Entropy accounting without a general mechanism-selection rule.
3. Algebraic observables without persistence dynamics.
4. Positive-signal phenomenology without structured null-record inference.
5. Static holographic codes rather than adaptive boundary alignment.

## Next Step

Build OP-20: a relational observable macrostate kernel. The strongest route is
to start from quantum-reference-frame / crossed-product observable algebras and
define finite relational macrocells \(m\in\mathcal M_\ell\), then compute
\(P_{\ell,\Delta}(m'|m)\), \(H_{\ell,\Delta}(m)\), and the boundary mutual
information diagnostics.

The simulation-side next step is to upgrade
`simulations/dark_constraint_wave_interference/` from a hidden phase bump to a
weak metric/lensing perturbation and measure how much bright plus dark records
reduce posterior uncertainty over the metric sector.
