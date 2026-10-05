# Isolated Linux verification: 25 supporting results

The unmodified AIM workflow [passed](https://github.com/sidneyholden1/AIM/actions/runs/37362894274)
on Ubuntu 24.04 at immutable source revision `41c4f33f6a65ac8c9f6901bf1875e4420ee6f980`. This record
covers exactly the 25 declarations in [that revision's comparator configuration](https://github.com/sidneyholden1/AIM/blob/41c4f33f6a65ac8c9f6901bf1875e4420ee6f980/research/lean/114/comparator.json).
It does not certify later Length or GraphLengthBridge additions or the complete
counterexample. The run was executed in the submitter's fork; upstream PR
Actions remain subject to maintainer approval.

## Original evidence

| Archive | GitHub artifact ID | SHA-256 |
| --- | --- | --- |
| [lean-114.zip](lean-114.zip) | `11367338467` | `0011b7c752a10dc11a30ebed3daccb43941e664766bed59c3aeef78b6609a33f` |
| [lean-checker-controls.zip](lean-checker-controls.zip) | `11367871801` | `003674685f6459d4ed31bed15ddd042733c30bf96ddd137d5d62b199c85098d9` |

The downloaded ZIP digests match the retained [GitHub artifact metadata](github-artifacts.json).
[Run](github-run.json) and [job](github-jobs.json) metadata record completed
success for selection, checker controls, and project verification. Extracted
logs retain their original bytes.

The exact [source archive](source.tar.gz) contains all **204**
project inputs from the verified commit, under `source/`. Its SHA-256 is
`289308fab7eccbea43c8974311689420949a7788b569b852bb382a12f47eacea`. Every input digest in the verifier's manifest
was checked against the immutable Git source before archiving.

The [Comparator log](lean-114/verify-20261005T193404Z-4196/comparator.log) records separate Challenge and
Solution builds and exports, all 25 targets, and successful default-kernel
acceptance with exit zero. The [result manifest](lean-114/verify-20261005T193404Z-4196/result.json) records
all input hashes and actual locked tool receipts. Twenty-four declarations
use `propext`, `Classical.choice`, and `Quot.sound`; the parallel-edge theorem
uses only `propext` and `Quot.sound`.

The [sandbox probe](lean-114/verify-20261005T193404Z-4196/sandbox.log) exercises real build/export filesystem,
namespace, process, network, and capability restrictions. The
[kernel controls](lean-114/verify-20261005T193404Z-4196/kernel-controls.log) accept an honest fixture, reject
an invalid raw proof, and reject a quotient mismatch in the post-check.
[Comparator controls](lean-114/verify-20261005T193404Z-4196/comparator-controls.log) check statement/definition
and axiom failures; separate [sorry](lean-114/verify-20261005T193404Z-4196/negative-sorry.log) and
[native trust](lean-114/verify-20261005T193404Z-4196/negative-native.log) fixtures are rejected. The separate
checker-controls job also passes its own self-test.

## Audit and scope

The independent [operational audit](OPERATIONAL-REVIEW.md) accepts the evidence
for this exact 25-result revision, separately from mathematical proof reviews. No raw log or immutable source has been edited. Historical
25-result metadata misattributed implementation of the initial three proofs
to root; current metadata corrects that role to `lean_feasibility`, with root
as integrator. The original independent referees were `spectral_review` and
`probability_review`, so their independence and all mathematical bytes remain
unchanged.

The 25 results concern supporting graph, inertia, variance, mixture, and
transfer blocks. Mechanical acceptance supplies none of the still-unencoded
metric spectral theory, stable ratio law, or process limit. It does not
justify a whole-problem Lean-verified catalogue status.
