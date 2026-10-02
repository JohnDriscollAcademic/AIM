# AIM 665: additional heat-semigroup proof

Date: 2026-10-02. Reviewer: OpenAI Codex (AI), fresh audit of the mathematical argument and its imported gradient estimate. This is not independent human peer review, formal verification, or a novelty determination. The submission records prior AI assistance in preparation.

**Decision:** accept [PR #19](https://github.com/MColbrook/AIM/pull/19), head `5a1ebd317fafc26225948a14838da7302bc5847c`, as an additional proof of [AIM 665](../../resolved/665-fisher-score-gradient-closure.md), originally 618. Its status was already **Solved**. Preserve the existing proof and review; do not add another problem or another solved count.

Reviewed the entire [manuscript](../../solutions/618-fisher-score-heat-semigroup/aim618_solution.tex) against the archived target at base `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.

## Mathematical audit

Writing u=sqrt(rho), the H1 assumption implies `rho=u^2` is W1,1 and `grad rho=2u grad u`. The gradient vanishes almost everywhere on the zero set of u, so the defined score has squared weighted norm exactly the Fisher information I. Approximation of u in H1 proves the needed weak Green identity for rho; only the smooth test function needs a zero normal derivative.

For `r=P_t rho`, `h=log(r+t)` and `phi=P_t h`, the added t handles vacuum, including zero-mass components. Positive-time smoothing gives smoothness through the boundary, and h has the Neumann condition, so it belongs to the generator domain. This checks the otherwise potentially invalid commutation of the Laplacian and semigroup.

Twice integrating by parts, using the Neumann conditions, and using self-adjointness in the L1-Linfinity pairing gives the exact mixed product `A=<score,grad phi>_rho=integral |grad r|^2/(r+t)`. The gradient estimate, with its constant uniform in the input h, gives `B=||grad phi||_rho^2 <= c(t) A`. Cauchy-Schwarz then implies `A <= c(t) I`, including the A=0 case. No approximation assertion is assumed in obtaining this inequality.

Strong L1 continuity gives `sqrt(r+t) -> sqrt(rho)` in L2. Its bounded H1 energy, equal to A/4, yields `I <= liminf A` by weak lower semicontinuity. Combined with `c(t)->1`, this gives `A->I`. Expanding the fixed-original-weight error now gives `0 <= ||grad phi-score||_rho^2 <= I+(c(t)-2)A -> 0`. The argument applies to vanishing and unbounded densities and nonconvex smooth boundary. Compactness supplies common bounds over finitely many components. The flux corollary follows directly by weighted Cauchy-Schwarz.

## Imported result and references

Checked [Sturm, arXiv:2502.01915v1](https://arxiv.org/html/2502.01915v1), Theorem 1.1(iii) and Remark 1.2: the p=2 estimate, after squaring, gives precisely `c(t)=exp(4 S sqrt(t/pi)+O(t))`, uniformly in the input function. Smooth compact geometry supplies the curvature bounds; extension of a compact smooth manifold across its boundary permits the domain formulation of that theorem. The boundaryless estimate is the usual Ricci-bound counterpart.

Checked [Casteras, Flaim and Monsaingeon, arXiv:2512.05826v2](https://arxiv.org/html/2512.05826v2): the conjecture following Theorem 4 is the target, and Section 3 states the same uniform gradient estimate and motivates the double regularization. The manuscript correctly distinguishes the separate rough-domain chain-rule question. The remaining Sobolev product/locality and semigroup facts are standard inputs with identified book references; the proof also directly supplies its product approximation argument.

I found no unresolved mathematical gap. The prior extension-to-a-closed-manifold proof remains the existing primary catalogue proof, with this argument linked as an additional resolution route.
