# Independent final proof review 1: actual multigraph

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of implementer `spectral_review`.
- Verdict: **APPROVE** all seven frozen statements at the exact hashes below.
- Scope: mathematical/source audit and independent local Lean checks. Expanded isolated Linux verification remains separate.

## Source and independent execution

| File | SHA-256 |
| --- | --- |
| `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| `GraphChallenge.lean` | `d08288b79567924d4e54853b48b48735dd4f37bc15a31e1162c525617f4f68b7` |
| `GRAPH_TARGETS.md` | `ab9f462562e75b7af02d33d5cf70c9af765edc8b14e50c2b960ebb625338633f` |
| `AIM/P114/GraphProof.lean` | `75232119b42e3cffb5829d959fc38842acc1381eeb409da33d9baef9faae95ea` |

The boundary files match my preproof approval exactly. I read the whole proof and explanation and independently ran `lake build AIM.P114.GraphProof`, `lake env lean AIM/P114/GraphProof.lean`, and a fresh import printing each advertised declaration's axioms. All exited zero; separate [build](../verification/referee-1-graph-build.log), [re-elaboration](../verification/referee-1-graph-reelaboration.log), and [axiom](../verification/referee-1-graph-axioms.log) records are retained. Six declarations use exactly `propext`, `Classical.choice`, and `Quot.sound`; `counterexample_parallel_edges` uses only `propext` and `Quot.sound`. There are no additional axioms, proof placeholders, native evaluation, or Challenge imports in the proof closure.

## Actual proof obligations

Looplessness is proved by the pendant/module split and all three finite module labels. The endpoint definitions separate the distinguished vertices or the two constructors of the vertex sum type. It is not an input assumption.

Connectivity uses actual links and the established looplessness to construct adjacency on the subtype of graph vertices. It explicitly reaches every module vertex from u, reaches t using the pendant, and reaches v through module zero, whose existence is proved from m>=1. Reflexivity handles u. Thus every vertex is reached with the exact stated index restriction; there is no hidden assumption that `Fin m` is inhabited at zero.

The actual vertex and edge sets are universal finite sets. Their counts reduce to sum, product, and option cardinalities. The parallel-edge theorem separately checks the unequal edge IDs and their actual common endpoint relation. Connectivity's simple-graph projection does not enter any count.

The incident-count helper derives a set equality from `Graph.Inc` and the explicit symmetric `IsLink` relation. It then counts actual edge IDs by a finite indicator sum. The subsequent option/product splits and exhaustive three-label sum give 2m+1, m, 1, and 3 at u,v,t,w_i respectively, including all the small-index cases stated in the boundary. The degree-two exclusion covers every sum-type vertex and uses m>=3 exactly where needed. Both parallel edges contribute separately.

The Euler theorem uses the proved set cardinalities and integer cast/subtraction arithmetic. It makes no homology-dimension claim, in particular at m=0 where the Euler expression is -1. This matches the reviewed scope and prevents a disconnected zero-index artifact from being presented as a Betti number.

No advertised graph property is a hypothesis. The implementation is faithful to the source finite multigraph, with the documented small-index generalizations. It does not define edge lengths or a metric realization, prove joint rational independence, define the Kirchhoff operator, identify the graph matrix with the separately proved quadratic form, or establish spectral surplus convergence. This approval concerns precisely seven finite combinatorial conclusions and does not certify the complete counterexample.
