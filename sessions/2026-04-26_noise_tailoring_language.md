# 2026-04-26 — Noise-Tailoring Language Pass

## Summary

Andrew clarified that the project should not be attached to the slogan "noise
as signal"; the function matters more than the name. Translated the core idea
into current quantum-information terminology and updated the project language
accordingly.

## Domain-Language Translation

The professional phrasing is:

- noise-tailored or noise-adapted encoding;
- symmetry-adapted decoherence-free-subspace encoding;
- correlated-noise or biased-noise QEC;
- syndrome-bearing environment fragments;
- detectable versus undetectable error components;
- logical information leakage to the environment.

The project phrase is now "noise-tailored quantum persistence" rather than
"structured noise as signal."

## Changes

- Retitled `bridges/quantum_noise_as_signal.md` internally as
  "Noise-Tailored Encoding in a Two-Qubit Decoherence-Free Subspace."
- Rewrote the abstract, motivation, interpretation, feedback, limitations, and
  conclusion language around noise-tailored QEC rather than slogan-level ACP
  language.
- Added a recent-literature positioning section connecting the note to:
  DFS-QECC concatenation, bias-tailored Floquet/stabilizer codes, subspace noise
  tailoring, and Pauli-noise characterization.
- Replaced ACP-style CSV regime labels with technical labels:
  `no_syndrome`, `leakage_limited`, `transition`, and `noise_tailored`.
- Renamed the score column to `noise_tailored_score`.
- Regenerated the noise-tailoring simulation outputs.
- Updated `README.md`, `STATUS.md`, `AGENTS.md`, `CLAUDE.md`, and
  `simulations/noise_as_signal/README.md`.

## Next Step

The next technical step remains the channel-native upgrade: replace the
classical Gaussian environment-fragment diagnostic with an explicit quantum
dilation, then compute entanglement fidelity or coherent information for the
DFS-adapted and unadapted encodings.
