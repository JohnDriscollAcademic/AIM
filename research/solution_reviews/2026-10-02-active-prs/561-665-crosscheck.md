# Separate adversarial cross-check: AIM 561 and the additional AIM 665 proof

**Date:** 2026-10-02. **Reviewer:** a separate OpenAI Codex AI review agent. The two full arguments were read and their critical estimates reconstructed before consulting the main review records. This is an additional mathematical check, not human peer review, formal verification or a novelty assessment. No proof files were changed in this cross-check.

**Decision:** Both acceptance decisions are supported. No unresolved mathematical gap was found. AIM 561 is disproved by the stated improved upper bound; AIM 665 receives an additional proof, without a new solved count.

## AIM 561: hydrogen splitting

Reviewed [the full proof](../../solutions/562-hydrogen-trotter-disproof/PROOF.md) associated with PR #18 head `823ea0c6f9151792238d8ccbe7d64ea7d66faf5d`, against its preserved statement and the current AIM 561 target. The [main review](561-review.md) supplies the target routing and source record.

The signs are consistent: $`T_h=\lambda_h W_h^{-1}U_h=e^{-ihV}e^{-ih\Delta}`$, and the state has energy $`-1/4`$, so the comparison after $`n`$ steps is exactly the requested $`e^{iH}\psi`$. The normalization of the radial Fourier transform independently gives $`\widehat\psi=1/(2\pi(|\xi|^2+1/4)^2)`$. The state belongs to the domain needed for $`K\psi=V\psi`$; the proof does not assume the nonexistent $`V^2\psi\in L^2`$.

The free remainder bound follows from the two elementary scalar inequalities applied before radial integration. Substitution $`z=h(\rho^2+1/4)`$ gives the displayed $`h^{5/2}/(2\pi)`$ factor in its squared norm. For the resonant part the integrand is controlled by $`\min(z^{1/2},z^{-3/2})`$. Resonance intervals have width at most $`\pi\delta`$. The zero interval contributes $`O(\delta^{3/2})`$ and every positive interval contributes $`O(\delta k^{-3/2})`$. The resulting infinite sum is finite uniformly in $`h`$ and $`\delta`$. Thus large resonant shells are genuinely covered; the argument does not silently truncate them.

The discontinuous Fourier projection causes no Sobolev gap. Membership of its inverse transform in physical-space $`H^1`$ requires square integrability of the Fourier transform after multiplication by $`|\xi|`$, not a derivative of the cutoff. The denominator on the retained set is at least $`\delta`$. The bound on the truncated weighted remainder therefore proves both required norms of $`\eta_h`$, and $`(U_h-I)\eta_h=-Pd_h`$ is an exact multiplier identity.

Expanding $`(T_h-\lambda_h)(\psi+\eta_h)`$ leaves exactly $`(I-P)d_h-q_h-(W_h-I)\eta_h`$, after the unitary prefactor. The physical-space split at radius $`h`$ gives $`\|q_h\|=O(h^{3/2})`$ without any higher potential-domain assumption. Hardy's inequality applies to the correction just proved to lie in $`H^1`$ and bounds the remaining Coulomb term.

The correction is permitted to depend on the step size: it is an auxiliary comparison vector for each fixed $`n`$. Telescoping uses only unitarity and gives a factor of $`n`$ on its defect. Returning to $`\psi`$ costs exactly $`2\|\eta_h\|`$, because both the split evolution and the scalar phase preserve norm. Neither the numerical method nor the requested initial state is changed.

For $`\delta=h^{1/4}`$ and $`R=h^{-3/4}`$, the five global error exponents are $`1,3/8,3/8,1/2,3/8`$. They prove $`O(n^{-3/8})=o(n^{-1/4})`$ for the full integer sequence. This is sufficient to refute every positive eventual lower-bound constant, and makes no claim that $`3/8`$ is optimal.

## AIM 665: Fisher score and the Neumann heat semigroup

Reviewed [the full manuscript](../../solutions/618-fisher-score-heat-semigroup/aim618_solution.tex) associated with PR #19 head `5a1ebd317fafc26225948a14838da7302bc5847c`, against [the archived target](../../resolved/665-fisher-score-gradient-closure.md). The [main review](665-additional-proof-review.md) records the additional-proof decision.

The original density need only belong to $`W^{1,1}`$. This follows directly from $`u=\sqrt\rho\in H^1`$ by approximation; no boundedness of $`\rho`$ is needed. Sobolev locality gives $`\nabla u=0`$ almost everywhere on the zero set, establishing the exact score norm and $`\rho s_\rho=\nabla\rho`$. The weak integration by parts uses smooth Neumann test functions, so no boundary condition on the input density is imposed.

For each fixed positive time, $`r=P_\tau\rho`$ is smooth through the boundary and has zero normal derivative. The positive shift makes $`h=\log(r+\tau)`$ smooth, including on a zero-mass component, and $`\partial_\nu h=0`$. Thus $`h`$ lies in the $`L^2`$ Neumann generator domain. The commutation $`\Delta_N P_\tau h=P_\tau\Delta_Nh`$ is consequently legitimate; it is not applied directly to $`\rho`$ or $`\log\rho`$.

All duality steps are valid with $`\rho\in L^1`$: $`\Delta h`$, $`P_\tau\Delta h`$ and the smooth test derivatives are bounded at fixed positive time, and the symmetric heat kernel transfers the semigroup in the $`L^1`$–$`L^\infty`$ pairing. Both integrations by parts have the necessary Neumann condition. They give the exact mixed product

```math
\langle s_\rho,\nabla P_\tau h\rangle_{L^2(\rho)}
=A_\tau=\int_M\frac{|\nabla r|^2}{r+\tau}\,dV.
```

The imported estimate was checked directly in [Sturm, arXiv:2502.01915v1](https://arxiv.org/pdf/2502.01915v1), Theorem 1.1(iii) and Remark 1.2. The latter makes the geometric constant uniform in the input function. Taking $`p=2`$ and squaring produces $`c(\tau)=\exp(4S\sqrt{\tau/\pi}+C\tau)\to1`$. A smooth compact manifold with boundary can be smoothly extended across a collar into a complete ambient manifold, allowing the stated domain formulation; compactness supplies the geometric bounds and finitely many componentwise constants. Convexity is not required.

Applying this estimate to the time-dependent $`h`$ is valid because of that uniformity. Self-adjointness then gives the crucial original-weight bound $`B_\tau=\|\nabla P_\tau h\|_{L^2(\rho)}^2\le c(\tau)A_\tau`$. Cauchy–Schwarz gives $`A_\tau\le c(\tau)I(\rho)`$, also when $`A_\tau=0`$. This argument does not assume the desired density or closure theorem.

Strong $`L^1`$ continuity gives $`\sqrt{r+\tau}\to\sqrt\rho`$ in $`L^2`$. The just-proved energy bound makes these square roots bounded in $`H^1`$, and weak lower semicontinuity yields $`I(\rho)\le\liminf A_\tau`$. Together with the upper bound this gives $`A_\tau\to I(\rho)`$. Finally,

```math
0\le\|\nabla P_\tau h-s_\rho\|_{L^2(\rho)}^2
=B_\tau+I(\rho)-2A_\tau
\le I(\rho)+(c(\tau)-2)A_\tau\longrightarrow0.
```

This conclusion is in the original requested weight, including vacuum and unbounded densities. Neumann conditions on the constructed approximating potentials are an allowed special choice of $`C^1`$ potentials. The flux corollary follows by weighted Cauchy–Schwarz. The proof is confined to smooth compact geometry and does not silently extend to the separate rough-boundary chain-rule question.
