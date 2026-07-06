# Session log — 2026-07-06 — Cadence control law recognized and verified (OP-30)

## Context

Fourth same-day installment of the quantum-foundations push. Andrew asked:
"is there a cadence control law to be discovered/recognized?" The answer
turned out to be *recognized*: the law was already implicit, quantitatively,
in two of the project's own prior simulation results — the
`risky_qec_claims` monitoring-interval scan (best correction interval moved
from 1 to 4 when backaction 0.012 was turned on) and the H1/H2 finding that
gated decoder adaptation beats overactive updating. The PU-2/CDT derivation
and local-discriminability (G3) targets from the purification session remain
queued.

## What was done

1. **New bridge:** `bridges/cadence_control_law.md`.
   - **Proposition 2.1 (proved):** for per-event record cost \(c>0\) and
     drift accumulation order \(s>0\), \(J(T)=\alpha T^{s}+c/T\) has the
     unique interior optimum \(T^{*}=(c/(s\alpha))^{1/(s+1)}\) with exact
     power-law comparative statics; the cadence exponent \(1/(s+1)\) is set
     by the accumulation order alone.
   - **Remark 2.2 (existence condition):** a cadence control law exists
     exactly when the record channel is *restorative* (resets accumulation,
     \(s>0\)) and *costly* (\(c>0\)); the failure cases are the Zeno /
     continuous-monitoring boundary and the never-monitor boundary — the
     productive interval projected onto the tempo axis.
   - **Instance A, correction cadence:** exact per-tick cost for the 3-qubit
     repetition memory with XOR composition of per-cycle miscorrection;
     square-root law \(T^{*}\approx\sqrt{\gamma_b/3}/p\); general
     \(t\)-error-correcting form \(T^{*}=(1/p)(\gamma_b/(tC))^{1/(t+1)}\);
     fill-fraction invariant \(pT^{*}\).
   - **Instance B, adaptation cadence:** moving-average tracking of drifting
     noise; cube-root law \(W^{*}\approx(2\sigma^{2}/a^{2})^{1/3}\); the
     quantitative form of the gated-vs-overactive adaptation finding.
   - **Invariants and conjecture:** optimal record-cost share is
     \(s/(s+1)\) (½ for single-error correction, ⅔ for tracking) —
     a clock-free signature; Conjecture C-1 states tempo covariance of the
     fill fraction and cost shares (the new concrete OP-29 target).
   - Careful boundaries: the crystallization identification is structural,
     not literal (the risk audit's warning against "measurement is
     crystallization" is kept in force); prior art (Zeno/anti-Zeno, QEC
     cycle-time optimization, bias-variance window selection) is
     acknowledged — the claimed contribution is unification, exponent
     classification, ACP tempo reading, and retrodiction.

2. **New simulation:** `simulations/cadence_control_law/` — exact objectives,
   integer argmins, log-log exponent fits; pure stdlib, deterministic.
   - Fitted exponents: backaction `0.5515` (predicted \(1/2\)); drift
     `-0.9942` (predicted \(-1\)); adaptation `-0.6571` (predicted
     \(-2/3\)).
   - **Retrodiction:** at \(p=0.02\), \(b=0.012\) the exact objective's
     integer optimum is `4`, exactly the prior scan's empirical best
     interval; at \(b=0\) it is `1`, also matching. One modeling bug was
     caught en route: naively dividing per-cycle failure by \(T\) lets the
     "rate" vanish as \(T\to\infty\); the correct per-tick rate uses XOR
     composition, \(-\ln(1-2P_{\mathrm{cyc}})/(2T)\).

3. **Trackers:** added OP-30 to `OPEN_PROBLEMS.md` (placed after OP-29);
   updated the OP-29 headline; STATUS gained an active-cadence-bridge line,
   front 15, OP-30 headline, and a changelog entry.

## Honesty boundary

- Proved: Proposition 2.1 and both instances at toy level (Markovian,
  uncorrelated drift, fixed controller class); exponents verified exactly;
  prior scan retrodicted exactly.
- Recognized, not invented: all component mathematics is standard; the
  contribution is the unified two-boundary tempo law, the \(1/(s+1)\)
  classification, the invariant forms, and the in-repo retrodiction.
- Conjectural: C-1 tempo covariance; hardware estimation of \(\alpha,c,s\)
  from H1/H2 traces not yet done; robustness under correlated drift open.

## Next steps

1. PU-2 from CDT and local discriminability (G3) — still the queued OP-21
   targets from the purification session.
2. OP-30 items: prove C-1; estimate the cadence constants from H1/H2 replay
   traces and compare with the gated policy's empirical update times.
