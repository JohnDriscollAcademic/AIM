# 665. Smooth-gradient approximation of finite-Fisher-information scores

**Area:** Optimal transport and weighted Sobolev approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Let $`(M,g)`$ be a smooth compact Riemannian manifold, possibly with smooth boundary, and let $`dV_g`$ denote its volume measure. Let $`\rho\ge0`$ satisfy $`\int_M\rho\,dV_g=1`$ and $`\sqrt\rho\in H^1(M)`$. Its Fisher information is

```math
I(\rho)=4\int_M|\nabla\sqrt\rho|_g^2\,dV_g<\infty.
```

Define the score $`s_\rho=2\nabla\sqrt\rho/\sqrt\rho`$ on $`\{\rho>0\}`$ and zero elsewhere.

Prove or disprove the conjecture following Theorem 4 of [1]: there exist $`\varphi_j\in C^1(M)`$, continuously differentiable up to the boundary, such that

```math
\int_M|\nabla\varphi_j-s_\rho|_g^2\rho\,dV_g\longrightarrow0.
```

No convexity, uniform positivity, upper bound on $`\rho`$, or boundary condition on $`\varphi_j`$ is assumed.

## Application

The approximation would remove an extra hypothesis from entropy chain rules on smooth nonconvex domains, allowing finite-action fluxes to be tested against the score in convergence arguments for variational diffusion schemes.

## References

1. J.-B. Casteras, M. Flaim and L. Monsaingeon, [Entropy and Fisher information in non-convex domains: one chain to rule them all](https://arxiv.org/abs/2512.05826), 2025. Section 2, discussion following Theorem 4; Lemma A.3.
2. C. Cancès, L. Monsaingeon and A. Natale, [Discretizing the Fokker–Planck equation with second-order accuracy: a dissipation driven approach](https://doi.org/10.1007/s00211-026-01537-3), *Numerische Mathematik* **158** (2026), 1513–1563. Appendix A motivates the related chain-rule problem.

## Status review

**Additional proof (2026-10-02):** [PR #19](https://github.com/MColbrook/AIM/pull/19) supplies a [heat-semigroup proof](../solutions/618-fisher-score-heat-semigroup/aim618_solution.pdf), checked in a [fresh Codex AI audit](../solution_reviews/2026-10-02-active-prs/665-additional-proof-review.md). It treats the same full smooth-manifold target, including vacuum, unbounded densities and nonconvex boundary. The previously recorded proof and review remain available below; this is one solved problem with two proof routes.

**Resolution (2026-10-02):** Affirmative proof. The complete target was checked in an independent Codex AI mathematical audit of [the submitted proof](../solutions/618-fisher-score/PROOF.md). See [the review record](../solution_reviews/2026-10-02/618-review.md) for the reasoning, scope and supporting checks.

**Original target:** [618 at the pinned catalogue revision](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/618-fisher-score-gradient-closure.md). Current archive ID: 665. Submitted in [PR #4](https://github.com/MColbrook/AIM/pull/4).

**Evidence:** Solved under the documented-independent-audit convention. This review was performed by AI. It does not assert human peer review, publication, proof-assistant verification or novelty priority. The submitted package retains its original pending-review wording.

### Previous status review at the pinned revision

**Known cases:** Lemma A.3 of [1] establishes the conclusion when $`0<c\le\rho\le C<\infty`$.

**Remaining target:** Allow arbitrary finite Fisher information, including vanishing or unbounded densities. This is a static approximation question on smooth geometry; the separate Lipschitz-domain chain-rule problem concerns time-dependent curves and rough geometry.

Current literature, arXiv, public GitHub, native Zenodo and Palomar checks found no resolution or matching announcement. An author-posted related regularization question remains unresolved; the proposed answer acknowledges a gap. No equivalent catalogue problem was found.
