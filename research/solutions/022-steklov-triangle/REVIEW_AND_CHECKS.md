# Review and checks: problem 022, triangle case

**Reviewers:** the AI system that wrote the proof (self-review, sections A, B and E), and a separate AI referee pass in a fresh context, run by another agent of the same Claude Code session (section C). Under this repository's convention both are *originating* checks, not an independent audit. **No human review.** Every item is marked OK, FIXED or OPEN.

## A. Lemma-by-lemma audit (self-review)

| # | item | check performed | status |
|---|---|---|---|
| A1 | Definition of σ₁ | Weak form with H¹ trial functions, mean-zero on ∂Ω — identical to (1.2) of arXiv:2603.25116 and the AIM statement. | OK |
| A2 | Lemma 1, surjectivity | T = A E + b, polar decomposition A = QP, P = λ exp(S). Reflections allowed: σ₁·Per is invariant under all isometries and dilations. | OK |
| A3 | Lemma 1, S = 0 iff equilateral | Affine map between equilateral triangles maps Steiner circum-ellipse (circle) to circle ⇒ similarity; SPD similarity of det 1 is I. | OK |
| A4 | Lemma 2(a) abstract bound | Re-derived: v ∈ S with M(v,u_{h,i}) = 0 (i<k) exists by dimension count; ‖P_hv‖²_N ≤ λ_{h,k}⁻¹‖P_hv‖²_M uses that discrete eigenvectors are M- and N-orthogonal to Ker N on V_h; C-S + Pythagoras. Direction: gives a LOWER bound on λ_k. | OK |
| A5 | Lemma 2(b) spectra | (M,N) on V: harmonic + weak Neumann ⇒ either m(f)=0 (Steklov) or λ = τPer. On V_h: constant vector 1 = Σφ_i, K·1 = 0, N·1 = m; nonzero (K,N)-eigenvectors are N-orthogonal to 1. With τ → large, λ₃ = σ₃ and λ_{h,3} = third nonzero (K,N) eigenvalue. | OK |
| A6 | Lemma 2(c) P_h = Π_h | ∇v_h constant per element; Π_h preserves every edge mean; also m(u − Π_hu) = 0. Π_h u ∈ V_h because both neighbours use the same edge mean of the single-valued trace. | OK |
| A7 | Lemma 2(d) trace constant | div((x−P₃)w²) = 2w² + (x−P₃)·∇w²; (x−P₃)·n = 0 on edges through P₃, = H on e; max‖x−P₃‖ ≤ h_K; Payne–Weinberger with d = h_K applied to v = w − w̄_K; mean-zero on e ⇒ ‖w‖_e ≤ ‖v‖_e. Only the edge-mean property of u − Π_hu on the boundary edge is used. Factor 2: every element has ≤ 2 boundary edges (asserted in code; corner elements have exactly 2). | OK |
| A8 | Lemma 2(e) matrices | K_loc = (2/√3)[[2,−1,−1],…] from ∫∇λ_i·∇λ_j = (1/√3)(1 or −½) for equilateral elements, φ_i = 1−2λ_i. Boundary mass: φ_own ≡ 1 on its edge, the other two are ±(2t−1) there: (h, h/3, h/3, −h/3, 0). Scaling: (2/√3)K_int x = λ(h/3)N₃x, h = √3/n ⇒ K_int x = (λ/2n)N₃x. Float CR eigenvalues converge from below to 0.745256, 2, 2.9646 (independent cross-check of assembly). | OK |
| A9 | Inertia | Integer matrix, symmetric (asserted). Characteristic polynomial exact (FLINT). Descartes exact for real-rooted polynomials; consistency npos+nneg+nzero = n asserted. #neg(K−μN) = #{finite eigenvalues < μ} via congruence with K+N ≻ 0 (c ∈ [0,1] ↦ λ = c/(1−c)). Count 3 ⇒ λ_{h,3} ≥ μ. Mutation μ = 1.98 gives 4 (detected). | OK |
| A10 | ρ arithmetic | ρ = μ/(1+C_h²μ) evaluated in Arb, lower endpoint taken, then rounded DOWN to the rational 1388851/10⁶ with an Arb-certified comparison. Monotonicity of x/(1+Cx). | OK |
| A11 | Sector 𝒮 | Closed, Λ-invariant (Λ commutes with isometries), inside mean-zero. Trial basis Re z^k (k odd), Im z^k (k even), 3∤k is odd under s and C₃-sum-free (Σω^{jk} = 0). Boundary mean of w̃₁ computed: 0 within 2·10⁻³⁶. | OK |
| A12 | Lemma 3(i) multiplicity | 𝓡f* ≠ c f* argument; σ* < ρ ≤ σ₃ ⇒ σ₁ = σ₂ = σ*, W = span{f*, 𝓡f*}; s-matrix [[−1,1],[0,1]] ⇒ W∩𝒮 one-dimensional. (Consistent with Thm 1.2 of arXiv:2603.25116, not used.) | OK |
| A13 | Lemma 3(ii)(iii) Temple | Spectrum of Λ restricted to 𝒮 ⊂ {σ₁} ∪ [ρ,∞) (other eigenvalues equal σ_k, k ≥ 3). Temple: ⟨(A−λ₁)(A−ρ)f,f⟩ ≥ 0. Inequality direction checked: lower bound λ̃ − ε²/(ρ−λ̃). Upper bound σ₁ ≤ λ̃ by Rayleigh. Mutation ρ = 0.7 detected. | OK |
| A14 | Exact integrals | All integrands are polynomials in the edge parameter; acb_poly composition (Horner) and exact ∫₀¹tⁱ = 1/(i+1); outward normal −i·d/‖d‖ for the counter-clockwise vertex order V₀→V₁→V₂ (angles 90°, 210°, 330°). ∂_ν Re F = Re(F′ν), ∂_ν Im F = Im(F′ν). | OK |
| A15 | Lemma 4 | g₁ ∈ D(Λ) ∩ 𝒮, spectral support in [ρ,∞); orthogonal splitting of the residual q; s/(s−λ̃)² decreasing for s > λ̃ > 0. | OK |
| A16 | Exact pair | ‖f₂‖ = ‖f₁‖ needs ⟨𝓡f₁,f₁⟩ = −½‖f₁‖², true for C₃-sum-free f₁; f₂ even ⇒ ⟨f₁,f₂⟩ = 0. Same for g's (also C₃-sum-free), and for the energy form. Float check: ‖w̃₂‖ = ‖w̃₁‖, ⟨w̃₁,w̃₂⟩ = 0 to 10⁻³². | OK |
| A17 | Lemma 5 Green formula | ∮ f dz = 2i∬ ∂f/∂z̄ for ccw boundary; with f = z̄Φ, ∂f/∂z̄ = Φ. F_a′F_b′ = (u_xv_x−u_yv_y) − i(u_xv_y+u_yv_x). Cross-checked against direct area quadrature in the float code (X ≈ 0.50768 both ways). | OK |
| A18 | Lemma 5 error propagation | Bilinear bounds by ‖∇p‖‖∇q‖ (pointwise C-S), edge bounds, length(e_k)^{1/2} = 3^{1/4} for linear moments; normalisation N₁² ∈ [n₀−δ₀², n₀] since f₁ ⊥ g₁. | OK |
| A19 | Lemma 6 logic | λ_min(M′) < 0 ⇒ c with cᵀ𝒜c < (3√3σ₁/P)cᵀ𝒟c; 𝒜, 𝒟 ⪰ 0 ⇒ cᵀ𝒟c > 0 ⇒ admissible trial function; strict inequality. det < 0 or tr < 0 ⇒ a negative eigenvalue. | OK |
| A20 | Pullback formulas | G = A⁻¹A⁻ᵀ = exp(−2S), det A = 1, edge factor j_k = ‖Aτ_k‖, j_k² = cosh2r + t_k sinh2r. **Independent check:** the moment-formula value of Per·λ_min(𝒜,𝒟) agrees with direct quadrature of the pulled-back trial functions on the actual triangles T_S to 7·10⁻¹⁴ at 5 points (`review/selfcheck_local.py`, log `logs/review_selfcheck_local.log`). | OK |
| A21 | Factored M′/r | Uses Σ_kB_k = I, Σ_kb_k = 0, Σ_k(j_k − j̄) = 0, (j_k − j_m)(j_k + j_m) = sinh2r(t_k − t_m). **Independent check:** factored vs direct M′/r agree to 4·10⁻²⁹ on 20 random data sets (random moments satisfying only the exact identities). | OK |
| A22 | r = 0 boxes | sinh2r/r and 2sinh²r/r are increasing on (0,∞) with limits 2 and 0; enclosures [2, value at r_b] and [0, value at r_b]. | OK |
| A23 | Box cover | r-boxes [iR/60,(i+1)R/60] with rational endpoints and bisection children cover [0, 3/5]; φ-boxes [2πk/120, 2π(k+1)/120] are enclosed outward (lower/upper endpoints of Arb balls) and cover [0, 2π]. Failure at max depth raises. Arb `<` means "certainly less" (tested: arb(0,1) < 0 is False). | OK |
| A24 | Local check not vacuous | Signs agree with independent float computation at 8 points; boxes beyond r ≈ 0.85 fail as they must; extending R_LOC to 1 is detected. A second, *unfactored* Arb implementation (λ_min(𝒜 − (3√3σ/P)𝒟) directly) verifies all 26400 boxes of [0.05,0.6]×[0,2π]. | OK |
| A25 | Lemma 7 | W ≥ e^r·W_E (W_E = 3/2 = altitude), W⊥ ≤ e^{−r}·d_E (d_E = √3); boundary = two monotone chains ⇒ ∫(u−c)² ≥ 2·W³/12; Per ≤ 2(W+W⊥) by monotonicity of perimeter for convex sets; bound decreasing in W, increasing in W⊥ — directions correct. Float sanity: B(r) ≥ true σ₁Per at 288 sampled triangles (min gap +6·10⁻⁴ at large r, where both → 0). | OK |
| A26 | Coverage | Local: (0, 3/5]; far: [11/20, ∞); asserted 11/20 ≤ 3/5 in `main.py`. S = 0 is E. | OK |
| A27 | Floating point | No floating-point value enters a certified step. The trial coefficients are exact rationals in `certify/trial_coeffs.json` (produced once by the non-rigorous `make_trial_coeffs.py`), and μ is an exact rational. All conclusions come from exact integers or Arb balls. | OK |
| A28 | Diagnostics pitfall | Arb `str(n)` inflates printed radii (decimal rounding of the midpoint); this once made a box look ±1 wide. True radii (via `mid()`/`rad()`) ≈ 0.15 as expected. Not a soundness issue; noted for future readers of the logs. | OK |
| A29 | Trusted software | FLINT/Arb (charpoly over ℤ, ball arithmetic), python-flint 0.6.0 bindings. Standard trust base for computer-assisted proofs. | accepted assumption |
| A30 | Literature inputs | Payne–Weinberger (convex Poincaré constant), Temple's inequality (proved inline), DtN self-adjointness/discreteness on Lipschitz domains, abstract You–Xie–Liu bound (re-proved inline). | accepted, standard |

