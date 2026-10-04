# AIM 505: target comparison and review

Contributor: **Siavash Sadeghi**. Reviewer: **Codex (AI)**. Date: 4 October 2026.

Target: [entry 505](https://github.com/MColbrook/AIM/blob/59a8f0c2957dd272f56bcf282dfe0c066a15f441/problems/505-upwind-discrete-aronson-benilan.md), commit `59a8f0c2957dd272f56bcf282dfe0c066a15f441`. Evidence: [paper](aim505_report.pdf), [source](aim505_report.tex), [target snapshot](TARGET_SNAPSHOT.md).

## Conclusion and limits

The uniform estimate fails with fixed data bounds and G(p)=1-p. The proof selects gamma after the mesh; the numerical experiments are corroboration, not a uniform choice of gamma.

Classification proposed for review: **Solution claimed; awaiting independent review**. This PR is a research submission, not an assertion of independent validation.

## Mathematical review

The analytic argument matches all four uniform initial-data bounds and the reflected endpoint stencil. The fixed-mesh implicit-function limit is used before choosing the mesh-dependent exponent. The comparison argument controls exterior influx with endpoint half-weights; a separate derivative estimate justifies the limit of gamma*w.

## Changes and checks

Separated the relevant proof and bibliography from the supplied combined note; added the requested contributor name, explicit target definitions, pinned repository references and reproducibility documentation. The mathematical construction and intended scope are preserved.

Repeated all four supplied meshes (10, 20, 40, 80); displayed numerical values agree with the original table. Added rejection of nonfinite or nonphysical accepted trajectories and strict JSON serialization. The numerical choice gamma=500*M is not the proof of the diagonal sequence.

The paper compiles in two passes with the existing MiKTeX installation. Every final PDF page was visually inspected. The built-in compiler failed because its platform directories were unavailable; this did not prevent the independently compiled PDF from being checked.

The original package, original scripts and original numerical outputs remain preserved outside this submission. No independent human or formal proof audit was performed.
