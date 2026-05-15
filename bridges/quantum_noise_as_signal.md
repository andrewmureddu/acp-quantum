# Noise-Tailored Encoding in a Two-Qubit Decoherence-Free Subspace

*A quantum ACP bridge note with Qiskit density-matrix simulation*

*Status: formal toy model; simulation-backed; not an active-feedback protocol.*

## Abstract

This note studies a minimal instance of noise-tailored quantum encoding. In a
two-qubit dephasing model, an encoding adapted to the symmetry of collective
phase noise lies in a decoherence-free subspace (DFS) and preserves true branch
coherence under environmental coupling that decoheres an unadapted encoding.
The result is analytic: under fully collective dephasing, the DFS coherence is
invariant, while the unadapted coherence decays exponentially. A classical
Gaussian environment-fragment model then computes explicit Shannon quantities:
charge-sector syndrome information and logical leakage to the environment.
Under correlated dephasing, the environment can carry information about the
error sector while remaining blind to the DFS logical branch. The induced
logical channel also has an explicit entanglement fidelity and coherent
information: in the fully collective limit the adapted DFS channel retains one
logical qubit of coherent information, while the unadapted channel loses it. A
Qiskit/NumPy density-matrix simulation confirms the analytic behavior across a
two-parameter scan of coupling strength and noise correlation structure.

## 1. Motivation and Terminology

In quantum error correction and mitigation, the professional version of "noise
as signal" is not that noise is desirable in itself. The standard formulation is
that physically realistic noise is often biased, correlated, or symmetry
constrained, and that an encoding, decoder, or mitigation protocol can exploit
that structure. The relevant vocabulary is:

- noise-tailored or noise-adapted encoding;
- symmetry-adapted encoding;
- decoherence-free subspace / noiseless subsystem;
- biased-noise or correlated-noise QEC;
- syndrome-bearing degrees of freedom;
- detectable versus undetectable error components;
- logical information leakage to the environment.

This note uses the two-qubit DFS for collective dephasing as the smallest
example of that program. The target is not generic isolation from the
environment. It is separation between information about the error sector and
information about the encoded logical state.

In quantum information language, the target is not

$$ I(\mathrm{system};\mathrm{environment}) = 0 $$

without qualification. Rather, the useful regime separates error information
from logical information:

$$ I(\mathrm{error};\mathrm{syndrome}) > 0, $$

while

$$ I(\mathrm{logical\ state};\mathrm{environment}) \approx 0. $$

This is the information-theoretic version of noise tailoring: expose or infer
the error degrees of freedom while keeping the logical degrees of freedom
private.

The civil-systems bridge in `bridges/restraint_ethics.md` and the
otherness-preserving recovery bridge in
`bridges/otherness_preserving_recovery.md` suggest a sharper future diagnostic
for non-ideal settings. When the error sector and logical label are
statistically coupled, raw \(I(\mathrm{logical};\mathrm{environment})\) can
conflate useful syndrome information with true logical leakage. The next
microscopic upgrade should therefore track excess leakage conditioned on the
syndrome/error sector, for example

$$
I(R_L;E_{\mathrm{env}}\mid S)\approx 0,
$$

where \(R_L\) purifies the logical input, \(E_{\mathrm{env}}\) is the
environment fragment, and \(S\) is the syndrome register. In the ideal DFS toy
model below the raw and conditional audits coincide, but hardware-scale
adaptive protocols should report the conditional quantity.

## 2. Model

Let the physical Hilbert space be

$$ \mathcal H = (\mathbb C^2)^{\otimes 2} $$

with computational basis

$$ \{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}. $$

We compare two logical superpositions:

$$ |\psi_U\rangle = \frac{|00\rangle + |11\rangle}{\sqrt 2}, $$

and

$$ |\psi_A\rangle = \frac{|01\rangle + |10\rangle}{\sqrt 2}. $$

The first is unaligned with collective phase noise. The second lies in the
standard two-qubit decoherence-free subspace for collective dephasing.

For a computational basis word \(x \in \{00,01,10,11\}\), define its collective
charge

$$ q(x) = \#0(x) - \#1(x), $$

