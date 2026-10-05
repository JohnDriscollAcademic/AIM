# AIM114 probability roadmap after the actual Gaussian mixture extension

Status: read-only technical assessment, 2026-10-05. No theorem in this document
has been implemented or approved as a new proof boundary. Pinned Mathlib is
0df444a360eaa60ab8c11dca51a86af692955474. Source manuscript is Sidney Holden,
v0.3, 2026-10-02, Sections 3--5, PDF SHA256
74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6.

## What is implemented now

The original three exact supporting results remain unchanged. The new
AIM/P114/MixtureProof.lean constructs the actual map law of
Z sqrt(V/EV) on mu.prod(gaussianReal 0 1), proves probability status and
first/second/fourth integrability, proves its moments 0,1,3 EV^2/(EV)^2,
and proves inequality to gaussianReal 0 1 under measurable V, a.e.
1/4<V<1/2, and intrinsic a.e. nonconstancy. The Gaussian fourth moment 3 is
proved from the existing MGF. Its build, fresh re-elaboration, and axiom audit
pass; both independent final mixture reviews approve. This DOES NOT yet
supply the manuscript's actual V, a stable vector, a process/random-evaluation
limit, or the spectral-frequency bridge.

## Recommended fastest route: finite grids, not a full Donsker development

The pinned library contains a one-dimensional iid CLT, finite-dimensional
Levy convergence, multivariate Gaussian measures, martingales and Doob's
maximal inequality. No Donsker theorem, empirical-process functional CLT,
Brownian-bridge construction, or ready-made Skorokhod process limit was found.
Building that entire infrastructure is unnecessary for this single random
index. The manuscript's one-jump representation permits a direct finite-grid
approximation of the scalar G_m(R_m).

### A. Prove the finite signed-threshold lemma

For independent fair signs sigma_i and deterministic |d_i|<=1, establish the
finite maximal inequality

  P(max_{k<=N}|sum_{i<=k} sigma_i d_i| > t)
    <= 2 P(|sum_{i<=N} sigma_i d_i| > t)
    <= 6 N^2 / t^4,                       t>0.

The first step is the elementary Levy reflection inequality for symmetric
independent increments; it can be proved on the finite sign cube by pairing
sign continuations after the first crossing. The second step is the exact
fourth-moment expansion E(sum sigma_i d_i)^4 <= 3 N^2 followed by Markov.
Alternatively derive a sufficiently large absolute constant from the existing
Doob maximal inequality and exponential supermartingale. Do not assume a
conditional-independence assertion involving xi: only sigma_i's independence
of their cosecants is used in this threshold estimate and must be established
from the original phase law.

Apply this lemma to jump marks inside each grid cell, conditionally on the
cosecants. The baseline cancels in differences. With N_k the number of
thresholds in cell k and p_k its one-module probability,

  E N_k^2 = m p_k + m(m-1)p_k^2,
  sum_k E(N_k^2/m^2) <= 1/m + max_k p_k.

Thus, for one half-line, the probability that any cell oscillation of G_m
exceeds epsilon is <= 6 epsilon^(-4)(1/m+max p_k); a union bound over both
half-lines gives a safe factor 12. These proposed constants require exact
checking in the actual threshold convention; there is no implemented lemma
claim here. Threshold atomlessness gives grids with max p_k arbitrarily
small on each [1/L,L]. Importantly, a second-moment/Chebyshev union bound does
NOT shrink with the mesh; the fourth moment is the essential improvement.

A practical finite statement should quantify over an actual finite product
of module data and signs, define G_m and the finite cell oscillation explicitly,
and conclude the displayed probability bound. It must not take asymptotic
equicontinuity as a hypothesis. The supremum can be a finite maximum over
sample thresholds; there are at most m jumps on each half-line. A deterministic
sorting/permutation lemma proves the sign bound without requiring a globally
measurable choice of permutation.

