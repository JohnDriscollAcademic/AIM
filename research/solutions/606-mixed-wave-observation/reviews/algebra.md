# Final AI audit of the proposed solution to AIM 606

- **Date:** 2026-10-02.
- **Reviewer:** Codex agent `scout_algebra`, reviewing separately from the proof
  author `scout_pde` within the same collaborative AI session.
- **Review type:** AI mathematical audit. No human review, external peer review,
  formal verification, or Lean verification is claimed.
- **File reviewed in full:**
  `research/solutions/606-mixed-wave-observation/PROOF.md`.
- **Exact SHA-256:**
  `4f8f8221548fc5c050ba95fe0a1aaea60173200e0a31014d402e92e700476135`.
- **Target baseline:** Problem 606 at repository commit
  `37a25361f243be77daea0ae0b3c5167b57f1b5f3`.

## Result of this review

I read all sections of this exact proof revision and found no mathematical gap
or unresolved objection in its argument. The proof establishes the complete
stated target, conditional only on the explicitly cited published spectral and
modal results of Castro and Micu. It does not merely establish a special case
or a weaker large-time statement. Numerical diagnostics played no role in the
logical conclusion of this final review.

This conclusion is an AI audit of a mathematical argument, with the limitations
identified above. Keeping the contribution labelled “Solution claimed” pending
independent external review is appropriate.

## Comparison with the full target

The theorem uses exactly the mass, stiffness, and sampled potential matrices
of Problem 606, together with exactly its energy and its two-component boundary
observation. Its assumptions cover every bounded measurable nonnegative
potential with the specified pointwise representative. The proof uses the
pointwise bound rather than confusing it with an essential supremum.

For every fixed `T>2`, Section 5 gives a positive constant independent of all
mesh sizes and all initial data. The finite collection of coarse meshes is
explicitly included. For every fixed `0<T<2`, Section 6 constructs admissible
meshes and exact nonzero solutions whose observation-to-energy ratios tend to
zero. These two assertions imply exactly that the infimum in Problem 606 is
`T_*(a)=2`. The target does not require deciding whether the estimate holds at
the single endpoint `T=2`; the manuscript correctly makes no such claim.

## Published inputs and their applicability

I previously checked the primary source
<https://arxiv.org/html/2501.11352v1>, specifically Lemma 4, Lemma 5 / (31),
Theorem 9 / (50), (48), and the finite-difference proof using the maximum of
the sampled potential values. The manuscript identifies the corresponding
published article, <https://doi.org/10.1007/s00211-025-01489-0>.

The source results provide the mass-orthonormal eigenbasis, simplicity and
positivity, a uniform positive separation of the signed frequencies on fine
meshes, and the needed lower and upper modal boundary estimates. They are
applicable to bounded pointwise samples. The separate continuity hypothesis
in the source's approximation/convergence results is not imported into or
needed for this proof. The first eigenvector component is also proved nonzero
directly in Section 2, so the later divisions are justified.

I checked the source statements and their use here; this audit does not claim
to have independently reproved every result of the published source.

## Checks of the new argument

### Spectral sandwich and asymptotic gap

The exact identity `h I=M_h+(h^2/4)K_h` gives the asserted ordered quadratic
forms. Applying generalized finite-dimensional min-max yields (3.1), with
the correct zero-potential frequencies `(2/h)tan(pi jh/2)`. Rationalization
gives (3.2) with the factors `1/2` and `1/8` as written.

Subtracting the upper bound at `j` from the lower bound at `j+1`, using the
monotonicity of `sec^2`, and completing the square gives precisely the error
term `A^2 h^2/(64 pi)` in (3.3). The implication `j<N => h<=1/(j+2)` is valid,
so (3.4) supplies a tail cutoff independent of the mesh. The signed tails are
also separated from each other by at least `2 pi J`. No bounded perturbation
in the mass-normalized operator norm is incorrectly assumed.

### Cosine-kernel Fourier estimates

I independently checked the Fourier transform of the compactly supported
cosine weight, including its diagonal value. For ordered separated frequencies,
the `n`th neighbor is at distance at least `n gamma`; the resulting absolute
row sum is bounded by the displayed series. The identity

`sum_(n>=1) 1/(n^2-1/4)=2`

follows by telescoping, and the off-diagonal quadratic-form estimate gives
exactly the coefficient `2/alpha-8 alpha/gamma^2`. It is strictly positive
under the stated condition `S>2 pi/gamma`.

For the upper bound, `L=max(2s,4 pi/g)` ensures both the required separation
bound and a weight of at least `1/sqrt(2)` on the interval of interest. Thus
(4.2) is valid with a constant independent of the number or magnitude of the
frequencies. These calculations supply the full Fourier ingredients within
the manuscript rather than relying on an unstated version of Ingham's theorem.

### Uniform finite insertion

The shifted difference cancels exactly the newly inserted frequency. The
integration over shifts gives the factor `8 epsilon` in (4.4). The displayed
quantity `d(g,epsilon)` is strictly positive and independent of the actual
frequency values, by global separation.

The manuscript then uses the uniform upper bound (4.2) to recover the added
coefficient. This is essential: a triangle estimate with a growing number of
modes would not suffice. It is handled correctly. The number of insertions is
fixed by the tail cutoff and all resulting constants remain independent of
the mesh. The proof also treats deletion of fewer than the allowed number of
frequencies by enlarging the final interval if necessary.

### Application to the two observation components

The factors in the modal expansion (5.1) make the conserved energy exactly
the squared coefficient norm; the positive and negative mode cross terms
cancel between position and velocity energy. The two observed sums have the
written `1/sqrt(2)` factors and the signed velocity coefficient. Applying the
same scalar Fourier bound to each and then the modal lower estimate proves
(5.2). Distinct frequencies and the nonzero first components imply positive
definiteness of the coarse-mesh observation Gramian for every positive time.

### Explicit failure below time two

For the normalized coefficients of `R_m`, the lower bound on their original
Euclidean norm follows from their `ell^1` norm being one and Cauchy–Schwarz.
On `[0,T]`, the maximum modulus of the base cosine is exactly bounded by
`rho=cos(pi(2-T)/4)<1`; hence both estimates in (6.1) are valid.

The choices `J_m=(m+1)^2` and `h_m=(m+1)^(-6)` define actual integer meshes,
and the entire block is inside the spectrum, including for `m=1`. The three
error orders listed after (6.2) are correct. In particular, the frequency
defect is `O_A(m^(-2))` while the block frequencies are `O_A(m^2)`.

Equation (6.3) is an exact discrete solution with a nonzero coefficient vector.
The first observed component tends to zero using the coefficient `ell^1`
bound and the frequency defect. The second tends to zero at the stated rate
because of its extra factor of `h_m`. The energy identity in the last display
is correct and the published modal upper bound gives its uniform positive
lower bound. No upper bound on these solutions' energy is needed for the
ratio argument. No convergence of sampled potentials to a continuum potential
is used. The real/imaginary decomposition also justifies the optional
real-solution conclusion.

## Objections and residual scope

No unresolved mathematical objection was found in this exact revision.
The source results remain explicitly cited external inputs. The claim covers
the infimum threshold and does not settle the endpoint `T=2`. It remains an
AI-generated contribution awaiting external mathematical review.
