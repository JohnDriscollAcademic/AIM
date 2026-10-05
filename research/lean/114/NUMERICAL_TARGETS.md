# AIM 114: exact boundary of a partial formalization

## Frozen sources and credit

- AIM ID: **114**; canonical page: `problems/114-quantum-graph-nodal-clt.md`.
- Repository source commit: `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.
- Complete source problem snapshot: `../../solutions/114-nodal-surplus-counterexample/statement.md`.
- Complete informal argument: `../../solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf`, revised v0.3, 2026-10-02, six pages.
- PDF SHA-256: `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.
- Mathematical author: **Sidney Holden**, supplied by the user. Formalization implementation: Codex for Sidney Holden (AI assisted).
- Scope is **partial**. None of these three theorems resolves AIM 114 or establishes its advertised non-Gaussian limit.

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
Cj = sqrt(1+Xj^2), and independent standard Cauchy Xj. These graph,
distributional, and limiting objects are currently **not defined in Lean**.

## The complete advertised Lean target list

There are exactly three advertised results; `comparator.json` must list all
three. All numbers and computations use exact real arithmetic. No numerical
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
representation, and the zero probability of excluded boundaries remain
informal.

### 3. `AIM.P114.variance_mixture_kurtosis`

For every measurable space Omega, every probability measure mu on it, and
every real function V with V and V^2 Bochner integrable, write a=integral V.
Assume a>0 and integral (V-a)^2 > 0. Prove

    3 < 3 * integral(V^2) / a^2.

This uses actual integrals and expands the centered second moment on a
probability space. The positive mean makes division legitimate. Neither
0<V<1/2 nor a particular Cauchy-derived V is required for this general
inequality. The factor 3 is the exact standard-normal fourth moment, but this
theorem **does not** construct a Gaussian random variable, prove mixture
moment identities, establish nonconstancy of the manuscript's V, or prove
non-Gaussianity of its standardized limit. Those connections remain explicit
formalization gaps. In particular the positive-variance hypothesis is not
claimed to have been discharged for the graph construction.

## Unformalized links to the source target

1. Prime-root rational independence, graph construction, the Kirchhoff
   operator, generic spectral-frequency laws, and the published edge-mixture
   measure theorem.
2. Edge nodal counting, spectral counting by inertia, Schur complements,
   genericity/null exceptional sets, and the full exact surplus reduction.
3. Cauchy-phase transformations, E W^2=2, the stable vector law and its density,
   full support, ratio convergence and the nonconstancy of v(R).
4. Empirical-process tightness, functional CLT, moment/tail bounds, and
   independence of the Gaussian process and stable vector.
5. Random evaluation, Gaussian-mixture distribution and moments, transfer
   from the pendant edge law to actual lengths, and standardized limit.

Theorems here must never be substituted for these missing links or advertised
as a Lean proof of the counterexample. The frozen Challenge contains deliberate
placeholders; only its signatures are trusted by Comparator. Solution must
not import Challenge. Two independent boundary approvals and type-checking
must precede any proof implementation. Changes to these mathematical bytes
reopen boundary review.
