# Independent AI probability audit of AIM114, manuscript v0.3

Reviewer: **probability_review, independent OpenAI Codex AI subagent**.
Date: **2026-10-05**.
Mathematical authorship: **Sidney Holden**, as supplied by the author in the submitting conversation; the submitted PDF itself has no author line.

**Verdict:** The probabilistic argument in Sections 3–5 passes this independent AI audit. I found no blocking mathematical defect in the stable limit, empirical-process argument, random evaluation, moment transfer, or non-Gaussian conclusion. This is a mathematical review, not a human referee report or a Lean verification. Its application to the actual graph surplus remains dependent on the spectral reduction in Section 2, which was outside this review's assigned primary scope.

The result disproves the unrestricted Gaussian assertion in AIM114. It does **not** decide the separate universal linear-variance assertion. The constructed sequence itself has asymptotically linear variance with a positive finite coefficient. Consequently this audit does not support a claim that both parts of the retained AIM114 target have been resolved.

## Evidence and independence

The reviewed manuscript is [the unchanged submitted v0.3 PDF](../submitted/short_proof-v0.3.pdf), titled *A non-Gaussian limit for nodal surplus*, dated October 2, 2026. Its SHA-256 is

```text
74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6
```

The repository base inspected was commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. At review time the canonical problem page `problems/114-quantum-graph-nodal-clt.md` had SHA-256

```text
ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f
```

I read the complete extracted manuscript, checked the rendered fifth page to disambiguate the characteristic-function expansion, read the repository contribution rules and original canonical target, and independently reconstructed the calculations below. The temporary extracted text had SHA-256 `2abdc98c549212a316521fc525f727210cbf02a2f085d91b883f801e4b767e6c`; it is a reading aid, not the authoritative submission. I did not rely on another AIM114 review, a numerical experiment, or a pre-existing PASS result to establish correctness. I made no changes to the manuscript or formal proof and did not run Lean.

After completing this audit I also inspected the expanded [PROOF.md](../PROOF.md), SHA-256 `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604`. Its sections beginning with “One-module variance and boundary law” faithfully preserve the reviewed probabilistic argument, constants, hypotheses, limiting order, and restricted conclusion. I found no probability-related discrepancy between that presentation and the submitted PDF.

