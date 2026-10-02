# Independent AI audit of AIM 606 proof

**Date:** 2026-10-02.

**Reviewer:** Codex agent `/root/scout_approximation`, acting as an independent AI reviewer of the proof constructed by `/root/scout_pde`. I did not construct the #606 argument. This is an AI-only mathematical review, not human peer review or formal proof verification.

**Reviewed artifact:** `research/solutions/606-mixed-wave-observation/PROOF.md`.

**SHA-256:** `4f8f8221548fc5c050ba95fe0a1aaea60173200e0a31014d402e92e700476135`.

**Target compared:** `research/solutions/606-mixed-wave-observation/statement.md`, preserving problem 606 from repository commit `37a25361f243be77daea0ae0b3c5167b57f1b5f3`.

**Finding:** I found no mathematical gap in the reviewed revision. The argument establishes the full stated threshold, including uniformity in every mesh and sharpness for every time below two. It correctly leaves the endpoint time itself undecided. I recommend retaining the conservative status **Solution claimed** pending external review.

## Scope and method

I reread the final manuscript from the matrix statement through both time directions, independently recalculated the estimates, and specifically attacked the newly added cosine-kernel Fourier argument and explicit counterexample sequence. This review was not inferred from my earlier approval of a shorter candidate. I also checked the imported results against the primary [published article](https://link.springer.com/article/10.1007/s00211-025-01489-0) and its [arXiv preprint](https://arxiv.org/pdf/2501.11352). Published numbering and normalization are consistent with the final note.

## Detailed checks

1. **Target and representative.** The matrices, energy, two observation channels, boundary conditions, and quantifiers match the archived statement. The pointwise supremum A is appropriate for the fixed bounded representative. The argument does not replace the sampled potential by its almost-everywhere equivalence class or assume convergence of its samples. Constants may depend on A and T but are independent of N. The remaining coarse meshes form a finite set.

2. **Published inputs.** Lemma 4 supplies the claimed orthonormal generalized eigenbasis. The signed frequencies in Theorem 9 are the ones used in the manuscript. Published equation (48) has the stated extra factor of square-root two in both normalized observation coefficients; absorbing its square into the modal constant is valid. Lemma 5, equation (31), implies the required uniform upper bound on q squared. The discrete estimates use bounded nonnegative sampled values; the separate continuity assumptions used for approximation convergence are not invoked. I checked these source hypotheses and identifications, without purporting to reprove the entire published article.

3. **Asymptotic gap.** The identity hI=M+(h squared/4)K is exact. Applying min–max after conjugation by M to the appropriate negative square root gives (3.1), with the same ordered index on both sides. Rationalization gives (3.2). The increasing derivative of the tangent gives the stated zero-potential gap. Subtracting the perturbation of the lower-index frequency, completing the square, and using h at most 1/(j+2) correctly give (3.3)–(3.4). The cutoff J depends only on A and gamma. Both same-sign tails and the gap between the two tails are covered.

4. **Cosine-kernel proof.** I recalculated the Fourier transform, including its sign and value at zero. The two-sided off-diagonal row bound is 4 alpha times the displayed series; the telescoping series equals two. Thus the lower Gram estimate is exactly 2/alpha minus 8 alpha/gamma squared, positive precisely in the required strict range. The chosen longer interval in the upper bound makes the weight at least 1/square-root two on the observed subinterval and satisfies the needed gap condition. The resulting constants do not depend on frequency count or location. No external Fourier theorem is silently needed.

5. **Finite insertion.** The shifted difference cancels the inserted coefficient. Integrating its squared norm gives the factor 8 epsilon in (4.4). The integral multiplier is uniformly positive for all frequency differences of magnitude at least g. Recovering the old coefficients, applying the uniform upper bound, and then recovering the new coefficient gives a strictly positive lower bound at each stage. The choice epsilon=(T-S)/(2m), with m=0 handled separately, covers every number of insertions at most m. Enlargement to T preserves the estimate.

6. **Observation above two.** The normalization in (5.1) makes the energy the sum of the squared signed coefficients: the cross terms cancel between displacement and velocity energy. Both boundary coefficient formulas are correct. Applying the scalar Fourier bound separately and adding gives (5.2). Nonzero first eigenvector components follow from the displayed recurrence. Finite exponential independence proves positive definiteness for every remaining coarse mesh, so no mesh is omitted.

7. **Explicit sharpness sequence.** On the whole observation interval, the distance on the period-two circle from t to t0 gives the claimed rho. Coefficient normalization costs at most square-root(m+1), and the coefficient l1 bound is correct. The prescribed integer mesh accommodates the entire block. On that block, the three frequency-error orders are respectively m to the minus six, minus two, and minus ten, yielding the stated total error. The trace perturbation is therefore of order m to the minus three-halves; the velocity observation is of order m to the minus seven-halves. The constructed solution is exact and nonzero. The energy lower bound is correctly oriented because q squared is uniformly bounded above. Both observations tend to zero while the energy stays bounded away from zero. Splitting real and imaginary parts gives the same obstruction for real solutions.

## Limitations of this review

This is a reasoning audit with primary-source checks. It is not a Lean verification, an independent human audit, or a claim to have exhausted the literature. No numerical experiment is used as a substitute for any universal step. I found no outstanding correction required in the proof revision identified above.
