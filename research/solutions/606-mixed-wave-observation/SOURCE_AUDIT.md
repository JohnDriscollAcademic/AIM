# Source and target audit for problem 606

**Review date:** 2026-10-02. **Reviewer:** OpenAI Codex and its research agents, all AI.

## Pinned target

The target is problem 606 at `37a25361f243be77daea0ae0b3c5167b57f1b5f3`: [permanent source link](https://github.com/MColbrook/AIM/blob/37a25361f243be77daea0ae0b3c5167b57f1b5f3/problems/606-mixed-wave-optimal-observation-time.md). The [local statement](statement.md) preserves its bytes. This ID must be accompanied by the commit because the catalogue renumbers active entries after archival.

The problem asks for an infimum. Proving observability at every time above two and failure at every positive time below two resolves it without deciding the endpoint. The proof retains the specified observation, nonnegative potential, pointwise sampling, and all mesh sizes.

## Published mathematical inputs

The primary source is C. Castro and S. Micu, [A mixed finite elements approximation of inverse source problems for the wave equation with variable coefficients using observability](https://doi.org/10.1007/s00211-025-01489-0), *Numerische Mathematik* 157 (2025), 1847–1895. The [published full text](https://link.springer.com/article/10.1007/s00211-025-01489-0) and [arXiv version 1](https://arxiv.org/html/2501.11352v1) were inspected.

The exact dependencies are Lemma 4, Lemma 5 and equation (31), Theorem 9, and the single-mode boundary estimate (48). Section 2 of [the proof](PROOF.md) restates them in a consistent normalization. The source's continuity requirement belongs to its separate convergence results; the spectral estimates used here require bounded nonnegative sampled values. The pointwise supremum bounds those values even when the chosen representative differs on a null set.

The source leaves the optimal-time question open after Theorem 1 and in Remark 15. Its existing large-time observability theorem alone does not identify the infimum. The added argument is the uniform asymptotic frequency-gap estimate, its application with finite frequency insertion, and the discrete construction below the threshold.

The Fourier estimates are proved in the note, with attribution to classical work: A. E. Ingham, [Some trigonometrical inequalities with applications to the theory of series](https://doi.org/10.1007/BF01180426), *Mathematische Zeitschrift* 41 (1936), 367–379. Related quantitative finite-frequency insertion results are in S. Jaffard and S. Micu, [Estimates of the constants in generalized Ingham's inequality and applications to the control of the wave equation](https://www.math.ucv.ro/~micu/auxiliare/work_ro/doc/papers/jaffard-micu.pdf), *Asymptotic Analysis* 28 (2001), 181–214. The present note does not claim a new general Ingham inequality.

## Bounded later-result search

On 2 October 2026 we checked the journal and arXiv records and searched combinations of the exact paper title, `2501.11352`, `Castro Micu optimal time`, `mixed finite elements variable potential observability`, and `mixed finite elements asymptotic gap`. These searches did not locate a later resolution of the exact target. This is a bounded search, not a guarantee of novelty or priority.

The search also found A. O. Ozer's announced manuscript *Sharp Uniform Boundary Observability For An Averaged Finite-Difference Approximation Of The Wave Equation On An Annulus*, listed as submitted on the [author's publication page](https://sites.google.com/view/aozkanozer/publications). Its full text was not available through the sources inspected. We therefore do not assert that its methods are distinct, or that no related unpublished result exists. The present claim rests on the displayed proof and exact target comparison, not on an exhaustive priority claim.

## Review limits

All research and checking in this package was performed by AI in one preparation session. Separate agents checked the argument and source applications, but this is not human peer review or formal verification. The numerical results are diagnostics only. No claim is made that checking links, rendering equations, or passing finite numerical examples proves the mathematical statement.
