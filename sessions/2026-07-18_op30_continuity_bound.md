# Session log — 2026-07-18 — OP-30(a) continuity bound

## Intent

Seventh pull on the braided-clock thread: prove the OP-30(a) continuity
bound — nearly transparent record channels are nearly clock-blind — and
verify it exactly.

## What was proved

Added to `bridges/clock_syndrome_record_splitting.md`:

- **Definition 3.** \(\epsilon\)-transparent instrument via the Kraus
  defect \(D_r(\theta)=[M_r,U_\theta]P\) and aggregate
  \(\epsilon^2=\sum_r\sup_\theta\|D_rP\|_\infty^2\); controlled by the
  commutator with the clock generator alone when \([M_r,P]=0\).
- **Lemma 5.1.** Single-step total variation
  \(\mathrm{TV}(p_\theta,p_0)\le\epsilon+\epsilon^2/2\), by expanding the
  outcome probabilities around the transparent case and applying
  Cauchy-Schwarz twice.
- **Proposition 5.** For adaptive record-conditioned sequences,
  \(I(\Theta;R)\le2\tau\log_2|\mathcal R|+h_2(2\tau)\) with
  \(\tau=\sum_i(\epsilon_i+\epsilon_i^2/2)\), via a hybrid argument plus
  Fannes-type entropy continuity. Proposition 1 is recovered as
  \(\epsilon\to0\).

## What the exact verification taught

Experiment F (exact 8x8 matrices, full record-branch enumeration, no
Monte Carlo; outputs `braiding_clock_continuity_scan.csv` and
`braiding_clock_continuity_curves.png`):

1. **Abelian clock-blindness.** The physically natural miscalibration —
   measuring \(VS_1V^\dagger\) with \(V=e^{-i\mu Z_1/2}\) — has nonzero
   commutator defect (up to `0.246`) but exactly zero clock information
   for every \(\mu\) and both \(n=1\) and \(n=8\). Reason: all Kraus
   products lie in \(\mathrm{span}\{I,A\}\) and \(PAP\propto P\), so
   every record POVM element is a scalar on the code sector. Proposition
   5 is satisfied but infinitely loose; the sharper defect should be a
   distance of the code-compressed Kraus algebra from the scalars. Folded
   into OP-30.
2. **True rate vs proved rate.** The axis-leak instrument
   (\(B_\mu=\cos\mu\,S_1+\sin\mu\,\bar Z\)) reads the clock with
   \(I\propto\mu^2\) (`0.00051 / 0.0020 / 0.0079 / 0.029` bits at
   \(\mu=0.05\)-\(0.4\), \(n=1\)) and linearly in \(n\) — the true
   accumulation is \(O(n\epsilon^2)\) against the proved
   \(O(n^2\epsilon)\). All 20 cells satisfy the bound with margin.
3. **Constructor subtlety worth remembering.** Building the weak
   measurement from sign projectors of \(B_\mu\) silently discards the
   logical tilt, because \([S_1,\bar Z]=0\) makes
   \(\mathrm{sign}(B_\mu)=S_1\) for \(\mu<\pi/4\). The correct pair is
   \(M_s=\sqrt{(I+s\kappa B_\mu)/2}\), which reduces to the projector
   form for involutions.

## Files touched

- `bridges/clock_syndrome_record_splitting.md` (Definition 3, Lemma 5.1,
  Proposition 5, revised Remark 3, updated OP-30 section).
- `simulations/quantum_braiding_clock/` (Experiment F, README, two new
  outputs).
- `OPEN_PROBLEMS.md` (OP-30 to open/partial+).
- `STATUS.md` (changelog).

## Next steps

- OP-30(a) refinements: algebraic defect (distance of the compressed
  Kraus algebra from the scalars) and the \(O(n\epsilon^2)\) rate.
- OP-30(b): covariant-code reconciliation.
- OP-23: measured-trace replay for a clocked code.
