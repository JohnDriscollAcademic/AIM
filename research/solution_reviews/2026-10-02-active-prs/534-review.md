# AIM 534: verbose-persistence pullback triangle inequality

Date: 2026-10-02. Reviewer: OpenAI Codex (AI), fresh mathematical and computational audit. This is not human peer review, proof-assistant verification, or certification of novelty.

**Decision:** accept the counterexample and mark [AIM 534](../../../problems/534-verbose-persistence-pullback-triangle.md) **Solved**. The submission disproves the universal statement in degree one over every field, and also proves its stated extension to every positive degree.

**Submission:** [PR #21](https://github.com/MColbrook/AIM/pull/21), head `5f6ade2be66c50663ed57371771c139d9222cde4`, original AIM 544. Reviewed the entire [manuscript](../../solutions/siavash-sadeghi-544/aim544_counterexample.tex), exact witness and all three verification programs against the current target at base `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.

## Proof audit

The definitions match: distinct vertices at zero pseudodistance are retained; every zero-length persistence pair is kept; the matching uses no auxiliary diagonal points; and the infimum is over all finite common sets with surjections. An upper bound on one witness alone would not suffice for the claimed positive distance. The manuscript supplies the required lower bound for every common pullback.

At levels 0, 1 and 2 the complexes are disjoint unions of simplices. The rank of the degree-(k+1) boundary on r vertices is `binom(r-1,k+1)` over every field. Boundaries of simplices containing one fixed vertex are independent by their opposite faces and span by the cone identity. Positive-degree homology vanishes at each filtration level, so the rank increments count the diagonal bars exactly.

For degree one, X has clusters of sizes 3 and 1 at level 1, Y has sizes 2 and 2, and Z has all distinct distances 2. Their native barcodes are respectively `{(1,1),(2,2),(2,2)}` and, for both Y and Z, three copies of `(2,2)`. Duplicating the isolated vertex of X and a vertex of Y gives the same five-vertex barcode, hence `D_1(X,Y)=D_1(Y,Z)=0`.

For arbitrary positive fiber sizes a,b,c over X's three-point cluster, the number of `(1,1)` bars is `ab+ac+bc-2 >= 1`. Every Z pullback has endpoints only at 0 or 2. Thus every matching costs at least 1, while the native matching costs 1. This establishes `D_1(X,Z)=1` without restricting the size of the common set.

The positive-degree extension has k+3 vertices, cluster sizes k+2 and 1 for X, k+1 and 2 for Y, and equilateral Z. The identical duplication witness works. The lower-bound multiplicity is

```
binom(sum(m_i)-1,k+1) - sum_i binom(m_i-1,k+1) >= 1.
```

Its subset-counting proof is valid: disjoint blocks of sizes `m_i-1` and a further block of size k+1 fill a set of size `sum(m_i)-1`; the further block is a subset not removed by the subtracted counts. This is uniform in all multiplicities and fields.

I also checked the ancillary minimality claim. A diameter-realizing edge in a (k+1)-simplex produces a newly born k-cycle at the diameter. The full simplex kills it at that same value. Consequently every pullback with at least k+2 vertices has a diameter bar. At equal cardinality k+2, this proves that the distance equals the absolute difference of diameters; at smaller equal cardinality the native barcodes are empty. Thus k+3 is indeed the smallest equal cardinality for failure. The correspondence restriction, scaling, and nontransitive zero-distance conclusions follow as stated.

## Fresh reproduction

Executed unmodified scripts from a byte-exact export of the pinned PR, with Python's bytecode writing disabled:

```
python -B verify_boundary.py --output 534-boundary-results.json
python -B verify_ranks.py --output 534-rank-results.json
python -B verify_supplementary.py --output 534-supplementary-results.json
```

All passed: 6,653 checks with 720 exact persistence reductions and 5,226 pullback-pair comparisons; 3,650 checks with 356 independent boundary ranks and 3,267 finite inequality instances; and 246 supplementary checks. Fresh outputs: [boundary](534-boundary-results.json), [ranks](534-rank-results.json), [supplementary](534-supplementary-results.json). The second implementation does not import the first. The supplementary checks do reuse it and are not represented as a third independent implementation. These finite computations support the proof; they do not establish its unrestricted quantifiers.

## Reference check

Checked the [primary author version, arXiv:2208.11770v8](https://arxiv.org/pdf/2208.11770v8), especially Remark 1.1, Definition 5.3 and Example 5.10. The source explicitly distinguishes the fixed-positive-degree open question from the already failing all-degrees interleaving construction. The submission acknowledges the source's X and Y example; its equilateral Z has distance 2, whereas the source figure's Z has distance 1. This is a valid new triple for the specified question, without implying a priority claim. The ordinary bottleneck metric and the degree-zero result are unaffected.
