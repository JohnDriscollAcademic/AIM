# AIM114 actual-variance extension: independent proof referee 2

- **Phase:** final proof-source audit, actual probability semantics, mathematical fidelity, reuse, and independent reproduction.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the variance implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the five actual-variance declarations at the hashes below.
- **Independent mechanical results:** module build, fresh direct re-elaboration, and all five transitive-axiom checks passed locally on macOS.
- **Limit:** this report does not claim authoritative isolated-Linux verification, kernel replay, or Comparator execution of this extension. Construction and convergence of the stable-ratio law and the spectral application remain outside the proved statements.

## Reviewed sources and reproduced checks

| File | SHA-256 |
|---|---|
| `AIM/P114/VarianceDefinitions.lean` | `39448627e15c3dc5b6d0a9c825928abe8f79a6b92fed300cf40313bc9b5ef3aa` |
| `AIM/P114/VarianceProof.lean` | `3a160951c60be915a49a2b9dedb1495e76e6f35007339ab7f30d03901e33e6c2` |
| `VarianceChallenge.lean` | `6b77c1f2e4debf3ac27f7264ab36ee8431a59c060e3e98ac99824160a21be0b5` |
| `VARIANCE_TARGETS.md` | `a215fb1019cd18812094ad0adac10aef5427e2346af39e9004db38e01cca14fb` |
| `VARIANCE_PROOF.md` | `575013a6e37c97e76b59f35a65db749812ec8f576f00e87bec0eb733546b5c27` |
| Imported `AIM/P114/MixtureProof.lean` | `2a5d65beeeb576efad8eaf9940ebe0b5cd81cd52e402807e004444ca2e9e6bcf` |

The boundary hashes match my [pre-implementation approval](variance-statement-referee-2.md). That report records the frozen source manuscript, complete canonical-target snapshot, and expanded proof hashes. The imported Gaussian-mixture implementation is unchanged from my [independent final mixture review](mixture-proof-referee-2.md). I read the actual final source and explanation before running checks, made no proof edits, and did not treat the implementer's success report as evidence.

Working directory: `/Users/sholden/Projects/AIM/research/lean/114`.

