# AIM 114: three supporting Lean lemmas

This is a **partial formalization** of Sidney Holden's six-page manuscript
*A non-Gaussian limit for nodal surplus*, revised v0.3 (2026-10-02). It proves
three exact supporting results. It does **not** prove the quantum-graph
counterexample, construct the spectral law, or establish its limiting law.
The complete gap list and source correspondence are in
[NUMERICAL_TARGETS.md](NUMERICAL_TARGETS.md).

## Results and proof approach

- `AIM.P114.module_count_identity` proves the local three-edge sign-count
  identity in manuscript Lemma 1. Two private sign lemmas reduce products and
  quotients to the signs of their nonzero inputs; exact ring arithmetic
  finishes the count. It does not prove the global spectral/inertia identity.
- `AIM.P114.sign_second_moment` proves the four equally weighted sign cases
  behind the triangle-event expression for `v(r)`. The proof splits the
  orders of the positive magnitudes and the two triangle boundaries, then
  checks exact rational values with linear arithmetic. The excluded
  equalities are explicit hypotheses; their probability zero is not proved.
- `AIM.P114.variance_mixture_kurtosis` expands the integral of `(V - EV)^2`
  using Bochner-integral linearity on a probability space and derives
  `3 E[V²] / E[V]² > 3` from positive mean and positive centered second
  moment. No scalar in this theorem stands in for an unmodeled expectation.
  The identification with the fourth moment of the manuscript's Gaussian
  mixture remains unformalized.

The solution imports only [AIM/P114/Proof.lean](AIM/P114/Proof.lean), which
imports [Definitions.lean](AIM/P114/Definitions.lean). The separate
[Challenge.lean](Challenge.lean) has deliberate statement placeholders and
is never imported by the solution. All three advertised results are listed
in [comparator.json](comparator.json), with no replaceable definitions.

## Review and verification

Two independent AI agents approved the exact definitions, challenge
signatures, and numerical targets before proof implementation; their reports
are in [reviews/](reviews/). They reviewed both the complete manuscript and
the canonical source-problem snapshot. The exact boundary typechecked before
proof implementation; the record is
[verification/boundary-typecheck.log](verification/boundary-typecheck.log).
Both independent final proof reviews, local builds, and the isolated Linux
Comparator/kernel verification passed for these three supporting results.
See [verification/](verification/) for the run records and
[retained Linux evidence](verification/linux-2026-10-05/README.md) for the
verified revision and original artifacts. This partial package does not
justify labeling AIM 114 “Lean verified.”

The project pins Lean 4.33.1, Mathlib, LeanCert, and all transitive dependencies
through the committed toolchain and manifest. To build locally from here:

```sh
lake exe cache get
lake build Challenge Solution
lake env lean Solution.lean
```

The final command prints the transitive axioms for each theorem. The verified
axiom set is `propext`, `Classical.choice`, and `Quot.sound` only. The repository's
Linux sandbox/Comparator workflow is the authoritative mechanical check;
see [the setup guide](../../../docs/lean/README.md).

## Reuse and credit

The pinned Mathlib was searched before implementation, including
`Data/Real/Sign.lean`, `Data/Sign/Basic.lean`,
`MeasureTheory/Integral/Bochner/Basic.lean`, and
`Probability/Moments/Variance.lean`. The proof uses existing Bochner-integral
linearity, integrability, sign/order, and arithmetic APIs. The tiny local
`nonzeroSign` extension assigns `+1` at zero; all source-facing sign uses have
explicit nonzero hypotheses. It is a project-local convenience and is not
proposed as a replacement for Mathlib's three-valued sign API.

Mathematical manuscript author: **Sidney Holden**, as confirmed by the user.
Formalization implementation: **Codex for Sidney Holden**, AI assisted.
The statement and proof referee reports identify their separate AI authors;
no human referee endorsement or full formal verification is implied.
