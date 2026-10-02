# 353. A genuinely periodic firing pattern in the delayed noisy integrate-and-fire PDE

**Area:** Mathematical neuroscience; nonlinear Fokker–Planck equations

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Do there exist $`a>0`$, $`b<0`$, delay $`d>0`$, reset and firing voltages $`V_R<V_F`$, and a period $`T>0`$, for which

```math
\partial_t p+\partial_v\bigl[(-v+bN(t-d))p\bigr]-a\partial_{vv}p=N(t)\delta_{V_R},\quad v<V_F,
```



```math
p(t,V_F)=0,\qquad N(t)=-a\partial_v p(t,V_F),\qquad\int_{-\infty}^{V_F}p(t,v)\,dv=1
```

has a nonnegative $`T`$-periodic solution with nonconstant firing rate $`N`$? Require $`p`$ to be continuous in $`v`$, classical away from $`V_R`$, with the derivative jump prescribed by the displayed distributional equation, vanishing probability flux at $`-\infty`$, and uniformly finite second voltage moment. Both $`p`$ and $`N`$ are defined for all real times so the delayed term is unambiguous.

## Application

This model represents a large inhibitory neuronal population with noise, firing resets and finite transmission time. Periodic solutions would rigorously establish self-sustained collective neural rhythms in the original density equation.

## References

1. K. Ikeda, P. Roux, D. Salort and D. Smets, [*Theoretical study of the emergence of periodic solutions for the inhibitory NNLIF neuron model with synaptic delay*](https://mna.episciences.org/10212), Mathematical Neuroscience and Applications 2 (2022), introduction and Gaussian-wave reduction.
2. J. A. Carrillo and P. Roux, [*Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory*](https://arxiv.org/abs/2501.06015), Mathematical Models and Methods in Applied Sciences 35 (2025), 403–584, §1.7.2.
3. C. Rieutord and D. Salort, [*Asymptotic dynamics of inhibitory networks for the NNLIF Model in the large-delay limit*](https://arxiv.org/abs/2606.17611), preprint (2026), §1.2, Theorem 1 and §7.

## Status review

**Resolution (2026-10-02):** A nonconstant positive periodic branch is constructed for an admissible choice of inhibitory coupling, delay and thresholds in the full delayed NNLIF PDE. The proof includes the reset operator, infinite-dimensional bifurcation argument, positivity and tail conditions. This is an existence result for some parameters, with negative thresholds allowed by the statement, not a claim for every fixed parameter choice.

**Proof and review:** [Accepted solution](../research/solutions/353-delayed-nnlif-periodic-branch/aim353_delayed_nnlif_periodic.pdf); [fresh mathematical audit](../research/solution_reviews/2026-10-02-active-prs/353-review.md); [PR #23](https://github.com/MColbrook/AIM/pull/23). The audit records the pinned submission, target comparison and any supporting computations.

**Evidence:** Solved under the documented-independent-audit convention. The review was performed by AI; it does not assert human peer review, publication, proof-assistant verification or novelty priority. The problem retains its existing page and ID.

### Previous status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using delayed NNLIF periodic existence, Hopf bifurcation, and the cited authors. The 2022 theorem concerns a reduced delay equation, not the reset PDE. The 2025 survey explicitly reports that periodicity for the full model remains unproved. The 2026 paper proves oscillation between pseudo-equilibria on arbitrary finite rescaled intervals as the delay tends to infinity; this does not produce an exactly periodic orbit at any fixed finite delay. No later matching existence theorem was located.
