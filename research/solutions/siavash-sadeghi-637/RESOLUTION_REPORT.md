# Resolution report: AIM 637

**Submitted by:** Siavash Sadeghi. **Date:** 2 October 2026.
**Target:** [Absolute continuity of stationary Elo ratings](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/637-elo-density.md).
**Repository commit:** `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.
**Evidence classification:** Solution claimed; independent review pending.

## Counterexample and target match

The [proof](aim637_counterexample.pdf), Theorem 1.1, proposes a negative answer
to the universal binary-score density assertion. Its [editable source](aim637_counterexample.tex)
uses `N=2`, `rho=(0,0)`, `c=1/2`, and `K=9/10`, so `K*c=9/20<1`.
Under the original ordered-pair update rule, `(x,-x)` has first-coordinate maps
`x-(9/10)tanh(x) +/- 9/10`, each with probability one half.
The unique invariant law is singular continuous with full support and a
full-measure Borel carrier of Hausdorff dimension at most `10*log(2)/7<1`.
The linear embedding into the zero-sum line transfers this singularity to the
precise target. No truncation, linearization, rounding or extra score noise is used.

The Partial badge records known existence, uniqueness, support and moment
properties. These are credited to Cortez and Tossounian; the contribution claimed
here is the certified singular example and dimension bound. This does not
classify other parameters, the small-step regime, or every larger player count.

## Evidence and review

The exact verifier certifies 5,001 grid inequalities and 14 analytic constants
using 192-bit outward-rounded integer intervals. Curvature, interpolation and
tail bounds extend the inequality to the whole real line. The paper supplies
the martingale and covering arguments needed for singularity.
The separate 80-digit Decimal implementation supplies 20,024 numerical checks;
these are supplementary approximations, not interval proofs.

Codex reviewed all nine items in [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md),
inspected both implementations, reran the checks, and added regression coverage.
The supplied work was AI assisted. This submission has no documented independent
human audit and no proof-assistant verification. The [review report](REVIEW_REPORT.md)
and [reproduction record](REPRODUCTION_RECORD.md) identify what was checked.

## Submission route

[CONTRIBUTING.md](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/CONTRIBUTING.md) accepts resolution reports as PRs and
requires the target ID, repository commit, proof link, full-target comparison,
and review provenance. This report supplies those items. The requested PR adds
this package to `research/solutions/siavash-sadeghi-637/` for maintainer review.
It does not claim a Solved or Lean verified classification or change catalogue
metadata. Any accepted status transition must follow the repository's coordinated
archive and catalogue process.

The [dated audit](TARGET_AUDIT.md) found no matching prior submission in the
public records checked. Its coverage and access limits are stated explicitly.
