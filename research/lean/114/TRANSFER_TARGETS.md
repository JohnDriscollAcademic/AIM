# Exact boundary: prescribed-length moment transfer

This extension formalizes the final contamination step of Sidney Holden's
v0.3 manuscript, Section 5, using the same frozen source PDF, full problem
statement, and expanded proof as `NUMERICAL_TARGETS.md`.

The five advertised declarations are in `TransferChallenge.lean`; the concrete
objects are in `AIM/P114/TransferDefinitions.lean`. Prime indexing starts at
zero in Lean, so the core uses indices `0,...,3m-1` and the pendant uses `3m`.
The lengths are exactly the source's square roots and pendant multiplier
`m^6`. The theorem holds for all natural `m >= 1`, which includes the source's
admissible graph range `m >= 3`. No assertion about a graph at `m=0,1,2` is made.

1. `core_weight_bound` proves nonnegativity and the explicit bound
   `omega_m <= 3/(m^5+3)` for the actual finite prime-root sums.
2. `contaminated_law_probability` proves the actual weighted sum of measures
   is a probability measure when `0 <= w <= 1`, including both endpoints.
3. `contamination_integral_bound` proves the error bound `w*B` for a measurable
   function lying in `[0,B]` almost everywhere under both probability measures.
   Integrability follows from these bounds, and is not an extra conclusion
   assumed as a hypothesis. This is the sharp interval-width form used by
   the source's nonnegative even-moment integrands.
4. `surplus_moment_contamination_bound` applies that result to the actual
   centered and scaled integrals, with the prime-root `omega_m`, for `k=1,2`
   (moments 2 and 4). The two source laws must have support in `[0,2m-1]`.
   The proved bound `3/(m^5+3) * m^k` slightly relaxes the source's displayed
   bound by using `((2m-1)/(2 sqrt m))^(2k) <= m^k`.
5. `surplus_moment_contamination_tendsto` proves the actual difference of
   those integrals tends to zero for arbitrary sequences of such laws.
   Support assumptions apply only for `m>=1`; all measures, including the
   irrelevant zeroth ones, are probability measures. No convergence of the
   uncontaminated law or its moments is assumed or claimed.

This closes the prescribed-length moment-error calculation conditionally on
the published spectral mixture representation and surplus-support theorem.
Those spectral statements remain unformalized; they are explicit hypotheses
of the application, not axioms in Lean. This file does not prove rational
independence of the lengths, graph admissibility, weak convergence, the
pendant law's limiting moments, or the full counterexample.

Before proofs, two independent referees must approve the exact definitions,
challenge signatures, and this scope document. The five theorem names must
be added to the combined Comparator boundary only after approval.