I checked the cited original [Marckert, arXiv:0710.3296v2, Theorem 1 and Note 1](https://arxiv.org/html/0710.3296v2). The theorem gives convergence of the uniform empirical process in the Skorokhod space `D[0,1]`; the adjacent note discusses reduction of other distributions by cumulative-distribution time change. The manuscript's application requires continuity only at finite thresholds, which is established below.

I also checked [Alon–Band–Berkolaiko, arXiv:2106.06096v2, Conjecture 3.1, equations (3.1)–(3.5)](https://arxiv.org/html/2106.06096v2#S3). Its Gaussian assertion allows arbitrary rationally independent lengths, and its variance assertion has separate universal quantifiers. The unusually dominant pendant length therefore lies within the stated Gaussian target. This audit does not establish publication priority or constitute an exhaustive search for subsequent literature.

## One-module calculation and variance profile

The simultaneous transformation of the three phases by `theta_j -> pi - theta_j` preserves their product-uniform law and each cosecant, while reversing every cotangent and hence `a`. Since `a=0` has probability zero, `sigma=sgn(a)` is a fair sign independent of the complete cosecant triple. Independence of modules then makes all the `sigma_i` independent fair signs even after conditioning on all modules' cosecants. This is the conditional independence actually used in the maximal inequality; it does not assert that the boundary response is independent of the module function.

For fixed magnitudes `C_1,C_2,C_3` and `rho=|r|`, fixing the third effective sign positive leaves four equally likely sign patterns for the first two signs. The corresponding values of `g(r)^2` are the indicators of

1. the certain event;
2. `C_2 > C_1 + rho C_3`;
3. `C_1 > C_2 + rho C_3`;
4. `rho C_3 > C_1 + C_2`.

The second and third events combine into `rho C_3 < |C_1-C_2|`. This independently reproduces the stated conditional second moment, and therefore the formula for `v(r)`. It also verifies `|h(r)| <= 1` and `E h(r)=0`.

For each fixed finite nonzero `r`, the strict triangle event contains an open subset of `(1,infinity)^3`: take `C_1,C_2` equal and sufficiently large. Its complement also contains an open subset: take `C_3` sufficiently large relative to fixed `C_1,C_2`. The law gives both subsets positive probability. Boundary equalities have probability zero by conditioning on `C_1,C_2`, and dominated convergence yields continuity and both endpoint limits `v(r) -> 1/2`. Thus `1/4 < v(r) < 1/2`, and `v` is nonconstant.

## Boundary response and stable law

Writing `s_0=x_1+x_2` gives the exact algebraic identities

```math
\xi^{(2)}=\frac{1-s_0x_3}{s_0+x_3}
=\tan(\theta_3-\arctan s_0),\qquad
\xi^{(1)}=\frac{p}{\sqrt{1+s_0^2}}
\sec(\theta_3-\arctan s_0).
```

The shifted phase is uniform and independent of the first two phases. Its tangent is Cauchy and its cosine sign is an independent fair sign. The prefactor is symmetric, so multiplication by that additional sign preserves its law `W` and leaves it independent of the tangent. This proves the asserted marginal representation of the two-dimensional response.

Averaging the two independent numerator signs removes their cross term. Under the change of variables `z=x+y`, the second-moment integrand simplifies to

```math
\frac{1}{1+z^2}
\left(\frac{1}{1+x^2}+\frac{1}{1+(z-x)^2}\right).
```

Tonelli's theorem applies to this nonnegative expression; the inner integral is `2 pi` and the outer integral is `pi`. Including the factor `1/pi^2` gives `E W^2=2`. The finite `3/4` moment of the response follows from this finite second moment, independence, and the Cauchy fractional-moment bound.

For the characteristic expansion, symmetry of `W` first replaces its complex exponential by a cosine. The inequality in (14) has error at most `t^2 W^2/(2m^2)`. After taking expectations, replacing `sqrt(1+X^2)` by `X` therefore costs `O(m^-2)`. Conditional Cauchy integration gives the average of `exp(-|s+tW|/m)` and `exp(-|s-tW|/m)`; symmetry makes the two expectations equal. Finally,

```math
|e^{-u}-1+u|\le u^2/2\quad(u\ge0)
```

and `E|tW+s|^2 < infinity` prove the claimed remainder. This validates the absence of a centering term, an essential point for an index-one stable limit.

The function `psi(t,s)=E|tW+s|` is continuous and strictly positive away from zero: otherwise a nonzero affine function of the nonconstant `W` would vanish almost surely. Compactness of the unit circle gives a positive linear lower bound, making `exp(-psi)` integrable. Fourier inversion therefore supplies a continuous density. Stability makes the closed support convex: neighborhoods of any two support points have positive probability for two independent copies, so their convex combinations are again support points. A proper closed convex support lies on one side of a separating hyperplane, whereas every nonzero projection has a nondegenerate Cauchy distribution. Hence support is all of the plane.

The density gives zero probability to every line. In particular, the denominator and numerator of `R=-A/B` are nonzero almost surely, and every proposed atom of the ratio is contained in a null line. Full planar support gives full support for `R`. Continuity and nonconstancy of `v` then force `Var(v(R))>0`.

## Process tightness, independence, and random evaluation

On either fixed half-line, `p+r q` has at most one zero. When such a zero occurs, the effective signs are mixed, their sum is `+1` or `-1`, and `g` changes between zero and one. This proves the one-jump decomposition (16), with coefficients measurable from the cosecants alone. For a prescribed finite positive threshold, conditioning on `c_1,c_2` reduces its occurrence to a single value of the continuously distributed `c_3`, except for a null degeneracy. Marking a threshold by the sign of its jump cannot introduce a finite atom: the event for the marked threshold is a subset of the corresponding unmarked event.

For each of the four marked-threshold CDFs, its empirical process has the marginal law of a uniform empirical process composed with its deterministic CDF. On any compact interval inside `(0,infinity)`, this CDF is continuous. The quantile representation is valid even with the residual mass at infinity; after the transformation `x/(1+x)` that mass is confined to the endpoint 1. Marckert's theorem, continuous limiting paths, and continuous composition yield marginal tightness. Finite products of tight laws are tight without any independence assumption. Applying the ordinary multivariate CLT to the bounded module evaluations and baselines identifies their joint finite-dimensional laws. A nested countable exhaustion by compact intervals gives the claimed local process limit, with continuous paths on both half-lines and covariance `E h(r)h(s)`.

For clarity, the four limiting bridges need not be independent. The manuscript does not require them to be. Their joint dependence is retained by the modulewise multivariate CLT.

The mixed characteristic-function argument correctly uses the **original joint law** of `h` and `xi`. For each bounded centered finite linear combination `H`,

```math
\left|E\left[H(e^{i\zeta\cdot\xi/m}-1)\right]\right|
\le \|H\|_\infty O(m^{-3/4}).
```

After multiplication by `m^-1/2`, this is `O(m^-5/4)=o(m^-1)`. Expanding only the bounded `H` exponential, the quadratic coefficient tends to `E H^2` by dominated convergence; the third-order remainder is `O(m^-3/2)`. Thus the one-module characteristic function is

```math
1-\frac{\psi(\zeta)+E H^2/2}{m}+o(m^{-1}).
```

The minus sign applies to both terms, as confirmed in the rendered PDF. Raising to the `m`th power factors the stable and Gaussian limits. Joint tightness and a countable dense set of process evaluations establish independence of the entire continuous Gaussian process from `(A,B)`. This is not inferred from the marginal representation of `xi`.

Evaluation at the random ratio is legitimate. On a compact interval away from zero in either half-line, evaluation is continuous at a continuous limiting path under Skorokhod convergence. Since `R` is finite, nonzero, and atomless, localization to `L^-1 <= |R_m| <= L` loses arbitrarily little limiting probability as `L` increases; endpoint events can also be excluded. Consequently `G_m(R_m)` converges to `G(R)`. Conditional on `R`, independence gives a normal law with variance `v(R)`, establishing the variance-mixture description.

## Uniform moments and transfer to graph lengths

Conditional on all cosecants, both baseline and threshold-ordered jump sums have deterministic coefficients bounded by one and independent Rademacher signs. The exponential-supermartingale maximal bound is therefore applicable after ordering the thresholds. Bounding a supremum by one baseline magnitude and one maximum partial sum, splitting at `x/2`, and taking a union bound over two half-lines gives exactly the factor `8 exp(-x^2/8)` in (18). No independence between those four maxima is required. Right continuity permits restriction of the supremum to a countable dense set and ensures measurability.

The tail bound supplies every fixed moment uniformly, including moments strictly above four. The additional sign term in (9) is bounded by `1/(2 sqrt(m))`. Thus the second and fourth powers of the normalized pendant-edge surplus are uniformly integrable, justifying convergence of these moments, not merely convergence in distribution.

For the submitted lengths, each core prime square root is at most the pendant prime square root, so the core-length fraction is at most `3/(m^5+3)`. The centered normalized support has magnitude at most `beta_m/(2 sqrt(m))`. Because the actual law is a convex mixture with weight `omega_m`, the difference of its nonnegative `p`th absolute moment and the pendant-law moment is bounded by the mixture weight times the maximum possible moment. This gives `O(m^(p/2-5))`, tending to zero for both `p=2` and `p=4`. A total-variation estimate alone would not justify these growing-support moment conclusions; the manuscript includes the required support estimate.

The exact symmetry supplies the exact mean. Since `E V` is positive, Slutsky's theorem yields the stated variance normalization. Strict convexity of `v -> exp(-t^2 v/(2 E V))` for nonzero `t`, together with `Var(V)>0`, separates the limiting characteristic function from that of the standard normal. Independently, its fourth standardized moment is `3 E V^2/(E V)^2 > 3`. The claimed non-Gaussian limit and linear variance asymptotic follow.

## Issue disposition and limits

| Potential issue | Disposition |
|---|---|
| Hidden centering in a 1-stable limit | Resolved by the direct second-order characteristic estimate. |
| Replacement of the actual coupled module by an independent surrogate | Not used; the mixed expansion preserves the original joint law. |
| Atom at infinity invalidating Donsker | Harmless for the explicitly local topology; finite marked CDFs are continuous. |
| Dependence between four marked empirical processes | Retained through the multivariate CLT; independence is unnecessary for tightness. |
| Random evaluation at a discontinuity or near zero | Resolved by continuous limiting paths, ratio atomlessness, and localization. |
| Weak convergence insufficient for moments | Resolved by the uniform maximal tail bound and explicit mixture-support estimates. |
| Counterexample to the Gaussian assertion misreported as resolution of the variance assertion | Must remain explicitly separated in all status and theorem-to-target claims. |
| Full formal verification | Not established by this report; no Lean source or build was reviewed here. |

There are **no unresolved blocking findings within Sections 3–5**. The core unresolved dependency of this scoped report is the separately reviewed spectral-to-probability reduction, not an identified defect in it. A complete mathematical audit must combine this report with verification of the graph construction, generic secular completion, and cited edge-measure formula. The original universal linear-variance target remains outside the conclusion.
