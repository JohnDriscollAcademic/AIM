# AIM114 graph-length bridge: independent proof referee 2

- **Phase:** final source, graph-length fidelity, correctness, reuse, and independent mechanical reproduction.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not this block's author or implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** all three declarations at the reviewed hashes.
- **Independent results:** module build, fresh direct re-elaboration, signature comparison, and all three transitive-axiom checks passed locally on macOS.
- **Limits:** this is not authoritative isolated-Linux verification, kernel replay, or a Comparator run; no spectral-law identification follows from these three results alone.

## Exact evidence and reproduction

| File | SHA-256 |
|---|---|
| `AIM/P114/GraphLengthBridgeProof.lean` | `bf60f07bc4ddb86274f7a7098709db825e15b47390e2966ba4b376c453922aea` |
| `GraphLengthBridgeChallenge.lean` | `d6ae573f026b748aab738c062995d65f4279f3da4c4f0ec410e4aa5a29cfb793` |
| `GRAPH_LENGTH_BRIDGE_TARGETS.md` | `11566eb5cc9c0903c9b2f8e1cf8dfca0a63b88c8d22d44bba05529ce511cacca` |
| `GRAPH_LENGTH_BRIDGE_PROOF.md` | `669a5a5228d2db7a19222b279dfaaefd0c2ea66d0ccbba2c9a824f7784b33448` |
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| `AIM/P114/TransferProof.lean` | `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c` |

The boundary and imported definitions agree with my [pre-proof statement approval](graph-length-bridge-statement-referee-2.md). I read the entire final proof and its explanation, inspected the pinned library's actual `finProdFinEquiv` definition, and checked reuse of the previously reviewed `core_weight_bound`. I made no mathematical file changes.

From `/Users/sholden/Projects/AIM/research/lean/114`, I independently ran:

| Command | Result | Independent log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.GraphLengthBridgeProof` | Exit 0; successful 3254-job build | [build](../verification/referee-2-graph-length-bridge-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/GraphLengthBridgeProof.lean` | Exit 0; fresh re-elaboration with no diagnostics | [re-elaboration](../verification/referee-2-graph-length-bridge-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-graph-length-bridge-axioms.lean` | Exit 0; all three axiom lists printed | [axioms](../verification/referee-2-graph-length-bridge-axioms.log) |

The temporary probe's complete source is retained in the axiom log. Each of `actual_graph_core_length_sum`, `actual_graph_total_length_sum`, and `actual_graph_core_length_ratio_bound` depends on exactly `[propext, Classical.choice, Quot.sound]`. There is no custom axiom or `sorryAx` in these transitive dependencies.

The [hash manifest](../verification/referee-2-graph-length-bridge-hashes.json) includes all reviewed inputs and the pinned dependency/toolchain files. The runner verified unchanged hashes after every command. All three public theorem signatures match frozen Challenge after whitespace normalization, as recorded in the [source-signature audit](../verification/referee-2-graph-length-bridge-source-audit.log). That comparison is not an authoritative Comparator run. The proof imports only the actual length definitions and the existing transfer proof; it contains no Challenge import, placeholder, or native-computation shortcut.

## Core sum: actual bijective reindexing

The first theorem starts with the actual prescribed lengths indexed by the complete product `Fin m × Fin 3`. `Fintype.sum_equiv finProdFinEquiv` changes this to a sum over `Fin (m*3)`. In the pinned library the equivalence's underlying natural index is exactly `j+3*i`, and the proof explicitly simplifies this to the assignment's `3*i+j`. Thus the summands match under a proved bijection; this is not merely a cardinality argument or a proposed reindexing with an unproved surjectivity claim.

`Fin.sum_univ_eq_sum_range` then changes that finite-type sum into the range sum, and multiplication commutativity identifies `m*3` with `3*m`. Unfolding `coreLength` gives precisely the previously defined sum. Both separately identified parallel edges retain their own label and prime-root summand. No quotient by endpoint pairs or sum over distinct neighbors appears.

The equivalence and sum conversion are valid also when `m=0`, where the product type and target finite type are both empty. Hence the first unrestricted identity has no hidden positive-module hypothesis.

## Total sum: unique pendant and every core edge

The actual edge type is the option type over that complete core product, and the graph's edge set is universal. `Fintype.sum_option` therefore separates the full actual-edge sum into exactly one `none` term and all `some` terms. The preceding theorem supplies the core contribution, and the unchanged assignment definition supplies the exact pendant contribution. Commutativity of addition puts the result in the target order `coreLength m + pendantLength m`.

This proof retains the prescribed pendant factor `m^6`; it does not identify its length with the unscaled next prime root. The identity remains valid at `m=0`, when the core sum is empty and the pendant's assigned length is zero. No positivity or connectivity assertion is silently claimed in that case.

## Fraction bound: exact reuse of the scalar theorem

The final theorem rewrites both occurrences of the actual core sum and both occurrences of the actual total sum using the first two results. The resulting fraction is definitionally the existing `coreWeight m`. The checked `core_weight_bound` supplies the two required inequalities, and `omega` derives its hypothesis `1<=m` from the source range `3<=m`.

The previously reviewed scalar proof establishes positivity of the total length before using division inequalities: the core sum is nonnegative and the prescribed pendant is positive in this range. Accordingly the bridge concerns an ordinary positive-denominator fraction, rather than relying on Lean's totalized division at zero. The exact exponent and constant in `3 / ((m:ℝ)^5+3)` are unchanged. No assumed sum identity, graph-to-weight correspondence, or inequality is introduced as a new hypothesis.

## Quality, correspondence, and scope

The implementation is short because it reuses the appropriate finite-sum equivalence, option-sum, and already verified length-bound results. All three proof paths are exact and uniform in `m`; none enumerates sample graph sizes. `GRAPH_LENGTH_BRIDGE_PROOF.md` accurately describes those paths, and the approved target document continues to identify Sidney Holden's source manuscript.

These results close the finite algebraic connection between the actual edge assignment and the existing scalar core fraction. They do not identify the quantum graph's spectral-frequency law with the edge-mixture or module law, define the Kirchhoff Laplacian, construct the stable response law, or prove empirical-process and random-evaluation convergence. The package remains a partial formalization of the counterexample, and the separate universal linear-variance question remains unresolved.

**Blocking findings: none.** Approval is limited to the exact three supporting results and source hashes above. Final combined-target integration and authoritative Linux verification remain separate gates; no further theorem scope is endorsed by this report.
