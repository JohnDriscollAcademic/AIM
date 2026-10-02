# AIM 561: fixed-time hydrogen Trotter lower bound

Date: 2026-10-02. Reviewer: OpenAI Codex (AI), reviewing the complete argument afresh for the repository. This is a mathematical audit, not human peer review, formal verification, or a claim of novelty priority.

**Decision:** accept the counterexample to the proposed lower bound; mark the existing AIM 561 page **Solved**. The proof establishes an upper bound of order `n^(-3/8)` at the specified final time 1, hence the error is `o(n^(-1/4))`.

**Submission:** [PR #18](https://github.com/MColbrook/AIM/pull/18), head `823ea0c6f9151792238d8ccbe7d64ea7d66faf5d`. Reviewed [PROOF.md](../../solutions/562-hydrogen-trotter-disproof/PROOF.md), its statement and supporting review. The package's original ID 562 and proposed archive ID 651 are historical; the current target is [AIM 561](../../../problems/561-hydrogen-trotter-lower-bound.md) at base `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`. Only the proof package is integrated from the PR; its catalogue renumbering is superseded by the current policy of retaining pages and IDs.

## Analytic audit

The signs and operator order match the target: with `K=-Delta+1/4`, `V=1/r`, `h=1/n`, `U=exp(ihK)`, `W=exp(ihV)` and `lambda=exp(-ih/4)`, the single step is `T=lambda W^{-1}U`. The normalized state has `K psi=V psi` and Fourier transform `1/[2 pi (|xi|^2+1/4)^2]` under the unitary convention. Both terms in this identity are in L2. No square of the Coulomb potential is applied to the state.

For `d=(U-I-ihK)psi`, the Fourier multiplier bound is `C min(h^2,h/a)`, where `a=|xi|^2+1/4`. Direct radial integration gives the three estimates used: `||d||=O(h^(5/4))`, the tail `O(h R^(-1/2))`, and the truncated gradient norm `O(h R^(1/2))`. I checked the radial substitution in the resonant-set integral, including its `h^(5/2)/(2 pi)` prefactor. Near zero its dominating integrand is `z^(1/2)`; near positive multiples of `2 pi` it is bounded by `z^(-3/2)`. Summing the resonance intervals gives squared mass `O(h^(5/2) delta)`, uniformly in h and delta.

Removing the resonant set and frequencies above R makes `eta_hat=-d_hat/(exp(iha)-1)` an H1 function. Its norm and gradient bounds follow by dividing by delta; no differentiation of the discontinuous Fourier cutoff is needed. The exact cancellation is `(U-I)eta=-Pd`. Substituting `psi+eta` into `(T-lambda)` leaves precisely the high-frequency/resonant remainder, the potential defect `q=(W-I-ihV)psi`, and `(W-I)eta`.

Splitting physical space at radius h bounds `||q||` by `C h^(3/2)`: inside use a linear phase bound, outside use the quadratic remainder. Hardy's inequality gives `||(W-I)eta|| <= 2h ||grad eta||`. The cutoff proof of Hardy's inequality extends to H1 by density. Unitary telescoping multiplies the corrected residual by n and adds `2||eta||` for the change of initial state; it makes no unjustified assertion about accumulation of local errors.

The resulting five terms are

```
h^(5/4)/delta + R^(-1/2) + h^(1/4) delta^(1/2)
    + h^(1/2) + h R^(1/2)/delta.
```

For `delta=h^(1/4)` and `R=h^(-3/4)`, their exponents are respectively `1, 3/8, 3/8, 1/2, 3/8`. The estimates hold for all sufficiently small h, so this refutes the eventual positive lower bound for the entire sequence, not merely for a subsequence. I found no gap in this argument.

## Sources and scope

Checked the primary records for [Becker, Galke, Salzmann and van Luijk, arXiv:2407.04045v2](https://arxiv.org/abs/2407.04045v2), including the linked [published DOI](https://doi.org/10.1007/s10208-025-09730-w), and [Fang and Wu, arXiv:2604.07704v2](https://arxiv.org/abs/2604.07704v2). The latter's one-step `5/4` local lower bound does not imply a fixed-time many-step lower bound. The submitted proof supplies its own analytic estimates and does not depend on numerical simulations or on an unproved rate assertion from either reference.

No assertion of an optimal `3/8` rate, a lower bound of that order, or an operator-norm result is established. The accepted conclusion is exactly the disproof requested by AIM 561.
