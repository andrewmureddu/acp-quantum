# 2026-05-02 — Restraint Ethics

## Context

Andrew reframed the ethical center of ACP as self-restraint as load-bearing
structure: preserving the gap. The question was how to integrate that into the
theory without turning ACP into "physics proves my politics," and how to test
it.

The working interpretation is now:

> restraint ethics is a record-channel problem: legitimate power learns enough
> about public error sectors to correct harm while suppressing excess leakage
> about protected agency states.

## Work Completed

- Added `bridges/restraint_ethics.md`.
- Added `simulations/restraint_ethics/`.
- Updated `bridges/quantum_noise_as_signal.md` with the conditional-leakage
  upgrade suggested by the civil bridge.
- Updated `OPEN_PROBLEMS.md`, adding OP-24 and refining OP-15.
- Updated `STATUS.md`.

## Bridge

The new bridge defines a civil system with:

- \(E\): public error sector;
- \(L\): protected agency/logical state;
- \(R\): institutional record;
- \(C(R)\): record burden.

The diagnostic target is:

$$
I(E;R)>0
$$

while

$$
I(L;R\mid E)\approx 0,
$$

with bounded burden and nonzero future-bearing retention
\(I(L_t;L_{t+\Delta t})>0\).

This gives ACP ethics a precise two-boundary form:

- no-record / abandonment: \(I(E;R)\to 0\);
- capture / crystallization: \(I(L;R\mid E)\to H(L)\) or burden becomes too
  high;
- restraint interval: usable error information with low excess agency leakage.

## Quantum Feedback

The civil bridge produced a real quantum-formalism upgrade. In non-ideal
settings, raw logical-environment mutual information can conflate useful
syndrome information with true logical leakage. The next OP-15 target should
therefore track conditional reference-environment leakage after syndrome
extraction:

$$
I(R_L;E_{\mathrm{env}}\mid S)\approx 0.
$$

This is now cross-linked in `bridges/quantum_noise_as_signal.md` and
`OPEN_PROBLEMS.md`.

## Simulation

The new simulator uses a binary Gaussian record channel:

$$
Y_E = g(1-\lambda)E+N_E,
$$

and

$$
Y_L = g\lambda L+N_L,
$$

where \(g\) is monitoring strength and \(\lambda\) is leakage fraction.

Outputs:

- `simulations/restraint_ethics/outputs/restraint_ethics_scan.csv`;
- `simulations/restraint_ethics/outputs/restraint_ethics_summary.csv`;
- `simulations/restraint_ethics/outputs/restraint_ethics_context_audit.csv`;
- `simulations/restraint_ethics/outputs/restraint_ethics_heatmap.png`;
- `simulations/restraint_ethics/outputs/restraint_ethics_curves.png`.

First run:

- grid points: `12221`;
- maximum restraint score: `0.747752`;
- location: monitor strength `2.033333`, leakage fraction `0.000000`;
- at maximum: \(I(E;R)=0.919466\) bits,
  \(I(L;R\mid E)=0.000000\) bits;
- regime counts: `2732` restraint interval, `1799` abandonment/no-record,
  `6247` leakage capture, `166` burden capture, `1277` transition.

The context-correlation audit showed why the conditional metric matters: with
an error-only record and rising correlation between \(E\) and \(L\), raw
\(I(L;R)\) rose to `0.698` bits while \(I(L;R\mid E)\) stayed approximately
zero.

## Interpretation

The toy result has the expected ACP shape. The productive ethical regime is not
no monitoring and not total visibility. It is syndrome-selective governance:
records strong enough to correct public error, narrow enough not to capture the
protected agency state, and restrained enough not to become their own burden.

This is exploratory, but it is no longer only rhetorical. It produces a
measurable diagnostic and a concrete feedback target for the quantum program.

## Next

1. Replace the binary toy with an agent-based institutional model where
   interventions affect \(L_{t+\Delta t}\).
2. Define domain-native record channels for AI governance, markets, education,
   courts, and public health.
3. Add conditional-leakage diagnostics to the next OP-15 microscopic
   Stinespring/syndrome model.
4. Consider a public essay version that teaches the idea through recognition:
   parents, teachers, courts, markets, scientific method, and AI governance.
