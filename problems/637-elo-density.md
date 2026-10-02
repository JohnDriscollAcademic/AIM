# 637. Absolute continuity of stationary Elo ratings

**Area:** Probability, statistics, and uncertainty quantification
**Status:** ✅ SOLVED
**Last checked:** 2026-10-02

## Problem statement

Fix an integer $`N\ge2`$, a vector $`\rho\in\mathbb R^N`$ with $`\sum_i\rho_i=0`$, and parameters $`c,K>0`$ satisfying $`Kc<1`$. Let

```math
Z_N=\{x\in\mathbb R^N:\textstyle\sum_i x_i=0\},
\qquad b(u)=\tanh(cu).
```

At each discrete time, choose an ordered pair of distinct players uniformly and independently of the past. Conditional on the pair $`i,j`$, draw a fresh score $`S\in\{-1,1\}`$, independently of the past, with

```math
\mathbb P(S=1\mid i,j)=\frac{1+b(\rho_i-\rho_j)}2.
```

Starting from $`X_0\in Z_N`$, update only these two coordinates:

```math
X_i'=X_i+K\{S-b(X_i-X_j)\},\qquad
X_j'=X_j-K\{S-b(X_i-X_j)\}.
```

This Markov chain has a unique invariant probability measure $`\pi_{N,\rho,c,K}`$ on $`Z_N`$.

Is $`\pi_{N,\rho,c,K}`$ absolutely continuous with respect to the $`(N-1)`$-dimensional Lebesgue measure on $`Z_N`$ for every such choice of parameters? Prove this assertion or exhibit admissible parameters for which it fails. This is the logistic, binary-score instance of the stationary-density question in Cortez and Tossounian, Section 6.

## Application

Elo ratings estimate relative skills in repeated paired comparisons. A density theorem would provide a foundation for continuous approximations to their long-run uncertainty and for interpreting simulated rating histograms.

## References

- Roberto Cortez and Hagop Tossounian, *Convergence and stationary distribution of Elo rating systems*, Annals of Applied Probability 36(4), 2026, DOI [10.1214/26-AAP2306](https://doi.org/10.1214/26-AAP2306). [Author manuscript, version 2](https://arxiv.org/abs/2410.09180v2), Sections 1.3, 5.1–5.2, and 6; Theorems 1, 13, and 26 in the manuscript numbering.
- David Aldous, *Elo ratings and the sports model: A neglected topic in applied probability?*, Statistical Science 32(4), 2017, 616–629, DOI [10.1214/17-STS628](https://doi.org/10.1214/17-STS628).

## Status review

**Resolution (2026-10-02):** For two players, equal true ratings, logistic parameter c=1/2 and update K=9/10, the unique stationary law is singular continuous with full support. A rigorous global drift certificate bounds the Hausdorff dimension of a full-measure carrier by 10 log(2)/7, strictly below 1. This disproves universal absolute continuity without classifying the other parameters.

**Proof and review:** [Accepted solution](../research/solutions/siavash-sadeghi-637/aim637_counterexample.pdf); [fresh mathematical audit](../research/solution_reviews/2026-10-02-active-prs/637-review.md); [PR #24](https://github.com/MColbrook/AIM/pull/24). The audit records the pinned submission, target comparison and any supporting computations.

**Evidence:** Solved under the documented-independent-audit convention. The review was performed by AI; it does not assert human peer review, publication, proof-assistant verification or novelty priority. The problem retains its existing page and ID.

### Previous status review

**Known cases:** The invariant measure exists uniquely, has full support and an exponential moment, and attracts the chain exponentially in the 2-Wasserstein distance under the source assumptions. The source contrasts binary scores with continuously distributed scores, where density existence is available. Its binary-score numerical experiments suggest densities but do not establish them.

**Remaining target:** Absolute continuity for the discrete binary-score update above. Full support and Wasserstein convergence do not imply this property. Smoothness conditional on density existence is a further question, not a prerequisite for resolving this entry.

The January 2026 manuscript explicitly retains this question. A July 2026 Zenodo preprint on Elo fluctuation laws treats linearized drift–diffusion covariances; its Section 8 explicitly limits those claims to the linearization. It does not establish a density for the nonlinear chain here.  No matching resolution was found; these searches do not establish exhaustive absence of unpublished or unindexed announcements.