## B. Mutation tests (each must FAIL)
Script `review/mutation_tests.py`, log `logs/review_mutation.log` (ends `ALL MUTATIONS DETECTED`):
* μ = 1.98 (above λ_{h,3}): inertia 4 ≠ 3 → AssertionError.
* ρ = 0.7 (< λ̃): Temple hypothesis assertion.
* R_LOC = 1: local check fails near r ≈ 1.
* R_FAR = 0.3: far bound fails.
* target lowered by 0.2·3√3: far bound fails.

## C. Separate AI referee pass (fresh context, adversarial brief)
The referee re-derived every lemma, independently re-implemented the four computational checks
(own CR assembly from real coordinates; mpmath 70-digit recomputation of λ̃, ε², Temple bound, δ₀, δ₁;
direct area quadrature for X, Y; direct Rayleigh–Ritz on T_S for the local bound; random-S test of the far
bound) and re-ran `certify/main.py` (log identical apart from timing lines, which were later removed). It also instrumented the box loop
(accepted boxes have total area 3.76991118 = 0.6·2π) and confirmed the float inertia (3, 0, 405) with
smallest positive eigenvalue 0.154. Its numerical trace-constant test on the reference element gives
sup ‖w‖²_e/‖∇w‖² ≈ 0.405 vs. the certified 0.969 (valid, conservative).
**Verdict: no fatal error, no mathematical error.** Findings and resolutions:

