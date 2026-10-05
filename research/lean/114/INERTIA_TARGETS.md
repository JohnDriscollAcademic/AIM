# Exact candidate boundary: finite core inertia

This proposed extension formalizes the finite-dimensional completing-squares
step in Sidney Holden's v0.3 manuscript, Lemma 1, using the immutable submitted
PDF SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.
The original AIM 114 target remains the one at upstream revision
`8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. The scalar coordinate is the vertex
value at `v`, and the `m` module coordinates are values at `w_i`, after removal
of vertex `u`. The pendant coordinate is not included in this core form.

The concrete objects are in `AIM/P114/InertiaDefinitions.lean`, and exactly two
advertised signatures are in `InertiaChallenge.lean`. This is a candidate
boundary: both independent approvals are required before proof implementation.
The deliberate Challenge placeholders are not proof certificates and must not
be imported into Solution.

## Actual objects

For arbitrary `m : Nat` and real arrays `a,q,x : Fin m -> Real`, the definition
`coreQuadraticForm` is assembled directly from linear coordinate maps and their
products as the actual quadratic form on `Real × (Fin m -> Real)`:

```math
Q(r,z)=-\sum_i a_i z_i^2+2r\sum_i q_i z_i-\left(\sum_i x_i\right)r^2.
```

It is not defined to equal its proposed diagonalization. In the source,
`a_i = cot(theta_i1)+cot(theta_i2)+cot(theta_i3)`,
`q_i = csc(theta_i3)`, and `x_i = cot(theta_i3)`.
The finite theorem is valid for arbitrary real arrays subject only to
`a_i != 0`; the trigonometric specialization is a later application.

`coreSchurValue` is the actual finite sum

```math
T=\sum_i\left(-x_i+q_i^2/a_i\right).
```

`coreDiagonalForm` is Mathlib's `QuadraticMap.weightedSumSquares` on the
coordinate space indexed by `Option (Fin m)`. The weight at `none` is `T`, and
the weight at `some i` is `-a_i`.

`coreDiagonalizingEquiv` is an actual `LinearEquiv`, built using the existing
invertible shear `LinearEquiv.skewProd` followed by
`LinearEquiv.piOptionEquivProd` in reverse. Its map is explicitly

```math
E(r,z)_{\mathrm{none}}=r,\qquad
E(r,z)_{\mathrm{some}(i)}=z_i-rq_i/a_i.
```

Its inverse adds `r*q_i/a_i` back to each module coordinate. Invertibility
of a shear requires no condition on its coefficients, so the equivalence
itself exists even when a denominator is zero under Lean's total division.
The completing-squares theorem explicitly excludes those zeros; total division
cannot be used to assert a false unrestricted identity.

## Advertised results

1. `core_completion_of_squares` proves equality of the actual quadratic forms
   `Q = coreDiagonalForm.comp E.toLinearMap`, under `forall i, a_i != 0`.
   Thus, pointwise, it proves
   `Q(r,z) = T*r^2 - sum_i a_i*(z_i-r*q_i/a_i)^2`.
   It neither assumes an inertia identity nor supplies an arbitrary witness
   whose relation to the source coordinates is unspecified.
2. `core_positive_index` proves
   `sigPos Q = card {i | a_i < 0} + (if T > 0 then 1 else 0)`
   under the same nonzero-diagonal hypothesis. Here `sigPos` is the actual
   Mathlib definition: maximal dimension of a linear subspace on which the
   real quadratic form is positive definite. In the pinned Mathlib source
   this constant is at the root namespace, even though its documentation
   sometimes calls it `QuadraticForm.sigPos`. It is not a custom count
   defined to be the theorem's right-hand side.

The proposed proof of the second theorem will construct a genuine quadratic
isometry equivalence from the first theorem and the explicit linear map, then
apply Mathlib's `QuadraticForm.sigPos_of_equiv_weightedSumSquares` (Sylvester's
law of inertia). Counting the positive `Option (Fin m)` weights gives the
displayed formula.

Neither theorem assumes `T != 0`. When `T=0` its diagonal weight contributes
zero to the positive index, as required. The theorem also covers `m=0`:
the empty sum gives `T=0` and the form on its one-dimensional scalar space
is zero. These valid degenerate cases generalize the purely algebraic step;
they do not assert existence or admissibility of a source graph for small `m`.

## Scope not covered

This block does not define the full graph, its edge matrix, the pendant block,
or a quantum-graph Laplacian. It does not prove the generic eigenvector
reduction `M ~ 0 ⊕ M_without_u`, nullity, rational independence of lengths,
exceptional-set nullity, the spectral min-max index formula, an edge zero
count, or any nodal-surplus law. In particular, the identification of this
finite positive index with the term in the actual spectral surplus formula
remains a mathematical application outside Lean. The precise contribution is
the claimed core pivot list and its real positive-index count.

## Pinned library evidence

The project uses Mathlib revision
`0df444a360eaa60ab8c11dca51a86af692955474`.

- Actual [`sigPos` definition and Sylvester signature theorem](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/QuadraticForm/Signature.lean#L65).
- Actual [`weightedSumSquares` constructor](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/QuadraticForm/Basic.lean#L1419).
- Actual [`skewProd` invertible shear](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/Prod.lean#L802).
- Actual [`piOptionEquivProd` reindexing](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/Pi.lean#L531).

The actual definition module and two Challenge signatures type-check in the
pinned project. The retained `verification/inertia-boundary-typecheck.log`
records both successful commands and the two intentional Challenge warnings.
No implementation or proof success is claimed by that boundary type-check.
