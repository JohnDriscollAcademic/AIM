# 114. A universal central limit law for quantum-graph nodal surplus

**Area:** Wave networks and quantum chaos

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

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

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Graphs with sufficiently independent cycle structure supply proved Gaussian cases. The 2025 discrete-signing paper explains that analogous discrete-matrix assertions can fail; those counterexamples do not resolve the metric Kirchhoff assertion. Conditioning on generic indices handles loop-supported eigenfunctions correctly.

**Search audit:** “quantum graph nodal surplus central limit conjecture 2025 2026”; “Alon Band Berkolaiko Conjecture 3.1 counterexample”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
