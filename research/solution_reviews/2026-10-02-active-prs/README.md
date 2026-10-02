# Review of active solution pull requests, 2 October 2026

This review covers the eight pull requests that were open when the review began: **#17–#24**. Closed requests were not reconsidered. The complete arguments were checked against their exact catalogue targets, with separate AI review agents for the larger analytic and certificate proofs. Supplied self-reviews and successful program runs were not treated as substitutes for checking the mathematical argument.

Seven previously open targets are resolved, one target receives a partial result, and one already solved target receives an additional proof. All existing problem IDs and pages are retained. Together with the previously requested in-place NLA labels for 043 and 045, the catalogue contains **642 open targets and 23 solved entries**, covering the same 665 identities.

## Decisions

| PR | Current problem | Decision and scope | Fresh audit |
| --- | --- | --- | --- |
| [#17](https://github.com/MColbrook/AIM/pull/17) | [605: mixed finite-element waves](../../../problems/605-mixed-wave-optimal-observation-time.md) | **Solved:** optimal observation-time infimum equals 2; no endpoint claim needed. | [605](605-review.md) |
| [#18](https://github.com/MColbrook/AIM/pull/18) | [561: hydrogen Trotter splitting](../../../problems/561-hydrogen-trotter-lower-bound.md) | **Solved:** an upper bound of order n^(-3/8) disproves the proposed n^(-1/4) lower bound. | [561](561-review.md) |
| [#19](https://github.com/MColbrook/AIM/pull/19) | [665: Fisher-score approximation](../../resolved/665-fisher-score-gradient-closure.md) | **Additional proof accepted:** existing Solved status and count unchanged. | [665](665-additional-proof-review.md) |
| [#20](https://github.com/MColbrook/AIM/pull/20) | [022: polygonal Steklov optimization](../../../problems/022-steklov-polygon-optimizer.md) | **Partially resolved:** unique optimizer proved for triangles; n>=4 remains open. | [022](022-triangles-review.md) |
| [#21](https://github.com/MColbrook/AIM/pull/21) | [534: verbose persistence](../../../problems/534-verbose-persistence-pullback-triangle.md) | **Solved:** counterexample to the triangle inequality in every positive degree. | [534](534-review.md) |
| [#22](https://github.com/MColbrook/AIM/pull/22) | [489: D-stable Lotka–Volterra systems](../../../problems/489-lotka-volterra-d-stable-global-attraction.md) | **Solved:** a strictly positive periodic orbit disproves global attraction. | [489](489-review.md) |
| [#23](https://github.com/MColbrook/AIM/pull/23) | [351: Burgers profiles](../../../problems/351-burgers-entire-limits.md); [353: delayed NNLIF](../../../problems/353-delayed-nnlif-periodic.md) | **Both Solved:** arbitrary-measure profile realization; a periodic PDE branch for some admissible parameters. | [351](351-review.md), [353](353-review.md) |
| [#24](https://github.com/MColbrook/AIM/pull/24) | [637: stationary Elo ratings](../../../problems/637-elo-density.md) | **Solved:** an admissible binary-score logistic example has a singular continuous stationary law. | [637](637-review.md) |

All decisions use the repository's documented-independent-audit convention. These are **AI mathematical audits**, not human peer review, publication, Lean verification or certification of novelty priority. Individual reports identify imported results, reproduced computations, exact target scope and limitations. No unresolved mathematical gap was found in the accepted claims.

## Pinned inputs and integration

The target baseline is `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`. Original package directory numbers sometimes differ from current catalogue IDs; the decision table above and the individual reports provide the mapping.

| PR | Reviewed head |
| --- | --- |
| 17 | `ebe4b6bee4040cc0c0a83249cfedc1653380dac0` |
| 18 | `823ea0c6f9151792238d8ccbe7d64ea7d66faf5d` |
| 19 | `5a1ebd317fafc26225948a14838da7302bc5847c` |
| 20 | `3889757da4a06da20011203b25c3bf9e6b0f386f` |
| 21 | `5f6ade2be66c50663ed57371771c139d9222cde4` |
| 22 | `7faf58307c22882ccd730eae421acb61fca3f43d` |
| 23 | `e8e9c121188cff156922ab06a4bd8333c5ec61dc` |
| 24 | `09eb03055ae12f58be5423c1c34b06ee90020b89` |

The mathematical packages from #18 and #22 are accepted, while their stale archive moves and broad renumbering are superseded by the current in-place status policy. Their current-record links are repaired and affected manifest hashes refreshed. Their historical proposed mappings remain labelled as historical evidence. Other submitted pending-review wording is retained as part of the original packages; the problem pages and this dated review record state the accepted disposition.

The triangle proof's two descriptions of 320-bit arithmetic are corrected: imports in the standard driver leave the Arb context at **128 bits**, whereas `cert_E.py` alone sets 320 bits. The full rigorous certificate passed at the actual driver precision. No numerical constants, certificate data, proof algorithms or mathematical conclusions were changed.

The research queue is synchronized administratively. All discovery dates, programme histories and campaign counters are preserved, and solved problems become ineligible for future selection. See the [queue snapshot](../../automated_attempts/queue-sync-2026-10-02-active-pr-reviews.json).

## Reproduction

The individual reports give commands, environments and fresh outputs. The certificate checks include the full exact and Python-integer Lotka–Volterra routes, an independently reconstructed Jacobian, the complete Steklov certificate and geometric reassembly, exact persistence reductions and independent ranks, and normal/optimized Elo certificates with regression tests. Wave computations are supporting diagnostics for the analytic proof. The Burgers, NNLIF, hydrogen and Fisher arguments do not depend on finite numerical certificates.

Catalogue structure and generated lists are checked with `python -B scripts/catalogue.py --check`; the stable-ID generator changes are exercised by `python -B scripts/test_catalogue.py`. These repository checks do not establish mathematical correctness.

The hydrogen and Fisher arguments also received a [separate adversarial cross-check](561-665-crosscheck.md), which found no unresolved gap.

The final [package integrity check](package-integrity.json) verifies all **141 manifest entries across nine solution packages**, including the refreshed entries for documented integration corrections. The queue check confirms unchanged IDs, paths, programme histories and discovery dates for all 665 records.

Final repository validation on 2026-10-02: **all 55 catalogue regression tests passed** (855.932 seconds); catalogue structure, generated-list freshness and local links passed; `git diff --check` passed. A separate read-only integration review confirmed that no problem statements or page names changed.
