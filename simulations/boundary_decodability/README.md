# Boundary Decodability: Page Turnover and the Remnant Capacity Bound

Numerical verification for `bridges/boundary_decodability.md`, the Stage 5 rung
of the quantum-gravity derivation ladder.

Everything here is computed from **exact reduced density matrices and exact von
Neumann entropies** — no proxy scores. Pure standard library.

## Model

A reference register `X_R` (1 qubit) purifies the protected interior
information of a collapsing region `H` (9 qubits). The global state on
`X_R (x) H` is Haar-random, which is the standard Page / Hayden-Preskill
setting: it models a maximally scrambling interior, the most favourable case
for information return.

Evaporation releases hole qubits to the boundary record one at a time. A
completion that permanently hides `r` qubits releases only `9 - r` of them.

Reduced density matrices are computed on whichever side of the purification is
cheaper. Hermitian eigenvalues come from a cyclic Jacobi rotation applied to
the real symmetric embedding `[[A, -B], [B, A]]` of `H = A + iB`, which carries
every eigenvalue of `H` exactly twice.

## Run

```bash
python3 simulations/boundary_decodability/boundary_decodability.py
```

Runtime roughly 14 seconds.

## Outputs

- `outputs/page_curve_timeseries.csv`
- `outputs/remnant_bound_scan.csv`

## Predictions under test

1. **Complementarity is exact** (Lemma 5): `I(R;rad) + I(R;hid) = 2 S(R)`.
2. **Page turnover is forced** (Corollary F1): `S(rad)` rises then falls,
   peaking at half the total and returning to `S(R)`.
3. **Remnant capacity bound** (Corollary F2b): decodability holds exactly while
   `log dim H_hidden <= log dim H_boundary - S(X_R)`, i.e. `r <= 4` here.

## Results

### Complementarity and the Page curve

| released | S(rad) | S(hid) | I(R;rad) | I(R;hid) | sum | 2S(R) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.0000 | 0.9984 | 0.0000 | 1.9968 | 1.9968 | 1.9968 |
| 1 | 0.9974 | 1.9906 | 0.0052 | 1.9916 | 1.9968 | 1.9968 |
| 2 | 1.9876 | 2.9541 | 0.0319 | 1.9649 | 1.9968 | 1.9968 |
| 3 | 2.9519 | 3.8133 | 0.1370 | 1.8598 | 1.9968 | 1.9968 |
| 4 | 3.8095 | 4.2706 | 0.5373 | 1.4595 | 1.9968 | 1.9968 |
| 5 | **4.2742** | 3.8183 | 1.4543 | 0.5425 | 1.9968 | 1.9968 |
| 6 | 3.8267 | 2.9618 | 1.8633 | 0.1335 | 1.9968 | 1.9968 |
| 7 | 2.9578 | 1.9915 | 1.9647 | 0.0321 | 1.9968 | 1.9968 |
| 8 | 1.9912 | 0.9986 | 1.9910 | 0.0059 | 1.9968 | 1.9968 |
| 9 | 0.9984 | 0.0000 | 1.9968 | 0.0000 | 1.9968 | 1.9968 |

- **Lemma 5 holds to `2e-08` bits.** The two mutual informations are computed
  independently — `S(R u rad)` directly rather than via purity — so the
  constant sum column is a real check, and it validates the code.
- **Page turnover confirmed**: peak `4.2742` bits at 5 released qubits, exactly
  half of the 10-qubit total; final value `0.9984` equals `S(R) = 0.9984` to
  four decimals, as Corollary F1(2) predicts.
- **Full budget returns**: `I(R;rad)` reaches `1.9968 = 2S(R)`.

### Validation against Page's analytic formula

Measured `S(rad)` against `<S_A> ~ ln d_A - d_A/(2 d_B)`:

| released | Page (bits) | measured | diff |
|---:|---:|---:|---:|
| 1 | 0.9972 | 0.9974 | +0.0002 |
| 2 | 1.9887 | 1.9876 | −0.0011 |
| 3 | 2.9549 | 2.9519 | −0.0030 |
| 4 | 3.8197 | 3.8095 | −0.0102 |
| 5 | 4.2787 | 4.2742 | −0.0045 |
| 6 | 3.8197 | 3.8267 | +0.0070 |
| 7 | 2.9549 | 2.9578 | +0.0029 |
| 8 | 1.9887 | 1.9912 | +0.0025 |
| 9 | 0.9972 | 0.9984 | +0.0012 |

Worst deviation 0.010 bits, typical 0.003.

### Remnant capacity threshold

Predicted admissible while `r <= (9 - r) - S(R)`, i.e. `r <= 4`.

| hidden r | released | predicted | I(R;rad) | decodable fraction |
|---:|---:|---|---:|---:|
| 0 | 9 | admissible | 1.9968 | 1.0000 |
| 1 | 8 | admissible | 1.9910 | 0.9971 |
| 2 | 7 | admissible | 1.9647 | 0.9839 |
| 3 | 6 | admissible | 1.8633 | 0.9331 |
| 4 | 5 | admissible | 1.4543 | 0.7283 |
| 5 | 4 | inadmissible | 0.5373 | 0.2691 |
| 6 | 3 | inadmissible | 0.1370 | 0.0686 |
| 7 | 2 | inadmissible | 0.0319 | 0.0160 |
| 8 | 1 | inadmissible | 0.0052 | 0.0026 |
| 9 | 0 | inadmissible | 0.0000 | 0.0000 |

The decodable fraction crosses one half exactly between `r = 4` (0.728) and
`r = 5` (0.269), the predicted threshold. The crossover is smooth rather than a
step because of finite-size Page corrections; the symmetry of the two values
about the threshold is Lemma 5 again.

## Caveats

- The Haar-random global state models a maximally scrambling interior. It is
  typical, not optimal: a completion that deliberately swaps the protected
  qubit into the record first achieves decodability with an arbitrarily small
  boundary. This is why Corollary F2(b) is stated as conditional on scrambling
  rather than as universally necessary.
- 1 reference qubit and 9 hole qubits is small enough that finite-size Page
  corrections are visible (they are what smooths the threshold). This is a
  feature for validation — the corrections match Page's formula — but the
  thresholds are sharp only asymptotically.
- Six Haar samples. The complementarity identity is exact per sample, so it is
  unaffected; the entropies are sample-averaged.