### B. Prove only finite-dimensional mixed convergence

For every finite deterministic nonzero grid r_1,...,r_k and coefficients a_j,
put H=sum a_j h(r_j) on the ORIGINAL module data. H is bounded, centered, and
has its actual covariance. Prove the manuscript's expansion

  E exp(i zeta.xi/m + i H/sqrt(m))
    = 1 - (psi(zeta)+E H^2/2)/m + o(1/m).

The mixed first-order error is controlled using E||xi||^(3/4)<infinity;
its normalized size is O(m^(-5/4)), so no false finite first moment of xi
is needed. The quadratic term converges by dominated convergence. Independence
across modules raises the one-module expression to the mth power. For the
limiting finite Gaussian vector, use the actual covariance matrix
C_ij=E[h(r_i)h(r_j)] and Mathlib's multivariateGaussian; prove it is positive
semidefinite by integrating a square. The stable-vector law is constructed
separately, then its product with this Gaussian vector is the candidate law.
Finite-dimensional Levy convergence identifies this product law, so the
required independence is a conclusion of characteristic-function factorization.
A one-dimensional CLT alone is insufficient for this joint statement.

Relevant existing APIs:
- Probability/CentralLimitTheorem.lean:
  tendstoInDistribution_inv_sqrt_mul_sum_sub and its characteristic-function
  proof pattern (the library explicitly advertises dimension 1 only).
- MeasureTheory/Measure/LevyConvergence.lean:
  isTightMeasureSet_of_tendsto_charFun (line 45),
  ProbabilityMeasure.tendsto_of_tendsto_charFun (line 202),
  ProbabilityMeasure.tendsto_iff_tendsto_charFun (line 215).
  These work in finite-dimensional real inner-product spaces.
- Probability/Distributions/Gaussian/Multivariate.lean:
  multivariateGaussian (line 168), charFun_multivariateGaussian (line 239),
  covariance_eval_multivariateGaussian (line 216).
- Probability/Independence/CharacteristicFunction.lean: joint characteristic
  function factorization APIs, including indepFun_iff_charFun_prod.
- Analysis/SpecialFunctions/Complex/LogBounds.lean:
  tendsto_pow_exp_of_isLittleO_sub_add_div, already used in the CLT proof.

### C. Evaluate at the random ratio without constructing a Gaussian process

For fixed L and a finite grid, replace R_m by its grid selector pi(R_m) on
1/L<=|R_m|<=L. Joint convergence of the finite vector and (U_m/m,T_m/m)
handles this finite selector; discontinuity sets are only B=0 and finitely
many ratio boundaries. Show these have limit probability zero, rather than
incorrectly invoking a globally continuous mapping theorem.

The limit of the selected Gaussian coordinate, independent of R, is a finite
variance mixture with variance v(pi(R)). The actual finite-grid mixture law
can be built on the product of R's law and the standard Gaussian, avoiding an
infinite Gaussian-process object. Let the grid mesh vanish; continuity of v
shows these laws tend to the actual mixture with variance v(R). Let L grow;
tightness of R_m and P(R=0)=0 control the excluded region.

A direct characteristic-function comparison avoids the need for a new general
'double approximation' distribution theorem:

  |E exp(itX)-E exp(itY)|
    <= |t| epsilon + 2 P(|X-Y|>epsilon).

Use this with the explicit cell-oscillation bound, pass first m->infinity,
then mesh->0, then L->infinity, and apply finite-dimensional Levy convergence
to the ALREADY CONSTRUCTED actual scalar mixture law. This route removes the
need for a Skorokhod space, path-space measurability, a full Donsker theorem,
and random evaluation on an infinite-dimensional function space. It still
requires genuine new finite-grid and mixed-characteristic-function proofs.

### D. Uniform integrability still needs its own theorem

