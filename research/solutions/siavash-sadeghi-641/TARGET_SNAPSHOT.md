# 641. Bos's cubic and quartic simplex interpolation nodes

**Area:** Multivariate approximation and optimal experimental design

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`S_d=\mathop{\mathrm{conv}}\nolimits\{v_1,\ldots,v_{d+1}\}`$ be a nondegenerate real $`d`$-simplex. Specify nodes by their barycentric coordinates. In each of the following lists, include all distinct coordinate permutations, append zero coordinates, and omit a type requiring more than $`d+1`$ coordinates.

The cubic set $`F_{3,d}`$ comprises

```math
(1),\qquad (t,1-t),\qquad (1/3,1/3,1/3),\qquad t=\frac{1+1/\sqrt5}{2}.
```

The quartic set $`F_{4,d}`$ comprises

```math
(1),\qquad (1/2,1/2),\qquad (s,1-s),\qquad (a,b,b),\qquad (1/4,1/4,1/4,1/4),
```

where

```math
s=\frac{1+\sqrt{3/7}}2,\qquad a=\frac{4+\sqrt5}{11},\qquad b=\frac{7-\sqrt5}{22}.
```

For $`k=3,4`$, these are unisolvent sets of $`N_{k,d}=\binom{d+k}{k}`$ nodes for the real polynomials of total degree at most $`k`$. Write $`\ell_x^{(k,d)}`$ for the cardinal polynomial satisfying $`\ell_x^{(k,d)}(y)=\delta_{xy}`$ at the nodes.

Resolve the following conjectures of Bos:

1. **Cubic Fejér property:** for every $`d\ge1`$ and $`z\in S_d`$,

```math
\sum_{x\in F_{3,d}}|\ell_x^{(3,d)}(z)|^2\le1.
```

2. **Quartic Fejér property in dimension three:** for every $`z\in S_3`$,

```math
\sum_{x\in F_{4,3}}|\ell_x^{(4,3)}(z)|^2\le1.
```

3. **Quartic Fekete property:** for every $`d\ge1`$, $`F_{4,d}`$ maximizes the absolute Vandermonde determinant among all $`N_{4,d}`$-point configurations in $`S_d`$. The polynomial basis is any fixed basis of $`\mathbb P_4(\mathbb R^d)`$.
4. **Quartic fourth-power bound:** for every $`d\ge1`$ and $`z\in S_d`$,

```math
\sum_{x\in F_{4,d}}|\ell_x^{(4,d)}(z)|^4\le1.
```

These are related assertions about prescribed node families. The Fejér property implies both the Fekete property and the fourth-power bound in the same degree and dimension. The Fekete property implies $`|\ell_x(z)|\le1`$ individually; that necessary condition alone is insufficient for either of the other properties.

## Application

Explicit extremal interpolation nodes support stable polynomial approximation on simplicial elements. Fejér sets also give equally weighted optimal experimental designs with the minimum possible number of support points.

## References

1. L. Bos, [On Fekete points for a real simplex](https://doi.org/10.1016/j.indag.2022.11.003), *Indagationes Mathematicae* **34**(2) (2023), 274–293; [arXiv:2205.06498](https://arxiv.org/abs/2205.06498), Sections 3–4, Proposition 3.1 and Conjectures 4.2, 4.3 and 4.6. The 2022 preprint gives the node definitions on pp.8 and 12 and the conjectures on pp.9 and 14–15.

## Status review

**Known cases:** The cubic Fejér property holds for $`1\le d\le28`$. The quartic Fejér property holds for $`d\le2`$, but fails for $`d\ge4`$: the source gives a violation at the four-dimensional centroid, which persists on faces in higher dimensions. The quartic Fekete and fourth-power questions remain meaningful in those dimensions.

**Remaining target:** Settle the cubic assertion for $`d\ge29`$ and the three stated quartic assertions beyond their known cases. These questions are kept together to retain their logical relationships. Targeted literature, arXiv, GitHub, Zenodo and Palomar checks found no matching solution announcement; no equivalent catalogue entry was found. The full source article was read for discovery.
