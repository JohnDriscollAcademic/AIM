# PR33 / AIM 114: fresh independent spectral referee audit

Date: 2026-10-05. Reviewer: a fresh OpenAI Codex AI referee agent with no role in preparing this submission, its expanded proof, its previous reviews, or its Lean package. This is an AI mathematical audit, not human peer review or a proof-assistant verification.

Review target: `problems/114-quantum-graph-nodal-clt.md`, PR33, immutable head `61916d1e9959dc7ed282edb124b51e8118735844`. Comparison main: `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. The original target asks two questions: a universal standardized Gaussian limit, and universal upper and lower variance bounds proportional to cycle rank.

## Verdict

**No blocking mathematical defect found.** The graph construction is admissible, the spectral-to-independent-phase reduction is supported by the cited primary results with the correct hypotheses and normalization, and the exact surplus identity is correct. I independently checked the subsequent argument for coherence, including the stable ratio, process/stable joint convergence, evaluation at the endogenous ratio, moment transfer, and non-Gaussianity. On these checks the submitted v0.3 proof supplies a valid counterexample to the unrestricted Gaussian assertion.

**PARTIAL is the appropriate catalogue status.** The exhibited graphs have variance asymptotic to a positive constant times cycle rank. They neither disprove nor prove universal linear variance bounds for other graph sequences. No conclusion follows for bounded-degree or comparable-length variants. The proof takes the spectral-frequency limit for each fixed graph before increasing graph size, as the target requires.

The verdict rests on the original manuscript, direct mathematical derivations, and the primary papers identified below. Previous AI reports, preparation claims, Lean logs, and existing algebra-check output were not used as evidence.

## Exact sources and checks performed

I read the full six-page submitted PDF, extracted all pages, visually inspected rendered images of all six pages, read all of `PROOF.md`, compared the original main problem with the PR target and frozen statement, and checked the cited results in the original arXiv versions through the web tool. PDF and Markdown contain the same construction, exact formula, and limiting argument. The PDF additionally states the optional length-contamination rates discussed below.

SHA-256 values below are computed from exact immutable Git blob bytes, using `git show` captured as bytes. The Windows snapshot normalizes Markdown newlines to CRLF, so its Markdown hashes differ; this is an export effect. The PDF bytes agree exactly.

| Exact Git source | SHA-256 |
| --- | --- |
| PR target `problems/114-quantum-graph-nodal-clt.md` | `5b3ad1e6be7b71f4ebadf7cd84c5eed27c25e6937ba9fa3ec980c2b898a1d869` |
| Frozen `research/solutions/114-nodal-surplus-counterexample/statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| `research/solutions/114-nodal-surplus-counterexample/PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |
| `research/solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf` | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |

The frozen statement equals the main target byte-for-byte. All proof line references below refer to `PROOF.md` at this head; PDF references use printed page numbers and equation numbers.

## Primary imported results: hypotheses and normalization

The primary spectral source is [Alon, Band and Berkolaiko, arXiv:2106.06096v2](https://arxiv.org/html/2106.06096v2). Its Assumptions 1–2 permit parallel edges and require a finite connected graph without degree-two vertices, with the Kirchhoff Laplacian. Proposition 6.1 defines normalized generic edge laws and weights them by `ell_e c_e`, where `c_e=2` for every nonloop edge. Thus the manuscript's weights are precisely `ell_e/sum ell_f`. Equation (6.7) supplies each edge law's symmetry. Lemma 6.7 says that projection omitting the selected edge pushes its normalized generic measure to uniform measure on the remaining torus. Definition 2.2 uses the same genericity convention as AIM 114. Theorem 5.4 identifies the phase surplus with the metric surplus for any positive phase lift and makes its level sets admissible for spectral averaging. All these hypotheses hold here; no comparison of lengths or bound on degrees is required.

[Alon, Band and Berkolaiko, arXiv:1709.10413v2, Theorem 2.1](https://arxiv.org/html/1709.10413v2) applies to nontrivial standard graphs with rationally independent lengths. It gives the limiting law among generic indices, its support in `{0,...,beta}`, and its reflection symmetry. This graph is nontrivial and has Neumann conditions at its pendant endpoint.

The non-spectral import is [Marckert, arXiv:0710.3296v2, Theorem 1](https://arxiv.org/html/0710.3296v2): the uniform empirical process converges to a continuous Brownian bridge in Skorokhod topology. The marked threshold processes here reduce to that case by a continuous CDF time change on each compact finite interval; their atom at infinity does not invalidate this local application.

These results were checked in the original primary papers, rather than inferred from the repository's prior reports. The surplus/inertia calculation below is also independently justified directly; it does not require assuming an unquoted nodal-magnetic theorem.

## 1. Graph, operator, and prescribed lengths

Locations: proof lines 11–15; PDF page 1, equation (1).

There are `m+3` distinct vertices and `3m+1` edges. Each `w_i` has two edges to `u` and one to `v`; `u` also has the edge to `t`. All endpoints of an edge are distinct, so parallel pairs are not loops. Every vertex is connected to `u` through one of these edges or paths. Hence

`beta = (3m+1) - (m+3) + 1 = 2m-1`.

The degree list `(2m+1,m,3,...,3,1)` is correct. For `m>=3`, there is no degree-two vertex. The leaf at `t` imposes a Neumann endpoint condition under Kirchhoff conditions. Finiteness and positive finite edge lengths make each individual graph compact, even though its pendant length grows with `m`. AIM 114 has no uniform bound on lengths or degrees.

Distinct primes have independent square classes over the rationals: a product of a nonempty subset cannot be a rational square, by its prime valuations. Consequently the multiquadratic field admits an automorphism reversing any selected root and fixing the others. Applying that automorphism to a rational linear relation and subtracting isolates its selected coefficient. Multiplying the last root by the nonzero integer `m^6` preserves the linear independence. Thus all prescribed lengths are jointly rationally independent. Growing odd cycle ranks form a legitimate sequence under the universal quantifier.

## 2. Why the core phases are independent

Locations: proof lines 19–25; PDF page 2, equation (6).

The normalization of the generic edge measure matters: the proof uses the restriction to the generic secular set divided by its mass. Dropping the pendant coordinate under that measure gives exactly uniform product measure on `T^(3m)`. Therefore module triples are independent and identically distributed, and the three phases within each triple are independent uniforms.

This conclusion concerns the selected pendant-edge component of the limiting spectral law. It is not a claim that phases sampled at unweighted eigenvalues are independently uniform. The full law is recovered by the stated convex combination of edge laws. The forthcoming formula has the same value at both pendant completions, which removes any need to guess their conditional weights.

The Kirchhoff graph is loop-free, so there is no loop-state correction to either the mixing weights or generic normalization. The published genericity definition asks for simplicity and nonzero vertex values, precisely the condition established below.

## 3. Direct nodal count and quadratic-form index calculation

Locations: proof lines 55–68; PDF page 2, equation (10).

For an edge of length `L`, prescribe endpoint values `F_a,F_b`. If `sin(kL)!=0`, its Helmholtz extension is

`f(x) = [F_a sin(k(L-x)) + F_b sin(kx)] / sin(kL)`.

The outgoing derivative vector is `k` times the edge matrix in the proof. Its sign convention is therefore correct. Counting crossings of a sinusoid on an interval with nonzero endpoints gives

`floor(kL/pi) + 1{F_a F_b csc(kL)<0}`

interior zeros. This also checks the parity change when `sin(kL)` is negative. Summing gives `D+Q`.

On the form domain of continuous edgewise `H^1` functions, let `H_D` consist of functions vanishing at all vertices. Every function splits uniquely as a member of `H_D` plus the above Helmholtz extension of its vertex data. Integration by parts makes these spaces orthogonal for

`q_k[f] = sum_e integral (|f'|^2 - k^2 |f|^2)`.

The negative index on `H_D` is the sum of the counts of Dirichlet edge eigenvalues below `k^2`, namely `D`. No edge Dirichlet eigenvalue is at `k^2` because its sine is nonzero. The extension form is `-k F^T M F`, so its negative index is `n_+(M)`, not `n_-(M)`. At a simple eigenvalue `lambda_n=k^2>0`, the full negative index is exactly `n-1`, even though the form has one zero direction. This proves

`n-1=D+n_+(M)`, and consequently `s=Q-n_+(M)`.

If `F_u!=0`, replacing coordinate vector `e_u` by the kernel vector `F` is an invertible change of basis. Since `MF=0`, congruence gives `0 direct-sum M_without_u`, proving the final equality in (10). This is a valid infinite-dimensional form argument with a finite-dimensional complement; it is not a heuristic reading of secular matrix eigenvalues as Laplacian eigenvalues.

The single zero Laplacian eigenvalue is omitted in this calculation. Its contribution is one index and hence disappears from the spectral-frequency limit. At a generic secular point, choose positive lengths congruent to the phases and `k=1`. The same calculation shows that `Q-n_+(M)` computes its surplus and depends only on those phases, so moving between positive lifts does not alter it.

## 4. Core Schur complement and pendant completions

Locations: proof lines 70–81; PDF pages 2–3, equations (7)–(10).

Before adding the pendant, eliminate the diagonal module entries `-a_i`. The resulting core matrix on `(u,v)` is exactly

```
[ Lambda_m  U_m ]
[ U_m       T_m ]
```

because each elimination adds `p_i^2/a_i`, `p_i q_i/a_i`, and `q_i^2/a_i` to the respective entries. Normalizing `F_u=1` gives `F_v=r=-U_m/T_m` and `F_wi=(p_i+r q_i)/a_i`, with the signs in the manuscript.

On a Neumann pendant, `f(x)=cos(theta_0-x)/cos(theta_0)` at `k=1`. Its response at `u` is `tan(theta_0)`, and `F_t=1/cos(theta_0)`. The remaining equation at `u` is therefore

`Lambda_m-U_m^2/T_m+tan(theta_0)=0`.

Thus `tan(theta_0)=-g_m`. When `g_m` is finite and nonzero there are exactly two solutions modulo `2pi`, both with nonzero sine and cosine. Removing `u` disconnects the pendant vertex; eliminating the module vertices gives diagonal pivots

`-a_1,...,-a_m,T_m,-cot(theta_0)`.

All are nonzero on the specified set. This shows that `M_without_u` is invertible, while the full matrix has the explicitly constructed nonzero kernel, so that kernel is exactly one-dimensional. Nonzero edge sines make the correspondence between vertex data and edge solutions bijective; hence the corresponding Laplacian eigenvalue is simple. Every vertex value is nonzero by `U_m,T_m!=0`, `p_i+R_m q_i!=0`, and `cos(theta_0)!=0`.

The pendant contributes to `Q` the indicator that `1/[sin(theta_0)cos(theta_0)]<0`, which is `1{tan(theta_0)<0}`. Its positive-inertia pivot contributes exactly the same indicator because `-cot(theta_0)>0` is equivalent. They cancel at both completions. This checks the potential half-period sign ambiguity: the endpoint value changes sign between completions, but the surplus does not.

For each module put `sigma=sgn(a)` and `z=sgn(p+r q)`. Its three sign counts are

`[3-sigma*z*(sgn(c_1)+sgn(c_2)+sgn(r q))]/2`.

Subtracting its positive pivot count `1{a<0}=(1-sigma)/2` gives exactly `1+h_i(r)`. Subtracting the final core pivot `1{T_m>0}` and centering at `(2m-1)/2` yields the asserted identity

`S_tilde_m-beta_m/2 = sum_i h_i(R_m) - sgn(T_m)/2`.

## 5. Exceptional sets and all completion endpoints

Locations: proof lines 77–81 and 171; PDF page 3, proof of Lemma 1.

Each listed condition is a rational expression in the sines and cosines of finitely many phases. Clearing denominators makes its zero equation a trigonometric-polynomial equation. The common witness with every core phase equal to `pi/4` has

`a_i=3`, `U_m=4m/3`, `T_m=-m/3`, `R_m=4`, `p_i+R_m q_i=6sqrt(2)`, `Lambda_m=2m/3`, `g_m=6m`.

Every denominator is nonzero there and each asserted numerator is nonzero. A nonzero real analytic trigonometric polynomial has a Lebesgue-null zero set. A finite union therefore excludes all edge sine zeros, `a_i=0`, `U_m=0`, `T_m=0`, vanishing `w_i` values, and `g_m=0`. This proves the required null assertion rather than assuming typical genericity suffices for this parameterization.

Additional endpoints deserve explicit consideration. With the core phases fixed off this exceptional set, an eigenfunction with `F_u=0` would force all other core vertex values to vanish because the deleted core matrix has pivots `-a_i,T_m`. All core edge functions then vanish because their sines are nonzero. Kirchhoff at `u` forces the pendant derivative there to vanish as well as its value, so the pendant solution vanishes identically. Thus there is no such eigenfunction for any pendant phase, including phases at which its sine or cosine vanishes.

For `F_u!=0`, a Neumann pendant with `cos(theta_0)=0` is impossible. At `sin(theta_0)=0`, its response is zero, so the core would require `g_m=0`, already excluded. These arguments rule out extra singular completions that the tangent equation might otherwise miss. The two finite nonzero tangent completions exhaust the fiber.

Evaluation of `h_i` at `R_m` avoids its potential jump because a jump requires `p_i+R_m q_i=0`, one of the excluded equations. Finite limiting ratios avoid zero and infinity almost surely as checked below. Possible events `p_i=0` have probability zero by the continuous independent cosecant magnitudes; alternatively such a module has no interior half-line jump. None of these endpoints creates a missing positive-measure component.

## 6. Independent checks of the rest of the argument

Locations: proof lines 85–214; PDF pages 3–5, equations (11)–(20).

The involution reversing all three cotangents while keeping all three cosecants fixed makes `sgn(a)` a conditionally fair sign. Thus it is independent of the entire cosecant triple. It follows that each deterministic-argument `h(r)` is centered. The effective signs are either all equal, giving `h/sigma=-1`, or mixed, giving 0 or 1. Hence `|h|<=1`.

I checked the eight effective sign choices in the variance computation: outside the strict triangle interval the conditional square mean is `1/2`, and inside it is `1/4`. This gives equation (2). For every finite nonzero `r`, both the triangle event and its complement contain open sets in the support of the three magnitudes. Their probabilities are strictly between zero and one. Boundary equalities are null, which proves continuity by dominated convergence. The endpoint limits at zero and infinity equal `1/2`; since the finite values are strictly smaller, `v` is nonconstant.

The change of variable `phi=theta_3-arctan(x_1+x_2)` gives the two response coordinates exactly. Conditional uniformity of `phi`, independence of its tangent and cosine sign, and symmetry of `W` give the claimed marginal vector representation. The integral for `E W^2=2` is justified by nonnegative integrands and the change of variables `z=x+y`. It yields the finite `3/4`-moment of the response. The cosine inequality follows from the derivative bound of `cos(sqrt(y))`, including its continuous derivative limit at zero. Symmetry then replaces the characteristic function by `E exp(-|tW+s|/m)` with an error bounded by `t^2 E W^2/(2m^2)`. Taylor's estimate has an integrable second-order bound. Taking powers establishes the stated stable vector with no centering term.

For a nonzero `(t,s)`, `E|tW+s|>0`: otherwise `W` would be a constant when `t!=0`; for `t=0` it is `|s|`. Continuity and compactness on the unit circle give the positive uniform lower bound. The integrable characteristic function therefore gives a continuous density. Stability under weighted sums of independent copies makes the closed support convex. A proper closed convex support would lie in a half-space, contradicted by the full support of each nondegenerate Cauchy projection. The planar support is full. Its density makes all lines null, proving that `R=-A/B` is finite, nonzero, and atomless. Its full support follows by taking an open rectangle around any point with a prescribed finite nonzero denominator. Continuity and nonconstancy of `v` therefore give `Var(v(R))>0`.

The half-line process representation has at most one jump, of size at most one after removing `sigma`. Marking positive and negative jumps gives ordinary empirical CDF processes. Their CDFs are continuous at finite thresholds, and marginal tightness plus the multivariate bounded CLT suffices for joint process convergence; independence of these marked processes is not needed. On a compact interval a continuous limiting path makes evaluation continuous in Skorokhod topology.

The uniform tail bound conditions only on the cosecants. Threshold ordering then depends only on these conditioned values, leaving independent fair module signs. The baseline and ordered jump partial sums satisfy the exponential maximal bound, and the union over both sums and both half-lines gives `8 exp(-x^2/8)`. This legitimately controls an endogenous evaluation by the supremum, without asserting a false finite-m conditional independence between `R_m` and `h_i`.

Finally, the actual one-module joint characteristic function is used. For bounded centered `H`, the mixed linear term is `O(m^(-1/2) m^(-3/4))=o(1/m)`, and the quadratic term converges by dominated convergence. This proves product finite-dimensional limiting characteristic functions. Together with joint tightness and a countable set of evaluations determining continuous paths, it proves independence of the Gaussian process and the stable vector. Localizing the ratio to `1/L<=|R_m|<=L` is valid because the limiting ratio has no zero or infinite mass. The localized continuous mapping theorem and then `L->infinity` give the Gaussian variance mixture. No use of the marginal response representation as an independent replacement of the joint `(h,xi)` law occurs.

## 7. Spectral contamination, moments, and standardization

Locations: proof lines 218–255; PDF page 6.

Write `L_core=sum_(j<=3m) sqrt(p_j)` and `L_0=m^6 sqrt(p_(3m+1))`. Since each core prime root is smaller than the last root,

`L_core < 3m sqrt(p_(3m+1))`, so `omega_m=L_core/(L_core+L_0) <= 3/(m^5+3)`.

The spectral law is exactly `(1-omega_m) law(S_tilde_m)+omega_m Rcal_m`. All its component laws are supported in `[0,beta_m]` and centered at `beta_m/2`. For the `sqrt(m)`-scaled centered variables, the difference of the second or fourth absolute moments is bounded by

`omega_m [beta_m/(2sqrt(m))]^p = O(m^(p/2-5))`, for `p=2,4`.

The bound needs no factor two: both component expectations lie between zero and this maximum. It tends to zero at rates at least `m^-4` and `m^-3`, respectively. Total variation alone would not justify moment transfer on a growing support, but this explicit bound does. The auxiliary tail bound supplies uniform integrability of its moments. Symmetry supplies the exact common center.

Consequently `Var(S_m)/m -> a_*=E v(R)`, with `1/4<a_*<1/2`. Since `beta_m/m->2`, the variance/cycle-rank ratio tends to `a_*/2` in `(1/8,1/4)`. Slutsky standardization is valid because `a_*>0`. The normalized variance mixture has fourth moment `3E[V^2]/(EV)^2>3`; more directly, strict Jensen gives its characteristic function strictly larger than the standard Gaussian characteristic function at every nonzero argument. Thus the limit is not Gaussian. This is an actual weak-limit obstruction, rather than a fourth-moment discrepancy unsupported by uniform integrability.

The optional PDF page 6 generalizations are also consistent: `omega_m->0` suffices for weak convergence on the `sqrt(m)` scale; `m omega_m->0` suffices for variance and standardized weak convergence; `m^2 omega_m->0` suffices for the fourth moment. These follow from the same growing-support bound.

## 8. Independent finite regression evidence and limits of this audit

I ran a new inline Python calculation with exact `Fraction` arithmetic, independently of the submitted check script. It parameterized each core phase by rational `z=tan(theta/2)`, using `cot(theta)=(1-z^2)/(2z)` and `csc(theta)=(1+z^2)/(2z)`. Seed: 11433. Across 1,000 proposed examples for `m=3,4,7,12`, 17 lay on excluded equations and 983 nonexceptional examples passed. The checks assembled and symmetrically eliminated the deleted core matrix, checked its exact pivots, checked all reconstructed core vertex equations, derived `g_m` from the `u` equation, checked the sign-count identity and total surplus formula, and checked integer surplus in `[0,2m-1]`. A separate exact enumeration checked all eight effective sign patterns in each of 296 nonboundary magnitude/ratio cases; every conditional variance formula passed.

These computations are regression evidence only. The continuum null-set assertion, form-index argument, sampling measure, and limiting laws are justified by the preceding mathematics and primary results; no finite computation or Lean log was substituted for them.

At the maintainer's subsequent request, I recovered both calculations from their original inline tool calls and preserved them in the [portable independent script](scratch/pr33-spectral-independent-checks.py). Only function boundaries and a JSON-output wrapper were added; the wrapper also guards against `-O` disabling the original assertions and checks the expected totals. No phase sampling, arithmetic, exclusion condition, or mathematical check changed. The separate snapshot-file validation from the second inline call was omitted because it was not part of the regression calculation. One reproduction with Python 3.12.14 exited successfully on 2026-10-05 at 21:18:13 UTC and again produced 983 passed graph examples, 17 exclusions, and 296 cases with eight sign patterns each. Its [actual JSON result](scratch/pr33-spectral-independent-checks.json) records the run. There is no difference in the regression findings or report verdict. The script uses only Python's standard library and reads no submission or snapshot file.

A bounded fresh literature search on 2026-10-05 found the current primary survey [Berkolaiko and Gnutzmann, arXiv:2604.12690v2, Section 4.3, Conjecture 4.1](https://arxiv.org/html/2604.12690v2), dated 2026-05-06, still stating the universal Gaussian and linear-variance assertions and reporting no known counterexample at that time. Searches for quantum-graph nodal-surplus variance counterexamples, Holden's non-Gaussian limit, and 2026 universality/variance results did not locate a separate resolution of the variance assertion. This is a bounded literature snapshot, not a proof of openness or priority.

No source repair is required for the mathematical conclusion at the reviewed head. For exposition, the expanded proof could state the direct-sum form domain explicitly at line 68 and explicitly mention the sine-zero/cosine-zero pendant cases at line 79; the submitted argument already contains the ingredients that settle them. These are optional clarifications, not blocking gaps.

All repository and GitHub operations in this review were read-only. The persistent review deliverables are this separate report and the subsequently requested independent regression script and JSON result, all outside the PR snapshot.
