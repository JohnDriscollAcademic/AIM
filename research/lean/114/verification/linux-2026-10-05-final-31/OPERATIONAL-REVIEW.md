# Independent operational review: final Linux verification of 31 supporting results

- **Reviewer:** `probability_review`, independent OpenAI Codex AI referee; not the package integrator or Linux-run operator.
- **Review date:** 2026-10-05.
- **Verdict:** **ACCEPT** the retained evidence as a successful authoritative Linux Comparator/default-kernel run for the exact 31 selected supporting declarations at commit `56afd77d2456af3da7934947699ee86735494010`.
- **Scope:** all eight reviewed supporting blocks, including the three Length results and three GraphLengthBridge results. This is not an end-to-end formalization of the spectral counterexample or a resolution of the separate universal linear-variance assertion.

I independently inspected the retained evidence and checked its source and artifact identities. I did not rerun the Linux checker on this Mac, and make no such claim. Original ZIPs, raw logs, retained metadata, and the source archive were left unchanged. My new cross-check record is [OPERATIONAL-CHECKS.json](OPERATIONAL-CHECKS.json).

## Run and artifact provenance

The [final GitHub Actions run](https://github.com/sidneyholden1/AIM/actions/runs/37365344243), run `37365344243`, attempt 1, is a successful completed `workflow_dispatch` run on the contributor's fork `sidneyholden1/AIM`, using exact source commit `56afd77d2456af3da7934947699ee86735494010`. I independently queried the live GitHub run API using `gh api`, and its identity, head SHA, status, conclusion, event, and attempt agree with the retained run metadata. The retained job records show all steps successful in `select`, `checker-controls`, and `verify (114, research/lean/114)` on `ubuntu-24.04`. This does not assert an upstream maintainer's review or approval.

I recomputed both original ZIP SHA-256 digests and checked them against the retained summary and artifact metadata and a fresh live GitHub artifact API response:

| Original artifact | Artifact ID | SHA-256 |
|---|---|---|
| `lean-114.zip` | `11368511818` | `a5ac1a395a6094e28d3d675c5c541739de0a58c353583893d72acb729171b3ba` |
| `lean-checker-controls.zip` | `11368063043` | `c201dae5aa511ece91ffb2d132a8dad773a1f712f3b4ca8da12f0c7482ade3b3` |

Both ZIP integrity checks passed. Every extracted file matches its original member: 13 files in the project-verification archive and 10 in the checker-control archive. Both artifact records bind to the same run and source SHA. The retained source archive has SHA-256 `ee357a709802b3162f8a8de782fb7dcec5da72bcc5a5beb135f9d0de5e0dbc4f`, matching `evidence-summary.json`.

## All 306 input files and the exact combined boundary

The [verifier result](lean-114/verify-20261005T195646Z-3965/result.json) has SHA-256 `1e2f910877632299e6a457f3e53ce3de0ce86e07ccdd946118108e8fee089f03`. It records 306 input hashes and exactly 31 theorem names. For every recorded input, I compared its bytes and hash with both the corresponding member of `source.tar.gz` and the immutable Git blob from `git show 56afd77d2456af3da7934947699ee86735494010:research/lean/114/<path>`. All match. The recorded path set, archive-member set, and complete tracked project-file set at the commit coincide; no omitted or extra input was found.

The immutable `comparator.json` is exactly the config recorded in the result. It selects distinct `Challenge` and `Solution` modules, 31 unique theorem names, no definition holes, and only the three standard permitted axioms. I also independently compared the combined Challenge signatures after whitespace normalization: the first 25 are unchanged from the prior verified 25-result commit, and the additional six exactly match their separately approved `LengthChallenge.lean` and `GraphLengthBridgeChallenge.lean` boundaries. This source comparison supplements the actual Comparator check; it does not replace it.

All current mathematical sources, individual and combined Challenge files, Solution, comparator config, Lakefile, dependency manifest, and Lean toolchain matched this run's input hashes at audit time. Administrative report changes described below do not alter those files.

## Infrastructure, toolchain, and fresh preparation

The verification workflow, harness, source lock, bootstrap/verify/selftest wrappers, and CI Lean toolchain are byte-identical at the final source commit, the prior 25-result commit `41c4f33f6a65ac8c9f6901bf1875e4420ee6f980`, the original verified three-result commit `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`, and the current inspected checkout. Their exact hashes are recorded in my checks JSON. No verification gate or allowed axiom set was weakened for the expanded package.

The source-lock hash is `b3833b07916e5db77579b9cc53ca582282f6a841f36d6a60d693e5b02d342b6b`, and the locked tooling commit is Forsythe `8d1b0c0545a77b40245e84705aa7d273e6c81e62`. Both final-run job receipts agree exactly, and they also agree with the previously audited 25-result tool receipt, including hashes of the actual Comparator, exporter, Landrun executable, environment, and derived sandbox probe. Lean is `4.33.1` on Linux x86-64, with Go `1.27.1`. The actual project manifest pins Mathlib to `0df444a360eaa60ab8c11dca51a86af692955474` and LeanCert to `621a43d7cf21f87872392a01e874f2f1dbddc926`. Dependency and Mathlib cache logs finish successfully.

I previously read and hash-checked the exact pinned Comparator main, comparison, axiom, and strict-sandbox sources during the 25-result operational audit; the source lock and receipts are unchanged. I also inspected the unchanged harness's fresh snapshot and verification paths. It copies ordinary tracked Git blobs into a fresh directory, rejects symlinks and tracked compiled artifacts, materializes locked dependencies, obtains the trusted cache, and checks unchanged input hashes before and after Comparator. The final log records the new fresh project directory `nla-fresh-proof-7i6lu5li/project`. No submitted Solution build precedes Comparator in that directory.

## Separate environments, real comparison, and kernel acceptance

The [actual project log](lean-114/verify-20261005T195646Z-3965/comparator.log) shows Challenge built and exported first, followed by Solution built and exported separately. Challenge produces exactly the expected 31 deliberate placeholder warnings. Solution builds all eight proof modules, including Length and GraphLengthBridge, without a placeholder warning. Independently computed immutable local import closures confirm that Solution imports no Challenge and Challenge imports no proof module. Shared definition imports are intentional.

The pinned Comparator compares declaration kinds and signatures, recursively compares relevant definitions, checks the solution's transitive axiom closure, and replays its exported declarations in a newly empty Lean default-kernel environment with explicit quotient post-checks. The actual final-run log ends with:

```text
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
EXIT_STATUS=0
```

The result is `comparator-accepted`. This is evidence of actual statement comparison and kernel replay, not merely a successful ordinary Lake build. No external kernel or Nanoda result is claimed.

I independently parsed every printed axiom list and matched the declaration names exactly with the selected 31. `counterexample_parallel_edges` uses exactly `propext` and `Quot.sound`; the other 30 use exactly `propext`, `Classical.choice`, and `Quot.sound`. No extra, `sorryAx`, or native-computation axiom appears. The full per-declaration sets are retained in my checks JSON.

## Runtime isolation and positive/negative controls

Both the standalone checker job and this actual final project-verification job contain successful complete control sets. I inspected the actual final project's logs and checked required outputs in all six control logs in both jobs.

The [sandbox log](lean-114/verify-20261005T195646Z-3965/sandbox.log) demonstrates private user, PID, mount, network, IPC, and UTS namespaces; an absent host parent and denied signal lookup; denied host-loopback access and AF_UNIX socket creation; dropped capabilities; and `no_new_privs`. Outside-file writes, truncation, creation, and a symlink write through `.lake` are denied. Only the designated build `.lake` is writable. Export `.lake` writes and truncation are denied. A nested-namespace write attempt is rejected, and unsupported options or unauthorized writable paths fail closed. The probe confirms its outside/export fixtures unchanged.

This uses the real pinned Bubblewrap/Landrun adapter and the surrounding AF_UNIX-restricted systemd service. The runtime checks support the specified isolation properties; they are not a host-file confidentiality claim, because the sandbox permits host-readable files.

The [default-kernel controls](lean-114/verify-20261005T195646Z-3965/kernel-controls.log) accept an honest inductive/quotient fixture, reject an invalid raw proof through the actual kernel, and reject a quotient-constant mismatch in the post-check. The [Comparator regressions](lean-114/verify-20261005T195646Z-3965/comparator-controls.log) accept the honest match and reject the four mismatch/extra-axiom fixtures, including a changed theorem type. The dedicated [`sorry` control](lean-114/verify-20261005T195646Z-3965/negative-sorry.log) rejects `sorryAx`; the [native control](lean-114/verify-20261005T195646Z-3965/negative-native.log) rejects `checked._native.native_decide.ax_1_1`. Both return the expected exit status one and exact illegal-axiom messages. These are expected successful rejection tests, not failures of the proof run.

## Both independent reviews bind all eight checked proof modules

For each checked proof module I verified that its input hash occurs in both independent final referee reports in the immutable source and in the current report copies. The complete path-to-report mapping is in `OPERATIONAL-CHECKS.json`.

| Proof module | Checked SHA-256 |
|---|---|
| `Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` |
| `TransferProof.lean` | `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c` |
| `MixtureProof.lean` | `2a5d65beeeb576efad8eaf9940ebe0b5cd81cd52e402807e004444ca2e9e6bcf` |
| `InertiaProof.lean` | `d0acd2dfda515f792ca12195be04b1b07d0ca76e75e7cb20b1afd0e09e06345d` |
| `VarianceProof.lean` | `3a160951c60be915a49a2b9dedb1495e76e6f35007339ab7f30d03901e33e6c2` |
| `GraphProof.lean` | `75232119b42e3cffb5829d959fc38842acc1381eeb409da33d9baef9faae95ea` |
| `LengthProof.lean` | `025f80e283f7b7b0a54ee74b55b45c234820b9ab0fa7b9ed828954268f650509` |
| `GraphLengthBridgeProof.lean` | `bf60f07bc4ddb86274f7a7098709db825e15b47390e2966ba4b376c453922aea` |

This binds the operational result to the exact independently reviewed mathematical implementations. The result appropriately says that the verifier itself did not perform semantic review; source correspondence is supplied by the separate reports. Mathematical authorship remains Sidney Holden's, with generated implementation and AI review separately identified.

## Historical administrative files and final disposition

The immutable final-run source includes an earlier snapshot of the historical 25-result `OPERATIONAL-CHECKS.json`, taken while that historical audit was in progress. Its checked hash is `025ed834d67bab0553f206cd6c69d4951caf30a39081b89e912951f20ac5e4c1`. The later completed administrative copy has hash `64c6363ff1d37ef9423b704befb4c2ca4f8608dfcd0a829972f44d7b616adc6d`, and its completed report was added later. I explicitly checked the archived version against the final run's recorded input; I did not substitute the later copy. Neither the historical audit JSON nor its later report is a Lean mathematical dependency. All actual mathematical inputs remain identical to those checked in this run.

The final source metadata also correctly attributes the initial three implementations to `lean_feasibility`, with root as integrator. That corrects the older 25-result metadata without altering proof bytes or the independent referee assignments.

**No blocking operational finding was found.** This evidence completes the operational verification gate for the exact 31 supporting results at the stated source commit. Administrative documentation and status updates may accurately report that scope and immutable run. They must retain the package's partial status: the Kirchhoff spectral reduction, spectral-law/module-law identification, stable response-ratio construction, and empirical-process/random-evaluation limit remain unformalized, and the separate universal variance question remains open.
