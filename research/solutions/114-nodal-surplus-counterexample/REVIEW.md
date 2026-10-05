# Combined review record for AIM 114

**Date:** 2026-10-05. **Outcome:** the complete informal counterexample passes the combined independent AI audit, with no blocking mathematical correction requested. The universal Gaussian assertion is disproved; the separate universal linear-variance assertion remains unresolved.

The mathematical source is Sidney Holden's unchanged [v0.3 manuscript](submitted/short_proof-v0.3.pdf), dated 2026-10-02. Two independent OpenAI Codex AI subagents reviewed it and the [expanded presentation](PROOF.md):

| Reviewer | Principal responsibility | Report |
| --- | --- | --- |
| `spectral_review` | Graph admissibility, reference hypotheses, secular projection, nodal count and inertia, genericity and exceptional sets; consistency of the continuation | [Spectral review](reviews/spectral-review.md) |
| `probability_review` | Cauchy response, stable law, functional convergence, limiting independence, random evaluation, uniform integrability, moment transfer, non-Gaussianity | [Probability review](reviews/probability-review.md) |

Both reports preserve source hashes and state what was actually checked. Neither reviewer authored the mathematical manuscript or implemented the accompanying Lean proofs. Root Codex prepared the repository presentation and exact finite checks, read both reports, and reconciled their shared conclusion with the original two-part target. No external human review, source-author endorsement of the AI implementation, or reproof of the reference papers is claimed.

The independent reviews address several potential failure points explicitly: equality of the two pendant completions' surplus without assuming their conditional weights; nontriviality of every exceptional equation; absence of a hidden stable-law centering term; dependence within each actual module; the atom at an infinite threshold; random evaluation in a local process topology; and stronger moment estimates beyond total variation. The fourth-moment result supplements an explicit proof of a non-Gaussian weak limit.

[Exact rational regression checks](check_algebra.py) passed in Python 3.9.6 both normally and with `-O`, including independent inertia controls. The [recorded output](algebra-checks.log) is deterministic. These finite checks validate implementations of selected identities, not the limit theorem.

The repository's catalogue validation passed on a clean copy of the candidate files. A clean copy avoids an existing catalogue scanner issue that traverses ignored local `.lake` dependency Markdown. The generator and its validation rules were not modified. Direct comparison confirms that the original **Problem statement** section is unchanged; the ID and canonical path remain 114 and `problems/114-quantum-graph-nodal-clt.md`.

## Formalization distinction

The complete counterexample is **not Lean verified**. The initial Lean project treated three supporting results. Its extensions now prove an actual normalized Gaussian-mixture law's moments and non-Gaussianity for bounded nonconstant mixing variance, and the actual prescribed-length moment-contamination error tending to zero. These have separate statement and proof reviews; the mathematical audits above concern the complete informal argument. The remaining formal gaps include graph spectral theory, the stable law and process limit, and the source-specific mixing variable's hypotheses. None is treated as a Lean axiom. Mechanical acceptance of the supporting blocks would not justify promoting the whole counterexample or catalogue entry to Lean verified.
