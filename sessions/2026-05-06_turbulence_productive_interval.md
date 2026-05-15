# 2026-05-06 — Turbulence Productive-Interval Admissibility Test

## Prompt

Andrew proposed turbulence as a stress test for the new
reality-reflective-mathematics criterion:

> Turbulence — arguably the most famous unsolved physics problem. It is
> literally the phenomenon of systems living between laminar rigidity and
> chaotic dissolution.

## Context Found

The workspace already contained a lightweight Navier-Stokes special-case entry
in `special_cases/acp_special_cases_v03.md` section 5.3.

That entry mapped:

- laminar flow to crystallization;
- fully developed isotropic turbulence to dissolution;
- transitional/structured turbulence to the productive interval.

The same catalog already flagged a limitation: real turbulent flows retain
coherent structures, so treating fully developed turbulence as dissolution is
an idealization.

## Work Done

Added `bridges/turbulence_productive_interval.md`.

The bridge upgrades the old mapping using
`bridges/reality_reflective_mathematics.md`.

Also added a refinement note to `special_cases/acp_special_cases_v03.md` §5.3
so the catalog itself no longer leaves the older global dissolution reading
unqualified.

Main correction:

> Fully developed turbulence is not automatically dissolution. It is
> dissolution only relative to a coarse-graining that cannot decode coherent
> structures or scale-local energy flux. Relative to inertial-range records,
> turbulence remains in the productive interval.

## Formal Shape

Defined scale-resolved macrostates:

$$
m_\ell(t)
=
(\bar u_\ell,E_\ell(k),\Pi_\ell,\omega_\ell,\mathcal C_\ell),
$$

with:

- resolved velocity;
- energy spectrum;
- inter-scale energy flux;
- resolved vorticity;
- coherent-structure inventory.

Defined the scale conditional entropy:

$$
H_\ell=H(m_\ell(t+\Delta t)\mid m_\ell(t)).
$$

The bridge classifies turbulence by scale:

- crystallization: laminarized or overcontrolled scale, \(\Pi_\ell\approx 0\),
  \(H_\ell\to 0\);
- productive interval: inertial-range structured turbulence,
  \(0<H_\ell<H_{\max}\), \(I(\Pi_\ell;R_\ell)>0\);
- dissolution: decorrelated, equipartitioned, or unresolved scale,
  \(H_\ell\to H_{\max}\), predictive information collapses.

## Key Insight

Turbulence is not just "between laminar and chaotic." It shows why ACP must be
record-relative and scale-relative.

The unsolved practical/mathematical problem is closure. A useful turbulence
closure should expose the cascade's syndrome:

$$
I(\Pi_\ell;R_\ell)>0,
$$

while preserving unresolved residual uncertainty:

$$
H(u_{<\ell}\mid R_\ell,\Pi_\ell)>0.
$$

This is the fluid analogue of "learn syndrome, not logical state."

## Tracker Updates

Updated `STATUS.md` and added OP-27 to `OPEN_PROBLEMS.md`.

OP-27 tracks a future DNS or shell-model diagnostic for:

- \(H_\ell\);
- \(I(\Pi_\ell;R_\ell)\);
- future predictive information;
- coherent-structure interaction excess \(J_\ell\);
- closure failure modes by underclosure/dissolution and
  overclosure/crystallization.
