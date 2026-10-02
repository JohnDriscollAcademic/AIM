# Independent audit: AIM 022, triangle case (PR #20)

**Audit date:** 2026-10-02. **Reviewer:** OpenAI Codex, in a review session separate from submission preparation. This is an AI mathematical and computational audit, not human peer review or formal verification.

**Pinned submission:** [PR #20](https://github.com/MColbrook/AIM/pull/20), head `3889757da4a06da20011203b25c3bf9e6b0f386f`; package `research/solutions/022-steklov-triangle`. Its snapshot is byte-identical to [AIM 022](../../../problems/022-steklov-polygon-optimizer.md) at `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.

**Recommendation:** Accept the triangle result and mark AIM 022 **Partially resolved**. The equilateral triangle is the unique maximizer among nondegenerate triangles of prescribed perimeter. The conjecture for polygons with four or more sides remains open. This submission must not move the full polygon problem into the solved list.

The complete analytic proof and all four certificate stages were read, their assumptions re-derived, and the certificate reproduced. The originating AI checks were not used as a substitute for this audit. One arithmetic-precision description needs the minor correction below; it does not invalidate the certificate or change its conclusions.

## Analytic and certificate checks

1. **All triangle shapes.** Polar decomposition of an affine map from the reference equilateral triangle gives a positive scalar, an orthogonal map and `exp(S)` with S symmetric and traceless. Its eigenvalues are plus/minus r. An affine map carrying an equilateral triangle to an equilateral triangle is a similarity (also follows by equating the three side lengths), so r=0 is exactly the equilateral case. Reflections, vertex labels and scale do not omit any triangle.
2. **Third-eigenvalue lower bound.** Adding the boundary-mean rank-one term makes the broken energy an inner product on `H^1(E)+V_h`: zero gradients give piecewise constants and the zero-mean CR jumps force one global constant. The chosen CR interpolant is exactly the orthogonal projection because it preserves all edge means, including the boundary mean. The projection estimate, triangle inequality and orthogonal Pythagoras give the displayed lower eigenvalue bound. Taking the rank-one penalty sufficiently large puts the constant eigenvalue above the third nonzero one on both spaces. This justifies counting the third nonconstant eigenvalue, rather than confusing it with the third eigenvalue including zero.
3. **Trace estimate.** The divergence identity has the correct height factor and sign. Subtracting the volume mean allows the convex Poincare inequality; subtracting the edge mean then decreases the edge L2 norm. Each element has at most two boundary edges, giving the stated factor two. For the equilateral mesh the resulting squared trace constant is `0.20981553491306422149...`.
4. **Integer matrices and inertia.** The CR basis `1-2 lambda_i` has the stated local stiffness and boundary mass integrals. The conversion of the pencil to `800 K_int - 49 N_3` at mu=1.96 is correct. Symmetry makes every characteristic root real, so applying Descartes' rule to the polynomial and its reflected argument counts signs exactly. The congruence with `K+N` converts the three negative directions into exactly three finite generalized eigenvalues below mu, including zero. The 408-dimensional exact computation returns `(3,0,405)`, and the trace correction gives `sigma_3(E) >= 1.388851`.
5. **Identification of the first eigenspace.** The odd, rotation-sum-free sector is closed and invariant under the Dirichlet-to-Neumann operator; the polynomial trial function lies in its operator domain. Its Rayleigh quotient below rho produces two linearly independent rotated eigenfunctions. Since the third positive eigenvalue is at least rho, these exhaust the first eigenspace. Reflection leaves exactly one odd direction, so the restricted lowest eigenvalue is simple and the next sector eigenvalue is at least rho. These facts supply the gap required by Temple's inequality, without assuming the desired multiplicity in advance.
6. **Eigenvalue and exact moments.** Boundary polynomial integration, outward normals and the complex Green formula have the correct signs. Temple's inequality supplies a lower bound and Rayleigh an upper bound. The spectral residual controls both the boundary error and its harmonic-extension energy, since `s/(s-lambda)^2` decreases for `s >= rho > lambda > 0`. The equivariant second function has the same error norm; projection orthogonality justifies the normalization interval. The bilinear and linear moment widenings in the code are the Cauchy--Schwarz bounds in Lemma 5, including the edge length square root `3^(1/4)`.
7. **All nearby shapes.** For the affine pullback, energy uses `exp(-2S)` and each edge uses its own length factor. Subtracting the boundary mean gives the rank-one correction in the denominator. A negative direction of the displayed 2 by 2 matrix necessarily has positive boundary denominator and gives a strict Rayleigh bound. The factorization by r uses only the exact sum identities for the exact eigenfunctions; enclosure entries need not themselves satisfy those identities. The removable singularity bounds at r=0 follow from the monotonicity of the two hyperbolic quotients. Rational radial endpoints, outward angular endpoints and complete subdivision cover `[0,3/5] x [0,2 pi]`. Every accepted box proves a strictly negative determinant or trace; the zero-radius limiting matrix is used only to cover positive r close to zero.
8. **All far shapes and uniqueness.** Convexity gives two monotone boundary arcs spanning the long-axis width, whence the boundary quadratic moment is at least `W^3/6`. Perimeter monotonicity inside the enclosing rectangle supplies the numerator bound. Width bounds in the expanding and contracting eigenvector directions give the stated decreasing B(r), including the constants `W_E=3/2` and `d_E=sqrt(3)`. At r=11/20 it is strictly below the equilateral lower bound. The local and far regions overlap, cover every positive r, and prove strictness away from the equilateral triangle.

## Primary sources and scope

The [Cheng--Gui--Hu--Li--Yao preprint](https://arxiv.org/html/2603.25116v1), Conjecture 1.2 and the paragraph immediately following it, matches the polygon target and identifies triangles as an open subcase in that paper. Its regular-polygon monotonicity theorem does not prove the arbitrary-triangle comparison.

The abstract lower-bound theorem was checked against Theorem 2.4 of [You, Xie and Liu](https://arxiv.org/pdf/1808.08148), also published as *Guaranteed Eigenvalue Bounds for the Steklov Eigenvalue Problem*, *SIAM Journal on Numerical Analysis* 57 (2019), 1395--1410, DOI [10.1137/18M1189592](https://epubs.siam.org/doi/10.1137/18M1189592). The submission supplies its own compatible proof using the rank-one boundary-mean modification and verifies the projection hypothesis.

The convex mean-zero Poincare bound with diameter/pi is the one established by [Bebendorf, *A Note on the Poincare Inequality for Convex Domains*](https://ems.press/content/serial-article-files/35407), *Zeitschrift fuer Analysis und ihre Anwendungen* 22 (2003), 751--756, DOI `10.4171/ZAA/1170`; all mesh elements are convex. The min--max principle and self-adjoint Dirichlet-to-Neumann operator on bounded Lipschitz polygons are the standard functional-analytic inputs stated in the submission. Temple's inequality and the Descartes specialization are proved in the submission. No cited theorem needs an unverified smooth-boundary hypothesis in this application.

## Fresh reproduction

Environment: Windows 11, Python 3.12.14, python-flint 0.9.0; the optional comparisons used SciPy 1.18.1 and mpmath 1.4.1. Dependencies were installed only in an isolated task scratch directory. Windows sandbox ACLs prevented importing the installed wheels in the restricted process; the inspected commands were therefore run with escalated filesystem access. No certificate source was changed.

From the exported package:

```text
python -B certify/main.py
python -B review/mutation_tests.py
python -B review/selfcheck_local.py
```

- [Full certified run](022-certified-run.log): `ALL CERTIFIED CHECKS PASSED`; exact inertia `(3,0,405)`; third-eigenvalue lower bound `1388851/1000000`; 8412 local boxes, 404 splits, maximum depth two; far upper bound about `3.19262378424102` versus equilateral lower bound about `3.8724615957728065693`.
- [Mutation tests](022-mutation_tests.log): all five invalid choices rejected, including the excessive discrete threshold, invalid Temple gap, excessive local radius, insufficient far radius and lowered target.
- [Alternate local checks](022-selfcheck_local.log): factored/direct matrix difference at most `3.5092e-29`; direct transformed-domain quadrature differs by at most `4.39648317751562e-14`; all 26,400 alternate-formula boxes pass. Floating endpoints in this optional check make it supporting evidence, not a replacement for the rational/outward certificate cover.
- New reviewer-written [coordinate assembly script](022-independent-assembly.py), run as `python -B 022-independent-assembly.py PATH_TO_PACKAGE`, directly integrated the physical CR basis on each triangle and used edge Gauss quadrature for the boundary mass. [Results](022-independent-assembly.json): all 256 elements and 408 degrees of freedom accounted for; stiffness/mass discrepancies at most `6.2173e-15` and `3.0532e-16`; correct area and perimeter; numerical inertia `(3,0,405)`. This checks the geometric meaning of the integer matrices independently of their hard-coded local entries; exact inertia is supplied by the certified run.

## Minor precision-description correction

At the pinned head, `PROOF.md` Section 3 (the trial-function paragraph) says **"computed exactly in Arb at 320 bits"**, and Section 8's step-2 table says **"Arb at 320 bits"**. In `certify/main.py`, imports of `cert_local` and then `cert_far` follow `cert_E`; each assigns the process-global `flint.ctx.prec = 128`. A fresh `import main, flint; print(flint.ctx.prec)` in the certificate directory printed **128**. Therefore the published driver performs its certificate operations at 128-bit precision, with geometric constants constructed during the earlier 320-bit import. The module-level setting in `cert_E.py` does not persist through the later imports.

Suggested documentation correction, without changing the verified algorithm: replace the Section 3 wording by **"enclosed using Arb ball arithmetic (128-bit working precision in the driver; the module's geometric constants are initialized at 320 bits)"**; replace the Section 8 entry by **"Arb at 128-bit working precision in the driver"**. The submitted output was reproduced at the actual driver precision and every rigorous comparison succeeds. The term "exactly" should describe rational coefficients and integer calculations; irrational polynomial integrals are rigorously enclosed, not generally represented exactly. Refresh the changed proof's checksum when integrating this textual correction and keep this audit's pinned-head hashes unchanged.

## Integrity and verdict

All 29 entries of the original SHA256SUMS manifest match the exported pinned bytes.

| Pinned file | SHA-256 |
| --- | --- |
| `PROOF.md` | `b5d3e4066b71d70aea47a9252ba4a83b866fee188792d8ac8fca56d2f552a7e2` |
| `statement.md` | `aa0bcafdf0177994cb5eee1ebc7e0438a590003649592eab0d084ca74325d6dd` |
| `SHA256SUMS` | `03b3298103469500f145c72ac4d34611bb3a0b92938a10e56b27d6529d6d17b6` |

No unresolved mathematical obstruction to the triangle result was found. Its trusted computational base is FLINT's exact integer arithmetic and Arb's outward enclosures through python-flint, together with Python's execution of the inspected certificate. The outcome is an independently AI-audited computer-assisted proof of the triangle subcase, not a formal proof-assistant certificate and not a resolution for all n.