| # | finding (severity) | resolution |
|---|---|---|
| C1 | (F4) Temple stated without hypothesis λ₁ < ρ (needs fix; application satisfies it) | FIXED: hypothesis added, proof line expanded. |
| C2 | Displayed enclosures in PROOF.md rounded *inward* (ε², 3√3σ_lo in §3 and §6); log values correct (needs fix) | FIXED: replaced by outward-rounded values / log radii. |
| C3 | Lemma 5 text √3·δ₀ vs code 3^{1/4}·δ₀ (cosmetic; code constant is the sharp C-S one, both valid) | FIXED: text now says length(e_k)^{1/2} = 3^{1/4}. |
| C4 | "σ₃(E) = 2 exactly" unproved (only σ₃ ≤ 2 and ≥ 1.389) (cosmetic; unused) | FIXED in PROOF.md. |
| C5 | "continuous at interior edge midpoints" for V + V_h imprecise (cosmetic) | FIXED: zero-mean jumps argument. |
| C6 | the norm of S undefined (cosmetic) | FIXED: spectral norm. |
| C7 | Symbol overloads ρ (operator/number), r (norm of S / residual) (cosmetic) | FIXED: rotation operator renamed 𝓡, residual renamed q. |
| C8 | "−6.11 r" slope remark is uncertified numerics (cosmetic) | FIXED: labelled as uncertified float remark about F_loc. |
| C9 | Could mention robustness margin (cosmetic) | DONE: re-verified myself — local check passes with all moment enclosures widened by ±0.01 and ±0.03; noted in PROOF.md §8. |

