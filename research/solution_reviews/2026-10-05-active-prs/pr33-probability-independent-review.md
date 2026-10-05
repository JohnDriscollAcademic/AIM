# PR 33 / AIM 114: independent probability and limit audit

Date: 2026-10-05. Reviewer: a fresh OpenAI Codex AI agent assigned the probability part of this review. This is an AI mathematical audit, not human peer review and not a formal verification of the graph theorem.

## Verdict and independence

**No blocking probability defect found at the pinned head.** I independently re-derived the stable vector limit, the intrinsic support and atom properties of its ratio, the process limit with its independence from the stable vector, the evaluation at the endogenous ratio, the uniform moment estimates, the contamination bounds, and normalization by the true centered variance. Subject to the spectral reduction audited separately, these arguments prove the advertised non-Gaussian counterexample to the unrestricted Gaussian assertion in AIM 114. The construction does not resolve the separate universal linear-variance assertion.

I read all of the expanded proof and all six pages of the unchanged submitted v0.3 PDF, inspected their mathematical content and rendered PDF pages, read the frozen problem and the current problem, and compared the latter with original main. I did **not** read the package's existing probability or spectral review reports, or use Lean results, Lean pass reports, numerical experiments, or previous approval conclusions as evidence in forming this verdict. The independently assigned spectral and formalization referees were not used to determine the probability verdict. The checked arguments are described below so this report can be assessed on its own.

## Pinned material and target

Repository: `C:/Users/MatthewColbrook/Documents/git_repos/AIM`.

| Item | Identity |
| --- | --- |
| PR head / `origin/pr-33` | `61916d1e9959dc7ed282edb124b51e8118735844` |
| Original main / `origin/main` used for comparison | `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88` |
| Expanded source | `research/solutions/114-nodal-surplus-counterexample/PROOF.md` |
| Source Git blob | `4a4cf26e804d3510efe77fa6b625eee5ed553ed0` |
| Source SHA-256 | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |
| Submitted source | `research/solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf` (six pages, dated 2026-10-02) |
| PDF Git blob | `146e91c657d4d386ebf4f8d1ed0192cb7574252a` |
| PDF SHA-256 | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Current target | `problems/114-quantum-graph-nodal-clt.md` |
| Target Git blob | `e0056afa785370bf4b667348fd580205a9ea6190` |
| Target SHA-256 | `5b3ad1e6be7b71f4ebadf7cd84c5eed27c25e6937ba9fa3ec980c2b898a1d869` |
| Frozen target | `research/solutions/114-nodal-surplus-counterexample/statement.md` |
| Frozen target SHA-256 | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |

All source and target SHA-256 identities above were independently computed from the exact binary output of `git show` at the pinned head, rather than from newline-converted exported Markdown files.

The current target preserves the original mathematical question: for every admissible graph sequence with cycle rank tending to infinity, does the surplus law, obtained by taking the spectral frequency limit for each fixed graph, become Gaussian after centering at half the cycle rank and division by its own standard deviation? It separately asks for universal linear variance bounds. The target contains no bounded-degree, comparable-length, simple-graph, or simultaneous spectral-window restriction. Parallel edges in the construction are therefore admissible. The status and supporting text change in this PR; the target's mathematical statement does not.

## 1. Integration with the spectral argument

For `m >= 3`, the graph has `3m+1` edges, `m+3` vertices, and cycle rank `2m-1`. It is finite, connected, loop-free, and has degrees `2m+1, m, 3, ..., 3, 1`, so no vertex has degree two. Every prescribed length is positive and finite. Independent sign changes of prime square roots prove their rational linear independence; multiplication of the last root by the nonzero integer `m^6` preserves it. These conditions match the spectral inputs' stated graph hypotheses.

