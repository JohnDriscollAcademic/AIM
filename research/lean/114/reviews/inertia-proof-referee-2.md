# AIM114 finite-inertia extension: independent proof referee 2

- **Phase:** final source, mathematical fidelity, correctness, reuse, and mechanical reproduction.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the inertia implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** both public inertia declarations at the exact hashes below.
- **Independent results:** module build, fresh direct re-elaboration, and both transitive-axiom checks passed locally on macOS.
- **Limit:** no authoritative isolated-Linux verification, kernel replay, or Comparator execution of this extension is claimed. The spectral interpretation remains an explicit unformalized application.

## Exact source and fresh checks

| File | SHA-256 |
|---|---|
| `AIM/P114/InertiaDefinitions.lean` | `d40bb849d050150f4688bee02ba4f2a88341593f1c37114d253c79b2651b0795` |
| `AIM/P114/InertiaProof.lean` | `d0acd2dfda515f792ca12195be04b1b07d0ca76e75e7cb20b1afd0e09e06345d` |
| `InertiaChallenge.lean` | `0c4fc841423c270b32cfe8761ec6258df1e30e8946ac4c396bfcbd94c1505e72` |
| `INERTIA_TARGETS.md` | `4f847915317cc8721e5108dd4fe3efc0209706a686ea9353576569a68cc245a1` |
| `INERTIA_PROOF.md` | `7ae3749e8401be0795478f54c94bee2c29dc1cf158d89d15085084771a4d39d2` |

The definitions and boundary documents match my [pre-implementation approval](inertia-statement-referee-2.md), which records the unchanged source manuscript and canonical-target hashes. I read the actual final proof and its explanation before executing it; I made no proof edits and did not rely on the implementer's reported results.

From `/Users/sholden/Projects/AIM/research/lean/114`, I independently ran:

| Command | Result | Log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.InertiaProof` | Exit 0; successful 3014-job build | [build](../verification/referee-2-inertia-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/InertiaProof.lean` | Exit 0; fresh re-elaboration, no diagnostics | [re-elaboration](../verification/referee-2-inertia-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-inertia-axioms.lean` | Exit 0; both axiom lists printed | [axioms](../verification/referee-2-inertia-axioms.log) |

The last log contains the complete temporary probe source. For both `AIM.P114.core_completion_of_squares` and `AIM.P114.core_positive_index`, the transitive axioms are exactly

```text
[propext, Classical.choice, Quot.sound]
```

The [hash manifest](../verification/referee-2-inertia-hashes.json) records source and pinned dependency/toolchain inputs; rehashing after every command showed no changes. The [source audit](../verification/referee-2-inertia-source-audit.log) confirms both signatures match the frozen Challenge after whitespace normalization. This source comparison is not an authoritative Comparator run. Neither proof nor definitions imports Challenge.

## Completion-of-squares proof

The proof establishes equality of the actual bundled quadratic forms by evaluating them at an arbitrary point `(r,z)`. Unfolding the concrete coordinate maps, shear, option-index reindexing, and weighted sums of squares yields the original cross-term expression and the claimed diagonal pullback. Finite-sum identities reduce equality to one scalar identity for each module.

For each index `i`, `field_simp [ha i]` uses exactly the supplied nonzero denominator hypothesis for `a_i`. Exact `ring` normalization then proves the identity. No proposed diagonalization, determinant, inertia count, or spectral assertion is assumed. The sign of the shear and the factor two in the original cross term agree with the source, as verified in the boundary review: the diagonal term is `-a_i*(z_i-r*q_i/a_i)^2`, and the residual scalar coefficient is `sum_i(-x_i+q_i^2/a_i)`.

The argument is uniform over all natural `m`, including the empty sum. It is not a fixed-size matrix calculation or a sampled numerical check. The hypotheses allow all real `q,x` and every nonzero `a_i`; there are no accidental positivity assumptions.

## Positive-index proof

The second theorem constructs a genuine `QuadraticMap.IsometryEquiv` using the explicit `coreDiagonalizingEquiv`. Its required pointwise form-preservation field comes from evaluation of the first theorem; the symmetry is in the correct direction for the isometry API. Therefore the subsequent `QuadraticForm.sigPos_of_equiv_weightedSumSquares` invocation applies to the actual real quadratic form via an invertible coordinate change.

That library theorem counts positive diagonal weights according to the standard maximal-positive-subspace definition of `sigPos`. The proof converts the resulting finite set cardinality into sums of indicators and splits the option-indexed sum into its `none` and `some` coordinates. Positivity of the scalar weight is exactly `T>0`, while positivity of each module weight `-a_i` is exactly `a_i<0`. The simplifications preserve the strict inequalities and give the advertised natural-number count.

No residual nonzero-pivot hypothesis is introduced. If `T=0`, the scalar coordinate is null and its positive-index contribution is zero. If `m=0`, the form on the one remaining scalar coordinate is zero and the final count is zero. These valid degenerate cases remain covered by the final proof. Conversely, the required `a_i!=0` hypotheses are not removed or replaced by Lean's totalized division.

## Quality, correspondence, and remaining scope

The implementation appropriately reuses the existing explicit linear equivalence, quadratic-form extensionality, exact field/ring arithmetic, and Mathlib's Sylvester/inertia API. It does not define a new “positive index” to equal the desired count. The proof is short because the substantial invariant is supplied by the established library theorem, while the source-specific form identity is proved directly. Its explanatory document accurately describes both paths and the limitations.

The finite form and coordinate meanings match the core of the vertex matrix after removing `u`: scalar coordinate at `v`, module coordinates at the `w_i`, with the pendant coordinate omitted. However the formal package still does not construct the full graph matrix, prove the generic kernel congruence, identify matrix positive eigenvalue count with the spectral index, establish the edge zero-count formula, or combine the pendant cancellation with a nodal-surplus law. Those application links remain outside these two declarations and are not being claimed as proved.

**Blocking findings: none.** These are exact finite-dimensional core results faithful to manuscript Lemma 1. Combined-target integration and authoritative Linux verification remain separate gates. A complete formal quantum-graph counterexample and the independent universal variance target do not follow from this extension alone.
