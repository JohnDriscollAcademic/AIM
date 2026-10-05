# 114. A universal central limit law for quantum-graph nodal surplus

**Area:** Wave networks and quantum chaos

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-05

## Problem statement

Consider finite connected compact metric graphs with positive edge lengths linearly independent over $`\mathbb Q`$. Impose the standard Kirchhoff Laplacian: $`-u''`$ on edges, continuity at vertices, and zero sum of outgoing derivatives at each vertex. Number its eigenvalues $`0=\lambda_1\le\lambda_2\le\cdots`$. Call an index generic if its eigenvalue is simple and a real eigenfunction is nonzero at every vertex. For a generic index $`n`$, let $`\phi_n`$ be the number of interior-edge zeros and let $`s_n=\phi_n-(n-1)`$. With cycle rank $`\beta=|E|-|V|+1`$, one has $`0\le s_n\le\beta`$.

Define $`S`$ by the limiting distribution of $`s_n`$ among generic indices in $`\{1,\ldots,N\}`$ as $`N\to\infty`$; these limits exist. Prove or disprove that for every sequence of these graphs with $`\beta_j\to\infty`$,

```math
\frac{S_j-\beta_j/2}{\sqrt{\mathop{\mathrm{Var}}\nolimits(S_j)}}\ \Longrightarrow\ \mathcal N(0,1),
```

and that universal constants $`c,C>0`$ bound $`c\beta_j\le\mathop{\mathrm{Var}}\nolimits(S_j)\le C\beta_j`$ for all sufficiently large $`j`$.

## Application

The surplus counts extra sign changes created by network cycles. A universal law would describe high-frequency wave patterns across large networks without requiring a particular network architecture.

## References

1. L. Alon, R. Band and G. Berkolaiko, [Universality of nodal count distribution in large metric graphs](https://doi.org/10.1080/10586458.2022.2092565), Experimental Mathematics 33 (2024), Definitions 2.2–2.4 and Conjecture 3.1: distribution and full proposed law.
2. L. Alon, R. Band and G. Berkolaiko, [Nodal statistics on quantum graphs](https://arxiv.org/abs/1709.10413), preprint (2017), Theorem 2.1 and disjoint-cycle results: limiting law and established special families.
3. L. Alon and M. Goresky, [Nodal count for a random signing of a graph with disjoint cycles](https://doi.org/10.4171/JST/578), Journal of Spectral Theory 15 (2025), introduction: distinction between metric graphs and discrete signed operators.
4. Sidney Holden, [A non-Gaussian limit for nodal surplus](../research/solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf), revised proof v0.3 (2026-10-02), Theorem 1. See the [expanded argument and provenance](../research/solutions/114-nodal-surplus-counterexample/README.md), [spectral audit](../research/solutions/114-nodal-surplus-counterexample/reviews/spectral-review.md), and [probability audit](../research/solutions/114-nodal-surplus-counterexample/reviews/probability-review.md).

## Status review

**Known cases:** The unrestricted Gaussian assertion is disproved by Holden's explicit loop-free graph sequence in reference 4, reviewed by two independent OpenAI Codex AI agents on 2026-10-05. For each $`m\ge3`$, join $`u`$ to each $`w_i`$ by two parallel edges, join $`w_i`$ to $`v`$ by one edge, and add a pendant edge at $`u`$. Then $`\beta_m=2m-1`$. Use successive prime square roots for the core lengths and $`m^6\sqrt{p_{3m+1}}`$ for the pendant length. These positive lengths are rationally independent. The standardized surplus tends to a nonconstant Gaussian variance mixture, with limiting standardized fourth moment strictly greater than three. Its variance-to-cycle-rank ratio tends to a constant in $`(1/8,1/4)`$.

**Remaining target:** Determine whether universal positive constants bound the variance above and below by the cycle rank for every admissible graph sequence. The counterexample has linear variance and does not decide that assertion. Gaussian limits under additional restrictions such as bounded degrees or comparable lengths are not settled by this construction.

**Review scope:** The linked reports independently audit the spectral reduction and probabilistic limit, including the original cited theorems, genericity, joint convergence, and moment transfer. They found no blocking defect in the submitted argument. These are AI mathematical audits, not external human peer review. Exact finite rational checks provide additional algebraic regression evidence. Any accompanying Lean supporting lemmas do not formalize the full graph counterexample; no Lean-verified status is claimed.

**Supporting Lean results:** The [partial formalization](../research/lean/114/README.md) has 31 results covering the actual multigraph and its positive jointly rationally independent lengths, local sign identities and finite core inertia, the actual Cauchy-defined variance function, an actual normalized Gaussian-mixture law with proved moments and non-Gaussianity, and exact graph length sums and prime-root weights with second/fourth-moment contamination error tending to zero. Its [exact scope](../research/lean/114/NUMERICAL_TARGETS.md), [independent reviews](../research/lean/114/reviews/), and [verification record](../research/lean/114/verification/README.md) identify the remaining metric/spectral, stable-ratio, and process-convergence links. The ratio law still must be constructed and shown to have full support and no atom at zero. Historical verification of the initial three lemmas is retained separately from the expanded package.

Graphs with sufficiently independent cycle structure supply proved Gaussian cases. The 2025 discrete-signing paper explains that analogous discrete-matrix assertions can fail; those counterexamples do not resolve the metric Kirchhoff assertion. Conditioning on generic indices handles loop-supported eigenfunctions correctly.

**Search audit:** On 2026-10-05, checked the supplied manuscript against arXiv:2106.06096v2, arXiv:1709.10413v2, and arXiv:0710.3296v2. Searches for “nodal surplus non-Gaussian counterexample” and “Universality of nodal count counterexample 2026” did not locate a separate subsequent resolution of the remaining universal variance assertion. This was a bounded source and literature check, not a proof of openness or priority.
