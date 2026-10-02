# 043. A nearly cubic Schur algorithm using only linear precision

**Area:** Stable algorithms for general eigenproblems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

For $`A\in\mathbb C^{n\times n}`$ with $`\|A\|_2\le1`$ and $`0<\delta<1`$, construct a randomized floating-point algorithm that, with probability at least $`0.99`$, returns $`Q,T\in\mathbb C^{n\times n}`$, with $`T`$ upper triangular, such that

```math
\|Q^*Q-I\|_2\le\delta,\qquad \|A-QTQ^*\|_2\le\delta.
```

Require $`O(n^3\log^c(n/\delta))`$ arithmetic operations and mantissa length $`O(\log(n/\delta))`$ bits, with universal constants, for every input, independently of eigenvalue gaps and nonnormality. Input entries are supplied to the working precision; input rounding must be included in the error bound. As usual in this floating-point model, exclude overflow and underflow.

## Application

An end-to-end error guarantee at modest precision would make fast Schur computation dependable even for severely nonnormal matrices, central to stability analysis and matrix functions.

## References

1. J. Banks, J. Garza-Vargas, A. Kulkarni and N. Srivastava, [Pseudospectral shattering, the sign function, and diagonalization in nearly matrix multiplication time](https://doi.org/10.1007/s10208-022-09577-5), Foundations of Computational Mathematics 23 (2023), 1959–2047. General finite-precision baseline.
2. J. Demmel, I. Dumitriu and R. Schneider, [Generalized pseudospectral shattering and inverse-free matrix pencil diagonalization](https://doi.org/10.1007/s10208-024-09682-7), Foundations of Computational Mathematics (2024). Inverse-free approach.
3. N. Amsel et al., [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394), 2026; Problem 3.3.

## Status review

**Resolution (2026-10-02):** Solved in [NLA IE-08](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/e375a6fc0a12df52c4f5a38b53df78b837e1c390/eigenvalues-and-inverse-problems/IE-08/README.md#resolution--2026-09-11). [Complete proof](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/e375a6fc0a12df52c4f5a38b53df78b837e1c390/eigenvalues-and-inverse-problems/IE-08/solution.md) · [Independent review](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/e375a6fc0a12df52c4f5a38b53df78b837e1c390/references/colbrook-additional-2026-09-11/verification/reviews/IE-08-review.md).

Theorem 1 supplies the stated work, precision, probability and residual guarantees, including input rounding and without spectral-gap assumptions. Smaller tolerances cover this entry's full tolerance range. The NLA repository records an independent AI audit; this is not Lean verification.

### Previous status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Problem 3.3 asks for logarithmic working precision in a general backward-stable decomposition. Hermitian linear-precision results do not cover arbitrary A. No subsequent general solution was located.

Searches included: `Schur form precision 2026`; `Schur linear precision diagonalization 2026`; `general matrix eigenproblem logarithmic bits backward stable`. This is a documented literature check, not a certification that no solution exists.
