# Research workflow for the observation time solution

**Author of the contribution:** Marcus Webb, with assistance from OpenAI Codex. The account below records the AI assistance used to develop, draft, and check the proof.

This session adapted the research workflow in H. Lin, D. P. Woodruff, Y. Deng, J. Mao, S. Zuo and V. Mirrokni, [Stellar Colosseum](https://arxiv.org/html/2609.15983v2), especially Sections 3–4. The user supplied a three-hour budget on 2 October 2026. The run used at most four concurrent Codex agents. It was a small adaptation of the paper's workflow, not an execution of its released harness or its full population and random aggregation configurations.

## Exploration and choice

Three parallel searches examined approximation, numerical PDE, and algebraic targets from the repository's numerical-analysis group. The primary agent also considered the fixed-grid Aronson–Bénilan problem. Each search was asked for a precise target, a concrete strategy, a falsifiable key claim, and any obstruction.

The PDE search identified problem 606 as a full-target opportunity. The matrix identity yielded an explicit gap estimate; the remaining tasks were uniform reinsertion of low modes and sharpness below time two. This was the readiness decision: all remaining steps had precise statements and a stable dependency structure.

The approximation search found a separate proposed result for the cubic part of problem 642. That target also contains unresolved quartic assertions, so it was not selected for this contribution. No result for problem 642 is claimed by this package. Other exploratory directions did not produce an argument selected for full verification.

## Construction and falsification

The argument was divided into the matrix comparison, Fourier estimates, finite frequency insertion, observation normalization, and a construction below the proposed threshold. The primary agent and the PDE agent developed the main argument. Two other agents separately attacked its assumptions and calculations; one also built numerical diagnostics.

The review specifically tested the high end of the discrete spectrum, uniformity in the number of modes, arbitrary bounded pointwise sampling, coarse meshes, nonzero boundary components, and the orientation of the energy estimate. It identified the need to retain a uniform upper Fourier bound when recovering each inserted coefficient. The completed proof includes that bound and its direct proof. It also gives an explicit sequence of concentrating wave packets, avoiding an unproved passage to a continuous sampled potential.

## Evidence and final disposition

The final contribution separates published input theorems, the proposed deduction, analytic sharpness, finite numerical diagnostics, and reviewer conclusions. See [REVIEW.md](REVIEW.md) for the final proof revision and review scope. The result is submitted as **Solution claimed**, with external mathematical review still outstanding.
