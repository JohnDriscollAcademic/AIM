# 489. Global attraction in D-stable Lotka–Volterra systems

**Area:** Population dynamics and nonlinear stability

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Let $`n\ge1`$, let $`A=(a_{ij})\in\mathbb R^{n\times n}`$, and fix a vector $`x^\ast\in(0,\infty)^n`$. Consider the population system

```math
\frac{dx_i}{dt}
=x_i\sum_{j=1}^n a_{ij}(x_j-x_j^\ast),
\qquad i=1,\ldots,n.
```

In particular, $`x^\ast`$ is a strictly positive equilibrium. Assume that $`A`$ is **D-stable**: for every constant diagonal matrix

```math
D=\mathop{\mathrm{diag}}\nolimits(d_1,\ldots,d_n),\qquad d_i>0,
```

all eigenvalues of $`DA`$ have strictly negative real parts.

Must every solution starting from $`x(0)\in(0,\infty)^n`$ exist for all forward times and converge to the coexistence equilibrium?

```math
\lim_{t\to\infty}x(t)=x^\ast.
```

This is the Hofbauer–Sigmund global-stability conjecture, in the explicit formulation of Lu–Takeuchi and Hong–Pego. Equivalently, write $`\dot x=\mathop{\mathrm{diag}}\nolimits(x)(b+Ax)`$ with $`b=-Ax^\ast`$. Hong–Pego use the interaction sign convention $`-B=A`$. [1, §2; 2, §2.4]

The question ranges over all finite dimensions and real interaction matrices satisfying the stated condition. It does not assume symmetry, a competitive or cooperative sign pattern, diagonal dominance, or boundedness of the trajectory. Forward existence is part of the requested conclusion. Initial states with an extinct species are excluded: the corresponding coordinate remains zero. The equilibrium is already locally asymptotically stable because its Jacobian is $`\mathop{\mathrm{diag}}\nolimits(x^\ast)A`$. The unresolved issue is attraction from every strictly positive initial population.

## Application

Lotka–Volterra equations describe populations whose per-capita growth rates depend linearly on the current abundances. They are used to study coexistence, species loss and alternative community states, including microbial communities. In this model, a strictly positive equilibrium represents coexistence of all species. Local stability only describes recovery from sufficiently small population perturbations. Global attraction would additionally imply recovery from any finite perturbation that leaves every population positive. [2, introduction]

D-stability ensures local stability at every feasible positive equilibrium when the growth vector changes while the interaction matrix remains fixed. Resolving the conjecture would determine whether this robust local criterion also controls the long-term nonlinear dynamics. Its relevance is to the behaviour of this ecological model; it does not remove the need to justify the interaction model or estimate its coefficients from data.

## References

