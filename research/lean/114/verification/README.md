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

Pending. An ordinary macOS build is not the repository's authoritative check. From a committed, unchanged checkout on a suitable non-root Linux runner:

```sh
tools/lean/bootstrap.sh /absolute/path/to/aim-lean-tools
tools/lean/selftest.sh /absolute/path/to/aim-lean-tools
tools/lean/verify.sh research/lean/114 /absolute/path/to/aim-lean-tools
```

The existing GitHub Actions workflow runs the pinned real sandbox, rejection controls, Comparator, and raw-kernel replay. Its eventual acceptance certifies only the three stated supporting results. It cannot supply the missing graph and probability theorems or promote AIM 114 to Lean verified.
