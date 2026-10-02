# 562. A fixed-time lower bound for Trotter splitting of the hydrogen ground state

**Area:** Numerical analysis and quantum dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

On $`L^2(\mathbb R^3)`$ let

```math
H=-\Delta-|x|^{-1},\qquad \psi_0(x)=(8\pi)^{-1/2}e^{-|x|/2}.
```

The normalized ground state satisfies $`H\psi_0=-\tfrac14\psi_0`$. For an integer $`n\ge1`$, define the first-order split evolution at the fixed final time $`t=1`$

```math
S_n=\left(e^{-i|x|^{-1}/n}e^{-i\Delta/n}\right)^n,
```

where the first factor is multiplication by its phase and the second is the free Schrödinger unitary.

Prove or disprove that there are constants $`c>0`$ and $`N`$ such that

```math
\left\|S_n\psi_0-e^{iH}\psi_0\right\|_{L^2(\mathbb R^3)}\ge c n^{-1/4}
\qquad(n\ge N).
```

This asks for the fixed-time $`t=1`$ instance of the source question. The time is held fixed while the number of steps tends to infinity. A one-step lower bound with the time tending to zero is a different assertion.

## Application

A sharp lower bound would identify an intrinsic cost of split-operator simulation for a Coulomb singularity in a physically standard state. It would explain why the nominal first-order accuracy of the method deteriorates for atomic wavefunctions.

## References

1. S. Becker, N. Galke, L. van Luijk and R. Salzmann, [Convergence rates for the Trotter splitting for unbounded operators](https://doi.org/10.1007/s10208-025-09730-w), *Foundations of Computational Mathematics* **26** (2026), 2471–2524, introduction, equation (1.3) and Corollary 2.23. [arXiv:2407.04045](https://arxiv.org/abs/2407.04045).
2. D. Fang and X. Wu, [Trotterization with many-body Coulomb interactions: convergence for general initial conditions and state-dependent improvements](https://arxiv.org/abs/2604.07704), arXiv:2604.07704v2, 24 August 2026, introduction and Section 6.

## Status review

The source [1] proves upper estimates approaching the exponent $`1/4`$ for general sufficiently regular states and identifies an analytic ground-state lower bound as open. Numerical results support the $`1/4`$ exponent. The later revision [2] proves exact one-step local error asymptotics of order $`t^{5/4}`$, while explicitly retaining the fixed-time many-step lower-bound question. Local errors may cancel during propagation, so these local asymptotics do not imply the displayed bound.

The statement isolates the ground-state, unit-time instance motivating [1]; the cited sources leave fixed-time lower bounds open without formulating a separate assertion for every positive time. Current announcement searches found no matching global lower bound.
