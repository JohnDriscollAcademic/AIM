# AIM 523: research submission

Author/submitting contributor: **Siavash Sadeghi**. Reviewed 4 October 2026.

**Solution claimed; awaiting independent review.** A fixed smooth amplitude on a smooth closed curve with a straight arc gives growth of order square root of log k. This addresses the arbitrary smooth amplitudes and general parametrizations allowed in the target; it does not assert a counterexample for every physical boundary-integral kernel.

Read the [paper](aim523_report.pdf) or its [editable source](aim523_report.tex), the [target comparison and review](REVIEW_REPORT.md), and the [dated submission audit](TARGET_AUDIT.md).

The target is [entry 523 at repository commit `59a8f0c2957dd272f56bcf282dfe0c066a15f441`](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/523-nystrom-logarithmic-loss.md); a verbatim [snapshot](TARGET_SNAPSHOT.md) is included for reproducibility.

## Reproduce

This package contains an analytic proof, with no computational certificate. Its review record explains the checks performed.



Compile the paper twice using `pdflatex aim523_report.tex`. See [reproduction details](REPRODUCTION_RECORD.md). Numerical tests and catalogue checks do not certify the mathematical proof.

## Submission process and provenance

The repository's [contribution instructions](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/CONTRIBUTING.md) accept resolution reports through issues or pull requests. This package supplies the target ID and commit, linked proof, target comparison, named contributor and disclosed review. Submit it as one PR adding only `research/solutions/siavash-sadeghi-523/`. Catalogue classification is left for maintainer review.

The supplied research note was AI-assisted and identified ChatGPT in its metadata. Codex separated and polished this argument and reviewed the proof and checks. No independent human audit, publication acceptance or Lean/formal verification is claimed. Source archive SHA-256: `dede24dd58ee1d818d520cf5736ad398b97ff2a8683b87b00b61cccfc7f626a7`.