Weak convergence alone does not give the source's second/fourth moment limits.
Use the same finite sign-maximal argument at order six: exact sixth moments
of a Rademacher sum are <=15 N^3, so a finite maximal inequality yields a
uniform sixth-moment bound for G_m evaluated at ANY nonzero random r. The
baseline and two half-lines only change an absolute constant. Then prove
second/fourth uniform integrability and transfer their limits. This avoids
formalizing the stronger all-moment exponential tail statement if desired.
It cannot be replaced by a hypothesis simply asserting the desired fourth
moment limit.

Existing starting points: Probability/Martingale/OptionalStopping.lean,
maximal_ineq (line 155); the pinned library has Doob's first maximal inequality,
not a ready-to-use L4 maximal theorem located in this search. Markov and moment
integral tools are available, but the finite sign combinatorics are new work.

## The next actual v(R) block that discharges the new mixture inputs

Use the REAL pinned Cauchy measure, whose API is cauchyMeasure (not cauchyReal):

  gamma := ProbabilityTheory.cauchyMeasure 0 1
  P3 := gamma.prod (gamma.prod gamma)
  C(x) := sqrt(1+x^2)
  T(r) := {p : R x (R x R) |
       |C(p.1)-C(p.2.1)| < |r|*C(p.2.2) and
       |r|*C(p.2.2) < C(p.1)+C(p.2.1)}
  actualV(r) := 1/2 - (P3(T(r))).toReal/4.

This is exactly the manuscript's deterministic v, using three fresh
independent Cauchy variables. Keep this explicit integral/measure definition;
do not replace it with an arbitrary continuous bounded nonconstant function.

The first feasible source-specific package has these proposed statements:

1. `actual_variance_zero`: actualV(0)=1/2.
2. `actual_variance_strict_bounds`: for EVERY real r!=0,
   1/4<actualV(r)<1/2.
3. `actual_variance_continuous`: Continuous actualV on all of R.
4. `actual_variance_mixture_inputs`: for every actual probability measure rho
   on R with IsOpenPosMeasure rho and rho({0})=0,
   actualV is measurable,
   a.e. 1/4<actualV<1/2 under rho, and
   not exists c with actualV=ae constant c under rho.
5. `actual_variance_mixture_not_gaussian`: under those SAME intrinsic measure
   hypotheses, normalizedVarianceMixture rho actualV != gaussianReal 0 1,
   invoking the now implemented mixture theorem.

These quantify over genuine measures, with actualV fixed by the Cauchy triple.
They remove the arbitrary-V input of the current extension. Applying them to
rho=law(-A/B) still requires constructing the actual stable vector and proving
its ratio law has the two stated properties; this is not an end-to-end theorem.

### Proof mechanics for actualV

The pinned Cauchy file provides cauchyMeasure, its probability instance,
cauchyMeasure_of_scale_ne_zero and strictly positive density cauchyPDF_pos;
it contains no characteristic-function or moment theorem. Absolute continuity
with Lebesgue gives atomlessness. Positive density makes every nonempty open
interval positive. Product open-set positivity is already an instance in
MeasureTheory/Measure/Prod.lean:270.

For r!=0, the triangle set and a strict complementary set are nonempty open
sets. For the triangle, pick C3=s>1 and C1=C2=L>max(1,|r|s/2).
For the complement, choose C1=C2 near1 and C3 large enough that
|r|C3>C1+C2. Every C>1 is realized by x=sqrt(C^2-1). Positivity of these open
sets proves the strict 1/4 and1/2 bounds. This is an explicit existence proof,
not a numerical check.

For continuity at r0!=0, condition on the first two Cauchy coordinates.
Each boundary equation imposes C3=k, whose preimage under sqrt(1+x^2) has at
most two points and hence probability zero. At r0=0, the remaining boundary
C1=C2 implies X1=+X2 or X1=-X2, also a null set by conditioning. Dominated
convergence of the bounded triangle indicators proves continuity everywhere.
Relevant API: MeasureTheory/Integral/DominatedConvergence.lean,
tendsto_integral_filter_of_dominated_convergence, and
MeasureTheory/Integral/Bochner/Basic.lean:426 continuousAt_of_dominated. The measurable strict-inequality event follows
from ordinary continuous-function comparisons.

