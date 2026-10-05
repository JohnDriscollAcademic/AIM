# Independent operational review: Linux verification of 25 supporting results

- **Reviewer:** `probability_review`, independent OpenAI Codex AI referee; not the package integrator or Linux-run operator.
- **Review date:** 2026-10-05.
- **Verdict:** **ACCEPT** this evidence as a successful authoritative Linux Comparator/default-kernel run for the exact 25 selected supporting declarations at commit `41c4f33f6a65ac8c9f6901bf1875e4420ee6f980`.
- **Scope:** this is the historical 25-result package. It excludes the later three Length results and three GraphLengthBridge results. The current 31-result package requires its own corresponding run and review.

This review independently inspects and cross-checks retained artifacts. It does not claim that the reviewer reran the Linux checker locally. I left raw logs, original archives, and retained GitHub metadata unchanged. My machine-readable cross-check results are in [OPERATIONAL-CHECKS.json](OPERATIONAL-CHECKS.json).

## Provenance and exact source

The [GitHub Actions run](https://github.com/sidneyholden1/AIM/actions/runs/37362894274) is run `37362894274`, attempt 1, a `workflow_dispatch` run on the contributor's fork `sidneyholden1/AIM`. Its exact source commit is `41c4f33f6a65ac8c9f6901bf1875e4420ee6f980`. The retained run and job metadata report completed success for `select`, `checker-controls`, and `verify (114, research/lean/114)` on `ubuntu-24.04`. I independently queried GitHub's API with `gh api` and confirmed the run ID, attempt, head SHA, completed status, and success conclusion. This is evidence from the fork's workflow, not an assertion that an upstream maintainer has reviewed or approved the PR.

I computed both ZIP digests and compared them with the retained and freshly queried GitHub artifact records and `evidence-summary.json`:

| Original artifact | Artifact ID | SHA-256 |
|---|---|---|
| `lean-114.zip` | `11367338467` | `0011b7c752a10dc11a30ebed3daccb43941e664766bed59c3aeef78b6609a33f` |
| `lean-checker-controls.zip` | `11367871801` | `003674685f6459d4ed31bed15ddd042733c30bf96ddd137d5d62b199c85098d9` |

Both ZIP integrity checks passed. All 13 extracted files from `lean-114.zip` and all 10 from `lean-checker-controls.zip` match their original ZIP members byte for byte. The source archive digest is `289308fab7eccbea43c8974311689420949a7788b569b852bb382a12f47eacea`, matching the retained summary.

The verifier's [result.json](lean-114/verify-20261005T193404Z-4196/result.json), SHA-256 `4391a5ca0260177f8eacd7cbaf17d0bdcbaaa0393aa8aa8ea54bcd4711830fad`, records 204 input paths. I checked every one against both the `source/` member in `source.tar.gz` and the Git blob obtained from the immutable commit with `git show`. Every byte and SHA-256 matches. The recorded paths, archive members, and entire tracked project-file set at that commit agree exactly; no extra or omitted tracked input was found. The archived `comparator.json` also equals the config recorded in the result.

## Locked infrastructure and clean preparation

The workflow, harness, source lock, bootstrap/verify/selftest wrappers, and CI Lean toolchain are byte-identical between this run's immutable commit, the original successful three-result commit `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`, and the files inspected in the current checkout. Their individual hashes are retained in my cross-check JSON. In particular, the source-lock hash is `b3833b07916e5db77579b9cc53ca582282f6a841f36d6a60d693e5b02d342b6b`, exactly the value in both tool receipts.

The receipts identify pinned Forsythe tooling commit `8d1b0c0545a77b40245e84705aa7d273e6c81e62`, Lean `4.33.1` on Linux x86-64, and Go `1.27.1`. The committed package manifest pins Mathlib to `0df444a360eaa60ab8c11dca51a86af692955474` and LeanCert to `621a43d7cf21f87872392a01e874f2f1dbddc926`. Dependency materialization and Mathlib cache logs both finish with exit status zero. The tool receipts in the two jobs agree on checker, exporter, Landrun, environment, and derived sandbox-probe hashes.

I inspected the actual harness. It takes ordinary tracked files directly from the immutable Git tree into a fresh project directory, rejects tracked compiled artifacts and symbolic links, validates the config and pinned dependencies, and checks input hashes after dependency preparation, cache retrieval, and Comparator execution. Its fresh-directory path is present in the retained command log. It does not build the submitted Solution before Comparator. The success result is emitted only after expected exit codes, acceptance markers, and unchanged input hashes have all been checked.

I also independently fetched the four relevant hash-locked source files for Comparator's main procedure, statement comparison, axiom traversal, and strict sandbox adapter from the immutable tooling commit. Each matched its source-lock byte count and SHA-256 before inspection. No locally altered checker was used as evidence.

## Separate statements, actual comparison, and kernel replay

The [Comparator log](lean-114/verify-20261005T193404Z-4196/comparator.log) shows Challenge built and exported first, then Solution built and exported in a separate module environment. Challenge has 25 deliberate placeholder warnings. Solution builds the six actual proof modules and has no placeholder warning. My examination of the immutable local import closures confirms that Solution imports no Challenge, and Challenge imports no proof module. They share the reviewed definitions, as intended.

The selected 25 declaration names in `result.json`, immutable config, exports, and Solution's printed axiom lists agree exactly. The pinned Comparator code compares declaration kinds and full constant signatures, traverses the definitions used by their types, checks the solution's axiom closure, and then replays the exported solution in a new empty default-kernel environment, with the quotient constants handled and post-checked explicitly. It does not simply accept a successful ordinary Lake build.

The actual project log ends with all of:

```text
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
EXIT_STATUS=0
```

The resulting status is `comparator-accepted`. This supports statement equality, allowed-axiom closure, and actual default-kernel replay for the selected 25 results. There is no external-kernel or Nanoda verification claim.

All 25 printed transitive-axiom sets were independently parsed and compared with the selected declaration set. `counterexample_parallel_edges` uses exactly `propext` and `Quot.sound`; each of the other 24 uses exactly `propext`, `Classical.choice`, and `Quot.sound`. There is no custom, `sorryAx`, or native-computation axiom. The config allows only those three standard axioms and has no definition holes.

## Real isolation and rejection controls

Both the standalone checker job and the actual project-verification job ran the full control suite successfully. I read the project logs and independently checked all expected control outcomes in both retained sets, rather than relying solely on a summary success flag.

The [sandbox probe](lean-114/verify-20261005T193404Z-4196/sandbox.log) confirms private user, PID, mount, network, IPC, and UTS namespaces; an absent host-parent process; denied parent-signal lookup, host-loopback access, and AF_UNIX socket creation; no effective capabilities; and `no_new_privs`. Ordinary outside writes, truncations, creation, and a symlink write from `.lake` to an outside file are denied. Only the designated build `.lake` is writable; export `.lake` writes and truncation are denied. The nested-namespace write attempt executes and is rejected. Unknown options and unauthorized writable-path requests fail closed with exit status two. Outer and export fixture contents remain unchanged.

The pinned adapter uses actual Bubblewrap plus the built Landrun executable; the surrounding systemd invocation restricts AF_UNIX. These are genuine runtime probes, not an empty or substituted sandbox command. They establish the tested isolation properties; the sandbox deliberately permits host-readable file access and is not a confidentiality claim.

The [kernel controls](lean-114/verify-20261005T193404Z-4196/kernel-controls.log) exercise the actual `Comparator.runBuiltinKernel`: an honest inductive/quotient fixture is accepted, an invalid raw proof is rejected by the kernel, and a quotient mismatch is rejected by the post-check. The [Comparator controls](lean-114/verify-20261005T193404Z-4196/comparator-controls.log) accept the honest match and reject the mismatched declaration, extra helper axiom, kind/axiom issue, and changed theorem type. Separate controls reject [`sorryAx`](lean-114/verify-20261005T193404Z-4196/negative-sorry.log) and the [native-decide axiom](lean-114/verify-20261005T193404Z-4196/negative-native.log) with the required nonzero exit status and exact illegal-axiom messages. Those expected negative exits are successful controls, not failures of the project proof.

## Binding to independent proof reviews

Each checked proof module's hash occurs in its corresponding independent final report, both in the immutable 25-result source and in the current report copy:

| Module | Checked SHA-256 | Independent referee-2 report |
|---|---|---|
| `Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` | `proof-referee-2.md` |
| `TransferProof.lean` | `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c` | `transfer-proof-referee-2.md` |
| `MixtureProof.lean` | `2a5d65beeeb576efad8eaf9940ebe0b5cd81cd52e402807e004444ca2e9e6bcf` | `mixture-proof-referee-2.md` |
| `InertiaProof.lean` | `d0acd2dfda515f792ca12195be04b1b07d0ca76e75e7cb20b1afd0e09e06345d` | `inertia-proof-referee-2.md` |
| `VarianceProof.lean` | `3a160951c60be915a49a2b9dedb1495e76e6f35007339ab7f30d03901e33e6c2` | `variance-proof-referee-2.md` |
| `GraphProof.lean` | `75232119b42e3cffb5829d959fc38842acc1381eeb409da33d9baef9faae95ea` | `graph-proof-referee-2.md` |

This connects the operational acceptance to the mathematical proofs I independently reviewed; it does not turn mechanical verification into informal-statement review. The verifier appropriately records `semantic_review: not-performed-by-this-command`.

## Attribution correction and disposition

The immutable 25-result metadata incorrectly attributes implementation of the original three results to root. The implementer has since directly confirmed that `lean_feasibility` implemented them and root integrated them; the current 31-result metadata records that correction. I have not rewritten the historical evidence. The original independent reviewers remain `spectral_review` and `probability_review`, and the checked proof bytes are unchanged, so this correction does not affect review independence or kernel acceptance.

**No blocking operational finding was found for the 25-result run.** The retained logs, live artifact digests, immutable source, locked infrastructure, runtime controls, and independent review hashes agree. This acceptance does not cover the six later results, any changed combined statement package, a complete Lean counterexample, or the separate unresolved universal linear-variance assertion. Final claims about the 31-result package must cite its own subsequent source-bound Linux evidence.
