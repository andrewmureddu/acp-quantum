# Cosmic Coordination Floor: A Formalization Program for ACP Quantum Gravity

*Status: active component of the ACP quantum-gravity derivation program; formal
at the ACP selection-rule level; conjectural as a complete derivation of
quantum gravity.*

## 1. Program Thesis

If singularities are inadmissible, quantum gravity is not merely a theory that
resolves them after they appear. It is the persistence-forced completion of
classical spacetime: a theory whose admissible state space, transition law, and
boundary channel enforce a cosmic coordination floor before the singular
endpoint is reached.

The ACP design specification is:

> no physically admissible gravitational process may drive the conditional
> future entropy of a nontrivial collapsing region to zero or make its exterior
> boundary channel depend on undefined interior data.

The target is not a preferred microscopic mechanism. The target is a derivation
constraint that any candidate mechanism must satisfy, and that may be strong
enough to force the shared holographic/QEC-like structure of quantum gravity.

## 2. Relational Macrostates

A gravitational macrostate cannot be a bare field configuration at coordinate
points. It must respect diffeomorphism invariance.

The full OP-20 kernel skeleton is now separated into
`bridges/relational_observable_macrostate_kernel.md`. This section keeps the
semiclassical starting point used by the coordination-floor program.

A useful semiclassical starting point is a coarse relational initial-data cell:

$$
m
=
\left[
\Sigma,\,
q_{ab},\,
K_{ab},\,
\phi,\,
\pi_\phi
\right]_{\mathrm{Diff}(\Sigma),\,\ell},
$$

where:

- \(q_{ab}\) is the spatial 3-metric;
- \(K_{ab}\) is the extrinsic curvature, or equivalently the gravitational
  momentum \(\pi^{ab}\);
- \(\phi,\pi_\phi\) are matter fields and momenta;
- the data satisfy the Hamiltonian and momentum constraints;
- the quotient removes diffeomorphism-equivalent descriptions;
- \(\ell\) is a coarse-graining scale, eventually no smaller than the scale at
  which the candidate quantum-gravity theory supplies finite observables.

The inclusion of \(K_{ab}\) matters. A 3-geometry alone is not enough initial
data for gravitational evolution.

Let \(\mathcal M_{\ell}\) be the resulting finite-resolution macrostate space.
For calculations, one should use a finite partition of relational observables
rather than raw continuum differential entropy, since differential entropy is
coordinate-dependent.

## 3. Transition Kernel and Future Entropy

A candidate quantum-gravity theory should induce a coarse transition kernel

