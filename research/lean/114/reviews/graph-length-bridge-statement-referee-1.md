# Independent statement review 1: actual graph length sums

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of intended implementer `lean_feasibility`.
- Verdict: **APPROVE** these three signatures before implementation. No GraphLengthBridgeProof existed at review time.

| Frozen input | SHA-256 |
| --- | --- |
| `GraphLengthBridgeChallenge.lean` | `d6ae573f026b748aab738c062995d65f4279f3da4c4f0ec410e4aa5a29cfb793` |
| `GRAPH_LENGTH_BRIDGE_TARGETS.md` | `11566eb5cc9c0903c9b2f8e1cf8dfca0a63b88c8d22d44bba05529ce511cacca` |
| Imported `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |

I read the complete boundary and unchanged imported definitions and independently ran `lake env lean GraphLengthBridgeChallenge.lean`: exit zero, exactly three deliberate statement placeholders, [log retained](../verification/referee-1-graph-length-bridge-boundary.log). This is a well-formedness check only. The mathematical source remains Sidney Holden's v0.3 manuscript, PDF SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.

The first identity sums actual assigned lengths over `Fin m × Fin 3`, retaining each parallel edge. The source ordering 3i+j enumerates precisely the indices in `Finset.range (3*m)` once each; its sum therefore is the existing `coreLength`. The second identity sums the actual `CounterexampleEdge m` option type and adds the single pendant exactly once. Both identities hold at zero as well as at positive indices, without an independence or positivity assumption.

The third statement displays both actual sums directly in its ratio. After the first two identities it is exactly `coreWeight m`, so the existing `core_weight_bound` applies because m>=3 implies m>=1. All lengths and the total denominator are positive in that source range by the completed Length block. The bound does not assume a sum equality, a contamination law, or a spectral interpretation. No custom predicate hides those obligations.

The statements faithfully connect the actual finite graph and length assignment to the earlier prescribed-weight formula. They do not supply the external spectral edge-mixture law, stable ratio, or process limit. No changes requested. Both statement approvals must precede implementation; two independent final reviews and the final expanded Linux check remain required.
