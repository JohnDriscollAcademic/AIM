# AIM114 Gaussian-mixture extension: independent statement referee 2

- **Phase:** pre-implementation mathematical-boundary review.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the three proposed declarations at the exact hashes below.
- **Mechanical evidence inspected:** the implementer's [boundary type-check log](../verification/mixture-boundary-typecheck.log), which records exit 0 and the three deliberate Challenge-placeholder warnings. I did not independently run this boundary check and do not treat it as proof evidence.

## Exact reviewed boundary

| File | SHA-256 |
|---|---|
| `AIM/P114/MixtureDefinitions.lean` | `63573393a3e5521a4276e822717f307bbabd4c327540e22895c99a1c0fab7652` |
| `MixtureChallenge.lean` | `edd2f69de4e8ba1552189d57856ae4bd7f35a4b9c73a53c0d2e1de81c5a3570a` |
| `MIXTURE_TARGETS.md` | `85fd7a64932d5fcd567f4cceb13711da60fcc1ffdde70e118c7ee4e6143ef1f8` |
| Submitted v0.3 PDF | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Frozen complete source problem `statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| Expanded informal `PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |

I read all proposed definitions and signatures and the complete scope document, checked them against my independent review of the original manuscript, and independently searched and read the relevant pinned Mathlib APIs. The initial candidate was subsequently moved into the standard `AIM/P114/` module path; I inspected the final import and recomputed all listed hashes after that move. No implementation was used as evidence and no proof changes were made by this reviewer.

## Construction and hypotheses

`normalizedVarianceMixture` is the actual pushforward of `μ.prod (gaussianReal 0 1)` under the map `(ω,z) -> z*sqrt(V(ω)/integral V)`. This is exactly the standardized variable in the source, with Gaussian independence implemented by the product probability space. It is not a named opaque distribution, a hypothetical characteristic function, or a scalar whose moments are simply postulated.

The input measure is explicitly a probability measure, the mixing variable is real valued and measurable, and its strict bounds `1/4<V<1/2` are imposed only almost everywhere. These match the manuscript's established properties of `v(R)`; no pointwise condition is substituted on a null exceptional set. Measurability makes the product-space map measurable. The bounds give actual integrability of `V` and `V^2` and a positive integral mean, so the normalization is meaningful. These consequences are not smuggled into the definition as hypotheses of the desired law equality.

The nonconstancy hypothesis excludes almost-everywhere equality to **any** constant. It is intrinsic to the input function and, under these boundedness assumptions, is equivalent to positive centered second moment. It neither asserts the non-Gaussian law conclusion nor assumes a kurtosis inequality. The assumptions are satisfiable, for example on a two-point equal-weight space with mixing values `1/3` and `2/5`.

## Each proposed result

**`standard_gaussian_fourth_moment`.** This computes the actual fourth-power Bochner integral under Mathlib's standard Gaussian measure as the exact real number 3. There are no fitted constants or numerical tolerances. The library's `memLp_id_gaussianReal` supplies fourth-moment integrability; `mgf_fun_id_gaussianReal` and `iteratedDeriv_mgf_zero` provide a direct proof route. Independently differentiating `exp(t^2/2)` gives the successive factors `t`, `1+t^2`, `3t+t^3`, and `3+6t^2+t^4`; evaluation of the fourth derivative at zero is 3. Thus this target is supported by existing analytic results without introducing an unproved Gaussian-moment axiom.

**`normalized_variance_mixture_moments`.** Its output explicitly establishes that the pushforward is a probability measure and that the first, second, and fourth powers are integrable. This matters because a bare Bochner-integral expression is not by itself a finite-moment assertion. The zero mean, unit second moment, and exact fourth moment are conclusions, not assumptions. They follow from the product construction, Gaussian moments, and the almost-everywhere identities `sqrt(V/a)^2=V/a` and `sqrt(V/a)^4=V^2/a^2`, where `a=integral V>0`. The factor 3 and denominator exponent two are correct. Proving the zero mean together with unit second moment also establishes the intended variance normalization.

**`normalized_variance_mixture_not_gaussian`.** The conclusion is the precise inequality of measures with `gaussianReal 0 1`. Together with the preceding mean and second-moment result, this is the source's failure of the standardized Gaussian law. Nonconstancy forces positive centered second moment for the bounded mixing variable; the already reviewed scalar integral inequality then makes the mixture's fourth moment strictly exceed 3. Equality of the actual measures would contradict the separately proved actual Gaussian fourth moment. This proof route requires no conditional-independence shortcut, distributional-limit hypothesis, or unproved moment-factorization assumption.

## API review and proof obligations

I read the pinned `Probability/Distributions/Gaussian/Real.lean` moment and MGF results, the derivative-to-moment theorem in `Probability/Moments/MGFAnalytic.lean`, the product integration APIs in `MeasureTheory/Integral/Prod.lean`, and the centered-variance APIs in `Probability/Moments/Variance.lean`. These support the proposed boundary. A direct fourth-moment theorem was not found in the pinned Gaussian-real file; the proposed derivative calculation extends the existing second-moment pattern rather than bypassing that missing proof.

There are two substantive implementation obligations to retain in final review. First, `integral_prod_mul` is stated even for nonintegrable factors; its use alone does not prove a probabilistic moment claim. The advertised integrability conclusions must be established from the bounds and Gaussian finite moments, for example with `Integrable.mul_prod`. Second, square-root identities and polynomial factorizations using `V>=0` must be justified almost everywhere, then transported correctly through the product measure and pushforward. They must not be rewritten as global pointwise identities outside the given full-measure set.

## Scope and disposition

The extension formalizes an actual probability-law implication that was absent from the earlier scalar-kurtosis lemma. It is a substantial part of the manuscript's concluding argument. It does not construct the stable pair `(A,B)`, prove the boundary ratio limit, define and identify the graph-specific `v(R)`, establish its nonconstancy, or prove that spectral surplus converges to this mixture. Those application links remain visible in the scope document, and the separate universal linear-variance assertion is untouched. Sidney Holden's mathematical authorship and the manuscript revision are preserved in the scope document and package attribution.

**Requested mathematical changes: none.** Approval applies only to these bytes. An independent second approval, completed type-checking, proof implementation that does not import Challenge placeholders, inclusion of all three results in the combined Comparator boundary, and independent final source and verification review remain required. This boundary approval does not establish any theorem or certify a full Lean proof of AIM114.
