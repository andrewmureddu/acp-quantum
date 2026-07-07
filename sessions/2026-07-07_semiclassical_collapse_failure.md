# Session Log — 2026-07-07 — Semiclassical Collapse Failure Theorem

## Goal chosen

STATUS.md, OP-18, OP-19, and OP-20 all named the same next hard step for the
highest-priority front: strengthen the modest classical-collapse failure
proposition (Proposition 2 of
`bridges/relational_observable_macrostate_kernel.md`) into a real theorem
under explicit semiclassical focusing assumptions. That was this session's
target.

## What was done

### 1. `proofs/semiclassical_collapse_failure.md` (new)

The Stage 2 theorem of the quantum-gravity derivation ladder. Structure:

- **Assumptions F1–F6:** classical Einstein flow with NEC matter; trapped
  bins (cell membership implies a closed future-trapped surface with
  \(\theta_+\leq-\alpha\)); Penrose causality inputs; fixed description (no
  adjoined variables, records, or stochastic rules); relational clock
  compatibility (finite verification image of the focusing interval);
  nondegenerate cell measure.
- **Lemma 1 (focusing bound):** null Raychaudhuri comparison gives expansion
  blowup at affine parameter \(\lambda^*\leq 2/\alpha\). Proven.
- **Lemma 2 (incompleteness):** Penrose's theorem, imported and labeled as
  such.
- **Lemma 3 (full-measure failure):** trappedness as a bin property makes the
  failing set the whole cell; openness/Cauchy stability makes trapped cells
  non-degenerate in the data topology.
- **Lemma 4 (admissibility exit):** incompleteness exits admissibility by
  finite observables (curvature blowup), finite continuation (inextendible
  MGHD), or determinism failure (extendible MGHD, censorship-violating case —
  handled without deciding strong cosmic censorship); the Schur interior
  block degenerates in every case.
- **Lemma 5 (exhaustiveness):** the classical description admits exactly
  three kernel constructions — naked pushforward, hard exclusion, terminal
  absorption.
- **Theorem 1 (quantitative failure):** naked loses normalization with
  \(Z=1-\mu_m(\tau_{\mathrm{fail}}\leq\Delta)\to 0\) at \(\Delta^*\); hard
  exclusion is postselection with divergent discarded coordination
  \(-\log Z\) and zero boundary record of the discarded branch; absorption
  crystallizes exactly (\(H=0\)) on active cells.
- **Theorem 2 (no-go):** no classical kernel construction satisfies classical
  consistency, normalization, record balance, and the floor simultaneously.
- **Corollary 1 (horizon deferral):** exterior restriction is admissible as a
  permanent-horizon idealization; semiclassical evaporation (marked as an
  import) removes that idealization, so the trichotomy reappears in the
  exterior algebra at the decoding scale.
- **Corollary 2 (forced completion):** any admissible continuation must be
  mechanism-changing before floor breach, normalization-preserving, and
  boundary-decodable — the Stage 3 object. Early privacy remains an axiom
  from Stage 6, not a consequence.
- **Referee seams section:** F5 (clock), F2 (bin design), pointwise NEC,
  extendible MGHDs, measure choice — ranked by expected severity.

The honesty boundary is explicit: classical-GR inputs are imported, the
kernel-level arguments are proven given them, and the identification of the
forced completion with quantum gravity remains the program's conjecture.

### 2. `simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py` (new)

Numerical companion, stdlib-only, seeded. Results:

```text
focusing samples: 400
lambda* <= 2/alpha violations: 0
lambda* <= 2/|theta0| violations: 0
Z(Delta) monotone nonincreasing: True
Z(Delta*) = 0.000000
exclusion entropy: 3.6174 bits (early) -> 0.0000 bits (last surviving grid point)
absorption channel future entropy: 0.000000 bits by construction
```

Outputs: `raychaudhuri_focusing_check.csv`, `raychaudhuri_mass_loss.csv`,
`raychaudhuri_floor_check.svg`. The script asserts all four theorem-derived
claims and fails loudly if any breaks.

### 3. Document updates

- `bridges/relational_observable_macrostate_kernel.md`: status header,
  companion list, strengthened-version note after Proposition 2, updated
  next-step framing.
- `bridges/quantum_gravity_derivation_program.md`: Stage 2 marked proven at
  the finite relational-kernel level; honesty boundary, anchors, and
  near-term work updated.
- `bridges/cosmic_coordination_floor.md`: Stage B marked done; proven/open
  summary updated.
- `bridges/singularity_inadmissibility.md`: §9 records that the first hard
  formal target is met.
- `OPEN_PROBLEMS.md`: OP-18 → Partial++, OP-19 → Partial+++, OP-20 →
  Partial++, each with the theorem pointer and refreshed next steps.
- `STATUS.md`: focus block, active front 1, headline OP lines, changelog.
- `simulations/cosmic_coordination_floor/README.md`: companion script
  documented with its seeded results.

## Honest assessment

The theorem is a genuine strengthening, not a relabeling: the failing set is
derived rather than assumed, the failure is quantitative, and the
exhaustiveness lemma converts a disjunction about one kernel into a no-go
over all classical constructions. But its geometric core is imported
classical GR — the ACP contribution is the admissibility framing, the
record-balance failure mode of hard exclusion, the exact-crystallization
reading of absorption, the horizon deadline, and the forced-completion
corollary. The weakest assumptions are F5 (interior/comoving relational
clock; the exterior story is only rescued by the semiclassical evaporation
import) and F2 (coarse bins implying pointwise trappedness — provable in
spherical symmetry, assumed with margin generally). Both are flagged in the
document.

## End state / next step

Stage 2 of the derivation ladder is closed at the finite-kernel level. The
highest-value next step is the completion half of OP-19/OP-20: instantiate
candidate completion kernels (holographic/QEC decoder-style, loop/effective
bounce, asymptotic-safety interior, fuzzball ensemble) as explicit stochastic
kernels on the macrocell space and audit them against the six
candidate-mechanism tests of the kernel bridge §10. Secondary refinements:
averaged/quantum focusing conditions in F1, and the OP-29 operational-time
covariance theorem that F5 imports.
