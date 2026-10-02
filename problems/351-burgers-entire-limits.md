# 351. Can every bounded entire Burgers profile recur at late times?

**Area:** Viscous conservation laws; asymptotic dynamics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Let $`\alpha<\beta`$ and let $`\mu`$ be any Borel probability measure supported in $`[\alpha,\beta]`$. Define

```math
\phi_\mu(x)=\frac{\int z e^{-zx/2}\,d\mu(z)}{\int e^{-zx/2}\,d\mu(z)}.
```

Does there exist $`u_0\in L^\infty(\mathbb R)`$ with $`\alpha\le u_0\le\beta`$ almost everywhere such that the solution of

```math
u_t+u u_x=u_{xx},\qquad u(0,x)=u_0(x),
```

admits sequences $`t_k\to\infty`$ and $`x_k\in\mathbb R`$ for which $`u(t_k,x+x_k)\to\phi_\mu(x)`$ uniformly on every compact interval? The measure may be continuous or have infinitely many atoms; finite shock mergers alone do not settle the question.

## Application

Burgers dynamics models nonlinear transport with viscosity. The question asks how complicated the locally observed late-time states can be when the initial medium is bounded but need not approach constants at infinity.

## References

1. T. Gallay and A. Scheel, [*Viscous shocks and long-time behavior of scalar conservation laws*](https://arxiv.org/abs/2306.13341), Communications on Pure and Applied Analysis 23 (2024), 1448–1482, §6 immediately after Proposition 6.2 and §7.
2. E. Hopf, [*The partial differential equation $`u_t+uu_x=\mu u_{xx}`$*](https://doi.org/10.1002/cpa.3160030302), Communications on Pure and Applied Mathematics 3 (1950), 201–230; the linearizing transformation underlying the profile representation.

## Status review

**Resolution (2026-10-02):** Every probability measure on the specified bounded interval is realized as a late-time, spatially translated Burgers profile. The locality and diagonal gluing argument covers continuous as well as atomic measures.

**Proof and review:** [Accepted solution](../research/solutions/351-burgers-profile-realization/aim351_burgers_realization.pdf); [fresh mathematical audit](../research/solution_reviews/2026-10-02-active-prs/351-review.md); [PR #23](https://github.com/MColbrook/AIM/pull/23). The audit records the pinned submission, target comparison and any supporting computations.

**Evidence:** Solved under the documented-independent-audit convention. The review was performed by AI; it does not assert human peer review, publication, proof-assistant verification or novelty priority. The problem retains its existing page and ID.

### Previous status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 by searching Gallay–Scheel, entire Burgers solutions, probability-measure profiles, and realization in omega-limit sets. The 2024 paper proves that every possible limit has the displayed representation and constructs particular recurrent two-shock mergers; it explicitly conjectures the converse for arbitrary probability measures. Searches located further shock-extinction and convergence results, but no proof of this full realization assertion. The Cole–Hopf formula characterizes entire solutions; it does not itself establish that they occur as late-time limits of a different trajectory.
