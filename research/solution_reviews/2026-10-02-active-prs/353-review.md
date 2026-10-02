# AIM 353: independent audit of the delayed NNLIF periodic branch

**Review date:** 2026-10-02. **Reviewer:** Codex review agent, conducting a fresh AI audit of the complete manuscript independently of its preparation and submitted check reports. This is neither a human review nor a formal proof-assistant verification.

**Disposition:** Accept the complete existence argument and classify AIM 353 as **Solved**. No unresolved mathematical gap was found in the precise existential target. The accepted theorem allows freely chosen **negative physical voltage thresholds**; it establishes neither a result for every prescribed threshold pair nor stability of the branch.

## Pinned materials and exact target

- [PR #23](https://github.com/MColbrook/AIM/pull/23), head `e8e9c121188cff156922ab06a4bd8333c5ec61dc`.
- Full proof: [`aim353_delayed_nnlif_periodic.tex`](../../solutions/353-delayed-nnlif-periodic-branch/aim353_delayed_nnlif_periodic.tex).
- Target: [`353-delayed-nnlif-periodic.md`](../../../problems/353-delayed-nnlif-periodic.md), read from that Git revision, whose statement matches the cited `fa98b7525fa3f78317536a8825f9cfa0ae1c369c` target.
- Proof Git-object SHA-256: `399f38a5f982b19b383a4b20b8b8199c4a4ad8451d2d43f9bfa53b407d678346`.
- Target Git-object SHA-256: `6de9293b9c49f7a20615bbd5debf597beabb84a6d5d5aa90ba3a794ea87059eb`.

The target asks for some a>0, b<0, d>0, real VR<VF and T>0 producing a nonnegative periodic density, unit mass, nonconstant firing rate, reset derivative jump, classical regularity off the reset, zero incoming flux at negative infinity and a uniformly finite second moment. It imposes no positivity of VR or VF. The proof chooses a=1, VF=bN0 and VR=VF-1. For each selected nonzero branch point these are fixed finite model parameters, even though they vary along the constructed parameter family. This is permitted by the target's existential quantifiers.

## Operator, domain and resolvent audit

1. **Stationary reset profile.** Direct differentiation and integration verify positivity, normalization, P(0)=0, -P'(0)=N0 and the derivative jump [P']=-N0 at -1. Tonelli gives the stated reciprocal firing rate m0. On the two component intervals AP=0. P and its first derivative have the Gaussian integrability needed in the chosen Hilbert space.

2. **Distributional signs.** A is the piecewise Ornstein-Uhlenbeck operator with continuity at -1, q(0)=0 and [q']=q'(0)=-Cq. The distributional second derivative therefore contributes -Cq times the reset delta; adding the positive source Cq delta cancels this singular term. Integration over both intervals gives integral Aq=q'(0)-[q']=0. The zero-mass subspace is consequently invariant. The transformed derivative jump carries the factor exp(1/4), as stated.

3. **Closed domain and compact resolvent.** The Gaussian conjugation turns the absorbing operator into the Dirichlet oscillator L=d2/dw2+1/2-w2/4. Its odd full-line oscillator modes have eigenvalues -1,-3,-5,... . The submitted local Dirichlet estimate controls the boundary derivative by the graph norm. The absorbing resolvent plus the fixed point-source Green function then controls the full piecewise H2 and w2-weighted norms. These norms are complete with the closed trace conditions, giving closedness; smooth compactly supported functions away from the exceptional points are dense. The rank-one reset correction is bounded and finite rank, so the resolvent is compact.

4. **Rank-one formula.** Independently derived q=R_D h+(Cq)g_lambda and (1-a(lambda))Cq=CR_D h. The Green-function derivative jump has the correct sign. The denominator a(lambda) is the transform of the absorbing hitting-time density. The Brownian time change for diffusion coefficient sqrt(2) has variance time exp(2t)-1, giving exactly the displayed density and normalization. Its positivity at every positive time proves |a(i xi)|<1 for nonzero xi. Its mean is m0, so 1-a(lambda)=m0 lambda+O(lambda2) near zero.

