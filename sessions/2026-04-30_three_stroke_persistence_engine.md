# 2026-04-30 — Three-Stroke Persistence Engine Triage

## Prompt

Andrew added a new manuscript to `paper/` and asked whether it was relevant.

## Work Completed

- Read `STATUS.md`, `OPEN_PROBLEMS.md`, and the new draft.
- Identified `paper/three_stroke_persistence_engine.md` as relevant to the coordination-neutrality / OP-7 thread, not as a replacement for the active main paper.
- Moved it to `bridges/three_stroke_persistence_engine.md`, restoring the `paper/` invariant that only `paper/acp_main_v10.md` lives there.
- Added a status note classifying the document as an exploratory bridge draft.
- Corrected ACP naming from "Adaptive Coherence Principle" to "Anti-Crystallization Principle."
- Weakened the wreath-composition claim to an open target consistent with `bridges/coordination_neutrality.md`.
- Corrected the local \(\alpha=0\) critical value from approximately `0.3934` to approximately `0.3994`.
- Repaired the local antisymmetric-variance section: the injection stroke preserves the symmetric coordinate at leading order, and the previous calculation had used \(\varepsilon=0.010\) as if \(\varepsilon^2=0.01\).
- Updated `STATUS.md`.
- Updated OP-7 in `OPEN_PROBLEMS.md` to include the three-stroke bridge as an adjacent but provisional route.

## Assessment

The draft is relevant, but it is not part of the active noise-tailored quantum-persistence front. Its strongest contribution is the operator-level slogan:

> stability is not persistence.

In ACP terms, a CN/EML two-stroke cycle can stabilize or slow collapse, but it still tends toward an attractor. The proposed third stroke, \(N_\varepsilon(x,y)=(xe^{\varepsilon\xi},ye^{-\varepsilon\xi})\), is useful because it preserves the geometric-mean coordination center while restoring antisymmetric coordination variance.

## Remaining Work

- Add `simulations/three_stroke_persistence_engine/` with a reproducible NumPy harness before treating the numerical plateau claims as established.
- Audit the hierarchical block-swap / wreath-symmetry claim separately from full tree-CN preservation.
- Decide whether the three-stroke architecture is best kept as an OP-7 companion note or eventually folded into `bridges/coordination_neutrality.md`.
