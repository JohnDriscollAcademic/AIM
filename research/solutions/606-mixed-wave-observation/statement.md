# 606. Optimal uniform observation time for mixed finite element waves

**Area:** Numerical control and inverse problems

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Fix a bounded measurable potential $`a:[0,1]\to[0,\infty)`$, with its pointwise representative specified. For $`N\ge1`$, put $`h=(N+1)^{-1}`$ and

```math
M_h=\frac h4\mathop{\mathrm{tridiag}}\nolimits(1,2,1),\qquad K_h=\frac1h\mathop{\mathrm{tridiag}}\nolimits(-1,2,-1),\qquad L_h=h\mathop{\mathrm{diag}}\nolimits(a(h),\ldots,a(Nh)).
```

All matrices have size $`N`$. Consider arbitrary solutions $`U=(u_1,\ldots,u_N)^T`$ of

```math
M_h\ddot U+(K_h+L_h)U=0.
```

Define

```math
\mathcal E_h(U^0,U^1)=(U^0)^*(K_h+L_h)U^0+(U^1)^*M_hU^1
```

and the observation

```math
\mathcal O_{h,T}(U)=\int_0^T\left(\left|\frac{u_1(t)}h\right|^2+\left|\frac{\dot u_1(t)}2\right|^2\right)dt.
```

Determine the optimal threshold

```math
T_*(a)=\inf\{T>0:\ \exists c(a,T)>0\ \forall N\ge1\ \forall(U^0,U^1),\quad \mathcal O_{h,T}(U)\ge c(a,T)\mathcal E_h(U^0,U^1)\}.
```

In particular, is $`T_*(a)=2`$ for every such potential? The constant must be independent of the mesh size. This is the optimal-time question following Theorem 1 of [1].

## Application

The threshold determines how long one must measure at a boundary to reconstruct wave sources with stability that persists as the computational mesh is refined.

## References

1. C. Castro and S. Micu, [A mixed finite elements approximation of inverse source problems for the wave equation with variable coefficients using observability](https://doi.org/10.1007/s00211-025-01489-0), *Numerische Mathematik* **157** (2025), 1847–1895. Equations (10)–(17), Theorem 1 and following discussion, pages 1852–1854. [Preprint](https://arxiv.org/abs/2501.11352).

## Status review

**Known cases:** Theorem 1 gives a finite mesh-independent threshold for bounded nonnegative potentials. The corresponding continuous equation is observable for every $`T>2`$; earlier work treats the zero-potential mixed discretization.

**Remaining target:** Determine the sharp threshold for general variable potentials. Existence of some sufficiently large observation time does not identify its infimum.

Literature and arXiv searches, public GitHub, native Zenodo and Palomar checks found no matching solution or announcement. No equivalent catalogue problem was found.
