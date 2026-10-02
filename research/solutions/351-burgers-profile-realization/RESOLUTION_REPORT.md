# Pre-submission check: AIM 351

Checked on 2 October 2026 by OpenAI Codex (AI). This is an editorial and mathematical check of the submitted argument, not independent human review or formal verification. The claim awaits pull-request review.

## Target comparison

The [pinned statement](statement.md) asks for one bounded Burgers datum, with values in a prescribed interval, realizing the profile of any prescribed Borel probability measure on that interval along translated late-time observations. Theorem 1.1 supplies the full requested quantifiers, with observation times exactly the positive integers. No finite-support, tail, monotonicity or recurrence hypothesis is added. The universal-datum corollary strengthens this same target.

## Argument checked

1. Compact support permits differentiation of the positive heat history at all real times. Its logarithmic derivative solves the Burgers equation and remains a weighted average in the prescribed value interval.
2. For any bounded measurable initial datum, its normalized Cole--Hopf datum grows at most exponentially. Gaussian convolution and differentiation are therefore valid. Integration by parts gives a positive weighted average of the initial datum, preserving its bounds. Approximate identities give the initial trace. Bounded well-posedness identifies this explicit solution with the target's solution.
3. Agreement on a centered interval implies exact agreement of the normalized Cole--Hopf data there. The exterior contribution and its first spatial derivative have uniformly vanishing Gaussian tails at each fixed positive time and on each compact observation interval. The explicit denominator lower bound is independent of all exterior values. Thus the locality estimate is uniform over the eventual infinite patching.
4. Convolution of the backward heat history at time minus k with the time-k Gaussian gives the time-zero history, by Tonelli and the exponential Gaussian identity. Hence each ideal patch evolves to exactly the prescribed profile.
5. Radii are chosen separately after each observation time. Disjoint windows can then be placed recursively with positive gaps. Their countable union defines one measurable bounded datum. Translation invariance follows from the Cole--Hopf formula; the normalization changes only by a cancelling positive scalar. Locality applies despite infinite heat-propagation speed.
6. For the universal corollary, a countable dense family repeated in successive finite blocks has every probability measure as a subsequential limit at unbounded indices. Weak convergence gives compact-uniform convergence of the numerator and denominator, by equicontinuity and a uniform positive denominator bound. A subsequence then realizes each requested profile.

No mathematical obstruction was found in this check. The result concerns the repository's literal bounded-datum formulation with unrestricted spatial shifts. It does not assert fixed-origin recurrence, prescribed tails or restrictions on the speed of observation shifts.

## Editorial and reference changes

The submitted Section 1 was separated from the combined notes, with its universal corollary retained. A title, author block, PDF metadata and patching diagram were added. Bibliography links identify the exact target revision. Hopf's and Cole's original transformation papers were added and cited; Gallay--Scheel's journal metadata and conjecture locator were verified. The proof mechanism was retained.

The original combined notes are preserved byte for byte. Their entropy example and unfinished targets are not claims in this submission. See [REFERENCES.md](REFERENCES.md), [source-checks.json](source-checks.json) and [document-checks.json](document-checks.json) for supporting checks. No catalogue status change is proposed in this submission.
