# Draft pull request

**Title:** Claim solution to problem 606: sharp mixed wave observation time

**Base:** `MColbrook/AIM:main`

**Head:** `codex/606-optimal-observation-time`

**Requested state:** Draft.

**Author:** Marcus Webb, with assistance from OpenAI Codex.

## Proposed description

Problem 606 asks whether the mixed finite element wave scheme remains uniformly observable at every time greater than two for an arbitrary bounded nonnegative sampled potential. This contribution gives a complete candidate proof that its infimum observation time is two: a uniform estimate above two and exact discrete countersequences below two.

The target is problem 606 at commit `37a25361f243be77daea0ae0b3c5167b57f1b5f3`. See the [original target](https://github.com/MColbrook/AIM/blob/37a25361f243be77daea0ae0b3c5167b57f1b5f3/problems/606-mixed-wave-optimal-observation-time.md), [proof](PROOF.md), and [full-target comparison](README.md).

The main addition is a uniform asymptotic spectral-gap estimate from the mass–stiffness identity, combined with a direct finite-frequency insertion argument. The proof explicitly relies on Castro and Micu's published global separation and boundary-mode estimates. It retains the exact matrices, both observation terms, arbitrary specified point values, and all mesh sizes. It does not assert an endpoint estimate at time two.

This is **Solution claimed**, submitted as a resolution report. It adds the proof, pinned statement, source audit, review records and reproducible numerical diagnostics. No catalogue status change or renumbering is included.

The author of this contribution is Marcus Webb, with assistance from OpenAI Codex. Codex developed the argument and drafted the proof using a small adaptation of Stellar Colosseum. Two separate AI agents reviewed the complete pinned proof during the same preparation session and found no unresolved gap. Independent human review and formal verification remain outstanding; [review details](REVIEW.md) identify the exact revision and scope.

Validation: 48 spectral cases and the modal normalization checks passed; 120 Gramian and 10 wave-packet diagnostics were reproduced. These finite calculations support the derivation but do not prove the theorem. Repository and equation-rendering checks are recorded in [validation.txt](validation.txt).
