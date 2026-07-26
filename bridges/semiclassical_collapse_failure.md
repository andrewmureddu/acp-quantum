# Semiclassical Collapse Failure Theorem

*Status: active OP-18/OP-19 bridge. Proven at the congruence-kinematic level
under stated hypotheses; numerically verified; conjectural only in the lift to
a complete microscopic quantum gravity.*

Companion notes:

- `bridges/quantum_gravity_derivation_program.md` (Stage 2 target theorem)
- `bridges/relational_observable_macrostate_kernel.md` (Proposition 2, superseded here)
- `bridges/cosmic_coordination_floor.md` (Stage B of the formalization roadmap)
- `bridges/singularity_inadmissibility.md`
- `simulations/semiclassical_collapse_failure/` (numerical verification)

## 1. What This Closes

Three documents named the same missing step. Stage 2 of the derivation program
asks for a theorem; Stage B of the coordination-floor roadmap asks for the same
theorem; OP-18 and OP-19 both list it as the next hard move.

The existing statement is Proposition 2 of
`bridges/relational_observable_macrostate_kernel.md`. That proposition is
honest but weak in a specific way: it *assumes* that a positive-measure subset
of the initial cell reaches an inadmissible singular set before \(\Delta\), and
then derives the consequences. The assumption is most of the content, and the
entropy branch is left qualitative ("if focusing also concentrates the retained
futures into a single cell").

This note removes that assumption. It derives the failure from explicit
focusing hypotheses, makes the entropy branch quantitative with a rate and a
breach time, and identifies precisely which further hypothesis the entropy
branch needs — a hypothesis that turns out to be false in an interesting
regime, which is reported rather than hidden.

The headline identification is:

> the expansion scalar \(\theta\) of the relational reference congruence *is*
> the crystallization drift rate of the CDT, expressed in geometric variables.

## 2. Honesty Boundary

**Proven here.** Lemmas 1–3 and Theorems A–C, under the stated hypotheses
(F1)–(F3), (R), and the global hypotheses of the Penrose theorem where invoked.
These are statements about geodesic-congruence kinematics and coarse-graining,
not new results in general relativity; the content is the translation into ACP
kernel variables with explicit rates.

**Numerically verified.** `simulations/semiclassical_collapse_failure/`
integrates the exact Jacobi deviation equation with a self-consistent dust
source and measures the coarse-grained entropy directly. The integrator
reproduces the analytic isotropic dust collapse time to five significant
figures.

**Assumed, not proven.** Hypothesis (R), shape regularity at scale \(\ell\).
Section 8 shows it fails under strong shear, and Section 9 records the
consequence.

**Conjectural.** That the completion forced by Theorem C and its corollary is
quantum gravity. This note constrains the completion; it does not construct it.

**Not claimed.** This note does not prove cosmic censorship, derive the
Einstein equations, quantize the metric, or establish curvature-invariant
blow-up. It deliberately uses geodesic incompleteness and frame breakdown
rather than curvature divergence, for the reason given in Section 6.

## 3. Setup: The Relational Frame Is a Congruence

`bridges/relational_observable_macrostate_kernel.md` §3 defines the relational
observables against a finite operational reference structure
\(\mathcal F_\ell=\{X^0,\ldots,X^3;\partial R;\ell\}\), with observables

$$
\mathcal O_i[f_i;X]
=
\int_R d^3y\,\sqrt q\,f_i(X(y))\,\mathcal O_i(q,K,\phi,\pi_\phi;y).
$$

The point to make explicit is that \(\mathcal F_\ell\) is not an abstract
label set. Physically realized, a reference frame of material clocks and rods
is a **congruence**: a family of timelike worldlines filling \(R\), with
tangent \(u^a\), proper time \(\tau\), and expansion \(\theta=\nabla_a u^a\).

This is what makes the focusing theorems speak directly to the ACP kernel. The
same object that defines which distinctions an observer can record is the
object that Raychaudhuri's equation governs.

Throughout, \(d=3\) spatial dimensions, \(v_\ell=\ell^3\) is the cell volume of
the macrocell partition \(\Pi_\ell\), and \(\delta V(\tau)\) is the
cross-sectional volume element of the congruence. Entropies are in nats where
\(\ln\) appears and bits where \(\log_2\) appears; conversions are stated.

### Focusing hypotheses

- **(F1) Energy condition.** The strong energy condition holds along the
  congruence: \(R_{ab}u^au^b\geq 0\).
- **(F2) Irrotational.** The congruence is hypersurface-orthogonal,
  \(\omega_{ab}=0\). This is the natural condition for a frame that defines
  simultaneity slices, i.e. for a frame that can carry a macrostate label.
- **(F3) Initial focusing.** The macrocell \(m\) lies in the collapse basin:
  \(\theta(0)\leq-\alpha<0\).

(F3) is exactly the macrocell-level bin condition \(\bar\theta_R<-\alpha\) of
\(\mathcal B_{\mathrm{coll}}(\alpha,\beta)\) in
`bridges/cosmic_coordination_floor.md` §5.

## 4. Lemma 1 (Volume Law)

**Lemma 1.** For a geodesic congruence with expansion \(\theta\), the
cross-sectional volume element obeys

$$
\frac{d}{d\tau}\ln\delta V=\theta,
\qquad
\delta V(\tau)=\delta V(0)\exp\!\int_0^\tau\theta\,d\tau' .
$$

This is exact and requires no energy condition. It is the definition of
\(\theta\) as the logarithmic rate of change of the congruence volume element.

Lemma 1 is the whole reason the expansion scalar is an ACP quantity: it is
already a *rate of change of a logarithm of a measure*, which is the functional
form of a drift rate on an entropy.

## 5. Lemma 2 (Quantitative Focusing)

**Lemma 2.** Assume (F1)–(F3). Then, on the domain where the congruence is
defined:

1. \(\theta\) is non-increasing, hence \(\theta(\tau)\leq-\alpha\);
2. \(\displaystyle\theta(\tau)\leq\frac{-3\alpha}{3-\alpha\tau}\), and a caustic
   \(\theta\to-\infty\) forms at some \(\tau_\times\leq 3/\alpha\);
3. the volume element obeys both a uniform and a sharp bound,

$$
\delta V(\tau)\leq\delta V(0)\,e^{-\alpha\tau},
\qquad
\delta V(\tau)\leq\delta V(0)\left(1-\frac{\alpha\tau}{3}\right)^{3}.
$$

**Proof.** The Raychaudhuri equation for a timelike geodesic congruence is

$$
\frac{d\theta}{d\tau}
=
-\frac{1}{3}\theta^{2}
-\sigma_{ab}\sigma^{ab}
+\omega_{ab}\omega^{ab}
-R_{ab}u^au^b .
$$

By (F2) the rotation term vanishes; by (F1) the curvature term is
non-positive; and \(\sigma_{ab}\sigma^{ab}\geq0\). Hence
\(d\theta/d\tau\leq-\tfrac13\theta^2\leq0\), which with (F3) gives claim 1.

For claim 2, on any interval where \(\theta<0\),

$$
\frac{d}{d\tau}\left(\theta^{-1}\right)
=-\theta^{-2}\frac{d\theta}{d\tau}
\geq
-\theta^{-2}\left(-\tfrac13\theta^{2}\right)
=\tfrac13 ,
$$

so \(\theta^{-1}(\tau)\geq\theta^{-1}(0)+\tau/3\geq-\tfrac1\alpha+\tfrac\tau3\).
Both sides are negative for \(\tau<3/\alpha\); inverting reverses the
inequality and gives \(\theta(\tau)\leq-3\alpha/(3-\alpha\tau)\). The right-hand
side diverges as \(\tau\uparrow3/\alpha\), so \(\theta\) cannot remain finite
beyond \(3/\alpha\).

For claim 3, substitute into Lemma 1. The uniform bound uses
\(\theta\leq-\alpha\), giving \(\int_0^\tau\theta\leq-\alpha\tau\). The sharp
bound uses claim 2:

$$
\int_0^\tau\theta\,d\tau'
\leq
\int_0^\tau\frac{-3\alpha}{3-\alpha\tau'}\,d\tau'
=
3\ln\!\left(1-\frac{\alpha\tau}{3}\right),
$$

and exponentiating gives the cubic law. \(\square\)

The exponent 3 is the spatial dimension; for a homogeneous dust ball
\(\delta V\propto a^3\) and the bound has the right form.

## 6. Lemma 3 (Coarse-Graining Bound) and Hypothesis (R)

The kernel \(P_{\ell,\Delta}(m'|m)\) is the distribution of the coarse label of
the image of cell \(C_m\). Its entropy is bounded by the log of the number of
cells the image meets.

**Lemma 3.** Let \(N_\Delta\) be the number of cells of \(\Pi_\ell\) met by the
image of \(C_m\) at time \(\Delta\). Then

$$
H_{\ell,\Delta}(m)\leq\log N_\Delta .
$$

**Proof.** The distribution \(P_{\ell,\Delta}(\cdot|m)\) is supported on those
\(N_\Delta\) cells, and the entropy of a distribution on a finite support is
maximized by the uniform distribution. \(\square\)

To convert Lemma 2's volume bound into an entropy bound, one needs a link from
volume to cell count. That link is a genuine extra hypothesis:

> **(R) Shape regularity at scale \(\ell\).** There is a constant \(c\geq1\)
> with
> $$N_\Delta\leq c\left(1+\frac{\delta V(\Delta)}{v_\ell}\right).$$

(R) holds when the image has bounded eccentricity at scale \(\ell\) — when its
diameter is comparable to \(\delta V^{1/3}\). It **fails** for images that are
filamented or pancaked at scale \(\ell\), where a set of vanishing volume can
still meet very many cells. Section 8 shows this failure is not hypothetical.

**Why geodesic incompleteness rather than curvature blow-up.** The ACP
admissibility conditions of `bridges/singularity_inadmissibility.md` §2 include
*finite continuation*: \(\Phi_t\) must carry admissible states to admissible
states over the verification timescale. That is precisely what the singularity
theorems deliver — they prove geodesic incompleteness, not curvature
divergence. ACP's admissibility criterion is therefore better matched to what
is actually provable in GR than a curvature-based criterion would be. This is a
strengthening of the framework's position, and it is worth stating plainly.

## 7. Theorem A (Entropy Floor Breach)

**Theorem A.** Assume (F1)–(F3) and (R). Then

$$
H_{\ell,\Delta}(m)
\leq
\ln c+\ln\!\left(1+\frac{\delta V(0)}{v_\ell}e^{-\alpha\Delta}\right)
\quad\text{nats}.
$$

Write \(H^{\mathrm{vol}}_0=\ln\!\big(\delta V(0)/v_\ell\big)\) for the
volumetric initial entropy scale. In the resolved regime
\(\delta V(\Delta)\geq v_\ell\) the bound linearizes to

$$
H_{\ell,\Delta}(m)
\leq
H^{\mathrm{vol}}_0+\ln(2c)-\alpha\Delta ,
$$

so the conditional future entropy decays at rate at least \(\alpha\) nats
(equivalently \(\alpha/\ln2\) bits) per unit proper time. Consequently the
coordination floor \(H_{\mathrm{floor}}>0\) is breached no later than

$$
\Delta_{\mathrm{floor}}
=
\frac{H^{\mathrm{vol}}_0+\ln(2c)-H_{\mathrm{floor}}}{\alpha},
$$

and in any case \(\delta V\to0\) at \(\tau_\times\leq3/\alpha\), where
\(N=1\) and \(H_{\ell,\Delta}(m)=0\) exactly.

**Proof.** Combine Lemma 3, (R), and Lemma 2(3) for the first bound. For the
linearization, put \(x_\Delta=\delta V(\Delta)/v_\ell\); in the resolved regime
\(x_\Delta\geq1\), so \(\ln(1+x_\Delta)\leq\ln(2x_\Delta)\), and
\(\ln x_\Delta\leq H^{\mathrm{vol}}_0-\alpha\Delta\) by Lemma 2(3). The final
claim uses Lemma 2(3) in cubic form, which vanishes at \(\tau=3/\alpha\).
\(\square\)

**On the two initial scales.** The theorem is stated with \(H^{\mathrm{vol}}_0\)
rather than the actual initial entropy \(H_{\ell,0}(m)\) because (R) bounds cell
count from above, which gives \(H_{\ell,0}\leq\ln c+\ln(1+x_0)\) — the wrong
direction to substitute. The two agree up to the additive constant whenever the
initial cell is well resolved and its coarse-graining is near-uniform. The
simulation confirms this is not a vacuous caveat: there
\(\log_2(\delta V(0)/v_\ell)=12.03\) bits against a measured
\(H_{\ell,0}=11.963\) bits.

**The CDT identification.** Differentiating the bound and comparing with
Lemma 1:

$$
\frac{dH_{\ell,\Delta}}{d\Delta}\ \lesssim\ \theta .
$$

The expansion scalar is the crystallization drift rate. Gravitational
focusing is not merely *analogous* to crystallization drift in the ACP sense —
under (R) it is the same quantity, written in geometric variables. This is the
sharpest contact the program has yet made between the CDT and general
relativity.

## 8. Theorem B (Normalization Failure) — Two Tiers

**Theorem B1 (frame tier).** Assume (F1)–(F3). Let \(C_m^{\mathrm{foc}}\subseteq C_m\)
be the subset of initial data whose reference congruence satisfies the focusing
hypotheses. For any \(\Delta>3/\alpha\), the relational frame \(\mathcal F_\ell\)
develops a caustic before \(\Delta\), so the relational observables
\(\mathcal O_i[f_i;X]\) — and hence the coarse label
\(\sigma_\ell(\Phi_\Delta(s))\) — are undefined on that subset. Those states
contribute no mass to any admissible macrocell, so

$$
Z^{\mathrm{adm}}_{\ell,\Delta}(m)\ \leq\ 1-\mu_m\!\left(C_m^{\mathrm{foc}}\right)\ <\ 1 .
$$

**Theorem B2 (spacetime tier).** Add the Penrose hypotheses: the maximal
development is globally hyperbolic with noncompact Cauchy surface, the null
energy condition holds, and \(C_m\) contains a closed trapped surface. Then the
development is future null geodesically incomplete, and no re-choice of
reference frame within classical general relativity restores finite
continuation.

**Why both tiers are needed.** A caustic is a breakdown of a *chosen*
congruence, not necessarily of spacetime; one can often re-choose the frame.
B1 alone therefore establishes that *this description* has failed and must be
replaced — which is exactly the reading of
`bridges/singularity_inadmissibility.md` §1, that a singularity is an
instruction to change the description. B2 is what rules out repairing the
failure by re-description within classical GR. Conflating the two tiers would
be an overclaim, and keeping them separate is what makes the ACP trigger fire
*earlier* than the curvature singularity — which is what "redistribution before
the floor is breached" requires.

## 9. Theorem C (Collapse Failure Trichotomy)

**Theorem C.** Let \(m\in\mathcal B_{\mathrm{coll}}(\alpha,\beta)\) satisfy
(F1)–(F3), and let \(\Delta>3/\alpha\). Then the classical relational
pushforward kernel satisfies at least one of:

1. **Normalization failure.** \(Z^{\mathrm{adm}}_{\ell,\Delta}(m)<1\)
   (Theorem B1; strengthened to genuine incompleteness by B2).
2. **Postselection.** The renormalized kernel
   \(\tilde P^{\mathrm{cl}}_{\ell,\Delta}\) is conditioned on non-singular
   survival, and therefore defines a different theory carrying an undischarged
   coordination debt with no boundary record.
3. **Floor violation.** \(H_{\ell,\Delta}(m)<H_{\mathrm{floor}}\), and in the
   limit \(H_{\ell,\Delta}(m)\to0\) (Theorem A, under (R)).

Hence classical collapse is not a complete admissible kernel for a nontrivial
persistent gravitational region.

This is the statement Stage 2 of the derivation program and Stage B of the
coordination-floor roadmap asked for. It supersedes Proposition 2 of
`bridges/relational_observable_macrostate_kernel.md` by deriving that
proposition's central hypothesis instead of assuming it.

### Proposition D (shear trade-off) — why the disjunction is the right form

Neither branch of Theorem C holds universally on its own, and the failure of
each is caused by the same quantity.

Shear enters the Raychaudhuri equation with the same sign as the energy term,
so it **accelerates** caustic formation and strengthens branch 1. Shear also
drives anisotropic distortion of the image, which increases \(N_\Delta\) at
fixed \(\delta V\) — that is, it degrades hypothesis (R) and **weakens**
branch 3.

**Proposition D.** Increasing shear strengthens the normalization branch and
weakens the entropy branch of Theorem C. The disjunction is therefore stable
even though neither disjunct is individually robust.

Section 10 verifies this numerically, including the regime where the entropy
branch fails outright.

## 10. Numerical Verification

`simulations/semiclassical_collapse_failure/` integrates the exact Jacobi
deviation equation \(\ddot J=-\mathcal R J\) for the congruence, with a
self-consistent pressureless dust source \(\mathrm{tr}\,\mathcal R=\kappa/\det J\)
(so the strong energy condition holds identically) plus an optional constant
traceless Weyl-like tidal term. Taking the trace of \(\dot B=-\mathcal R-B^2\)
with \(B=\dot JJ^{-1}\) reproduces the Raychaudhuri equation identically, so
this is congruence kinematics rather than an analogy. The coarse entropy is
measured by binning a cloud of 20 000 sample points at resolution
\(\ell=0.10\), averaged over four random grid offsets.

Initial expansion \(\theta_0=-0.60\) in all focusing runs, so \(\alpha=0.60\)
and the Lemma 2 bound is \(\tau_\times\leq3/\alpha=5.0\). The floor is
\(H_{\mathrm{floor}}=1.50\) bits, matching the existing
`cosmic_coordination_floor` toy.

| scenario | \(\sigma_0\) | \(H_0\) bits | \(H_{\mathrm{final}}\) bits | measured slope (bits/\(\tau\)) | Thm A bound | \(\tau\) floor breach | \(\tau_\times\) measured | \(c\) initial | max \(c\) in (R) regime |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| isotropic | 0.00 | 11.963 | 0.000 | −5.563 | −0.866 | 1.8621 | 1.8717 | 1.086 | 9.09 |
| moderate shear | 0.12 | 11.963 | 4.221 | −4.477 | −0.866 | none | 1.7294 | 1.086 | 23.0 |
| strong shear | 0.45 | 11.963 | 8.095 | −3.920 | −0.866 | none | 0.9868 | 1.086 | 251.8 |
| unbound expansion | 0.00 | 11.963 | 14.220 | +0.376 | n/a | none | none | 1.086 | 1.086 |

**Integrator validation.** For the isotropic case the model reduces to
\(\ddot a=-\kappa/(3a^2)\), whose collapse time can be computed in closed form.
The analytic value is \(\tau=1.871746\); the simulation gives \(1.8717\).

**Readings.**

1. *Theorem C holds in every focusing run.* All three collapse scenarios reach
   a caustic well inside the bound \(3/\alpha=5.0\), so branch 1 fires
   universally.
2. *Theorem A's bound is valid but conservative.* Measured decay slopes are
   4.5–6.4 times steeper than the guaranteed \(-\alpha/\ln2=-0.866\) bits per
   unit proper time, because self-consistent dust drives \(\theta\) far below
   \(-\alpha\) rather than holding it at the initial value. The floor is
   breached much earlier than the theorem promises.
3. *The entropy branch alone is not robust.* Only the isotropic run breaches
   the floor before the caustic. Under shear the coarse entropy is still 4.2
   and 8.1 bits at frame breakdown — comfortably above the floor.
4. *Proposition D is confirmed quantitatively.* Across
   \(\sigma_0=0.00,0.12,0.45\): caustic time falls monotonically
   \(1.8717\to1.7294\to0.9868\) while final entropy rises monotonically
   \(0.000\to4.221\to8.095\). More shear buys an earlier normalization failure
   at the cost of a weaker entropy failure.
5. *Hypothesis (R) fails under shear, as suspected.* The shape constant is
   \(c\approx1.086\) initially and stays there for the isotropic control, but
   reaches 251.8 under strong shear while the image still has volume above one
   cell. The filamentation loophole is real and large.
6. *The control behaves.* The unbound run has no focusing, constant
   \(c=1.086\), and monotonically growing entropy — confirming that focusing,
   not coarse-graining per se, is what drives the decay.

**Caveats.** The measured \(H_0=11.963\) bits is sample-limited (the ceiling is
\(\log_2 20\,000=14.29\) bits), so initial entropies are underestimates and the
unbound control's final value is a lower bound. This does not affect any
conclusion, all of which concern decay toward zero rather than absolute level.
The model is congruence kinematics with a homogeneous dust source, not
numerical relativity.

## 11. Corollary (Forced Completion)

**Corollary.** Any completion of classical gravity that avoids all three
branches of Theorem C for a collapsing region must:

1. **Trigger in time.** Supply new admissible support before
   \(\tau_\times\leq3/\alpha\), where \(\alpha=|\theta(0)|\) is read directly
   off the initial macrocell bin. The trigger deadline is set by the expansion
   scalar, not by a curvature threshold.
2. **Match the drift rate.** Offset a classical contraction of conditional
   future entropy proceeding at rate \(|\theta|\) nats per unit proper time
   (Lemma 1). Holding \(H_{\ell,\Delta}\geq H_{\mathrm{floor}}\) requires the
   mechanism to supply admissible support at no less than that rate — and
   \(|\theta|\) diverges as the caustic approaches, so the requirement
   stiffens without bound as the deadline nears.
3. **Discharge the debt.** Carry the removed coordination into a decodable
   boundary record, per Criterion 3 of
   `bridges/cosmic_coordination_floor.md`; otherwise the completion has merely
   relabelled branch 2.
4. **Survive shear.** Remain admissible in the shear-dominated regime, where
   Proposition D shows the entropy branch is weak and the normalization branch
   is what actually fires — and fires *sooner*.

Requirement 2 is new and quantitative: it converts "quantum gravity must
prevent crystallization" into a rate condition with a number in it, tied to an
observable of the classical solution.

## 12. What Is Proven, Assumed, and Open

**Proven.** Lemmas 1–3; Theorems A, B1, B2, C; Proposition D. Theorem A is
conditional on (R); Theorems B1 and C branch 1 are not.

**Assumed.** (F1) strong energy condition, (F2) irrotational congruence, (F3)
initial focusing, and (R) shape regularity. (F1)–(F3) are the standard focusing
hypotheses and are stated at macrocell level in
\(\mathcal B_{\mathrm{coll}}(\alpha,\beta)\). (R) is the weak point and is
known to fail.

**Open — and now sharper.** Section 10 turns a suspicion into a measured
failure: shear-dominated collapse focuses *faster* while keeping coarse entropy
*high*. Two questions follow, tracked as **OP-30**:

1. Is there a shear-robust replacement for (R) — a bound on \(N_\Delta\) that
   survives filamentation, perhaps in terms of the full deformation spectrum of
   \(J\) rather than \(\det J\) alone? The natural candidate is a bound using
   the singular values \(s_1\geq s_2\geq s_3\) of \(J\), with
   \(N_\Delta\approx\prod_i\max(1,s_i/\ell)\) replacing \(\delta V/v_\ell\).
2. Does a filamented high-entropy state actually satisfy the ACP productive
   interval, or does it fail a *different* admissibility condition — record
   decodability rather than future entropy? A congruence that is one cell thick
   in one direction cannot support the relational observables that define the
   macrocell, which suggests filamentation breaches admissibility through
   \(\mathcal F_\ell\) rather than through \(H\).

Question 2 is the more interesting one for the program, because an affirmative
answer would mean the entropy floor is not the only ACP boundary that
gravitational collapse can hit — and would connect this note to the operational
frame conditions in `bridges/operational_time_relativity.md`.

**Still conjectural.** That the forced completion of Section 11 is quantum
gravity. Theorem C establishes that classical spacetime is not a complete
admissible kernel and Section 11 constrains what must replace it. Neither
constructs the replacement.
