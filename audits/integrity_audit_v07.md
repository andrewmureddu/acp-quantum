# ACP v0.7 Integrity Audit

**Date:** April 10, 2026 (Session 11)
**Scope:** Full cross-reference, numbering, notation, and logic audit of `acp_physics_paper_v07.md`

---

## 1. NUMBERING GAPS (Missing formal objects)

The following numbered objects are missing from the sequence, creating gaps that a reviewer will immediately notice:

| Expected | Status | Notes |
|----------|--------|-------|
| Definition 2.4 | **Missing** | Remark 2.4 exists, but no Definition 2.4. Jump from Def 2.3 → Def 2.5 |
| Definition 2.6 | **Missing** | Remark 2.6 exists, but no Def 2.6. Jump from Def 2.5 → Def 2.7 |
| Lemma 4.3–4.6 | **Numbering clash** | Theorem 4.3 and Corollaries 4.4–4.5 exist, but there is no Lemma 4.3. The jump from Lemma 4.2 → Theorem 4.3 is fine (mixed object types share a counter). But then Def 4.7 skips 4.6 (which is Remark 4.6). The sequence is actually consistent if all objects share one counter per section. |
| **Lemma 4.15** | **Missing** | Jump from Lemma 4.14 directly to Lemma 4.16. No Lemma 4.15 exists. |
| **Theorem 4.18** | **Missing** | Jump from Lemma 4.17 directly to Theorem 4.19. No Theorem/Definition 4.18 exists. |
| **Corollary 4.21** | **Missing** | Remark 4.21 exists. Jump from Corollary 4.20 → Corollary 4.22 (skipping 4.21 because it's a Remark). This is actually fine if Remarks share the counter. |

**Assessment:** The numbering appears to use a single sequential counter per section (Definitions, Lemmas, Theorems, Corollaries, and Remarks all increment the same counter). Under this convention, the sequence is mostly consistent. However:

- **Lemma 4.15 is genuinely missing.** 4.14 → 4.16 with no 4.15 in between.
- **4.18 is genuinely missing.** 4.17 → 4.19 with no 4.18 in between.

**Recommendation:** Either (a) renumber 4.16 → 4.15, 4.17 → 4.16, 4.19 → 4.17, etc. (cascading renumber), or (b) add placeholder remarks/notes at 4.15 and 4.18 to fill gaps. Option (a) is cleaner but requires updating all downstream references in the paper AND in appendices. Option (b) is ugly. Best approach: renumber the entire Section 4.4 formal object sequence to be gapless. This is a mechanical task.

---

## 2. CROSS-REFERENCE ERRORS

### 2a. Introduction claims "five steps" but lists six

Line 39: "We proceed in five steps" → then lists (i) through (vi).

**Fix:** Change "five steps" to "six steps" or restructure.

### 2b. Prediction 7: "Beyond T" should be "Beyond T*"

Line 239: "Beyond T, the system can no longer self-correct."

Should read: "Beyond T*, the system can no longer self-correct."

### 2c. ε(t) vs ε*(t) inconsistency

- Corollary 4.23 (line 213) defines ε*(t) with the asterisk
- Section 4.4.6 / Ostrom paragraph (line 231) uses ε(t) without asterisk
- Notation table (line 594) lists ε(t) without asterisk
- Prediction 7 in Section 6.7 (line 325) uses ε*(T) with asterisk

The asterisk is needed to distinguish the critical threshold from the small parameter ε in Definition 2.5 and the boundary parameter ε in Definition 2.8/2.9. Should be ε*(t) everywhere when referring to the critical perturbation threshold.

### 2d. Section 4.4.5 reference: "See Section 4.4.5" for coherence crises

Remark 4.12 (line 159) says "See Section 4.4.5." But Section 4.4.5 is titled "Corollaries" and does not contain a substantive treatment of coherence crises. The anti-crystallization mechanisms are mentioned only in passing. This forward reference is somewhat misleading.

---

## 3. NOTATION ISSUES

### 3a. σ overloading

- σ: Ω → M is the coarse-graining function (Definition 2.1, used throughout)
- σ is the entropy production rate dᵢS/dt (Prigogine reduction, Section 5.1, notation table line 612)

These appear in different contexts (core framework vs. Prigogine-specific), but a careful reader will flag this. The Prigogine usage could use σ_P or σ_prod to disambiguate.

### 3b. T overloading

- T is the time-evolution operator (Definition 2.1)
- T is temperature (Axiom 1, line 85: "temperature T")
- T* is the reformation timescale (Prediction 7)

The time-evolution vs. temperature clash is the most serious. In Axiom 1 the free energy formula F = E − TS uses T for temperature in the same paper where T is defined as the dynamics operator. Could disambiguate with 𝒯 for the dynamics or T_env for temperature.

### 3c. ε overloading

- ε is a small parameter in Definition 2.5 (future-bearing dynamics condition)
- ε, η are small positive parameters defining boundary regions (Definitions 2.8, 2.9)
- ε*(t) is the critical perturbation threshold (Corollary 4.23)
- ε is the perturbation magnitude in Theorem 4.19

These are distinguishable from context, but the asterisk convention should be consistent.

---

## 4. UNCITED REFERENCES

The following references appear ONLY in the References section and are never cited in the body text of v0.7. They may be cited in the appendices (which are separate documents), but in the main paper they are orphaned:

- Bertschinger & Natschläger (2004)
- DeLong, DeLong & Clarke-Pearson (1988)
- Glansdorff & Prigogine (1971)
- Koch-Janusz & Ringel (2018)
- Kubo (1966)
- Langton (1990)
- Lewontin (1978)
- Onsager (1931)
- Penrose (1996)
- Pinsker (1964)
- Prigogine (1945)
- Prigogine (1967)
- Prigogine & Wiame (1946)
- Prigogine & Stengers (1984)
- Schrödinger (1944)
- Stein, Zanasi, Piedeleu & Samuelson (2025)
- Tsybakov (2009)

**Note:** Some of these (e.g., Langton, Bertschinger, Glansdorff) are likely cited in the formal appendices. If the paper is intended to be read with its appendices as a single unit, this is fine. If the main paper is meant to stand alone, these should either be cited in the text or moved to an appendix-specific reference list.

Also: the Price equation is mentioned by name in Lemma 4.14's proof sketch (line 169) but Price is not in the References. Either add the reference or remove the citation.

---

## 5. LOGIC / STRUCTURAL ISSUES

### 5a. Lemma 4.2 open problem partially undermines the main theorem

The ⚠ after Lemma 4.2 (line 115) notes that the claim "holds in the limit of strong coarse-graining (high degeneracy) but needs qualification for weakly coarse-grained descriptions." This is honest and good. But the main theorem (Theorem 4.3) cites Lemma 4.2 directly. A reviewer will ask: does the qualification on Lemma 4.2 propagate to Theorem 4.3?

**Recommendation:** Add a brief remark after Theorem 4.3's proof acknowledging that the crystallization-boundary case inherits the qualification from Lemma 4.2, and note that the dissolution case (via Lemma 4.1) is unconditional. This makes the proof's strength explicit rather than leaving it ambiguous.

### 5b. Proof of Theorem 4.19 step (a): logical tightness

The proof says: "By Lemma 4.13, each active self-reinforcing mechanism reduces conditional entropy. By (b), the number of such mechanisms is non-decreasing. By Lemma 4.16, their compound effect is superadditive when they interact. Therefore the total reduction in conditional entropy is non-decreasing in t."

This is correct but slightly imprecise. What's actually shown is that the *rate* of conditional entropy reduction is non-decreasing (because k is non-decreasing and compounding is superadditive). Then: "Since conditional entropy is bounded below by zero, the sequence H(m(t+Δt) | m(t)) is monotonically non-increasing and bounded below—hence convergent."

The convergence claim follows from the monotone convergence theorem, which is correct. But the superadditivity claim requires that the mechanisms *interact* (are non-independent). The proof should note that independent mechanisms merely add (not compound superadditively), and that the result holds a fortiori in that case (additivity ≥ individual contributions).

### 5c. Corollary 4.22 is labeled "Restating Remark 4.6"

This is unusual. A corollary should follow from a theorem, not restate a prior remark. The content is correct—it IS a corollary of Theorem 4.19 combined with Axiom 1—but the label "(Restating Remark 4.6)" makes it look like it's merely repeating earlier text rather than deriving a new consequence. Drop the "Restating" label.

---

## 6. FORMATTING / PRESENTATION ISSUES

### 6a. Section 7 headers with "— RESOLVED"

Sections 7.1, 7.2, 7.4, 7.9 have "— RESOLVED" or "— SUBSTANTIALLY RESOLVED" or "— PARTIALLY RESOLVED" in their headers. This is useful for internal tracking but inappropriate for a submission-ready paper. Options:
- (a) Move resolved items to a "Resolved in this paper" subsection
- (b) Present them as accomplishments rather than crossed-off todo items
- (c) Restructure Section 7 into "Remaining open problems" (genuinely open) and remove resolved items entirely, noting their resolution elsewhere

### 6b. v0.7 version notes at top

Lines 13–23 are version tracking notes. Remove for submission.

### 6c. "⚠" markers

These are valuable for internal tracking. For submission, either (a) replace with prose ("We note as an open problem that...") or (b) adopt a formal convention explained in the introduction.

### 6d. Subsection numbering style inconsistency

Sections 4.4.1–4.4.7 use **bold text** headers rather than the ### or ## markdown convention used elsewhere. This creates visual inconsistency.

---

## 7. SUMMARY OF REQUIRED FIXES

### Critical (would cause reviewer rejection or confusion):
1. **Renumber Section 4.4 formal objects** to eliminate gaps at 4.15 and 4.18
2. **Fix "five steps" → "six steps"** in Introduction (line 39)
3. **Fix "Beyond T" → "Beyond T*"** in Prediction 7 (line 239)
4. **Add Price equation reference** or remove the citation (line 169)
5. **Standardize ε*(t) notation** for critical perturbation threshold throughout

### Important (reviewer will notice, reduces confidence):
6. **Address Lemma 4.2 qualification propagation** to Theorem 4.3
7. **Disambiguate σ** (coarse-graining vs. entropy production)
8. **Disambiguate T** (dynamics operator vs. temperature)
9. **Resolve or document uncited references** 
10. **Drop "Restating Remark 4.6"** from Corollary 4.22

### Submission-readiness (not errors but presentation):
11. Restructure Section 7 (remove RESOLVED tags from headers)
12. Remove version tracking notes (lines 13–23)
13. Replace ⚠ with prose conventions
14. Normalize subsection header formatting