| Command | Result | Independent log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.VarianceProof` | Exit 0; successful 3646-job build | [build](../verification/referee-2-variance-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/VarianceProof.lean` | Exit 0; fresh re-elaboration, no diagnostics | [re-elaboration](../verification/referee-2-variance-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-variance-axioms.lean` | Exit 0; all five transitive-axiom lists | [axioms](../verification/referee-2-variance-axioms.log) |

The axiom log retains the complete temporary probe source. Every public declaration reports exactly

```text
[propext, Classical.choice, Quot.sound]
```

There is no `sorryAx` or custom axiom. The [hash manifest](../verification/referee-2-variance-hashes.json) records the complete local source chain and dependency/toolchain inputs. Rehashing after each command confirmed no changes. The [source comparison](../verification/referee-2-variance-source-audit.log) shows all five signatures exactly match the frozen Challenge after whitespace normalization. This comparison is not an authoritative Comparator run. Neither this proof nor its proof imports relies on Challenge placeholders.

## Actual Cauchy law and strict bounds

The two private standard-Cauchy instances are proved from the actual density definition. Atomlessness follows by expressing the nonzero-scale Cauchy measure as a density with respect to atomless Lebesgue measure. For full support, the proof establishes the reverse absolute-continuity relation `volume << cauchyMeasure 0 1` from the density's everywhere strict positivity, then uses the existing open-positive-measure theorem. The direction is correct: an open set of positive Lebesgue measure cannot have zero Cauchy measure. The probability and open-positive properties of the actual three-coordinate product follow from existing product instances, not from new assumptions.

Continuity and positivity of `sqrt(1+x^2)` are proved or obtained from standard square-root facts with nonnegative radicands. The triangle event is an intersection of two open strict-inequality sets. For `r!=0`, its explicit witness is the actual coordinate triple `((r,r),0)`: the magnitude difference is zero, the third magnitude is one, and `|r|<2*sqrt(1+r^2)`. The complement contains the open strict-violation set where the third effective magnitude exceeds the sum of the first two; its actual coordinate witness is `((0,0),3/|r|)`. The estimate `sqrt(1+x^2)>=|x|` makes the third effective magnitude at least three, while the other sum is two. The denominator is justified by `r!=0`.

The proof converts nonzero finite ENNReal masses to positive real masses explicitly, using probability-measure finiteness. It combines the positive event and positive complement with their real-mass sum one to prove both strict bounds. Thus `1/4<v(r)<1/2` follows for the exact Cauchy event, not a surrogate probability. At zero, it proves the event empty and obtains `v(0)=1/2` directly.

## Null boundaries and global continuity

`magnitude_ae_ne` proves every fiber of the magnitude function is Cauchy-null. If a fiber is nonempty, choose one member `y`; equality of magnitudes implies equality of squares and hence `x=y` or `x=-y`. Atomlessness excludes those two values almost everywhere. If the fiber is empty, the result is immediate. This argument handles all real target values, including impossible negative ones, without asserting an invalid inverse-square-root formula.

The proof applies the measurable product almost-everywhere theorem to show the first two magnitudes differ almost everywhere. It then proves the two triangle boundaries are null with two genuinely separate cases. At `r=0`, projection preserves the previously proved almost-everywhere distinctness of the first two magnitudes, and strict positivity of their sum rules out the upper boundary. At `r!=0`, conditioning on the first coordinate pair converts each boundary to a fixed value of the third magnitude; division by `|r|` is guarded by nonzeroness. All set-measurability obligations for these product-null arguments are discharged using continuity and closed equality sets.

For a fixed parameter and triple off those boundaries, `continuousAt_triangle_indicator` splits the possible strict orders around the lower and upper thresholds. Continuity of `s -> |s|*C3` keeps the event's truth value unchanged in a neighborhood. Thus the event indicator is locally constant and continuous at that parameter. The case analysis correctly covers both event membership and each kind of strict nonmembership; it does not presume that the parameter lies in the event.

`triangle_probability_continuous` identifies the actual event mass with its measurable indicator integral using `integral_indicator_one`. It invokes dominated continuity with the integrable constant one on the actual product probability measure. The proof supplies measurable integrands for every parameter, the uniform absolute bound, and almost-everywhere parameterwise continuity from the null-boundary result. It does not require a single exceptional set working for all parameters simultaneously; the theorem is applied separately at each fixed parameter. This proves global continuity, including zero. The final affine transformation preserves that continuity for `actualNodalVariance`.

## Concrete mixture hypotheses and nonequality

For any input probability law `ρ` with full support and `ρ{0}=0`, global continuity supplies measurability. The singleton-mass condition gives `r!=0` almost everywhere, so the previously proved strict bounds apply almost everywhere under that actual law. No full atomlessness assumption is used or needed.

If the continuous variance function were equal to a constant `ρ`-almost everywhere, the library's `Measure.eq_of_ae_eq` would make it equal to that constant everywhere because `ρ` assigns positive mass to every nonempty open set. Its values at zero and one then contradict `v(0)=1/2` and `v(1)<1/2`. This use of continuity/full support is valid even though zero itself has zero mass; no positive mass at a singleton is inferred.

The final theorem applies the already proved actual Gaussian-mixture law theorem using these established inputs. It therefore concludes genuine nonequality of the actual product/pushforward law, using the manuscript's fixed variance function, with the standard Gaussian measure. None of the regularity, strict bounds, nonconstancy, or resulting moment identities is introduced as an unproved assumption about that function.

## Quality, scope, and disposition

The implementation appropriately reuses Mathlib's density, absolute-continuity, finite-measure, product-measure, indicator-integral, dominated-continuity, and full-support equality APIs. Its source-specific work consists of explicit realizable witnesses and exact algebraic analysis of the triangle-boundary fibers. The private helpers are focused and their role is reflected accurately in `VARIANCE_PROOF.md`. The new module introduces no placeholders, custom axioms, probabilistic independence assumption, or numerical certificate.

This removes a substantive earlier formal gap: the mixing function is now exactly the source's Cauchy triangle probability, and its necessary mixture properties are proved. However the law `ρ` is still a general input satisfying intrinsic support and zero-atom conditions. The package has not constructed the stable response pair, proved convergence of response sums, identified `ρ` with the law of `-A/B`, proved those conditions for that particular ratio, established the empirical-process limit and random evaluation, or connected the laws to spectral surplus. These remaining links are explicit in the approved documentation. The universal linear-variance assertion is still a separate unresolved target.

**Blocking findings: none.** Final combined-target integration and authoritative Linux verification are separate gates. This review and local success do not establish the complete quantum-graph counterexample in Lean.
