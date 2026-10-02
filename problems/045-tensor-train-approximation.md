# 045. Improve the worst-case tensor-train approximation factor

**Area:** Tensor computation and high-dimensional models

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

For a real order-$`d`$ tensor $`A\in\mathbb R^{n_1\times\cdots\times n_d}`$, $`d\ge3`$, fix rank bounds $`r_1,\ldots,r_{d-1}`$. Let $`\mathcal T_r`$ be the tensors whose matricization across the split $`(1,\ldots,j)\mid(j+1,\ldots,d)`$ has matrix rank at most $`r_j`$ for every $`j`$. Set $`e_r(A)=\min_{X\in\mathcal T_r}\|A-X\|_F`$.

Does a polynomial-time algorithm return $`\widehat A\in\mathcal T_r`$ with

```math
\|A-\widehat A\|_F^2<(d-1)\,e_r(A)^2
```

for every input with $`e_r(A)>0`$, over all dimensions and rank bounds? Use the standard arithmetic-operation model for dense tensor approximation, with polynomial work in the dense input size and rank data. When $`e_r(A)=0`$, exact recovery is required in exact arithmetic. The conventional sequential SVD guarantee uses a non-strict inequality with factor $`d-1`$. Any strict improvement is requested; the margin need not be uniform over inputs or dimensions.

## Application

Tensor trains represent high-dimensional states and functions in quantum dynamics, stochastic PDEs and data compression. A better guaranteed factor would make rank budgets more predictable without assuming favorable input structure.

## References

1. I. V. Oseledets, [Tensor-Train Decomposition](https://doi.org/10.1137/090752286), SIAM Journal on Scientific Computing 33 (2011), 2295–2317; Theorem 2.2 and Corollary 2.4.
2. N. Amsel et al., [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394), 2026; Problem 6.1.
3. G. Yu, J. Feng, Z. Chen, X. Cai and L. Qi, [A randomized block Krylov method for tensor train approximation](https://doi.org/10.3389/fams.2026.1824146), Frontiers in Applied Mathematics and Statistics 12 (2026). Recent approximation algorithms.

## Status review

**Resolution (2026-10-02):** Solved in [NLA TR-04](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/e375a6fc0a12df52c4f5a38b53df78b837e1c390/tensor-computations/TR-04/README.md#resolution--2026-09-11). [Complete proof](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/e375a6fc0a12df52c4f5a38b53df78b837e1c390/references/colbrook-recovered-tensors-2026-09-11/manuscripts/TR-04.pdf) · [Independent review](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/e375a6fc0a12df52c4f5a38b53df78b837e1c390/references/colbrook-recovered-tensors-2026-09-11/verification/reviews/TR-04-review.md).

Theorem 3 and Sections 2–4 provide the requested pointwise strict improvement at unchanged ranks, with exact recovery at zero optimum, in the exact arithmetic/SVD model. The NLA repository records an independent AI audit; this is not Lean verification.

### Previous status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Problem 6.1 explicitly asks even for a pointwise strict improvement of the conventional factor, with larger improvements also of interest. This entry takes its tensor-train special case and separates exact inputs to avoid demanding the impossible inequality $`0<0`$. The May 2026 Krylov paper concerns randomized construction and error estimates; no algorithm meeting the stated guarantee for every input was located.

Searches included: `tensor train approximation 2026 optimal polynomial`; `tensor train approximation sqrt d lower bound 2026`; `randomized block Krylov tensor train approximation`. This is a documented literature check, not a certification that no solution exists.
