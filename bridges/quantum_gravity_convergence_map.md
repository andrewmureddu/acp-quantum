# Quantum-Gravity Convergence Map: Where ACP Can Attach

*Status: supporting literature map for the ACP quantum-gravity derivation
program; source snapshot from web search on 2026-04-27; conjectural as a
complete derivation of quantum gravity.*

Companion notes:

- `bridges/quantum_gravity_derivation_program.md`
- `bridges/dark_constraint_quantum_gravity.md`
- `bridges/singularity_inadmissibility.md`
- `bridges/cosmic_coordination_floor.md`

## 1. Purpose

The useful question is not only "which quantum-gravity program is right?" The
useful question is:

> where are active quantum-gravity programs already converging on an ACP-shaped
> constraint, and what are they not yet asking sharply enough?

The current convergence is strong. Holography is using quantum error correction
to explain bulk reconstruction. Black-hole information work is using fine-grained
entropy, islands, and decodability. Relational-observable work is using quantum
reference frames, crossed products, and modified local algebras. Regular
black-hole programs are trying to replace singular endpoints with finite
effective structure.

ACP does not need to compete with those mechanisms. The derivation program uses
them as evidence for the structure that ACP should force:

> A candidate quantum-gravity mechanism is admissible only if it preserves a
> nondegenerate relational macrostate channel, prevents singular
> crystallization, and returns decodable boundary coordination without leaking
> detailed interior logical information too early.

This is the gravitational analog of the active QEC target and one rung in the
derivation ladder:

$$
I(\mathrm{error};\mathrm{syndrome})>0
$$

while

$$
I(\mathrm{logical\ state};\mathrm{environment})\approx 0.
$$

For gravity, replace "error" with geometry sector, "syndrome" with boundary
record, and "logical state" with interior microstate:

$$
I(\mathrm{geometry\ sector};R_{\partial})>0
$$

while

$$
I(\mathrm{interior\ microstate};R_{\partial}^{\mathrm{early}})\approx 0
$$

until the appropriate decoding timescale.

## 2. The Convergence

### 2.1 Holography Has Already Become Quantum Error Correction

The AdS/CFT literature now treats bulk locality and subregion reconstruction as
QEC-like. Almheiri, Dong, and Harlow connect bulk locality to operator-algebra
quantum error correction and subregion duality. Pastawski, Yoshida, Harlow, and
Preskill make the same intuition explicit in tensor-network toy codes, where
bulk degrees of freedom behave like logical data encoded into boundary degrees
of freedom.

This is extremely close to ACP. The bulk persists because boundary access is
redundant but constrained. Local bulk information is not simply exposed to the
environment; it is recoverable from appropriate boundary regions.

**What is not quite right yet.** The code is usually treated as a structural
encoding, not as a noise-tailored or record-tailored persistence mechanism. The
question is often "which boundary region reconstructs the bulk operator?" ACP
asks the adjacent channel question:

$$
I(\mathrm{bulk\ sector};R_{\partial})>0
\quad\text{and}\quad
I(\mathrm{bulk\ logical};E_{\mathrm{uncontrolled}})\approx 0.
$$

This converts holographic reconstruction from a static code picture into a
boundary-syndrome alignment problem.

### 2.2 Islands and Page Curves Already Encode Decodable Redistribution

The island program computes fine-grained Hawking-radiation entropy with quantum
extremal surfaces and replica-wormhole machinery. The Page curve becomes a
decodability statement: information that seemed trapped in the interior becomes
recoverable from radiation after the appropriate transition.

This is already Criterion 3 in `bridges/cosmic_coordination_floor.md` in a more
mature language:

$$
I(X_R;Y_{\mathscr I^+}^{[t,t+T]})
$$

must eventually rise enough to pay down the coordination debt of collapse.

**What is not quite right yet.** Islands give a powerful entropy accounting, but
they do not by themselves state a general admissibility rule for non-AdS,
non-ideal, finite-resolution gravitational systems. ACP can package the Page
curve as one instance of a broader boundary-channel rule:

1. singular collapse is inadmissible;
2. hidden repair without eventual decoding is inadmissible;
3. viable repair must transfer recoverable coordination to the exterior record.

### 2.3 Relational Observables Are Becoming the Algebraic Core

Recent work on quantum reference frames and measurement schemes builds physical
observables from joint system-plus-reference-frame structures. In the relevant
cases, invariant observable algebras can be described by crossed products and
can undergo type reduction from type III behavior toward semifinite or type II
algebras. Recent relational quantum geometry work similarly unifies extended
phase spaces, crossed products, and quantum reference frames by adjoining
degrees of freedom and imposing constraints.

This is an especially strong ACP attachment point. ACP already uses
boundary/interior partitions and Schur complements; relational quantum geometry
gives a domain-native way to define what the partitions are allowed to mean in a
diffeomorphism-invariant theory.

