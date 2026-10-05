# Independent statement review 1: actual multigraph

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of author and intended implementer `spectral_review`.
- Phase: preproof boundary review.
- Verdict: **APPROVE** the seven signatures at the hashes below. No GraphProof module existed at review time.

## Frozen inputs and independent check

I read the complete definition module, Challenge, and target document, the source graph paragraph in PROOF.md, and the pinned Mathlib definitions of `Graph.Loopless`, `incidenceSet`, `toSimpleGraph`, and `SimpleGraph.Connected`. The source is Sidney Holden's unchanged v0.3 manuscript (PDF SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`); the original AIM 114 target remains at upstream `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| `GraphChallenge.lean` | `d08288b79567924d4e54853b48b48735dd4f37bc15a31e1162c525617f4f68b7` |
| `GRAPH_TARGETS.md` | `ab9f462562e75b7af02d33d5cf70c9af765edc8b14e50c2b960ebb625338633f` |

I independently ran `lake env lean GraphChallenge.lean`. It exited zero with exactly seven deliberate Challenge placeholders; [the log](../verification/referee-1-graph-boundary.log) is retained. This establishes well-formed statements, not their proofs.

## Mathematical correspondence

The vertex type has exactly the m module vertices and u,v,t, distinguished by sum constructors and three different finite indices. Every ambient vertex is included. The edge type has three separate identifiers per module and the pendant; its endpoints agree exactly with the source. In particular, parallel u--w_i edges remain distinct, and the separate parallel-edge theorem checks both their inequality and link relation. Structural Graph obligations in the definition module do not assume any advertised admissibility property.

The seven conclusions are correct at their stated indices. Endpoint constructors exclude loops for every m. With m positive, all vertices are joined through u and any chosen module joins v; no connectivity is asserted at zero. Vertex and edge counts are m+3 and 3m+1. The incidence sets count 2m+1 edges at u, m at v, one at t, and three at each w_i. These are the appropriate degrees after looplessness, and the restriction m>=3 excludes degree two everywhere, including the distinguished v vertex.

Mathlib's `toSimpleGraph` is on the subtype of actual graph vertices and drops parallel-edge multiplicity. Here the vertex set is universal; its connectivity therefore is exactly the requested connectivity. Neither counts nor degrees use this simple graph. `incidenceSet` counts identifiers, not distinct neighbors. The scope document explicitly identifies the no-loop condition needed to interpret incidence counts as degrees.

The final theorem uses integer subtraction. It is the exact Euler expression even at m=0, where it equals -1. No homology dimension is silently substituted for that expression. The source's first Betti-number interpretation in the connected range remains a separate mathematical identification, as advertised.

No conclusion is smuggled into a hypothesis. The only nontrivial input restrictions are m>=1 for connectivity and m>=3 for absence of degree two. The candidate makes no claim about metric lengths, rational independence, a Laplacian, spectral-frequency laws, or the link to the separate quadratic-form block. Those remain substantial obligations and cannot be inferred from this approval.

No changes requested. Both boundary approvals must precede implementation. Independent final proof reviews, transitive axiom checks, and the expanded isolated Linux run remain separate gates.
