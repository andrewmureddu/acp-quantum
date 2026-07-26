# Session: Stage 5 — Boundary Decodability

**Date:** 2026-07-26
**Front:** ACP quantum-gravity derivation program (priority: highest)
**Closes:** Stage 5 of the derivation ladder; Criterion 3 and Conjecture 3 of
the coordination-floor note
**Continues:** `sessions/2026-07-26_op30_frame_rank_dichotomy.md`

## What was chosen

With Stage 2 proven and OP-30 closed, Stage 5 — boundary decodability — was the
next unproven rung. It appeared in three places as an *assumption*: Criterion 3
of `bridges/cosmic_coordination_floor.md`, Conjecture 3 of the same note, and
Stage 5 of the derivation program. In each it was a selection rule that
admissible mechanisms must satisfy, with no argument that anything forces it.

## The move

One exact identity does the work. For a pure tripartite state on
(reference, boundary record, hidden sector):

$$
I(X_R;Y_\partial)+I(X_R;S)=2\,S(X_R).
$$

Elementary to prove — purity gives \(S(X_RY_\partial)=S(S)\) and
\(S(Y_\partial)=S(X_RS)\), and the two mutual informations add with those terms
cancelling. The content is not the proof but the recognition that ACP's two
record conditions are the two sides of it.

**This dissolved an apparent tension I had not previously noticed was
dissolvable.** Stage 6 demands early privacy; Stage 5 demands late
decodability. These read as separate requirements needing reconciliation.
Lemma 5 says they are one requirement about *when* a conserved budget has
moved. There is nothing to reconcile.

From there:

- **Theorem F.** Criterion 3 is not an independent axiom — it is equivalent to
  requiring the hidden share of \(2S(X_R)\) to vanish. And Conjecture 3 becomes
  a theorem: a sector permanently retaining \(I(X_R;S)\geq\delta\) leaves
  \(I(X_R;Y_\partial)\leq2S(X_R)-\delta\) *for all time*, so no boundary decoder
  works at any time, however long \(T_{\mathrm{dec}}\) is taken. The budget is
  conserved and the hidden share never returns.
- **Corollary F1.** Finite-record admissibility — already required by
  `bridges/singularity_inadmissibility.md` §2 — forces
  \(\log\dim\mathcal H_S\to0\), hence \(I(X_R;S)\to0\), hence full decodability.
  And by purity \(S(Y_\partial)\leq S(X_R)+\log\dim\mathcal H_S\to S(X_R)\), so
  the record entropy must rise, peak, and come back down.

  **The Page curve is forced, not assumed.** That is the second known
  quantum-gravity structure the program has found to be a consequence of ACP
  admissibility rather than an import.
- **Corollary F2.** Capacity bounds — universally the boundary channel must be
  at least as wide as the protected information; under scrambling the hidden
  capacity must fall below the boundary capacity by at least \(S(X_R)\).

## Numerics

`simulations/boundary_decodability/` computes **exact** reduced density
matrices and **exact** von Neumann entropies — no proxy scores, which matters
because the whole claim is an identity between information quantities. Needed a
Jacobi eigensolver, applied to the real symmetric embedding
\([[A,-B],[B,A]]\) of the Hermitian RDM, which carries each eigenvalue twice.

Reference 1 qubit, collapsing region 9 qubits, Haar-random global state, 6
samples.

| released | \(S(Y_\partial)\) | \(I(X_R;Y_\partial)\) | \(I(X_R;S)\) | sum | \(2S(X_R)\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.0000 | 0.0000 | 1.9968 | 1.9968 | 1.9968 |
| 3 | 2.9519 | 0.1370 | 1.8598 | 1.9968 | 1.9968 |
| 5 | **4.2742** | 1.4543 | 0.5425 | 1.9968 | 1.9968 |
| 7 | 2.9578 | 1.9647 | 0.0321 | 1.9968 | 1.9968 |
| 9 | 0.9984 | 1.9968 | 0.0000 | 1.9968 | 1.9968 |

1. **Lemma 5 holds to `2e-08` bits.** The two mutual informations are computed
   independently — \(S(X_R\cup Y_\partial)\) directly rather than via purity —
   so the constant sum is a genuine check and validates the code.
2. **Page turnover confirmed**: peak `4.2742` bits at exactly half the total,
   final value `0.9984` = \(S(X_R)\) to four decimals, exactly as F1(2)
   predicts.
3. **Remnant threshold lands where F2(b) predicts**: decodable fraction crosses
   one half between `r=4` (0.728) and `r=5` (0.269). The crossover is smooth
   from finite-size Page corrections; the symmetry of those two values about
   the threshold is Lemma 5 again.
4. **Independent validation**: the measured curve matches Page's analytic
   \(\langle S_A\rangle\approx\ln d_A-d_A/2d_B\) to within 0.010 bits at every
   point, typical deviation 0.003.

## Where I held back

Corollary F2(b), the scrambling capacity threshold, is stated as **conditional
and not universally necessary**. A completion that deliberately swaps the
protected qubit into the record first achieves decodability with an arbitrarily
small boundary — Haar scrambling is typical, not optimal. It is the operative
constraint for a fast-scrambling interior, which is the black-hole case and
exactly what remnant and baby-universe proposals posit, so it is the right test
to apply to them. It is not a theorem about all conceivable mechanisms and
should not be quoted as one.

Lemma 6 (decoupling implies recoverability) is quoted with a generic modulus
rather than a specific constant. Quoting a sharp constant from memory would be
worse than not quoting one.

## What it does to the candidate audit

The criterion turns out to be insensitive to curvature and sensitive only to
whether the hidden capacity vanishes. Consequently several proposals that look
quite different geometrically are the same proposal informationally: a bounce
into a causally disconnected region is a baby universe under another name, and
both are excluded by Theorem F(2) for the same reason. Remnants are not
excluded as such — only when too large.

## Files touched

- **Added** `bridges/boundary_decodability.md`
- **Added** `simulations/boundary_decodability/boundary_decodability.py`
- **Added** `simulations/boundary_decodability/README.md`
- **Added** `simulations/boundary_decodability/outputs/` (2 CSVs)
- **Updated** `bridges/quantum_gravity_derivation_program.md` (Stage 5 proven;
  Stage 2 OP-30 text refreshed; anchors; near-term work)
- **Updated** `bridges/cosmic_coordination_floor.md` (Criterion 3 derived,
  Conjecture 3 proved)
- **Updated** `OPEN_PROBLEMS.md`, `STATUS.md`, `README.md`, `AGENTS.md`

## Next

1. **Bound \(T_{\mathrm{dec}}\).** Theorem F says the budget arrives; it says
   nothing about how fast. The gravitational analogue of the scrambling time is
   the natural target, and it is what would connect this note to
   `bridges/operational_time_relativity.md`, where transfer rates are the
   primitive.
2. **OP-3.** Identifying coordination capacity \(\Delta C_R\) with \(S(X_R)\)
   needs the same Schur regularity conditions as Proposition E1 of the collapse
   note. OP-3 is now load-bearing for two rungs of the ladder.
3. **Candidate completion kernels** against the three quantitative acceptance
   conditions now in hand.