Nonconstancy under any full-support rho follows especially cheaply from
continuity, actualV(0)=1/2, and actualV(1)<1/2:
MeasureTheory/Measure/OpenPos.lean:130 `eq_of_ae_eq` and line142
`Continuous.ae_eq_iff_eq` upgrade a.e. constancy to everywhere constancy.
The limit of v at infinity is NOT necessary for this conclusion and can be
omitted from the first formalization boundary. Likewise a continuous density
for (A,B) is stronger than the eventual mixture inference needs.

## Actual stable vector and ratio: major remaining work

The manuscript's response identity, E W^2=2, fractional moment, and one-module
characteristic expansion are not yet formalized. In particular, the pinned
Cauchy.lean ends after its probability instance: no Cauchy characteristic
function theorem was found. A real theorem proving
charFun(cauchyMeasure 0 scale)(t)=exp(-scale*|t|) is a genuine prerequisite;
it may be built through Fourier inversion of exp(-scale*|t|), whose half-line
integrals are elementary, rather than a new contour integration development.
That proposed route needs a separate exact API/proof audit.

Construct the stable law from the actual response sums and characteristic
limit exp(-E|tW+s|), using finite-dimensional characteristic tightness and
Prokhorov compactness. Mathlib Levy convergence is stated against an already
existing candidate probability measure; it does NOT directly construct a
measure from an arbitrary continuous candidate function. A tight subsequence,
its characteristic function, and uniqueness must therefore be supplied, or an
explicit stable-law construction must be formalized.

A useful simplification avoids the manuscript's continuous-density claim:
for each nonzero linear projection, the limiting characteristic function is
that of a nondegenerate Cauchy. Cauchy atomlessness then gives
P(B=0)=0 and P(A+rB=0)=0 for each real r. Thus ratio atoms vanish without
Fourier inversion for a two-dimensional density.

To prove full support of the ratio, retain the source's convex-support argument:
1-stability makes the planar support convex; every nonzero projection is a
nondegenerate Cauchy with full real support; a proper closed convex planar
support would be separated by a half-space. This is mathematically shorter
than building a smooth density theorem, but support-of-product/map and
separation bridges require new lemmas. The pinned Measure/Support.lean has
closedness, conullness and the neighborhood characterization; no ready-made
product/map-support equality was found in this search. Basic product-positive
open-set arguments can prove the specific bridges directly.

## Recommended order of the next frozen boundaries

1. Actual Cauchy-triple variance function and its full-support-law application.
   This directly discharges all generic-V assumptions of the completed mixture
   theorem once ratio support/zero mass are available.
2. Exact Cauchy characteristic function and finite response-law reduction,
   E W^2=2, fractional moment, and cosine error estimate (manuscript Eq.14).
3. Stable sum law existence/convergence; projection Cauchy laws; ratio atomlessness
   and full support. Avoid proving planar density unless a later use requires it.
4. Deterministic signed-threshold fourth/sixth maximal bounds and finite-grid
   oscillation. These can proceed independently once the phase/sign law is fixed.
5. Finite-grid mixed characteristic expansion on original joint module data;
   scalar random-evaluation limit by characteristic-function approximation;
   uniform integrability and second/fourth moment convergence.
6. Apply the separately formalized prescribed-length contamination estimates
   and normalizations. The spectral graph-to-module bridge still has to be
   constructed and proved; probability progress does not cover that gap.

This is a roadmap, not a claim these new blocks have been proved. The existing
11-target package removes real algebra, Gaussian-mixture and contamination
connections; it still cannot be advertised as an end-to-end Lean proof of the
quantum-graph counterexample.
