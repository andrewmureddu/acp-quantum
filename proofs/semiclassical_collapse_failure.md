# Semiclassical Collapse Failure Theorem

*Status: formal at the finite relational-kernel level given explicitly imported
classical-GR inputs (Raychaudhuri comparison, Penrose incompleteness,
trapped-surface existence and stability); ACP-native in its admissibility and
kernel arguments; conjectural only in the final identification of the forced
completion with quantum gravity.*

Companion notes:

- `bridges/relational_observable_macrostate_kernel.md` (the kernel this theorem
  strengthens; its Proposition 2 is the modest predecessor)
- `bridges/quantum_gravity_derivation_program.md` (Stage 2 of the ladder)
- `bridges/cosmic_coordination_floor.md` (floor axiom and trigger criterion)
- `bridges/singularity_inadmissibility.md` (admissibility conditions and the
  Schur reading)
- `simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py`
  (numerical companion)

## 1. Purpose

Proposition 2 of `bridges/relational_observable_macrostate_kernel.md` proved a
trichotomy for the classical pushforward kernel **conditional on the
hypothesis** that a positive-measure subset of a collapse macrocell reaches an
inadmissible singular set within the verification interval. That hypothesis
did the real work, and it was assumed, not derived.

This document removes the assumption. Under explicit focusing assumptions
stated below, the failing subset is derived rather than posited, the
normalization failure is quantitative, the trichotomy is upgraded to a no-go
theorem over every kernel constructible from the classical description, and
two corollaries make precise (i) why horizon formation defers but does not
escape the failure, and (ii) what any admissible continuation is thereby
forced to contain.

The result is the Stage 2 theorem of the derivation ladder in
`bridges/quantum_gravity_derivation_program.md`:

> For a finite-resolution relational collapse macrostate satisfying the
> classical focusing assumptions, the classical transition kernel either
> becomes undefined on admissible future macrostates or violates the positive
> future-entropy floor.

## 2. Honesty Boundary

**Imported from classical GR, not derived from ACP.** The null Raychaudhuri
equation; the Penrose singularity theorem (global hyperbolicity + noncompact
Cauchy surface + null convergence condition + closed trapped surface implies
future null geodesic incompleteness); existence of trapped surfaces from
sufficient concentration of matter (Schoen–Yau-type results; exact in
spherical symmetry); Cauchy stability of strict trappedness. These are used as
explicitly labeled hypotheses. ⚠ If any imported input fails in a candidate
setting (e.g. NEC-violating matter), the theorem's conclusion is not claimed
there.

**Formal in this document, given the imports.** The focusing bound
(Lemma 1); full-measure admissibility exit for trapped macrocells (Lemmas 3–4);
the quantitative normalization failure, record-balance failure, and floor
failure (Theorem 1); the exhaustive no-go over classical kernel constructions
(Theorem 2); the horizon-deferral corollary at the level of kernel structure
(Corollary 1, with its evaporation input marked ⚠ semiclassical); the
forced-completion corollary (Corollary 2).

**Still conjectural.** That the forced completion is quantum gravity — with
the correct microscopic Hilbert/algebraic structure, boundary records, and
classical limit. Nothing below closes that gap; the theorem sharpens exactly
what the gap is.

## 3. Setup

Fix a compact gravitational region \(R\) with exterior access \(\partial R\),
a finite relational reference structure \(\mathcal F_\ell\), the relational
observable algebra \(\mathcal A_{\mathrm{rel},\ell}(R)\), the finite macrocell
space \(\mathcal M_\ell\), and the classical description

$$
\mathcal D_{\mathrm{cl}}
=
(\mathcal S_{\mathrm{cl}},\ \Phi_t,\ \sigma_\ell,\ \mu),
$$

all as defined in `bridges/relational_observable_macrostate_kernel.md` §§3–6:
\(\mathcal S_{\mathrm{cl}}\) is the constraint-satisfying initial-data space
with admissible subset \(\mathcal S_{\mathrm{adm}}\), \(\Phi_t\) is the
classical Einstein flow on the maximal globally hyperbolic development (MGHD)
of each datum, \(\sigma_\ell:\mathcal S_{\mathrm{adm}}\to\mathcal M_\ell\) is
the coarse map, and for each cell \(C_m=\sigma_\ell^{-1}(m)\), \(\mu_m\) is a
probability measure on \(C_m\).

