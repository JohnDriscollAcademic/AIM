# Independent statement review 1: actual prescribed lengths

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of author and intended implementer `lean_feasibility`.
- Phase: preproof boundary review.
- Verdict: **APPROVE** the three statements at the following exact hashes. No LengthProof existed at review time.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `LengthChallenge.lean` | `0ee1d8866b88d3e389209a16d21ff51291fcfce759bbdff15cbc4c18ce774809` |
| `LENGTH_TARGETS.md` | `765439e1e49999c292a0c30a37ee1a1925e8b808770dcde9f30000bd835ee3dd` |

I read every candidate byte, the imported exact graph and length definitions, the manuscript's length assignment, and the relevant Mathlib linear-independence and infinite-Galois APIs. I independently ran `lake env lean LengthChallenge.lean`: exit zero, exactly three intentional Challenge placeholders, [log retained](../verification/referee-1-length-boundary.log). This checks signature formation, not proofs. The source remains Sidney Holden's unchanged v0.3 PDF, SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`.

The new definition attaches the exact prescribed lengths to the actual multigraph's edge IDs. The two parallel edges receive different consecutive prime roots, rather than being collapsed. For i in Fin m and j in Fin 3, the core index 3i+j ranges uniquely over 0,...,3m-1. The pendant uses index 3m, outside that core range, with multiplier m^6. Zero-based prime indexing agrees with the source's first through (3m+1)st primes. No length parameter or independence assumption is introduced.

The first conclusion is full `LinearIndependent` over the scalar field Q for the entire sequence of actual real prime roots; it controls every finitely supported rational relation. It is a correct stronger conclusion than the needed finite-family result. It cannot be discharged by proving individual irrationality or merely pairwise irrational ratios. The other two conclusions give strict positivity and joint independence for every actual edge at every source index m>=3. This hypothesis ensures that the rational pendant multiplier is nonzero. There is no inadmissible claim at m=0, where the pendant formula vanishes.

The proposed route is mathematically valid: each quadratic root defines a sign-valued character of the rational automorphism group of an algebraic closure; distinct prime square classes give distinct characters; Dedekind independence then annihilates all coefficients in a rational relation after applying every automorphism. The distinct-character step uses the infinite-Galois fixed-field theorem and the nonsquare product of two distinct primes. It does not assume independent sign-flip automorphisms, which would merely hide the difficult independence claim. Constructing all these objects, proving character multiplicativity, and transporting actual real roots are implementation obligations, not supplied hypotheses.

Restriction to distinct actual edge indices and nonzero rational rescaling of the pendant preserve independence. The exact indexing injection and equality with `counterexampleMetricLength` must appear in the proof. Positive lengths plus the already proved finite combinatorics do not themselves define a compact metric realization, Kirchhoff operator, or spectral-frequency law. The source's spectral and probabilistic convergence links remain outside this boundary.

No changes requested. Obtain both independent approvals before implementation, then perform independent final proof and axiom reviews and fresh isolated Linux verification for the expanded scope.
