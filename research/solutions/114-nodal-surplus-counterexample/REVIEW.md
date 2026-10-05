# Combined review record for AIM 114

**Date:** 2026-10-05. **Outcome:** the complete informal counterexample passes the combined independent AI audit, with no blocking mathematical correction requested. The universal Gaussian assertion is disproved; the separate universal linear-variance assertion remains unresolved.

The mathematical source is Sidney Holden's unchanged [v0.3 manuscript](submitted/short_proof-v0.3.pdf), dated 2026-10-02. Two independent OpenAI Codex AI subagents reviewed it and the [expanded presentation](PROOF.md):

| Reviewer | Principal responsibility | Report |
| --- | --- | --- |
| `spectral_review` | Graph admissibility, reference hypotheses, secular projection, nodal count and inertia, genericity and exceptional sets; consistency of the continuation | [Spectral review](reviews/spectral-review.md) |
| `probability_review` | Cauchy response, stable law, functional convergence, limiting independence, random evaluation, uniform integrability, moment transfer, non-Gaussianity | [Probability review](reviews/probability-review.md) |

Both reports preserve source hashes and state what was actually checked. Neither reviewer authored the mathematical manuscript. They did not implement the initial three Lean proofs. In subsequent extensions, the spectral reviewer implemented the Inertia and Graph blocks; root and the probability reviewer independently audited those proofs. Every block has two final referees other than its implementer. Root Codex prepared the repository presentation and exact finite checks, read both reports, and reconciled their shared conclusion with the original two-part target. No external human review, source-author endorsement of the AI implementation, or reproof of the reference papers is claimed.

The independent reviews address several potential failure points explicitly: equality of the two pendant completions' surplus without assuming their conditional weights; nontriviality of every exceptional equation; absence of a hidden stable-law centering term; dependence within each actual module; the atom at an infinite threshold; random evaluation in a local process topology; and stronger moment estimates beyond total variation. The fourth-moment result supplements an explicit proof of a non-Gaussian weak limit.

[Exact rational regression checks](check_algebra.py) passed in Python 3.9.6 both normally and with `-O`, including independent inertia controls. The [recorded output](algebra-checks.log) is deterministic. These finite checks validate implementations of selected identities, not the limit theorem.

The repository's catalogue validation passed on a clean copy of the candidate files. A clean copy avoids an existing catalogue scanner issue that traverses ignored local `.lake` dependency Markdown. The generator and its validation rules were not modified. Direct comparison confirms that the original **Problem statement** section is unchanged; the ID and canonical path remain 114 and `problems/114-quantum-graph-nodal-clt.md`.

## Formalization distinction

The complete counterexample is **not Lean verified**. The package now contains 25 supporting results in six independently reviewed blocks: the initial sign/moment algebra, actual finite multigraph, finite core inertia, actual Cauchy variance function, Gaussian-mixture law, and prescribed-length moment transfer. Each block has two preproof boundary approvals and two final proof audits, with separate local checks. The [verification record](../../lean/114/verification/README.md) states the exact scope of each isolated Linux run. The full informal mathematical audits above are distinct from these block-specific proof reviews.

The remaining formal gaps include metric-graph spectral theory, the stable ratio law and its intrinsic support/zero-atom properties, process convergence and random evaluation, and the identification of the actual graph limit with the proved mixture. No missing theorem is treated as a Lean axiom. Mechanical acceptance of these supporting blocks cannot promote the complete counterexample or catalogue entry to Lean verified.
