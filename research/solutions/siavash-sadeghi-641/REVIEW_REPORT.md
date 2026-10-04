# AIM 641: target comparison and review

Contributor: **Siavash Sadeghi**. Reviewer: **Codex (AI)**. Date: 4 October 2026.

Target: [entry 641](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/641-bos-simplex-interpolation-nodes.md), commit `59a8f0c2957dd272f56bcf282dfe0c066a15f441`. Evidence: [paper](aim641_report.pdf), [source](aim641_report.tex), [target snapshot](TARGET_SNAPSHOT.md).

## Conclusion and limits

This is a claimed proof of the cubic Fejer assertion only. The three quartic assertions grouped in entry 641 are outside the result, so this is a partial resolution of the catalogue entry.

Classification proposed for review: **Partial result: cubic claim awaiting independent review**. This PR is a research submission, not an assertion of independent validation.

## Mathematical review

Reviewed the prescribed cubic nodes, cardinal polynomials, stable degree-six sum-of-squares identity, full-orthant centroid substitution, the positive base cases and the induction in symbolic dimension. The printed 45-type table is now checked against the full symbolic polynomial certificate. The argument covers every integer M>=8, not just sampled dimensions.

## Changes and checks

Separated the relevant proof and bibliography from the supplied combined note; added the requested contributor name, explicit target definitions, pinned repository references and reproducibility documentation. The mathematical construction and intended scope are preserved.

The exact verifier and independent 3,432-monomial expansion pass in both normal and optimized Python. The printed table agrees in all 45 rows. Regression tests reject fractional coefficient damage, missing and duplicate records, shifted-array corruption and a changed printed row, including optimized execution. Replaced removable assert checks with explicit failures and removed the independent checker's truncating int conversion.

The paper compiles in two passes with the existing MiKTeX installation. Every final PDF page was visually inspected. The built-in compiler failed because its platform directories were unavailable; this did not prevent the independently compiled PDF from being checked.

The original package, original scripts and original numerical outputs remain preserved outside this submission. No independent human or formal proof audit was performed.
