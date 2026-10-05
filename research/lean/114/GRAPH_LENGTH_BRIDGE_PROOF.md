# Proof connecting actual graph lengths and the core weight

`AIM/P114/GraphLengthBridgeProof.lean` proves the three exact signatures
reviewed in `GraphLengthBridgeChallenge.lean`. The imported length/graph
definitions, candidate signatures, and target document are unchanged.

For the core sum, `Fintype.sum_equiv finProdFinEquiv` reindexes the actual
edge pairs `(i,j) : Fin m × Fin 3` by `j+3*i : Fin (m*3)`. The proof checks
that this is the same natural index as the assignment's `3*i+j`.
`Fin.sum_univ_eq_sum_range` then gives precisely the defining sum for
`coreLength m`, using commutativity to identify m*3 and 3*m. The equivalence
is bijective, so every core edge occurs exactly once, including both
parallel edges in each module. No assertion about a set of distinct endpoint
pairs is substituted for the actual edge sum.

For the total sum, `Fintype.sum_option` splits the actual edge type into
the unique pendant `none` and all the core entries `some e`. Substitution
of the core identity and the pendant length definition gives exactly
`coreLength m + pendantLength m`. Both identities hold for every natural m.

For m≥3, rewriting both actual sums in the stated ratio reduces the bound
to `core_weight_bound m`, whose m≥1 hypothesis follows by arithmetic. Thus
the proved bound applies to the actual graph length fraction. It is not
an assumed relation between an abstract length parameter and a graph.

Local build, fresh re-elaboration and axiom evidence are retained in
`verification/graph-length-bridge-{build,reelaboration,axioms}.log`, with
the audit source and source SHA256 manifest beside them. Two independent
final proof audits and integrated isolated Linux verification are separate
gates. No further extension is included in this block.

These results connect the concrete graph and prescribed lengths to the
existing scalar core-weight estimate. They do not identify the quantum
graph's spectral law with a module law or prove the stable/process limits;
those remaining gaps continue to limit the package to a partial
formalization of the full counterexample.
