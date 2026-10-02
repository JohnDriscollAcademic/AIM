# A periodic branch for the delayed noisy leaky integrate-and-fire equation

**Author:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom. Email: [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk).

**Target:** [AIM 353 at revision `fa98b7525fa3`](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/353-delayed-nnlif-periodic.md), with a [local statement snapshot](statement.md).

**Submission status:** Solution claim awaiting pull-request review. This package does not change the catalogue status.

Read the [manuscript (PDF)](aim353_delayed_nnlif_periodic.pdf) or [standalone LaTeX source](aim353_delayed_nnlif_periodic.tex). The [pre-submission check](RESOLUTION_REPORT.md) compares the argument with the complete target; the [reference audit](REFERENCES.md) records checked primary sources and additions to the uploaded bibliography. These checks were performed by OpenAI Codex (AI); independent human review and formal verification are not claimed.

The proof varies the physical voltage thresholds with the coupling. It establishes an existential claim with negative thresholds, without asserting a branch for prescribed thresholds or biological parameter values. Figure 1 shows the reset domain.

[SUBMISSION.json](SUBMISSION.json) records the input and pinned target. The [complete original notes](submission-original/aim_nonlinear_waves_research_notes.tex) are preserved byte for byte in this package; only the indicated proof is submitted here. The unrelated entropy example and eight unfinished targets are excluded from the manuscript.

[source-checks.json](source-checks.json), [document-checks.json](document-checks.json) and [SHA256SUMS.txt](SHA256SUMS.txt) record source validation, PDF production and file identities.

To reproduce the PDF with an existing LaTeX distribution, run twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim353_delayed_nnlif_periodic.tex
```

The figures are built into the source; no external images or bibliography files are required.

[numerical-checks.py](numerical-checks.py) and [numerical-checks.json](numerical-checks.json) provide reproducible response-function sanity checks. They do not certify the existence theorem.

To reproduce those optional checks, use Python with mpmath 1.3.0 and run `python numerical-checks.py` from this directory.
