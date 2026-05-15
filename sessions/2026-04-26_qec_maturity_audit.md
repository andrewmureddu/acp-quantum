# 2026-04-26 — QEC Maturity Audit After SACR Reference Check

## Trigger

Andrew clarified that the goal is a mature contribution to QEC theory or
hardware practice and asked to check the file in `references/` before
continuing.

## References Checked

- `references/shadow geometry vibe guide.docx`
- `references/odrzywolek_2026_eml_operator.pdf`

The Odrzywolek PDF is about elementary functions from a binary operator and is
not directly relevant to the QEC front. The shadow-geometry guide is directly
relevant: it contains the earlier SACR active-alignment protocol narrative,
simulation claims, bug notes, parameter sweeps, and the explicit framing that
the core is DFS plus active feedback.

## Main Judgment

The project is expert-useful as a research program, but not yet a mature QEC
result. The two-qubit DFS model is clean and useful as a lemma. The mature
target must be the active protocol, reformulated in QEC-native terms:

> adaptive syndrome-space alignment under drifting structured noise.

The phrase "shadow geometry" should remain internal motivation only. Domain
experts need the formal register:

- stabilizer / subsystem codes;
- syndrome distinguishability;
- Pauli or channel covariance \(\Sigma(t)\);
- decoder likelihoods;
- logical error rates;
- entanglement fidelity and logical-channel diagnostics;
- explicit characterization and update overhead.

## Files Updated

- Added `audits/qec_maturity_audit.md`.
- Updated `STATUS.md`.
- Added OP-16 to `OPEN_PROBLEMS.md`.

## Next Best Step

Create `bridges/adaptive_syndrome_alignment.md` and define the narrow theorem
target:

Adaptive alignment helps when noise anisotropy is real, noise drift is large
enough to obsolete static tailoring, and characterization/update overhead is
smaller than the logical-error penalty of staying misaligned.

The simulation target is `simulations/adaptive_syndrome_alignment/`, comparing:

1. fixed standard code/decoder;
2. static noise-tailored code/decoder;
3. adaptive tailored code/decoder;
4. overactive adaptive protocol.

Metrics should be logical error per round, logical Pauli transfer matrix,
entanglement fidelity, and overhead-adjusted memory time.