5. **Resolvent powers.** Checked the Mehler kernel normalization and the Dirichlet reflection. Its interior diagonal and mixed boundary derivative scale as t^-1/2 and t^-3/2. The corresponding spectral counting bounds imply squared resolvent-source and resolvent-trace norms O(|xi|^-3/2) and O(|xi|^-1/2), respectively. Their product supplies the required O(|xi|^-1) rank-one correction. Riemann-Lebesgue bounds the denominator away from zero for large |xi|. Near zero the at-most-simple residue is P times the mass functional; it vanishes on the zero-mass space. Thus the entire imaginary axis lies in the resolvent of A0 and the two stated multiplier bounds follow. No semigroup generation assertion is substituted for these estimates.

6. **Traces and time spaces.** The local derivative trace inequality has exponents 1/4 and 3/4, and the global first-derivative interpolation has exponents 1/2 and 1/2. The latter also controls the term wr/2 after conjugation using ||wr||2 squared <= ||r||2 ||w2r||2. Applying these inequalities to Fourier coefficients gives Cq in H^(5/4) and q_w in H^(3/2) for q in Y. The scalar trace is compact into H1 on the time circle. The Fourier resolvent estimates give the isomorphism omega*d_theta-A0:Y_s -> H^s for all required s. These facts verify the mapping and Fredholm claims used later, including the zero Fourier mode.

## Response asymptotics and nonlinear reduction

7. **Exact response.** Integration by parts gives CR_D g=integral h_lambda*g. Applying stationarity to the derivative of the backward hitting equation yields the factor lambda+1 and the numerator N0(h'(0)-h'(-1)). The resulting K(lambda) has denominator (lambda+1)(1-h(-1)). The forcing f=-P' has zero mass. The integrations at negative infinity are justified by Gaussian decay; for fixed imaginary lambda, differentiating the hitting-time formula in starting distance gives at most polynomial bounds there.

8. **Asymptotics and derivative.** At w=0 the integral formula yields sqrt(2)*Gamma((lambda+1)/2)/Gamma(lambda/2). The first gamma-ratio correction is -1/(4 lambda); multiplying by (lambda+1)^-1 adds -1/lambda and gives the stated -5/(4 lambda). For starting distance 1 the hitting-time density and its time and distance derivatives are flat at zero and exponentially decaying at infinity. Repeated integration by parts makes the remote-reset terms and their frequency derivatives smaller than every inverse power. The uniform analytic gamma-ratio remainder can be differentiated on discs inside its sector. Thus arg K(i xi)=-pi/4+5/(4xi)+O(xi^-2), and its derivative is -5/(4xi2)+O(xi^-3), with the correct nonzero sign for large xi. The differentiation of the remainder is justified, not inferred from a bare asymptotic formula on a line.

9. **Zero and higher harmonics.** The constant-input mean-time formula has m'(I)<0; differentiating its normalized stationary density in the fixed graph domain proves K(0)=N'(0)>0 with the correct sign. The high-frequency modulus bounds 0.9 N0/sqrt(xi) and 1.1 N0/sqrt(xi) imply the simultaneous separation of every harmonic n>=2 because (1.1/0.9)/sqrt(2)<1. The selected b0 is negative and the selected phase delta lies strictly between 0 and 2pi. Consequently the only critical Fourier modes are +1 and -1.

10. **Nonlinear map and complement.** The delayed trace is a fixed translation by delta in the Banach map, avoiding a derivative loss from variable-delay translation. The scalar/vector H1 product estimate makes the full quadratic feedback analytic from Y to X. Each forcing has zero mass since the density and perturbation vanish at both spatial endpoints. The compact trace perturbation gives Fredholm index zero. Fourier rank-one equations identify a two-real-dimensional kernel and range condition ell(h1)=0. The complementary condition Cq1=0 is legitimate because the chosen kernel vector satisfies Ce=1; the restricted operator is an isomorphism onto that range.

