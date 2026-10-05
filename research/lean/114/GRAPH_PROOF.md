# Actual multigraph admissibility proof

The seven declarations in `AIM/P114/GraphProof.lean` prove the finite graph
conditions from Section 1 of Sidney Holden's v0.3 manuscript. The two
independent statement approvals preceded implementation; the definition,
challenge, and target-document bytes remain unchanged.

The graph is the actual `Graph` from the approved boundary, with all `3m+1`
edge identifiers retained. Looplessness follows by separating the pendant
edge and the three possible module labels: the endpoints always lie in
distinct distinguished vertices or different sides of the vertex sum type.
For connectivity, the proof constructs actual links `u-w_i`, `w_i-v`, and
`u-t`, then uses their images in `toSimpleGraph` as one-edge walks. The route
`u-w_0-v` is available whenever `m>=1`. These walks reach every vertex.
Only connectivity uses this simple projection.

Vertex and edge cardinalities reduce to the finite sum, product, and option
types underlying the actual full vertex and edge sets. A separate theorem
proves that module edge IDs zero and one are unequal and both link `u` to
the same `w_i`, so the parallel edges are explicitly verified.

The degree proof first identifies the actual multigraph `incidenceSet v`
with the set of edge IDs for which `v` equals either endpoint. Its cardinality
is a finite sum of indicator values. Splitting the option sum separates the
pendant; splitting the product sum and enumerating the three module labels
gives incident-edge counts `2m+1,m,1,3` at `u,v,t,w_i`. Parallel edges each
contribute separately. The counts equal multigraph degrees because this graph
is loopless. Case analysis on every vertex and elementary arithmetic then
exclude degree two for `m>=3`.

Finally, the Euler result substitutes the proved actual set cardinalities
into integer arithmetic, obtaining `|E|-|V|+1=2m-1`. It does not claim that a
cycle-space or homology dimension was defined or identified. The formula is
valid at zero as an integer identity, while connectivity has its explicit
positive-index hypothesis and source admissibility uses `m>=3`.

No theorem assumes any of the advertised graph conditions as an input. No
Challenge is imported, and the implementation contains no proof placeholders,
new axioms, or native evaluation. It defines no metric realization or spectral
operator and does not establish joint rational independence of edge lengths.
Those remain separate obligations, as do the graph-to-matrix and spectral
surplus connections.
