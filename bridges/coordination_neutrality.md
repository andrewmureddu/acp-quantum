# Appendix A.20 Addendum: Coordination-Neutrality and the Log-Lift

*Working draft v01. Minimal formalization emerging from Session 18 informal discussion. For integration into `restraint_power_v01.md` or as standalone appendix.*

---

## A.20.10bis. Setup and motivation

A two-slot operator $B : D \to \mathbb{R}^*$ on a swap-stable domain $D \subseteq X \times X$ represents a coordination act between two subsystems. A natural algebraic question, implicit in the restraint-power framework (§A.20.5), is what symmetry such an operator must possess to represent a genuinely symmetric coordination protocol — one that does not privilege either side of the handshake.

This addendum isolates one such symmetry (coordination-neutrality), establishes basic consequences for the logarithmic lift of $B$, and identifies a concrete open problem: whether the symmetry is preserved under tree-compositional iteration, as would be required to build multi-party coordination from pairwise primitives.

**Relationship to prior material.** The content is orthogonal to the restraint-power theorem (A.20.14), which concerns N-body dynamics on a mechanism graph. The present addendum concerns the algebraic structure of the dyadic coordination operator itself, extending the Schur-propagation framework of §A.9 by asking which dyadic symmetries survive the multi-scale iteration of §A.18.

---

## A.20.10bis.1 Coordination-neutrality

**Definition A.20.33 (Coordination-neutrality).** Let $D \subseteq X \times X$ be open and swap-stable (i.e. $(x, y) \in D \Rightarrow (y, x) \in D$), and let $B : D \to \mathbb{R}^*$. The operator $B$ is *coordination-neutral* (CN) if

$$ B(y, x) = \frac{1}{B(x, y)} \qquad \text{for all } (x, y) \in D. $$

**Example A.20.34 (Bridge family).** For $\alpha, \lambda > 0$, the family
$$ B_{\alpha, \lambda}(x, y) = \frac{e^{\alpha x} - \lambda \ln y}{e^{\alpha y} - \lambda \ln x} $$
is coordination-neutral on its regular domain (where numerator, denominator, and both $\ln$ arguments are defined). CN is immediate: swapping $(x, y) \mapsto (y, x)$ exchanges numerator and denominator.

**Example A.20.35 (Ratio).** $B(x, y) = x/y$ on $(\mathbb{R}^*)^2$ is coordination-neutral.

**Non-example A.20.36 (EML).** $B_{\mathrm{EML}}(x, y) = e^x - \ln y$ is *not* coordination-neutral. Explicitly $B_{\mathrm{EML}}(x, x) = e^x - \ln x \ne \pm 1$ generically, which already violates the diagonal consequence of CN (Proposition A.20.37(c) below).

---

## A.20.10bis.2 Properties of the log-lift

**Proposition A.20.37 (Log-lift of a coordination-neutral operator).** Let $B : D \to \mathbb{R}^*$ be coordination-neutral, and define the *log-lift* $L : D \to \mathbb{R}$ by $L(x, y) = \log |B(x, y)|$. Then:

**(a)** $L$ is well-defined and smooth wherever $B$ is smooth and non-vanishing.

**(b)** $L$ is swap-antisymmetric: $L(y, x) = -L(x, y)$ on $D$.

**(c)** On $\Delta := \{(x, x) \in D\}$, $B$ takes values in $\{+1, -1\}$, and $L \equiv 0$.

**(d)** Every smooth $G : D \to \mathbb{R}$ decomposes uniquely as $G = G_{\mathrm{sym}} + G_{\mathrm{skew}}$ with $G_{\mathrm{sym}}(y, x) = G_{\mathrm{sym}}(x, y)$ and $G_{\mathrm{skew}}(y, x) = -G_{\mathrm{skew}}(x, y)$. For a coordination-neutral $B$, the log-lift satisfies $L_{\mathrm{sym}} \equiv 0$, i.e. $L$ lies entirely in the swap-odd subspace.

*Proof.*
(a) Follows from smoothness of $\log : \mathbb{R}^* \to \mathbb{R}$ composed with smooth $|B|$ on its non-vanishing locus.

