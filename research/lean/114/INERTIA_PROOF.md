# Finite core quadratic-form proof

The two declarations in `AIM/P114/InertiaProof.lean` establish the actual core
completion of squares and positive index in Sidney Holden's v0.3 manuscript,
Lemma 1. Both statement reviews preceded implementation and bind the unchanged
definitions, challenge, and target-document bytes.

`core_completion_of_squares` proves equality of concrete quadratic forms by
evaluating them on an arbitrary `(r,z)`. Expanding the coordinate shear and the
weighted sum of squares reduces the equality to a finite sum of scalar
identities. Each scalar identity uses the explicit nonzero hypothesis for its
own `a_i` to clear denominators, then follows by polynomial normalization.
No diagonalization or inertia formula is assumed.

`core_positive_index` constructs a genuine `QuadraticMap.IsometryEquiv` from
that equality and the explicit `coreDiagonalizingEquiv`. Mathlib's
`QuadraticForm.sigPos_of_equiv_weightedSumSquares` then identifies the actual
positive index with the number of positive diagonal weights. The finite sum
over `Option (Fin m)` separates its scalar coordinate from its module
coordinates. The scalar coordinate contributes one exactly when `T>0`, and
each module coordinate contributes one exactly when `a_i<0`.

The proofs do not require the residual pivot to be nonzero and remain valid
when `m=0`. They use the actual maximal-positive-subspace definition `sigPos`,
not a new index defined by counting the proposed pivots. They import no
Challenge, contain no placeholders, and add no axioms.

This block proves the core pivot-count step. The full graph matrix, pendant
coordinate, generic eigenvector congruence, exceptional null sets, and spectral
min-max interpretation remain outside the formalization. In particular, these
two theorems alone do not yield a nodal-surplus distribution or the full AIM
114 counterexample.
