# AIM 114: supporting algebra, Gaussian mixture, and length transfer

This is a **partial formalization** of Sidney Holden's six-page manuscript
*A non-Gaussian limit for nodal surplus*, revised v0.3 (2026-10-02). The current
package contains eleven results in three blocks. It does **not** yet prove
that the graph's spectral surplus converges to the constructed non-Gaussian
law. The complete source correspondence and remaining gaps are in
[NUMERICAL_TARGETS.md](NUMERICAL_TARGETS.md).

## What is proved

| Block | Actual mathematical content | Frozen scope and proof explanation |
| --- | --- | --- |
| Initial algebra: 3 results | Local three-edge sign-count identity, exact four-sign second moment, and strict integral kurtosis inequality | [Initial targets](NUMERICAL_TARGETS.md#the-initial-three-algebraic-results) |
| Prescribed lengths and transfer: 5 results | The exact prime-root core fraction bound; actual convex probability mixture; bounded integral error; actual standardized second/fourth moment error tending to zero | [Transfer boundary](TRANSFER_TARGETS.md), [proof explanation](TRANSFER_PROOF.md) |
| Actual Gaussian mixture: 3 results | Standard Gaussian fourth moment; an actual product-space pushforward law with integrable powers, mean zero, second moment one, and fourth-moment formula; nonequality to the standard Gaussian for bounded nonconstant mixing variance | [Mixture boundary](MIXTURE_TARGETS.md), [proof explanation](MIXTURE_PROOF.md) |

The last block proves a statement about an actual probability distribution.
It derives positive normalization and variance from the source bounds and
intrinsic nonconstancy of the mixing variable. It does not assume mixture
moment identities or a non-Gaussian conclusion. The transfer block uses the
actual prescribed prime-root lengths and integrals, not unspecified scalar
errors. Identifying their inputs with the graph's spectral law and concrete
mixing variable remains a separate obligation.

The solution imports only the proof modules under `AIM/P114/`. The combined
[Challenge.lean](Challenge.lean) has deliberate statement placeholders and is
never imported by the solution. The separate [TransferChallenge.lean](TransferChallenge.lean)
and [MixtureChallenge.lean](MixtureChallenge.lean) retain the exact extension
boundaries independently approved before implementation. Every advertised
result is listed in [comparator.json](comparator.json), with no replaceable
definitions.

## Review and verification

Each block received two independent AI statement reviews before proof
implementation and a successful boundary typecheck. Independent final
referees inspect the actual proofs and separately rebuild, re-elaborate, and
print their transitive axioms. Reports identify their exact scope and source
hashes in [reviews/](reviews/).

The expanded local build passes for all eleven results with exactly
`propext`, `Classical.choice`, and `Quot.sound`. The earlier isolated Linux
[verification](verification/linux-2026-10-05/README.md) covers the initial three
results only; it is historical evidence, not a certificate for the new
extensions. See the [verification record](verification/README.md) for the
current gate status. No whole-problem Lean-verified status is claimed.

The pinned project uses Lean 4.33.1, Mathlib, LeanCert, and immutable transitive
dependencies. To build locally from this directory:

```sh
lake exe cache get
lake build Challenge Solution
lake env lean Solution.lean
```

The final command prints each theorem's transitive axioms. The repository's
[isolated Linux workflow](../../../docs/lean/README.md) remains the authoritative
mechanical check for each expanded immutable proof revision.

## Further formalization

The [dependency assessment](FORMALIZATION_ROADMAP.md) and
[probability roadmap](PROBABILITY_ROADMAP.md) record concrete library support
and next steps. Existing Mathlib quadratic forms, signature invariance,
and multigraph APIs support further finite spectral reduction. The compact
metric-graph operator, spectral-to-phase measure theorem, stable-vector law,
and random-evaluation process limit still need substantial new proofs. A lack
of a packaged theorem is not treated as an impossibility result or an axiom.

Mathematical manuscript author: **Sidney Holden**, as confirmed by the user.
Formalization implementation: **Codex for Sidney Holden**, AI assisted.
Referee reports identify their separate AI authors; no human referee
endorsement or full formal verification is implied.
