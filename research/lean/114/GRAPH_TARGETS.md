# Exact candidate boundary: multigraph admissibility

This extension models the actual graph in Section 1 of Sidney Holden's v0.3
manuscript, whose immutable PDF SHA-256 is
`74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.
The original AIM 114 target is preserved at upstream revision
`8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. The seven advertised declarations
are in `GraphChallenge.lean`; the actual objects are in
`AIM/P114/GraphDefinitions.lean`. Two independent approvals of these exact
files are required before proof implementation. Challenge placeholders are
not certificates and must not be imported by Solution.

## Actual multigraph

`counterexampleGraph m` has Mathlib type
`Graph (CounterexampleVertex m) (CounterexampleEdge m)`.
Its vertex type is `Fin m ⊕ Fin 3`: `Sum.inl i` denotes `w_i`, and the three
`Sum.inr` values `0,1,2` denote `u,v,t`, respectively. All ambient vertices
belong to the graph's actual `vertexSet`.

Its edge type is `Option (Fin m × Fin 3)`: `none` denotes the pendant `ut`;
`some (i,0)` and `some (i,1)` are distinct edges from `u` to `w_i`; and
`some (i,2)` connects `w_i` to `v`. All these identifiers belong to the
actual `edgeSet`. `counterexampleEnds` supplies a chosen pair of endpoints
for each edge, and `IsLink` is explicitly the two possible orders of that
pair. Only the symmetry, endpoint uniqueness, and membership obligations
required to construct a `Graph` are proved in the definition module.

Parallel edges are retained, not collapsed into adjacency pairs. Every
cardinality and degree statement uses the actual multigraph's edge identifiers.
The only use of `toSimpleGraph` is to formulate connectivity, since collapsing
parallel edges does not change whether two vertices are reachable. It does
change edge counts and degrees, so those statements never use simple-graph
edge or neighbor counts.

## Seven advertised conclusions

1. `counterexample_loopless`: the actual graph satisfies Mathlib's
   `Graph.Loopless` for every natural `m`.
2. `counterexample_connected`: its actual vertices are connected via
   `Graph.toSimpleGraph.Connected` whenever `m>=1`. One module suffices to
   join `u` to `v`, so this valid generalization includes the source range
   `m>=3`. No connectedness claim is made at `m=0`, where `v` is isolated.
3. `counterexample_cardinalities`: the actual finite sets have `m+3` vertices
   and `3m+1` edges, for every `m`.
4. `counterexample_parallel_edges`: for each module, edge identifiers
   `some(i,0)` and `some(i,1)` are unequal, and both are actual links between
   `u` and `w_i`. This explicitly checks that the implementation retains the
   source's parallel edges.
5. `counterexample_degrees`: cardinalities of the actual `incidenceSet`s
   at `u,v,t,w_i` are `2m+1,m,1,3`, respectively. Mathlib's present `Graph`
   API supplies `incidenceSet`, but no general multigraph degree definition
   was found in its six graph modules. For a loopless graph these incidence
   counts are precisely its multigraph degrees; every distinct incident edge
   is counted once. This convention would undercount loops in an arbitrary
   graph, which is why the separate looplessness conclusion matters.
6. `counterexample_no_degree_two`: for `m>=3`, every actual vertex has an
   incident-edge count different from two. The vertex type contains no unused
   vertices, and its three distinguished vertices and all module vertices are
   covered. This is the source's degree restriction.
7. `counterexample_euler_count`: using the actual vertex and edge cardinalities,
   integer arithmetic gives `|E|-|V|+1 = 2m-1`. It is valid for every `m`, with
   value `-1` at zero. For connected graphs in the source range it is the
   familiar Euler expression used for the first Betti number. The theorem
   itself is deliberately only the integer Euler expression, not a claim
   that a cycle-space or homology dimension has been formalized.

All theorem hypotheses refer only to the index or the actual finite objects.
No connectivity, cardinality, degree, looplessness, or parallel-edge property
is supplied as an input assumption. The construction is defined at small
indices to avoid partial definitions; admissibility is asserted in the
source's `m>=3` range, with clearly stated stronger component results.

## Remaining scope

This block establishes the finite combinatorial graph conditions. It defines
no edge-length assignment, metric realization, standard Kirchhoff Laplacian,
secular manifold, eigenfunction, or spectral-frequency law. The separate
Transfer block concerns the prescribed prime-root sums, but linking those
lengths to these particular edges and proving their joint rational
independence remain separate obligations. Positivity of individual prime
roots is not a proof of joint rational independence.

No cycle-space dimension theorem for `Graph` was found in the pinned graph
modules. Accordingly this boundary makes no homological claim and introduces
no custom `Betti` definition that would disguise the missing identification.
It also does not establish the graph's vertex matrix or connect this graph
to the separately proved core quadratic form and spectral surplus formula.

## Pinned library and boundary verification

The project pins Mathlib revision
`0df444a360eaa60ab8c11dca51a86af692955474`. Relevant actual APIs are:

- [`Graph`, distinct edge identifiers, and `incidenceSet`](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/Graph/Basic.lean).
- [`Graph.Loopless` and `Graph.toSimpleGraph`](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/Graph/Simple.lean).
- [`SimpleGraph.Connected` and reachability](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Combinatorics/SimpleGraph/Connectivity/Connected.lean).

The definition module and all seven candidate Challenge signatures are
type-checked separately; the retained log is
`verification/graph-boundary-typecheck.log`. Boundary type-checking with
deliberate Challenge placeholders does not certify any advertised theorem.