1. Zhengyi Lu and Yasuhiro Takeuchi, *Global Dynamical Behavior for Lotka–Volterra Systems*, RIMS Kôkyûroku **828** (1993), 171–178. [Full text](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0828-16.pdf), equation (1), p.171; Definitions 1–2 and the named conjecture, p.172; Definition 3, p.174, and Theorem 2, p.176.
2. Won Eui Hong and Robert L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, Journal of Mathematical Biology **83** (2021), Article 16, DOI 10.1007/s00285-021-01638-7. [Institutional manuscript](https://par.nsf.gov/servlets/purl/10289787), §§2.1–2.4 and Theorems 3.1, 3.4 with Example 3.5, manuscript pp.4–10. [Published identity](https://link.springer.com/article/10.1007/s00285-021-01638-7).
3. Pablo Almaraz, Piotr Kalita, José A. Langa and Fernando Soler-Toscano, *Structural stability of invasion graphs for Lotka–Volterra systems*, Journal of Mathematical Biology **88** (2024), Article 64. [Full published text](https://link.springer.com/article/10.1007/s00285-024-02087-8), Definitions 1–4, Theorems 5 and 8, and §7.1, Question 35. Also inspected: [arXiv:2209.09802v6](https://arxiv.org/pdf/2209.09802v6), March 12, 2024.
4. M. C. Bortolan, P. Kalita, J. A. Langa and R. O. Moura, *A theoretical and computational study of heteroclinic cycles in Lotka–Volterra systems*, Journal of Mathematical Biology **90** (2025), Article 28. [Full published text](https://link.springer.com/article/10.1007/s00285-025-02190-4), Definition 3.1, Proposition 3.9, Corollary 3.10, and Theorems 3.14, 3.19–3.20.
5. Anna Cima, Arno van den Essen, Armengol Gasull, Engelbert Hubbers and Francesc Mañosas, *A Polynomial Counterexample to the Markus–Yamabe Conjecture*, Advances in Mathematics **131** (1997), 453–457, DOI 10.1006/aima.1997.1673. [Author-hosted published text](https://www.cs.ru.nl/E.Hubbers/pubs/A-Polynomial-Counterexample-to-the-Markus-Yamabe-Co_1997_Advances-in-Mathema.pdf), Theorem 1.1 and its proof, pp.454–455.
6. Stephen Baigent and Zhanyuan Hou, *Global Stability of Interior and Boundary Fixed Points for Lotka–Volterra Systems*, Differential Equations and Dynamical Systems **20** (2012), 53–66, DOI 10.1007/s12591-012-0103-0. [Author manuscript](https://www.ucl.ac.uk/~ucess29/resources/preprints/JDEDSGlobal_Stab_Rev.pdf), §2 definitions and Theorems 5–6, manuscript pp.8–10.

## Status review

**Resolution (2026-10-02):** An exact rational four-species D-stable interaction matrix admits a nonconstant strictly positive periodic orbit. Exact certificates cover all positive diagonal scalings and an infinite Fourier tail, disproving global attraction under D-stability alone.

**Proof and review:** [Accepted solution](../research/solutions/490-lotka-volterra-counterexample/PROOF.md); [fresh mathematical audit](../research/solution_reviews/2026-10-02-active-prs/489-review.md); [PR #22](https://github.com/MColbrook/AIM/pull/22). The audit records the pinned submission, target comparison and any supporting computations.

**Evidence:** Solved under the documented-independent-audit convention. The review was performed by AI; it does not assert human peer review, publication, proof-assistant verification or novelty priority. The problem retains its existing page and ID.

### Previous status review

**Known cases:** Positive diagonal Lyapunov stability yields forward existence and attraction of all strictly positive trajectories; references 1–3 discuss this sufficient subclass.

**Remaining target:** Global existence and convergence under D-stability alone, in all dimensions and for arbitrary real interaction patterns.

**Integration review (2026-09-23):** The September 19 source audit was refreshed with problem-specific web searches and searches scoped to arXiv, Zenodo, GitHub and Palomar. No matching full-scope solution announcement was located. Search coverage is limited by indexing and access; this is not a proof of openness. See the [integration record](../research/integration-2026-09-23.md).

The explicit open assessment inspected is Hong–Pego's 2021 discussion [2, §2.4]. The September 19, 2026 check covered the conjecture's names, D-stability and global-attraction formulations, proofs, counterexamples, recent work, revisions and corrections. The newer papers [3, 4] address stronger assumptions and related dynamics; neither is cited as a new statement of the exact conjecture.

A standard sufficient condition is **Volterra–Lyapunov stability**: there exists a positive diagonal matrix $`H`$ such that

```math
HA+A^{\mathsf T}H\prec0.
```

This means the symmetric matrix is negative definite. It yields a Lyapunov function and global convergence. D-stability does not supply this stronger certificate. Theorems 5 and 8 of [3] retain the Volterra–Lyapunov assumption; Question 35 asks about extending their invasion-graph conclusions to broader matrix classes. Lu–Takeuchi's Theorem 2 [1] proves global stability under qualitative stability, which requires stability for every matrix with the same entrywise sign pattern. That is an additional restriction.

Hong–Pego's Theorem 3.4 excludes strictly stable proper subcommunities under internal D-stability; it does not prove convergence of all positive trajectories. Their Example 3.5 has stable nested communities but fails D-stability. The cycles studied in [4] concern boundary connections and backward limit behaviour under Volterra–Lyapunov stability; they do not contradict its forward-attraction theorem.

The split Lyapunov criterion [6, Theorem 5] additionally assumes permanence, a suitable real eigenvector and a quadratic-form condition on its orthogonal hyperplane. Those hypotheses are not a consequence of D-stability alone. Theorem 6 retains analogous conditions for boundary equilibria.

The general Markus–Yamabe conjecture is false in dimensions at least three [5]. Its counterexample is a different polynomial vector field, not a D-stable Lotka–Volterra system. In logarithmic population coordinates, the present model forms a restricted exponential class of vector fields with everywhere stable Jacobians. Failure for the larger class does not resolve this restricted question.

The [evidence record](../research/expansion-2026-09/candidates/lotka-volterra-d-stable-global-attraction.json) records theorem comparisons, source versions and access limits. The original Hofbauer–Sigmund book formulation was not inspected; the complete restatements in [1, 2] were read. The published Hong–Pego article's identity was checked, while its mathematics was read in the institutional manuscript. The author text [6] was readable through the browser despite a direct-download restriction. Research was followed by a separated adversarial self-review; no independent expert review or proof certification is claimed.

The [carrying-simplex question](300-carrying-simplex-interior.md) concerns differentiability for discrete competitive population maps. The [chemostat question](334-chemostat-unequal-removal-exclusion.md) concerns resource-mediated competitive exclusion. The [local-stability decidability question](338-polynomial-local-stability-decidability.md) asks for a terminating algorithm for general polynomial systems. These have different models or conclusions. Dimensions, sign subclasses and equivalent formulations are counted as one family here.
