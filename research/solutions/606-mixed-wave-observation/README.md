# Resolution report for the optimal mixed wave observation time

**Target:** AIM problem 606, [Optimal uniform observation time for mixed finite element waves](statement.md), at repository commit `37a25361f243be77daea0ae0b3c5167b57f1b5f3`.

**Status:** Solution claimed, awaiting independent mathematical review.

**Prepared:** 2 October 2026 by OpenAI Codex, with separate AI research and review agents in the same preparation session. No human review or proof-assistant verification is claimed.

The [proposed proof](PROOF.md) establishes

```math
T_*(a)=2
```

for every bounded nonnegative potential with the specified pointwise representative. It proves a mesh-independent observation inequality for every time greater than two and constructs solutions with observation-to-energy ratio tending to zero for every time less than two. The estimate at the single endpoint is not needed to determine the infimum and is not claimed.

The key calculation uses the exact identity between the mass and stiffness matrices to obtain a uniform lower bound on the gaps between high eigenfrequencies. A direct Fourier argument reinserts the finitely many low frequencies. The proof builds on the global spectral separation and boundary eigenvector estimates of Castro and Micu; it does not claim those published estimates as new results.

## Match to the full target

| Requirement in the pinned problem | Treatment in the proof |
| --- | --- |
| Exactly the stated mass, stiffness and sampled-potential matrices | Section 1 states the same matrices; Section 3 uses their exact identity. |
| Arbitrary bounded measurable nonnegative potential with fixed point values | The pointwise bound is used throughout; no continuity or convergence of sampled potentials is assumed. |
| Both boundary observation terms with their stated scaling | Sections 2 and 5 give the modal expansion and its energy normalization explicitly. |
| A constant independent of every mesh size | Sections 3–5 give uniform constants for fine meshes and handle the finitely many coarse meshes. |
| Determine the infimum observation time | Section 5 proves the upper bound and Section 6 proves failure at every smaller positive time. |

## Review and reproducibility

- [Full argument and mathematical dependencies](PROOF.md).
- [Source comparison and bounded literature search](SOURCE_AUDIT.md).
- [AI review record](REVIEW.md), identifying the reviewers and what they checked.
- [Research workflow](WORKFLOW.md), describing the adaptation of Stellar Colosseum.
- [Numerical diagnostics](check_606.py), [recorded results](results.json), and [validation log](validation.txt).
- [Original problem statement](statement.md), copied without changes from the pinned revision.

From the repository root, reproduce the optional numerical checks with Python 3.13 and the recorded dependency versions:

```sh
python3 -m venv /tmp/aim606-venv
/tmp/aim606-venv/bin/python -m pip install -r research/solutions/606-mixed-wave-observation/requirements.txt
/tmp/aim606-venv/bin/python research/solutions/606-mixed-wave-observation/check_606.py --output /tmp/aim606-results.json
python3 scripts/catalogue.py --check
```

The numerical checks test finite examples and normalization identities. They are not a certificate of the theorem, whose proof is analytic. The catalogue check validates repository structure and links, not mathematical correctness.

## Contribution scope

This is a resolution report for review under [CONTRIBUTING.md](../../../CONTRIBUTING.md). It supplies the problem ID and revision, a linked complete argument, a full-target comparison, and review disclosure. It adds a proof package only. It proposes no catalogue status change or renumbering during review; the existing problem page and metadata remain consistent. A later accepted status change should follow the repository's coordinated archival procedure.

A bounded human review can focus on the uniform tail-gap estimate in Section 3, the finite-insertion constants in Section 4, and the source assumptions in Section 2. A complete review should also check the explicit subcritical construction in Section 6. These checks have been performed by AI during preparation; external mathematical review remains outstanding.
