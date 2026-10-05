# Independent statement review 1: finite core inertia

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of the Inertia definitions and proof implementer (`spectral_review`). Root implemented the separate transfer block; that authorship is not presented as independence for transfer.
- Phase: preproof boundary review.
- Verdict: **APPROVE** the two advertised Inertia statements at the exact hashes below.

## Inspected source and exact boundary

I read the complete preserved problem statement, the expanded informal argument's spectral reduction, and every line of the three candidate files. I also inspected the actual pinned Mathlib definitions of `sigPos`, `weightedSumSquares`, `linMulLin`, `skewProd`, and `piOptionEquivProd`. The source manuscript is Sidney Holden's v0.3 PDF, SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`; the source problem remains upstream revision `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/InertiaDefinitions.lean` | `d40bb849d050150f4688bee02ba4f2a88341593f1c37114d253c79b2651b0795` |
| `InertiaChallenge.lean` | `0c4fc841423c270b32cfe8761ec6258df1e30e8946ac4c396bfcbd94c1505e72` |
| `INERTIA_TARGETS.md` | `4f847915317cc8721e5108dd4fe3efc0209706a686ea9353576569a68cc245a1` |

I checked that no `InertiaProof.lean` existed at review time. I independently ran `lake env lean InertiaChallenge.lean`; it exited zero with exactly the two deliberate placeholder warnings. The separate record is [referee-1-inertia-boundary.log](../verification/referee-1-inertia-boundary.log). Typechecking certifies well-formed statements, not their proofs.

## Source correspondence and correctness of the boundary

The source principal core matrix after removing `u` has diagonal entries `-a_i` at module vertices and `-sum x_i` at `v`, with symmetric off-diagonal entries `q_i` between `v` and `w_i`. Accordingly its quadratic form is exactly `-sum a_i*z_i^2 + 2*r*sum q_i*z_i - (sum x_i)*r^2`. The definition assembles that expression from independent linear coordinate maps. It does not define the original form to be the proposed diagonal form. The factor two and both diagonal signs are correct.

The explicit `skewProd` has output `(r, z + r*(-q/a))`; the inverse `piOptionEquivProd` places `r` at `none` and each shifted module coordinate at `some i`. Thus the actual linear equivalence has precisely the advertised shear direction, not its inverse. The candidate equality `Q = D.comp E` is the correct orientation. Expanding a module term gives `-a*z^2 + 2*r*q*z - r^2*q^2/a`, and adding `T*r^2` with `T=sum(-x+q^2/a)` cancels the final terms. The hypothesis that every `a_i` is nonzero is essential for that cancellation and is present.

The index theorem uses the genuine Mathlib `sigPos`, defined through maximal dimensions of positive-definite subspaces. It is not a count defined to equal the desired answer. The diagonal `-a_i` is positive exactly when `a_i<0`; the residual coordinate contributes one exactly when `T>0`. Hence the count and strict comparison in the proposed conclusion match the spectral calculation. No eigenvalue or inertia identity is assumed as a premise.

Allowing arbitrary real arrays is a valid generalization of the trigonometric inputs. Allowing `T=0` is also correct: that coordinate then contributes zero to the positive index. The empty module family has `T=0` and a zero form, consistent with the stated conclusion. These finite algebraic generalizations do not claim graph admissibility for small `m`.

The assumptions are nonvacuous: take all `a_i=1`, `q_i=0`, and `x_i=0`. Nothing in the definitions hides the desired theorem as a premise. The equivalence remains well-defined even at zero denominators because Lean's division is total, but neither theorem drops the explicit nonzero assumptions needed for the identity.

## Scope and next gates

This proves the finite core completion of squares and positive-index count. It does not yet construct the full graph matrix, include the pendant coordinate, prove the kernel/congruence reduction at a generic eigenfunction, or identify a metric-graph spectral count with this finite index. Those are correctly listed as missing links. The published spectral theorem is not being smuggled in as a custom Lean axiom.

No mathematical changes are requested. The second independent boundary approval, proof implementation, independent final proof reviews, combined-boundary comparison, and fresh Linux verification remain separate gates. Root's role here is an independent Inertia referee; the implementer may not count its own review as a second approval.
