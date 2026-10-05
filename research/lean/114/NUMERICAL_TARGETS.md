# AIM 114: exact boundary of a partial formalization

## Frozen sources and credit

- AIM ID: **114**; canonical page: `problems/114-quantum-graph-nodal-clt.md`.
- Repository source commit: `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.
- Complete source problem snapshot: `../../solutions/114-nodal-surplus-counterexample/statement.md`.
- Complete informal argument: `../../solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf`, revised v0.3, 2026-10-02, six pages.
- PDF SHA-256: `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.
- Mathematical author: **Sidney Holden**, supplied by the user. Formalization implementation: Codex for Sidney Holden (AI assisted).
- Scope is **partial**. The combined package contains the initial three algebraic results, five prescribed-length transfer results, three actual Gaussian-mixture results, two actual finite core inertia results, five actual Cauchy-variance results, seven actual multigraph results, three actual edge-length admissibility results, and three actual graph length-sum/weight results (31 declarations total). They do not establish the graph's convergence to that mixture or resolve AIM 114 in Lean.

## Original target, preserved without weakening

For every sequence of finite connected compact metric graphs with positive
rationally independent lengths and cycle rank tending to infinity, does the
standardized spectral-frequency nodal-surplus law converge to the standard
normal, and do universal positive constants bound its variance above and below
by the cycle rank? The proposed counterexample addresses the unrestricted
Gaussian assertion only. It does not refute the universal variance assertion.
The spectral-frequency limit comes before the graph-size limit.

The manuscript uses m >= 3, m modules of two parallel edges u--w_i and one
edge w_i--v, and a pendant u--t. Thus beta_m = 2m-1. Core length j is sqrt(p_j),
1 <= j <= 3m; pendant length is m^6 sqrt(p_(3m+1)). The limiting mixing
variance is v(R), with v(r) = 1/2 - P(|C1-C2| < |r|C3 < C1+C2)/4,
Cj = sqrt(1+Xj^2), and independent standard Cauchy Xj. The finite multigraph, prescribed length formulas, actual Cauchy variance
function, and Gaussian-mixture law are now defined in Lean. The metric graph
operator, stable ratio law R, and spectral/process limiting objects are not.

## The initial three algebraic results

This initial block has exactly three results. The additional reviewed blocks
are listed below; `comparator.json` must list every result from all blocks.
All numbers and computations use exact real arithmetic. No numerical
certificate, rounding tolerance, sample, truncation, or asymptotic estimate
is used in these three results.

### 1. `AIM.P114.module_count_identity`

For all reals a,x,y,z with a,x,y,z,x+y+z nonzero, let F=(x+y+z)/a.
The result is

    1{xF<0} + 1{yF<0} + 1{zF<0} - 1{a<0}
      = 1 + sign(a) (1 - sign(x+y+z)(sign(x)+sign(y)+sign(z)))/2.

The correspondence is a=x_1+x_2+x_3, x=c_1, y=c_2, z=r*c_3 in
manuscript Eq. (8). This is the local three-edge sign-count/pivot identity in
Lemma 1, not the spectral or global inertia identity (9)/(10). Variables are
arbitrary real numbers, a valid generalization of the phase-derived variables.
The real-valued indicator is for **strict** negativity. `nonzeroSign` extends
sign by +1 at zero solely to simplify definitions; all arguments to sign in
this result are explicitly nonzero.

### 2. `AIM.P114.sign_second_moment`

For every x,y,z > 0 such that z != x+y and z != |x-y|, define

g(x,y,z)=(1-sign(x+y+z)(sign(x)+sign(y)+sign(z)))/2.
Then the equally weighted four-sign average

    [g(x,y,z)^2 + g(-x,y,z)^2 + g(x,-y,z)^2 + g(-x,-y,z)^2]/4
       = 1/2 - 1{|x-y|<z and z<x+y}/4.

The four terms fix the third effective sign positive. Global sign reversal
leaves g unchanged when its four sign arguments are nonzero; no probabilistic
symmetry theorem is claimed by this finite average. The stated hypotheses
exclude zero signed sums and both degenerate triangle endpoints. In the
manuscript, x=C1, y=C2, z=|r|C3. This proves the exact finite sign calculation
behind v(r). The fair-sign law, the independence of sign(a), the Cauchy
representation remain informal. The actual Cauchy variance extension below now proves
that its triangle boundaries have probability zero.

### 3. `AIM.P114.variance_mixture_kurtosis`

For every measurable space Omega, every probability measure mu on it, and
every real function V with V and V^2 Bochner integrable, write a=integral V.
Assume a>0 and integral (V-a)^2 > 0. Prove

    3 < 3 * integral(V^2) / a^2.

This uses actual integrals and expands the centered second moment on a
probability space. The positive mean makes division legitimate. Neither
0<V<1/2 nor a particular Cauchy-derived V is required for this general
inequality. The factor 3 is the exact standard-normal fourth moment, but this
theorem by itself does not construct a Gaussian random variable or prove its
moment identities. The actual mixture block below now supplies those results
and law nonequality for an abstract bounded nonconstant mixing variable.
The actual-variance extension below discharges the function hypotheses for
v under any full-support law with no atom at zero. The graph's particular
stable ratio law remains unconstructed.

