# ACP Quantum

This workspace now focuses on the quantum-gravity frontier of the **Anti-Crystallization Principle (ACP)**:

> quantum gravity is the persistence-forced completion of classical spacetime: admissible gravitational dynamics must replace singular collapse with relational, finite-record, boundary-decodable quantum channels that preserve nonzero future entropy while protecting interior logical information until the appropriate decoding scale.

The parent ACP/CDT program remains here as the theoretical base. In current project language, the goal is to derive quantum gravity, at least implicitly and eventually explicitly, from ACP admissibility, singularity exclusion, relational observability, boundary decodability, and protected interior information.

Noise-tailored QEC remains the technical engine: error/syndrome/logical-state separation in QEC is the finite laboratory for the gravitational lift from error sectors to geometry sectors, syndromes to boundary records, and logical states to protected interior degrees of freedom.

## Where to start

- **`STATUS.md`** — current state of the paper, active fronts, what's next.
- **`bridges/quantum_gravity_derivation_program.md`** — explicit derivation roadmap.
- **`proofs/classical_collapse_failure_theorem.md`** — Stage 2 theorem: the classical collapse trichotomy under explicit focusing assumptions.
- **`bridges/relational_observable_macrostate_kernel.md`** — OP-20 kernel: relational observables to macrocells, transition channels, and diagnostics.
- **`bridges/cosmic_coordination_floor.md`** — core quantum-gravity formalization program.
- **`bridges/quantum_gravity_convergence_map.md`** — map to holographic QEC, islands, relational algebras, and regular black holes.
- **`bridges/quantum_noise_as_signal.md`** — current focal technical note.
- **`simulations/hardware_adaptive_decoder/`** — current QEC/hardware scaffold.
- **`simulations/cosmic_coordination_floor/`** — current gravitational toy collapse model.
- **`AGENTS.md` / `CLAUDE.md`** — operating charter and research focus.
- **`paper/acp_main_v10.md`** — parent ACP paper.
- **`OPEN_PROBLEMS.md`** — canonical tracker of unsolved problems.

## Layout

```
paper/           the active paper (one file)
proofs/          core theorems + standalone proof documents
reductions/      six classical frameworks shown to be special cases of ACP
bridges/         quantum-gravity derivation, structural bridges, A.20 Restraint-Power + Heisenberg
simulations/     Qiskit/NumPy and dependency-free quantum/gravitational simulations
special_cases/   extended 22-domain catalog
essays/          philosophical / foundational companion pieces
audits/          integrity audits
references/      external source material
sessions/        per-session logs
archive/         frozen prior versions
```

## How this workspace is run

Andrew provides high-level direction; Codex/Claude acts as primary researcher and author with full autonomy over technical decisions and next-step selection. Everything lives in markdown. Each session starts from `STATUS.md` and, unless redirected, prioritizes the ACP quantum-gravity derivation program, using noise-tailored encoding / alignment as the technical engine.

## License

This repository is dedicated to the public domain under CC0 1.0 Universal. See `LICENSE`.