(b) By CN, $|B(y, x)| = |1/B(x, y)| = 1/|B(x, y)|$. Taking $\log$: $L(y, x) = -L(x, y)$.

(c) Evaluating CN at $y = x$: $B(x, x) = 1/B(x, x)$, so $B(x, x)^2 = 1$, so $B(x, x) \in \{+1, -1\}$. Hence $|B(x, x)| = 1$ and $L(x, x) = 0$.

(d) The sym/skew decomposition $G_{\mathrm{sym}}(x, y) = \tfrac{1}{2}[G(x, y) + G(y, x)]$, $G_{\mathrm{skew}}(x, y) = \tfrac{1}{2}[G(x, y) - G(y, x)]$ is standard. Applied to $L$, part (b) gives $L_{\mathrm{sym}} = \tfrac{1}{2}[L(x, y) + L(y, x)] = 0$. $\blacksquare$

**Remark A.20.38 (Sign branch).** Proposition A.20.37(c) permits $B(x, x) = -1$, but for a CN operator continuous on a connected swap-stable domain containing $\Delta$, $B(x, x) = +1$ is forced (the continuous map $x \mapsto B(x, x)$ into the discrete set $\{+1, -1\}$ is constant on connected components, and most natural examples — including the bridge family on its positive subdomain — place $\Delta$ in the $+1$ component). The $-1$ branch is a non-generic case that may be excluded by a continuity assumption.

**Remark A.20.39 (On EML).** The operator $B_{\mathrm{EML}}(x, y) = e^x - \ln y$ used as a running example in recent informal work fails CN by Example A.20.36. Empirical observations about $B_{\mathrm{EML}}$'s iterated-value closure therefore address a different property — closure under tree-composition from a fixed seed — and do not bear on the CN framework developed here. The bridge family (Example A.20.34) is the smallest natural CN extension preserving the exp–log structure and is the appropriate numerical testbed for CN-based claims.

---

## A.20.10bis.3 Compositional preservation: an open problem

**OP-CN-1 (Compositional preservation of coordination-neutrality).** Let $\{B_i\}$ be a collection of coordination-neutral operators on a common swap-stable domain. Let $T$ be a two-slot operator constructed by tree-composition from the $\{B_i\}$ — a finite binary tree with each internal node labeled by some $B_j$, leaves labeled by input variables, evaluated recursively. Under what algebraic conditions on the $\{B_i\}$ is $T$ coordination-neutral (under a natural multi-argument analog of swap)?

**Preliminary analysis: depth-2 case.** Consider the simplest non-trivial composition — a depth-2 tree with root $B_1$, both children $B_2$, on four leaves:
$$ T(a, b, c, d) = B_1\bigl(B_2(a, b),\, B_2(c, d)\bigr). $$

The natural analog of swap for a 4-argument function is argument-reversal $T(a, b, c, d) \mapsto T(d, c, b, a)$. Using CN of $B_2$:
$$ T(d, c, b, a) = B_1\bigl(B_2(d, c),\, B_2(b, a)\bigr) = B_1\bigl(1/B_2(c, d),\, 1/B_2(a, b)\bigr). $$

Setting $u = B_2(a, b)$, $v = B_2(c, d)$:
$$ T(d, c, b, a) = B_1(1/v,\, 1/u). $$

For $T$ to satisfy reversal-CN, i.e. $T(d, c, b, a) = 1/T(a, b, c, d)$, we require
$$ B_1(1/v,\, 1/u) = 1/B_1(u, v) = B_1(v, u), $$
where the last equality uses CN of $B_1$. Thus the preservation condition is
$$ B_1(1/v,\, 1/u) = B_1(v, u) \qquad \text{(joint-inversion invariance).} \tag{$\ast$} $$

Condition $(\ast)$ is logically independent of CN.

**Partial result (negative: bridge family fails $(\ast)$).** For the bridge $B_{\alpha, \lambda}$, direct computation gives
$$ B_{\alpha, \lambda}(1/v,\, 1/u) = \frac{e^{\alpha/v} + \lambda \ln u}{e^{\alpha/u} + \lambda \ln v}, \qquad B_{\alpha, \lambda}(v, u) = \frac{e^{\alpha v} - \lambda \ln u}{e^{\alpha u} - \lambda \ln v}. $$
These expressions differ in every entry (both in functional form — $e^{\alpha/v}$ vs $e^{\alpha v}$ — and in sign structure). Equality holds at most on a measure-zero subset. Therefore $(\ast)$ fails for the bridge family, and depth-2 tree compositions of $B_{\alpha, \lambda}$ are not coordination-neutral under argument-reversal.