$$
P_{\ell,\Delta}(m'|m)
$$

for macrostates separated by a verification time \(\Delta\).

In a decoherent-histories formulation, this can be written schematically as

$$
P_{\ell,\Delta}(m'|m)
=
\frac{
\mathrm{Tr}\!\left(C_{m'}\,\rho_m\,C_{m'}^\dagger\right)
}{
\sum_{\tilde m\in\mathcal M_\ell}
\mathrm{Tr}\!\left(C_{\tilde m}\,\rho_m\,C_{\tilde m}^\dagger\right)
},
$$

where \(C_{m'}\) is the class operator for histories that begin in the
macrocell \(m\) and end in macrocell \(m'\). In path-integral language,
\(C_{m'}\) is obtained by summing over histories whose boundary data lie in the
specified relational cells.

The conditional future entropy is then

$$
H_{\ell,\Delta}(m)
=
-
\sum_{m'\in\mathcal M_\ell}
P_{\ell,\Delta}(m'|m)
\log P_{\ell,\Delta}(m'|m).
$$

For continuum limits, replace this with a relative entropy or a projective
limit of finite partitions. The operational object is always a finite
coarse-grained uncertainty over future relational macrostates.

## 4. Criterion 1: Coordination Floor

**Criterion 1 (Cosmic coordination floor).** For every physically admissible
nontrivial collapsing macrostate \(m\), a viable quantum-gravity theory must
satisfy

$$
H_{\ell,\Delta}(m)
\geq
H_{\mathrm{floor}}(m;\ell,\partial R)
>
0
$$

over the verification window in which the collapse channel remains physically
active.

The floor need not be a universal constant. It may depend on boundary area,
energy, angular momentum, charge, coarse-graining scale, and the verification
time. What matters is that it is strictly positive for a nontrivial collapsing
region.

Classical GR fails this criterion in the following precise sense: under the
standard focusing assumptions, the classical continuation of the collapse
channel concentrates on a geodesically incomplete endpoint. The admissible
future channel either collapses to a delta-like classical continuation or
becomes undefined. Both are ACP failures:

$$
P_{\ell,\Delta}(m'|m)\to\delta(m'-m_{\mathrm{sing}})
$$

with \(m_{\mathrm{sing}}\notin\mathcal M_{\ell}^{\mathrm{adm}}\), or else the
kernel cannot be normalized over admissible future macrostates.

## 5. Criterion 2: Collapse as Self-Reinforcement

The classical collapse mechanism is self-reinforcing. The local expression is
the Raychaudhuri equation. For a hypersurface-orthogonal timelike congruence,

$$
\frac{d\theta}{d\tau}
=
-
\frac{1}{3}\theta^2
-
\sigma_{ab}\sigma^{ab}
-
R_{ab}u^a u^b ,
$$

where \(\theta\) is expansion and \(\sigma_{ab}\) is shear. Under the usual
positive-energy focusing condition, negative expansion feeds on itself:

$$
\theta<0
\quad\Rightarrow\quad
\frac{d\theta}{d\tau}<0
$$

up to rotation and energy-condition qualifications.

Define a collapse reinforcement basin

$$
\mathcal B_{\mathrm{coll}}(\alpha)
=
\{m\in\mathcal M_\ell:
\mathbb E_m[\theta_R]<-\alpha,\,
\mathbb E_m[R_{ab}u^a u^b]\geq 0
\}.
$$

Inside this basin, the classical flow narrows the set of admissible future
macrostates. In ACP language, collapse is a gravitational self-reinforcing
mechanism. If no mechanism-changing transformation intervenes, crystallization
drift drives the channel toward singular inadmissibility.

**Criterion 2 (Redistribution trigger).** A viable quantum-gravity theory must
contain a mechanism-changing transformation before

$$
H_{\ell,\Delta}(m)-H_{\mathrm{floor}}(m;\ell,\partial R)
\leq
\epsilon .
$$

Equivalently, near Planckian curvature or entropy-density concentration, the
effective dynamics must leave the classical reinforcement basin:

$$
\mathcal T_{\mathrm{QG}}:
\mathcal B_{\mathrm{coll}}
\longrightarrow
\mathcal M_{\mathrm{redist}},
$$

with

$$
\Delta H_{\ell,\Delta}>0
$$

or at least with \(H_{\ell,\Delta}\) prevented from decreasing further.

## 6. Criterion 3: Visible Redistribution

The Restraint-Power Theorem says that when a system approaches its coordination
floor, the subsystem with highest coordination concentration must undergo a
decodable mechanism-changing transformation before the global floor is
breached.

In gravitational collapse, the concentrated subsystem is the collapsing core or
near-core geometry. A hidden repair is not enough. If the repair creates a
permanently disconnected baby universe, an arbitrarily information-dense
remnant, or an eternal non-decoding horizon for an otherwise finite collapse
process, then the exterior channel has not received a decodable transfer.

Let \(X_R\) denote the recoverable interior macro-information of the collapsing
region, and let

$$
Y_{\mathscr I^+}^{[t,t+T]}
$$

be the radiation and boundary record available to asymptotic observers over the
outgoing interval \([t,t+T]\).

**Criterion 3 (Decodable redistribution).** There must exist a finite transfer
time \(T_{\mathrm{dec}}\) such that

$$
I\!\left(
X_R;
Y_{\mathscr I^+}^{[t,t+T_{\mathrm{dec}}]}
\right)
\geq
\eta\,\Delta C_R
-
\varepsilon ,
$$

where \(\Delta C_R\) is the coordination capacity removed from the collapsing
core and \(0<\eta\leq 1\) is a theory-dependent recoverability efficiency.

For a unitary asymptotically complete collapse-and-evaporation process, this
criterion should appear as a Page-curve condition:

$$
S_{\mathrm{rad}}(u)
\ \text{eventually decreases after the Page time}
$$

and returns to the entropy allowed by the final admissible exterior state, not
to an unbounded hidden remnant entropy.

This is the sharp version of the visibility requirement: quantum gravity may
hide interior details temporarily, but it may not make the coordination debt
permanently undecodable.

## 7. Path-Integral Form

Start from a formal quantum-gravity amplitude

$$
Z[R]
=
\int
\mathcal Dg\,\mathcal D\phi\,
\exp(iS[g,\phi]/\hbar).
$$

The ACP admissible version inserts two pieces of structure:

1. an admissible history class excluding singular endpoints as ordinary
   histories;
2. a floor-enforcing weight or constraint suppressing histories whose
   coarse-grained future entropy violates the coordination floor.

Schematically,

$$
Z_{\mathrm{ACP}}[R]
=
\int
\mathcal Dg\,\mathcal D\phi\,
\chi_{\mathrm{adm}}[g,\phi]\,
\Omega_{\mathrm{floor}}[g,\phi]\,
\exp(iS_{\mathrm{eff}}[g,\phi]/\hbar).
$$

Here \(\chi_{\mathrm{adm}}=0\) for histories that leave the admissible state
space. A simple Euclidean or influence-functional analog of the floor penalty
would be

$$
\Omega_{\mathrm{floor}}
=
\exp\!\left[
-
\Lambda
\int dt\,
\max\{0,H_{\mathrm{floor}}(m_t)-H_{\ell,\Delta}(m_t)\}^2
\right].
$$

The Lorentzian version should not be read literally as a probability weight.
It is a placeholder for whatever the microscopic theory uses: contour
selection, constraint algebra, saddle suppression, quantum bounce dynamics,
topology change, nonlocal form factors, or a boundary Hilbert-space rule.

The ACP claim is not that one of these mechanisms is known to be correct. The
claim is that a candidate mechanism must implement the same selection rule.

## 8. Candidate Mechanism Tests

The following are not endorsements. They are audit questions.

| Candidate ingredient | Floor mechanism to test | Decodability risk |
|---|---|---|
| Asymptotic safety / running couplings | Does the UV fixed point bound curvature concentration and keep \(P(m'|m)\) non-delta? | Does the collapse channel return information to \(\mathscr I^+\)? |
| Loop / polymer corrections | Does the modified Hamiltonian constraint create a bounce before \(H_{\ell,\Delta}\) reaches the floor? | Does the bounce couple to exterior radiation rather than remaining hidden? |
| Noncommutative or minimal-length geometry | Does the short-distance cutoff regularize \(D\) and finite observables? | Does cutoff regularity imply recoverability, or only finite curvature? |
| Fuzzball / microstate geometries | Does the ensemble replace the singular endpoint with finite horizon-scale structure? | Are exterior records sufficient to decode the microstate in principle? |
| Holographic unitarity | Does the boundary theory provide a nondegenerate transition kernel for bulk collapse? | Is the bulk singularity absent, emergent, or merely hidden by dual variables? |
| Topology change / spacetime foam | Does tunneling restore future entropy without losing normalization? | Is information transferred to the original exterior or lost to disconnected sectors? |

The ACP selection rule rejects any candidate that only moves the singularity
behind a permanently undecodable boundary.

## 9. Formalization Roadmap

**Stage A: Relational macrostate construction.** Use
`bridges/relational_observable_macrostate_kernel.md` to choose a finite
relational observable algebra for compact regions and define
\(\mathcal M_\ell\) as constraint-satisfying initial-data cells modulo
diffeomorphism and coarse-graining.

**Stage B: Classical failure theorem.** Under the assumptions of the
singularity theorems, show that the induced classical transition kernel either
concentrates on an inadmissible endpoint or fails to define a normalized kernel
over admissible macrostates.

**Stage C: Floor axiom.** State the cosmic coordination floor as an
admissibility axiom for quantum-gravity transition kernels:

$$
H_{\ell,\Delta}(m)\geq H_{\mathrm{floor}}(m)>0
$$

for nontrivial collapse channels.

**Stage D: Trigger theorem.** Prove that if collapse remains self-reinforcing
and the floor is enforced, then a mechanism-changing transformation must occur
before the floor is breached.

**Stage E: Visibility theorem for collapse.** Specialize A.20.18 to
asymptotically observable gravitational collapse and derive a lower bound on
the mutual information between interior macro-information and outgoing records.

**Stage F: Candidate audits.** For each quantum-gravity proposal, compute or
estimate the three diagnostics:

$$
H_{\ell,\Delta}(m),
\qquad
\Delta H_{\mathrm{trigger}},
\qquad
I(X_R;Y_{\mathscr I^+}).
$$

**Stage G: Toy collapse model.** The first finite simulation now exists in
`simulations/cosmic_coordination_floor/`. It compares naked collapse,
singular-history exclusion, and horizon transfer into a finite boundary
register.

## 10. First Macrocell Collapse Toy

The executable toy in `simulations/cosmic_coordination_floor/` now tracks the
finite OP-20 macrocell vector

$$
m
=
(
M_{\partial},
J_{\partial},
Q_{\partial},
C_R,
\bar\theta_R,
\bar K_R,
A_{\partial},
N_0,
Y_{\partial}
),
$$

rather than a single collapse coordinate. It is still not a gravitational
simulation. It is a finite stochastic test of whether the diagnostics separate
the right logical possibilities.

Four policies are compared:

- **naked collapse:** classical focusing leaks probability mass into an
  inadmissible singular endpoint and directly exposes protected interior
  information in the failed branch;
- **hard exclusion:** singular histories are removed and the admissible
  remainder is renormalized, but no coordination is redistributed;
- **horizon transfer:** near the trigger, probability mass is moved away from
  the singular boundary and finite boundary records carry late decodable
  information;
- **quantum completion:** a schematic completion triggers earlier, preserves
  normalization, emits geometry-sector records, bounds early protected-interior
  leakage, and releases late decodable information.

The default run gives:

| Policy | min \(H\) bits | min adm. mass | max sing. mass | max \(I(G;R_\partial)\) bits | max early leakage bits | final late decode bits | first floor violation |
|---|---:|---:|---:|---:|---:|---:|---:|
| naked collapse | 4.627 | 0.001 | 0.079 | 1.298 | 0.238 | 0.000 | 1 |
| hard exclusion | 0.205 | 1.000 | 0.000 | 2.101 | 0.000 | 0.000 | 22 |
| horizon transfer | 4.628 | 1.000 | 0.000 | 1.928 | 0.000 | 3.000 | none |
| quantum completion | 4.628 | 1.000 | 0.000 | 1.496 | 0.004 | 3.000 | none |

The point is not numerical realism. It is the separation of four logical
possibilities:

1. naked collapse fails by losing normalization and protected-interior privacy;
2. hard exclusion avoids the singular bin but still crystallizes the future
   channel and emits no late decodable redistribution;
3. horizon transfer preserves admissibility by converting collapse into a
   finite boundary record;
4. a candidate completion must satisfy the full bundle: normalization,
   future-entropy floor, geometry-record information, early privacy, and late
   decodability.

## 11. Working Conjectures

**Conjecture 1 (Quantum gravity as floor enforcement).** A physically viable
quantum gravity theory is exactly a microscopic completion of semiclassical
gravity whose induced relational macrostate kernel satisfies the cosmic
coordination floor.

**Conjecture 2 (Collapse repair is forced redistribution).** In any collapse
process satisfying the classical focusing assumptions, floor enforcement
requires a mechanism-changing redistribution event before the classical
singularity time.

**Conjecture 3 (No permanent undecodable storage).** A repair that preserves
finite curvature but stores unbounded information in a permanently hidden
sector is ACP-inadmissible for finite collapse, because it fails visibility and
decodability.

**Conjecture 4 (Gravity and quantum uncertainty are one cycle).** Classical
gravity supplies the crystallizing tendency by concentrating geometry and
matter. Quantum gravity supplies the anti-crystallizing completion by enforcing
nonzero conditional future entropy and redistributing coordination through
finite boundary channels.

## 12. What Is Proven and What Is Open

**Proven inside ACP/Schur:** singular \(D\) breaks the effective boundary law;
future-bearing dynamics require a nondegenerate internal block.

**Structurally derived from ACP:** if a collapsing gravitational subsystem is
approaching a coordination floor, a mechanism-changing transfer must occur
before the floor is breached, and the transfer must be decodable to stabilize
the composite system.

**Conjectural in quantum gravity:** the correct microscopic theory implements
this transfer through a bounce, horizon microstructure, holographic unitary
evolution, topology change, or some other finite mechanism.

**Open technical problem:** instantiate the relational macrostate kernel in a
semiclassical collapse model and then in a concrete candidate theory, proving
the floor, trigger, and visibility criteria rather than stating them as
selection rules.
