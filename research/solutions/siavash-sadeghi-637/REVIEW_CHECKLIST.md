# Independent review checklist

The proposed proof depends on the following items; every one should be audited.

1. **Exact target.** Verify the factor of two in the logistic argument for
   `(x,-x)`, the `c=1/2` choice, ordered-pair sampling, fair signs, and `K*c<1`.
2. **Invariant probability.** Check the exponential Lyapunov bound, the Feller
   Cesaro argument, and uniqueness through an invariant synchronous coupling.
3. **Arithmetic engine.** Inspect outward rounding, signed multiplication and
   reciprocal handling, exponential range reduction/remainder, logarithm
   normalization/remainder, and the mathematical formula implemented for `R`.
4. **Global certificate.** Rerun every node. Verify the `|R''|<4000` estimate,
   interpolation error `M*Delta^2/8`, and the tail constant. No step should infer
   a global sign from the grid without these arguments.
5. **Stationary path estimate.** Check that `h` is square integrable, the
   martingale differences are centered and orthogonal, the telescope sign is
   correct, and the error in the summed drift is `o(n)` in probability.
6. **Covering.** Check the nonexpansion and the 18-Lipschitz bound on log
   derivative. Verify the diameter bound for an entire starting interval from
   one good point, the `2^n` word count, and stationarity in the mass estimate.
7. **Full-measure carrier.** Verify reverse Fatou, the union over compact
   starting intervals, the intersection over decreasing epsilon, and that the
   result bounds the dimension of a full-measure Borel set rather than merely
   a positive-measure subset.
8. **Additional conclusions.** Audit the maximal-atom argument and the separate
   full-support proof. Do not confuse support dimension with measure dimension.
9. **Scope and provenance.** Confirm the latest repository status and external
   submission records. Pin a commit before publication/submission. Do not call
   a second program independent mathematical review or call a numerical check
   a rigorous interval certificate.

No independent review is claimed by this document. It is a checklist for one.
