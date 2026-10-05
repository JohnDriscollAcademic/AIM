# Isolated Linux verification: final 31 supporting results

The unmodified AIM workflow [passed on 2026-10-05](https://github.com/sidneyholden1/AIM/actions/runs/37365344243)
on Ubuntu 24.04 at immutable source revision `56afd77d2456af3da7934947699ee86735494010`. It certifies exactly
the **31 supporting declarations** in [that revision's Comparator configuration](https://github.com/sidneyholden1/AIM/blob/56afd77d2456af3da7934947699ee86735494010/research/lean/114/comparator.json).
It does not formalize the complete graph spectral counterexample or settle
the separate universal variance assertion.

## Original artifacts and exact source

| Archive | GitHub artifact ID | SHA-256 |
| --- | --- | --- |
| [lean-114.zip](lean-114.zip) | `11368511818` | `a5ac1a395a6094e28d3d675c5c541739de0a58c353583893d72acb729171b3ba` |
| [lean-checker-controls.zip](lean-checker-controls.zip) | `11368063043` | `c201dae5aa511ece91ffb2d132a8dad773a1f712f3b4ca8da12f0c7482ade3b3` |

Both original ZIP hashes match the digests in [GitHub artifact metadata](github-artifacts.json).
The retained [run](github-run.json) and [job](github-jobs.json) metadata identify
the exact successful revision and all three successful jobs. The extracted
logs retain their original bytes.

The [source archive](source.tar.gz) contains all **306 project inputs**
from that exact commit under `source/`. Its SHA-256 is
`ee357a709802b3162f8a8de782fb7dcec5da72bcc5a5beb135f9d0de5e0dbc4f`. Every input digest was checked against the
immutable Git source and the verifier's manifest. The original manuscript
and problem-statement hashes remain recorded in the source package; no
mathematical target or proof source was changed to obtain this result.

## Actual mechanical checks

The [Comparator log](lean-114/verify-20261005T195646Z-3965/comparator.log) records separate Challenge and
Solution builds and exports, all 31 target declarations, and actual default-kernel
acceptance with exit status zero. The [result/input manifest](lean-114/verify-20261005T195646Z-3965/result.json)
records every input hash, the permitted axiom policy, the pinned source lock,
Lean 4.33.1 compiler revision, and actual checker/exporter/sandbox binary receipts.
The parallel-edge theorem uses only `propext` and `Quot.sound`; all other 30
use those plus `Classical.choice`. No placeholder, custom axiom, or native
execution axiom supports an accepted theorem.

The [sandbox probe](lean-114/verify-20261005T195646Z-3965/sandbox.log) exercises actual build/export restrictions
on filesystem writes, namespaces, process visibility, networking, capabilities,
and privilege acquisition. The [kernel controls](lean-114/verify-20261005T195646Z-3965/kernel-controls.log)
accept an honest inductive/quotient fixture, reject an invalid raw proof,
and reject a mismatched quotient in the post-check. The
[Comparator controls](lean-114/verify-20261005T195646Z-3965/comparator-controls.log) exercise statement,
definition, and axiom failures. The separate [sorry](lean-114/verify-20261005T195646Z-3965/negative-sorry.log)
and [native trust](lean-114/verify-20261005T195646Z-3965/negative-native.log) fixtures fail as required.
The checker-controls job independently passes its own self-test.

## Independent audit and remaining scope

The independent [operational audit](OPERATIONAL-REVIEW.md) accepts the evidence
for this exact revision, separately from the mathematical statement/proof reviews. Those earlier reviews and the [31-result integration
audit](../../reviews/integration-audit-31.md) bind the frozen mathematical files;
this Linux run supplies the separate isolation/export/kernel gate.

The run took place in the submitting user's fork using the unchanged workflow
and verifier. Upstream pull-request Actions remain subject to maintainer
approval. Later verification records and administrative status text do not
change the recorded source revision or its checked Lean statements, definitions,
proofs, Comparator configuration, or dependency pins. The historical
[25-result](../linux-2026-10-05-expanded-25/README.md) and
[3-result](../linux-2026-10-05/README.md) evidence is retained separately.
The final 25-result operational audit was completed after this 31-result proof
commit; its added checks/report are later administrative evidence, not changed
mathematical inputs.

The exact [remaining gaps](../../NUMERICAL_TARGETS.md) include the compact
metric-graph operator and spectral-to-phase identification, the stable response
ratio and its support/zero-atom properties, process convergence, random
evaluation, and identification of the actual graph limit with the proved
non-Gaussian mixture. Kernel acceptance of these supporting results supplies
none of those unencoded links. The catalogue remains PARTIAL.
