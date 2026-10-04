# Independent mathematical review of AIM505 / PR28

**Repository evidence:** [proof](../../solutions/siavash-sadeghi-505/aim505_report.pdf), [source](../../solutions/siavash-sadeghi-505/aim505_report.tex), and [problem](../../../problems/505-upwind-discrete-aronson-benilan.md). Submitted in [PR #28](https://github.com/MColbrook/AIM/pull/28) at `3fc0b48d419c023fc4113306878e6ac02d24c3c2`.

Date: 2026-10-04 (Europe/London). Reviewer: **independent_505_pr28 (OpenAI Codex AI)**.

**Verdict: the inspected argument gives a valid counterexample to the complete stated target.** I found no substantive mathematical defect. In particular, it handles the actual reflected Neumann scheme, proves the required pressure derivative convergence rather than inferring it from pressure convergence, and supplies a diagonal sequence of finite integer exponents satisfying all initial bounds with one fixed constant. The proof, rather than the numerical examples, establishes failure of a constant uniform in both mesh and exponent.

This is a fresh independent AI audit. It is not independent human review, publication peer review, or formal proof verification. I formed the argument from the manuscript and exact problem statement; I did not read or rely on the package's REVIEW_REPORT.md, TARGET_AUDIT.md, REPRODUCTION_RECORD.md, pre-existing experiment output, or claimed check results.

## Reviewed revision and integrity

- PR: 28. Problem: AIM505.
- Exact PR head: 3fc0b48d419c023fc4113306878e6ac02d24c3c2.
- Source: research/solutions/siavash-sadeghi-505/aim505_report.tex.
- **Exact Git-blob SHA256:** d69bb81475880833d4c274b4490fffc1522efed8b5e17832e15cbd778f2d46d5.
- **Inspected snapshot SHA256:** a44d8b2a8af9159d7d8c54e6d23b2c547476f15ab67cca213b05bf616ab041c1.
- Git blob: 14,140 bytes; inspected snapshot: 14,437 bytes. I independently retrieved the exact head blob using read-only git cat-file and verified equality after CRLF/LF normalization. The byte difference is line endings, not manuscript content. See independent-source-integrity.json.
- Submitted numerical script's inspected snapshot SHA256: 4bd880ce0d9b80815331db170781488467c99b1925e231c74ba4c6de050f4dba.

I read CONTRIBUTING.md and problems/505-upwind-discrete-aronson-benilan.md in the repository. I also retrieved the target at the manuscript's cited repository commit 59a8f0c2957dd272f56bcf282dfe0c066a15f441 using read-only git show; its displayed mathematical target agrees with the statement reviewed here. The snapshot review-input.json identifies target commit c4b2a812bb5babdb1efdad8c3b8080e7301ee507. No repository files or manuscript files were changed and no git mutations or GitHub comments were made.

## Complete-target comparison

| Target requirement | What the counterexample establishes |
|---|---|
| Fixed admissible X, T, p_H and G | X=T=p_H=1 and G(p)=1-p; G is C1, G(1)=0 and G'=-1. |
| Exact fixed-grid upwind mobility | The flux is exactly F(a,b)=max(a,b)(b^gamma-a^gamma); this follows because pressure order and density order agree. |
| Reflected ghost values at both endpoints | The full ODE uses the reflected values; endpoint diffusion is doubled and the exterior estimate uses half endpoint weights to account for it. |
| Nonnegative density and p=n^gamma, gamma>1 | A sequence of finite integers gamma_h>=2 is selected. The full solution stays in [0,1]. |
| 0<=p_i(0)<=p_H | Initial core pressure is a^gamma P_i^{h,gamma} with 0<P_i^{h,gamma}<1; exterior pressure is zero. |
| Uniform initial density and pressure sums | Each h-weighted full-grid sum is <=2+h<=3. |
| Uniform initial density total variation | Symmetry, monotonicity and the exterior zeros give TV<=2a=3/2. |
| Uniform initial derivative sum, evaluated with the actual scheme | The core derivative is (1-a^gamma)n_i(0); only two exterior derivatives are nonzero. Their combined h-weighted contribution is <=2a^(gamma+1)/h. Choosing a^(gamma_h+1)/h<=1 gives a total <=5. |
| One common initial-data constant | C0=10 therefore works for every member of the sequence. |
| Observation at a legitimate full-grid node and time in (0,T] | K=M/2 is an interior node; t_h>t0=-log(3/4)>0 and t_h<1 for all sufficiently fine even meshes. |
| Failure of every permitted uniform C | -gamma_h t_h w_K(t_h)>=t_h A_h/2 tends to infinity while all permitted parameters and C0 remain fixed. |

The manuscript does not need to construct counterexamples for every admissible G or every exponent: one fixed admissible set of parameters and an admissible sequence suffice to refute the proposed general estimate.

## Independent mathematical checks

### 1. Exact flux, comparison, and existence

For b>=a>=0,


```math
F(a,b)=b^{\gamma+1}-ba^\gamma,\qquad
\partial_bF=(\gamma+1)b^\gamma-a^\gamma\ge0,\quad
\partial_aF=-\gamma ba^{\gamma-1}\le0.
```


For b<a, F=ab^gamma-a^(gamma+1), so partial_b F=gamma a b^(gamma-1)>=0 and partial_a F=b^gamma-(gamma+1)a^gamma<=0. The derivatives agree at a=b. Consequently each off-diagonal component of the ODE vector field is nonnegative. At a reflected endpoint the same neighboring flux is simply multiplied by two; this preserves cooperativity.

At a zero density all incoming diffusion is nonnegative. At a spatial maximum of density, both neighboring pressures are no larger, diffusion is nonpositive, and the reaction is zero at n=1. Thus [0,1] is invariant. For the selected integer exponents the finite system is locally Lipschitz and bounded on this invariant box, giving existence and uniqueness through the needed interval and indeed for all finite positive times. The usual finite-dimensional cooperative comparison theorem applies; the diagonal reaction derivative need not have a favorable sign.

The zero extension of the pinned core is a genuine subsolution: its equations agree with the full equations on the core, its derivative is zero outside, and the actual exterior vector field at that zero extension is nonnegative. Thus full core density is at least pinned core density.

### 2. Linear profile and edge asymptotics

The relation 2 cosh(eta_h)=2+h^2 verifies the centered recurrence exactly. The given profile with zero neighbors at +/- (K+1) therefore satisfies Delta_h P+1-P=0. Positivity, strict upper bound by one, symmetry and strict decrease to the right follow directly from cosh.

Write L=(K+1)eta_h. Then


```math
P_K=1-\cosh(\eta_h)+\tanh(L)\sinh(\eta_h).
```


Since eta_h=h+O(h^3) and L tends to 1/2, this gives P_K/h -> c=tanh(1/2). Applying the same identity with a displacement 2 eta_h gives P_(K-1)/h ->2c, whence the ratio tends to two and the last core edge slope tends to c. All asymptotics used for A_h are correct.

### 3. Nonlinear stationary core and implicit-function theorem

For positive core pressure, dividing density diffusion by n_i gives precisely D_(gamma,h): a lower-pressure neighbor has mobility n_i; a higher-pressure neighbor has the extra factor (p_j/p_i)^(1/gamma). Zero Dirichlet neighbors contribute to the Laplacian but not to the extra term.

With nu=1/gamma, the extra positive-neighbor term is C1 near the positive profile. If s=p_j-p_i, its potentially nonsmooth part is s_+[exp(nu log(1+s/p_i))-1]. Near s=0 this is O(s_+^2), and its first derivatives join continuously across the tie. Ghost neighbors remain strictly below the nearby positive core and cause no logarithm of zero.

At nu=0 the pressure derivative is the Dirichlet matrix Delta_h-I. For a vector v with zero Dirichlet neighbors, its quadratic form is the negative sum of squared differences divided by h^2, minus sum v_i^2; hence it is invertible. The finite-dimensional C1 implicit-function theorem therefore supplies a locally unique branch for every sufficiently small positive nu, equivalently every sufficiently large finite gamma at each fixed h. Reflection preserves the equations and the neighborhood, so local uniqueness gives symmetry. Strict inequalities and the finitely many strict monotonicity gaps survive by closeness.

There is no required bound on this existence threshold uniform in h. The later diagonal selection allows the threshold to depend on h.

### 4. Exact pinned-core solution

D_(gamma,h) is homogeneous of degree one in pressure. Thus p_i^D=theta P_i^(h,gamma) gives density derivative (1-theta)n_i^D exactly, and theta'=gamma theta(1-theta), theta(0)=a^gamma. The displayed logistic solution is correct.

At fixed t<t0=-log(a), theta tends to zero; at fixed t>t0, theta tends to one and theta' tends to zero exponentially with an additional polynomial gamma factor. The value at t0 has no effect on the later dominated-convergence integral. At fixed h, each initial pinned core density tends to a>q, so the finite minimum exceeds q for large enough gamma and continues to do so because the pinned density is increasing.

### 5. Core discrepancy

Let delta_i=n_i-n_i^D>=0 on the core. Internal face fluxes cancel in the unweighted core sum. Under the exterior bootstrap n_out<=q<n_core, the actual core boundary term minus the pinned one is


```math
n_{\rm core}p_{\rm out}
 -\bigl(n_{\rm core}^{\gamma+1}-(n_{\rm core}^D)^{\gamma+1}\bigr)
\le q^\gamma.
```


For the reaction the difference is delta_i minus a nonnegative power difference, so it is <=delta_i. There are exactly two boundary faces. Therefore D'<=D+2q^gamma/h^2, D(0)=0, giving D<=2(e^t-1)q^gamma/h^2. Each coordinate difference is <=D, and the gamma-Lipschitz bound for n^gamma on [0,1] gives the asserted pressure error C_h gamma q^gamma. These constants may depend on h but not on gamma.

### 6. Reflected exterior weights and bootstrap

At the right endpoint the diffusion contribution is -2F(n_(M-1),n_M)/h^2. Multiplying that equation by 1/2 cancels exactly the terminal flux in the sum over the right exterior. The left endpoint cancellation is analogous. The exterior diffusion sum consequently consists only of the two fluxes entering from the core. Each is <=p_edge/h^2 because the core density is <=1. The reaction contribution is <=E. This proves the displayed E' inequality for the actual reflected system; an unweighted exterior sum would not cancel correctly.

Every exterior density is <=2E because every weight is at least 1/2. Combining the edge pressure error and the pinned solution gives the claimed convolution estimate. Its upper bound is increasing in time. At fixed h and the chosen t_h,


```math
\int_0^{t_h}e^{t_h-s}\theta_\gamma(s)\,ds
\longrightarrow e^{t_h-t_0}-1
=\frac{q h^2}{8P_K^h}.
```


The full right-hand bound for E therefore tends to q/4. For sufficiently large gamma it is strictly less than q/2 at t_h and hence throughout any interval ending at a putative first exit. That would imply every exterior density is strictly below q at the first exit, a contradiction. The bootstrap closes through t_h. The margin is strict; the proof does not rely on an equality estimate at exit.

### 7. Pressure derivative convergence

The face flux has both coordinate derivatives bounded in absolute value by gamma+1 on [0,1]^2. On internal core faces this and the discrepancy bound control the flux difference by C_h gamma q^gamma. On a core/exterior face, the absolute flux difference is bounded by (gamma+1)delta_i+q^gamma; the same estimate holds for either orientation.

The reaction is also Lipschitz with a bound O(gamma). Substituting into the full and pinned core density equations therefore gives |dot n_i-dot n_i^D|<=C_h gamma q^gamma. Since |dot n_i^D|<=1 and n^(gamma-1) is (gamma-1)-Lipschitz on [0,1] for gamma>=2,


```math
|\dot p_i-\dot p_i^D|\le C_h\gamma^2q^\gamma.
```


At the fixed time t_h>t0 the pinned pressure derivative tends to zero, so the full core pressure derivative does as well. This is an actual equation-based derivative estimate. Mere pressure convergence would not have justified the next step, but the manuscript supplies the needed stronger argument.

### 8. Negative defect and finite-exponent quantifiers

At the right core edge, for large gamma the inward neighbor has larger pressure, while the outward neighbor has pressure <=q^gamma and hence less than p_K. Dividing the exact density equation by positive n_K and applying the pressure law yields exactly the manuscript's pressure identity. After multiplication by gamma it reads


```math
\gamma w_K=\frac{\dot p_K}{p_K}
-\frac{\gamma}{h^2}\left[\exp\left(\frac1\gamma
\log\frac{p_{K-1}}{p_K}\right)-1\right]\bigl(p_{K-1}-p_K\bigr).
```


For each fixed h, p_K tends to the strictly positive P_K^h, dot p_K tends to zero, and the ratio has a finite positive limit. The elementary exponential difference quotient therefore gives gamma w_K(t_h)->-A_h. The sign is negative because P_(K-1)>P_K.

The edge limits imply h A_h ->c log(2)>0 and t_h->t0>0. Consequently t_h A_h diverges. For each sufficiently small h one can choose a finite integer gamma_h satisfying every fixed-h threshold, gamma_h w_K(t_h)<=-A_h/2, and a^(gamma_h+1)/h<=1. The last condition is compatible with arbitrarily large gamma because a<1. If desired one can also require gamma_h>=M, so these exponents diverge, though divergence is not needed beyond the displayed estimates.

This is a legitimate diagonal sequence, not a simultaneous limit whose rates are assumed. For every proposed C the sequence eventually has -gamma_h t_h w_K>C, at a legitimate node and time with all parameters and initial-data bounds fixed.

### 9. All initial-data bounds

The initial profiles are zero outside the core and symmetric unimodal inside. Both full-grid weighted sums are <=h(2M+1)=2+h<=3. Total variation is exactly twice the peak initial density and thus <=2a.

At initial time the true core equations agree with the pinned equations, so dot n_i(0)=(1-a^gamma)n_i(0)>=0. The only initially nonzero exterior derivatives are at +/- (K+1), each equal to n_edge(0)p_edge(0)/h^2 and <=a^(gamma+1)/h^2. For M>=4 these two nodes are strictly inside the full outer endpoints, so no omitted reflected factor occurs. All other initial exterior derivatives are zero. Hence h sum |dot n_i(0)|<=3+2a^(gamma+1)/h<=5 after diagonal selection. This covers the often restrictive fourth assumption using the actual scheme.

## Primary-reference verification

I opened the [published David–Ruan paper](https://www.numdam.org/item/10.1051/m2an/2021080.pdf) and its [arXiv record](https://arxiv.org/abs/2105.10376) on 2026-10-04. The publication is ESAIM M2AN 56 (2022), 121–150, DOI 10.1051/m2an/2021080. Pages 124–125, equations (2.1)–(2.5), verify the scheme, upwind rule, reflected ghosts and four initial bounds. Page 130, section 2.3 and Theorem 2.3, discusses the discrete lower bound with linear growth in the cases gamma=1 and notation gamma approximately infinity, and leaves general finite gamma unresolved. The present proof does not invoke that theorem as a quantified finite-exponent result.

The web retrieval of the manuscript's pinned GitHub target URL failed; the exact target was instead successfully read from the local Git object. I did not attempt a complete fresh later-literature search: the analytic counterexample is self-contained and does not depend on a claim of novelty or on the other references listed in the target.

## Fresh computational corroboration and script inspection

Before execution I inspected check_505.py. Its half-grid restriction is justified by symmetry. Reflection at the center doubles the first flux and reflection at M doubles the last flux with the opposite sign. Its stationary residual uses the correct reflected center/Dirichlet core stencil, and its flux Jacobian derivatives agree with direct differentiation. The clipping and exponent guards affect nonphysical trial iterates; accepted trajectories are checked for finiteness and [0,1] up to the stated numerical tolerance. This is ordinary floating-point integration, not a certified enclosure.

The first unprivileged reproduction attempts failed because bundled Python lacked an accessible SciPy installation, and the existing external scratch dependency directory returned access denied. This was an environment access limitation, not evidence of a script defect. A subsequent read-only escalation using those existing isolated dependencies succeeded; no package installation was required or completed.

Fresh run: Python 3.12.14, bundled NumPy 2.3.5, existing isolated SciPy 1.18.1; submitted script with meshes 10 20 40 80, default gamma multiplier 500, and output explicitly directed to pr28/independent-experiments.json. The printed output is preserved in independent-experiments-log.txt.

| M | gamma | Fresh gamma w_K | -A_h | Fresh -gamma t_h w_K |
|---:|---:|---:|---:|---:|
| 10 | 5000 | -2.31735417 | -2.31722590 | 0.69617953 |
| 20 | 10000 | -5.46771068 | -5.46736412 | 1.60876870 |
| 40 | 20000 | -11.84682201 | -11.84617081 | 3.44751462 |
| 80 | 40000 | -24.64578580 | -24.64478213 | 7.13146609 |

I separately wrote and executed independent_checks.py using NumPy only, without importing the submitted script. It implements the complete full grid using explicit reflected ghosts, checks the pressure identity at every node including the endpoints, verifies weighted diffusion cancellation, and compares a symmetric full-grid RHS with the submitted half-grid form. The largest identity error in its sampled cases is 1.14e-13, weighted diffusion cancellation error is 1.87e-13, and symmetric reduction error is 5.69e-14. It also checks the closed-form profile from M=10 through M=1280: h A_h approaches c log(2)=0.3203152046431526, and t_h A_h rises from 0.69614 to 117.70797. Its maximum linear profile residual is 8.55e-10 on the finest sampled grid, consistent with floating-point cancellation at h^-2.

Files: independent_checks.py, independent-checks.json, independent-checks-log.txt, independent-source-integrity.json, independent-experiments.json, independent-experiments-log.txt. All are new reviewer evidence in the PR28 snapshot root. To reproduce the independent checks, run the saved independent_checks.py with the bundled Python executable. To reproduce the submitted integration, use the same executable with PYTHONPATH pointing to the existing active-pr-audit-wave-steklov/deps, execute the inspected check_505.py, and pass an explicit output path in the review directory.

The computations support the argument but establish neither the infinite mesh sequence nor the exponent-selection thresholds. Neither the accepted proof nor this verdict assumes gamma=500M for every mesh.

## Defects and limitations

No mathematical correction is required by this audit. The finite-dimensional ODE comparison and implicit-function results are conventional analytic tools rather than machine-checked theorems in this package. Their applicability was independently checked above. The proof is nonconstructive in the threshold gamma_h and supplies no uniform or computable rate for it; that is sufficient for the requested counterexample.

The identity, hashes, and numerical files are reproducible supporting evidence. The floating-point solver and NumPy checks are not rigorous numerical certificates. This report is an independent AI assessment of this exact manuscript revision, not a human or formal verification record. Subject to those explicit distinctions, it audits the complete counterexample rather than a partial case or a different discretization.
