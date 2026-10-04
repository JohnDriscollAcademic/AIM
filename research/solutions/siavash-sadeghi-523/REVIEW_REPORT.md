# AIM 523: target comparison and review

Contributor: **Siavash Sadeghi**. Reviewer: **Codex (AI)**. Date: 4 October 2026.

Target: [entry 523](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/523-nystrom-logarithmic-loss.md), commit `59a8f0c2957dd272f56bcf282dfe0c066a15f441`. Evidence: [paper](aim523_report.pdf), [source](aim523_report.tex), [target snapshot](TARGET_SNAPSHOT.md).

## Conclusion and limits

A fixed smooth amplitude on a smooth closed curve with a straight arc gives growth of order square root of log k. This addresses the arbitrary smooth amplitudes and general parametrizations allowed in the target; it does not assert a counterexample for every physical boundary-integral kernel.

Classification proposed for review: **Solution claimed; awaiting independent review**. This PR is a research submission, not an assertion of independent validation.

## Mathematical review

Reviewed the smooth periodic extension, the fixed amplitude and its uniform derivative bounds, the quadratic stationary-phase reduction and the second, degenerating angular phase. The scale k*A^2 tends to infinity uniformly for delta >= k^(-1/4); a uniform oscillatory-tail bound justifies the Fresnel limit. Integrating the 1/delta lower bound and summing a positive proportion of the Fourier modes gives the square-root logarithm.

## Changes and checks

Separated the relevant proof and bibliography from the supplied combined note; added the requested contributor name, explicit target definitions, pinned repository references and reproducibility documentation. The mathematical construction and intended scope are preserved.

This is an analytic proof with no numerical verifier supplied or needed. Checked the phase derivatives, frequency cutoffs, arc-length measure and s=0 target comparison; compiled and visually reviewed the paper.

The paper compiles in two passes with the existing MiKTeX installation. Every final PDF page was visually inspected. The built-in compiler failed because its platform directories were unavailable; this did not prevent the independently compiled PDF from being checked.

The original package, original scripts and original numerical outputs remain preserved outside this submission. No independent human or formal proof audit was performed.
