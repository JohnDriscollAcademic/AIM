# Independent operational review of Linux verification

- Date: 2026-10-05.
- Reviewer: Codex AI subagent `spectral_review`, independent of the proof implementer. This is an audit of execution evidence, not a new Linux execution or human peer review.
- Verdict: **APPROVE the operational evidence for the three supporting Lean declarations at the immutable revision below.** The artifacts support successful fresh sandboxed Comparator and kernel verification, with the required acceptance and rejection controls. They do not prove the complete AIM 114 counterexample.
- [GitHub Actions run 37344385173](https://github.com/sidneyholden1/AIM/actions/runs/37344385173), attempt 1, repository `sidneyholden1/AIM`.
- Verified proof revision: `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`.
- Project: `research/lean/114`.

## Provenance and independent checks

I independently queried the GitHub API for the run, jobs, and artifacts. The run and all three jobs (`select`, `checker-controls`, and `verify (114, research/lean/114)`) were completed successfully. The project-verification job finished at `2026-10-05T16:59:12Z`. The API's head revision agrees with the receipt's repository revision.

I hashed the two original downloaded ZIP archives and compared them with the artifact digests returned by the live GitHub API:

| Artifact | GitHub artifact ID | Verified SHA-256 |
| --- | --- | --- |
| [lean-114.zip](lean-114.zip) | `11360376107` | `49294a858cd44018f28c16db769a239341bf22888dd2815abeb935bec0918f2e` |
| [lean-checker-controls.zip](lean-checker-controls.zip) | `11359099459` | `8e62b3cd1cca5d180703a6f318989962b9770bd3d40a674582aa2e1c2fd81e21` |

Every extracted evidence file linked below was compared byte-for-byte with its original ZIP entry: 13 files in the project archive and 10 in the checker-control archive matched.

The project [result receipt](lean-114/verify-20261005T165548Z-4176/result.json) contains 33 input SHA-256 entries. I checked each against `git show 4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e:research/lean/114/<path>`, and checked that the recorded set is exactly the complete tracked project-file set at that revision. **All 33 matched.** I did not compare administrative files against the moving working tree and mistake later documentation updates for changed proof inputs.

The nine mathematical/configuration/toolchain inputs also match my preceding independent source review: Definitions, Proof, Challenge, Solution, NUMERICAL_TARGETS, Comparator configuration, Lakefile, dependency manifest, and toolchain file. In particular:

| File | SHA-256 |
| --- | --- |
| `AIM/P114/Definitions.lean` | `0c29c3c5b0cec95e1463ca190792b26a8d42733cdcca5b99796f84bd03a854ff` |
| `AIM/P114/Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` |
| `Challenge.lean` | `762965dcaab9eff7d0fca577597a1b900a7acde8899928eceb38d9a0c0c740fe` |
| `Solution.lean` | `40cecf7e29a88f5756d10385648ca2fee0b33da8124c1d31bdde08b52321f0b4` |

The complete comparison results, minimal independently fetched API metadata, and archive matches are recorded in [referee-1-operational-source-audit.json](referee-1-operational-source-audit.json).

I also independently checked the retained [source.tar.gz](source.tar.gz), SHA-256 `d829678666eb4934e51c8958ed9f5b430861ccb1fdc5cfe87e2899b043c7e785`. Its complete set of 33 regular source files matches the receipt's input set, and each file matches both the receipt hash and the immutable Git blob. This archive preserves the actual verified source snapshot alongside the run evidence.

## Toolchain and fresh-run procedure

Both tool receipts identify Lean `4.33.1` on `x86_64-unknown-linux-gnu`, Lean commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`, Go `1.27.1`, and Linux `6.17.0-1022-azure` with glibc `2.39`. The workflow selects Ubuntu 24.04. The source lock digest is `b3833b07916e5db77579b9cc53ca582282f6a841f36d6a60d693e5b02d342b6b`, with Forsythe source revision `8d1b0c0545a77b40245e84705aa7d273e6c81e62` and derived CI sandbox-probe digest `31057195baf238807cacbb4126c5b07f02cec55a4e4437de5f3a755b3fada803`.

I inspected `tools/lean/harness.py`, its source lock, and the workflow, and verified that those inspected bytes match the immutable run revision. The driver checks hash-locked tools, runs controls, copies ordinary tracked source files from the committed tree into a fresh project, rejects tracked build artifacts and symlinks, and checks input hashes after dependency preparation, cache preparation, and Comparator. Its proof procedure has no separate preceding Solution build in that fresh directory.

The [dependency log](lean-114/verify-20261005T165548Z-4176/dependencies.log) records immutable checkouts of Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`, LeanCert `621a43d7cf21f87872392a01e874f2f1dbddc926`, and the remaining manifest dependencies. The [cache log](lean-114/verify-20261005T165548Z-4176/mathlib-cache.log) records successful Mathlib cache preparation. These are dependency preparation steps, not substituted proof results.

## Actual sandbox evidence

I read the sandbox logs from both the standalone controls and the project verification. The [project sandbox log](lean-114/verify-20261005T165548Z-4176/sandbox.log) reports both `build` and `export` modes with exit zero under the strict Landrun/Bubblewrap setup. The systemd wrapper explicitly uses `RestrictAddressFamilies=~AF_UNIX`.

- In build mode, writes inside the designated `.lake` directory are allowed. Outside write-open, truncation, read-only truncate-open, creation, and a symlink-directed outside write are denied.
- In export mode, the same outside writes are denied, and `.lake` writes and truncations are also denied.
- Both modes report private user, PID, mount, network, IPC, and UTS namespaces; the host parent is absent from private `/proc`, parent signal lookup fails, and the host loopback listener is unreachable.
- AF_UNIX socket creation is denied, effective capabilities are empty, and `no_new_privs` is set. The sandbox UID is the unprivileged UID 1001.
- The nested Bubblewrap attempt exits one with `setting up uid map: Permission denied`. This records rejection at nested namespace setup; it should not be described as a successful nested namespace followed by an independently exercised inner write denial.
- Unknown options, an unexpected `--rw`, an unexpected `--rwx`, and a relative `--rwx` each fail closed with exit two.
- The log confirms that outer and export fixture contents remained unchanged and only the designated build fixture was written.

The retained probe is the recorded noninteractive CI adaptation of the original probe, not an unchanged PTY execution. I found no missing required mode or skipped assertion in the observed evidence. The sandbox is an integrity/isolation control and does not promise confidentiality of host-readable files; this audit adds no such claim.

## Kernel and rejection controls

Both archives contain the expected controls. I inspected the main verification's [kernel-control log](lean-114/verify-20261005T165548Z-4176/kernel-controls.log):

1. The honest fixture with inductives and quotients is accepted by the default kernel.
2. The invalid raw proof is rejected with the actual type mismatch `True` versus `False`.
3. The quotient-mismatch fixture reaches kernel acceptance but is then rejected by the quotient post-check for `Quot.lift`. This is a distinct post-check result, not a kernel rejection.

The [Comparator-control log](lean-114/verify-20261005T165548Z-4176/comparator-controls.log) shows all five expected outcomes: `simple_match` succeeds; `simple_mismatch` fails on constant kind; `simple_axiom_issue` and the fixture named `simple_kind_mismatch` fail on the illegal `helper` axiom; and `type_mismatch` fails on the theorem-statement mismatch. The log reports the required reason for each case, rather than merely a nonzero process exit.

The [sorry control](lean-114/verify-20261005T165548Z-4176/negative-sorry.log) builds both modules and then rejects `sorryAx` with exit one. The [native control](lean-114/verify-20261005T165548Z-4176/negative-native.log) builds both modules and then rejects `checked._native.native_decide.ax_1_1` with exit one. Neither rejection is a compilation failure being misreported as a trust-policy test.

The separate checker artifact's [self-test receipt](lean-checker-controls/selftest-20261005T165537Z-4171/result.json) correctly labels its result as checker fixtures only. It is not itself evidence of an AIM theorem; the following project run supplies that evidence.

## Project theorem verification

The [actual Comparator log](lean-114/verify-20261005T165548Z-4176/comparator.log) records fresh builds and exports of Challenge and Solution for exactly:

- `AIM.P114.module_count_identity`
- `AIM.P114.sign_second_moment`
- `AIM.P114.variance_mixture_kurtosis`

Each Solution axiom report is exactly `[propext, Classical.choice, Quot.sound]`. The configuration contains no definition holes. Challenge's three deliberate placeholder warnings appear only in the Challenge build; they are not silently counted as proved Solution theorems.

The log then invokes the default kernel on the solution, reports kernel acceptance, reports Comparator acceptance, and ends with `EXIT_STATUS=0`. The matching receipt gives `result: comparator-accepted`. The source hashes establish that this acceptance pertains to the same three proofs and fixed definitions independently reviewed earlier, rather than a substituted set of theorem names or definitions.

## Limits of the approval

This report audits retained GitHub Actions evidence and immutable source correspondence. It does not independently rebuild the checker binaries or rerun the Linux job, and it does not claim formal verification of the checker implementation. The recorded toolchain, dependencies, Challenge, and execution service remain within the stated trusted infrastructure.

The successful Linux run verifies **three partial supporting lemmas**. It does not formalize the graph, its Kirchhoff operator, generic spectral-frequency law, published secular measure reduction, functional/stable limits, or the full non-Gaussian counterexample. It also does not resolve the universal variance assertion. The mathematical reviews and explicit scope document remain necessary; kernel acceptance cannot establish those unencoded links.

This evidence may support a statement that the three supporting lemmas passed AIM's isolated Linux verification at revision `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`. It does not support promoting the entire AIM 114 entry to Lean verified. No proof, definition, manifest, README, or original evidence archive was changed during this audit.
