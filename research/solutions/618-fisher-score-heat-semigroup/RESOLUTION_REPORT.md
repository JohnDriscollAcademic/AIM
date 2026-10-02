# Pre-submission check: original AIM 618, current AIM 665

**Date:** 2026-10-02.

**Checked by:** OpenAI Codex (AI), in the same session as editorial packaging. This is a pre-submission mathematical and reference check, not the repository's independent acceptance review.

**Submission:** An additional heat-semigroup proof, supplied as `aim618_solution.tex`, with author Matthew J. Colbrook as requested. The original file is preserved in [submission-original/](submission-original/aim618_solution.tex); [SUBMISSION.json](SUBMISSION.json) records its hash and both catalogue identities.

**Result of this check:** No unresolved mathematical step was identified in the complete supplied argument after checking its analytic input and scope. The new proof remains a solution claim pending pull-request review. The existing Solved decision for [AIM 665](../../resolved/665-fisher-score-gradient-closure.md), based on a different proof, is unchanged.

## Target comparison

The theorem uses the same smooth compact Riemannian manifold, nonnegative probability density and finite square-root Sobolev energy as the [pinned original statement](statement.md). It establishes convergence in the original density's weighted vector-field space, rather than a space weighted by the smoothed density. Smoothness up to the boundary is stronger than the requested continuously differentiable potentials.

No positivity, boundedness or convexity assumption is added. The additive heat-time shift makes the logarithm legitimate on zero-mass components and vacuum regions. The constructed potentials have zero normal derivative, which is permitted by the target; the original density needs no boundary condition. A compact manifold has finitely many connected components, so geometric constants can be chosen uniformly. In dimension zero both the score and gradients vanish.

## Argument checked

1. Strong smooth approximation of the square root in the Sobolev space gives the density's weak integrable gradient by the product calculation written in the manuscript. Sobolev locality on the zero set gives the score identity and its exact squared norm, equal to the Fisher information. The proof does not assume a Sobolev logarithm of the original density.
2. At every fixed positive heat time, the regularized density is smooth up to the boundary and the shifted density is uniformly positive. Its logarithm is smooth and satisfies the Neumann condition, so it belongs to the Laplacian's operator domain. The outer heat flow has the same boundary condition. All pairings with the original integrable density are finite.
3. Both integrations by parts in the mixed-product calculation have zero boundary terms: the first uses the outer potential's Neumann condition, and the second uses the logarithm's Neumann condition. Commutation is applied to the logarithm in the operator domain. Kernel symmetry supplies self-adjointness in the integrable-density/bounded-test-function pairing.
4. Sturm's Theorem 1.1(iii), with exponent two and its estimate squared, gives the stated short-time factor. Remark 1.2 makes the constant uniform over input functions, including the time-dependent logarithm used here. Casteras, Flaim and Monsaingeon's Section 3 explicitly states this squared estimate in the same smooth compact geometry. The factor tends to one even for nonconvex boundaries.
5. The exact mixed product is the regularized Fisher-type energy. The gradient estimate bounds the outer potential's norm, weighted by the original density, by that energy times the short-time factor. Cauchy-Schwarz then bounds the regularized energy by the original Fisher information times the factor. Division is used only when that energy is positive; the zero-energy case is handled separately.
6. Strong continuity in the integrable-function space and the square-root inequality give strong square-root convergence in the unweighted square-integrable space. The preceding energy bound gives Sobolev boundedness. Weak lower semicontinuity gives the lower energy limit, while the short-time factor gives the upper limit. Thus the regularized energy converges to the original Fisher information without a circular density assumption.
7. Expansion of the required weighted squared error uses the exact mixed product. Its upper bound tends to zero by the energy limit and the short-time factor. Nonnegativity completes strong convergence. The flux corollary then follows by testing against the constructed smooth potentials and applying Cauchy-Schwarz. For the time-dependent consequence of Casteras-Flaim-Monsaingeon Theorem 4, finite Fisher information holds at almost every time under that theorem's integrability hypothesis.

## References and editorial corrections

The [reference audit](REFERENCES.md) checks the target conjecture, heat-gradient estimate and version-specific locators. The stale `main/problems/618-fisher-score-gradient-closure.md` URL was replaced by pinned original and current archive links. References for standard semigroup and Sobolev background were added, and the previously recorded extension proof was identified as related work. Every bibliography item is cited and every equation/theorem reference resolves.

Author affiliation and email were checked against University of Cambridge-hosted pages. The visible author block and PDF metadata name Matthew J. Colbrook. Editorial changes do not replace the core proof.

## Evidence limits

This is an analytic argument conditional on the cited established heat-gradient estimate and standard semigroup/Sobolev facts. The check read the entire proof and compared the cited theorem statements; it does not reprove Sturm's theorem. It supplies neither a Lean certificate nor independent human peer review, publication acceptance or a novelty determination. No numerical experiment is needed for this proof. Pull-request acceptance and status processing remain outstanding by the submitter's instruction.
