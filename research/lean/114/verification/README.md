# Verification record: supporting lemmas only

Date: 2026-10-05. This package formalizes three supporting steps, **not** the full AIM 114 counterexample. The unformalized links are listed in [NUMERICAL_TARGETS.md](../NUMERICAL_TARGETS.md).

## Local checks completed

Lean 4.33.1 on local macOS successfully built the frozen Challenge before proof implementation. Both independent statement reviews approved the exact source bytes before proofs were written. The Challenge's three `sorry` placeholders are intentional statements, not proofs, and are never imported by Solution.

After implementation, these commands passed:

```sh
lake build Challenge Solution
lake env lean AIM/P114/Proof.lean
lake env lean Solution.lean
```

The [build log](build.log), [fresh re-elaboration](proof-reelaboration.log), and [axiom report](axioms.log) are retained. Each of `AIM.P114.module_count_identity`, `AIM.P114.sign_second_moment`, and `AIM.P114.variance_mixture_kurtosis` has exactly these transitive axioms: `propext`, `Classical.choice`, `Quot.sound`. No `sorryAx`, custom axiom, or native-execution axiom supports them.

Both [final referee 1](../reviews/proof-referee-1.md) and [final referee 2](../reviews/proof-referee-2.md) separately built Solution, freshly elaborated Proof, and printed its axioms. Their distinct logs are retained in this directory. They also checked fidelity to the frozen signatures, proof structure, reuse, attribution, and the partial scope.

[local-source-sha256.json](local-source-sha256.json) fixes the mathematical files and dependency configuration. The Proof SHA-256 is `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797`; the Solution SHA-256 is `40cecf7e29a88f5756d10385648ca2fee0b33da8124c1d31bdde08b52321f0b4`.

## Isolated Linux check

**Passed for all three supporting declarations.** [GitHub Actions run 37344385173](https://github.com/sidneyholden1/AIM/actions/runs/37344385173) used the existing unmodified AIM workflow on Ubuntu 24.04 at immutable revision `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`. The run completed on 2026-10-05 with success for project selection/metadata tests, checker controls, and project verification.

The [retained Linux evidence](linux-2026-10-05/README.md) includes both original artifact ZIPs with API-matched hashes, extracted logs, the tool receipt, and the project input hash manifest. The actual Comparator log reports statement/axiom acceptance and default-kernel acceptance of Solution. The controls cover sandbox restrictions, invalid raw proofs, statement/definition mismatch, custom axioms, `sorryAx`, and native-execution trust. Both source and configuration match the reviewed mathematical boundary.

This was remote execution in the submitting user's fork, followed by local inspection of the original logs. The upstream PR's own workflow requires maintainer approval. An ordinary macOS build is not substituted for the Linux result. To reproduce from that committed revision on a suitable non-root Linux runner:

```sh
tools/lean/bootstrap.sh /absolute/path/to/aim-lean-tools
tools/lean/selftest.sh /absolute/path/to/aim-lean-tools
tools/lean/verify.sh research/lean/114 /absolute/path/to/aim-lean-tools
```

Acceptance certifies only the three stated supporting results. It cannot supply the missing graph and probability theorems or promote AIM 114 to Lean verified. Later commits record evidence and documentation; the immutable proof revision above is the run's exact input.
