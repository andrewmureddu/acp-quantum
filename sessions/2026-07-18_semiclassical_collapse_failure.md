# Session log — 2026-07-18 — semiclassical collapse failure theorem

## Intent

Direction chosen autonomously: attack the derivation program's central
unproved claim (OP-18/OP-19 "prove the stronger semiclassical collapse
failure theorem") at the level where it is actually provable now — the
relational macrocell kernel — with the physics isolated into one named
assumption so the mathematics is complete and the remaining gap is a
single precisely-stated lemma.

## What was proved

`proofs/semiclassical_collapse_failure.md`:

- **Setting.** Finite admissible macrocells with compactness
  \(C\in[0,1)\), absorbing inadmissible endpoint at \(C=1\)
  (singularity inadmissibility), admissibility margin \(B=1-C\).
- **Assumptions.** (A1) focusing drift
  \(\mathbb E[B_{t+1}|\mathcal F_t]\le B_t-\delta\) on trapped cells —
  the kernel shadow of Raychaudhuri focusing; (A2) bounded increments;
  (A3) mechanism stationarity (the "purely semiclassical" hypothesis
  under refutation); (A4) trapped start.
- **Theorem 1.** (i) \(\mathbb E[T]\le B_0/\delta\) and retained
  admissible mass \(\le B_0/(\delta n)\to0\): normalization failure is
  total. (ii) Survival probability decays exponentially (Azuma), so the
  postselected survivor theory conditions on an exponentially unnatural
  branch, diverges from the physical channel in total variation, and is
  record-free about the discarded coordination by construction.
  (iii) Survivor-branch entropy floor breach under a concentration
  hypothesis, flagged ⚠ as observed-in-toy rather than proved in
  general.
- **Theorem 2 (completion trigger).** Any kernel family that is
  normalized, floor-respecting, and drift-obeying outside a core must
  change mechanism strictly before the singular threshold; the drift must
  already fail on the whole final band, \(C_{\mathrm{trig}}\le1-\delta\).
  This is the kernel-level skeleton of the project thesis: persistence
  forces a completion.
- **OP-19a named.** The drift transfer lemma — derive (A1) from
  semiclassical focusing for an explicit initial-data family, coarse map
  \(\sigma_\ell\), and operational step \(\Delta\) — is now the single
  remaining conditional in the Stage 2/3 argument, and is where the
  OP-29 clock choice enters the gravitational story.

## Honesty posture

The theorems are unconditional mathematics over their assumptions;
nothing gravitational is claimed as proved. The masthead states this, the
kernel bridge marks Proposition 2 as superseded with the gap named, and
the derivation program anchor lists OP-19a explicitly.

## Numerical anchors

The macrocell collapse toy realizes every branch: naked collapse retains
`0.001` admissible mass (total failure, not marginal); hard exclusion
breaches the floor at step 22 with `0.205` bits (branch-3 concentration);
horizon transfer and quantum completion are Theorem 2 triggers, emitting
geometry-central records with the interior clock censored until the
transfer step.

## Files touched

- `proofs/semiclassical_collapse_failure.md` (new).
- `bridges/relational_observable_macrostate_kernel.md` (Proposition 2
  superseded note).
- `bridges/quantum_gravity_derivation_program.md` (anchor).
- `OPEN_PROBLEMS.md` (OP-18 partial++, OP-19 partial+++ with OP-19a).
- `STATUS.md` (changelog).

## Next steps

- OP-19a, the drift transfer lemma — now the sharpest single target in
  the derivation program.
- Candidate-theory kernels for the Theorem 2 trigger regime (OP-20
  candidate-mechanism audit).