Additional code hygiene after review: an explanatory message was added to the Temple-hypothesis assertion in
`cert_E.py` (no change in behaviour). The full pipeline was re-run after all edits (see final log).

## E. Packaging checks for this submission (2026-10-02)

| # | check | result |
| --- | --- | --- |
| E1 | Cross-platform determinism | `certify/main.py` gives byte-identical output, apart from the environment line, under Python 3.9.23 with python-flint 0.6.0 (macOS x86_64) and Python 3.12.14 with python-flint 0.9.0 (macOS arm64). Logs: `logs/certify.log` and `logs/certify_python3.9_flint0.6.0.log`. |
| E2 | Review scripts under Python 3.12 | `review/mutation_tests.py` reports all 5 mutations detected; `review/selfcheck_local.py` agrees to 4e-29, 4e-14 and 26400/26400 boxes. |
| E3 | Mathematics formatting | `scripts/check_math.py` (cmarkgfm 2025.10.22, mathjax-full 3.2.2): all 536 expressions in `PROOF.md` are preserved by GFM and rendered by MathJax without errors. The full-repository run reports errors only in the pre-existing `research/solutions/593-analytic-bandwidth/PROOF.md`. |
| E4 | Repository checks | With this package present, `python3 scripts/catalogue.py --check` reports "Validated 651 unique problems, metadata, required sections, math delimiters, local links …", and `python3 scripts/test_catalogue.py` passes (54 tests, OK). |
| E5 | Statement | `statement.md` is a byte-for-byte copy of `problems/022-steklov-polygon-optimizer.md` at the pinned commit. It is identical to problem 023 at `37a2536` apart from the ID. |

## D. Unresolved issues
**None.** Accepted (not unresolved) assumptions, as in any computer-assisted proof: correctness of
FLINT/Arb/python-flint, and the classical results cited in PROOF.md §0 (Payne–Weinberger; self-adjointness
and discreteness of the Dirichlet-to-Neumann operator on Lipschitz domains; min–max). The abstract
You–Xie–Liu bound and Temple's inequality are re-proved in PROOF.md.
**Human review: none has taken place.** The result must be treated as an unrefereed, AI-generated claim.