Admissibility is the four-condition package of
`bridges/singularity_inadmissibility.md` §2: finite observables, normalizable
boundary channel, nondegenerate interior block, finite continuation over the
verification interval.

**Definition 1 (failure time).** For \(s\in C_m\), let \(\tau_{\mathrm{fail}}(s)
\in(0,\infty]\) be the infimum of relational verification times (measured by
\(\mathcal F_\ell\)) at which the development of \(s\) ceases to define an
admissible state of \(\mathcal D_{\mathrm{cl}}\). If the development is
admissible for all times, \(\tau_{\mathrm{fail}}(s)=\infty\).

**Definition 2 (classical kernel construction).** A kernel construction for
\(\mathcal D_{\mathrm{cl}}\) is any stochastic kernel on
\(\mathcal M_\ell^{\mathrm{adm}}\) built from the data
\((\mathcal S_{\mathrm{cl}},\Phi_t,\sigma_\ell,\mu)\) alone — without
adjoining new dynamical variables, new record channels, or new stochastic
transition rules not generated by \(\Phi_t\). The classical data admit exactly
three canonical constructions on a cell whose mass partially or totally exits
admissibility:

1. **naked (unconditioned) pushforward:** keep
   \(K^{\mathrm{cl}}_{\ell,\Delta}(m'|m)\) as defined, with retained mass
   \(Z^{\mathrm{adm}}_{\ell,\Delta}(m)\leq 1\);
2. **hard exclusion:** delete the failing mass and renormalize,
   \(\tilde P=K/Z\);
3. **terminal absorption:** redirect each failing datum \(s\), at
   \(\tau_{\mathrm{fail}}(s)\), into the admissible macrocell containing its
   last admissible snapshot, and freeze it there (an absorbing cell family).

Lemma 5 below shows this list is exhaustive for Definition 2.

## 4. Focusing Assumptions

Let \(m\in\mathcal M_\ell\) be a candidate collapse macrocell. The assumptions
are:

**F1 (classical flow with focusing matter).** Every \(s\in C_m\) evolves under
the Einstein flow \(\Phi_t\) on its MGHD, with matter satisfying the null
energy condition, hence the null convergence condition
\(R_{ab}k^ak^b\geq 0\) along null congruences.

**F2 (trapped bins).** The bins defining \(m\) imply trappedness: every
\(s\in C_m\) contains a closed future-trapped surface \(\mathcal T_s\) whose
outgoing null expansion satisfies \(\theta_+\leq-\alpha<0\) pointwise, with
\(\alpha\) determined by the \(\bar\theta_R\) bin edge. ⚠ This is an
assumption on bin design, not a free lunch: coarse averaged bins
\((C_R,\bar\theta_R)\) do not automatically imply pointwise trappedness. It is
satisfiable — in spherical symmetry, compactness \(C_R>1\) at areal radius
\(R_{\mathrm{areal}}\) implies an outer trapped surface exactly, and in the
general case sufficient concentration of matter implies existence of trapped
surfaces (Schoen–Yau). A macrocell whose bins sit strictly inside the trapped
regime, with margin, satisfies F2.

**F3 (Penrose causality inputs).** Each development is globally hyperbolic
with a noncompact Cauchy surface.

**F4 (fixed description).** Over the verification window, no new admissible
variables, extensions, boundary transfers, or stochastic completion rules are
adjoined: the description remains \(\mathcal D_{\mathrm{cl}}\).

**F5 (relational clock compatibility).** The reference structure
\(\mathcal F_\ell\) includes a clock interior to or comoving with the
collapsing region, and this clock assigns finite verification duration to the
focusing interval: there exists \(\Delta^*(m)<\infty\) with
\(\tau_{\mathrm{fail}}(s)\leq\Delta^*(m)\) for all \(s\in C_m\) once Lemmas
1–4 below apply. ⚠ This is a substantive assumption and a deliberate seam: a
purely exterior static clock never registers the failure in finite time. That
is not a defect of the theorem; it is the content of Corollary 1. In the
benchmark interiors (Oppenheimer–Snyder and its perturbations) the comoving
proper time from trapped-surface formation to the incompleteness boundary is
finite and of order \(GM/c^3\), so F5 holds where it can be checked.

**F6 (nondegenerate cell measure).** \(\mu_m\) is a probability measure on
\(C_m\) absolutely continuous with respect to the background initial-data
measure, with full support on \(C_m\).

## 5. Lemmas

**Lemma 1 (focusing bound).** Under F1, let \(\theta(\lambda)\) be the
expansion of the outgoing null congruence orthogonal to a closed trapped
surface with \(\theta(0)=\theta_0\leq-\alpha<0\). Then \(\theta(\lambda)\to
-\infty\) at some affine parameter

$$
\lambda^*\leq\frac{2}{\alpha}.
$$

**Proof.** For a hypersurface-orthogonal null congruence in four dimensions,

$$
\frac{d\theta}{d\lambda}
=
-\frac{1}{2}\theta^2
-\sigma_{ab}\sigma^{ab}
-R_{ab}k^ak^b
\leq
-\frac{1}{2}\theta^2,
$$

since twist vanishes, shear-squared is nonnegative, and the null convergence
condition holds. Comparison with \(y'=-y^2/2\), \(y(0)=\theta_0\), which has
solution \(y(\lambda)=\theta_0/(1+\theta_0\lambda/2)\), gives
\(\theta(\lambda)\leq y(\lambda)\) while both exist; \(y\) diverges to
\(-\infty\) at \(\lambda=2/|\theta_0|\leq 2/\alpha\). Hence \(\theta\)
diverges no later. \(\square\)

**Lemma 2 (incompleteness; imported).** Under F1–F3, the MGHD of every
\(s\in C_m\) is future null geodesically incomplete.

**Source.** This is the Penrose singularity theorem applied pointwise on the
cell: F2 supplies the closed trapped surface, F1 the null convergence
condition, F3 the causality inputs. It is imported, not reproved. ⚠ Note the
conclusion is incompleteness, not curvature divergence; Lemma 4 handles the
distinction.

**Lemma 3 (full-measure failure set; openness).** Under F2 and F6, the subset
of \(C_m\) whose developments are future incomplete has \(\mu_m\)-measure one.
Moreover, strict trappedness is an open condition in the initial-data
topology, so the trapped cell contains an open set: trapped macrocells are
stable under perturbation of the data and are not measure-zero curiosities in
\(\mathcal S_{\mathrm{cl}}\).

**Proof.** The first claim is immediate from Lemma 2: F2 makes trappedness a
bin property, so every state in the cell — not merely a positive-measure
subset — develops incompleteness; the failing set is \(C_m\) itself. For the
second claim, \(\theta_+\leq-\alpha<0\) pointwise on a compact surface is a
strict inequality of continuous functionals of the data, hence survives
sufficiently small perturbations in any topology in which the constraint
solutions depend continuously on the data (Cauchy stability); the set of
strictly trapped data is therefore open, and by F6 any macrocell containing it
has positive measure. \(\square\)

**Lemma 4 (admissibility exit).** Under F4, every future-incomplete
development ceases to be an admissible state of \(\mathcal D_{\mathrm{cl}}\)
at finite relational time (finite by F5). Specifically, at least one of the
four admissibility conditions fails:

1. if curvature invariants diverge along the incomplete generators, **finite
   observables** fails;
2. if the MGHD is inextendible without curvature divergence, **finite
   continuation** fails directly: the flow \(\Phi_t\) has no admissible image
   beyond the boundary;
3. if the MGHD is extendible (a strong-cosmic-censorship-violating case),
   extensions beyond the Cauchy horizon are non-unique, so \(\Phi_t\) is no
   longer a single-valued flow determined by \(\mathcal D_{\mathrm{cl}}\);
   selecting an extension is new structure, excluded by F4, and without a
   selection the pushforward is not a function of the state — **finite
   continuation** fails for the fixed description.

In every case the local information-geometric interior block \(D_\ell\)
degenerates on the failing support (\(\lambda_{\min}(D_\ell)\to 0\)), so
**nondegenerate interior** fails as well, matching Proposition 1 of
`bridges/singularity_inadmissibility.md`.

**Proof.** Cases 1 and 2 are immediate from the definitions of admissibility.
Case 3: non-uniqueness of extensions beyond a Cauchy horizon is the standard
failure of determinism there; a kernel requires a well-defined pushforward
measure, which requires either a selection rule (new structure, violating F4)
or restriction to the MGHD, which returns to case 2. The Schur statement
follows because the failing directions are exactly those whose conditional
precision degenerates as the collapse concentrates: in the local Gaussian
approximation of the kernel bridge §8, focusing sends the retained interior
variance in the collapsing directions to zero, so \(D_\ell\) is singular on
that support. ⚠ The status of strong cosmic censorship is open in general;
the lemma does not need it to hold or fail — both branches exit
admissibility. \(\square\)

**Lemma 5 (exhaustiveness of classical constructions).** Under F4, any
stochastic kernel on \(\mathcal M_\ell^{\mathrm{adm}}\) constructible from
\((\mathcal S_{\mathrm{cl}},\Phi_t,\sigma_\ell,\mu)\) that agrees with the
classical flow wherever the flow is defined and admissible is one of the three
canonical constructions of Definition 2, up to the choice of absorbing cell
assignment.

**Proof.** On the sub-interval where the development of \(s\) is admissible,
agreement with the flow fixes the kernel's action. The only freedom is the
disposition of the mass of each \(s\) at \(\tau_{\mathrm{fail}}(s)\). The
available measurable data at failure are the classical data of \(s\)'s
development up to \(\tau_{\mathrm{fail}}(s)\). A disposition rule either
assigns this mass to no admissible cell (construction 1), removes it from the
ensemble with renormalization (construction 2), or maps it — necessarily as a
deterministic function of the available classical data, since F4 excludes new
stochastic rules — into admissible cells, where by continuity of
\(\sigma_\ell\circ\Phi_t\) up to the failure time the image is the cell of the
last admissible snapshot, frozen thereafter because the flow provides no
further admissible evolution (construction 3). A rule that spreads the mass
of a single datum over several cells, or evolves it after failure, would be a
new stochastic transition law or new dynamics, excluded by F4. \(\square\)

## 6. Main Theorems

**Theorem 1 (semiclassical collapse failure, quantitative form).** Let
\(m\) satisfy F1–F6 and let \(\Delta\) be a verification interval. Then for
the three classical constructions:

**(a) Naked pushforward: normalization failure.** The retained admissible
mass obeys

$$
Z^{\mathrm{adm}}_{\ell,\Delta}(m)
=
1-\mu_m\big(\{s:\tau_{\mathrm{fail}}(s)\leq\Delta\}\big),
$$

which is strictly less than \(1\) for every
\(\Delta>\inf_s\tau_{\mathrm{fail}}(s)\) and equals \(0\) for every
\(\Delta\geq\Delta^*(m)\). The kernel is not a stochastic kernel on admissible
macrocells for any such \(\Delta\).

**(b) Hard exclusion: postselection and record-balance failure.** For
\(\Delta\) with \(0<Z^{\mathrm{adm}}_{\ell,\Delta}(m)<1\), the renormalized
kernel \(\tilde P=K/Z\) is conditioned on non-failure. The discarded
coordination

$$
\Delta C_R(\Delta)
=
-\log Z^{\mathrm{adm}}_{\ell,\Delta}(m)
>
0
$$

grows without bound as \(\Delta\uparrow\Delta^*(m)\), while the boundary
record carries zero information about the discarded branch:

$$
I\big(X_R^{\mathrm{disc}};Y_{\partial}\big)=0 .
$$

This violates the decodable-redistribution requirement (Criterion 3 of
`bridges/cosmic_coordination_floor.md`) at every such \(\Delta\), and for
\(\Delta\geq\Delta^*(m)\) the construction is undefined (renormalizing zero
mass).

**(c) Terminal absorption: floor failure.** The absorbing construction is a
normalized kernel, but each absorbing cell \(m^\dagger\) has

$$
P_{\ell,\Delta}(m^\dagger|m^\dagger)=1
\quad\Longrightarrow\quad
H_{\ell,\Delta}(m^\dagger)=0
<
H_{\mathrm{floor}}(m^\dagger;\ell,\partial R),
$$

while the absorbed region remains physically active in the sense of the floor
axiom (nonzero stress-energy flux and growing sub-bin curvature: the freeze is
a property of the description, not of the region). The channel crystallizes
exactly.

**Proof.** (a) By Lemma 3 the failing set is all of \(C_m\); by Lemma 4 with
F5, \(\tau_{\mathrm{fail}}(s)\leq\Delta^*(m)<\infty\) on the cell. The
displayed identity is the definition of \(Z^{\mathrm{adm}}\) applied to the
failure-time sublevel sets, and both claims follow. (b) The discarded mass has
no image in \(\mathcal M_\ell^{\mathrm{adm}}\) and, under F4, no record
channel was adjoined that could carry information about it; the mutual
information between any function of the discarded branch and the boundary
record is therefore zero, while \(\Delta C_R=-\log Z\to\infty\) as
\(Z\to 0\). Conditioning on non-failure is by construction a postselection: it
defines a different theory, not the classical flow. (c) Absorption freezes the
image: the diagonal entry is \(1\), so the future entropy of the absorbing
cell is exactly zero; positivity of \(H_{\mathrm{floor}}\) for active cells is
the floor axiom, and activity holds because absorption was triggered by
failure of the description while the physical collapse (by F1–F2) continues
below bin resolution. \(\square\)

**Theorem 2 (no admissible classical collapse kernel).** Under F1–F6, with
\(\Delta\geq\Delta^*(m)\), there is no kernel constructible from
\(\mathcal D_{\mathrm{cl}}\) (Definition 2) that simultaneously satisfies:

- **(K1) classical consistency:** agreement with \(\Phi_t\) wherever the flow
  is defined and admissible;
- **(K2) normalization** on \(\mathcal M_\ell^{\mathrm{adm}}\);
- **(K3) record balance:** no coordination discarded without a decodable
  boundary record;
- **(K4) floor:** \(H_{\ell,\Delta}\geq H_{\mathrm{floor}}>0\) on active
  collapse cells.

**Proof.** By Lemma 5, any such kernel is one of the three canonical
constructions. Theorem 1(a) shows construction 1 violates K2; Theorem 1(b)
shows construction 2 violates K3 (and is undefined at \(\Delta^*\));
Theorem 1(c) shows construction 3 violates K4. \(\square\)

Theorem 2 is the strengthening this document exists for: Proposition 2 of the
kernel bridge concluded a disjunction of failures for the pushforward under an
assumed failing subset; Theorem 2 derives the failing subset (Lemmas 1–4),
quantifies the failure (Theorem 1), and closes the exit routes by quantifying
over every kernel the classical description can define (Lemma 5).

## 7. Corollary 1: Horizon Deferral Is Not Escape

Let \(\mathcal A_{\mathrm{ext}}\subset\mathcal A_{\mathrm{rel},\ell}(R)\) be
the exterior subalgebra and \(\mathcal M_\ell^{\mathrm{ext}}\) the exterior
macrocells labeled by \((M_\partial,J_\partial,Q_\partial,A_\partial,
N_0,Y_\partial)\).

**Corollary 1.** Under F1–F3 and F6, with horizon formation:

1. The exterior-restricted kernel can satisfy K1–K2 with an exterior static
   clock: mass flows into horizon-sector cells and remains normalized. This is
   the horizon-transfer policy, and it is a genuine boundary regularization of
   the exterior channel (`bridges/singularity_inadmissibility.md` §5).
2. The composite description still fails: the interior block \(D_\ell\) of the
   full partition degenerates by Lemma 4, so the Schur elimination defining
   the effective exterior law is illegal on the failing interior support. The
   exterior theory is admissible only as a theory that never again asks about
   the interior — a permanent-horizon idealization.
3. ⚠ (Semiclassical import.) Under Hawking evaporation the permanent-horizon
   idealization is unavailable: the horizon-area bin \(A_\partial\) descends
   toward zero in finite exterior relational time. At that scale the
   accumulated coordination debt \(\Delta C_R\) comes due, and a purely
   classical exterior kernel must either discard it without a decodable record
   (violating K3: information loss) or fail normalization on exterior
   macrocells (violating K2). Hence deferral has a deadline: the failure of
   Theorem 2 reappears in the exterior algebra at the decoding scale.

**Proof.** Claim 1 is a construction: redirect the collapsing mass to
horizon-sector cells at trapped-surface formation; normalization is preserved
because horizon cells are admissible exterior labels. Claim 2 is Lemma 4
applied to the interior directions together with Proposition 1 of
`bridges/singularity_inadmissibility.md`. Claim 3: evaporation makes the
horizon-cell family non-absorbing on exterior relational timescales; when
\(A_\partial\to 0\), the exterior kernel must dispose of the interior-sector
mass with only the classical data available, and Lemma 5's trichotomy applies
to the exterior description: no image (K2), deletion without record (K3), or
freezing an active channel (K4). The evaporation input is semiclassical and is
used only to exclude the permanent-horizon idealization. \(\square\)

## 8. Corollary 2: Forced Completion

**Corollary 2.** Any continuation of the collapse channel that satisfies
K2–K4 on a trapped macrocell with \(\Delta\geq\Delta^*(m)\) must:

1. **change mechanism:** adjoin structure beyond
   \(\mathcal D_{\mathrm{cl}}\) — new variables, a nonclassical transition
   rule, or a new record channel (by Theorem 2, no classical construction
   suffices);
2. **trigger before the floor is breached:** the intervention must act at some
   \(\Delta_{\mathrm{trig}}<\Delta^*(m)\), because by Theorem 1 every
   classical construction has already failed K2, K3, or K4 at \(\Delta^*\),
   and K4 is monotone under the classical flow inside the reinforcement basin
   (focusing narrows the admissible future set);
3. **preserve normalization** as a genuine stochastic/CPTP channel on
   admissible relational macrocells;
4. **be boundary-decodable:** the redistributed coordination must appear in
   the exterior record channel with
   \(I(X_R;Y_{\partial}^{[t,t+T_{\mathrm{dec}}]})\geq\eta\,\Delta C_R
   -\varepsilon\), since a hidden repair merely relocates the record-balance
   failure of Theorem 1(b) or Corollary 1.3.

This is exactly the Stage 3 object of the derivation ladder. Its early-privacy
property (bounded \(I(L_R;R_{\partial}^{\mathrm{early}}\mid G_\ell)\)) is not
forced by Theorem 2 and remains an axiom imported from Stage 6. ⚠ The
identification of the forced completion with quantum gravity — rather than
with some other mechanism-changing, normalization-preserving,
boundary-decodable channel — is the program's remaining conjecture, unchanged
in status by this theorem but now carrying a sharper burden: any candidate
that is *not* quantum gravity must still instantiate properties 1–4.

## 9. Referee Seams

The assumptions a hostile reviewer should attack, in expected order of
severity:

1. **F5 (relational clock).** The failure is finite-time only in an
   interior/comoving frame. The theorem is honest about this: the exterior
   story is Corollary 1, and the evaporation deadline there is a semiclassical
   import. A fully relational treatment of the clock transformation belongs to
   OP-29 (operational-time covariance).
2. **F2 (trapped bins).** Coarse bins implying pointwise trappedness is a bin
   design condition. It is provable in spherical symmetry and supported by
   concentration results generally, but a careless bin choice (averaged
   expansion only, no compactness margin) breaks the implication.
3. **NEC (in F1).** Quantum matter violates pointwise NEC; the classical
   theorem uses it. The correct semiclassical refinement would use achronal
   averaged energy conditions or quantum focusing ⚠ — an upgrade target, not
   a defect, since the theorem's role is to characterize the *classical*
   description's failure.
4. **Lemma 4 case 3 (extendible MGHDs).** The argument handles
   censorship-violating cases by determinism failure rather than curvature
   blowup. This is deliberate and ACP-native, but it means "singularity" in
   this document reads "exit from admissibility," which is broader than
   "curvature singularity."
5. **Measure choice (F6).** Full support and absolute continuity are mild but
   not free; a measure concentrated on non-generic symmetric data would be
   nonphysical for stability claims, though Lemma 3's full-measure conclusion
   needs only F2.

## 10. What This Adds

- Proposition 2's assumed hypothesis (positive-measure singular subset) is now
  derived from F1–F3 via Lemmas 1–3, and upgraded from positive measure to
  full measure on trapped macrocells.
- The normalization failure is quantitative:
  \(Z^{\mathrm{adm}}_{\ell,\Delta}(m)=1-\mu_m(\tau_{\mathrm{fail}}\leq\Delta)\),
  vanishing at \(\Delta^*(m)\), with the focusing bound
  \(\lambda^*\leq 2/\alpha\) controlling the failure clock.
- The trichotomy is now a no-go theorem (Theorem 2) over all kernels the
  classical description can define, via the exhaustiveness lemma (Lemma 5) —
  including the terminal-absorption route Proposition 2 treated only as a
  limiting case.
- Hard exclusion's failure is stated as record-balance violation with a
  divergent discarded-coordination bound \(\Delta C_R=-\log Z\), connecting
  Stage 2 directly to the Criterion 3 decodability requirement.
- Horizon formation is placed precisely: an admissible exterior
  regularization that defers the failure, with a semiclassical deadline at
  which the same trichotomy reappears in the exterior algebra.
- The forced-completion corollary converts Stage 3 from a structural
  requirement into a consequence of Theorem 2 plus the floor and
  record-balance axioms.

The numerical companion
`simulations/cosmic_coordination_floor/raychaudhuri_floor_check.py` verifies
the focusing bound, the quantitative mass-loss curve \(Z(\Delta)\), and the
hard-exclusion entropy collapse in a finite ensemble.
