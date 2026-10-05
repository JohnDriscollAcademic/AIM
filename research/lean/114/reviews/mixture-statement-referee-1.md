# Independent statement review 1: actual Gaussian variance mixture

- Date: 2026-10-05.
- Phase: preproof boundary review of the actual definitions, three Challenge signatures, and scope document.
- Reviewer: Codex AI subagent `spectral_review`, independent of the manuscript author and proof implementer; this is an AI review.
- Verdict: **APPROVE the mathematical boundary at the exact hashes below.** The second independent approval and successful boundary type-checking remain required before implementation.

## Frozen sources and inspected bytes

The mathematical source is Sidney Holden's complete six-page *A non-Gaussian limit for nodal surplus*, revised proof v0.3 (2026-10-02), PDF SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`, particularly Theorem 1 equation (5) and Section 5. I read that complete manuscript and the original AIM 114 statement at `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88` in the preceding independent audit. For this review I read every definition and theorem signature below, not merely the implementer's summary.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/MixtureDefinitions.lean` | `63573393a3e5521a4276e822717f307bbabd4c327540e22895c99a1c0fab7652` |
| `MixtureChallenge.lean` | `edd2f69de4e8ba1552189d57856ae4bd7f35a4b9c73a53c0d2e1de81c5a3570a` |
| `MIXTURE_TARGETS.md` | `85fd7a64932d5fcd567f4cceb13711da60fcc1ffdde70e118c7ee4e6143ef1f8` |

These are the final module-path versions, with `import AIM.P114.MixtureDefinitions`. I also inspected `verification/mixture-boundary-typecheck.log`: it records a zero exit from `lake env lean MixtureChallenge.lean` and exactly the three intended placeholder warnings. I did not independently execute that type-check for this report; the log is evidence of the recorded run, not of an additional reviewer run.

## Concrete law and normalization

`normalizedVarianceMixture μ V` is a genuine `Measure ℝ`: it is the pushforward of `μ.prod (gaussianReal 0 1)` under `(ω,z) ↦ z*sqrt(V(ω)/integral V)`. The pinned Mathlib Gaussian has mean zero and variance parameter one. The two coordinates are independent by the product construction; independence is not assumed through a scalar identity or custom predicate.

The map definition is total, but all advertised mixture theorems require a probability measure, measurable `V`, and the exact almost-everywhere bounds `1/4<V<1/2`. These imply integrability, a strictly positive finite mean, and a nonnegative ratio almost everywhere. Thus Lean's total real division and square root on nonpositive inputs cannot change the intended law on a positive-measure set. Measurability of the map also follows from the explicit hypothesis, so the totalized nonmeasurable-map behavior of `Measure.map` is not a hidden issue.

The scale is `sqrt(V/E[V])`, as in the source's standardized law. It is not `sqrt(V)/E[V]` or an arbitrary normalization constant. The input space need not itself contain a Gaussian variable: the product construction creates the independent Gaussian coordinate explicitly.

## Each advertised result

### `standard_gaussian_fourth_moment`

The target is the actual Bochner integral of `z^4` under Mathlib's `gaussianReal 0 1`, equal to three. It has no moment or integrability assumptions disguised as hypotheses. Gaussian integrability must be established or obtained from Mathlib in the proof. Its result is the exact reference moment needed to distinguish the standardized mixture from the standard Gaussian.

### `normalized_variance_mixture_moments`

For an arbitrary probability measure and measurable bounded positive mixing variance, the result proves all of the following for the actual mapped measure: probability mass one; integrability of the first, second, and fourth powers; mean zero; second moment one; and fourth moment

```text
3 * integral(V^2) / (integral V)^2.
```

All factors and exponents agree with the source. The explicit integrability conclusions prevent a nonintegrable integral's default value from masquerading as a valid moment calculation. Zero mean together with unit second moment proves the intended standardization. Nonconstancy is correctly absent from this theorem: a constant positive mixing variance should also satisfy these moment identities.

The almost-everywhere bounds do not silently become pointwise bounds. Proofs of the product and pushforward integrals must transport the full-measure set correctly. Values outside that set may be arbitrary and remain harmless to the law.

### `normalized_variance_mixture_not_gaussian`

The additional hypothesis says `V` is not almost everywhere equal to any real constant. This is an intrinsic, measurable-law property of the input; it is not the desired conclusion restated as an assumption. Boundedness ensures square integrability, so that nonconstancy forces strictly positive centered second moment. Combined with the proved moment identities and the Gaussian fourth moment, it establishes actual inequality of measures.

No mixture moment formula, positive mean, positive variance, independence, or inequality of laws appears as a hypothesis. Those are precisely the substantive bridges to be proved in this extension. The assumptions are satisfiable, for example with a two-point probability space and distinct values `1/3` and `5/12`. There is no vacuity.

## Relationship to the complete counterexample

This removes the gap between the earlier scalar kurtosis inequality and a constructed non-Gaussian standardized probability law. It formalizes the concluding mixture inference under the same variance bounds as the source and an equivalent nonconstancy condition in the bounded setting.

It still does not define the stable vector `(A,B)`, form its ratio, construct the specific deterministic function `v`, prove the manuscript's `V=v(R)` has these hypotheses, or show convergence of the actual spectral surplus laws to this measure. The corresponding source argument and the new scope document make those remaining links explicit. The universal variance assertion is likewise not resolved. These are material scope limits, accurately stated; they are not a reason to reject this substantive partial extension.

## Proof gates and remaining review

No proof implementation was inspected in this preproof review. Challenge's `sorry` placeholders certify no mathematics and must never enter the Solution dependency graph. Once both approvals and type-checking are recorded, the actual proofs require independent post-proof review, exact combined-boundary comparison, transitive axiom inspection, and a fresh authoritative Linux run for the enlarged theorem set.

Any change to the definitions, the quantifiers, the almost-everywhere conventions, the three formulas, or their assumptions reopens this approval. No changes are requested to the reviewed boundary.
