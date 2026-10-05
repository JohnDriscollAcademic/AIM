# Independent final proof review 1: graph length sums and weight

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of implementer `lean_feasibility`.
- Verdict: **APPROVE** all three frozen conclusions at the hashes below.

| Input | SHA-256 |
| --- | --- |
| `GraphLengthBridgeChallenge.lean` | `d6ae573f026b748aab738c062995d65f4279f3da4c4f0ec410e4aa5a29cfb793` |
| `GRAPH_LENGTH_BRIDGE_TARGETS.md` | `11566eb5cc9c0903c9b2f8e1cf8dfca0a63b88c8d22d44bba05529ce511cacca` |
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `AIM/P114/GraphLengthBridgeProof.lean` | `bf60f07bc4ddb86274f7a7098709db825e15b47390e2966ba4b376c453922aea` |

The approved boundary is unchanged. I read the entire proof and independently ran the module build, fresh direct source re-elaboration, and a fresh import printing all three axiom sets. All exited zero, and the source hash was unchanged before and after execution. Separate [build](../verification/referee-1-graph-length-bridge-build.log), [re-elaboration](../verification/referee-1-graph-length-bridge-reelaboration.log), and [axiom](../verification/referee-1-graph-length-bridge-axioms.log) records are retained. Each result uses exactly `propext`, `Classical.choice`, and `Quot.sound`; no additional axiom, placeholder, native evaluation, or Challenge import is present in the proof closure.

`Fintype.sum_equiv finProdFinEquiv` supplies an actual bijection between the finite core-edge pairs and consecutive finite indices. The proof checks its formula against `counterexampleMetricLength`, including the order of addition and multiplication. Converting the finite-index sum to the range sum then gives the exact existing `coreLength` definition. Consequently no edge is omitted, duplicated, or identified with its parallel neighbor.

The option-type sum splits into precisely the unique pendant and all core entries. Substituting the first theorem yields the actual total sum, with the pendant formula unchanged. Both identities retain the all-natural-index quantifier, including the empty-core zero case.

The final proof rewrites both actual sums using these established identities and applies the already reviewed `core_weight_bound`, discharging m>=1 from m>=3. It supplies no abstract weight or assumed sum identity. This therefore closes the documented finite bookkeeping link between the actual graph assignment and the prescribed fraction bound.

The proof is correct and source-faithful within its exact scope. It does not establish a spectral measure-mixture identity, stable response law, or process limit. Integrated isolated Linux verification remains a distinct mechanical gate, and these results cannot certify the complete counterexample.
