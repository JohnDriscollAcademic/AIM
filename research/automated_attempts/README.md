# Autonomous Mathematical Research Programme

This is the persistent coordination layer for the repository's growing problem collection. Repository problem files and their established indexes determine membership. Discover membership from the current metadata rather than assuming a fixed count or maximum identifier. Problem-page IDs are consecutive from 001 and may change after deletions; solved pages keep their IDs and are ineligible for research selection.

**Current checkpoint (2026-10-02):** [649 open targets and 16 solved entries](QUEUE.md). Campaign 001 remains incomplete conditional research; see [its evidence summary](001/STATUS.md). This queue checkpoint is administrative; external solution reviews are recorded [separately](../solution_reviews/2026-10-02/README.md).

## Scope and layout

Programme writers may create or modify files only beneath `research/automated_attempts/` unless a later user instruction explicitly expands that scope. Problem files, the [open-target index](../../CATALOG.md), the [resolution archive](../../RESOLVED.md), the main README, and other existing research files are read-only inputs.

| Path | Purpose |
| --- | --- |
| `STATE.md` | Current campaign, counters, priorities, phase, and revision. |
| `QUEUE.md` | Dynamically synchronized membership and preserved campaign history. |
| `<problem-id>/PROGRESS.md` | Compact cumulative memory, separated by evidence class. |
| `<problem-id>/attempts/` | Immutable Sol attempt records. |
| `<problem-id>/reviews/` | Immutable Astra senior reviews, including substantive research. |
| `<problem-id>/artifacts/` | Reproducible proofs, code, exact certificates, and source audits. |

Keep canonical identifiers as strings. New senior reviews use UTC names `YYYY-MM-DD_HHMM_astra.md`; if a collision exists, use another unused minute after recording the actual run time, or a disambiguating suffix. Existing names remain valid and immutable. Sol records retain the established `YYYYMMDDTHHMMSSZ-sol-<id>.md` convention unless the invocation specifies otherwise. Corrections cite old records rather than rewriting them.

## Every invocation

1. Discover all current problem files, including files beyond the initial index ranges. Check their canonical headings against every current machine-readable index and [CATALOG.md](../../CATALOG.md). Check [RESOLVED.md](../../RESOLVED.md) for retained entries outside the open catalogue. Do not limit discovery to historical index ranges.
2. Compare actual membership with `QUEUE.md`. Add newly discovered problems as `unstarted`, preserving canonical identifiers and titles. Preserve all existing statuses and history. Record actual discovery dates; do not invent old dates or priority scores.
3. Preserve unexpectedly missing files' queue entries and research directories. Explicit owner-requested removals recorded in `catalogue.json` stay excluded; retained entries are kept separately and are ineligible for active selection. Update a rename/renumber only when correspondence is unambiguous. Record duplicate IDs, contradictory indexes, malformed entries, and ambiguous correspondences as `queue_integrity_issues`; continue unaffected research.
4. Read `STATE.md`, `QUEUE.md`, the exact current statement, and current `PROGRESS.md`. A senior run also reads all Sol attempts since the preceding Astra review and the two most recent reviews, if present. Load older history only to resolve a claim.
5. Record the starting revision. Audit claims adversarially, make substantive mathematical progress where possible, and write a new run record and substantial reproducibility artifacts.
6. Update compact cumulative memory and current instructions. A senior run decides campaign allocation; only Astra may change `current_problem`.

## Evidence and candidate policy

`PROGRESS.md` separates VERIFIED RESULTS, PROMISING BUT UNPROVED CLAIMS, COMPUTATIONAL EVIDENCE, FAILED / EXHAUSTED ROUTES, CURRENT BOTTLENECK, and NEXT HIGH-VALUE ATTACKS. Distinguish programme proofs, external source statements, abstract method obstructions, and results about actual admissible domains. Repetition, floating-point experiments, or symbolic output do not establish an unproved lemma.

An apparent complete solution changes `phase` to `verification` and requires `CANDIDATE_PROOF.md`: reconstruct the proof coherently and enumerate every dependency. Direct subsequent Sol runs to adversarial checking. Use `solved_candidate_verified` only after at least TWO separate Astra senior-review invocations whose principal purpose was verification survive without an unresolved critical gap. Subagents within one invocation are not separate senior-review runs. Computer-assisted proofs require an explicit finite mathematical reduction, rigorous exact/interval certification, and reproducible artifacts. A diagnostic lemma or a special case does not enter full-problem verification.

## Preparing a request for human review

Before requesting volunteer human review, prepare a compact review packet linked from the current status summary. Include:

1. The precise proposed theorem, its hypotheses and conclusion, and how its scope compares with the catalogue target.
2. The claimed new contribution, relevant prior work and its attribution, and any rediscovered results.
3. An argument map identifying the main steps and dependencies, with links to the full argument.
4. All known gaps, conditional assumptions and outstanding checks, and what has actually been checked so far.
5. Reproduction commands, pinned source or artifact revisions, and the logs or certificates needed for any computational component.
6. A specific, bounded requested task, with an estimated effort where possible, such as checking one lemma or reproducing one certificate.

Review is voluntary. Agree the requested scope with the reviewer; do not treat silence or an unfinished review as acceptance. Obtain consent before naming a reviewer publicly, and record the agreed review scope and contribution. Preparing a packet does not authorize unsolicited messages to potential reviewers.

## Campaigns and fair selection

A campaign normally receives roughly sixteen Sol attempts and four Astra reviews, with evidence-based extension or early reassessment. Extend concrete promising work or candidate verification. After a substantial unproductive campaign, record `deferred_after_campaign`, preserve the strongest result and remaining gap, and choose a successor from the CURRENT synchronized queue. New arrivals do not automatically end a campaign.

Consider all `unstarted`, legacy `queued`, `active`, legacy `research`, and eligible revisit entries. Ordinarily prefer an unstarted problem over repeatedly exhausted deferred work. Use waiting history and actual discovery dates to prevent permanent starvation; use tractability, implications, and concrete leads as secondary criteria. Never select by hard-coded numeric increment. Initialize an unseen successor directly from its current actual statement. If no unresolved current entries remain, use `all_current_problems_reviewed` and keep synchronizing on every future invocation.

Legacy status strings remain readable: `queued` means unstarted; `research` means active; `paused`/`exhausted` require recorded revisit decisions. Preserve legacy status history rather than rewriting it silently.

## Concurrency and commits

Immediately before final GitHub writes, reread the latest `STATE.md` AND `QUEUE.md`; if changing the current problem, recheck the latest problem set. Prefer checking the full tree in every senior run. If revision changed, incorporate the newest state, progress, attempts, reviews, and queue additions; recompute counters and direction from that state. Preserve the other run's artifacts and history.

Prefer one atomic tree/commit based on the latest branch head, then a non-forced fast-forward ref update. If the branch advances, reconcile and retry from the new head; never force over concurrent work. Every successful run increments `revision` exactly once from the latest value. Count one Astra review per senior invocation, not per subagent; a failed or abandoned run does not advance state. Confirm the resulting committed files and scope.
