# AIM114 actual-variance extension: independent statement referee 2

- **Phase:** pre-implementation mathematical-boundary review.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the boundary author or proposed implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the five proposed statements at the exact hashes below.
- **Mechanical evidence inspected:** [the retained boundary log](../verification/variance-boundary-typecheck.log) records a successful Challenge type-check with five deliberate placeholders. This was not my execution and establishes no theorem.

## Exact reviewed sources

| File | SHA-256 |
|---|---|
| `AIM/P114/VarianceDefinitions.lean` | `39448627e15c3dc5b6d0a9c825928abe8f79a6b92fed300cf40313bc9b5ef3aa` |
| `VarianceChallenge.lean` | `6b77c1f2e4debf3ac27f7264ab36ee8431a59c060e3e98ac99824160a21be0b5` |
| `VARIANCE_TARGETS.md` | `a215fb1019cd18812094ad0adac10aef5427e2346af39e9004db38e01cca14fb` |
| Submitted v0.3 PDF | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Frozen complete source problem `statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| Expanded informal `PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |

I read the complete source manuscript for the earlier independent probability audit, then read the complete proposed definitions, Challenge, and scope document for this extension. I independently inspected the pinned Cauchy measure, its density and probability instance, the open-positive-measure API, and continuous-function equality from almost-everywhere equality. Following resumption of the task, I reread the final definitions and statements and recomputed their hashes; they remain identical to the candidate first inspected. No proof body was used as evidence and I have not implemented new mathematics.

## Actual objects and correspondence

`cauchyMagnitude x=sqrt(1+x^2)` agrees exactly with the manuscript's `C_j`. `cauchyTripleMeasure` is the actual iterated product of three Mathlib `cauchyMeasure 0 1` measures, with coordinates grouped as `((X1,X2),X3)`. The pinned library defines the positive-scale Cauchy distribution through its density with respect to Lebesgue measure and proves its total mass is one. Thus the probability in the definition is a concrete standard-Cauchy product probability, not an unconstrained scalar or predicate.

`varianceTriangleEvent r` uses the correct coordinate projections, absolute value of `r`, and both strict inequalities of manuscript Eq. (3). `actualNodalVariance` uses real-valued mass of precisely that event, with the exact coefficients `1/2` and `1/4`. Its definition is total for every real `r`; the added value at zero is obtained from the same formula and leaves the manuscript's required nonzero values unchanged.

## Statement-by-statement assessment

**`actual_nodal_variance_zero`.** At `r=0`, the first strict triangle inequality asks for a nonnegative absolute difference to be less than zero. The event is empty, and its actual mass is zero. The value `1/2` follows exactly. No endpoint convention for an indicator is left implicit.

**`actual_nodal_variance_bounds`.** For every nonzero finite real parameter, write `t=|r|>0`. The event is open in the three real coordinates because the relevant functions are continuous. It is nonempty: set the first two magnitudes equal to `t+1` and the third equal to one. This gives `0<t<2(t+1)`; these magnitudes are realized by the real coordinates `sqrt((t+1)^2-1)`, the same coordinate again, and zero. The complement contains a nonempty open strict-violation set: take the first two magnitudes equal to one and the third equal to `1+2/t`, so `t*C3=t+2>2`. Again all magnitudes are at least one and are exactly realizable by real Cauchy coordinates.

The actual Cauchy density is positive at every real point; its product therefore gives positive mass to both indicated nonempty open sets. Consequently the event's probability lies strictly between zero and one, giving precisely `1/4<v(r)<1/2`. This independently verifies the target without treating arbitrary positive numbers below one as possible cosecant magnitudes. No property of the future ratio law is an assumption of this result.

**`actual_nodal_variance_continuous`.** Continuity on all of the real line is a valid strengthening of the source's continuity away from zero together with its stated zero-limit. For a fixed nonzero `r0`, conditioning on the first two coordinates reduces each event-boundary equation to a prescribed value of `sqrt(1+X3^2)`. Each such fiber contains at most two real points and is null for the atomless Cauchy law. At `r0=0`, the upper boundary is impossible because both first magnitudes are at least one; the lower boundary is equality of those two magnitudes. That equality entails `X1=X2` or `X1=-X2` and is null by conditioning and atomlessness. Off those exceptional boundaries the strict-event indicator is continuous locally in `r`, and its bound by one gives dominated continuity of the actual probability. Thus the stated global continuity is mathematically correct; the zero case must be addressed and cannot be handled by dividing by `|r0|`.

**`actual_nodal_variance_mixture_inputs`.** The output includes exactly the three requirements of the previously formalized Gaussian-mixture application: measurability, the strict source bounds almost everywhere, and intrinsic failure of almost-everywhere constancy. Continuity supplies measurability. The hypothesis `ρ {0}=0` removes precisely the sole parameter where strict bounds fail. `Measure.IsOpenPosMeasure ρ` is an intrinsic full-support condition, meaning every nonempty open set has positive measure. For such a measure, continuous functions equal almost everywhere are equal everywhere. Were the actual variance function almost everywhere constant, global continuity would make it everywhere constant, contradicting its value `1/2` at zero and its strict upper bound at one. The use of the value at zero is sound even though zero itself has measure zero: continuity and full support make it a constraint on all nearby positive-mass neighborhoods.

The input assumptions do not require atomlessness away from zero, and none is needed. They are non-vacuous, being satisfied by the standard Cauchy and Gaussian probability laws. The conclusion is not concealed inside a custom assumption structure; no regularity, bounds, nonconstancy, or moment identity of the actual variance function is assumed.

**`actual_nodal_variance_mixture_not_gaussian`.** The conclusion concerns the previously defined actual product/pushforward probability law, now using the specific Cauchy-defined function rather than an arbitrary mixing function. Applying the preceding proved inputs to the previously reviewed actual Gaussian-mixture theorem would give exactly this nonequality with `gaussianReal 0 1`. Its hypotheses remain intrinsic properties of the parameter law `ρ`, rather than a disguised non-Gaussianity assertion or a assumed variance inequality.

## Implementation obligations and scope

The proof must establish full support and atomlessness for the actual standard Cauchy measure from the library's density definition, not introduce them as new axioms. It must justify real-mass and indicator-integral conversion using the finite probability measure, transport null boundary fibers through the actual product measure, handle continuity at zero separately, and justify square-root identities with nonnegative radicands. These are genuine proof obligations of the approved statements; the scope document identifies them accurately.

This extension would remove the arbitrary-`V` gap in the concluding mixture inference: the deterministic function would be the exact one from the manuscript, with its needed properties proved. It still does **not** construct the stable pair `(A,B)`, prove response-sum convergence, identify `ρ` with the distribution of `-A/B`, establish the required intrinsic hypotheses for that future ratio law, or prove the spectral graph-to-module connection and nodal-surplus convergence. In particular, taking an arbitrary full-support law as input is not a substitute for proving the source stable-ratio law exists. Those remaining application dependencies are explicit in the boundary documentation. The independent universal linear-variance question remains unresolved.

**Requested mathematical changes: none.** Approval is specific to the listed bytes. Implementation, independent final proof review, integration into the combined target list, and authoritative Linux verification are later gates. This report establishes no theorem and does not certify a complete formal resolution of AIM114.
