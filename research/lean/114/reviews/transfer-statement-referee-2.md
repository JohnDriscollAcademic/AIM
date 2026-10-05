# AIM114 transfer extension: independent statement referee 2

- **Phase:** pre-implementation boundary review.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the five declarations at the exact reviewed hashes below.
- **Mechanical status:** this report does not claim independent type-checking. Root reported that definition/challenge checking was running; its successful completion remains a separate gate before proofs.

## Reviewed sources

| File | SHA-256 |
|---|---|
| `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| `TransferChallenge.lean` | `48d4e6a969b304dd89145bf8be6df2697db220b6e8a51ed458c6631047a544d1` |
| `TRANSFER_TARGETS.md` | `6deb2147a2742f8cefbbdec369932b654d6153227d59b6686c4887bc71b69538` |
| Submitted v0.3 PDF | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Frozen complete source problem `statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| Expanded informal `PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |

I previously read the complete source manuscript and independently audited its probability argument. For this extension I reread all three candidate files, checked the actual pinned prime-indexing API, and compared the proposed results with the original Section 5 calculation. No TransferProof existed when this review was requested, and no proof implementation or another referee's verdict was used as evidence.

During boundary type-checking, the two support-hypothesis binders in the final declaration were annotated explicitly as `m : ℕ`. I reread the resulting complete Challenge and recomputed its hash shown above. This correction makes the intended natural-number quantifier explicit and preserves the reviewed mathematical statement; the initial failed inference is not being reported as a successful type-check.

## Boundary correspondence

**Actual lengths and `core_weight_bound`.** The pinned library's `Nat.nth_prime_zero_eq_two` confirms the declared zero-based convention. The core sum over `Finset.range (3*m)` uses exactly the source primes numbered 1 through `3m`; the pendant uses the next prime and the exact multiplier `m^6`. `coreWeight` is the actual ratio of these finite sums, not a freely assumed weight. All natural `m>=1` are allowed, a valid algebraic generalization of the source's admissible graph range `m>=3`. The positive-prime square roots and positive `m` make the denominator strictly positive. Bounding each core root by the pendant root gives the claimed `3/(m^5+3)` upper bound. The `m=0` totalized division does not enter this theorem or any support-dependent claim.

**`contaminated_law_probability`.** The definition is a genuine sum of measures with ENNReal weights obtained from the real numbers `1-w` and `w`. The closed interval assumptions ensure those conversions do not truncate a negative weight and ensure total mass is one. Both endpoints are explicitly included; the formula reduces to the first law at zero and the second at one. There is no circular probability-status hypothesis on the contaminated measure.

**`contamination_integral_bound`.** The hypotheses concern two probability measures and one measurable observable lying in the same interval `[0,B]` almost everywhere under each. These bounds imply its Bochner integrability. The bound has the correct sharp interval width: the two expectations each lie in `[0,B]`, and the difference under contamination is `w` times their difference. Consequently `w*B`, rather than `2*w*B`, is justified. The theorem does not assume the expectation identity or the desired error estimate. The cases `B=0`, `w=0`, and `w=1` are mathematically sound.

**`surplus_moment_contamination_bound`.** Both laws have the exact source support `[0,2m-1]`. The integrand is centered at `(2m-1)/2` and divided by `sqrt(m)`, as in the manuscript. Its exponent `2*k`, with `k=1` or `2`, represents the second or fourth absolute moment because those powers are even. On this interval the absolute centered value is at most `(2m-1)/2 <= m`, so its scaled absolute value is at most `sqrt(m)` for `m>=1`; its even power is at most `m^k`. This explains the explicitly disclosed relaxation of the source's sharper bound and gives exactly the displayed upper bound. No symmetry or mean hypothesis is needed for an error estimate about a fixed common center; the theorem does not assert that arbitrary input laws have that center as their mean.

**`surplus_moment_contamination_tendsto`.** The two law sequences are arbitrary probability measures subject only to the same eventual support conditions. The theorem asserts convergence to zero of the actual signed difference of their centered/scaled integrals after the actual prime-root contamination. The finite estimate tends to zero for both allowed `k`, since its numerator grows with degree at most two and its denominator with degree five. The lack of a support condition at `m=0` is harmless for a limit at infinity. Neither convergence of the original law nor convergence of its moments is built into the hypotheses or falsely asserted in the conclusion.

## Scope, non-vacuity, and disposition

The hypotheses are satisfiable: for each `m>=1`, either endpoint Dirac law lies in the permitted surplus interval, and all weight and observable bounds have ordinary realizations. No theorem-shaped conclusion is hidden in a definition. The prime-root sum, measure mixture, and centered even-moment integrands are all transparent mathematical objects.

This is a substantial formalization of the source's final transfer calculation, including its actual prescribed length fraction and limiting moment error. It does not identify the abstract input measures with spectral surplus laws. The published edge-measure representation and surplus support facts remain application dependencies; no unproved Lean axiom is introduced for them. Prime-root rational independence, graph admissibility, the pendant-law limit, weak convergence, and the full counterexample remain outside this boundary. The independent universal linear-variance assertion remains unresolved.

**Requested mathematical changes: none.** Approval is specific to these bytes. The approved statements must still pass their type-checking gate, be implemented without importing intentional Challenge placeholders, be included in the combined Comparator target list, and receive independent final proof and verification review. This statement approval is not Lean verification of the extension or the original AIM114 problem.
