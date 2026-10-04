# 553. Minimum number of continuous adaptive measurements for vector recovery

**Area:** Information-based complexity and approximation theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-04

## Problem statement

For $`m\ge2`$, let $`N(m)`$ be the smallest integer $`n`$ such that, for every $`\varepsilon>0`$, there exists a deterministic algorithm recovering each $`x\in\mathbb R^m`$ with Euclidean error at most $`\varepsilon`$ from at most $`n`$ exact real-valued measurements. The measurements are sequential:

```math
y_j=\lambda_{j,y_1,\ldots,y_{j-1}}(x),
```

where, for every fixed history, $`\lambda_{j,y_1,\ldots,y_{j-1}}:\mathbb R^m\to\mathbb R`$ is continuous. The choice of the next functional may depend arbitrarily on the preceding values; no continuity in the history is imposed. The reconstruction $`\Phi:\mathbb R^n\to\mathbb R^m`$ is unrestricted, and the required guarantee is

```math
\sup_{x\in\mathbb R^m}\|x-\Phi(y_1,\ldots,y_n)\|_2\le\varepsilon.
```

Determine $`N(m)`$, or its sharp asymptotic growth as $`m\to\infty`$. In particular, is $`N(m)`$ unbounded, or can an absolute constant number of such measurements achieve arbitrary precision in every dimension?

At the time of listing, the published bounds were

```math
2\le N(m)\le \lceil\log_2 m\rceil+1.
```

The upper bound is the improved version in [2, Theorem 1, September 2026 revision]. The unresolved case $`m=3,n=2`$ is part of this single problem, rather than a separate entry.

## Application

This question identifies the information complexity of adaptive nonlinear sensing when measurements are exact. It separates the benefit of choosing subsequent measurements from the familiar requirement of $`m`$ linear measurements for uniform recovery of arbitrary vectors.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* **35** (2026), 273–457. Section 10.3, especially Theorem 10.6 and Remark 10.7.
2. D. Krieg, E. Novak and M. Ullrich, [How many continuous measurements are needed to learn a vector?](https://arxiv.org/abs/2412.06468), arXiv:2412.06468v2, 22 September 2026. Theorem 1 and Section 3, page 7.

## Status review

**Resolution:** The sharp-asymptotic alternative in the target is established:

```math
\lfloor\log_2m\rfloor+1\le N(m)\le\lceil\log_2m\rceil+1,
\qquad N(m)\sim\log_2m.
```

The lower bound applies to the full stated adaptive model: every algorithm using $`n`$ measurements has infinite worst-case error on $`\mathbb R^m`$ when $`m\ge2^n`$. It assumes continuity only in the input along each fixed history; history dependence and decoding remain unrestricted. The upper bound is [2, Theorem 1].

[PR #30](https://github.com/MColbrook/AIM/pull/30) supplies the [proof](../research/solutions/siavash-sadeghi-553/aim553_report.pdf) and [editable source](../research/solutions/siavash-sadeghi-553/aim553_report.tex). A [fresh independent AI audit](../research/solution_reviews/2026-10-04-active-prs/553-review.md) on 4 October 2026 checked the complete argument against this target and found no blocking mathematical defect. No independent human audit or formal verification is claimed.

Exact values at powers of two follow, $`N(2^r)=r+1`$. The one-integer gap at other dimensions, including $`2\le N(3)\le3`$, remains open. The solved label records the expressly permitted sharp-asymptotic resolution and does not claim every exact value is determined.
