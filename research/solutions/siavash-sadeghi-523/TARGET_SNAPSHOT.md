# 523. Removing the logarithmic loss in Helmholtz Nyström estimates

**Area:** Numerical PDEs and boundary integral equations

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`\Gamma\subset\mathbb R^2`$ be a smooth embedded closed curve with a smooth periodic parametrization $`\gamma:\mathbb R/(2\pi\mathbb Z)\to\Gamma`$ satisfying $`0<|\gamma'(t)|<c_{\max}`$. Consider the oscillatory logarithmic-kernel coefficients from equation (9.6) of the reference:

```math
L_{1,k}(t,\tau)=k\int_{S^1}e^{ik\langle\gamma(t)-\gamma(\tau),\omega\rangle}f_k(\omega,t,\tau)\,dS(\omega),
```

where $`f_k`$ is smooth and periodic in $`t,\tau`$, with every derivative in $`(\omega,t,\tau)`$ bounded independently of $`k`$. Define

```math
\widehat L_{1,k,m}(t)=\frac1{\sqrt{2\pi}}\int_0^{2\pi}e^{-im\tau}L_{1,k}(t,\tau)\,d\tau,\qquad \langle z\rangle=(1+|z|^2)^{1/2}.
```

Identify functions of $`t`$ with functions on $`\Gamma`$. Write $`H_k^s(\Gamma)`$ for the Sobolev norm with derivatives weighted by $`k^{-1}`$, equivalently $`\|u\|_{H_k^s}=\|(I-k^{-2}\Delta_\Gamma)^{s/2}u\|_{L^2(\Gamma)}`$.

Is it true that, for every $`k_0>0`$ and $`s\in\mathbb R`$, there is a constant $`C`$ such that

```math
\frac1k\sum_{0<|m|\le(1-\epsilon)N}\|\widehat L_{1,k,m}\|_{H_k^s(\Gamma)}\langle m/k\rangle^s\le C
```

for all $`k>k_0`$, $`N>0`$ and $`0<\epsilon<1`$? The constant may depend on the fixed curve, parametrization, amplitude bounds, $`s`$ and $`k_0`$, but must be independent of $`k,N,\epsilon`$.

This is Conjecture 11.4, with $`F_L^{s,\epsilon}(N,L)`$ expanded using (9.3)–(9.4). The bound is proved for unit-speed convex curves with nonvanishing curvature in Lemma 11.3. For general smooth curves, the available estimate in Lemma 11.1 loses a factor $`\sqrt{\log k}`$ at high frequency.

## Application

These coefficients control Kress quadrature for Helmholtz boundary integral equations. The conjecture would remove the logarithmic oversampling factor from the Dirichlet Nyström estimate in Theorem 2.26(ii), allowing the number of quadrature nodes to grow linearly with frequency under that theorem's uniformly bounded inverse assumption.

## References

1. J. Galkowski, M. Rachh and E. A. Spence, [Helmholtz boundary integral methods and the pollution effect](https://arxiv.org/abs/2507.22797v3), version 3 (21 March 2026), Theorem 2.26, §3.1, equations (9.3)–(9.6), Lemmas 11.1 and 11.3, and Conjecture 11.4.

## Status review

**Known cases:** Lemma 11.3 proves the bound for unit-speed convex curves with nonvanishing curvature. Lemma 11.1 gives the general smooth-curve estimate with a square-root logarithmic loss.

**Remaining target:** Establish the displayed constant bound for general smooth curves, with the stated uniformity in frequency and cutoffs. The current preprint explicitly retains this conjecture. Searches for the estimate, Kress quadrature, Nyström pollution and later work by the authors found no matching solution or announcement as of the check date. Indexed arXiv, Zenodo, GitHub and Palomar searches were included. Fixed-frequency convergence and conditional discrete-stability results do not establish the target.
