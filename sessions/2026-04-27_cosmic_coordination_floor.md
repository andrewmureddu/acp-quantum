# 2026-04-27 — Cosmic Coordination Floor

## Prompt

Andrew extended the singularity-inadmissibility direction into a quantum-gravity
program: quantum gravity should not merely resolve singularities after they
appear, but enforce the cosmic coordination floor that prevents inadmissible
collapse.

## Work Completed

- Added `bridges/cosmic_coordination_floor.md`.
- Added `simulations/cosmic_coordination_floor/`.
- Updated `bridges/singularity_inadmissibility.md` to point to the new program
  note.
- Added OP-19 to `OPEN_PROBLEMS.md`.
- Updated `STATUS.md`.

## Main Formal Move

The program now starts from relational gravitational macrostates:

$$
m
=
\left[
\Sigma,\,
q_{ab},\,
K_{ab},\,
\phi,\,
\pi_\phi
\right]_{\mathrm{Diff}(\Sigma),\,\ell}.
$$

The note explicitly includes \(K_{ab}\) or \(\pi^{ab}\), because a spatial
3-geometry alone is not enough initial data for gravitational evolution.

A candidate quantum-gravity theory must induce a coarse transition kernel

$$
P_{\ell,\Delta}(m'|m)
$$

and corresponding future entropy

$$
H_{\ell,\Delta}(m)
=
-
\sum_{m'\in\mathcal M_\ell}
P_{\ell,\Delta}(m'|m)
\log P_{\ell,\Delta}(m'|m).
$$

## Selection Criteria

The bridge states three criteria:

1. **Cosmic coordination floor:** nontrivial collapsing regions satisfy
   \(H_{\ell,\Delta}(m)\geq H_{\mathrm{floor}}>0\).
2. **Redistribution trigger:** when collapse approaches the floor, the
   effective dynamics must leave the classical reinforcement basin.
3. **Decodable redistribution:** the transfer must be visible to asymptotic
   observers, formalized by a mutual-information lower bound between interior
   macro-information and outgoing records.

## Toy Model

Added a finite stochastic model with three policies:

- `naked_collapse`: allows probability mass to leak into the singular state.
- `hard_exclusion`: excludes singular histories but does not redistribute
  coordination.
- `horizon_transfer`: triggers near the floor, moves mass away from the
  singular boundary, and emits decodable exterior records.

Default output:

```text
hard_exclusion: min_H=1.270, min_adm=1.000, max_sing=0.000, final_I=0.000, first_violation=30
horizon_transfer: min_H=4.573, min_adm=1.000, max_sing=0.000, final_I=3.000, first_violation=-1
naked_collapse: min_H=4.573, min_adm=0.021, max_sing=0.256, final_I=0.000, first_violation=7
```

## Status

The ACP/Schur singularity-inadmissibility result remains formal. The quantum
gravity program is conjectural but now has a concrete mathematical checklist:
macrostate kernel, floor, trigger, and visibility/decodability. OP-18 and OP-19
are now partial+.

## Next Step

Replace the finite stochastic skeleton with a relational macrostate kernel tied
to semiclassical collapse variables, then prove the classical failure theorem
under explicit focusing assumptions.
