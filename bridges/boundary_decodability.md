# Boundary Decodability

*Status: active Stage 5 bridge. Lemma 5 and Theorem F are exact and proven;
Corollary F1 follows from them plus finite-record admissibility; Corollary F2(b)
is conditional on scrambling. Conjectural only in the lift to a microscopic
quantum gravity.*

Companion notes:

- `bridges/quantum_gravity_derivation_program.md` (Stage 5)
- `bridges/cosmic_coordination_floor.md` (Criterion 3, Conjecture 3)
- `bridges/semiclassical_collapse_failure.md` (Stages 2–3, the completion corollary)
- `bridges/relational_observable_macrostate_kernel.md` §7 (the diagnostic)
- `simulations/boundary_decodability/` (numerical verification)

## 1. What This Closes

Stage 5 of the derivation ladder asserts that a completion must return
decodable coordination to the boundary:

$$
I\!\left(X_R;Y_{\partial}^{[t,t+T_{\mathrm{dec}}]}\right)
\geq
\eta\,\Delta C_R-\varepsilon .
$$

This appears in three places as an *assumption*: Criterion 3 of
`bridges/cosmic_coordination_floor.md`, Conjecture 3 of the same note ("no
permanent undecodable storage"), and Stage 5 of the derivation program. In each
it is posited as a selection rule that admissible mechanisms must satisfy.

This note derives it. The result is that Criterion 3 is **not an independent
axiom**: given closure, it is equivalent to the statement that the permanently
hidden sector's share of the protected information tends to zero, and that in
turn follows from finite-record admissibility — a condition the framework
already requires. Conjecture 3 becomes a theorem.

The engine is one exact identity. It is the same complementarity that underwrites
the QEC prototype, which is why the gravitational lift goes through cleanly.

## 2. Honesty Boundary

**Proven here.** Lemma 5 (exact, no approximation), Theorem F, Corollary F1,
and Corollary F2(a). Lemma 5 is elementary; the content is recognizing that the
ACP early-privacy and late-decodability conditions are the two sides of it, so
they are in exact trade-off rather than independent requirements.

**Cited, not reproved.** Lemma 6, decoupling implies approximate
recoverability. This is standard; it is stated with a generic modulus rather
than a specific constant because the sharp constant is not needed here and
quoting one from memory would be worse than not quoting one.

**Conditional.** Corollary F2(b), the scrambling capacity threshold. It is the
operative constraint for a fast-scrambling interior — the black-hole case — but
it is not universally necessary, and §8 says exactly why.

**Not claimed.** No derivation of Hawking radiation, the island formula, or a
microscopic evaporation mechanism. This note constrains the record channel any
completion must supply; it does not construct one.

## 3. Setup

Let \(X_R\) be a reference register purifying the protected interior
information of the collapsing region — the gravitational lift of the logical
state in the QEC dictionary. Let the completion act on

$$
\mathcal H_{\mathrm{int}}\otimes\mathcal H_{\partial}\otimes\mathcal H_{S},
$$

where \(Y_\partial\) is the boundary/exterior record accessible to asymptotic
observers and \(S\) is whatever the mechanism renders permanently inaccessible:
a remnant, a disconnected baby universe, a non-decoding horizon interior, or a
sector behind a topology change.

**Closure hypothesis (C).** The completion is a channel on
\(\mathcal H_{\mathrm{int}}\otimes\mathcal H_\partial\otimes\mathcal H_S\), and
the reference \(X_R\) is untouched by it.

(C) is not a restriction of generality — it is the statement that the
description is a description *of something*. A completion violating (C) has
already failed Theorem C branch 1 of
`bridges/semiclassical_collapse_failure.md`, since it does not define a
normalized channel on its own state space.

## 4. Lemma 5 (Record Complementarity)

**Lemma 5.** For a pure state on \(X_R\otimes Y_\partial\otimes S\),

$$
I(X_R;Y_\partial)+I(X_R;S)=2\,S(X_R).
$$

**Proof.** Purity of the tripartite state gives \(S(X_RY_\partial)=S(S)\) and
\(S(Y_\partial)=S(X_RS)\). Hence

$$
I(X_R;Y_\partial)=S(X_R)+S(Y_\partial)-S(X_RY_\partial)=S(X_R)+S(X_RS)-S(S),
$$
$$
I(X_R;S)=S(X_R)+S(S)-S(X_RS).
$$

Adding cancels \(S(S)\) and \(S(X_RS)\). \(\square\)

The identity is exact — no energy condition, no semiclassical limit, no
approximation. It says that boundary-decodable information and permanently
hidden information are not two independent quantities to be constrained
separately. They are a single conserved budget, \(2S(X_R)\), split between two
places.

**This reframes the ACP conditions.** Stage 6 requires early privacy,
\(I(L_R;R_\partial^{\mathrm{early}}\mid G_\ell)\leq\epsilon_L\), and Stage 5
requires late decodability. These read as two separate demands. Lemma 5 shows
they are one demand about *when* the budget moves: early, the interior share
must dominate; late, the boundary share must. There is no tension between them
to reconcile, and no extra assumption needed to hold them together.

## 5. Lemma 6 (Decoupling Implies Recoverability)

**Lemma 6.** If \(I(X_R;S)\leq\varepsilon\), there exists a recovery channel
acting on \(Y_\partial\) alone whose entanglement fidelity for the protected
information is at least \(1-f(\varepsilon)\), with \(f(\varepsilon)\to0\) as
\(\varepsilon\to0\).

This is the standard decoupling statement underlying quantum error correction
and the black-hole information-recovery arguments: information absent from one
side of a purification is present and recoverable on the other. It is quoted
here, not reproved.

Lemmas 5 and 6 together mean the mutual information \(I(X_R;Y_\partial)\) is
not merely a diagnostic that correlates with decodability. Up to the modulus
\(f\), it *is* decodability.

## 6. Theorem F (Boundary Decodability Dichotomy)

**Theorem F.** Assume (C). Then at every time, the protected information budget
\(2S(X_R)\) is split exactly between the boundary record and the hidden sector.
Consequently:

1. **Decodability is equivalent to hidden-share suppression.**
   \(I(X_R;Y_\partial)\geq2S(X_R)-\varepsilon\) holds if and only if
   \(I(X_R;S)\leq\varepsilon\); and by Lemma 6 the former yields an explicit
   boundary decoder.
2. **Conjecture 3 is a theorem.** If the mechanism permanently retains
   \(I(X_R;S)\geq\delta>0\), then \(I(X_R;Y_\partial)\leq2S(X_R)-\delta\) *for
   all time*, so no boundary decoder recovers the interior information at any
   time, however long \(T_{\mathrm{dec}}\) is taken. A repair that preserves
   finite curvature while storing information in a permanently hidden sector is
   therefore inadmissible — not by stipulation, but because the budget is
   conserved and the hidden share never returns.

**Proof.** Immediate from Lemma 5, with Lemma 6 supplying the decoder in
case 1. \(\square\)

**Criterion 3 is not an independent axiom.** It is the requirement that the
hidden share of a conserved budget tends to zero. The next corollary shows that
requirement is itself forced.

## 7. Corollary F1 (The Page Turnover Is Forced)

Finite-record admissibility — `bridges/singularity_inadmissibility.md` §2 and
`bridges/reality_reflective_mathematics.md` — requires a finite collapse to
leave no unbounded permanently hidden capacity. Write
\(\log\dim\mathcal H_S(t)\to0\) for that condition.

**Corollary F1.** Under (C) and finite-record admissibility:

1. **Decodability follows.** \(I(X_R;S)\leq2\log\dim\mathcal H_S\to0\), so by
   Lemma 5, \(I(X_R;Y_\partial)\to2S(X_R)\): the full protected budget reaches
   the boundary, and by Lemma 6 it is recoverable.
2. **The record entropy must turn over.** By purity,
   \(S(Y_\partial)=S(X_R\cup S)\leq S(X_R)+\log\dim\mathcal H_S\to S(X_R)\).
   Since \(S(Y_\partial)\) grows while the record is small, it must rise and
   then fall, returning to the entropy of the protected information alone.

The Page curve is therefore not an extra physical assumption imported from
black-hole thermodynamics. It is what ACP admissibility *requires* of any
finite collapse: the boundary record entropy rises, peaks, and comes back down
to \(S(X_R)\).

This is the second time the program has found a known quantum-gravity structure
to be forced rather than assumed, the first being the QEC-like code structure of
Stage 7.

## 8. Corollary F2 (Boundary Capacity Bounds)

Theorem F says *whether* information is decodable. This says *how much room the
boundary needs*.

**Corollary F2(a) — universal.** Since
\(I(X_R;Y_\partial)\leq2S(Y_\partial)\leq2\log\dim\mathcal H_\partial\),
decodability at tolerance \(\varepsilon\) requires

$$
\log\dim\mathcal H_{\partial}\ \geq\ S(X_R)-\varepsilon/2 .
$$

The boundary record channel must be at least as wide as the protected
information content. This holds for any dynamics.

**Corollary F2(b) — under maximal scrambling.** If the interior scrambles, the
typical-state (Page) values apply, and decodability holds precisely while

$$
\log\dim\mathcal H_{\partial}\ \geq\ \log\dim\mathcal H_{S}+S(X_R).
$$

*Derivation.* For a typical state, \(S(Y_\partial)\approx\min\{\log\dim\mathcal H_\partial,\ S(X_R)+\log\dim\mathcal H_S\}\)
and \(S(X_R\cup Y_\partial)=S(S)\approx\min\{\log\dim\mathcal H_S,\ S(X_R)+\log\dim\mathcal H_\partial\}\).
In the regime \(\log\dim\mathcal H_\partial\geq\log\dim\mathcal H_S+S(X_R)\)
these give \(I(X_R;Y_\partial)=S(X_R)+[S(X_R)+\log\dim\mathcal H_S]-\log\dim\mathcal H_S=2S(X_R)\),
which is the full budget. Below the threshold the hidden term dominates and the
budget stays with \(S\). \(\square\)

**Why (b) is conditional and (a) is not.** F2(b) is *not* universally
necessary: a completion that deliberately swaps the protected qubit into the
boundary record first achieves decodability with an arbitrarily small record.
Haar scrambling is typical, not optimal. So F2(b) is the operative constraint
for an interior that scrambles — the black-hole case, since black holes are
believed to be fast scramblers — and it is the right test to apply to remnant
and baby-universe proposals, which posit exactly such interiors. It is not a
theorem about all conceivable mechanisms, and it should not be quoted as one.

**What F2(b) makes quantitative.** Remnant proposals are usually assessed on
whether curvature stays finite. F2(b) supplies the missing information-theoretic
test: the permanently hidden capacity must fall below the boundary record
capacity by at least the protected information content. A remnant is not
inadmissible because it is a remnant — it is inadmissible when it is *too
large*.

## 9. Numerical Verification

`simulations/boundary_decodability/` computes exact reduced density matrices
and exact von Neumann entropies — no proxies — for a reference register
\(X_R\) (1 qubit) purifying the protected information of a 9-qubit collapsing
region, in a Haar-random global pure state, averaged over 6 samples. Hole
qubits are released to the boundary record one at a time; a completion hiding
\(r\) qubits releases only \(9-r\).

### Complementarity and the Page turnover

| released | \(S(Y_\partial)\) | \(S(S)\) | \(I(X_R;Y_\partial)\) | \(I(X_R;S)\) | sum | \(2S(X_R)\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.0000 | 0.9984 | 0.0000 | 1.9968 | 1.9968 | 1.9968 |
| 1 | 0.9974 | 1.9906 | 0.0052 | 1.9916 | 1.9968 | 1.9968 |
| 2 | 1.9876 | 2.9541 | 0.0319 | 1.9649 | 1.9968 | 1.9968 |
| 3 | 2.9519 | 3.8133 | 0.1370 | 1.8598 | 1.9968 | 1.9968 |
| 4 | 3.8095 | 4.2706 | 0.5373 | 1.4595 | 1.9968 | 1.9968 |
| 5 | **4.2742** | 3.8183 | 1.4543 | 0.5425 | 1.9968 | 1.9968 |
| 6 | 3.8267 | 2.9618 | 1.8633 | 0.1335 | 1.9968 | 1.9968 |
| 7 | 2.9578 | 1.9915 | 1.9647 | 0.0321 | 1.9968 | 1.9968 |
| 8 | 1.9912 | 0.9986 | 1.9910 | 0.0059 | 1.9968 | 1.9968 |
| 9 | 0.9984 | 0.0000 | 1.9968 | 0.0000 | 1.9968 | 1.9968 |

Entropies in bits.

1. **Lemma 5 holds exactly.** The sum column is constant at \(2S(X_R)\) to
   \(2\times10^{-8}\) bits. The two mutual informations were computed
   independently — \(S(X_R\cup Y_\partial)\) directly, not via purity — so this
   is a genuine check, and it validates the code.
2. **Corollary F1(2) is confirmed.** \(S(Y_\partial)\) rises to 4.2742 bits at
   5 released qubits, exactly half of the 10-qubit total, then falls to 0.9984
   — which equals \(S(X_R)=0.9984\) to four decimals, precisely as predicted.
3. **Corollary F1(1) is confirmed.** \(I(X_R;Y_\partial)\) rises from 0 to
   1.9968 bits, the full budget \(2S(X_R)\).
4. **Independent validation against Page's formula.** The measured curve
   matches \(\langle S_A\rangle\approx\ln d_A-d_A/2d_B\) at every point, worst
   deviation 0.010 bits (at 4 released qubits), typical deviation 0.003 bits.

### The remnant capacity threshold

Predicted admissible while \(r\leq(9-r)-S(X_R)\), i.e. \(r\leq4\).

| hidden \(r\) | released | predicted | \(I(X_R;Y_\partial)\) | decodable fraction |
|---:|---:|---|---:|---:|
| 0 | 9 | admissible | 1.9968 | 1.0000 |
| 1 | 8 | admissible | 1.9910 | 0.9971 |
| 2 | 7 | admissible | 1.9647 | 0.9839 |
| 3 | 6 | admissible | 1.8633 | 0.9331 |
| 4 | 5 | admissible | 1.4543 | 0.7283 |
| 5 | 4 | inadmissible | 0.5373 | 0.2691 |
| 6 | 3 | inadmissible | 0.1370 | 0.0686 |
| 7 | 2 | inadmissible | 0.0319 | 0.0160 |
| 8 | 1 | inadmissible | 0.0052 | 0.0026 |
| 9 | 0 | inadmissible | 0.0000 | 0.0000 |

The decodable fraction crosses one half exactly between \(r=4\) (0.728) and
\(r=5\) (0.269) — the threshold Corollary F2(b) predicts. The crossover is
smooth rather than a step because of finite-size Page corrections; the
symmetry of the two values about the threshold is Lemma 5 again.

A remnant holding half the collapsing region's qubits leaves 0.269 of the
protected information decodable. One holding two thirds leaves 0.069.

## 10. Consequences for the Candidate Audit

The audit table in `bridges/cosmic_coordination_floor.md` §8 asks of each
candidate whether information returns to \(\mathscr I^+\). That question now
has a quantitative form, and some entries change status.

| candidate | test from this note |
|---|---|
| Remnants | Admissible only if \(\log\dim\mathcal H_{\mathrm{remnant}}\leq\log\dim\mathcal H_\partial-S(X_R)\). Large remnants are excluded by Theorem F(2), not by taste. |
| Baby universes | If the disconnected sector permanently holds \(I(X_R;S)\geq\delta\), excluded outright by Theorem F(2). Disconnection is exactly the case where the hidden share cannot return. |
| Holographic unitarity | Passes by construction: \(\dim\mathcal H_S\to0\), so Corollary F1 applies and the Page turnover follows. |
| Bounces | Admissible only if the post-bounce sector remains causally connected to \(\partial\); otherwise it is a baby universe under another name. |
| Fuzzballs / microstate geometries | Passes if horizon-scale structure is exterior-accessible, since then \(S\) is empty by construction. |
| Eternal non-decoding horizons | Excluded by Theorem F(2) for a *finite* collapse. |

The through-line: the criterion is insensitive to whether curvature is finite,
and sensitive only to whether the hidden capacity vanishes. Several proposals
that look different geometrically are the same proposal informationally.

## 11. What Is Proven, Assumed, and Open

**Proven.** Lemma 5 (exact); Theorem F including the promotion of Conjecture 3
to a theorem; Corollary F1 (given finite-record admissibility); Corollary
F2(a).

**Assumed.** Closure (C), which is the statement that the completion is a
channel on its own state space; finite-record admissibility, already required
by `bridges/singularity_inadmissibility.md` §2. Lemma 6 is quoted, not
reproved.

**Conditional.** Corollary F2(b) holds for scrambling interiors and is not
universally necessary, for the reason given in §8.

**Open.**

1. *The efficiency \(\eta\) and the transfer time.* Criterion 3 is stated with
   a recoverability efficiency \(\eta\) and a finite \(T_{\mathrm{dec}}\).
   Theorem F establishes that the budget arrives; it says nothing about how
   *fast*. Bounding \(T_{\mathrm{dec}}\) — the gravitational analogue of the
   scrambling time — is the natural next target, and it is what would connect
   this note to `bridges/operational_time_relativity.md`, where transfer rates
   are the primitive.
2. *Coordination capacity versus information.* Stage 5 is stated in terms of
   \(\Delta C_R\), coordination capacity removed from the core; this note works
   with \(S(X_R)\). Identifying the two requires the Schur-block reading, whose
   regularity conditions are **OP-3** — the same gap flagged by Proposition E1
   of the collapse failure note. OP-3 is now load-bearing for two rungs of the
   ladder.
3. *Non-scrambling completions.* §8 notes that a deliberate early transfer
   beats Page. Whether any *gravitational* mechanism can do so, or whether
   horizon dynamics forces scrambling, is open and would settle whether F2(b)
   is the operative bound in general.

**Still conjectural.** That the completion these constraints describe is
quantum gravity.
