# AIM114 multigraph extension: independent statement referee 2

- **Phase:** pre-implementation mathematical-boundary review and independent type-checking.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the graph boundary author or implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the seven proposed declarations at the exact hashes below.
- **Independent mechanical result:** Definitions build and Challenge type-check both exited zero. The seven intentional Challenge placeholders remain unproved and certify no theorem.

## Exact sources and independent boundary check

| File | SHA-256 |
|---|---|
| `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| `GraphChallenge.lean` | `d08288b79567924d4e54853b48b48735dd4f37bc15a31e1162c525617f4f68b7` |
| `GRAPH_TARGETS.md` | `ab9f462562e75b7af02d33d5cf70c9af765edc8b14e50c2b960ebb625338633f` |
| Submitted v0.3 PDF | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Frozen source problem `statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| Expanded informal `PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |

I read all three candidate files and compared their actual graph with manuscript Section 1. I independently inspected the pinned library definitions of `Graph`, `Graph.Inc`, `incidenceSet`, `Graph.Loopless`, `Graph.toSimpleGraph`, and `SimpleGraph.Connected`. No GraphProof was supplied or used as evidence, and no proof edits were made by me.

From `/Users/sholden/Projects/AIM/research/lean/114`, I ran:

```text
/Users/sholden/.elan/bin/lake build AIM.P114.GraphDefinitions
/Users/sholden/.elan/bin/lake env lean GraphChallenge.lean
```

The first command completed a successful 3027-job build. The second exited zero with precisely the seven deliberate `sorry` warnings. My [independent log](../verification/referee-2-graph-boundary-typecheck.log) retains commands, output, hashes, exit codes, and confirmation that all three reviewed sources were unchanged after each command. This checks well-formedness of the exact frozen boundary, not correctness of the advertised conclusions.

## Concrete graph and source correspondence

The actual vertex type `Fin m ⊕ Fin 3` contains exactly the `m` module vertices and the distinct vertices `u,v,t`. All are in the actual vertex set; there are no extraneous ambient vertices omitted from the graph. The actual edge type `Option (Fin m × Fin 3)` has one pendant identifier and three distinct identifiers per module. The endpoint function sends labels zero and one to `(u,w_i)`, label two to `(w_i,v)`, and the pendant to `(u,t)`. The link relation is precisely either ordering of those endpoints. Its structural constructor proofs establish only the valid-graph obligations.

This is the manuscript's multigraph. Parallel edges remain separate elements of the edge type even though their endpoint pairs agree. None of the cardinality or incident-edge statements substitutes a simple-graph edge set. The library's `toSimpleGraph` has vertex type equal to the graph's actual vertex-set subtype and adjacency given by distinctness plus existence of a link. Its use solely for connectivity therefore preserves reachability and does not silently alter the original graph for the other conclusions.

## Seven statements

**Looplessness.** Every endpoint pair is between distinct distinguished vertices or between the disjoint summands of the vertex type. The conclusion is the actual library `Graph.Loopless`, which excludes a loop at every edge and vertex. It is true even at `m=0`, when only the pendant remains and `v` is isolated.

**Connectivity.** For `m>=1`, each `w_i` is adjacent to `u`; `t` is adjacent to `u`; and the existing module with index zero provides a path `u,w_0,v`. Hence all actual vertices lie in one component, which is nonempty. This matches `SimpleGraph.Connected` rather than only a vacuous pairwise relation on an empty type. The theorem does not claim connectivity at `m=0`, where it would be false. The generalization from the source's `m>=3` to `m>=1` is valid.

**Cardinalities.** Actual universal vertex and edge sets on these finite types have cardinalities `m+3` and `3m+1`. Both counts include the pendant and all parallel-edge identifiers and cover every natural `m`.

**Parallel edges.** The assertion explicitly requires the two identifiers `some(i,0)` and `some(i,1)` to be different and both to satisfy the actual link relation between `u` and `w_i`. This prevents the common erroneous collapse into one adjacency edge and directly validates the feature used in the source construction. At `m=0` the quantified module type is empty, consistently with there being no modules.

**Incident-edge counts.** `incidenceSet` is the actual set of edge identifiers incident to the given vertex, according to the pinned library's definition. Thus `u` has the two edges from each module plus the pendant (`2m+1`), `v` has the label-two edges (`m`), `t` has only the pendant (one), and each module vertex has its three labels (three). Parallel edges count separately. For the already asserted loopless graph these counts are precisely multigraph degrees. The document correctly avoids identifying this convention with the usual loop-counting degree for arbitrary graphs that have loops.

**No degree two.** The source range `m>=3` is necessary for the stated uniform conclusion: the vertex `v` would have incident count two at `m=2`. Within the advertised range, the counts at `u,v,t,w_i` are respectively at least seven, at least three, one, and three, none equal to two. Quantification over the complete actual vertex type covers all vertices.

**Euler expression.** The integer expression is `(3m+1)-(m+3)+1=2m-1`. Casting set cardinalities to integers avoids truncated subtraction at small indices. The claim is true also at `m=0`, giving `-1`, and is accurately documented as an Euler expression rather than a cycle-space dimension at that disconnected index. The declaration does not define a fake Betti number equal to this expression or assert an unproved homological identification.

## Scope, non-vacuity, and disposition

All properties are conclusions about an explicitly constructed graph, rather than input assumptions or definitions that encode the desired answers. Each source-range hypothesis is satisfiable; `m=3` already produces a finite connected loopless multigraph with the displayed counts and degrees. The preproof boundary has no mathematical inconsistency or vacuity.

This extension would establish the finite combinatorial conditions of the source graph. It does not assign the prescribed lengths to those actual edge identifiers, prove rational independence, define a compact metric graph or Kirchhoff Laplacian, build its vertex matrix, identify its cycle-space dimension, or connect it to the separately formalized quadratic form and surplus law. The existing scalar length-sum formalization is relevant but does not by itself supply those missing graph/length links. These gaps are expressly retained in the scope document.

**Requested mathematical changes: none.** Approval applies to the exact listed bytes. A second independent approval, actual proof implementation without Challenge imports, independent final proof review, combined-target integration, and authoritative Linux checks remain later requirements. Neither this boundary check nor future success on these seven structural theorems alone would prove the complete quantum-graph counterexample or settle the separate universal variance assertion.
