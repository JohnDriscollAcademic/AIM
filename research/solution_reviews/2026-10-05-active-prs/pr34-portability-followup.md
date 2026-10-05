# PR 34 portability correction: independent follow-up

Date: 2026-10-05. Reviewer: the OpenAI Codex AI agent that independently identified the original P3 Windows extension-matching regression. This report is separate from the unchanged original infrastructure audit.

**Verdict: the applied correction addresses the P3 finding. No new blocker found.** `scripts/catalogue.py:41` now uses `Path(name).match("*.md")`. This restores Windows case-insensitive extension matching while preserving POSIX case-sensitive matching, equivalent to the old recursive pathlib glob for individual filenames. Cache pruning remains unchanged.

## Reviewed identities

Original PR 34 head: `70212479ac5e4b5808fb6a4dfb86d0f03d675339`. Observed repository HEAD during the applied-working-tree review: `4e77593932f44ecc206d55a5d9641185323a6ae1`.

| Reviewed bytes | SHA-256 |
| --- | --- |
| Actual `scripts/catalogue.py` bytes read from disk | `d966c2b35344f5af12c34564f95ddf469ca462cf8822d2f2abad7b2f0214cd79` |
| Actual `scripts/test_catalogue.py` bytes read from disk | `e88b49b1b4ae3ab365426aed386557a59ef85d1d1fe814e20f02df0bec818639` |
| Raw 1,645-byte output of `git diff --no-ext-diff -- scripts/catalogue.py scripts/test_catalogue.py` against the observed HEAD | `6703cd63f30339da71c39782557023622426a37140e6b1a299280b063ba4189e` |

These are exact raw disk/diff identities, not newline-converted Markdown export hashes. The reviewed diff contains only the one-line filename predicate correction and the added ten-line regression test in these two files.

## Independent check

A disposable Windows probe imported the actual corrected implementation with bytecode generation disabled. It created ordinary `research/UPPER.MD` and `research/lower.md`, each containing a unique broken local link, alongside `.lake/README.md` with its own broken link. The old recursive pathlib traversal and corrected walker visited exactly the same two ordinary paths. The actual `validate` function reported both ordinary missing-link errors and no cache-content error. In particular it reported `research\\UPPER.MD: broken local link missing-uppercase-file.md`, closing the originally demonstrated bypass.

The same probe checked the platform path classes: `PureWindowsPath("UPPER.MD").match("*.md")` was true; the corresponding `PurePosixPath` result was false; lowercase matching was true for both. This verifies the POSIX predicate semantics directly; a native POSIX integration suite was not run by this reviewer.

The new `test_uppercase_markdown_extension_preserves_platform_link_checks` at `scripts/test_catalogue.py:162` writes a real uppercase-extension source containing a local link to `missing-uppercase-file.md`. On Windows it invokes the catalogue CLI and requires exit status one **and that unique missing-target diagnostic**, while the shared helper also rejects a traceback. Thus unrelated fixture failures cannot satisfy the intended assertion by themselves. On POSIX it requires successful catalogue generation; inclusion of the uppercase source would produce a broken-link failure and fail that branch. The test therefore checks the former platform-dependent validator behavior in both directions, rather than merely mirroring the filename predicate.

No repository, snapshot, manuscript, Git state, or GitHub state was modified by this reviewer. The original audit remains unchanged. I did not rerun the full suite; the root reviewer's clean corrected 58-test run and subsequent committed identities are separate verification evidence.
