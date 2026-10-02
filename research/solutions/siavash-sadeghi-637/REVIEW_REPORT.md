# Review report

**Submitter:** Siavash Sadeghi. **Reviewer:** Codex (AI). **Date:** 2 October 2026.

The supplied AI-assisted proof, both programs and all package documentation were
read. The review found no mathematical defect requiring a change to the proposed
argument. This is a submission review, not a documented independent human audit.

## Proof review

1. **Target match.** Checked the `2x` rating difference, `c=1/2`, fair signs under
   both ordered pairs, and `K*c=9/20<1` against the repository and source paper.
2. **Invariant law.** Checked the exponential drift with contraction
   `491/728<3/4`, the Feller/Cesaro existence argument and the stationary
   synchronous-coupling uniqueness argument. The finite exponential moment
   makes the auxiliary function square integrable.
3. **Arithmetic.** Inspected signed floor/ceiling rounding, multiplication,
   reciprocals, crossing-zero squares, exponential range reduction and Taylor
   remainder, logarithm normalization and atanh remainder. The implemented
   residual matches the paper's `g+7/10-h+Ph`.
4. **Global bound.** Reproduced all grid nodes. Checked the curvature constant
   `18956/5<4000`, interpolation error `1/2000`, evenness and the analytic tail
   lower bound `2555547/500000` for `h-Ph`. These steps, not grid sampling alone,
   justify the global drift inequality.
5. **Stationary paths.** Checked the telescope sign, centered orthogonal
   martingale differences and the second-moment estimate giving an error of
   order `o(n)` in probability.
6. **Covering.** Checked nonexpansion, the Lipschitz constant 18 for the log
   derivative, distortion across each starting interval and the `2^n` word count.
7. **Full measure.** Checked the stationarity mass bound and reverse-Fatou
   limsup argument, union over compact starting sets and intersection as epsilon
   decreases. The bound concerns a full-measure Borel carrier, not only a
   positive-mass subset or the topological support.
8. **Other properties.** Checked the maximal-atom contradiction and the
   independent full-support argument. The zero-sum embedding is bi-Lipschitz.
9. **Scope.** Pinned the actual repository revision, checked submission records
   and primary sources, and retained the claimed-result classification.

## Changes made

- Added Siavash Sadeghi to the proof, package and resolution metadata.
- Pinned the target and contribution rules; replaced stale access and submission
  statements with this dated audit and an explicit submission route.
- Made the numerical checker reject incomplete or malformed exact-result records
  before computing, including missing sample enclosures. Its completeness checks
  do not authenticate a result file; rerunning the exact verifier is essential.
- Added focused rational-arithmetic, parameter-consistency, malformed-input and
  partial-run regression tests. Mathematical coefficients and the exact verifier
  are unchanged. Numerical results remain equal to the supplied results.
- Rebuilt and visually checked the proof PDF; refreshed reproduction records
  and checksums. Removed unrelated submission history from the supplied audit.

## Limits

The full proof remains a computer-assisted claim awaiting independent review.
Successful programs and this AI review do not replace an independent audit of
the probability and dimension arguments, the interval implementation or its
mathematical remainder bounds. No formal proof assistant was used.
