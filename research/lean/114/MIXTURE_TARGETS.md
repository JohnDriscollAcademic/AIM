# Proposed next boundary: the actual standardized Gaussian variance mixture

This removes the missing connection from nonconstant mixing variance to an actual
non-Gaussian probability law. It does not assume mixture moment identities,
independence, mean positivity, or a positive variance conclusion. Those must be
proved from the explicit product construction and stated input hypotheses.

## Exact files and signatures

- `research/lean/114/AIM/P114/MixtureDefinitions.lean`: `normalizedVarianceMixture mu V`
  is the pushforward of `mu.prod (gaussianReal 0 1)` under
  `(omega,z) -> z * sqrt(V omega / integral V dmu)`.
- `research/lean/114/MixtureChallenge.lean` contains the three exact proposed
  signatures. They supplement, without editing, the original three theorems.
- `standard_gaussian_fourth_moment`: the integral of z^4 under the actual pinned
  Mathlib `gaussianReal 0 1` is exactly 3.
- `normalized_variance_mixture_moments`: for any probability space, measurable V,
  and a.e. 1/4 < V < 1/2, the actual pushforward is a probability measure; z, z^2,
  z^4 are integrable under it; its mean is 0, its second moment is 1, and its
  fourth moment is `3 * integral(V^2) / (integral V)^2`.
- `normalized_variance_mixture_not_gaussian`: adding the explicit hypothesis
  that V is not a.e. equal to any constant, the actual pushforward is unequal
  to `gaussianReal 0 1`.

The bounds are exactly those established for the manuscript's V. Strict bounds
are only needed for source alignment and nondegenerate normalization; no
pointwise assumption outside an a.e. full-measure set is imposed. Measurability
is explicit. All real divisions use the mean that the proof must show is
positive; no arbitrary scalar represents an expectation. The construction
makes independence explicit through the product measure. The standardization
is established by both the zero mean and unit second moment. Nonconstancy is
an intrinsic property of the input V, not the desired inequality between laws.

## Source correspondence and remaining gap

Mathematical source: Sidney Holden, *A non-Gaussian limit for nodal surplus*,
v0.3, 2026-10-02, Section 5 and Theorem 1, Eq. (5). Source PDF SHA-256 remains
74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6.
This proves the concluding mixture inference as an actual probability-law
statement. It does not yet construct R=-A/B, identify V=v(R), prove that this V
is measurable and nonconstant with the stated bounds, or establish spectral
surplus convergence to this mixture. Those are still explicit gaps.

## Pinned Mathlib reuse and proof plan

Pinned Mathlib commit 0df444a360eaa60ab8c11dca51a86af692955474 was searched.

1. `Probability/Distributions/Gaussian/Real.lean` provides gaussianReal,
   integral_id_gaussianReal, variance_fun_id_gaussianReal,
   memLp_id_gaussianReal, mgf_fun_id_gaussianReal, and the second-derivative
   pattern at lines 557--570. No direct fourth-moment theorem was found.
2. `Probability/Moments/MGFAnalytic.lean` provides iteratedDeriv_mgf_zero.
   Four ordinary derivatives of exp(t^2/2) are polynomial times the same
   exponential, ending `(3+6*t^2+t^4)*exp(t^2/2)`, with value 3 at zero.
   This proves the missing fourth moment from an existing Gaussian MGF theorem.
3. `MeasureTheory/Integral/Prod.lean` provides Integrable.mul_prod and
   integral_prod_mul. Prove integrability separately, then factor the actual
   product-space integrals after squaring/raising the sqrt to the fourth power.
4. `MeasureTheory/Integral/Bochner/Basic.lean` provides integral_map,
   integral_mono_ae, integral_congr_ae, and integral linearity. Bounded V implies
   its relevant powers and square root are integrable. The positive lower
   bound gives a positive mean and a denominator bounded away from zero.
5. `Probability/Moments/Variance.lean` provides variance_eq_integral,
   variance_eq_sub, variance_nonneg, and ae_eq_integral_of_variance_eq_zero.
   Alternatively integral_eq_zero_iff_of_nonneg_ae derives positive centered
   second moment directly from boundedness and nonconstancy. Reuse the existing
   integral kurtosis lemma, then contradict the actual Gaussian fourth moment
   if the two measures were equal.

## Principal implementation risks

- No ready-made Gaussian fourth moment: derivative rewrites require explicit
  differentiability certificates, but follow an existing pinned Mathlib proof.
- A.e. bounds must be transported correctly to the product and mapped laws;
  pointwise nonnegativity cannot silently replace the hypotheses.
- Mathlib's integral returns zero for nonintegrable functions. The advertised
  theorem therefore explicitly proves first/second/fourth integrability;
  integral_prod_mul alone is insufficient evidence.
- The absence of graph-specific V from this theorem must remain visible in all
  README, manifest and PR claims. This is a substantial missing link removed,
  not an end-to-end counterexample yet.

No proof body is implemented at this boundary stage. Two independent statement
approvals and typechecking are required before implementation.
