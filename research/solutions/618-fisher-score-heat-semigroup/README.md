# Heat-semigroup approximation of finite-Fisher-information scores

**Author:** Matthew J. Colbrook, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge CB3 0WA, United Kingdom. Email: [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk).

**Target:** Original AIM 618 at revision `aa776a01d7d48a79f93251af11fde9454b0aea95`; [pinned statement](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/618-fisher-score-gradient-closure.md) and [local snapshot](statement.md). This target is now [AIM 665](../../resolved/665-fisher-score-gradient-closure.md), rather than the unrelated current problem 618.

**Submission status:** Additional solution claim, awaiting pull-request review. The catalogue already records a different [closed-manifold extension proof](../618-fisher-score/PROOF.md), submitted in [PR #4](https://github.com/MColbrook/AIM/pull/4). This submission preserves that record and its status.

Read the [manuscript (PDF)](aim618_solution.pdf) or [standalone LaTeX source](aim618_solution.tex). The [pre-submission check](RESOLUTION_REPORT.md) compares the complete argument with the target; the [reference audit](REFERENCES.md) records source versions, theorem locators and author-information sources. These checks were performed by OpenAI Codex (AI); they are not independent human peer review or formal verification, and this package makes no priority claim.

The proposed smooth potentials are

```math
\varphi_\tau=P_\tau\log(P_\tau\rho+\tau),\qquad \tau\downarrow0,
```

where $`P_\tau`$ is the Neumann heat semigroup. The outer heat flow transfers estimates to the original density, while an exact mixed-product identity and lower semicontinuity give the required weighted convergence. The argument permits vacuum, unbounded densities, disconnected manifolds and smooth nonconvex boundaries. The constructed potentials satisfy a Neumann condition; no boundary condition is imposed on the input density.

[SUBMISSION.json](SUBMISSION.json) identifies the uploaded file and pinned target revisions. [The original upload](submission-original/aim618_solution.tex) is preserved byte for byte. [source-checks.json](source-checks.json) records citation and label checks; [document-checks.json](document-checks.json) records compilation and PDF inspection. [SHA256SUMS.txt](SHA256SUMS.txt) identifies the packaged files.

To reproduce the PDF with an existing LaTeX distribution, run twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim618_solution.tex
```

No external figures or bibliography files are required.