**The open problem, stated precisely.**

**OP-CN-1(a).** Characterize the class $\mathcal{C}$ of operators $B : D \to \mathbb{R}^*$ satisfying both CN and $(\ast)$. Is $\mathcal{C}$ non-empty beyond trivial examples (identity, constant $\pm 1$)?

**OP-CN-1(b).** Determine the analog of $(\ast)$ at depths $n \geq 3$. Is there an infinite tower of independent conditions — one per depth — or does closure at depth 2 suffice? (Conjecturally the former, but we have not verified.)

**OP-CN-1(c).** If $\mathcal{C}$ is small or empty, identify the alternative symmetry (if any) that tree-compositions of CN operators do naturally satisfy. Preliminary calculation for the ratio operator $B(x, y) = x/y$ suggests the composition $T(a, b, c, d) = ad/(bc)$ is *reversal-invariant* ($T(d, c, b, a) = T(a, b, c, d)$) rather than reversal-CN, indicating that composition may convert CN into a different structural property.

---

## A.20.10bis.4 Speculative connections (not part of formal content)

*The following conjectures motivated this addendum but are not established here. They are flagged as working-hypothesis only.*

**C1 (Two-mode restraint-power, speculative).** A strengthening of the restraint-power theorem in which the concentrated element $\arg\max_i \gamma_i$ is obligated to initiate *both* crystallizing and releasing transfers. If CN is the operator-level signature of "handshake-symmetric" coordination, operators failing CN may correspond to single-mode dynamics, while CN operators are candidates for genuine two-mode dynamics. The formal link between CN and the restraint-power dynamics is not established.

**C2 (Topological charge via complexification, speculative).** For CN operators extended to $\mathbb{C}^*$-valued domains (not treated here), the winding of the complexified log-lift $\log B$ around zero and pole loci would give integer-valued topological invariants. On $\mathbb{R}^*$ only a $\mathbb{Z}/2$ crossing-count is available. A full $\mathbb{Z}$-valued theory requires complexification and is outside the scope of this addendum.

**C3 (Connection to canonical commutation relations, speculative).** The CN structure shares formal features with the conjugate-variable structure of the Heisenberg algebra (cf. A.20.27 and OP-RP-5). Whether CN is the classical shadow of the Heisenberg commutation structure, or a distinct algebraic property, is open.

---

## Flagging note

*This addendum emerged from a working session that also produced exploratory numerical simulations of non-CN operators (specifically $B_{\mathrm{EML}}$, $B_{\mathrm{POW}}(x, y) = x^2 - y$, and variants). Those simulations established empirical patterns: discrete closure of $B_{\mathrm{EML}}$ at shallow tree-depth; an inverse-magnitude fragility law $\sigma_{\mathrm{half}} \approx \varepsilon/|v|$ for operators with unbounded $\Psi$; failure of depth-alternation between sharp and smooth operators to preserve arithmetic-shadow structure.*

*These simulations tested $B_{\mathrm{EML}}$ and other non-CN operators and therefore do not bear directly on the formal claims here. The "arithmetic shadow" and "fragility law" observations apply to EML's iterative structure specifically, not to any property of coordination-neutrality. Claims connecting the numerics to CN require a separate numerical study of the bridge family $B_{\alpha, \lambda}$ and are not asserted.*

*Formal content of this addendum is limited to:*

- *Definition A.20.33 of coordination-neutrality.*
- *Proposition A.20.37 on the log-lift (four small results, each with a one-line proof).*
- *Example/non-example catalog (A.20.34–36).*
- *Two remarks (A.20.38–39).*
- *Open problem OP-CN-1 in three parts, with a preliminary negative result on the bridge family.*
- *Three speculative conjectures (C1–C3), explicitly flagged as conjecture.*

*Nothing else in this document is claimed as a theorem.*

---

*Drafted by Claude, Session 18. Version 01.*
