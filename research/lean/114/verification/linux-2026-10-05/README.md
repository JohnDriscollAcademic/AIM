# Isolated Linux verification: AIM 114 supporting lemmas

The unmodified AIM verification workflow [passed on 2026-10-05](https://github.com/sidneyholden1/AIM/actions/runs/37344385173), on GitHub-hosted Ubuntu 24.04 in the submitting user's fork. Its exact source revision is [`4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`](https://github.com/sidneyholden1/AIM/tree/4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e/research/lean/114).

The run proves only the three supporting declarations listed in [comparator.json](../../comparator.json). It does not formally establish the graph counterexample or the original AIM 114 target. [NUMERICAL_TARGETS.md](../../NUMERICAL_TARGETS.md) identifies the missing links.

## Retained original artifacts

| File | GitHub artifact ID | SHA-256 |
| --- | --- | --- |
| [lean-114.zip](lean-114.zip) | `11360376107` | `49294a858cd44018f28c16db769a239341bf22888dd2815abeb935bec0918f2e` |
| [lean-checker-controls.zip](lean-checker-controls.zip) | `11359099459` | `8e62b3cd1cca5d180703a6f318989962b9770bd3d40a674582aa2e1c2fd81e21` |

The locally recomputed archive hashes match the digests in the retained [GitHub artifact metadata](github-artifacts.json). [GitHub run metadata](github-run.json) records the completed successful run and exact head SHA. The ZIP contents are also extracted in the correspondingly named directories.

The [source archive](source.tar.gz) retains all 33 project inputs from the verified revision, under the `source/` prefix. Its SHA-256 is `d829678666eb4934e51c8958ed9f5b430861ccb1fdc5cfe87e2899b043c7e785`. Every extracted file was compared with the verifier's input hashes and the immutable Git source.

The decisive evidence is the project's [Comparator log](lean-114/verify-20261005T165548Z-4176/comparator.log) and [result/input-hash manifest](lean-114/verify-20261005T165548Z-4176/result.json). Comparator built Challenge and Solution separately in a fresh committed-source copy, exported all three target declarations, checked allowed axioms and statement correspondence, and reported default-kernel acceptance with exit status zero. Every declaration printed exactly `propext`, `Classical.choice`, and `Quot.sound`.

The manifest contains all 33 original project file hashes and the pinned checker receipt. It records Lean 4.33.1, compiler commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, the locked Forsythe checker source, and the actual checker/exporter/sandbox binary hashes. The independent [operational audit](OPERATIONAL-REVIEW.md) compares these inputs against the immutable revision and earlier source reviews.

## Controls

The [project sandbox probe](lean-114/verify-20261005T165548Z-4176/sandbox.log) exercised the real build/export restrictions. [Kernel controls](lean-114/verify-20261005T165548Z-4176/kernel-controls.log) accepted an honest quotient/inductive fixture and rejected an invalid raw proof. A separate mismatched-quotient fixture passed the default kernel but was rejected by the quotient post-check. [Comparator controls](lean-114/verify-20261005T165548Z-4176/comparator-controls.log) exercised matching and mismatching statements/definitions and custom axioms. Separate [sorry](lean-114/verify-20261005T165548Z-4176/negative-sorry.log) and [native trust](lean-114/verify-20261005T165548Z-4176/negative-native.log) controls were rejected as required. The additional checker-only job independently passed its [self-test](lean-checker-controls/selftest-20261005T165537Z-4171/result.json).

This record reports actual remote Linux execution and subsequent evidence inspection. It is not a claim of a local Mac sandbox run. The upstream pull request's workflow remains subject to maintainer approval; the verified fork run uses the same workflow bytes and mathematical source. Subsequent documentation/metadata updates do not change the recorded revision or its scope.