11. **Two-parameter implicit function argument.** Recomputed the reduced Jacobian after dividing by the real amplitude. The b column is -1/b0, real and nonzero. The omega column is -i*K'(i omega0)/K(i omega0); its imaginary part is minus the derivative of arg K(i omega). Contributions from derivatives of the range correction are annihilated by ell, including mixed parameter/amplitude terms. The determinant is therefore nonzero. This establishes an actual nontrivial nonlinear periodic branch, without assuming that linear instability by itself implies periodicity. The first firing-rate Fourier coefficient is exactly the branch amplitude kappa, so nonconstancy is proved.

## Positivity and all requested solution properties

12. **Positivity.** Smallness gives N>=N0/2 and |I|<=1/2 but does not by itself give a positive density in the far tail. The separate negative-part argument remedies this. Checked the conjugated equation and the sign of every term tested against -r_minus. The positive reset source contributes a nonpositive term. Constant-in-voltage transport integrates to zero. The remaining I*w term is bounded by ||wz||2 squared/16 + I2||z||2 squared. The half-line Dirichlet oscillator lower bound is 3/2, so retaining three quarters of that form gives the claimed negative coefficient -5/8+I2<=-3/8. Periodicity forces the negative part to vanish. The graph/time regularity suffices for this energy test.

13. **Regularity.** From Y_s, trace and derivative interpolation yield time exponents s+1/4 and s+1/2. Both exceed 1/2, so the scalar/vector Sobolev multiplication theorem gives a gain of 1/4 through the periodic inverse. Iteration yields all required time regularity in the graph domain. The differential equation then gives local spatial smoothness separately on the two voltage intervals. Continuity and the reset jump persist because they are fixed graph-domain conditions.

14. **Mass, moments, flux and reconstruction.** The perturbation has zero mass at every time. Gaussian weighted L2 boundedness gives the uniform second moment by Cauchy-Schwarz. The transformed graph domain bounds r and its first derivative on the lower half-line; the Gaussian prefactor therefore forces the displayed physical flux to vanish at negative infinity. The fixed coordinate translation v=w+bN0 exactly changes the drift to -w+b(N(t-d)-N0). Taking d=delta/omega and T=2pi/omega gives the original delayed PDE and its boundary flux relation, for all real times by periodic extension. A fixed finite voltage translation preserves the moment bound. Each target condition is therefore met.

## Primary-reference checks and reproducibility scope

The principal imported asymptotic result was checked at [NIST DLMF, Section 5.11(iii)](https://dlmf.nist.gov/5.11.iii), including the sector of validity of the gamma-ratio expansion. The oscillator, resolvent, trace and nonlinear arguments were checked from their derivations in the manuscript rather than borrowed from the submission's earlier report.

The literature distinctions were freshly checked against the primary sources:

- [Ikeda, Roux, Salort and Smets, publisher article](https://mna.episciences.org/10212): the 2022 result establishes periodicity of a Gaussian-wave delay reduction and gives heuristic/numerical support for that approximation.
- [Caceres, Canizo and Ramos-Lora, arXiv v1, Theorem 1.4](https://arxiv.org/html/2401.13534v1): linear stability and instability; the introduction explicitly distinguishes this from nonlinear periodic existence.
- [Carrillo and Roux, Section 1.7.2](https://arxiv.org/html/2501.06015v1): the discussion concerns the outstanding full-model periodicity question.
- [Rieutord and Salort, Theorem 1](https://arxiv.org/html/2606.17611v2): large-delay rescaled convergence, with 0<VR<VF, rather than a fixed finite-delay periodic orbit. The present proof's different admissible threshold choice is explicit.

This is an analytic existence proof; no finite numerical certificate is used or required. An optional mpmath response spot-check was attempted in the bundled Python environment but could not run because mpmath is not installed. No package was installed, and no numerical response check is claimed. All response signs and constants above were instead checked analytically, including the two separate contributions to -5/4. Repository/document compilation checks are separate from this mathematical review and cannot establish the theorem.

The acceptance recommendation is limited to the stated existential target and the pinned complete argument. It does not assert stability, uniqueness of a periodic branch, positive physical thresholds, every prescribed parameter choice, or proof-assistant verification.
