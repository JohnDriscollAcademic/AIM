# Audit of the fixed-time hydrogen Trotter disproof

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this submission-preparation session.

**Decision:** Solved under the repository's documented-independent-audit convention. The supplied argument disproves the complete recorded target by establishing an upper bound of order $`n^{-3/8}`$ for its exact initial state and splitting scheme.

**Pinned target:** Problem 562 at repository commit `61dec31d3c3ffe6e15aae8ad84ecf0968a18866d`; [original page at that revision](https://github.com/April-Hannah-Lena/AIM/blob/61dec31d3c3ffe6e15aae8ad84ecf0968a18866d/problems/562-hydrogen-trotter-lower-bound.md), [verbatim local statement](statement.md).

**Reviewed proof:** [PROOF.md](PROOF.md), SHA-256 `cac159018343ff49ddff55bedfa784bba28ffdbc570ecba00cc97c3c83045b45`.

**Current catalogue record:** [Archive 651](../../resolved/651-hydrogen-trotter-lower-bound.md). [Current integration mapping](../../solution_reviews/2026-10-02/562-merge-id-mapping.json); [original submission mapping](id-mapping.json).

**Catalogue integration:** The original audit and submission are retained at commit `1a187cd00296b87fcbbd261a161aa1b3b9a30881`. Merging upstream `fa98b7525fa3f78317536a8825f9cfa0ae1c369c` moves this record from archive 652 to 651 because upstream independently archived the Robin gap problem. The proof's catalogue link and its pinned digest have been updated; its mathematical content is unchanged.

## Provenance and scope

The contributor supplied the mathematical argument before this session. The supplied material does not identify its author. I did not originate that derivation: I read the complete supplied proof and independently rederived its operator identities, integral estimates, resonant-shell bound, perturbation estimate and final exponent balance. I also prepared the repository version, converting the math delimiters, using supported core TeX operators, placing an equation tag outside its aligned environment, and adding the target and reference links. The mathematical argument and its estimates are preserved.

This is a documented AI audit of a previously supplied derivation. The reviewer also performed the submission's formatting and catalogue maintenance; there is no additional reviewer of those edits. No human peer review, publication, proof-assistant verification or novelty priority is asserted. The date records an evidence review; the earlier literature review is preserved separately and has not been represented as a new search.

The proof is analytic. Numerical simulation and catalogue validation are not premises of the mathematical conclusion. The following audit covers all six sections of the argument, including the unbounded-operator and singular-potential issues.

## Exact target comparison

| Item | Recorded target and audited argument |
| --- | --- |
| Hilbert space | $`L^2(\mathbb R^3)`$ with Lebesgue measure. |
| Hamiltonian | $`H=-\Delta-\lvert x\rvert^{-1}`$ with the usual self-adjoint Coulomb realization. |
| Initial state | Exactly $`\psi=\psi_0=(8\pi)^{-1/2}e^{-\lvert x\rvert/2}`$. |
| Factor order and signs | Exactly $`T_h=e^{-ih\lvert x\rvert^{-1}}e^{-ih\Delta}`$, with $`S_n=T_{1/n}^n`$. |
| Time | The fixed final time is $`1`$ throughout. |
| Quantifiers | A finite constant independent of every integer $`n\ge1`$ bounds the error by $`Cn^{-3/8}`$. |
| Disproof | The scaled error $`n^{1/4}\lVert S_n\psi_0-e^{iH}\psi_0\rVert_2`$ tends to zero, contradicting every proposed $`c>0`$ for all sufficiently large $`n`$. |

## Operator domains, normalization and phases

Spherical integration gives $`\|\psi\|_2^2=\frac12\int_0^\infty r^2e^{-r}\,dr=1`$. For $`r>0`$,

```math
\Delta\psi=\left(\frac14-\frac1r\right)\psi.
```

There is no point mass at zero: the flux of the bounded radial derivative through a sphere of radius $`\varepsilon`$ is of order $`\varepsilon^2`$. Also $`\psi/r\in L^2`$. The Fourier transform computed below shows $`\psi\in H^2`$, so this distributional identity is the actual operator identity $`H\psi=-\psi/4`$. The Coulomb potential is relatively bounded with respect to the Laplacian with arbitrarily small relative bound, by Hardy's inequality and the Fourier interpolation estimate for $`\|\nabla f\|_2`$; the usual self-adjoint realization therefore applies.

With $`K=-\Delta+1/4`$, $`V=1/r`$, $`U_h=e^{ihK}`$, $`W_h=e^{ihV}`$ and $`\lambda_h=e^{-ih/4}`$, direct multiplication of the scalar phase gives

```math
K\psi=V\psi,\qquad
\lambda_hW_h^{-1}U_h=e^{-ihV}e^{-ih\Delta}=T_h,
\qquad e^{iH}\psi=e^{-i/4}\psi=\lambda_h^n\psi
\quad(h=1/n).
```

All three evolution factors are unitary. The Taylor remainders only use $`K\psi`$ and $`V\psi`$, which belong to $`L^2`$; they do not require second operator powers applied to the state.

## Free remainder and all resonant shells

For the unitary Fourier convention in the proof, the radial transform follows from

```math
\int_0^\infty r e^{-r/2}\sin(\rho r)\,dr
=\frac{\rho}{(\rho^2+1/4)^2},\qquad
\widehat\psi(\xi)=\frac{1}{2\pi(|\xi|^2+1/4)^2}.
```

This also verifies the required $`H^2`$ membership. Writing $`a=|\xi|^2+1/4`$, the integral Taylor formula and $`|e^{iz}-1|\le z`$ give

```math
|e^{iz}-1-iz|\le\min\{z^2/2,2z\},\qquad
|\widehat d_h|\le C\min\{h^2,h/a\}.
```

The radial integrals in proof equations (4)–(6) then give, uniformly for $`0<h\le1`$ and $`R\ge1`$,

```math
\|d_h\|_2^2\le Ch^{5/2},\qquad
\|\mathbf1_{|\xi|>R}\widehat d_h\|_2^2\le Ch^2/R,
\qquad
\||\xi|\mathbf1_{|\xi|\le R}\widehat d_h\|_2^2\le Ch^2R.
```

I checked both the low-frequency contribution and the tail; the split at $`h^{-1/2}`$ is valid for the entire stated range of $`h`$.

For the resonant set $`\mathcal B_{h,\delta}`$, the substitution $`z=h(\rho^2+1/4)`$ has Jacobian

```math
\rho^2\,d\rho=\frac{\sqrt{z-h/4}}{2h^{3/2}}\,dz.
```

Together with the exact Fourier normalization this gives the coefficient $`h^{5/2}/(2\pi)`$ in section 3 of the proof. Replacing $`\sqrt{z-h/4}`$ by $`\sqrt z`$ and extending the nonnegative integral to zero bounds its weight by $`C\min\{z^{1/2},z^{-3/2}\}`$.

The distance estimate $`2\sin(d/2)\ge2d/\pi`$ on $`0\le d\le\pi`$ places each resonant interval within distance $`\pi\delta/2`$ of $`2\pi k`$. The interval next to zero contributes at most $`C\delta^{3/2}`$. For each $`k\ge1`$, its length is at most $`\pi\delta`$ and $`z\ge(3\pi/2)k`$, so its contribution is at most $`C\delta k^{-3/2}`$. The convergent sum over every positive integer $`k`$ proves

```math
\|\mathbf1_{\mathcal B_{h,\delta}}\widehat d_h\|_2
\le Ch^{5/4}\delta^{1/2}.
```

No shell is omitted, and no constant depends on the number of shells below the cutoff.

## Correction vector and Coulomb terms

The correction divides $`-\widehat d_h`$ by $`e^{iha}-1`$ only on $`G=\{|\xi|\le R\}\setminus\mathcal B_{h,\delta}`$, where the denominator has modulus at least $`\delta`$. The preceding estimates imply

```math
\|\eta_h\|_2\le Ch^{5/4}/\delta,\qquad
\|\nabla\eta_h\|_2\le ChR^{1/2}/\delta.
```

The sharp Fourier cutoff causes no domain problem: membership in $`H^1`$ uses multiplication of the Fourier transform by $`\xi`$, not differentiation of that transform. Hence the correction is an admissible $`H^1`$ vector. The identity $`(U_h-I)\eta_h=-Pd_h`$ holds exactly as an $`L^2`$ Fourier-multiplier identity.

Expanding $`U_h-W_h`$ on $`\psi+\eta_h`$ gives the sign-sensitive residual

```math
(T_h-\lambda_h)(\psi+\eta_h)
=\lambda_hW_h^{-1}
\bigl((I-P)d_h-q_h-(W_h-I)\eta_h\bigr).
```

The complement of $`G`$ is covered by the high-frequency tail and the resonant set, so the triangle inequality yields exactly the two terms in proof equation (13).

For the potential remainder, split physical space at $`r=h`$. Boundedness of $`\psi`$ and the two elementary exponential estimates give

```math
\|q_h\|_2^2
\le C\left(h^2\int_0^h dr+h^4\int_h^\infty r^{-2}\,dr\right)
\le Ch^3.
```

This is valid even though $`V^2\psi\notin L^2`$. Hardy's inequality, proved in the supplied argument by integration by parts and density, applies to the correction and gives

```math
\|(W_h-I)\eta_h\|_2
\le h\|\eta_h/r\|_2
\le2h\|\nabla\eta_h\|_2
\le Ch^2R^{1/2}/\delta.
```

In the integration-by-parts proof of Hardy's inequality, removing a ball of radius $`\varepsilon`$ introduces a boundary term of order $`\varepsilon`$ for smooth functions, which vanishes. Thus the singularity does not invalidate that step. No unbounded commutator or second-order Taylor expansion on the ground state is being assumed.

## Iteration, parameter balance and conclusion

The telescoping identity is an identity of bounded operators $`T_h`$ and $`\lambda_h I`$, so it applies without a generator-domain requirement on the comparison vector. Unitarity bounds the propagated residual by $`n`$ times its one-step norm. Replacing the comparison vector by the actual initial state costs at most $`2\|\eta_h\|_2`$. Therefore

```math
\|T_h^n\psi-\lambda_h^n\psi\|_2
\le C\left(h^{5/4}/\delta+R^{-1/2}
+h^{1/4}\delta^{1/2}+h^{1/2}+hR^{1/2}/\delta\right).
```

The choices $`\delta=h^{1/4}`$ and $`R=h^{-3/4}`$ satisfy all earlier restrictions. I checked the five resulting powers individually:

| Term | Power of $`h`$ |
| --- | --- |
| $`h^{5/4}/\delta`$ | $`h`$ |
| $`R^{-1/2}`$ | $`h^{3/8}`$ |
| $`h^{1/4}\delta^{1/2}`$ | $`h^{3/8}`$ |
| $`h^{1/2}`$ | $`h^{1/2}`$ |
| $`hR^{1/2}/\delta`$ | $`h^{3/8}`$ |

For $`h\le1`$ their sum is at most a constant times $`h^{3/8}`$. Substituting $`h=1/n`$ and the checked eigenstate phase gives the claimed global error bound for the original state. Multiplying it by $`n^{1/4}`$ gives an upper bound $`Cn^{-1/8}\to0`$, contradicting the precise eventual lower-bound assertion.

The supplied proof therefore resolves the full recorded target. I found no unresolved mathematical gap in these steps. This conclusion makes no claim that the upper exponent is optimal, or that the same result holds for arbitrary initial states. Sharp one-step errors of order $`h^{5/4}`$ are compatible with the argument, which controls their accumulation through an auxiliary approximate eigenvector.

## Evidence and reproduction

The [proof](PROOF.md) and [unchanged statement](statement.md) contain the mathematical inputs. [SHA256SUMS](SHA256SUMS) pins this review, the proof, the statement and the ID mapping. From the repository root, verify the package with `sha256sum -c research/solutions/562-hydrogen-trotter-disproof/SHA256SUMS` (or `shasum -a 256 -c` on macOS).

Repository structure and generated indexes can be checked with `python3 scripts/catalogue.py --check`. These checks validate the submission's structure, links and formatting; the analytic audit above supplies the mathematical evidence for the status decision.
