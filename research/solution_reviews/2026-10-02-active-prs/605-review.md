# Independent audit: AIM 605 (PR #17)

**Audit date:** 2026-10-02. **Reviewer:** OpenAI Codex, in a review session separate from submission preparation. This is an AI mathematical audit, not human peer review or formal verification.

**Pinned submission:** [PR #17](https://github.com/MColbrook/AIM/pull/17), head `ebe4b6bee4040cc0c0a83249cfedc1653380dac0`; package `research/solutions/606-mixed-wave-observation`. The original problem 606 at `37a25361f243be77daea0ae0b3c5167b57f1b5f3` is current [AIM 605](../../../problems/605-mixed-wave-optimal-observation-time.md). The problem statement, matrices, potential class, observation and energy match.

**Recommendation:** Accept the complete argument and mark AIM 605 **Solved**, retaining its existing ID and page. The proved result is the infimum of admissible observation times, equal to two. No conclusion at the endpoint time two is needed by the problem and none is claimed.

## Argument checked

The full proof was read and re-derived, including its quantitative Fourier lemmas. Submitted self-reviews were not treated as evidence of correctness.

1. The identity `h I = M_h + h^2 K_h/4` is exact. Combining it with `0 <= L_h <= A h I` gives the stated generalized-eigenvalue sandwich. The sine eigenvectors of the zero-potential pencil give frequencies `2 tan(pi j h/2)/h`. Rationalizing the upper sandwich gives both perturbation terms in (3.2), with the correct constants.
2. Subtracting the perturbed upper bound at index j from the unperturbed lower bound at j+1 gives (3.3). Completing the square in `pi tan(theta)^2 - (A h/4) tan(theta)` contributes `-A^2 h^2/(64 pi)`. Because `j < N`, replacing `h` by `1/(j+2)` is legitimate. Consequently the tail gap approaches pi uniformly over every mesh, including the high-frequency end. This uniformity is the key improvement over the published global positive gap.
3. The cosine-weight Fourier transform and its zero-frequency value are correct. Ordering a separated frequency set bounds each off-diagonal row by the telescoping series `sum 1/(n^2-1/4)=2`; the resulting lower constant is positive precisely for the sufficient condition `S > 2 pi/gamma`. The upper bound uses a larger cosine window which is at least `1/sqrt(2)` on the smaller interval.
4. In the finite-insertion lemma the translated difference cancels the inserted exponential. Integrating the existing lower bound over translations gives (4.4) with the factor `8 epsilon`. The separation excludes zero from the sinc argument, giving a strictly positive infimum. An upper Fourier bound controls the old sum, and the triangle inequality then controls the inserted coefficient. Thus constants depend on the number of inserted frequencies, the two gaps and the interval, never on the mesh or the absolute frequency locations.
5. Applying this lemma to the two signed spectral tails and finitely many central modes proves the required Fourier lower estimate for every time above two. The expansion in (5.1) has exactly unit-energy coefficients: positive/negative-frequency cross terms cancel between the potential and kinetic energies. Applying the scalar lower estimate separately to both observations and using the modal lower bound gives (5.2). For each of the finitely many remaining coarse meshes, a vanishing observation forces all exponential coefficients to vanish; the boundary component of every eigenvector is nonzero by the tridiagonal recurrence.
6. The short-time polynomial concentrates at the middle of the complementary arc of the period-two circle. The stated rho is the maximum modulus on the observation interval. The l1/l2 coefficient estimates and the block choice `J=(m+1)^2`, `h=(m+1)^(-6)` give frequency defects `O_A(m^(-2))`, first-observation error `O(m^(-3/2))`, and second observation `O(m^(-7/2))`. The upper modal estimate bounds q uniformly, so the exact constructed solutions have energy bounded away from zero. Ratios therefore tend to zero. Splitting into real and imaginary parts preserves the failure for real solutions.

There is no appeal to convergence of sampled potentials. A specified pointwise bounded representative, including arbitrary changes on a null set within its pointwise bound, is covered.

## Imported results and source comparison

The [published Castro--Micu article](https://link.springer.com/article/10.1007/s00211-025-01489-0) was inspected directly: condition (15), Lemmas 4 and 5, equation (31), Theorem 9, equation (48), and the end of Section 4. Its signed frequencies are the submitted positive and negative square roots; its modal observation coefficients have the extra `1/sqrt(2)` factor correctly accounted for in the submission. The finite-matrix estimates use a bound on sampled potential values. Replacing the source's notation for the potential norm by the submission's pointwise supremum supplies that bound. Continuity is an additional assumption in the source's separate convergence theorem, not in the spectral statements used here.

Bibliographic metadata agree with the publisher: C. Castro and S. Micu, *Numerische Mathematik* 157 (2025), 1847--1895, DOI `10.1007/s00211-025-01489-0`; [arXiv 2501.11352](https://arxiv.org/abs/2501.11352) is the corresponding preprint. The source still states the optimal-time question after Theorem 1 and in Remark 15. Ingham is historical attribution; all Fourier estimates used in the submission are proved inside the submission, so there is no unchecked external Fourier theorem application.

## Reproduction and integrity

The pinned package was exported with `git show` without checking out or modifying the PR. Its 13 manifest entries all match their SHA-256 values. After inspection, the submitted diagnostic script was run using Python 3.12.14, bundled NumPy and isolated SciPy 1.18.1:

```text
python -B check_606.py --output ../605-reproduced-results.json
PASS: 48 spectral cases; modal/Gram normalization checked.
Computed 120 full-observation Gram minima and 10 packet diagnostics.
```

The full output is [605-numerical-checks.json](605-numerical-checks.json). The relative discrepancy between the analytic observation Gram matrix and direct time quadrature is `2.643131059262157e-10`. At time one, the finite packet ratios decrease from `0.15130` to `0.006748` for zero potential and from `0.13184` to `0.006730` for the step potential, as m runs from two to six. These are diagnostics; the all-mesh and asymptotic conclusions rest on the analytic argument above.

| Pinned file | SHA-256 |
| --- | --- |
| `PROOF.md` | `e76ed45199c8ab49ea9b4b69f2101dc0bf50f972ece67f2c449dbfd90d76a7de` |
| `statement.md` | `307372e49be8c007dd20df7ecd107b0585beb3d081ecedcc254120eaa7c082cd` |
| `SHA256SUMS` | `46c9f97b88becc0ab3ee0f57848d5eb23b7f0827a817443089026b8c8c16786d` |

No unresolved mathematical gap was found. The result remains an independently AI-audited argument relying on the cited published spectral estimates; it has not been checked in a proof assistant or by a human referee in this audit.