I checked the original spectral-measure locators rather than taking their summary on trust. For this loop-free graph, the edge factors in Proposition 6.1 are all equal to two, so its weighting reduces to length divided by total length. Lemma 6.7 gives uniform projection after restriction to the generic secular set and normalization, and equation (6.7) supplies the individual edge-law symmetry. Thus selecting the pendant edge really leaves all `3m` core phases independent uniform variables. This is a product law, not a heuristic sampling approximation. These checks use [Alon, Band and Berkolaiko, arXiv:2106.06096v2](https://arxiv.org/html/2106.06096v2), Proposition 6.1, equation (6.7), Lemma 6.7 and Assumptions 1-2.

The probabilistic identity imported from the global argument is

```math
\widetilde S_m-(2m-1)/2
=\sum_{i=1}^m h_i(R_m)-\tfrac12\mathop{\mathrm{sgn}}\nolimitsT_m,
\qquad R_m=-U_m/T_m.
```

I checked its integration points. Eliminating the module vertices gives `F_w=(p+r q)/a`, and the remaining core equation at `v` gives `U+Tr=0`. The principal pivots listed in the manuscript are the ones whose signs are used by this identity. The pendant's sign-count contribution cancels its inertia contribution, so the two pendant completions have the same surplus. Consequently no assumption of equal conditional weights of those completions is required. The all-`pi/4` witness gives nonzero values for every stated exceptional numerator, including `p_i T_m-U_m q_i`, which is the equation for an endogenous jump. Real-analytic zero-set nullity therefore applies, with the already-excluded denominators treated separately. Nullity of a deterministic threshold event alone would not have sufficed for this endogenous jump, but the proof does not rely on that shortcut.

I also checked the sign conventions of the form argument: the Helmholtz extension form is minus `k` times the outgoing-derivative matrix, so its negative index is the positive index of that matrix. Dirichlet edges give the sum of the floors. Hence `s=Q-n_+(M)` has the sign required by the module formula. Full independent spectral verification remains the spectral referee's responsibility; the probability argument uses the exact identity above, not a numerically fitted surrogate.

## 2. The fair sign and the actual variance function

For a uniform phase,

```math
(\cot\theta,\csc\theta)
\overset d=(X,\epsilon\sqrt{1+X^2}),
```

where `X` is standard Cauchy and `epsilon` is a fair sign independent of `X`. The two phases differing by `pi` have the same cotangent and opposite cosecant, which gives this independence directly.

Write `sigma=sgn(a)` and `h(r)=sigma g(r)`. The simultaneous reflection `theta_j -> pi-theta_j` fixes all three cosecants and negates `a`. The event `a=0` is null (a sum of independent continuous Cauchy variables), and this reflection proves that `sigma` is conditionally fair given the cosecant triple. For independent modules, these conditional fair signs are independent across modules. It follows that `E h(r)=0` for every deterministic nonzero `r`. This conclusion does not say that `sigma` or `h` is independent of the response vector `xi`.

For fixed effective signs of `(c_1,c_2,r c_3)`, if all three signs agree, `g=-1`; otherwise their sign sum is `+1` or `-1` and `g` is `0` or `1`. Hence `|h|<=1`. Squaring and averaging the eight independent cosecant signs gives

```math
E[h(r)^2\mid C_1,C_2,C_3]
=\tfrac14\left(1+\mathbf{1}_{\{|r|C_3>C_1+C_2\}}
+\mathbf{1}_{\{|r|C_3<|C_1-C_2|\}}\right).
```

Boundary equalities have probability zero by conditioning on the first two magnitudes and using the independent continuous third magnitude. This establishes the actual deterministic variance function

```math
v(r)=\tfrac12-\tfrac14
P(|C_1-C_2|<|r|C_3<C_1+C_2),\qquad C_j=\sqrt{1+X_j^2}.
```

Its advertised strict bounds and nonconstancy are valid. Each magnitude has a density positive on `(1,infinity)` and support `[1,infinity)`. For each finite `rho=|r|>0`, choose `C_1,C_2` close to the same large `L` and `C_3` close to a number above one; taking `2L>rho C_3` gives a nonempty open triangle event. Taking `C_3` sufficiently large and `C_1,C_2` bounded gives a nonempty open complement. Both have positive probability, so `1/4<v(r)<1/2`. Boundary nullity and dominated convergence give continuity. Evenness is explicit. As `rho` tends to zero the triangle indicator tends to zero except on the null event `C_1=C_2`; as `rho` tends to infinity it again tends to zero for every finite magnitude triple. Therefore both limiting values are `1/2`. Since every finite nonzero value is smaller, `v` is nonconstant.

## 3. Direct stable vector limit, without an imported tail theorem

Let `s_0=x_1+x_2`, `p=c_1+c_2`, and `phi=theta_3-arctan(s_0)`. Algebra gives

```math
\xi^{(2)}=\frac{1-s_0x_3}{s_0+x_3}=\tan\phi,
\qquad
\xi^{(1)}=\frac{p}{s_0\sin\theta_3+\cos\theta_3}
=\frac{p}{\sqrt{1+s_0^2}}\sec\phi.
```

Conditioned on the first two phases, the shifted third phase is uniform. Its tangent is Cauchy and its cosine sign is an independent fair sign. The coefficient `p/sqrt(1+s_0^2)` has exactly the symmetric law of the stated `W`; absorb the independent cosine sign into that coefficient. This proves the marginal vector law

```math
\xi\overset d=(W\sqrt{1+X^2},X),\qquad W\perp X.
```

Only this marginal law is used here; replacing the actual joint pair `(h,xi)` by a newly coupled pair would invalidate the later independence proof. The manuscript expressly avoids that replacement.

Averaging the two signs removes their cross term. With `z=x+y`, Tonelli's theorem applies to the nonnegative integral and gives

```math
EW^2
=\frac1{\pi^2}\int_{\mathbb R}\frac{dz}{1+z^2}
\int_{\mathbb R}\left(\frac1{1+x^2}+\frac1{1+(z-x)^2}\right)dx
=2.
```

In particular `W` has finite first and three-quarter moments. Independence in the vector representation and finite Cauchy moments of orders below one imply `E||xi||^(3/4)<infinity`.

The function `y -> cos(sqrt(y))` has derivative bounded in absolute value by `1/2`, including its limit at zero. Applying this to `b^2(1+x^2)` and `b^2 x^2` proves the manuscript's uniform estimate with error `b^2/2`. Symmetry of `W` lets one replace its exponential by the corresponding cosine. Replacing `sqrt(1+X^2)` with `X` inside that cosine gives error at most `t^2 EW^2/(2m^2)`. The standard Cauchy characteristic function then yields

```math
\chi_m(t,s)
=E e^{i(t\xi^{(1)}+s\xi^{(2)})/m}
=E e^{-|tW+s|/m}+O(m^{-2})
=1-\psi(t,s)/m+O(m^{-2}),
\quad \psi(t,s)=E|tW+s|.
```

For the last expansion, the error is bounded by `E(tW+s)^2/(2m^2)`, which is finite. The sign symmetries justify the real Cauchy expression for every `s,t`; there is no overlooked imaginary linear term or logarithmic centering. Independence of the actual modules gives the `m`th power of this characteristic function, tending to `exp(-psi)`. This limit is continuous at the origin, since `psi(t,s)<=|t|E|W|+|s|`. Levy's continuity theorem therefore provides a probability law `(A,B)` and the stated weak convergence of `(U_m/m,T_m/m)`.

## 4. Intrinsic full support and ratio properties

The symmetric `W` is not constant because `EW^2=2`; a symmetric constant would have to be zero. If `psi(t,s)=0`, then `tW+s=0` almost surely, which forces `(t,s)=(0,0)`. Continuity and positive homogeneity then give a positive minimum on the unit circle, so `psi(t,s)>=c sqrt(t^2+s^2)`. Thus `exp(-psi)` is integrable on the plane and Fourier inversion gives a continuous density for `(A,B)`. No atom on a line can remain.

The full-support claim is also justified intrinsically, rather than postulated as a condition. Positive homogeneity gives

```math
\alpha Z_1+(1-\alpha)Z_2\overset d=(A,B),\quad 0<\alpha<1,
```

for independent copies. For any two points in the closed support, independent positive-probability neighborhoods of those points prove that their convex combination is also in the support. The support is consequently convex. Every nonzero linear projection has characteristic function `exp(-|u| psi(t,s))`, a nondegenerate centered Cauchy law, and so has support all of the real line. A proper nonempty closed convex subset of the plane has a supporting separating half-space. Its projection in that half-space's normal direction could not have full real support. This contradiction proves that the planar support is all of `R^2`.

Absolute continuity excludes `A=0`, `B=0`, and each line `A+rB=0` with positive probability. Hence `R=-A/B` is finite, nonzero almost surely and has no atoms, including no atom at zero. Every real open interval has a nonempty open preimage under this ratio map with `B!=0`; full planar support gives it positive probability. Thus `R` has full real support, even though its value is almost surely nonzero. The continuous mapping theorem gives `R_m => R`.

Since `v` is continuous and nonconstant on the nonzero reals, choose two nonzero points with different `v` values and small neighborhoods whose value ranges are separated. Full support of `R` gives each neighborhood positive probability. Therefore `V=v(R)` is not almost surely constant and `Var(V)>0`; also `1/4<V<1/2` almost surely. This closes the stable-ratio and variance-function links without any formalization assumption.

## 5. Functional CLT and its source hypotheses

On either oriented half-line `r=delta rho`, `rho>0`, the cosecant signs and the sign of `r` are fixed, and `p+delta rho q` can cross zero at most once. At such a crossing the three effective signs cannot all agree, so their sign sum has absolute value one. Thus the jump of `g` has absolute value one. This proves

```math
h_i(\delta\rho)=\sigma_i
\left(b_i^\delta+j_i^\delta\mathbf{1}_{\{\tau_i^\delta\le\rho\}}\right),
\quad |b_i^\delta|\le1,\quad j_i^\delta\in\{-1,0,1\}.
```

The coefficients and thresholds depend only on the cosecants. Finite thresholds have no atoms: condition on the first two cosecants, exclude the null event `p=0`, and use the third cosecant's continuous law in the equation `tau=-p/(delta q)`. Marking with `sigma j=+1` or `-1` and assigning infinity otherwise cannot introduce finite atoms, because a marked finite equality is contained in the corresponding unmarked equality event.

For each marked threshold, its empirical CDF process is based on independent identically distributed modules. The decomposition into a baseline plus the difference of the two centered CDF processes is exact; conditional fairness of `sigma` makes the baseline mean zero and makes the two jump CDF expectations cancel.

The cited primary source is [Marckert, arXiv:0710.3296v2](https://arxiv.org/html/0710.3296v2), Theorem 1. It proves the uniform empirical-process limit in `D[0,1]` with the Skorokhod topology and continuous Brownian-bridge limit. Here each one-dimensional threshold CDF can be represented by applying its generalized inverse to independent uniforms. On a fixed finite threshold interval, its CDF is continuous; composition with that CDF consequently preserves uniform convergence at a continuous limit. Mapping infinity to one shows that its possible terminal atom is outside every such interval. Thus all four marked CDF processes are marginally tight on every compact subset of `(0,infinity)`. This application satisfies the source hypotheses; it does not require the four marked processes to be independent of each other.

The two bounded-variable baselines are tight by the ordinary finite-dimensional CLT. Finite products of these tight marginals are tight jointly. The multivariate CLT on the original module variables identifies their joint finite-dimensional limit, including all cross covariances. On a countable compact exhaustion of both half-lines, this gives a locally Skorokhod-convergent process with continuous limiting paths:

```math
G_m(r)=m^{-1/2}\sum_i h_i(r)\Longrightarrow G(r),
\qquad E[G(r)G(s)]=E[h(r)h(s)].
```

In particular `G` is centered Gaussian and `E G(r)^2=v(r)`. The baselines, marks, positive and negative half-lines, and their correlations all come from the actual module law. Marginal tightness is used only for tightness; joint finite-dimensional convergence determines the correlations.

## 6. Uniform moments and joint independence from the stable vector

Condition on all cosecants. The remaining `sigma_i` are independent fair signs. For deterministic coefficients of absolute value at most one, `cosh(t d_i)<=exp(t^2/2)` gives the exponential supermartingale. Its maximal inequality, separately in both signs and optimized at `t=z/sqrt(m)`, gives

```math
P\left(\max_{k\le m}\left|\sum_{i\le k}\sigma_i d_i\right|>z\sqrt m\right)
\le2e^{-z^2/2}.
```

The ordering of the jump thresholds depends only on the conditioned cosecants, so permuting the signs into that order preserves conditional independence and fairness. The absolute baseline plus the maximum absolute jump partial sum bounds each half-line supremum. Splitting a threshold `x` equally between those two terms, and taking a union bound over both half-lines, gives precisely

```math
P(\sup_{r\ne0}|G_m(r)|>x)\le8e^{-x^2/8}.
```

Right continuity in `rho` makes these suprema measurable through rational `rho`. Integrating the tail proves uniform bounds for every fixed positive moment. For second- and fourth-moment convergence, one may use any uniformly bounded moment above four, for example the sixth. The estimate does not condition on `R_m` and hence remains valid at that endogenous ratio.

For the indispensable independence check, take any bounded centered `H=sum_j a_j h(r_j)` on one **original** module. For `q=3/4`, the elementary inequality `|e^{iu}-1|<=C_q |u|^q` and the actual fractional moment give

```math
E|e^{i\zeta\cdot\xi/m}-1|=O(m^{-3/4}).
```

Expanding only the bounded exponential in `H/sqrt(m)` gives a uniform `O(m^-3/2)` remainder. Since `EH=0`, its linear mixed term is bounded by `||H||_infinity m^-1/2 O(m^-3/4)=O(m^-5/4)=o(m^-1)`. Its quadratic coefficient tends to `EH^2` by dominated convergence; no integrability of `xi` at order one is invoked. Together with the response characteristic expansion this gives

```math
E e^{i\zeta\cdot\xi/m+iH/\sqrt m}
=1-\{\psi(\zeta)+EH^2/2\}/m+o(m^{-1}).
```

Taking powers identifies a product characteristic function for every finite set of process evaluations and both stable coordinates. Their already-proved tightness gives the joint process-vector limit. Continuous paths and a countable dense evaluation set identify the process law and show that its whole sigma-field is independent of `(A,B)`. Therefore

```math
(G_m,U_m/m,T_m/m)\Longrightarrow(G,A,B),\qquad G\perp(A,B).
```

This is an asymptotic independence argument that allows arbitrary dependence within each module. It avoids assuming a conditional CLT given the global response, assuming an independent random evaluation point at finite `m`, or discarding the actual `h`-`xi` coupling.

## 7. Evaluation at the endogenous ratio

Joint convergence, rather than separate marginal convergence, is what allows evaluation. On a compact region `L^-1<=|r|<=L` of the two oriented half-lines, a continuous limit path makes the map `(f,r)->f(r)` continuous for local Skorokhod convergence. The ratio map is continuous wherever `B!=0`. The limit excludes both zero and infinity for `R`, so the probability of leaving these regions tends to zero as `L` tends to infinity; atomlessness also removes boundary issues. The exact exceptional-set calculation noted in Section 1 excludes evaluating the finite-`m` surplus identity at a jump.

Consequently

```math
G_m(R_m)\Longrightarrow G(R).
```

The established independence implies that, conditioned on `R`, the right side is a centered Gaussian with variance `v(R)`. It has the mixture law `Z sqrt(V)`, for a new standard normal `Z` independent of `V`. Independence of this new scalar Gaussian is a description of the limiting law, not an assumption about the finite graph.

## 8. Moment transfer and true variance normalization

The exact surplus identity gives

```math
\widetilde X_m
=\frac{\widetilde S_m-\beta_m/2}{\sqrt m}
=G_m(R_m)-\frac{\mathop{\mathrm{sgn}}\nolimitsT_m}{2\sqrt m}
\Longrightarrow Z\sqrt V.
```

The bounded last term and the supremum moment estimate give uniform integrability of both its square and fourth power. Thus

```math
E\widetilde X_m^2\to a_*=EV,\qquad
E\widetilde X_m^4\to3EV^2.
```

The last prime's square root exceeds every core length. Writing the total core length as `c_m`, one has `c_m<=3m sqrt(p_(3m+1))`, while the pendant length is `m^6 sqrt(p_(3m+1))`. Monotonicity of `c/(c+ell_0)` yields `omega_m<=3/(m^5+3)`. The edge-measure formula then makes the actual law a mixture with weight `1-omega_m` on the pendant law. Its total-variation distance from that law is at most `omega_m`; pushing forward by the centered `sqrt(m)` scaling cannot increase this distance, so the weak limit transfers.

Moment transfer requires more than total variation. All individual surplus laws are supported on `[0,beta_m]` and are symmetric about `beta_m/2`. Existence, support and symmetry of the spectral law use [Alon, Band and Berkolaiko, arXiv:1709.10413v2](https://arxiv.org/html/1709.10413v2), Theorem 2.1, whose nontrivial standard graph, generic-index, and rational independence hypotheses hold here. Individual edge-law symmetry is the previously checked equation (6.7). In particular the actual mean is exactly `beta_m/2`, not an asymptotic replacement for an unknown mean.

For `p=2,4`, the nonnegative function `|(s-beta_m/2)/sqrt(m)|^p` has maximum `(beta_m/(2sqrt(m)))^p`. In the mixture, the difference of two expectations of a function ranging between zero and that maximum is at most that maximum. Therefore

```math
|E|X_m|^p-E|\widetilde X_m|^p|
\le\omega_m\left(\frac{\beta_m}{2\sqrt m}\right)^p
=O(m^{p/2-5})\to0.
```

Thus the second and fourth moments of the actual centered law have the same limits. Exact centering gives `Var(S_m)=m E X_m^2`. Since `1/4<a_*<1/2`, the denominator is eventually positive, and

```math
\frac{\mathop{\mathrm{Var}}\nolimits(S_m)}{\beta_m}\to\frac{a_*}{2}\in(1/8,1/4),
\qquad
\frac{S_m-\beta_m/2}{\sqrt{\mathop{\mathrm{Var}}\nolimits(S_m)}}
\Longrightarrow Z\sqrt{V/a_*}.
```

Slutsky's theorem applies with this deterministic convergent variance factor. The standardized fourth moments tend to `3 EV^2/a_*^2`, because their denominator is `(E X_m^2)^2` and tends to the positive `a_*^2`. The PDF's extension to other lengths is also correct: `omega_m->0` suffices for the unstandardized weak limit, `m omega_m->0` suffices for variance and standardized weak convergence, and `m^2 omega_m->0` suffices for the fourth-moment transfer.

## 9. Non-Gaussianity, quantifiers, and status consequence

The variable `V` is bounded, strictly positive, and nonconstant. The limiting standardized mixture has mean zero and variance one. For each nonzero real `t`, the strictly convex function `x -> exp(-t^2 x/(2a_*))` gives strict Jensen inequality:

```math
E e^{-t^2 V/(2a_*)}>e^{-t^2/2}.
```

Its characteristic function therefore differs from that of the standard Gaussian. Its fourth moment is `3 EV^2/a_*^2>3`, with strictness exactly equivalent to `Var(V)>0`. The actual standardized fourth moments converge to this quantity. A fourth-moment obstruction alone would need moment convergence to exclude a Gaussian weak limit; here that convergence has been proved, and the characteristic-function argument additionally excludes Gaussianity directly.

The original question quantifies over every admissible sequence with cycle rank tending to infinity. This single explicit sequence meets every target hypothesis and has `beta_m=2m-1->infinity`; convergence along all possible integer cycle ranks is unnecessary to refute a universal sequence assertion. Each graph's spectral law is taken first and only then is `m` sent to infinity, precisely as the target defines it. The prime-root pendant prescription supplies the required fast vanishing contamination, rather than merely assuming a limiting length regime.

The graph sequence itself has asymptotically linear variance with a positive finite coefficient, so it neither disproves nor proves universal linear variance bounds for arbitrary graph sequences. Growing hub degrees and a dominant pendant length are allowed by the unrestricted target. This audit makes no claim about bounded-degree or comparable-length variants, simultaneous spectral-window limits, priority, or a complete current-literature resolution of the variance question.

## Blockers, qualifications, and recommendation

Blocking proof gaps found in the probability and limit chain: **none**.

The main steps that required substantive checking were the actual joint module law in the independence expansion, local process tightness before endogenous evaluation, intrinsic full support of the stable law rather than an assumed support condition, finite-threshold atom control despite a terminal atom at infinity, and bounded-support moment contamination rather than total variation alone. The supplied argument includes valid mechanisms for each. The calculations above make the implicit standard details explicit; they do not introduce an additional unproved hypothesis.

Within this audit's mathematical scope, the PR's `PARTIAL` status for AIM 114 is supported: the unrestricted Gaussian assertion is false, while the separate universal variance assertion remains unresolved by this construction. Final acceptance of the complete graph counterexample should also use the separately assigned spectral audit. The manuscript and expanded source have not been edited by this reviewer, and no Git state or GitHub state was changed. The supporting Lean claims were not treated as evidence for this mathematical verdict; this report does not assert that the metric spectral theorem, stable-ratio construction, or process convergence have been formally verified.
