# Independent proof review 1: finite core inertia

- Date: 2026-10-05; completed after resuming the saved checkpoint.
- Reviewer: root Codex AI agent, independent of the Inertia implementer `spectral_review`. Root's separate authorship of the Transfer block is not presented as independence for that block.
- Verdict: **APPROVE** both finite-inertia proofs at the exact hashes below.

I read the complete actual definitions, Challenge, proof and scope explanation and compared them with my [preproof approval](inertia-statement-referee-1.md). The source remains Sidney Holden's v0.3 manuscript and the original AIM114 target. The three boundary files are unchanged. I did not edit the Inertia proof.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/InertiaDefinitions.lean` | `d40bb849d050150f4688bee02ba4f2a88341593f1c37114d253c79b2651b0795` |
| `InertiaChallenge.lean` | `0c4fc841423c270b32cfe8761ec6258df1e30e8946ac4c396bfcbd94c1505e72` |
| `INERTIA_TARGETS.md` | `4f847915317cc8721e5108dd4fe3efc0209706a686ea9353576569a68cc245a1` |
| `AIM/P114/InertiaProof.lean` | `d0acd2dfda515f792ca12195be04b1b07d0ca76e75e7cb20b1afd0e09e06345d` |

`core_completion_of_squares` evaluates the genuine quadratic forms on an arbitrary `(r,z)`, expands the actual shear and option-coordinate reindexing, distributes the finite sums, and proves each scalar identity with exact arithmetic. `field_simp [ha i]` uses the required nonzero denominator at that same index. The sign of the shift, the factor two in the cross term, and the residual Schur coefficient agree with the source. No diagonalization conclusion appears as a premise or definition of the original form.

`core_positive_index` packages the equality as a genuine quadratic-form isometry using the explicit linear equivalence. It then applies Mathlib's Sylvester signature theorem and counts positive option-indexed weights. Positivity of `-a_i` correctly becomes `a_i<0`, and the scalar contributes exactly when `T>0`. The proof uses the actual maximal-positive-subspace `sigPos`, not a custom pivot-count definition. The permitted cases `T=0` and `m=0` remain covered.

The implementation appropriately reuses existing finite-dimensional linear algebra. It contains no unproved claim, custom axiom, native evaluation, or import of any Challenge. It proves the finite core result only: the full graph matrix, pendant cancellation, generic-kernel congruence, spectral counting formula, and quantum-graph interpretation remain unformalized.

I independently executed the following before the pause and retained their unmodified logs; the source hashes are unchanged on resumption:

- `lake build AIM.P114.InertiaProof`: exit zero, [build log](../verification/referee-1-inertia-build.log).
- `lake env lean AIM/P114/InertiaProof.lean`: exit zero, [fresh elaboration](../verification/referee-1-inertia-reelaboration.log).
- Separate probe importing the proof and printing both advertised declarations: exit zero, [axioms](../verification/referee-1-inertia-axioms.log).

Both transitive axiom sets are exactly `propext`, `Classical.choice`, and `Quot.sound`. The [source hash manifest](../verification/referee-1-inertia-source-sha256.json) fixes the inspected bytes. These are my own local commands, not a new isolated Linux verification. Combined-target integration and fresh Linux evidence are still separate gates. No blocking finding remains.