so that

$$ q(00)=2,\quad q(01)=0,\quad q(10)=0,\quad q(11)=-2. $$

Let \(d_H(x,y)\) be the Hamming distance between basis words \(x\) and \(y\).
The simulation applies a dephasing channel parameterized by total coupling
strength \(\sigma \geq 0\) and structure fraction \(s \in [0,1]\). The matrix
elements transform as

$$
\mathcal E_{\sigma,s}(\rho)_{xy}
=
\exp\left[
-\frac12(\sigma s)^2(q(x)-q(y))^2
-\frac12(\sigma(1-s))^2 d_H(x,y)
\right]\rho_{xy}.
$$

The first exponential is collective dephasing. The second is independent
dephasing. Thus:

- \(s=1\): fully collective, structured phase noise.
- \(s=0\): fully independent, unstructured phase noise.
- \(0<s<1\): mixed structured and unstructured dephasing.

This channel is a Gaussian phase-average dephasing channel. It is completely
positive and trace-preserving because it is obtained by averaging unitary phase
rotations over centered Gaussian random variables.

## 3. Coherence Metric

We measure true branch coherence, not merely population in a code subspace.
For a superposition of two basis states \(|a\rangle, |b\rangle\), define

$$ C_{ab}(\rho)=2|\rho_{ab}|. $$

A perfect equal-amplitude coherent superposition has \(C_{ab}=1\). The fully
dephased incoherent mixture

$$
\frac12 |a\rangle\langle a|
+\frac12 |b\rangle\langle b|
$$

has \(C_{ab}=0\), even though its population in the two branches is one. This
distinction is essential. Population survival is not coherence survival.

For the unaligned and aligned states, write

$$ C_U(\sigma,s)=2|\mathcal E_{\sigma,s}(|\psi_U\rangle\langle\psi_U|)_{00,11}|, $$

and

$$ C_A(\sigma,s)=2|\mathcal E_{\sigma,s}(|\psi_A\rangle\langle\psi_A|)_{01,10}|. $$

## 4. Main Result

**Proposition 1 (Symmetry-adapted encoding protects coherence under correlated
dephasing).**
Under the channel \(\mathcal E_{\sigma,s}\),

$$ C_U(\sigma,s)=\exp\{-8\sigma^2s^2-\sigma^2(1-s)^2\}, $$

while

$$ C_A(\sigma,s)=\exp\{-\sigma^2(1-s)^2\}. $$

In particular, for fully collective dephasing \(s=1\),

$$ C_A(\sigma,1)=1 $$

for all \(\sigma\), while

$$ C_U(\sigma,1)=\exp\{-8\sigma^2\}. $$

Therefore the same correlated environmental coupling that destroys the
unadapted logical coherence leaves the symmetry-adapted DFS encoding invariant.

*Proof.* The unaligned coherence is the \((00,11)\) matrix element. Since
\(q(00)-q(11)=4\) and \(d_H(00,11)=2\), the dephasing factor is

$$
\exp\left[-\frac12(\sigma s)^2 4^2-\frac12(\sigma(1-s))^2 2\right]
= \exp\{-8\sigma^2s^2-\sigma^2(1-s)^2\}.
$$

The aligned coherence is the \((01,10)\) matrix element. Since
\(q(01)-q(10)=0\) and \(d_H(01,10)=2\), the collective factor is one and the
independent factor is

$$
\exp\left[-\frac12(\sigma(1-s))^2 2\right]
=\exp\{-\sigma^2(1-s)^2\}.
$$

The fully collective case \(s=1\) follows immediately. ■

## 5. Environment-Fragment Information

The first version of this note used a monotone proxy
\(s(1-e^{-\sigma^2})\) for structure in the environmental coupling. That proxy
had the right qualitative shape, but it did not compute a Shannon quantity. We
now add a minimal classical environment-fragment model coupled to the same
collective and independent coordinates that define the dephasing channel.

For a basis word \(x=x_1x_2\), define single-qubit signs

$$
z_k(x)=
\begin{cases}
+1, & x_k=0,\\
-1, & x_k=1.
\end{cases}
$$

Let

