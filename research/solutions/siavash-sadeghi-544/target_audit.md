# Target and prior-submission audit - 2 October 2026

**Contributor and submitter:** Siavash Sadeghi.

## Exact problem identity

The supplied package targets **Triangle inequality for the pullback distance
of verbose persistence barcodes**. Repository numbering has changed:

| Identity | Pinned revision | Statement |
|---|---|---|
| Original AIM 544 | `aa776a01d7d48a79f93251af11fde9454b0aea95` | [Original statement](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/544-verbose-persistence-pullback-triangle.md) |
| Current AIM 534 | `fa98b7525fa3f78317536a8825f9cfa0ae1c369c` | [Current statement](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/534-verbose-persistence-pullback-triangle.md) |

A direct comparison confirms that only the first-line ID heading changed.
The current statement is Open, last checked 24 September 2026. Filenames
retain the original 544 identity. The current problem bearing number 544
has a different target and is not the subject of this contribution.

The target retains duplicated zero-distance vertices and every zero-length
persistence pair. It uses actual multiset bijections without free diagonal
padding and an infimum over arbitrary finite common sets and surjections.
The proposed degree-one example over F_2 suffices to disprove the universal
assertion; the proof also covers every field and every positive degree.

## Current repository audit

AIM 544 (current 534) repository duplicate-submission audit
Checked UTC: 2026-10-02T10:42:35.803035+00:00

Result: no matching prior repository submission found in the public sources inspected.

Target identity: original AIM 544 at aa776a01d7d48a79f93251af11fde9454b0aea95 is now AIM 534 at fa98b7525fa3f78317536a8825f9cfa0ae1c369c. Its file is problems/534-verbose-persistence-pullback-triangle.md. The complete text differs only in its first-line ID heading. Current AIM 544 concerns a different problem.

Scope: 20 indexed PR entries (4 open, 16 closed), 18 available dedicated PR records, 3 issue comments, 0 inline-review comments, and 1,144 tracked main files. Review endpoints for all four open PRs succeeded and returned no submitted reviews. The fourteen closed-PR review endpoints were rate-limited.

Changed-file coverage: available API records covered 138 changed-file observations. Ten cached immutable diffs were reused only after fresh base/head SHA equality checks. Five missing current diffs were recovered through public Git refs, adding 891 changed-file observations. Thus paths and available text changes were inspected for all eighteen PRs with dedicated records. Recovered matches concern catalogue renumbering or unrelated uses of the search terms; no matching solution appeared.

Five focused issue searches, for the original and current IDs plus verbose, pullback and persistence, each returned zero with incomplete_results=false. Target/source terminology was also searched directly in titles, bodies, comments, changed files and current main text.

Current target status remains Open; its automated-attempt queue is unstarted. Relevant main-tree hits describe the target, catalogue, source-screening history and ID mapping. The updated contribution instructions retain the same resolution-report and PR route; a package-only PR does not require a catalogue status change.

Limitations: GitHub core API rate limiting prevented fourteen closed-PR review reads and dedicated-detail reads for two closed entries retained in the issue index. Their retained titles, bodies and comments concern unrelated targets. Binary contents are not semantically searched by text-patch inspection. Deleted, private, unsubmitted or unindexed work and search lag cannot be excluded. This is a bounded repository check, not proof of literature novelty or mathematical correctness. No external change was made during this audit.

## Primary source and attribution

F. Mémoli and L. Zhou, *Ephemeral persistence features and the stability of
filtered chain complexes*, Journal of Computational Geometry 15(2), 258-328
(volume labeled 2024, published 2025):
[published paper](https://jocg.org/index.php/jocg/article/download/5193/3734/16411),
[DOI](https://doi.org/10.20382/jocg.v15i2a8),
[author revision v8](https://arxiv.org/abs/2208.11770v8).

The separate AI mathematical reviewer checked Remark 1.1, Definitions 4.7
and 5.3, and Example 5.10/Figure 7 against the proposed argument. The published
paper uses nonempty multiset bijections and finite tripods; the counterexample
has nonempty barcodes on every common pullback. The author's v8 revision still
poses the fixed-positive-degree question. These observations are not a
literature-wide novelty guarantee.

The degree-one X,Y pair and zero-cost duplication comparison are already in
Example 5.10. The proposed construction uses an equilateral third space with
distance 2; it differs from the distance-1 space called Z in that source.
The uniform lower bound addresses every common pullback, not just finitely
many tested sizes. Credit for the known pair is retained explicitly.

## Required submission route

The current [README](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/README.md)
and [CONTRIBUTING](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/CONTRIBUTING.md)
accept issues and pull requests. A resolution report must include the problem
ID and commit, a proof link, a full-target comparison, and who reviewed what,
including whether review was human or AI. The supplied resolution report,
proof and verification record meet that submission format.

The package is prepared for `research/solutions/siavash-sadeghi-544/` with
**Solution claimed** evidence language. No catalogue status change is proposed.
If maintainers change a catalogue status later, the contribution rules require
coordinated problem/data/catalogue updates, archiving and renumbering as needed.
New retained-entry metadata requirements do not apply to this package-only PR.
