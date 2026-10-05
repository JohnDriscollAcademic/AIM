# Independent AI review: spectral reduction for AIM 114

- Review date: 2026-10-05.
- Reviewer: an independent Codex AI subagent (`spectral_review`), separate from the manuscript author and the implementing agent. This is an AI review, not human peer review.
- Mathematical author: Sidney Holden, as identified by the submitter.
- Source: [`../submitted/short_proof-v0.3.pdf`](../submitted/short_proof-v0.3.pdf), *A non-Gaussian limit for nodal surplus*, revised proof v0.3, dated 2026-10-02, six pages.
- Source SHA-256: `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.
- Expanded presentation also read: [`../PROOF.md`](../PROOF.md), SHA-256 `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604`. In particular its first two sections, from the graph sequence through the spectral reduction, faithfully preserve the PDF's formulas, hypotheses, exceptional-set argument, and scope. I found no introduced mathematical discrepancy in that presentation.
- Target: [`problems/114-quantum-graph-nodal-clt.md`](../../../../problems/114-quantum-graph-nodal-clt.md) at upstream commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.
- Scope: all six manuscript pages were read and visually inspected. The detailed audit below concentrates on graph admissibility, the cited spectral measure theorems, the exact nodal-surplus formula, and exceptional null sets. The probabilistic continuation was also checked for consistency and logical closure. No Lean code was reviewed or executed in this audit.

## Verdict and scope of the result

I found no fatal mathematical gap in the submitted argument. The graph family is admissible for the stated metric Kirchhoff problem, and the spectral-to-phase reduction uses the cited published results with their hypotheses satisfied. The sign and inertia computation in Lemma 1 is correct. The continuation supplies a nonconstant Gaussian variance mixture, rather than merely a non-Gaussian fourth-moment sequence.

The argument disproves the universal Gaussian assertion in AIM 114. It does **not** disprove, prove, or otherwise settle the separate universal linear-variance assertion. Its own graph family has a positive finite limiting variance-to-cycle-rank ratio. A catalogue update must preserve this distinction.

This is an ordinary mathematical audit that accepts the cited published theorems and standard spectral/probability results as established. It is not a proof certificate, an independent reproof of the reference papers, or a claim of complete Lean verification.

## Primary-source check

The following version-specific sources were opened during the audit:

1. [Alon, Band and Berkolaiko, arXiv:2106.06096v2](https://arxiv.org/html/2106.06096v2), Assumptions 1-2, Conjecture 3.1, Proposition 6.1, equation (6.7), and Lemma 6.7. Parallel edges are permitted. The assumptions require a finite connected graph with no degree-two vertices and standard vertex conditions. Proposition 6.1 gives weights proportional to edge length times a loop/nonloop factor; all factors are equal here because this graph has no loops. Equation (6.7) gives each edge law's symmetry. Lemma 6.7 gives uniform projection after restriction to generic phases and normalization. These are exactly the three ingredients claimed in manuscript equation (6).
2. [Alon, Band and Berkolaiko, arXiv:1709.10413v2](https://arxiv.org/pdf/1709.10413v2), Theorem 2.1 and its preceding definitions. The theorem gives existence of the frequency law among generic indices and symmetry about half the cycle rank for the relevant standard graph and rationally independent lengths.
3. [Marckert, arXiv:0710.3296v2](https://arxiv.org/pdf/0710.3296v2), Theorem 1 and Note 1. The theorem is the uniform empirical-process functional CLT in the Skorokhod topology; the manuscript supplies the needed CDF time change on compact parameter intervals with continuous CDFs.

The first source's Conjecture 3.1 imposes neither a maximum-degree bound nor comparability of edge lengths. The large hubs and dominant pendant length therefore do not evade its quantifiers.

## Graph and lengths

For integer `m >= 3`, the construction has `3m+1` edges and `m+3` vertices, giving cycle rank `2m-1`. Its degrees are `2m+1` at `u`, `m` at `v`, three at every `w_i`, and one at `t`. It is connected and loop-free, and has no degree-two vertex. The doubled `u--w_i` connections are allowed parallel edges.

Every assigned length is positive. Distinct prime square classes are independent over the field with two elements, so the multiquadratic extension admits the individual sign changes used in the manuscript. Applying such a sign change to a rational linear relation isolates the coefficient of the corresponding square root. Multiplication of the pendant length by the nonzero integer `m^6` does not change rational independence.

The spectral-frequency limit is taken separately for every fixed graph before `m` tends to infinity. No uniform-in-graph equidistribution assertion is being used.

## Nodal count and inertia: a direct derivation

Fix a positive generic eigenvalue `k^2` and assume every edge sine is nonzero. On an edge, write its phase as `d*pi + alpha`, where `d` is the integer part and `0 < alpha < pi`. An edgewise sine wave has either `d` or `d+1` interior zeros. Comparing endpoint signs with the sign of the edge sine selects the extra zero precisely when `F_a F_b csc(theta) < 0`. Thus the nodal count is `D+Q` with the manuscript's definitions.

The form domain is the space of continuous edgewise `H^1` functions. The nonzero-sine assumption gives a unique Helmholtz extension of arbitrary vertex values. Subtracting that extension gives an algebraic direct sum of the edgewise vertex-zero space and the finite-dimensional extension space. Integration by parts makes these spaces orthogonal for the form `integral (|f'|^2-k^2|f|^2)`.

The first summand has negative index `D`: the strict Dirichlet eigenvalue count on each edge is exactly the integer part of its phase divided by `pi`. The extension form is `-k F^T M F`, so its negative index is the number of positive eigenvalues of `M`. The full form has negative index `n-1`, including the zero eigenvalue of the Kirchhoff Laplacian in that count. This proves `n-1 = D+n_+(M)` and hence surplus `Q-n_+(M)` with the stated sign.

If `F_u` is nonzero, replace the `u` coordinate basis vector by the kernel vector `F`. This is an invertible change of basis, and the transformed matrix is the direct sum of zero and the principal matrix with `u` deleted. Sylvester inertia therefore justifies the second equality in (10). The formula is phase-periodic; positive lifts of a secular phase give a valid graph at `k=1`, without requiring those temporary lifted lengths to be rationally independent.

## Elimination and pendant cancellation

With `F_u=1` and `F_v=r`, the `w_i` equation gives `F_wi=(p_i+r q_i)/a_i`. Eliminating the `w_i` variables gives the core matrix on `(u,v)` with entries `Lambda_m`, `U_m`, and `T_m`. Its `v` equation is `U_m+T_m r=0`, exactly as stated.

Deleting `u` and eliminating the `w_i` variables produces diagonal pivots `-a_i`, followed by `T_m`. The isolated pendant coordinate contributes the pivot `-cot(theta_0)`. The pendant endpoint equation gives `F_t=1/cos(theta_0)`; its contribution at `u` is `tan(theta_0)`. Consequently the last secular equation is `tan(theta_0)=-g_m`.

The pendant's sign count is the indicator of `tan(theta_0)<0`, because `F_u F_t csc(theta_0)=1/(sin(theta_0)cos(theta_0))`. Its positive-pivot count is the same indicator. They cancel.

For a module, let `sigma=sgn(a)`, `tau=sgn(p+r q)`, and let `L` be the sum of the signs of `c_1,c_2,r q`. Its three sign counts sum to `(3-sigma*tau*L)/2`. Subtracting the positive-pivot count `(1-sigma)/2` gives `1+sigma*(1-tau*L)/2 = 1+h(r)`. Therefore the full surplus is `m+sum_i h_i(r)-1{T_m>0}`. Subtracting `(2m-1)/2` gives exactly (9), including its final minus sign.

There are two pendant completions modulo `2*pi`. Their surplus values coincide by this calculation. Uniform projection of the generic pendant-edge measure therefore determines the surplus law without any unproved assertion about equal conditional weights on the two completions.

## Exceptional sets and genericity

Every expression listed in the manuscript is a rational expression in edge sines and cosines. Clearing its finitely many denominators gives a trigonometric polynomial. The common choice of every core phase equal to `pi/4` gives:

- `a_i=3`, `p_i=2 sqrt(2)`, `q_i=sqrt(2)`;
- `U_m=4m/3`, `T_m=-m/3`, `R_m=4`;
- `F_wi=2 sqrt(2)`, `Lambda_m=2m/3`, `g_m=6m`.

This verifies that none of the numerator polynomials needed for the listed exclusions is identically zero. Nonzero real-analytic trigonometric polynomials have Lebesgue-null zero sets. A finite union remains null under the uniform core-phase measure.

Outside that union, the two solutions of the pendant equation have nonzero sine and cosine, all vertex values are nonzero, and all the pivots of `M` with `u` deleted are nonzero. The assembled matrix has a nonzero kernel vector and an invertible principal minor, so its kernel is one-dimensional. Nonzero edge sines identify that kernel with the full graph eigenspace. This establishes both simplicity and vertex nonvanishing, rather than assuming genericity after elimination.

There is no additional completion with `F_u=0`, even at a potentially resonant pendant phase: the invertible core matrix with `u` deleted forces all core vertex values, hence all core edges, to vanish. Kirchhoff at `u` then forces the pendant derivative to vanish as well as its value, so that edge also vanishes. The two constructed generic completions exhaust the relevant fiber. Assigning right-continuous values at the module jumps does not affect (9), since evaluation at such a jump would be one of the already excluded equations `p_i+R_m q_i=0`.

## Check of the probabilistic continuation

The simultaneous phase reflection fixes the three cosecants while reversing `a`, giving the claimed conditional fair sign. This justifies both centering at every fixed `r` and the conditional Rademacher bound; it does not assert independence of a module's response vector and its surplus function.

I checked the algebra giving the response vector in terms of the shifted third phase and the displayed nonnegative integral for `E W^2=2`. The characteristic-function estimate uses the symmetry of `W` and a quadratic cosine error; the resulting stable exponent has no missing centering term. Positivity on the unit circle gives integrability of the limiting characteristic function. Stability makes the closed support convex, and the nondegenerate Cauchy projections exclude a proper closed convex support. Consequently the ratio is finite and nonzero almost surely, has no atoms, and has full real support.

The sign average for `E h(r)^2` gives the displayed triangle-event expression. Its boundary equalities have probability zero. Both the event and its complement have positive probability for every finite nonzero `r`; the two endpoint limits and continuity make `v` nonconstant. Full support of the ratio then gives `Var(v(R))>0`.

The empirical-process argument uses joint tightness plus finite-dimensional joint CLTs, not independence of the four marked empirical CDFs. Finite threshold distributions are atomless; the possible mass at infinity does not affect compact intervals of positive finite thresholds. The mixed characteristic-function expansion uses the original joint module variables. Its linear error is `O(m^(-5/4))`, and the weighted quadratic term converges by dominated convergence. Thus the stable response is independent of the limiting Gaussian process. Localizing away from zero and infinity permits random evaluation at the ratio.

The conditional maximal bound is uniform over all nonzero `r`. It supplies higher moments sufficient for uniform integrability of both the second and fourth powers. For the actual lengths, the core fraction is at most `3/(m^5+3)`; the residual contribution to a centered normalized moment of order `p` is bounded by that fraction times `((2m-1)/(2 sqrt(m)))^p`. This tends to zero for `p=2,4`. Hence the moment passage does not misuse total variation for unbounded observables. Strict convexity of the exponential Laplace-transform function, applied to nonconstant `V`, proves that the standardized weak limit is genuinely non-Gaussian. The manuscript also correctly separates weaker assumptions needed for weak, second-moment, and fourth-moment convergence under other length choices.

## Lean feasibility and limits

A complete Lean proof would have to connect actual generic eigenfunction frequencies of compact metric Kirchhoff graphs to the phase measure, prove the nodal-count/inertia formula, build the graph and rationally independent lengths, and establish the joint empirical-process/stable limit, moment transfer, and non-Gaussian law. The two cited quantum-graph papers are substantial mathematical dependencies. Ordinary citation is acceptable in this informal audit but cannot substitute for a theorem in a kernel-checked proof claiming the complete target.

The finite module sign identities, graph counts, variance-transfer inequalities, and algebraic non-Gaussian moment obstruction are plausible separately formalizable components. A theorem that assumes the spectral reduction, joint weak limit, or variance-mixture representation is a conditional or partial result. It must not be advertised as complete Lean verification of AIM 114 or conceal those assumptions in definitions or custom axioms.

This audit did not inventory the entire pinned Mathlib tree, attempt full formalization, run a kernel checker, or perform fresh spectral simulations. Its conclusion is based on independent mathematical derivation and source checking. It identifies no mandatory mathematical correction to v0.3 within the reviewed scope; preserving the unresolved universal variance assertion and accurately reporting formalization coverage are mandatory for a resolution report.
