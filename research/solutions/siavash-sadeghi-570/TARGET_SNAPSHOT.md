# 570. The cost of continuous reconstruction on Banach unit balls

**Area:** Information-based complexity and nonlinear approximation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

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

For continuous solution maps on compact metric input sets, the corresponding inequality holds with factor $`2`$. Banach unit balls in their norm topology generally lack this compactness. The source explicitly leaves such a bound for Banach unit balls unresolved; for operators between Hilbert spaces the two errors are equal.

The latest revision [2] retains compactness in Lemma 9 and expressly notes that its compact-set theorem does not cover infinite-dimensional Banach unit balls. Results about adaptive measurements or uniformly Lipschitz encoders and decoders concern different restrictions.

No matching resolution or announcement was found in current literature, arXiv, public GitHub and native Palomar checks. Native Zenodo access returned HTTP 403; indexed searches found no matching announcement. The existing Besov stable-manifold-width problem prescribes uniform Lipschitz bounds and is distinct from this universal continuity question.
