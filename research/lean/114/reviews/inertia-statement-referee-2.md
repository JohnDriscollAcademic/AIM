# AIM114 finite-inertia extension: independent statement referee 2

- **Phase:** pre-implementation mathematical-boundary review.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the inertia boundary author or proposed implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the two proposed declarations at the exact hashes below.
- **Mechanical evidence inspected:** [the retained boundary log](../verification/inertia-boundary-typecheck.log) records a successful Definitions build and Challenge type-check, with only the two deliberate placeholders. These were not executions by this reviewer and are not proof certificates.

## Reviewed evidence

| File | SHA-256 |
|---|---|
| `AIM/P114/InertiaDefinitions.lean` | `d40bb849d050150f4688bee02ba4f2a88341593f1c37114d253c79b2651b0795` |
| `InertiaChallenge.lean` | `0c4fc841423c270b32cfe8761ec6258df1e30e8946ac4c396bfcbd94c1505e72` |
| `INERTIA_TARGETS.md` | `4f847915317cc8721e5108dd4fe3efc0209706a686ea9353576569a68cc245a1` |
| Submitted v0.3 PDF | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Frozen complete source problem `statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| Expanded informal `PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |

I read the complete candidate boundary and compared it with the module elimination and pivot list in manuscript Lemma 1. I independently read the pinned Mathlib definitions of `linMulLin`, `weightedSumSquares`, `sigPos`, `LinearEquiv.skewProd`, and `LinearEquiv.piOptionEquivProd`, as well as the signature theorem proposed for reuse. No implementation existed for this boundary when requested, and I did not use an author's claimed proof or another referee's verdict as evidence.

## Exact connection to the source core

After deleting vertex `u`, the core vertex coordinates are a scalar `r` at `v` and one real `z_i` at each `w_i`. The remaining core matrix has module diagonal entries `-a_i`, scalar diagonal entry `-sum x_i3`, and scalar/module cross entries `q_i=csc(theta_i3)`. Thus its quadratic form is exactly

```math
Q(r,z)=-\sum_i a_i z_i^2+2r\sum_i q_i z_i-\left(\sum_i x_i\right)r^2.
```

The proposed `coreQuadraticForm` assembles that expression from coordinate linear maps, their products, and a weighted sum of squares. In particular, the library's `linMulLin_apply` is ordinary multiplication of the two linear evaluations; the factor 2 in the cross term is therefore correct. The initial form is not defined to equal its desired diagonalization. The pendant coordinate is absent, as explicitly documented.

The arrays `a,q,x` are arbitrary real arrays indexed by `Fin m`, with only `a_i!=0` required in the theorems. This is a legitimate algebraic generalization of the trigonometric specialization, not a change to the original graph target. The finite sum called `coreSchurValue` is exactly the manuscript's residual `T_m=sum_i(-x_i3+q_i^2/a_i)`.

## The explicit equivalence and completion identity

Reading the actual library `skewProd_apply` confirms that this shear sends `(r,z)` to `(r,z+f(r))`. The chosen linear map has `f(r)_i=-r*q_i/a_i`. Composing with the inverse of `piOptionEquivProd` therefore places `r` at the `none` coordinate and `z_i-r*q_i/a_i` at `some i`, precisely as claimed. The object is an actual `LinearEquiv`, with an inverse that adds the same coefficient back; invertibility is not an assumed determinant condition or unspecified witness.

For each nonzero `a_i`, expanding

```math
-a_i(z_i-rq_i/a_i)^2
=-a_i z_i^2+2r q_i z_i-r^2q_i^2/a_i
```

shows that addition of the scalar term `T r^2` yields exactly the original form. The equation in `core_completion_of_squares` uses the correct direction of composition: `Q=diagonalForm.comp E`. The nonzero hypotheses exclude precisely the denominators needed for this identity. The shear remains an equivalence under totalized real division even if a denominator vanishes, but the theorem correctly does not assert the completion identity in that invalid case.

## The positive-index target

The pinned `sigPos` definition is the maximum finite rank of a subspace on which the form restricts to a positive-definite form; over these real finite-dimensional coordinate spaces this is the standard positive index. It is an imported mathematical definition, not a custom alias for the proposed answer. The proposed proof route via a genuine quadratic isometry equivalence and `QuadraticForm.sigPos_of_equiv_weightedSumSquares` is therefore a substantive application of inertia invariance.

The diagonal weights are `T` at `none` and `-a_i` at the module coordinates. Hence positive module weights correspond to the strict inequalities `a_i<0`, and the scalar contribution is one exactly when `T>0`. The source of both terms in `core_positive_index` is correct, including its strict inequalities and natural-number count.

No `T!=0` assumption is needed or imposed. At `T=0`, the remaining diagonal direction is null and contributes zero to the positive index. This correct degeneracy handling is stronger than the generic source case. For `m=0`, both finite sums are empty, the core form on the remaining scalar line is zero, and the formula gives zero. Neither case is represented as an admissible quantum graph; these are valid extensions of the finite algebraic statement only.

## Scope and disposition

The boundary is non-vacuous for every `m`: choosing all `a_i=1` satisfies its only denominator condition, with unrestricted `q,x`. Its definitions are transparent actual forms and maps. It proves the finite core pivot count without assuming that count or an inertia identity as a hypothesis.

The retained scope document correctly excludes the full graph and edge matrix, pendant cancellation, generic kernel reduction, spectral min–max argument, edge zero count, null exceptional sets, and identification with nodal surplus. In particular, converting this real quadratic-form index into the spectral term of the source argument remains an application gap outside these two Lean theorems. The extension is meaningful progress on Lemma 1 but is not the complete spectral reduction or a full AIM114 proof.

**Requested mathematical changes: none.** Approval is specific to these bytes. The second independent approval and proof implementation must precede final source/axiom review and the authoritative verification workflow. This report does not establish either theorem and does not promote the full counterexample or the separate universal variance question to a formally resolved status.
