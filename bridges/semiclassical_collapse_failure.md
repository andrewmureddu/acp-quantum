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
branch needs — a hypothesis that turns out to be false in the generic case.
Section 11 then repairs that gap (OP-30), which changes the conclusion: the
boundary gravitational collapse generically reaches is not the entropy floor
at all.

Two headline results:

> the expansion scalar \(\theta\) of the relational reference congruence *is*
> the crystallization drift rate of the CDT, expressed in geometric variables;

and

> gravitational collapse has two distinct ACP failure modes. Near-isotropic
> collapse crystallizes. Shear-dominated collapse — the astrophysically
> generic case — instead destroys the reference frame's capacity to carry its
> own macrostate label, while its coarse entropy stays far above the floor.

## 2. Honesty Boundary

**Proven here.** Lemmas 1–4 and Theorems A, A\('\), B, C, E, under the stated
hypotheses (F1)–(F3) and the global hypotheses of the Penrose theorem where
invoked. These are statements about geodesic-congruence kinematics and
coarse-graining, not new results in general relativity; the content is the
translation into ACP kernel variables with explicit rates, and the
identification of which ACP admissibility boundary collapse actually reaches.

**Numerically verified.** `simulations/semiclassical_collapse_failure/`
integrates the exact Jacobi deviation equation with a self-consistent dust
source and measures the coarse-grained entropy directly. The integrator
reproduces the analytic isotropic dust collapse time to five significant
figures.

**Assumed, then eliminated.** Hypothesis (R), shape regularity at scale
\(\ell\), underwrites Theorem A. Section 10 shows it fails under strong shear.
Section 11 replaces it with the provable Lemma 4 and then removes the need for
any shape hypothesis via Theorem E, which closes OP-30.

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
still meet very many cells. Section 10 shows this failure is not hypothetical:
the constant \(c\) rises to 251.8 under strong shear.

**(R) is superseded.** Section 11 replaces it with a deformation-spectrum bound
(R\('\)) that is provable rather than assumed, holds uniformly across all
scenarios with \(c_3\approx3.6\), and yields an exhaustive dichotomy requiring
no shape hypothesis at all. Hypothesis (R) is retained here because Theorem A
is stated in terms of it and because the contrast between (R) and (R\('\)) is
what identifies the real mechanism.

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

## 11. Closing the Shear Loophole (OP-30)

Section 10 leaves the entropy branch broken in the generic case. This section
repairs it — not by rescuing (R), but by replacing it with a bound that is
provable, and then observing that the repaired bound makes the shape hypothesis
unnecessary altogether.

### 11.1 Hypothesis (R\('\)): the deformation-spectrum bound

The defect in (R) is that it tracks \(\det J\), a single number, when the
object that determines cell count is the full deformation spectrum. Let
\(s_1\geq s_2\geq s_3\) be the singular values of the Jacobi matrix \(J\) —
the semi-axes of the image ellipsoid.

**Lemma 4 (cell count from the deformation spectrum).** For the image of a
convex body under \(J\),

$$
N_\Delta
\ \leq\
c_3\prod_{i=1}^{3}\left(1+\frac{s_i(\Delta)}{\ell}\right),
$$

with \(c_3\) a purely dimensional constant.

**Proof.** Any \(\ell\)-cell meeting a set \(K\) is contained in the
\(\ell\sqrt3\)-neighbourhood \(K\oplus B_r\), \(r=\ell\sqrt3\), so
\(N_\Delta\,\ell^3\leq\mathrm{vol}(K\oplus B_r)\). For convex \(K\), Steiner's
formula gives

$$
\mathrm{vol}(K\oplus B_r)=V(K)+A(K)\,r+M(K)\,r^{2}+\tfrac{4\pi}{3}r^{3},
$$

with \(V\), \(A\), \(M\) the volume, surface area, and integral mean curvature.
For an ellipsoid with semi-axes \(s_i\) these are, up to dimensional constants,
the elementary symmetric polynomials \(e_3=s_1s_2s_3\),
\(e_2=\sum_{i<j}s_is_j\), and \(e_1=\sum_i s_i\). Hence

$$
N_\Delta
\lesssim
\frac{e_3+\ell e_2+\ell^{2}e_1+\ell^{3}}{\ell^{3}}
=
\prod_{i=1}^{3}\left(1+\frac{s_i}{\ell}\right),
$$

the last equality being the exact factorization of the elementary symmetric
expansion. \(\square\)

(R) is the special case in which all \(s_i\) are comparable. (R\('\)) reduces
to it then, and departs from it exactly when the spectrum is anisotropic.

**Theorem A\('\) (spectral entropy bound).** Under (F1)–(F3),

$$
H_{\ell,\Delta}(m)
\ \leq\
\ln c_3+\sum_{i=1}^{3}\ln\!\left(1+\frac{s_i(\Delta)}{\ell}\right).
$$

The bound is unconditional — no shape hypothesis is required.

### 11.2 Why the entropy branch was failing

Theorem A\('\) makes the mechanism transparent. The right-hand side vanishes
only when **every** \(s_i\) falls below \(\ell\). But Lemma 2 guarantees only
that the *product* \(\det J=s_1s_2s_3\to0\). Focusing constrains the volume; it
does not constrain the individual axes.

> The entropy floor is breached when the congruence contracts below the
> resolution scale in *every* direction. Focusing only forces contraction *in
> volume*. Shear is precisely the difference between the two.

This is not a defect in the collapse argument. It is a statement about which
ACP boundary gravitational collapse actually hits — and it points directly at
the answer to OP-30's second question.

### 11.3 Frame resolution rank

**Definition (frame resolution rank).**

$$
\mathrm{rank}_\ell(J)=\#\{i:\ s_i\geq\ell\}.
$$

**Proposition E1 (frame degeneracy).** If \(\mathrm{rank}_\ell(J)<3\), the
relational reference structure \(\mathcal F_\ell\) no longer supplies three
independent directions resolvable at scale \(\ell\). The smearing functions
\(f_i(X(y))\) then cannot resolve the degenerate direction, so the bin map
\(b_i\) defining the macrocell is undefined there, and the description has
lost a distinction it claimed to make.

This is not a new axiom. It is the *nondegenerate interior* condition of
`bridges/singularity_inadmissibility.md` §2 — \(0<\mathrm{rank}(D)\) and
\(\kappa(D)<\infty\) — specialized to a congruence-realized frame. The two
clauses of that condition correspond to the two ways the spectrum can fail:

| spectrum failure | \(\mathrm{rank}_\ell\) | admissibility clause violated | ACP reading |
|---|---:|---|---|
| all \(s_i<\ell\) | 0 | \(\mathrm{rank}(D)>0\) | total crystallization |
| some but not all \(s_i<\ell\) | 1 or 2 | \(\kappa(D)<\infty\) | partial rank failure |

Proposition 1 of the singularity note already establishes that *partial* rank
failure is inadmissible for the original description, because the effective
boundary law requires \(D^{-1}\) in every retained internal direction. The
framework therefore already contained the criterion that shear-dominated
collapse violates; it had simply not been connected to the collapse kernel.

### 11.4 Theorem E: the exhaustive dichotomy

**Theorem E.** Assume (F1)–(F3). By the caustic deadline
\(\tau_\times\leq3/\alpha\), the relational description fails in exactly one of
two ways:

- **(a) Entropy floor breach.** \(\mathrm{rank}_\ell(J)=0\): every axis has
  contracted below the resolution scale, \(N_\Delta=1\), and
  \(H_{\ell,\Delta}(m)=0\). This is crystallization.
- **(b) Frame rank failure.** \(0<\mathrm{rank}_\ell(J)<3\): the congruence has
  contracted below \(\ell\) in some directions while remaining resolvable in
  others. The future entropy may remain far above the floor, but the frame can
  no longer label its own macrocells, and \(\kappa(D)\to\infty\).

**Proof.** By Lemma 2(3), \(\delta V\to0\) at \(\tau_\times\leq3/\alpha\), so
\(s_1s_2s_3\to0\) and therefore \(s_3\to0<\ell\). Hence
\(\mathrm{rank}_\ell(J)<3\) necessarily. The two cases are distinguished by
whether \(\mathrm{rank}_\ell\) is zero, and they are exhaustive and mutually
exclusive. \(\square\)

**No shape hypothesis is used.** Theorem E follows from Lemma 2 alone. It is
strictly stronger than the entropy branch of Theorem C, which required (R) and
was false in the generic case.

The upshot for the program: gravitational collapse has **two** distinct ACP
failure modes, not one. Near-isotropic collapse crystallizes. Shear-dominated
collapse — the astrophysically generic case — instead destroys the reference
frame's ability to carry the macrostate label, while its coarse entropy stays
high. Both are inadmissible, and both are covered by admissibility conditions
the framework already had.

### 11.5 Numerical verification of the repair

Same runs as Section 10, with the deformation spectrum now tracked.

| scenario | \(s_{\mathrm{final}}=(s_1,s_2,s_3)\) | \(\mathrm{rank}_\ell\) | \(\tau\) rank-deficient | \(\tau_\times\) | \(H_{\mathrm{final}}\) | Thm A\('\) ceiling | max \(c_3\) | max \(c\) (old) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| isotropic | (0.00118, 0.00118, 0.00118) | 0 | 1.843 | 1.8717 | 0.000 | 1.90 | 3.43 | 9.09 |
| moderate shear | (0.234, 0.234, 1.8e−05) | 2 | 1.6485 | 1.7294 | 4.221 | 5.33 | 3.44 | 23.0 |
| strong shear | (0.961, 0.961, 1.84e−05) | 2 | 0.900 | 0.9868 | 8.095 | 8.67 | 3.61 | 251.8 |
| unbound expansion | (4.03, 4.03, 4.03) | 3 | none | none | 14.220 | 17.96 | 3.42 | 1.086 |

Entropies in bits; \(\ell=0.10\); floor 1.50 bits.

1. **(R\('\)) holds uniformly.** The measured constant \(c_3\) is
   3.43, 3.44, 3.61, 3.42 — essentially scenario-independent — where the old
   constant \(c\) ranged over 1.086 to 251.8. The deformation spectrum is the
   right variable.
2. **Theorem A\('\) is tight where it matters.** Predicted ceilings against
   measured entropies: 8.67 vs 8.095 (strong shear), 5.33 vs 4.221 (moderate).
   The bound is not merely valid, it is close.
3. **Theorem E's dichotomy is confirmed.** \(\mathrm{rank}_\ell\) drops below 3
   before the caustic in every focusing run
   (1.843 < 1.8717, 1.6485 < 1.7294, 0.900 < 0.9868), and reaches 0 only in the
   isotropic run — which is exactly the only run that breaches the entropy
   floor. Rank predicts the branch with no exceptions.
4. **The control stays admissible.** The unbound run keeps
   \(\mathrm{rank}_\ell=3\) throughout, with all axes growing.

The final spectra make the mechanism visible directly: under shear the
collapsing congruence ends as a pancake with \(s_3\sim10^{-5}\ell\) and
\(s_1=s_2\approx10\,\ell\). Its volume has vanished, its coarse entropy is 8
bits, and it cannot resolve its own third direction.

## 12. Corollary (Forced Completion)

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
4. **Restore frame rank, not merely volume.** By Theorem E the generic failure
   is \(\mathrm{rank}_\ell(J)<3\), not \(H\to0\). A completion that keeps the
   future entropy above the floor while leaving the congruence degenerate in
   one direction has not repaired the description — it has satisfied the wrong
   diagnostic. The requirement is
   $$s_i(\tau)\geq\ell\quad\text{for all }i,$$
   i.e. the mechanism must arrest contraction *in every direction* before the
   deadline, not just in volume.

Requirement 2 is quantitative: it converts "quantum gravity must prevent
crystallization" into a rate condition with a number in it, tied to an
observable of the classical solution. Requirement 4 is the sharper acceptance
test that OP-30 produced, and it is the one that bites in the astrophysically
generic case — the two are independent, since a mechanism can inject entropy
at rate \(|\theta|\) while still permitting one axis to collapse.

## 13. What Is Proven, Assumed, and Open

**Proven.** Lemmas 1–4; Theorems A, A\('\), B1, B2, C, E; Propositions D, E1.
Theorem A is conditional on (R); Theorems A\('\), B1, C branch 1, and E are
not.

**Assumed.** (F1) strong energy condition, (F2) irrotational congruence, (F3)
initial focusing. These are the standard focusing hypotheses, stated at
macrocell level in \(\mathcal B_{\mathrm{coll}}(\alpha,\beta)\). The former
weak point, (R), is no longer load-bearing: Theorem A\('\) replaces it with the
provable Lemma 4, and Theorem E dispenses with a shape hypothesis entirely.

**OP-30 is closed.** Both questions are answered.

1. *A shear-robust replacement for (R)?* Yes — hypothesis (R\('\)), proven as
   Lemma 4 via Steiner's formula, with the elementary-symmetric expansion
   factorizing exactly into \(\prod_i(1+s_i/\ell)\). The measured constant is
   \(c_3\approx3.6\) uniformly across all four scenarios, against an old
   constant \(c\) ranging over two orders of magnitude.
2. *Does filamented collapse fail a different admissibility condition?* Yes —
   frame rank failure rather than the entropy floor. Theorem E makes the
   dichotomy exhaustive: since \(\det J\to0\) forces \(s_3<\ell\), the
   description always loses frame rank, and it breaches the entropy floor only
   in the special case where *all* axes contract below \(\ell\). Numerically,
   \(\mathrm{rank}_\ell\) predicts the branch with no exceptions.

The affirmative answer to question 2 has the consequence anticipated for it:
the entropy floor is **not** the only ACP boundary gravitational collapse can
hit, and the one it generically hits is the other one. This connects the
collapse kernel to the operational frame conditions of
`bridges/operational_time_relativity.md`, where the reference frame's capacity
to carry distinguishable verification steps is the primitive.

**Residual gap.** Proposition E1 identifies frame rank failure with
\(\kappa(D)\to\infty\) in the Schur reading. The precise identification of
\(D\) with the deformation spectrum requires the local Gaussian approximation
of `bridges/relational_observable_macrostate_kernel.md` §8, whose regularity
conditions are exactly the content of **OP-3**. The correspondence in §11.3
should be read as structural until OP-3 is closed.

**Still conjectural.** That the forced completion of Section 12 is quantum
gravity. Theorem C establishes that classical spacetime is not a complete
admissible kernel, Theorem E identifies which boundary it fails at, and
Section 12 constrains what must replace it. None of them constructs the
replacement.
