# 523. Removing the logarithmic loss in Helmholtz Nyström estimates

**Area:** Numerical PDEs and boundary integral equations

**Status:** ✅ SOLVED

**Last checked:** 2026-10-04

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

**Resolution:** The displayed general smooth-amplitude bound is false. One fixed smooth amplitude and one fixed smooth closed curve with a flat arc and a variable-speed parametrization make the target quantity grow at least as $`c\sqrt{\log k}`$ at $`s=0`$, with admissible integer cutoffs.

[PR #29](https://github.com/MColbrook/AIM/pull/29) supplies the [proof](../research/solutions/siavash-sadeghi-523/aim523_report.pdf) and [editable source](../research/solutions/siavash-sadeghi-523/aim523_report.tex). A [fresh independent AI audit](../research/solution_reviews/2026-10-04-active-prs/523-review.md) on 4 October 2026 checked the complete argument against this target and found no blocking mathematical defect. No independent human audit or formal verification is claimed.

This resolves the arbitrary smooth-amplitude formulation stated here. The example is not identified with a physical single-layer or double-layer Helmholtz kernel and does not establish a numerical oversampling lower bound for every Nyström method. The positive-curvature unit-speed case remains valid. The [28 September 2026 revision of the primary paper](https://arxiv.org/abs/2507.22797v4) retains Conjecture 11.4; the audit checks both cited versions and the precise scope distinction.
