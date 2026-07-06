# Session log — 2026-07-06 — Operational state space from ACP record statistics (G1a)

## Context

Same-day continuation of the quantum-foundations session
(`sessions/2026-07-06_hilbert_geometry_from_acp.md`). Andrew green-lit the
recommended next step: attack gap G1 (why prediction states carry linear
structure at all) operationally, by proving that ACP-admissible record
statistics force the convex state space that every operational reconstruction
of quantum theory assumes as its starting frame.

## What was done

1. **New bridge:** `bridges/operational_state_space_from_acp.md`.
   - Setup: preparations, a finite set of record channels with finite
     alphabets at resolution \(\ell\), the fiducial embedding
     \(\Phi(P)=(p(o\mid P,M))\in[0,1]^N\).
   - Axioms with ACP motivations: OS-1 reproducible record statistics
     (persistent boundary law), OS-2 record-native identification (states are
     record-equivalence classes; reality-reflective admissibility), OS-3
     non-disturbing classical randomization (coordination-neutral coins;
     ⚠ non-disturbance flagged as a real assumption, sibling of TP-1), OS-4
     finite fiducial capacity (sibling of HG-2), OS-5 statistical completion
     (⚠ idealization; only compactness depends on it).
   - **Lemma 4.1 (proved):** mixing is affine — the convex structure *is* the
     law of total probability over a decodable, non-disturbing classical
     record.
   - **Theorem 4.2 (proved):** the state space is a nonempty compact convex
     subset of \([0,1]^N\).
   - **Theorem 4.4 (proved):** cone lift — the state space generates an
     ordered finite-dimensional vector space with closed generating cone and
     order unit \((V,C,u)\); every affine functional extends uniquely to a
     linear one (well-definedness argument via positive/negative part
     splitting and convexity); admissible outcome functionals become effects
     \(0\le\hat e\le u\) with per-channel completeness. This is the GPT frame
     derived rather than postulated.
   - **Theorem 5.2 (proved):** record-capacity bounds — jointly perfectly
     distinguishable states are bounded by the distinguishing channel's
     alphabet and are affinely independent, hence bounded by
     \(\dim_{\mathrm{aff}}(K)+1\); the record capacity
     \(N_{\mathrm{dist}}(\ell)\) is finite. Read as the coordination floor in
     kinematic form.
   - **Propositions 6.1–6.2 (proved):** the state space is a singleton iff
     every record channel is preparation-independent iff all
     preparation-record mutual informations vanish; both ACP absorbing
     boundaries (dissolution and crystallization) are operational singletons,
     distinguishable only dynamically; the productive interval therefore
     requires positive affine state-space dimension. Gap flagged: positive
     mutual information gives distinct states, not perfectly distinguishable
     ones — sharpness (\(N_{\mathrm{dist}}\ge2\)) is a separate lemma target.

2. **Cross-references:** update paragraph in
   `bridges/hilbert_geometry_from_acp.md` §10 splitting G1 into G1a (closed
   at framework level by this note) and G1b (convex state space → branch
   vector space via the §7 reconstruction rows).

3. **Trackers:** OP-21 statement and status extended in `OPEN_PROBLEMS.md`
   ("Partial++++ (G1a closed at framework level)"); STATUS front 7, OP-21
   headline, and changelog updated.

## Honesty boundary

- Proved: Lemma 4.1, Theorems 4.2/4.4, Theorem 5.2, Propositions 6.1/6.2,
  given OS-1–OS-5.
- Flagged: OS-3 non-disturbance and OS-4 finiteness are ACP-motivated, not
  CDT-derived; OS-5 is an idealization; nothing in the note separates quantum
  from classical — it derives their common convex-linear frame (classical
  probability satisfies OS-1–OS-5 with a simplex state space). The
  quantum/classical fork is G1b.

## Next steps (recorded in the bridge's §10)

1. Sharp-records lemma: derive \(N_{\mathrm{dist}}(\ell)\ge2\) inside the
   productive interval (asymptotic-repetition sharpening).
2. Derive OS-3 non-disturbance from coordination-neutral composition.
3. Composite systems and local decodability (entry point for HG-C1).
4. Purification row of the reconstruction table from restraint-power
   conservation — the highest-value single target now that the GPT frame is
   derived.