## Prescribed-length transfer extension

The exact definitions, five signatures, and independently reviewed source
correspondence are frozen in [TRANSFER_TARGETS.md](TRANSFER_TARGETS.md) and
[TransferChallenge.lean](TransferChallenge.lean). They prove the explicit
prime-root core fraction bound, probability status of the genuine convex
mixture, a bounded-observable estimate, and convergence to zero of the actual
standardized second/fourth-moment contamination errors. The spectral
identification of the input laws remains outside this extension.

## Actual Gaussian-mixture extension

The exact definition and three signatures are frozen in
[MIXTURE_TARGETS.md](MIXTURE_TARGETS.md) and
[MixtureChallenge.lean](MixtureChallenge.lean). They construct the pushforward
of an actual product probability space, prove its first/second/fourth
integrability and moments, and prove it differs from the standard Gaussian
when the bounded positive mixing variable is not almost everywhere constant.
No mixture moment or positive variance formula is assumed. Identification
of the graph's particular mixing variable and convergence to the law remain
outside this extension.

## Finite core inertia extension

The two exact signatures in [InertiaChallenge.lean](InertiaChallenge.lean) and
[INERTIA_TARGETS.md](INERTIA_TARGETS.md) prove completing the actual core
quadratic form by an explicit linear equivalence and counting its actual
Mathlib positive index. The full graph matrix, pendant coordinate, and
spectral interpretation are still separate obligations.

## Actual Cauchy-variance extension

The five exact signatures in [VarianceChallenge.lean](VarianceChallenge.lean)
and [VARIANCE_TARGETS.md](VARIANCE_TARGETS.md) fix the variance function to the
source's strict triangle-event probability under three actual independent
standard Cauchy measures. The proofs establish its value at zero, strict
bounds off zero, continuity on the entire real line, and the mixture inputs
under any full-support real probability law with no atom at zero. Applying
the proved mixture theorem gives an actual non-Gaussian law for this fixed
variance function. No regularity or nonconstancy of v is assumed. The stable
ratio law itself and its connection to the graph limit remain missing.

## Actual finite multigraph extension

The seven exact signatures in [GraphChallenge.lean](GraphChallenge.lean) and
[GRAPH_TARGETS.md](GRAPH_TARGETS.md) establish looplessness, connectivity for
m>=1, the actual vertex and edge cardinalities, retention of parallel edge
identifiers, exact incident-edge counts, no degree two for m>=3, and the
integer Euler expression 2m-1. The graph is an actual Mathlib multigraph;
only connectivity uses the underlying simple graph. The Euler theorem does
not identify a homology or cycle-space dimension. Metric realization and
spectral interpretation are separate obligations.

## Actual edge-length admissibility extension

The three exact signatures in [LengthChallenge.lean](LengthChallenge.lean)
and [LENGTH_TARGETS.md](LENGTH_TARGETS.md) prove full joint rational independence
of the entire sequence of prime square roots, strict positivity of every
actual graph edge length for m>=3, and joint independence after the pendant's
prescribed rational scaling. The definition attaches those lengths to the
actual multigraph edge IDs, including both parallel edges. The proof uses
constructed sign characters and Dedekind independence, with distinctness
proved from prime arithmetic and the Galois fixed-field theorem.

## Actual graph length-sum and weight bridge

The three exact signatures in
[GraphLengthBridgeChallenge.lean](GraphLengthBridgeChallenge.lean) and
[GRAPH_LENGTH_BRIDGE_TARGETS.md](GRAPH_LENGTH_BRIDGE_TARGETS.md) prove that
the actual assigned core-edge sum equals coreLength, the actual total equals
coreLength plus pendantLength, and their actual ratio satisfies the prescribed
core-weight bound. These exact finite sums preserve all parallel-edge IDs.
They connect the graph/length and transfer blocks without assuming a sum
identity or an abstract graph fraction.

## Unformalized links to the source target

1. Metric realization of the actual graph with its now-proved positive
   independent lengths, the Kirchhoff operator, generic spectral-frequency laws, and the published edge-mixture
   measure theorem.
2. Edge nodal counting, spectral counting by inertia, the full graph-matrix
   reduction beyond the proved finite core completion of squares,
   genericity/null exceptional sets, and the full exact surplus reduction.
3. Cauchy-phase transformations, E W^2=2, the stable vector law and its density,
   full support, zero-atom property, and ratio convergence. The concrete
   function v is now continuous and nonconstant, with strict bounds off zero;
   these conclusions give nonconstancy under any full-support ratio law.
4. Empirical-process tightness, functional CLT, moment/tail bounds, and
   independence of the Gaussian process and stable vector.
5. Random evaluation, identification of the actual stable ratio law and verification of its
   intrinsic full-support/zero-atom hypotheses, the spectral mixture
   equality needed to apply the proved moment-transfer calculation, and the
   standardized graph-surplus limit. The abstract mixture law and its moments
   and the conditional moment-error calculation are now formalized.

Theorems here must never be substituted for these missing links or advertised
as a Lean proof of the counterexample. The frozen Challenge contains deliberate
placeholders; only its signatures are trusted by Comparator. Solution must
not import Challenge. Two independent boundary approvals and type-checking
must precede any proof implementation. Changes to these mathematical bytes
reopen boundary review.
