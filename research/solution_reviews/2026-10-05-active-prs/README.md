# Independent review of the open PRs, 5 October 2026

Only two PRs were open when this review began. Closed requests were excluded. Three newly assigned OpenAI Codex AI referees independently checked the spectral argument, probability argument and supporting formalization in PR 33. A separate infrastructure review checked PR 34. The coordinating agent also read the complete informal argument and all supporting Lean statements/proofs. These are AI audits; no external human review or priority certification is claimed.

| PR | Pinned head | Outcome |
| --- | --- | --- |
| [33: AIM 114](https://github.com/MColbrook/AIM/pull/33) | `61916d1e9959dc7ed282edb124b51e8118735844` | Accepted non-Gaussian counterexample; AIM 114 remains Partial because universal variance bounds are unresolved |
| [34: catalogue cache validation](https://github.com/MColbrook/AIM/pull/34) | `70212479ac5e4b5808fb6a4dfb86d0f03d675339` | Accepted cache pruning and complete Lean fixtures; Windows extension matching corrected in the maintainer integration |

The original target and comparison main were `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. PR 34 was merged as `dbad7c7b19f49a587a220bf2ce55e4db42498f23`, followed by PR 33 as `4e77593932f44ecc206d55a5d9641185323a6ae1`.

## Mathematical acceptance

The [fresh spectral review](pr33-spectral-independent-review.md) verifies graph admissibility, the hypotheses and normalization of the primary spectral results, a direct quadratic-form index calculation, all pendant completions and exceptional sets, and spectral contamination. The [fresh probability review](pr33-probability-independent-review.md) independently derives the stable vector and ratio law, intrinsic support and atomlessness, process tightness and joint independence, endogenous evaluation, uniform moments, contamination and normalization by the actual variance. Both read the entire submitted PDF and expanded argument and found no blocking defect. Earlier package reviews were not used to form their mathematical verdicts.

The graph sequence disproves the unrestricted Gaussian assertion. Its own variance is asymptotically linear in cycle rank, so it does not decide the separate universal variance bounds. The target imposes neither bounded degrees nor comparable edge lengths. AIM 114 stays in the open-target list with a Partial label; no complete solution or Lean-verified status is recorded.

All nine submitted provenance hashes match exact immutable Git blobs, and the frozen statement matches the original target. The [integrity record](solution-integrity.json) pins this check to the submitted head. Windows archive exports normalize text to CRLF; authoritative hashes were computed from raw Git blobs. The submitted mathematical source, PDF and proof code are unchanged. The package README gains only the later acceptance link, and its provenance hash is refreshed; the original head remains identifiable in this historical integrity record.

## Supporting formalization

The [fresh formal referee](pr33-formal-independent-review.md) and [maintainer semantic audit](pr33-maintainer-semantic-review.md) inspected all 31 actual supporting declarations and their proofs. Concrete graph/length definitions, finite inertia, the actual Cauchy variance, normalized Gaussian-mixture law and contamination results match their advertised statements. The complete spectral operator and phase law, stable response/ratio construction, process limit and identification with the graph remain outside the certificate.

The formal referee freshly bound the successful [fork Linux run](https://github.com/sidneyholden1/AIM/actions/runs/37365344243) at `56afd77d2456af3da7934947699ee86735494010` to both original artifacts, all 306 archived input files and all 58 pinned checker source files. Current mathematical and checker bytes match that successful revision. [Machine evidence](pr33-formal-independent-evidence/audit.json) records each comparison and primary API metadata. Comparator/default-kernel acceptance, isolation gates, permitted transitive axioms and rejection controls were inspected in actual logs.

The newly approved [upstream Linux run 37368047705](https://github.com/MColbrook/AIM/actions/runs/37368047705) also passed at the exact PR head. Its [independent receipt audit](scratch/pr33-upstream-ci/upstream-ci-review.md) verifies the artifact digest, all 340 input hashes and all 31 results, including the project kernel/rejection/isolation controls. The receipt records synthetic merge checkout `3ecc437c88a801ee3e028b0a34054366b0f8ce10`; its project and checker bytes match the submitted head. The separate checker-controls job was skipped because the checker was unchanged; the controls inside project verification ran successfully. The [machine audit](scratch/pr33-upstream-ci/upstream-ci-audit.json) and original artifact retain this distinction.

The portable [formal evidence reproduction script](scratch/pr33-formal-reproduce.py) requires Git, authenticated GitHub CLI access and the two pinned revisions. Its default output is a new system temporary directory. Only CLI input/output routing was adapted after the original audit; the recorded audit was not rerun for that adaptation.

## Infrastructure and reproducible checks

The [independent PR 34 review](pr34-independent-review.md) confirms cache pruning and ordinary source coverage. It identified a Windows portability regression: `.endswith('.md')` skips uppercase extensions which the previous pathlib traversal checked on Windows. The integration uses `Path(name).match('*.md')` to preserve the original platform rules and adds a broken-uppercase-link regression. The prior head passed all 57 catalogue tests; its [completion summary](catalogue-regression.log) records that result.

The [independent portability follow-up](pr34-portability-followup.md) confirms that the applied correction closes the Windows bypass and preserves POSIX matching. It exercised actual local-link validation in a disposable source tree and inspected the new CLI regression independently.

The corrected clean snapshot passed all **58 catalogue tests** in 587.209 seconds; the [final log](catalogue-regression-final.log) records this run. Audit-report links and math macros were adapted to repository Markdown conventions without changing findings. Local console-log whitespace was normalized; original CI artifacts and extracted evidence remain unchanged.

The submitted exact checker passed normally and with Python optimization ([normal log](combined-check-1.log), [optimized log](combined-check-2.log)): 504 sign-average cases, 448 graph instances and 24 response cases. The fresh spectral referee's separate [portable Fraction script](scratch/pr33-spectral-independent-checks.py) reproduced 983 nonexceptional graph instances and 296 cases with all eight effective sign patterns; its [actual result](scratch/pr33-spectral-independent-checks.json) records the seed and exclusions. These finite checks support algebraic identities; the cited theorems and mathematical audits establish the spectral and limiting steps.

The combined immutable PR snapshots passed [catalogue validation](combined-check-3.log) for all 651 problems and [manifest validation](combined-check-4.log) for all 31 declarations. The local [metadata suite](combined-check-5.log) encountered eight Windows symlink-privilege errors; this is not recorded as a local pass. The unchanged 43 metadata/project-selection tests and 12 harness tests passed on Linux in [PR 34 run 37344861467](https://github.com/MColbrook/AIM/actions/runs/37344861467); the [local 12-test harness run](combined-check-6.log) also passed.

From the repository root, the independent algebra regression is reproduced with:

```sh
python -B research/solution_reviews/2026-10-05-active-prs/scratch/pr33-spectral-independent-checks.py
```

Final catalogue validation uses an isolated snapshot of tracked repository content and the intended integration changes. Five pre-existing untracked draft solution directories are preserved untouched and excluded from that snapshot.

The [final check record](final-checks.json) records successful catalogue generation and [651-page validation](final-check-2.log), [31-declaration manifest validation](final-check-3.log), and the [relocated independent algebra reproduction](final-check-4.log). The [integration integrity record](integration-integrity.json) confirms all nine current package hashes, preservation of the original problem statement and no changes to the accepted Lean project. The [merge record](merged-prs.json) identifies both accepted commits.
