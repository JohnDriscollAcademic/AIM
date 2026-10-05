# Actual Cauchy-defined nodal variance: proposed next boundary

## Frozen source and preserved scope

Mathematical source: Sidney Holden, *A non-Gaussian limit for nodal surplus*,
v0.3, 2026-10-02, Eq. (3), Section 3, and the concluding application in
Section 5. Full submitted PDF SHA256:
74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6.
The canonical AIM target remains problem114, the unrestricted quantum-graph
nodal-surplus Gaussian conjecture and the separate universal variance question.
No ID, canonical path, or original target changes here.

This block fixes the deterministic function v to the actual Cauchy triangle
probability. It removes the arbitrary measurable/bounded/nonconstant V of the
previous mixture extension. It does not construct the stable vector (A,B),
prove convergence of response sums, identify the input law rho with law(-A/B),
or formalize the spectral graph-to-module bridge. Those remain missing.

## Exact definitions

Definitions are in AIM/P114/VarianceDefinitions.lean. The original three
supporting results and the previous mixture mathematics are unchanged.

- `cauchyMagnitude x = sqrt(1+x^2)` for every real x.
- `cauchyTripleMeasure = ((cauchyMeasure 0 1).prod
  (cauchyMeasure 0 1)).prod (cauchyMeasure 0 1)`. Thus the coordinates are three
  fresh independent standard Cauchy variables, grouped `(X1,X2),X3`.
- `varianceTriangleEvent r` is precisely
  `|C1-C2| < |r|*C3 and |r|*C3 < C1+C2`, with both inequalities strict.
- `actualNodalVariance r = 1/2 - cauchyTripleMeasure.real(event r)/4`.
  The event's probability is actual measure mass, not an unconstrained scalar
  and not a placeholder predicate. This definition covers ALL real r,
  including zero, through the same formula.

The original manuscript defines v for the needed nonzero ratio values. The
extension at zero is canonical from the displayed event and is useful for a
short continuity/nonconstancy proof; it does not alter v away from zero.
No numeric approximation, truncation or sampled distribution is used.

## Five advertised statements

Exact signatures appear in VarianceChallenge.lean. All quantifiers, constants,
endpoints and measure assumptions are displayed there without bundled custom
assumption structures.

1. `actual_nodal_variance_zero`: actualNodalVariance 0 = 1/2.
2. `actual_nodal_variance_bounds`: for every real r!=0,
   1/4 < actualNodalVariance r < 1/2.
3. `actual_nodal_variance_continuous`: Continuous actualNodalVariance on ALL
   of R, including zero.
4. `actual_nodal_variance_mixture_inputs`: for any actual real probability
   measure rho with `Measure.IsOpenPosMeasure rho` and rho({0})=0, prove that
   actualNodalVariance is measurable, satisfies the strict bounds rho-a.e.,
   and is not rho-a.e. equal to any constant.
5. `actual_nodal_variance_mixture_not_gaussian`: under exactly the same
   intrinsic hypotheses on rho, the actual product/pushforward law
   normalizedVarianceMixture rho actualNodalVariance is unequal to the actual
   `gaussianReal 0 1` measure.

`IsOpenPosMeasure` means every nonempty open set has strictly positive measure;
it is a precise full-support assumption, not an assumed conclusion about v.
Only the atom at zero is excluded: no atomlessness assumption at other real
points is needed. The law rho is a real measure with total mass one, not a
numerical surrogate. These assumptions are nonvacuous (for example standard
Cauchy/Gaussian laws). Proving them for the manuscript's future stable-ratio
law is explicitly separate. No regularity, bound, nonconstancy, or moment
identity of actualNodalVariance is assumed anywhere in this boundary.

## Concrete proof route and pinned-library assessment

The pinned Mathlib commit is0df444a360eaa60ab8c11dca51a86af692955474.
Relevant definitions/results were inspected directly:

- Probability/Distributions/Cauchy.lean: cauchyMeasure, its probability
  instance, cauchyMeasure_of_scale_ne_zero, and cauchyPDF_pos.
- MeasureTheory/Measure/WithDensity.lean: automatic null-singleton instance
  for withDensity, withDensity_absolutelyContinuous', and absolute continuity.
- MeasureTheory/Measure/OpenPos.lean: AbsolutelyContinuous.isOpenPosMeasure,
  eq_of_ae_eq, Continuous.ae_eq_iff_eq.
- MeasureTheory/Measure/Prod.lean: product IsOpenPosMeasure instance and
  ae_prod_iff_ae_ae.
- MeasureTheory/Integral/Bochner/Set.lean: integral_indicator_one, identifying
  the actual event mass with an integral of its bounded indicator.
- MeasureTheory/Integral/Bochner/Basic.lean: continuousAt_of_dominated.
- MeasureTheory/Measure/Typeclasses/NullSingletonClass.lean: countable/finite
  sets have measure zero under atomless measures, and Measure.ae_ne.

First derive full-support and atomlessness of the actual standard Cauchy law
from its strictly positive density; these are not added as theorem inputs.
The triple product is a probability measure positive on every nonempty open
set. For r!=0 the strict triangle event is nonempty and open. Its complement
contains a nonempty open strict-violation event. Explicit witnesses can be
chosen in magnitude coordinates Cj>1, and then realized by
Xj=sqrt(Cj^2-1). Positivity of both sets gives event probability strictly
between0and1 and hence the source bounds on v.

For continuity at any r0!=0, condition on the first pair of Cauchy coordinates.
Each boundary equation fixes C3 to one value. A fiber of sqrt(1+x^2) is contained
in at most two points, so it has zero Cauchy probability. For r0=0, the only
potential boundary is C1=C2; this implies X1=X2 or X1=-X2 and has zero product
probability by atomlessness and conditioning. Off these null boundaries the
triangle indicator is locally constant in r. Its absolute value is at most1;
dominated continuity therefore applies to its actual integral/event mass.

For a full-support law rho, continuity upgrades any a.e. constancy of v to
everywhere constancy. But v(0)=1/2 and v(1)<1/2 contradict that. The no-atom-zero
hypothesis separately makes the already-proved strict bounds hold rho-a.e.
Then apply the completed normalized_variance_mixture_not_gaussian theorem.
There is no need for the endpoint limit as |r|->infinity, so it is intentionally
outside this coherent next block.

## Risks and implementation obligations

- The probability/event expression uses `Measure.real`; it must be converted
  correctly to indicator integrals, and finiteness of the triple probability
  law must remain explicit when converting ENNReal bounds.
- Boundary-null proofs must handle r=0 separately. Dividing by |r| in that case
  or silently assuming all signed sums are nonzero is invalid.
- Full support must be proved from the actual Cauchy density. The open-set
  witnesses must respect Cj>=1; arbitrary positive Cj are not valid witnesses.
- Every occurrence of a square-root identity needs its nonnegative-radicand
  justification. The fiber argument and magnitude witness are exact algebra.
- No theorem in this new block is an end-to-end quantum-graph theorem. The
  intrinsic assumptions on the future ratio law must be retained honestly.

At this boundary stage there are no proof bodies. The definitions/signatures
must typecheck and receive two independent approvals before implementation.
