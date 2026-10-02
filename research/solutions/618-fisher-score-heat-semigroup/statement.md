# 618. Smooth-gradient approximation of finite-Fisher-information scores

**Area:** Optimal transport and weighted Sobolev approximation

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

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

**Known cases:** Lemma A.3 of [1] establishes the conclusion when $`0<c\le\rho\le C<\infty`$.

**Remaining target:** Allow arbitrary finite Fisher information, including vanishing or unbounded densities. This is a static approximation question on smooth geometry; the separate Lipschitz-domain chain-rule problem concerns time-dependent curves and rough geometry.

Current literature, arXiv, public GitHub, native Zenodo and Palomar checks found no resolution or matching announcement. An author-posted related regularization question remains unresolved; the proposed answer acknowledges a gap. No equivalent catalogue problem was found.
