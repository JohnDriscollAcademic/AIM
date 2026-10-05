# AIM114 graph-length bridge: independent statement referee 2

- **Phase:** independent pre-implementation review of mathematical statements and boundary type-check.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not this boundary's author or implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the three proposed declarations at the exact hashes below.
- **Mechanical result:** Definitions build and Challenge type-check exited zero; the three deliberate placeholders establish no theorem.

## Reviewed evidence

| File | SHA-256 |
|---|---|
| `GraphLengthBridgeChallenge.lean` | `d6ae573f026b748aab738c062995d65f4279f3da4c4f0ec410e4aa5a29cfb793` |
| `GRAPH_LENGTH_BRIDGE_TARGETS.md` | `11566eb5cc9c0903c9b2f8e1cf8dfca0a63b88c8d22d44bba05529ce511cacca` |
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| Existing `AIM/P114/TransferProof.lean` | `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c` |

I read the full candidate boundary and scope document, the actual graph and length definitions, and the existing core-weight proof. I compared the statements with the submitted manuscript's equation (1) and prescribed-length estimate, as presented in the already reviewed `PROOF.md`. The source remains Sidney Holden's submitted v0.3 PDF, SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`. No bridge proof file existed when I started the independent check, and I made no mathematical file changes.

From `/Users/sholden/Projects/AIM/research/lean/114`, I independently ran:

```text
/Users/sholden/.elan/bin/lake build AIM.P114.LengthDefinitions
/Users/sholden/.elan/bin/lake env lean GraphLengthBridgeChallenge.lean
```

The Definitions build passed with 3252 jobs. The candidate type-check passed with exactly the three deliberate `sorry` warnings. The [independent log](../verification/referee-2-graph-length-bridge-boundary-typecheck.log) records commands, outputs, exit codes, input hashes, and unchanged-hash checks after both commands. The [hash manifest](../verification/referee-2-graph-length-bridge-boundary-hashes.json) also includes the pinned toolchain and dependency manifest. This is a local well-formedness check, not proof verification or authoritative Linux validation.

## Exact sums and multiplicity

`actual_graph_core_length_sum` ranges over the full product `Fin m × Fin 3`, and evaluates the approved actual edge assignment at each `some e`. The three labels in every module include both distinct parallel edge identifiers. The index formula is exactly `3*i+j`, so the finite product sum enumerates the first `3m` zero-indexed prime roots once each. Its claimed equality to the existing `coreLength m`, a range sum over those same indices, is correct. It asserts this equality as a conclusion; no reindexing or sum identity is an input hypothesis.

`actual_graph_total_length_sum` ranges over the full actual edge type `Option (Fin m × Fin 3)`. This is the genuine edge set because the unchanged graph definition includes every ambient edge. Splitting its finite sum isolates exactly one `none` pendant term and one copy of every `some` core term. The definition assigns the former precisely `pendantLength m`; the first bridge identity supplies the remaining sum. No sum is taken over adjacent vertex pairs or the simple projection, so parallel edges cannot disappear.

Both equalities are true for every natural module count. At `m=0` the core type is empty, its sum and `coreLength 0` are zero, and the actual pendant assignment is also zero because of its factor `0^6`. Thus the unrestricted identity statements do not assume positive lengths at an invalid index or accidentally assert connectivity for zero modules.

## Fraction bound and source correspondence

`actual_graph_core_length_ratio_bound` explicitly divides the actual core-edge sum by the actual sum over all edges. Substituting the first two conclusions produces exactly the already defined `coreWeight m`. The existing `core_weight_bound` proves its nonnegativity and upper bound `3 / ((m:ℝ)^5+3)` under `1<=m`; the source-facing hypothesis `3<=m` is sufficient.

The denominator is positive throughout this source range: the prescribed pendant is positive and the core sum is nonnegative. Therefore the real division in the statement represents the ordinary fraction of total length, rather than obtaining its inequality from Lean's value for division by zero. The real casts occur before the power and division, so the expression has neither truncated natural arithmetic nor an unintended rational/integer quotient. Both inequalities are correctly non-strict, matching the previously proved bound.

The exponent five follows from the exact prescribed pendant factor `m^6` and `3m` core edges. No abstract length family, assumed monotonicity, replacement pendant factor, or assumed ratio identity appears in any of the three signatures. This is a useful connection between two already formalized constructions, not an assertion that the graph's spectral measure has these mixture weights.

## Review disposition and scope

The target document faithfully explains the exact edge-index sum, its multiplicities, the finite reindexing obligation, and the reduction to the existing transfer result. It retains Sidney Holden's source attribution and explicitly bounds the extension's scope. The source problem's permanent ID and original target are unaffected.

**Requested changes: none.** Approval is specific to the reviewed bytes. A proof must still establish the product-to-range sum, the option-sum identity, and the exact reduction of the displayed fraction; type-checking placeholders does not establish any of them. Independent final proof/axiom review, combined-target integration, and authoritative Linux verification remain later gates.

These statements do not formalize a Kirchhoff operator, a spectral-frequency law, the edge-measure representation, the stable response-ratio law, or the empirical-process/random-index limit. They do not close the full formal counterexample or resolve the separate universal linear-variance assertion.