**What is not quite right yet.** The algebraic literature is excellent on
observables and type structure, but it often leaves the persistence diagnostics
implicit. ACP's addition is a channel layer on top of the algebra:

$$
\mathcal A_{\mathrm{rel}}
\longrightarrow
P_{\ell,\Delta}(m'|m)
\longrightarrow
H_{\ell,\Delta}(m)
\quad\text{and}\quad
I(X_R;Y_{\partial}).
$$

That is: once the relational observable algebra is defined, ask whether its
coarse macrostates have a nondegenerate future channel and a decodable boundary
record.

### 2.4 Singularity Resolution Is Everywhere, But Finite Curvature Is Too Weak

Loop-inspired effective black holes, Wheeler-DeWitt black-hole interiors,
unimodular quantization, and asymptotic-safety black holes are all trying to
replace classical singularities with finite quantum-corrected structures. Some
recent examples produce nonsingular black-hole/white-hole transitions,
non-singular wormhole-like effective spacetimes, or wave functions satisfying
DeWitt-type singularity-avoidance conditions.

ACP agrees with the direction: singularities are not physical states; they are
failures of the admissible description.

**What is not quite right yet.** Many regular-black-hole proposals can satisfy
the local regularity test while leaving the exterior information channel
unclear. Finite curvature is necessary, not sufficient. ACP's stronger test is:

$$
\text{regular geometry}
\quad+\quad
H_{\ell,\Delta}(m)>H_{\mathrm{floor}}
\quad+\quad
I(X_R;Y_{\mathscr I^+})\ \text{eventually positive}.
$$

A bounce, remnant, baby universe, or wormhole continuation fails the ACP test if
it preserves regularity by hiding unbounded coordination in a permanently
undecodable sector.

### 2.5 Phenomenology Is Looking for Shadows, Quasinormal Modes, and Constraints

Asymptotic-safety and regular-black-hole work is increasingly tied to
observational handles: shadows, quasinormal modes, grey-body factors, particle
dynamics, and formation probabilities. This is exactly where
`bridges/dark_constraint_quantum_gravity.md` can mature. A dark region, a
missing echo, a shifted ringdown spectrum, or a shadow deformation is not merely
"absence"; it is a structured null record.

**What is not quite right yet.** The observational side often asks whether a
metric correction produces a signal. ACP asks the inverse-problem version:

$$
I(G;R_+,R_0)>0,
$$

where \(R_+\) are positive detections and \(R_0\) are structured null records.
This keeps the work tied to measurable boundary channels rather than to
unobservable interior narratives.

## 3. The ACP Added Insight

The field has many mechanisms. ACP supplies a derivation target that first
appears as a cross-mechanism admissibility filter:

**A. Relational nondegeneracy.** The physical observable algebra must define a
finite-resolution relational macrostate space \(\mathcal M_\ell\). Its
boundary/interior partition cannot require an inverse of a singular internal
block.

**B. Future-entropy floor.** For nontrivial collapsing macrostates,

$$
H_{\ell,\Delta}(m)
=
-
\sum_{m'}P_{\ell,\Delta}(m'|m)\log P_{\ell,\Delta}(m'|m)
\geq
H_{\mathrm{floor}}(m)>0.
$$

**C. Mechanism-changing trigger.** If classical focusing drives
\(H_{\ell,\Delta}(m)\) toward the floor, the effective dynamics must leave the
self-reinforcing collapse basin before the floor is breached.

**D. Boundary decodability.** The exterior must eventually receive a decodable
record of the redistributed coordination:

$$
I(X_R;Y_{\partial}^{[t,t+T_{\mathrm{dec}}]})
\geq
\eta\,\Delta C_R-\varepsilon .
$$

**E. Logical privacy before decoding.** The exterior record may constrain
charges, area, geometry sector, and coarse interior labels, but it must not
prematurely leak arbitrary detailed interior logical information:

$$
I(\mathrm{interior\ microstate};R_{\partial}^{\mathrm{early}})
\approx 0.
$$

This makes quantum gravity look like a noise-tailored persistence problem:
structured boundary records carry syndrome-like information about geometry
while protected interior degrees remain logical until the correct decoding
window.

## 4. What People Are Missing

The recurring blind spots are now clear:

1. **Regularity without recoverability.** Many proposals resolve curvature but
   do not prove that exterior observers get a decodable channel.
2. **Entropy without mechanism selection.** Islands and generalized entropy
   compute the right accounting in special settings, but the general
   selection rule is not isolated.
3. **Algebra without dynamics.** Relational algebras define observables, but
   not yet a persistence criterion for coarse gravitational histories.
4. **Signals without null records.** Phenomenology tracks positive deviations
   more naturally than structured absences, even though null records can be
   highly informative.
5. **Static codes instead of adaptive boundary alignment.** Holographic QEC is
   usually framed as a fixed encoding. ACP suggests asking how the encoding,
   wedge, or reconstruction map adapts to changing boundary access, noise, and
   collapse phase.

None of these are fatal flaws. They are openings.

## 5. Best Near-Term Build

The strongest next bridge is:

> ACP relational macrostate kernels built on quantum-reference-frame /
> crossed-product observable algebras.

Reason: this line is mathematically native to quantum gravity and already
speaks the ACP language of partitions, observable access, finite entropy, and
boundary/interior structure. It gives us a serious foundation for replacing the
toy finite collapse model with a relational macrostate kernel.

The first formal document now exists as
`bridges/relational_observable_macrostate_kernel.md`. It defines:

1. a finite relational observable algebra \(\mathcal A_{\partial,\ell}\) for an
   exterior observer or boundary region;
2. a hidden/interior companion algebra \(\mathcal A_{R,\ell}\);
3. coarse relational macrocells \(m\in\mathcal M_\ell\);
4. a candidate transition kernel \(P_{\ell,\Delta}(m'|m)\);
5. diagnostics \(H_{\ell,\Delta}(m)\), \(I(G;R_+,R_0)\), and
   \(I(X_R;Y_{\partial})\).

The next simulation upgrade should be an inverse problem rather than a full
quantum-gravity simulation:

> replace the hidden optical phase bump in
> `simulations/dark_constraint_wave_interference/` with a weak metric/lensing
> perturbation and score how much bright plus dark boundary records reduce
> posterior uncertainty over the metric sector.

That keeps the project honest: measurable records first, grand interpretation
second.

## 6. Working Conjecture

**Conjecture (ACP quantum-gravity convergence).** The viable quantum-gravity
mechanisms now visible in holography, relational-observable algebra, and
regular-black-hole dynamics are special cases of the derivation target stated
in `bridges/quantum_gravity_derivation_program.md`:

> gravitational systems remain physically admissible only when their relational
> boundary channels carry enough structured syndrome information to constrain
> geometry, while preserving nonzero future entropy and preventing uncontrolled
> leakage of protected interior logical information.

Equivalently, quantum gravity is not just "quantize the metric." It is the
persistence-forced completion of gravitational dynamics into a noise-tailored,
boundary-decodable quantum channel whose classical limit is spacetime.

## 7. Source Snapshot

- Almheiri, Dong, and Harlow, "Bulk locality and quantum error correction in
  AdS/CFT," JHEP 2015:
  <https://link.springer.com/article/10.1007/JHEP04%282015%29163>
- Pastawski, Yoshida, Harlow, and Preskill, "Holographic quantum
  error-correcting codes," JHEP 2015:
  <https://link.springer.com/article/10.1007/JHEP06%282015%29149>
- Almheiri, Hartman, Maldacena, Shaghoulian, and Tajdini, "The entropy of
  Hawking radiation," Rev. Mod. Phys. 2021:
  <https://www.osti.gov/pages/biblio/1839660>
- Almheiri, Engelhardt, Marolf, and Maxfield, "The entropy of bulk quantum
  fields and the entanglement wedge of an evaporating black hole," JHEP 2019:
  <https://link.springer.com/article/10.1007/JHEP12%282019%29063>
- Fewster, Janssen, Loveridge, Rejzner, and Waldron, "Quantum Reference Frames,
  Measurement Schemes and the Type of Local Algebras in Quantum Field Theory,"
  Commun. Math. Phys. 2025:
  <https://link.springer.com/article/10.1007/s00220-024-05180-7>
- Ahmad, Chemissany, Klinger, and Leigh, "Relational quantum geometry,"
  Nuclear Physics B 2025:
  <https://www.sciencedirect.com/science/article/pii/S0550321325001208>
- Giddings, "Quantum gravity observables: observation, algebras, and
  mathematical structure," J. Phys. A 2025:
  <https://doi.org/10.1088/1751-8121/ae0b12>
- Gielen and Ried, "Quantum Schwarzschild-(A)dS black holes: unitarity and
  singularity resolution," JHEP 2025:
  <https://link.springer.com/article/10.1007/JHEP06%282025%29074>
- Belfaqih, Bojowald, Brahma, and Duque, "Black holes in effective loop quantum
  gravity: Covariant holonomy modifications," Phys. Rev. D 2025:
  <https://journals.aps.org/prd/accepted/10.1103/1tyh-87sr>
- Singh and Nandy, "Universality in the quantum nature of spacetime in
  Wheeler-DeWitt black holes," Nuclear Physics B 2025:
  <https://www.sciencedirect.com/science/article/pii/S0550321325000574>
- Platania, "Some thoughts about black holes in asymptotic safety," Gen. Rel.
  Grav. 2025:
  <https://link.springer.com/article/10.1007/s10714-025-03390-5>
