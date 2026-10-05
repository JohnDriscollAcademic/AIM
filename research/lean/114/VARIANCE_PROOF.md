# The actual Cauchy-defined variance function

`AIM/P114/VarianceProof.lean` proves the five statements frozen in
`VarianceChallenge.lean` for the actual deterministic function in manuscript
Eq. (3). `actualNodalVariance` is defined by the probability of the strict
triangle event under the product of three standard Cauchy measures. The
proof does not assume a bound, continuity statement, or nonconstancy property
of that function.

The standard Cauchy law is atomless because it has a density with respect to
Lebesgue measure. Its strictly positive density also makes Lebesgue measure
absolutely continuous with respect to the Cauchy law, so every nonempty open
set has positive Cauchy measure. These properties pass to the relevant product
measures using existing Mathlib results.

For nonzero `r`, the triangle event is open and contains `((r,r),0)`.
The strict complementary event is open and contains `((0,0),3/|r|)`.
These witnesses use actual Cauchy coordinates and respect the constraint
`sqrt(1+x²) >= 1`. Consequently both the triangle event and its complement
have positive mass, proving `1/4 < v(r) < 1/2`. At zero the strict triangle
event is empty, so the same formula gives `v(0)=1/2`.

For continuity, every fiber of `x -> sqrt(1+x²)` has at most two points:
equal magnitudes imply `x²=y²`, hence `x=y` or `x=-y`. Cauchy atomlessness
therefore makes every fiber null. For nonzero `r`, conditioning on the first
two coordinates leaves each triangle-boundary equality as a single magnitude
fiber in the third coordinate. At `r=0`, the lower boundary reduces to equal
first and second magnitudes, another null set by conditioning; the upper
boundary cannot occur because both magnitudes are positive. Off these null
boundaries, the indicator of the triangle event is locally constant in `r`.
Its absolute value is bounded by one, so dominated continuity proves that its
integral, and therefore the actual variance function, is continuous on all
of the real line.

For any real probability law `ρ` that gives positive mass to every nonempty
open set, a.e. constancy of the continuous variance function would imply
everywhere constancy. This contradicts `v(0)=1/2` and `v(1)<1/2`. If also
`ρ({0})=0`, the strict bounds hold `ρ`-a.e. These facts discharge every input
of the already proved Gaussian-mixture theorem, giving an actual law unequal
to the standard Gaussian with the manuscript's fixed mixing-variance function.

The input law `ρ` is still general. The stable response-vector law, its ratio
law, verification of these intrinsic support/zero-atom hypotheses for that
ratio, the empirical-process limit, and the spectral graph-to-module bridge
remain to be formalized. This module does not establish the end-to-end nodal
surplus counterexample.
