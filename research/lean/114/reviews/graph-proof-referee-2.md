# AIM114 multigraph extension: independent proof referee 2

- **Phase:** final source, graph fidelity, correctness, reuse, and independent mechanical reproduction.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the graph implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the seven graph declarations at the reviewed hashes.
- **Independent results:** module build, fresh direct re-elaboration, and seven transitive-axiom checks passed locally on macOS.
- **Limits:** this report does not claim authoritative isolated-Linux verification, kernel replay, or Comparator execution. Metric lengths, rational independence, homological identification, and the spectral interpretation remain separate obligations.

## Exact evidence and local reproduction

| File | SHA-256 |
|---|---|
| `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| `AIM/P114/GraphProof.lean` | `75232119b42e3cffb5829d959fc38842acc1381eeb409da33d9baef9faae95ea` |
| `GraphChallenge.lean` | `d08288b79567924d4e54853b48b48735dd4f37bc15a31e1162c525617f4f68b7` |
| `GRAPH_TARGETS.md` | `ab9f462562e75b7af02d33d5cf70c9af765edc8b14e50c2b960ebb625338633f` |
| `GRAPH_PROOF.md` | `3b969cb86b00fec44a9d9236cfed60cbd46fa33fc66932ecaafdd0e382cc49de` |

The boundary hashes agree with my [independent pre-proof approval](graph-statement-referee-2.md), which records the source-manuscript and canonical-target hashes and my direct boundary type-check. I read the final proof and explanation before running these new checks, made no proof edits, and did not use the implementer's output as evidence.

From `/Users/sholden/Projects/AIM/research/lean/114`, I ran:

| Command | Result | Independent log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.GraphProof` | Exit 0; successful 3028-job build | [build](../verification/referee-2-graph-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/GraphProof.lean` | Exit 0; fresh direct re-elaboration, no diagnostics | [re-elaboration](../verification/referee-2-graph-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-graph-axioms.lean` | Exit 0; all seven axiom lists printed | [axioms](../verification/referee-2-graph-axioms.log) |

The complete temporary axiom probe is retained in its log. `AIM.P114.counterexample_parallel_edges` uses exactly `[propext, Quot.sound]`. The other six public results use exactly `[propext, Classical.choice, Quot.sound]`. These are all permitted; there is no `sorryAx` or custom axiom.

The [hash manifest](../verification/referee-2-graph-hashes.json) includes the reviewed source and pinned dependency/toolchain inputs; the runner confirmed those hashes unchanged after every command. The [signature audit](../verification/referee-2-graph-source-audit.log) finds all seven proof statements identical to frozen Challenge after whitespace normalization. This is a source comparison, not an authoritative Comparator run. The proof imports only GraphDefinitions and no Challenge.

## Actual graph and connectivity

The unchanged definitions retain the actual full vertex set and the distinct edge identifiers of the manuscript's multigraph. The looplessness proof splits the pendant and module edges, then exhaustively considers the three possible module labels. Each case reduces to distinct distinguished endpoints or distinct summands of the vertex type. This is a uniform proof over all module indices, not a check of finitely many graph sizes.

The private `actualVertex` constructs the actual vertex-set subtype used by Mathlib's simple projection. `simple_adj_of_link` correctly supplies the proved looplessness instance before translating an actual multigraph link into simple adjacency. The connectivity proof explicitly constructs links `u-w_i`, `w_i-v`, and `u-t`, then turns each into a one-edge reachable path. For `v` it concatenates the two links through module zero, whose index existence is established from `m>=1`. It handles every element of the complete vertex sum type and anchors reachability at the actual `u` vertex. Consequently its use of the connectedness characterization establishes both reachability and nonemptiness.

Only connectivity uses the simple projection. Collapsing parallel adjacency pairs for this purpose does not affect reachability and does not alter any later multigraph count. The false disconnected case `m=0` is excluded from this theorem, as required.

## Actual cardinalities and parallel edges

The cardinality result reduces the actual universal vertex and edge sets to the finite sum, product, and option types. Their counts are `m+3` and `3m+1`, including every module label and the pendant. No count is taken on the simple projection.

The separate parallel-edge theorem proves that labels zero and one are unequal actual edge identifiers and both satisfy the link relation between the same `u,w_i` pair. It follows directly from the actual endpoint definition; there is no hypothesis asserting distinctness or parallelism. This explicitly checks the construction's most important multigraph feature.

## Incidence counts and degree restriction

The private `incident_count_sum` proves that the actual library `incidenceSet v` equals the set of edge identifiers for which `v` is either of the two chosen endpoints. It unfolds the existential incidence predicate and the symmetric endpoint relation, then converts finite-set cardinality to a sum of zero/one indicators. This avoids replacing the number of incident edges by the number of distinct neighboring vertices.

The public degree theorem splits the option sum into its pendant and module parts, the product sum into module and label coordinates, and the three label cases by the finite `Fin 3` enumeration. Exact normalization gives counts `2m+1,m,1,3` at `u,v,t,w_i`. Each parallel edge appears under its own identifier and contributes separately. Since looplessness was already proved, these counts are the intended multigraph degrees; the implementation makes no unsupported claim about this incidence convention for arbitrary graphs with loops.

The no-degree-two proof performs exhaustive case analysis over every actual vertex and substitutes those established counts. Arithmetic uses the source range `m>=3` in the distinguished cases; the module and pendant cases are exactly three and one. It does not overlook `v`, whose degree would be two at `m=2`, and it does not weaken the range to include that invalid graph index.

## Euler expression and degenerate indices

The final theorem substitutes the actual edge and vertex counts into integer arithmetic and normalizes the resulting polynomial equality. Its casting before subtraction preserves the correct value `-1` at `m=0`; no truncated natural subtraction is used. The theorem is explicitly the integer Euler expression, without an unproved identification as a cycle-space or homology dimension.

The other unrestricted structural results remain valid at zero: the graph has three distinguished vertices, one pendant, and an isolated `v`; its incident counts and looplessness are correct, while module-indexed statements are vacuous because there are no modules. Connectivity has its positive-module hypothesis, and full source admissibility is only asserted for `m>=3`. The proof preserves those distinctions.

## Quality, correspondence, and limits

The implementation uses the actual pinned graph link, incidence, looplessness, and connectivity APIs, and exact finite counting and arithmetic. Its finite label case analysis is appropriate because each module has exactly three declared edge labels, while the module count remains arbitrary. Helper declarations are private and focused. There is no new axiom, native computation, proof placeholder, or custom graph-property definition arranged to make the desired theorem true by definition. `GRAPH_PROOF.md` accurately explains the proof paths and limitations, with Sidney Holden's source attribution preserved.

These seven results establish the finite combinatorial construction faithfully. They do not assign the prime-root lengths to these actual edges, prove their rational independence, realize a compact metric graph, define its Kirchhoff operator, identify a homological cycle rank, build its vertex matrix, or connect it to the previously formalized core quadratic form and spectral law. Those remain documented gaps; the scalar length-sum and inertia theorems alone do not fill them.

**Blocking findings: none.** Combined-target integration and the authoritative Linux workflow remain separate gates. This approval and local success do not constitute an end-to-end Lean counterexample or a resolution of the separate universal variance assertion.
