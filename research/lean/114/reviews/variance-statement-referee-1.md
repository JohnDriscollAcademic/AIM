# Independent statement review 1: actual nodal-variance function

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of the candidate author and future implementer `lean_feasibility`.
- Phase: preproof boundary review.
- Verdict: **APPROVE** the five statements at the exact hashes below. No proof body existed at review time.

## Inspected source and exact boundary

I read all definitions and signatures, the complete target document, and the source's one-module variance and concluding mixture argument. The source remains Sidney Holden's v0.3 PDF, SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`, and the unchanged original AIM114 statement at `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. I inspected the pinned Mathlib definition of `cauchyMeasure` and the semantics of `IsOpenPosMeasure` and continuous almost-everywhere equality.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/VarianceDefinitions.lean` | `39448627e15c3dc5b6d0a9c825928abe8f79a6b92fed300cf40313bc9b5ef3aa` |
| `VarianceChallenge.lean` | `6b77c1f2e4debf3ac27f7264ab36ee8431a59c060e3e98ac99824160a21be0b5` |
| `VARIANCE_TARGETS.md` | `a215fb1019cd18812094ad0adac10aef5427e2346af39e9004db38e01cca14fb` |

I independently ran `lake env lean VarianceChallenge.lean` after checking those hashes and absence of a proof module. It exited zero with exactly five deliberate placeholders, recorded in [referee-1-variance-boundary.log](../verification/referee-1-variance-boundary.log). This is a statement well-formedness check, not a proof.

## Actual probability function and correspondence

`cauchyTripleMeasure` is the product of three actual Mathlib standard Cauchy measures, with location zero and nonzero unit scale. Grouping as `((X1,X2),X3)` is only a coordinate convention. Each magnitude is exactly `sqrt(1+Xj^2)`. The triangle event uses the strict lower and upper boundaries from the manuscript with `abs r` in the third magnitude; there is no replacement distribution or arbitrary event mass. Its real measure mass is finite because the actual triple measure is a probability measure.

The formula `1/2-P(event)/4` is exact. At zero the lower strict inequality is impossible, giving one half. For nonzero r, both the strict triangle event and a strict violation of its upper bound have nonempty open witnesses. For example `((r,r),0)` satisfies the event and `((0,0),3/abs r)` violates it strictly. Their magnitudes satisfy the actual constraint of being at least one. Once full support is proved from the Cauchy density, these witnesses give probability strictly between zero and one and hence the stated strict variance bounds.

The global continuity assertion is faithful to the source and mathematically sound. Away from zero each boundary equality, conditioned on the first two coordinates, fixes the third magnitude to one value, whose preimage has at most two Cauchy points. At zero the potential lower-bound equality is equality of the first two magnitudes, again a null event by conditioning; the upper boundary is impossible. Off these boundary sets the event indicator is locally constant in r, and its uniform bound permits dominated continuity. These facts are obligations to prove, not hypotheses in the Challenge.

## Application hypotheses and nonequality of laws

The fourth statement fixes the variance function to this concrete Cauchy construction and proves measurability, the strict bounds almost everywhere under rho, and intrinsic almost-everywhere nonconstancy. The only input law assumptions are actual probability mass one, positive mass for every nonempty open set, and no atom at zero. The last is precisely what is needed to apply the strict nonzero-r bounds almost everywhere; no unnecessary full atomlessness assumption is imposed.

Continuity and open-set positivity make almost-everywhere constancy imply everywhere constancy, while the value at zero and strict bound at one rule that out. The input assumptions are nonvacuous, e.g. a standard Cauchy law. None assumes a regularity, moment, or nonconstancy conclusion about the concrete variance function.

The fifth statement applies the already proved actual Gaussian-mixture construction to that concrete function. It asserts inequality of real probability measures, not just a scalar moment inequality. The future stable ratio law still must be constructed, shown to satisfy the three intrinsic law hypotheses, and identified as the limit of graph responses. Those substantial obligations and the spectral/process convergence remain explicit gaps; this block does not claim a complete counterexample.

No mathematical changes are requested. Both independent written approvals and typechecking must precede implementation. The proof must establish full support and atomlessness of the actual Cauchy factors, handle the zero parameter separately where needed, and avoid introducing an assumed boundary-null or variance-regularity theorem. Final source review, transitive axiom checks, and expanded isolated Linux verification remain separate gates.
