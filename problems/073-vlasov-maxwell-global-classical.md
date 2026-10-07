# 073. Large-data global classical solutions of relativistic Vlasov–Maxwell

**Area:** Kinetic theory and plasma physics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Set $`\widehat v=v/\sqrt{1+|v|^2}`$. For nonnegative $`f_0\in C_c^\infty(\mathbb R_x^3\times\mathbb R_v^3)`$ and smooth finite-energy electromagnetic data with bounded derivatives satisfying
$`\nabla\cdot E_0=\int f_0\,dv`$ and $`\nabla\cdot B_0=0`$, does the system

```math
\partial_tf+\widehat v\cdot\nabla_x f+
(E+\widehat v\times B)\cdot\nabla_v f=0,
```



```math
\partial_tE=\nabla\times B-j,\quad
\partial_tB=-\nabla\times E,\quad
j=\int\widehat v f\,dv
```

have a classical solution for all $`t\ge0`$? Require the propagated Gauss constraints, finite field energy, and bounded particle-momentum support on every finite time interval. There is no smallness or symmetry assumption; units normalize the particle mass, charge and speed of light.

## Application

This is the self-consistent collisionless model for relativistic plasmas; momentum growth controls whether classical particle-field evolution remains predictive.

## References

- [Daniel Han-Kwan, Toan T. Nguyen and Frédéric Rousset, *Linear Landau Damping for the Vlasov-Maxwell System in R³* (Annals of PDE, 2025), introduction and references to the classical continuation theory](https://doi.org/10.1007/s40818-025-00217-z).
- [Luis Silvestre, *Regularity estimates and open problems in kinetic equations* (2022), kinetic regularity background](https://arxiv.org/abs/2204.06401).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Han-Kwan–Nguyen–Rousset explicitly describe the three-dimensional large-data classical Cauchy problem as open in September 2025. Their linearized damping result is a different assertion. Known weak-solution, small-data and lower-dimensional results do not supply the stated continuation.

Searches run on 2026-09-08: `site.arxiv.org Vlasov Maxwell open problem 2025`; `Vlasov Maxwell global classical solutions open problem 2025 2026`. This is a literature search, not a proof that no solution exists.

OpenAI's September 23, 2026 preprint *Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system* establishes global existence and uniqueness of classical solutions for the three-dimensional one-species relativistic Vlasov–Maxwell system under the hypotheses stated above. The solution remains smooth on every finite time interval and has compact particle-phase support there, with no smallness, symmetry, or neutrality assumption.

OpenAI claims The main result has been formally verified in Lean; the accompanying formalization is `VlasovMaxwell.lean`.

Paper: https://github.com/openai/math/blob/main/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf

Lean documentation: https://github.com/openai/math/blob/main/lean/docs/362.md
