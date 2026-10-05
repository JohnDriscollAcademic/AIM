# Verification record: supporting results only

Date: 2026-10-05. The current package advertises eleven supporting results,
not the full AIM 114 counterexample. [NUMERICAL_TARGETS.md](../NUMERICAL_TARGETS.md)
identifies the exact scope and remaining gaps.

## Expanded local checks

The initial three statements and each extension had two independent boundary
approvals and successful typechecks before proofs. [TransferChallenge.lean](../TransferChallenge.lean)
and [MixtureChallenge.lean](../MixtureChallenge.lean) retain the frozen extension
signatures. Their intentional placeholders are never imported by Solution.

The combined `lake build Challenge Solution` passes with eleven declarations.
Each uses exactly `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`,
custom axiom, or native-execution axiom supports Solution.

| Extension | Author's local evidence | Independent reviews and distinct logs |
| --- | --- | --- |
| Prescribed-length transfer | [Build](transfer-build.log), [fresh elaboration](transfer-reelaboration.log), [axioms](transfer-axioms.log), [hashes](transfer-source-sha256.json) | [Referee 1](../reviews/transfer-proof-referee-1.md), [referee 2](../reviews/transfer-proof-referee-2.md) |
| Actual Gaussian mixture | [Build](mixture-build.log), [fresh elaboration](mixture-reelaboration.log), [axioms](mixture-axioms.log), [hashes](mixture-source-sha256.json) | [Referee 1](../reviews/mixture-proof-referee-1.md), [referee 2](../reviews/mixture-proof-referee-2.md) |

A new isolated Linux run is required for the enlarged theorem set. The
historical successful run below does not certify any extension added later.

## Historical initial-three-result checks

The original local [build](build.log), [fresh elaboration](proof-reelaboration.log),
[axiom report](axioms.log), and [source hashes](local-source-sha256.json) record
the first three declarations. Both original [referee 1](../reviews/proof-referee-1.md)
and [referee 2](../reviews/proof-referee-2.md) independently checked that initial
source. These retained records precede the extensions; the current combined
Challenge and scope documents have grown since those hashes were fixed.

[GitHub Actions run 37344385173](https://github.com/sidneyholden1/AIM/actions/runs/37344385173)
passed the unmodified AIM workflow on Ubuntu 24.04 at immutable revision
`4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`. It accepted the initial three
declarations using real isolation, separate Challenge/Solution builds,
Comparator statement and axiom checks, default-kernel replay, and rejection
controls. The [original Linux evidence](linux-2026-10-05/README.md) retains
both original ZIPs, their extracted logs and tool receipts, the exact verified
source archive and input hashes, and the independent operational audit.

That execution took place in the submitting user's fork. Upstream PR Actions
remain subject to maintainer approval. Neither local builds nor referee
approval substitute for an isolated run. To reproduce a committed project on
a suitable non-root Linux runner:

```sh
tools/lean/bootstrap.sh /absolute/path/to/aim-lean-tools
tools/lean/selftest.sh /absolute/path/to/aim-lean-tools
tools/lean/verify.sh research/lean/114 /absolute/path/to/aim-lean-tools
```

Mechanical acceptance covers only the declarations present at its recorded
revision. It cannot supply unencoded spectral or probabilistic links or
promote the complete AIM 114 counterexample to Lean verified.
