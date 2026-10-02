# Review record for the proposed observation time solution

**Date:** 2026-10-02. **Evidence status:** Solution claimed, awaiting external mathematical review.

The reviewed [proof](PROOF.md) has SHA-256

```text
4f8f8221548fc5c050ba95fe0a1aaea60173200e0a31014d402e92e700476135
```

All reviews below concern that complete revision and the [pinned statement](statement.md), problem 606 at `37a25361f243be77daea0ae0b3c5167b57f1b5f3`.

## Reviewers and scope

The argument was developed by the primary Codex agent and a PDE research agent. Two other Codex agents then reviewed the completed argument separately. All agents ran in the same collaborative preparation session. These are distinct AI checks, not an external human audit, proof-assistant verification, or a claim to satisfy the repository's criteria for a **Solved** badge.

| Reviewer | Recorded review | Scope and conclusion |
| --- | --- | --- |
| Codex `scout_approximation` | [Complete review](reviews/approximation.md) | Independently recalculated all proof sections and checked the source hypotheses and normalization. Found no mathematical gap in the identified revision. |
| Codex `scout_algebra` | [Complete review](reviews/algebra.md) | Checked the full target, matrix inequalities, Fourier bounds, insertion constants, both time directions and coarse meshes. Found no unresolved mathematical objection. Also authored the separate numerical diagnostics. |
| Primary Codex agent | This record and integrated proof | Independently derived the gap calculation, supplied the direct cosine-kernel bounds and explicit sequence used in the final manuscript, checked the completed argument, and reproduced the numerical diagnostics. This is author self-review. |

The linked reviewer records are preserved as written by the reviewers. Each identifies its own scope and limits. They check the use of published results; they do not claim to reprove the entire Castro–Micu paper.

## Questions specifically tested

The high-frequency perturbation is not bounded in the ordinary mass-normalized operator norm. The proof instead uses a quadratic-form comparison and completes a square, retaining control at the highest discrete frequencies. The finite-insertion proof retains the uniform upper Fourier bound needed to recover each new coefficient. A bound growing with the number of modes would not suffice.

The sharpness construction uses exact discrete solutions, with all denominators justified by the tridiagonal recurrence. It uses only bounded pointwise samples and does not import the continuity assumptions needed for convergence to a continuous PDE. The upper bound explicitly covers the finitely many coarse meshes. Both directions address the infimum in the target; the endpoint remains outside the claim.

## Computational evidence

The primary agent reran [check_606.py](check_606.py) independently after inspecting its implementation. Its output matched [results.json](results.json) exactly. The run tests 48 spectral cases and the energy and observation normalizations, then computes 120 Gramian diagnostics and 10 wave-packet diagnostics. These finite, floating-point calculations are supporting checks only.

See [validation.txt](validation.txt) for execution, version, repository and mathematics-rendering records. The proof is analytic and does not depend on any floating-point result.

## Outstanding review

No unresolved mathematical objection was found by the AI reviewers. Human or other external mathematical review and any formal verification remain outstanding. The [source audit](SOURCE_AUDIT.md) records the limits of the later-result search, including an adjacent announced manuscript whose full text was not inspected. No priority claim is made.