$$ \sigma_c=\sigma s,\qquad \sigma_i=\sigma(1-s). $$

The environment fragment is a Gaussian readout

$$
Y_c=\sigma_c q(x)+N_c,
$$

and

$$
Y_k=\sigma_i z_k(x)+N_k,\qquad k=1,2,
$$

where \(N_c,N_1,N_2\) are independent standard normal variables. The collective
fragment \(Y_c\) is the correlated-noise coordinate; the independent fragments
\(Y_1,Y_2\) are leakage coordinates for residual local noise.

Let \(Q\in\{-2,0,2\}\) be the collective charge of a uniformly sampled
computational-basis word, so that

$$
\Pr(Q=-2)=1/4,\quad \Pr(Q=0)=1/2,\quad \Pr(Q=2)=1/4.
$$

Define the syndrome information carried by the correlated fragment

$$
S_{\mathrm{MI}}(\sigma,s)=I(Q;Y_c).
$$

Explicitly,

$$
S_{\mathrm{MI}}
=
\sum_q p(q)\int p(y|q)
\log_2
\frac{p(y|q)}
{\sum_{q'}p(q')p(y|q')}
\,dy,
$$

with

$$ p(y|q)=\mathcal N(y;\sigma_c q,1). $$

Now let \(L_A\) be the aligned logical branch variable over
\(|01\rangle,|10\rangle\), and let \(L_U\) be the unaligned logical branch
variable over \(|00\rangle,|11\rangle\). Define logical-environment leakage as

$$
\Lambda_A(\sigma,s)=I(L_A;Y_c,Y_1,Y_2),
$$

and

$$
\Lambda_U(\sigma,s)=I(L_U;Y_c,Y_1,Y_2).
$$

For the aligned code, the two logical branches have the same collective charge:

$$ q(01)=q(10)=0. $$

Thus the structured collective fragment \(Y_c\) is exactly blind to the aligned
logical branch. Only the independent fragments distinguish \(|01\rangle\) from
\(|10\rangle\).

For two equiprobable unit-covariance Gaussian classes, the mutual information
depends only on half the Euclidean distance \(a\) between the class means:

$$
I_{\mathrm{bin}}(a)
=
1-
\mathbb E_{N\sim\mathcal N(0,1)}
\log_2\left(1+\exp[-2a(a+N)]\right).
$$

Therefore

$$
\Lambda_A(\sigma,s)=I_{\mathrm{bin}}(\sqrt 2\,\sigma_i),
$$

while

$$
\Lambda_U(\sigma,s)
=
I_{\mathrm{bin}}\left(\sqrt{4\sigma_c^2+2\sigma_i^2}\right).
$$

The noise-tailored score used in the simulation is

$$
P_{\mathrm{MI}}(\sigma,s)
=
S_{\mathrm{MI}}(\sigma,s)\,
C_A(\sigma,s)\,
\left(1-\Lambda_A(\sigma,s)\right).
$$

This score is zero when the correlated fragment carries no syndrome
information, is suppressed when DFS coherence is lost, and is suppressed when
the environment learns the adapted logical branch. It operationalizes the
target condition

$$ I(\mathrm{error};\mathrm{syndrome})>0 $$

while

$$ I(\mathrm{logical\ state};\mathrm{environment})\approx 0 $$

inside this toy environment-fragment model.

The same physical channel also induces a logical dephasing channel on either
two-branch encoding. Let \(X\in\{U,A\}\), and let
\(\eta_X(\sigma,s)=C_X(\sigma,s)\) be the off-diagonal multiplier for that
encoding. On the corresponding logical qubit,

$$
\mathcal N_X
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
=
\begin{pmatrix}
a & \eta_X b\\
\eta_X c & d
\end{pmatrix}.
$$

Equivalently,

$$
\mathcal N_X(\rho)=p_X\rho+(1-p_X)Z\rho Z,
$$

where

$$
p_X=\frac{1+\eta_X}{2}.
$$

For the maximally mixed logical input, the entanglement fidelity is

$$
F_e^X(\sigma,s)=p_X=\frac{1+C_X(\sigma,s)}{2},
$$

and the coherent information is

$$
I_c^X(\sigma,s)=1-H_2\left(\frac{1+C_X(\sigma,s)}{2}\right),
$$

where \(H_2\) is binary entropy in bits. This is the channel-native memory
quantity recorded in the simulation. It is stricter than branch population:
when \(C_X=0\), \(F_e^X=1/2\) and \(I_c^X=0\).

**Proposition 2 (Correlated fragments can carry syndrome without DFS logical
leakage).** In the fully collective limit \(s=1\),

$$
\Lambda_A(\sigma,1)=0
$$

for all \(\sigma\), while

$$
S_{\mathrm{MI}}(\sigma,1)>0
$$

for every \(\sigma>0\), and

$$
\Lambda_U(\sigma,1)>0
$$

for every \(\sigma>0\).

Thus the same environmental coordinate is informative about the collective
charge sector and about the unaligned logical branch, but blind to the aligned
DFS logical branch.

*Proof.* If \(s=1\), then \(\sigma_i=0\). The two aligned branches
\(|01\rangle\) and \(|10\rangle\) both have \(q=0\), so all three fragment
coordinates have the same conditional distribution for both values of \(L_A\).
Therefore \(\Lambda_A(\sigma,1)=0\). For \(\sigma>0\), the three charge classes
have distinct means \(-2\sigma,0,2\sigma\) in \(Y_c\), so
\(I(Q;Y_c)>0\). The unaligned branches \(|00\rangle\) and \(|11\rangle\) have
collective charges \(2\) and \(-2\), so their \(Y_c\) distributions also have
distinct means and \(\Lambda_U(\sigma,1)>0\). ■

**Proposition 3 (The DFS channel retains coherent information under collective
dephasing).** In the fully collective limit \(s=1\),

$$
F_e^A(\sigma,1)=1,\qquad I_c^A(\sigma,1)=1
$$

for all \(\sigma\), while

$$
F_e^U(\sigma,1)=\frac{1+e^{-8\sigma^2}}{2},
$$

and

$$
I_c^U(\sigma,1)
=
1-H_2\left(\frac{1+e^{-8\sigma^2}}{2}\right).
$$

Thus the adapted DFS channel retains a full logical qubit of coherent
information under arbitrarily strong collective dephasing in this ideal model,
whereas the unadapted channel approaches zero coherent information as
\(\sigma\to\infty\).

*Proof.* Proposition 1 gives \(C_A(\sigma,1)=1\) and
\(C_U(\sigma,1)=e^{-8\sigma^2}\). Substituting these coherence multipliers
into the logical dephasing-channel formulas above gives the stated
entanglement fidelities and coherent-information quantities. ■

## 6. Noise-Tailoring Interpretation

In the language of noise-tailored QEC, the model separates three regimes.

**No-coupling / no-syndrome regime.** When \(\sigma \approx 0\), coherence may
remain high, but the environment carries essentially no syndrome information:

$$ S_{\mathrm{MI}}(\sigma,s)\approx 0. $$

The system is coherent but operationally isolated. There is no syndrome
coordinate from which a decoder, calibration routine, or feedback protocol can
infer the relevant error sector.

**Residual local-noise / logical-leakage regime.** When \(s\approx 0\), the
dephasing is independent rather than correlated. The adapted and unadapted
coherences both decay as

$$ e^{-\sigma^2}. $$

The environment perturbs without supplying an exploitable common-mode
coordinate, and the independent fragments increasingly reveal the adapted
logical branch:

$$ \Lambda_A(\sigma,0)=I_{\mathrm{bin}}(\sqrt 2\,\sigma). $$

**Noise-tailored / symmetry-adapted regime.** When \(s>0\) and \(\sigma>0\),
the environment carries charge-sector information in a correlated coordinate.
The DFS encoding can preserve logical coherence while suppressing logical
leakage to the environment. The physical noise has not been eliminated; the
encoding has been matched to its symmetry.

In Shannon terms, useful persistence requires distinguishing information about
the error process from information about the logical state. The environment may
carry the former while remaining blind to the latter. This is the informational
core of decoherence-free subspaces and quantum error correction.

## 7. Simulation Protocol

The simulation is implemented at

`simulations/noise_as_signal/noise_as_signal_qiskit.py`.

Qiskit is used to construct the initial density matrices for \(|\psi_U\rangle\)
and \(|\psi_A\rangle\). The dephasing channel is then applied directly to the
density matrix using the analytic elementwise formula above. This avoids
sampling noise and makes the scan exactly reproducible.

The parameter grid is:

$$ \sigma \in [0,2.5] $$

with 151 points, and

$$ s \in [0,1] $$

with 101 points.

For each grid point, the script records:

- `structured_syndrome_mi_bits`: \(S_{\mathrm{MI}}=I(Q;Y_c)\);
- `aligned_logical_env_mi_bits`: \(\Lambda_A=I(L_A;Y_c,Y_1,Y_2)\);
- `unaligned_logical_env_mi_bits`: \(\Lambda_U=I(L_U;Y_c,Y_1,Y_2)\);
- `unaligned_coherence`: \(C_U(\sigma,s)\);
- `aligned_coherence`: \(C_A(\sigma,s)\);
- `alignment_gain`: \(C_A-C_U\);
- `aligned_entanglement_fidelity`: \(F_e^A=(1+C_A)/2\);
- `unaligned_entanglement_fidelity`: \(F_e^U=(1+C_U)/2\);
- `aligned_coherent_information_bits`: \(I_c^A\);
- `unaligned_coherent_information_bits`: \(I_c^U\);
- `noise_tailored_score`: \(P_{\mathrm{MI}}=S_{\mathrm{MI}}C_A(1-\Lambda_A)\).

Outputs:

- `simulations/noise_as_signal/outputs/noise_as_signal_scan.csv`
- `simulations/noise_as_signal/outputs/noise_as_signal_heatmap.png`
- `simulations/noise_as_signal/outputs/noise_as_signal_curves.png`

## 8. Results

At fixed coupling \(\sigma \approx 1.5\), the simulation gives:

| correlation fraction \(s\) | \(I(Q;Y_c)\) | \(\Lambda_A\) | \(C_A\) | \(F_e^A\) | \(I_c^A\) | \(P_{\mathrm{MI}}\) | regime |
|---:|---:|---:|---:|---:|---:|---:|---|
| 0.00 | 0.000 | 0.934 | 0.105 | 0.553 | 0.008 | 0.000 | no_syndrome |
| 0.25 | 0.179 | 0.797 | 0.282 | 0.641 | 0.058 | 0.010 | leakage_limited |
| 0.50 | 0.541 | 0.525 | 0.570 | 0.785 | 0.249 | 0.146 | transition |
| 0.75 | 0.892 | 0.178 | 0.869 | 0.934 | 0.651 | 0.637 | noise_tailored |
| 0.90 | 1.067 | 0.032 | 0.978 | 0.989 | 0.912 | 1.010 | noise_tailored |
| 1.00 | 1.164 | 0.000 | 1.000 | 1.000 | 1.000 | 1.164 | noise_tailored |

The global maximum over the scanned grid occurs at

$$ \sigma=2.5,\quad s=1.0,\quad P_{\mathrm{MI}}=1.4651. $$

This is expected: in the ideal fully collective pure-dephasing model, the DFS
is exact, so stronger collective coupling supplies more charge-sector syndrome
information without damaging the adapted logical coherence or leaking the
adapted logical branch. For partially correlated noise, the score is limited by
the competing growth of independent dephasing and adapted logical leakage.

## 9. Relation to Noise-Adapted QEC and Feedback

This note does not simulate an active feedback protocol. It establishes the
static noise symmetry that such a protocol would exploit. In standard
engineering language, an active noise-adapted protocol would add:

1. noise characterization or spectroscopy estimating the correlated component
   of the channel;
2. code or gauge selection that maps the logical degrees of freedom into the
   corresponding DFS/noiseless subsystem when available;
3. syndrome extraction or symmetry verification for residual detectable errors;
4. recovery, mitigation, or adaptive recalibration for the residual
   undetectable error components.

The current result is the precondition for that program: if the environmental
noise has stable collective structure, then a symmetry-adapted encoding can
preserve coherence by matching that structure rather than treating the full
coupling as an arbitrary local error channel.

## 10. Relation to Recent Literature

The closest current terminology is noise-tailored or noise-adapted error
correction. Recent work concatenating DFS and QECC constructions explicitly
treats DFS encodings as passive protection against correlated errors and QECCs
as active protection against independent residual errors. Bias-tailored
stabilizer and Floquet-code work similarly designs checks and decoders around
structured Pauli noise, especially dephasing-biased channels. Subspace noise
tailoring and symmetry-verification methods separate detectable from
undetectable error components, then apply mitigation or cancellation only to
the residual component that the subspace checks cannot reject.

The distinctive contribution of this note is narrower: it isolates the
two-qubit DFS limit and writes the separation as a pair of mutual-information
conditions. The correlated environment fragment carries charge-sector
information, while the symmetry-adapted logical branch remains private. This is
the smallest channel-level example of the general noise-tailoring principle.

## 11. Limitations

1. The noise model is pure dephasing. Amplitude damping, leakage, crosstalk,
   non-Markovian drift, and measurement backaction are not included.

2. The environment-fragment model is classical and Gaussian. It now computes
   explicit Shannon mutual informations, and the induced logical dephasing
   channel has explicit entanglement-fidelity and coherent-information
   diagnostics. This is still short of a full microscopic Stinespring
   environment-state model or recoverability bound for an active decoder.

3. Fully collective dephasing is an ideal symmetry. Real devices have residual
   independent noise, so the \(s=1\) monotonic behavior should be read as the
   symmetry limit, not a hardware prediction.

4. The model is two-qubit. Scaling requires characterizing the structure of
   correlated noise in larger devices and the cost of estimating that structure.

5. The regime labels in the CSV are heuristic diagnostic labels. The analytic
   claims are the coherence formulas and the mutual-information separation in
   Proposition 2.

## 12. Conclusion

This minimal model gives a precise instance of noise-tailored encoding. The
same collective dephasing channel that decoheres an unadapted logical
superposition preserves a symmetry-adapted DFS superposition. In the associated
environment-fragment model, the correlated fragment can reveal charge-sector
information while remaining blind to the adapted logical branch. The technical
claim is therefore not that noise is beneficial per se, but that correlated or
biased noise can define an exploitable error geometry when the code, decoder,
or mitigation protocol is matched to it.

## References

Breuer, H.P. and Petruccione, F. (2007). *The Theory of Open Quantum Systems.*
Oxford University Press.

Duan, L.M. and Guo, G.C. (1997). Preserving coherence in quantum computation by
pairing quantum bits. *Physical Review Letters* 79, 1953-1956.

Lidar, D.A., Chuang, I.L. and Whaley, K.B. (1998). Decoherence-free subspaces
for quantum computation. *Physical Review Letters* 81, 2594-2597.

Dash, N.R., Dutta, S., Srikanth, R. and Banerjee, S. (2024). Concatenating
quantum error-correcting codes with decoherence-free subspaces and vice versa.
*Physical Review A* 109, 062411.

Setiawan, F. and McLauchlan, C. (2025). Tailoring dynamical codes for biased
noise: the X3Z3 Floquet code. *npj Quantum Information* 11, 149.

Papič, M. et al. (2026). Near-term fermionic simulation with subspace noise
tailored quantum error mitigation. *npj Quantum Information* 12, 72.

Chen, E.H. et al. (2025/2026). Disambiguating Pauli noise in quantum
computers. arXiv:2505.22629.

Wang, Y.-X., Bringewatt, J., Seif, A., Brady, A.J., Oh, C. and Gorshkov, A.V.
(2024). Exponential entanglement advantage in sensing correlated noise.
arXiv:2410.05878.

Nielsen, M.A. and Chuang, I.L. (2010). *Quantum Computation and Quantum
Information.* Cambridge University Press.

Shannon, C.E. (1948). A mathematical theory of communication. *Bell System
Technical Journal* 27, 379-423, 623-656.

Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the
classical. *Reviews of Modern Physics* 75, 715-775.
