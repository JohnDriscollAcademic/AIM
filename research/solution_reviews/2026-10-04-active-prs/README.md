# Independent review of the open solution PRs, 4 October 2026

Five fresh Codex AI referee agents, each with no role in manuscript preparation, independently checked the complete submitted arguments against the exact catalogue targets at `c4b2a812bb5babdb1efdad8c3b8080e7301ee507`. The coordinating agent had participated in earlier preparation; its checks of packaging and integration are recorded separately from these fresh mathematical audits. No independent human review, publication acceptance, priority certification, or formal verification is claimed.

| AIM | PR | Outcome | Independent audit |
| --- | --- | --- | --- |
| 505 | [28](https://github.com/MColbrook/AIM/pull/28) | Uniform upwind estimate disproved | [Audit](505-review.md) |
| 523 | [29](https://github.com/MColbrook/AIM/pull/29) | General smooth-amplitude bound disproved | [Audit](523-review.md) |
| 553 | [30](https://github.com/MColbrook/AIM/pull/30) | Sharp asymptotic established; exact non-power-of-two values remain open | [Audit](553-review.md) |
| 570 | [31](https://github.com/MColbrook/AIM/pull/31) | Universal bound disproved using nonseparable spaces | [Audit](570-review.md) |
| 641 | [32](https://github.com/MColbrook/AIM/pull/32) | Cubic assertion proved in every dimension; three quartic targets remain open | [Audit](641-review.md) |

The [integrity record](package-integrity.json) compares all 67 manifest entries with exact raw Git blobs at the five pinned heads: every submitted hash matches. Inspection snapshots have CRLF where Git stores LF; normalization gives identical content. The [document checks](document-technical-checks.json) record PDF page counts, metadata, and source label/citation checks: no missing citations or references, duplicate labels, or unused bibliography entries were found. Each referee separately checked mathematical dependencies and primary sources as described in its audit.

The manuscript sources, PDFs, certificates, and submitted mathematical code are retained unchanged. Package README updates identify the later maintainer acceptance and link these audits; their README manifest entries are refreshed. Earlier preparation reports and wording inside the original PDFs remain historical records.

Fresh AIM505 numerical checks are in [505-independent-checks](505-independent-checks/independent_checks.py). AIM641's independently derived symbolic-dimension check and reproduction runner are in [641-independent-checks](641-independent-checks/independent_checks.py). Those independent scripts were relocated with only repository input-path adjustments; their mathematics is unchanged. Stored original logs record the inspection environment and original paths. Reproduction from the repository root requires NumPy 2.3.5 for AIM505 and SymPy 1.14.0 for AIM641; submitted AIM505 ODE diagnostics also require SciPy 1.18.1.

```sh
python -B research/solution_reviews/2026-10-04-active-prs/505-independent-checks/independent_checks.py
python -B research/solution_reviews/2026-10-04-active-prs/641-independent-checks/independent_checks.py
python -B research/solution_reviews/2026-10-04-active-prs/641-independent-checks/review_runner.py
```

The exact-computer-algebra checks support the conventional cubic proof; they are not a proof-assistant development. Floating-point AIM505 diagnostics corroborate the analytic argument and do not establish its mesh/exponent limits.

The [merge record](merged-prs.json) pins all five accepted merge commits. Catalogue generation and validation passed on an isolated snapshot of tracked repository content plus these intended changes; five pre-existing, untracked preparation directories with unfinished links were excluded and preserved untouched. The [catalogue log](catalogue-check.log) records validation of all 651 problem pages, metadata, math delimiters, local links and generated lists.

After relocation, both independent checks and the complete AIM641 normal/optimized reproduction and corruption-control runner passed again. The [relocated reproduction record](relocated-reproduction-results.json) links its three logs by filename. Only input paths and Markdown/typesetting were adapted; no submitted mathematical source, PDF, certificate, or proof code was changed.
