# Target identity and theorem-to-target comparison

This is a mathematical paraphrase of the source, not a byte-identical repository
snapshot. Source accessed 2026-10-02:
https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/637-elo-density.md

**Title:** Absolute continuity of stationary Elo ratings.
**Observed active ID:** 637.
**Observed badge:** Partial.
**Source last-checked field:** 2026-09-24.
**Repository commit:** `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.

For `N >= 2`, a zero-sum skill vector `rho`, and positive `c,K` with `K*c < 1`,
consider the zero-sum Elo chain. At each step a uniformly chosen ordered player
pair `(i,j)` receives a fresh independent binary score, with

`P(S=1 | i,j) = (1+tanh(c*(rho_i-rho_j)))/2`.

Player `i` gains `K*(S-tanh(c*(X_i-X_j)))`, and player `j` loses that amount.
The target asks whether the invariant probability has a density relative to
Lebesgue measure on the zero-sum hyperplane for every admissible parameter set.

The counterexample chooses `N=2`, `rho=(0,0)`, `c=1/2`, `K=9/10`.
Writing the vector as `(x,-x)` gives the two maps

`F_plus(x)=x-(9/10)*tanh(x)+9/10`,
`F_minus(x)=x-(9/10)*tanh(x)-9/10`,

with equal probabilities. Reversing the player order just exchanges the two
fair outcomes. The map from `x` to `(x,-x)` is a linear bi-Lipschitz bijection
onto the zero-sum line. Thus singularity of the scalar invariant law proves
failure of precisely the requested absolute-continuity property.
