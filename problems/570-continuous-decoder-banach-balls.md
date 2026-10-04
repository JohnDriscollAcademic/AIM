# 570. The cost of continuous reconstruction on Banach unit balls

**Area:** Information-based complexity and nonlinear approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-04

## Problem statement

Let $`X,Y`$ be real Banach spaces, let $`B_X=\{x:\|x\|_X\le1\}`$ with its norm topology, and let $`S:X\to Y`$ be bounded and linear. For $`n\ge1`$ define

```math
e_n(S)=\inf_{N,\phi}\sup_{x\in B_X}\|Sx-\phi(N(x))\|_Y,
```

where $`N:B_X\to\mathbb R^n`$ is continuous and $`\phi:\mathbb R^n\to Y`$ is arbitrary. Define $`\delta_n(S)`$ by the same infimum with the additional requirement that $`\phi`$ be continuous on all of $`\mathbb R^n`$.

Does there exist a universal constant $`C<\infty`$ such that

```math
\delta_n(S)\le C e_n(S)
```

for every $`X,Y,S,n`$? In particular, does $`C=2`$ suffice?

The measurements are taken nonadaptively: $`N`$ is a single continuous map. Both infima optimize the measurement map as well as the reconstruction. No common Lipschitz constant is prescribed for either map.

## Application

Finite-dimensional representations of functions and solutions are useful only when they can be decoded reliably. This question asks whether imposing continuity on reconstruction can cause an unbounded loss in worst-case accuracy, even when the encoded data already depend continuously on the input.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* (2026). Proposition 9.5 and the immediately following open question, published page 411 (PDF page 139).
2. D. Krieg, E. Novak and M. Ullrich, [How many continuous measurements are needed to learn a vector?](https://arxiv.org/abs/2412.06468v2), version 2, 22 September 2026. Lemma 9 and the discussion after Theorem 10.

## Status review

**Resolution:** No universal finite constant exists over the arbitrary real Banach spaces specified here. For the single inclusion $`S:\ell_1([0,1])\to\ell_2([0,1])`$, with the index set understood as discrete for sequence-space sums,

```math
\delta_n(S)=1\quad(n\ge1),\qquad e_{2K}(S)\le(K+1)^{-1/2}\quad(K\ge1).
```

The encoder uses continuous soft-thresholded moments and an arbitrary globally defined decoder. Every continuous decoder has range supported in a countable set of coordinates, which gives the lower bound even when its encoder is optimized. Thus the same operator refutes every proposed constant; $`C=2`$ already fails at $`n=8`$.

[PR #31](https://github.com/MColbrook/AIM/pull/31) supplies the [proof](../research/solutions/siavash-sadeghi-570/aim570_report.pdf) and [editable source](../research/solutions/siavash-sadeghi-570/aim570_report.tex). A [fresh independent AI audit](../research/solution_reviews/2026-10-04-active-prs/570-review.md) on 4 October 2026 checked the complete argument against this target and found no blocking mathematical defect. No independent human audit or formal verification is claimed.

Both spaces in the counterexample are nonseparable. A variant restricted to separable Banach spaces remains unaddressed. The compact-input factor-two result and Hilbert-space equality in the primary references remain consistent with this example; the audit checks the original Acta Numerica definitions and question directly.
