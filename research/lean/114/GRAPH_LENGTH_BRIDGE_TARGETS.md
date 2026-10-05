# Actual graph length sums and core fraction

## Source and scope

Mathematical source: Sidney Holden, *A non-Gaussian limit for nodal surplus*,
v0.3, 2026-10-02, Section 1 equation (1) and Section 5's prescribed-length
estimate. Submitted PDF SHA256:
74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6.
This small block connects the independently reviewed graph, prescribed
length, and core-weight blocks. It changes no existing definition or
mathematical statement and introduces no abstract input lengths.

The actual edge type is `CounterexampleEdge m = Option (Fin m × Fin 3)`.
Each `some (i,j)` is one core edge; two parallel edges retain different
values of j. The unique `none` edge is the pendant. The already defined
assignment `counterexampleMetricLength m` maps a core edge to the actual
prime-root length at index 3*i+j and maps the pendant to `pendantLength m`.

## Three exact statements

`GraphLengthBridgeChallenge.lean` imports the existing unchanged
`AIM/P114/LengthDefinitions.lean` and gives the complete signatures:

1. `actual_graph_core_length_sum`: for every natural m, the sum of
   `counterexampleMetricLength m (some e)` over all `e : Fin m × Fin 3`
   equals `coreLength m`.
2. `actual_graph_total_length_sum`: for every natural m, the sum of the
   actual assigned lengths over all `e : CounterexampleEdge m` equals
   `coreLength m + pendantLength m`.
3. `actual_graph_core_length_ratio_bound`: for m≥3, the ratio of the actual
   core-edge sum in statement 1 to the actual total-edge sum in statement 2
   lies between zero and `3 / ((m : ℝ)^5 + 3)`, with both inequalities
   non-strict. The exact numerator and denominator appear explicitly twice
   in the statement, so no assumed sum identity or abstract fraction is
   hidden in a custom predicate.

The first two identities also hold for m=0, with an empty core sum and the
defined zero pendant length. The ratio statement uses precisely the source
range m≥3; positivity of all actual graph edge lengths has already been
proved on this range. No theorem assumes a sum identity or weight bound.

## Proof route and review gate

Reindex the finite product sum over `(i,j) : Fin m × Fin 3` using the exact
index 3*i+j. These are the consecutive indices 0 through 3*m-1, each once.
The proof may use the standard finite product-sum and consecutive-block
sum identities, or prove the block identity by induction. This is an exact
finite equality, preserving multiplicities of parallel edges.

The sum over `Option (Fin m × Fin 3)` splits into the pendant contribution
and the core contribution. Substitute the first equality to obtain the
second. Substituting both identities into the ratio and unfolding the
existing `coreWeight` definition reduces the third statement to the already
proved `core_weight_bound` (whose m≥1 hypothesis follows from m≥3).

Pinned Mathlib is 0df444a360eaa60ab8c11dca51a86af692955474. Expected library
dependencies are finite-type product/option summation and sums over finite
intervals. The existing local dependency for the final inequality is
`AIM/P114/TransferProof.lean`. No new measure or graph abstraction is needed.

Two independent statement approvals and boundary typechecking precede any
proof implementation. The candidate's deliberate placeholders certify no
mathematical result. Existing graph/length/transfer mathematical files stay
unchanged. After these three identities and bound, this extension's scope
is fixed for final integration and isolated Linux verification.

This block still does not identify the graph's spectral law with a phase
or module distribution, formalize the Kirchhoff Laplacian, prove the stable
response-ratio law, or prove the process/random-index limit. Those larger
connections remain outside the proved package.
