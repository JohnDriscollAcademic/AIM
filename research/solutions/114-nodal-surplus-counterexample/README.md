# AIM 114: a non-Gaussian nodal-surplus limit

**Mathematical author:** Sidney Holden.

The [submitted manuscript](submitted/short_proof-v0.3.pdf), *A non-Gaussian limit for nodal surplus*, revised v0.3 (2026-10-02), constructs a sequence of loop-free Kirchhoff metric graphs whose standardized spectral-frequency surplus laws tend to a nonconstant Gaussian variance mixture. The [expanded proof](PROOF.md) presents its argument in repository Markdown.

This addresses the Gaussian assertion in [AIM 114](../../../problems/114-quantum-graph-nodal-clt.md). The separate universal linear-variance assertion remains open. The construction itself has variance asymptotic to a positive constant times cycle rank. The original ID, path, problem statement, and both subquestions are preserved.

## Evidence and limitations

- [Unchanged source PDF](submitted/short_proof-v0.3.pdf): the mathematical submission; its author was identified by the submitter as Sidney Holden on 2026-10-05.
- [Frozen original target](statement.md): byte-for-byte copy from AIM commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.
- [Expanded mathematical argument](PROOF.md): prepared by OpenAI Codex, retaining the original sequence and limit law.
- The [spectral review](reviews/spectral-review.md) and [probability review](reviews/probability-review.md), performed by two independent OpenAI Codex AI agents on 2026-10-05, found no blocking defect in their combined coverage of the complete argument. Their reports identify the source bytes and checks. They are not human peer review or proof-assistant verification.
- [Exact finite checks](check_algebra.py) and [recorded output](algebra-checks.log): check sign averaging, the response identities, and the sign-count/inertia reduction on explicit rational phase data. They do not establish infinite-dimensional spectral results, null-set assertions, distributional convergence, or non-Gaussianity.

The [Lean package](../../lean/114/README.md) contains 31 supporting results: the actual finite multigraph, its admissibility counts, and positive jointly rationally independent prescribed lengths; local sign algebra and core quadratic-form inertia; the actual Cauchy-defined variance function with strict bounds, continuity, and intrinsic nonconstancy; an actual normalized Gaussian-mixture law with proved moments and non-Gaussianity; and the actual graph length sums, prescribed prime-root weight, and actual second/fourth-moment contamination error tending to zero. Its [verification record](../../lean/114/verification/README.md) and [gap list](../../lean/114/NUMERICAL_TARGETS.md) distinguish historical from expanded checks. The stable ratio law, its support/zero-atom properties, the spectral-to-phase bridge, and the graph/process limit remain unformalized. No whole-problem Lean-verified catalogue status is claimed.

## Reproduce the finite checks

No third-party packages are needed. From the repository root:

```sh
python3 research/solutions/114-nodal-surplus-counterexample/check_algebra.py
python3 -O research/solutions/114-nodal-surplus-counterexample/check_algebra.py
```

All acceptance checks use exact rational arithmetic and explicit exceptions; Python's optimization flag does not remove them. The tests enumerate 504 sign-average cases, 448 nonexceptional graph instances with 3, 4, 7, or 12 modules, and 24 response cases. The graph checks compute inertia using independent symmetric elimination, not the manuscript's preassigned pivot signs. Deterministic sampling and skipped exceptional cases are visible in the source.

## Source correspondence

| Manuscript part | Mathematical role | Verification evidence |
| --- | --- | --- |
| Section 1 | Admissible graph family, independent lengths, precise limiting law | Frozen target, mathematical reviews |
| Section 2, equations (6)–(10) | Published spectral-measure input and exact surplus reduction | Source checks, spectral review, finite algebra checks |
| Section 3, equations (11)–(15) | Variance profile and stable boundary vector | Probability review, finite sign/response checks |
| Section 4, equations (16)–(20) | Functional convergence, joint independence, uniform moments | Probability review |
| Section 5 | Transfer to actual lengths, standardization, non-Gaussianity | Probability review |

The construction permits increasing degrees and a dominant pendant length. It makes no claim for bounded-degree or comparable-length variants. Spectral frequency is sent to infinity before graph size.

## Provenance

The submission's SHA-256 is `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`; the original target's SHA-256 is `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f`. Source authorship is separate from the AI preparation, review, and formalization work. The spectral results are credited to Lior Alon, Ram Band, and Gregory Berkolaiko, and the empirical-process reference to Jean-François Marckert. No endorsement by those authors is implied.
