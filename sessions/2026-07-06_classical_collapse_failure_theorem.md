# Session 2026-07-06 — Classical Collapse Failure Theorem

## Goal

Discharge the declared next step of the quantum-gravity derivation program:
strengthen the kernel bridge's modest classical-collapse failure proposition
(Proposition 2 of `bridges/relational_observable_macrostate_kernel.md`) into a
real theorem with explicit assumptions, quantitative bounds, and an exhaustive
case analysis, and instantiate its quantities in the macrocell toy.

## What was done

1. **New proof document: `proofs/classical_collapse_failure_theorem.md`.**
   - Setting: finite relational collapse chain — a sub-stochastic kernel
     \(K(m'|m)\) on the macrocells of the OP-20 bridge with singular defect
     \(q(m)\), collapse basin, and top band defined through the binned
     relational compactness observable.
   - Focusing assumptions stated exactly: F1 (focusing drift \(\delta\) and
     band monotonicity), F2 (semiclassical concentration with terminal entropy
     scale \(H_{\mathrm{top}}\), deterministic-freeze idealization
     \(H_{\mathrm{top}}=0\)), F3 (record rigidity / classical censorship),
     F4 (mechanism rigidity).
   - Lemmas: drift hitting-time bound
     \(\mathbb E[\tau]\leq(c_K-c_\dagger)/\delta\) via optional stopping;
     geometric normalization failure via path-measure domination
     (\(K\leq\hat K\) factor by factor); entropy ceiling
     \(H_{\ell,\Delta}(m)\leq H_{\mathrm{top}}\) in the top band via the
     grouping bound.
   - Theorem 1 (classical collapse trichotomy): with probability
     \(1-\varepsilon\) by explicit time
     \(T^*(\varepsilon)\leq(c_K-c_\dagger)/(\delta\varepsilon)\), the occupied
     cell is in the top band and the description shows either strict
     sub-normalization (case a) or a sub-floor crystallized channel (case b);
     the only continuations avoiding both violate F1–F4, i.e. are mechanism
     changes.
   - Corollaries: uniformly naked collapse exhausts admissible mass with
     explicit threshold time; hard exclusion is record-free postselection that
     itself crystallizes; record starvation (the classical boundary channel
     carries at most \(H_{\mathrm{top}}\) bits/step in the top band, so the
     Stage 5 decodability requirement is unsatisfiable classically); forced
     completion (floor-respecting continuations are exactly the
     mechanism-changing, decodable redistributions).
   - Honesty boundary: the mathematics is exact and finite; the claim that
     semiclassical gravitational collapse satisfies F1–F4 (Raychaudhuri
     focusing, Penrose incompleteness, balding/no-hair, classical censorship,
     universality of the field equations) is standard physics stated as
     motivation, not proof. Deriving F1–F4 from explicit collapse
     pushforwards (Oppenheimer–Snyder, Vaidya, numerical interiors) is the
     residual OP-19 task at this rung.

2. **Simulation upgrade: `simulations/cosmic_coordination_floor/`.**
   - Added theorem-certificate diagnostics to the transition kernel:
     mass-weighted per-cell conditional future entropy
     `conditional_future_entropy_bits` (Definition 3 of the theorem — the
     quantity the entropy-ceiling lemma bounds), `mean_forward_drift` (F1
     certificate), `forward_width` (F2 certificate), and a
     `conditional_floor_violation` flag, plus matching summary columns.
   - Regenerated seeded outputs. The run instantiates both classical failure
     cases: `naked_collapse` keeps conditional entropy high (min `4.039`
     bits) while admissible mass collapses to `0.001` — case (a); `hard_exclusion`
     crystallizes the per-cell channel (`min_cond_H=0.068` bits, final forward
     width `0.0009` against compactness bin width `0.0099` — the
     deterministic-freeze endpoint), breaching the conditional floor at step
     15, seven steps earlier than the marginal-entropy diagnostic — case (b).
     `horizon_transfer` and `quantum_completion` keep conditional entropy
     above `3.5` bits with near-zero drift — the mechanism-change branch.
   - Updated the simulation README with the new metrics and summary line.

3. **Document updates.**
   - `bridges/relational_observable_macrostate_kernel.md`: Proposition 2
     marked as superseded, upgrade note added, §9 result discussion extended
     with the certificate quantities, §12 next-step text updated.
   - `bridges/quantum_gravity_derivation_program.md`: Stage 2 marked proven at
     the finite-kernel level; the proof doc added to the anchors; near-term
     work item 1 now targets deriving F1–F4 from explicit pushforwards.
   - `bridges/singularity_inadmissibility.md` §9 and
     `bridges/cosmic_coordination_floor.md` Stage B: pointers added.
   - `OPEN_PROBLEMS.md`: OP-18 → Partial++, OP-19 → Partial+++,
     OP-20 → Partial++ with updated remaining-work statements.
   - `STATUS.md`: focus line, research-focus section, front 1, changelog.
   - `CLAUDE.md` / `AGENTS.md`: proof document added to the derivation anchor
     list.

## Honest status

- **Proven (exact, finite):** the trichotomy, its lemmas, and its corollaries
  for any finite sub-stochastic kernel satisfying F1–F4.
- **Derived from ACP:** inadmissibility of case (a), crystallization reading
  of case (b), decodability/privacy requirements on the completion.
- **Motivated, not proven:** that semiclassical collapse satisfies F1–F4 with
  nontrivial constants.
- **Open:** the explicit-pushforward derivation of F1–F4; candidate completion
  kernels; everything from Stage 4 upward.

## Next highest-value steps

1. Derive F1–F4 constants \((\delta,q_0,N_{\mathrm{top}},
   \varepsilon_{\mathrm{tail}})\) for an explicit collapse family
   (Oppenheimer–Snyder or Vaidya pushforward at finite resolution).
2. Replace the schematic `quantum_completion` policy with candidate-theory
   kernels (bounce, horizon microstructure) and audit them against the six
   candidate-mechanism tests of the kernel bridge.
3. Continue the H2 → stabilizer/subsystem-code upgrade on the QEC engine
   front (OP-16/OP-23).
