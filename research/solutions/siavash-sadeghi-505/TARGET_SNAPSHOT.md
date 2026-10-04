# 505. A discrete Aronson–Bénilan estimate for an upwind growth scheme

**Area:** Numerical PDE analysis and free-boundary limits

**Status:** 🔵 OPEN

**Last checked:** 2026-09-23

## Problem statement

Fix $`X,T,p_H>0`$ and $`G\in C^1([0,p_H])`$ satisfying

```math
G(p_H)=0,\qquad G'(p)\le-\alpha<0.
```

On a uniform grid $`x_i=ih`$ in $`[-X,X]`$, with $`h=X/M`$ and $`-M\le i\le M`$, consider nonnegative densities $`n_i(t)`$, pressures $`p_i=n_i^\gamma`$ with $`\gamma>1`$, and the semidiscrete scheme

```math
\dot n_i=\frac{n_{i+1/2}q_{i+1/2}-n_{i-1/2}q_{i-1/2}}h+n_iG(p_i),
\qquad q_{i+1/2}=\frac{p_{i+1}-p_i}h,
```



```math
n_{i+1/2}=\begin{cases}n_i,&q_{i+1/2}\le0,\\n_{i+1},&q_{i+1/2}>0.\end{cases}
```

Use the reflected Neumann ghost values $`n_{-M-1}=n_{-M+1}`$ and $`n_{M+1}=n_{M-1}`$, with the same pressure law at the ghost nodes.

Assume $`0\le p_i(0)\le p_H`$ and the initial-data bounds of (2.5) in [1], uniformly in $`h`$ and $`\gamma`$: for a fixed $`C_0`$, each of

```math
h\sum_i n_i(0),\quad h\sum_i p_i(0),\quad
\sum_{i=-M}^{M-1}|n_{i+1}(0)-n_i(0)|,\quad h\sum_i|\dot n_i(0)|
```

is at most $`C_0`$. Here unrestricted sums run over $`-M\le i\le M`$, and $`\dot n_i(0)`$ is evaluated using the scheme.

Does there exist $`C=C(X,T,p_H,G,C_0)`$, independent of $`h`$ and $`\gamma>1`$, such that every such solution satisfies

```math
\frac{p_{i+1}(t)-2p_i(t)+p_{i-1}(t)}{h^2}+G(p_i(t))
\ge-\frac{C}{\gamma t}
\qquad(-M\le i\le M,\;0<t\le T)?
```

Prove this uniform bound or give a counterexample under these assumptions. The target concerns the displayed fixed-grid upwind scheme, not an alternative discretization of the same continuum equation.

## Application

This one-sided control of the discrete pressure Laplacian would supply compactness estimates for convergence of a porous-medium growth scheme as the mesh is refined, with constants compatible with the stiff-pressure limit leading to a Hele-Shaw free-boundary model.

## References

1. N. David and X. Ruan, [An asymptotic preserving scheme for a tumor growth model of porous medium type](https://doi.org/10.1051/m2an/2021080), ESAIM: Mathematical Modelling and Numerical Analysis **56** (2022), 121–150. Equations (1.3), (2.1)–(2.5), and §2.3, especially the open question immediately before Theorem 2.3 on p.130; [PDF](https://www.numdam.org/item/10.1051/m2an/2021080.pdf), [preprint](https://arxiv.org/abs/2105.10376).
2. S. Kräss and R. Zacher, [Aronson–Bénilan and Harnack estimates for the discrete porous medium equation](https://arxiv.org/abs/2301.07683), 2023. Graph porous-medium equation estimates.
3. M. Di Francesco and D. Matthes, [The Aronson–Bénilan estimate for a Lagrangian particle discretization of the Porous Medium Equation](https://arxiv.org/abs/2602.06835), 2026 preprint.
4. F. Coudreuse, [An Aronson–Bénilan / Li-Yau estimate in the JKO scheme in small dimension](https://arxiv.org/abs/2604.04169), 2026 preprint.
5. W. Huang and X. Ruan, [An Onsager Variational Scheme for Pressure-Driven Tumor Growth and Hele-Shaw Limits](https://arxiv.org/abs/2607.03252), 2026 preprint.

## Status review

Reference [1] explicitly leaves the discrete estimate open for general $`\gamma>1`$ and general pressure-dependent $`G`$. Its Theorem 2.3 treats linear $`G`$ with $`\gamma=1`$ and a calculation denoted $`\gamma\approx\infty`$; the latter is not a quantified theorem covering all sufficiently large finite $`\gamma`$.

References [2]–[4] establish estimates for different graph, particle, or Wasserstein time discretizations of the source-free porous-medium equation. Reference [5] uses a different variational time step with explicit mobility and implicit pressure. Their statements do not supply the estimate for the scheme above.

Searches on 23 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar checks, located no matching resolution or announcement.
