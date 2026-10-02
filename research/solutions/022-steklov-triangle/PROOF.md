# The equilateral triangle maximizes the perimeter-normalized first Steklov eigenvalue among triangles

**Target:** Problem 022 at `fa98b7525fa3f78317536a8825f9cfa0ae1c369c` (numbered 023 at `37a25361f243be77daea0ae0b3c5167b57f1b5f3`); [unchanged statement](statement.md). Only the case $`n=3`$ is treated.

**Status:** Partial result claimed — complete computer-assisted proof of the case $`n=3`$ (triangles), awaiting independent review. Nothing is claimed for $`n\ge4`$.

**Prepared:** 2026-10-02 by Claude Opus 5.5 (Anthropic, in Claude Code), submitted by GitHub user cthalhammer. The construction, the certified computations, a self-review and a separate referee pass by another AI agent of the same session were all AI-performed. No independent or human audit is claimed.

**Reproduction:** `python3 certify/main.py` from this folder (about 20 s) prints `ALL CERTIFIED CHECKS PASSED` only if every check succeeds. See [README](README.md) and [ENVIRONMENT](ENVIRONMENT.txt).

## Theorem

For a bounded Lipschitz domain $`\Omega\subset\mathbb R^2`$ let

```math
\sigma_1(\Omega)=\inf\Big\{\frac{\int_\Omega|\nabla u|^2}{\int_{\partial\Omega}u^2}\;:\;u\in H^1(\Omega),\ \int_{\partial\Omega}u\,ds=0,\ u|_{\partial\Omega}\ne0\Big\}
```

be the first positive Steklov eigenvalue. For every triangle $`T`$,

```math
\sigma_1(T)\,\mathop{\mathrm{Per}}(T)\le\sigma_1(E)\,\mathop{\mathrm{Per}}(E),
```

where $`E`$ is equilateral, with equality if and only if $`T`$ is equilateral. Since $`\sigma_1\mathop{\mathrm{Per}}`$ is invariant under similarities, this is exactly the case $`n=3`$ of problem 022 (fixed perimeter $`L`$, convex polygons with at most three sides).

Certified value (Lemma 3):

```math
\sigma_1(E)\mathop{\mathrm{Per}}(E)\in[3.87246159577280656925872,\ 3.87246159577280656925874].
```

For $`E`$ with circumradius $`1`$, $`\sigma_1(E)\in[0.7452555815819725420924091,\ 0.7452555815819725420924117]`$. In the normalization $`\mathop{\mathrm{Per}}=2\pi`$ of Cheng–Gui–Hu–Li–Yao, $`\sigma_1(\Omega_3)=0.61632140490077122907605\pm3\cdot10^{-25}`$.

**Notation.** $`E`$ is the equilateral triangle with circumradius $`1`$ and counterclockwise vertices $`V_0=(0,1)`$, $`V_1=(-\sqrt3/2,-1/2)`$, $`V_2=(\sqrt3/2,-1/2)`$; side $`\sqrt3`$, $`\mathop{\mathrm{Per}}(E)=3\sqrt3`$, $`|E|=3\sqrt3/4`$. Edge $`e_k`$ runs from $`V_k`$ to $`V_{k+1}`$ (indices mod $`3`$) with unit tangent $`\tau_k`$. We identify $`\mathbb R^2`$ with $`\mathbb C`$. "Arb" denotes the ball arithmetic of FLINT/Arb (python-flint), which returns rigorous enclosures with outward rounding.

## 0. Standard facts used

**(F1) Min–max.** For a bounded Lipschitz domain the Steklov eigenvalues $`0=\sigma_0<\sigma_1\le\sigma_2\le\cdots`$ are the min–max values of $`R(u)=\int|\nabla u|^2/\int_{\partial\Omega}u^2`$ on $`H^1(\Omega)`$; $`\sigma_k`$ $`(k\ge1)`$ is the $`k`$-th min–max value on $`\{\int_{\partial\Omega}u=0\}`$. In particular $`\sigma_1(\Omega)\le R(u)`$ for every admissible $`u`$.

**(F2) Dirichlet-to-Neumann operator.** $`\Lambda`$ on $`L^2(\partial\Omega)`$ is the nonnegative self-adjoint operator of the closed form $`q(f)=\int_\Omega|\nabla Hf|^2`$ on $`H^{1/2}(\partial\Omega)`$, where $`Hf`$ is the harmonic extension. Its spectrum is discrete and equals $`\{\sigma_k\}`$. If $`u`$ is a harmonic polynomial and $`f=u|_{\partial\Omega}`$, then $`f\in D(\Lambda)`$ and $`\Lambda f=\partial_\nu u`$, by Green's formula $`\int_\Omega\nabla u\cdot\nabla Hg=\int_{\partial\Omega}\partial_\nu u\,g`$ on Lipschitz domains. $`\Lambda`$ commutes with the isometries of $`\Omega`$ acting on $`L^2(\partial\Omega)`$.

**(F3) Payne–Weinberger** (1960; complete proof by Bebendorf, 2003). For a convex domain $`K`$ of diameter $`d`$ and $`w\in H^1(K)`$, $`\|w-\bar w_K\|_{L^2(K)}^2\le(d/\pi)^2\|\nabla w\|_{L^2(K)}^2`$.

**(F4) Temple's inequality.** Let $`A`$ be self-adjoint, $`\lambda_1<\rho`$, $`\sigma(A)\subset\{\lambda_1\}\cup[\rho,\infty)`$, $`f\in D(A)`$, $`\|f\|=1`$ and $`\eta=\langle Af,f\rangle<\rho`$. Then

```math
\lambda_1\ge\eta-\frac{\|Af\|^2-\eta^2}{\rho-\eta}.
```

*Proof.* $`(s-\lambda_1)(s-\rho)\ge0`$ on $`\sigma(A)`$: it vanishes at $`s=\lambda_1`$, and both factors are nonnegative for $`s\ge\rho>\lambda_1`$. Hence $`\langle(A-\lambda_1)(A-\rho)f,f\rangle\ge0`$, i.e. $`\|Af\|^2-(\lambda_1+\rho)\eta+\lambda_1\rho\ge0`$. Solve for $`\lambda_1`$ using $`\rho-\eta>0`$. ∎

**(F5) Descartes' rule for real-rooted polynomials.** If all roots of $`p\in\mathbb R[x]`$ are real, the number of positive roots, with multiplicity, equals the number of sign changes in its coefficient sequence. Indeed, Descartes bounds the positive roots of $`p(x)`$ and of $`p(-x)`$; the two bounds sum to at most $`\deg p`$ minus the multiplicity of the root $`0`$, and the two root counts sum to exactly that.

## 1. Moduli coordinates

**Lemma 1.** For symmetric $`S`$ with $`\mathop{\mathrm{tr}}S=0`$ put $`T_S=\exp(S)E`$. Every triangle is similar, possibly through a reflection, to some $`T_S`$, and $`T_S`$ is equilateral if and only if $`S=0`$. Write $`S=r\hat S(\varphi)`$ with

```math
\hat S(\varphi)=\begin{pmatrix}\cos\varphi&\sin\varphi\\ \sin\varphi&-\cos\varphi\end{pmatrix},\qquad r=\|S\|\ge0,
```

where $`\|S\|`$ is the spectral norm (the eigenvalues of $`S`$ are $`\pm r`$). Then $`\hat S^2=I`$, $`\exp(S)=\cosh r\,I+\sinh r\,\hat S`$ and $`\det\exp(S)=1`$.

*Proof.* A triangle is $`T=AE+b`$ for an invertible affine map matching vertices. Polar decomposition gives $`A=QP`$ with $`Q`$ orthogonal and $`P`$ symmetric positive definite; $`P=\lambda\exp(S)`$ with $`\lambda=(\det P)^{1/2}`$ and $`S=\log P-\tfrac12(\mathop{\mathrm{tr}}\log P)I`$. So $`T=Q(\lambda T_S)+b`$, and $`\sigma_1\mathop{\mathrm{Per}}`$ is invariant under isometries and dilations. If $`T_S`$ is equilateral, the affine map $`\exp(S)`$ sends the circumcircle of $`E`$ (its Steiner circum-ellipse, the unique centred ellipse through the vertices) to a circle. Hence $`\exp(S)`$ is a similarity, and a symmetric positive definite similarity with determinant $`1`$ is $`I`$; so $`S=0`$. ∎

## 2. A lower bound for the third eigenvalue of E

**Lemma 2.** $`\sigma_3(E)\ge\rho:=1388851/10^6=1.388851`$.

*Proof.* (a) *Abstract bound* (You–Xie–Liu, SIAM J. Numer. Anal. 57 (2019), Theorem 2.4, re-proved in the form used). Let $`V=H^1(E)`$, let $`V_h`$ be the Crouzeix–Raviart (CR) space of a triangulation $`\mathcal T_h`$ of $`E`$, and $`\tilde V=V+V_h`$. Fix $`\tau>0`$ and set

```math
M(u,v)=\sum_{K\in\mathcal T_h}\int_K\nabla u\cdot\nabla v+\tau\,m(u)m(v),\qquad m(u)=\int_{\partial E}u,\qquad N(u,v)=\int_{\partial E}uv.
```

$`M`$ is an inner product on $`\tilde V`$. If $`\sum_K\|\nabla u\|_K^2=0`$ then $`u`$ is piecewise constant. For $`u=v+v_h`$ with $`v\in V`$, $`v_h\in V_h`$, the jump of $`u`$ across an interior edge equals the jump of $`v_h`$, which has zero mean there (CR continuity at midpoints). So all jumps vanish, $`u`$ is constant, and $`m(u)=0`$ forces $`u=0`$.

Let $`P_h`$ be the $`M`$-orthogonal projection $`\tilde V\to V_h`$, and suppose $`\|u-P_hu\|_N\le C_h\|u-P_hu\|_M`$ for all $`u\in V`$. Let $`\lambda_{h,1}\le\lambda_{h,2}\le\cdots`$ be the finite eigenvalues of the pencil $`(M,N)`$ on $`V_h`$ and $`\lambda_k`$ the $`k`$-th min–max value of $`M/N`$ on $`V`$. Then

```math
\lambda_k\ge\frac{\lambda_{h,k}}{1+C_h^2\lambda_{h,k}}.
```

Indeed, let $`u_{h,i}`$ be $`M`$-orthonormal discrete eigenvectors. Any $`k`$-dimensional $`\mathcal S\subset V`$ on which $`N`$ is positive definite contains $`v\ne0`$ with $`M(v,u_{h,i})=0`$ for $`i<k`$. Then $`P_hv`$ is $`M`$-orthogonal to $`u_{h,1},\dots,u_{h,k-1}`$. Expanding in eigenvectors and the kernel of $`N`$ on $`V_h`$ gives $`\|P_hv\|_N^2\le\lambda_{h,k}^{-1}\|P_hv\|_M^2`$, and

```math
\|v\|_N\le\lambda_{h,k}^{-1/2}\|P_hv\|_M+C_h\|v-P_hv\|_M\le\big(\lambda_{h,k}^{-1}+C_h^2\big)^{1/2}\|v\|_M
```

by Cauchy–Schwarz and Pythagoras. Hence $`\max_{\mathcal S}M/N\ge\lambda_{h,k}/(1+C_h^2\lambda_{h,k})`$.

(b) *Identification of eigenvalues.* On $`V`$ the $`(M,N)`$-eigenvalues are $`\{\sigma_k\}_{k\ge1}`$ (Steklov eigenfunctions, $`m=0`$) and $`\tau\mathop{\mathrm{Per}}(E)`$ (constants). On $`V_h`$ they are $`\tau\mathop{\mathrm{Per}}(E)`$ (constants) and the nonzero eigenvalues of the pencil $`(K,N)`$, where $`K`$ is the stiffness matrix, because $`K\mathbf 1=0`$ and $`N`$-orthogonality to $`\mathbf1`$ means $`m=0`$. For $`\tau`$ large, $`\lambda_3=\sigma_3(E)`$ and $`\lambda_{h,3}`$ is the third nonzero eigenvalue of $`(K,N)`$; $`C_h`$ below does not depend on $`\tau`$.

(c) *$`P_h`$ is CR interpolation on $`V`$.* The interpolant $`\Pi_hu`$ is defined element by element by $`\int_e\Pi_hu=\int_eu`$ on every edge. For $`v_h\in V_h`$,

```math
\sum_K\int_K\nabla(u-\Pi_hu)\cdot\nabla v_h=\sum_K\sum_{e\subset\partial K}(\nabla v_h|_K\cdot n_e)\int_e(u-\Pi_hu)=0,
```

and $`m(u-\Pi_hu)=\sum_{e\subset\partial E}\int_e(u-\Pi_hu)=0`$. So $`M(u-\Pi_hu,v_h)=0`$, i.e. $`P_hu=\Pi_hu`$.

(d) *Trace constant.* Let $`K`$ be a triangle, $`e`$ an edge, $`P_3`$ the opposite vertex, $`H`$ the height onto $`e`$ and $`h_K`$ the longest edge. For $`w\in H^1(K)`$, the divergence theorem applied to $`(x-P_3)w^2`$, with $`(x-P_3)\cdot n=0`$ on the two edges through $`P_3`$ and $`=H`$ on $`e`$, gives

```math
H\|w\|_e^2=2\|w\|_K^2+\int_K(x-P_3)\cdot\nabla(w^2)\le2\|w\|_K^2+2h_K\|w\|_K\|\nabla w\|_K.
```

Apply this to $`v=w-\bar w_K`$ and use (F3) with $`d=h_K`$: $`H\|v\|_e^2\le(2/\pi^2+2/\pi)h_K^2\|\nabla w\|_K^2`$. If $`\int_ew=0`$ then $`w|_e=v|_e-\mathrm{mean}_e(v)`$, so $`\|w\|_e\le\|v\|_e`$. Hence, for $`w=u-\Pi_hu`$,

```math
\|u-\Pi_hu\|_{0,e}^2\le C_e^2|u-\Pi_hu|_{1,K}^2,\qquad C_e^2=\Big(\frac2{\pi^2}+\frac2\pi\Big)\frac{h_K^2}{H}.
```

Summing over boundary edges, with every element having at most two boundary edges, $`\|u-\Pi_hu\|_N^2\le2\max C_e^2\,\|u-\Pi_hu\|_M^2`$. So $`C_h^2=2\max C_e^2`$.

(e) *Computation* (`certify/cr_mesh.py`, `certify/cert_rho.py`). The uniform mesh of $`E`$ has $`n^2=256`$ equilateral elements of side $`h=\sqrt3/16`$ $`(n=16)`$ and $`408`$ CR degrees of freedom; every element has at most two boundary edges (checked). For equilateral elements $`h_K^2/H=2h/\sqrt3=2/n`$, so $`C_h^2=(4/n)(2/\pi^2+2/\pi)\in[0.2098155349130642,\,0.2098155349130643]`$.

With the CR basis $`\varphi_i=1-2\lambda_i`$, $`K=(2/\sqrt3)K_{\mathrm{int}}`$ and $`N=(h/3)N_3`$ with integer local matrices: $`K_{\mathrm{int}}^{\mathrm{loc}}`$ has diagonal $`2`$ and off-diagonal $`-1`$, and on a boundary edge $`N_3^{\mathrm{loc}}`$ has own-dof entry $`3`$, entries $`1,1`$ for the other two dofs, coupling $`-1`$ between them and $`0`$ between own and other. Thus $`Kx=\lambda Nx`$ if and only if $`K_{\mathrm{int}}x=(\lambda/2n)N_3x`$. For $`\mu=196/100`$ we have $`\mu/(2n)=49/800`$, and $`A=800K_{\mathrm{int}}-49N_3`$ is an integer symmetric matrix. Its characteristic polynomial is computed exactly over the integers (FLINT), and (F5) gives inertia $`(\text{neg},\text{zero},\text{pos})=(3,0,405)`$.

Since $`K+N`$ is positive definite on $`V_h`$, a congruence shows that the number of negative eigenvalues of $`K-\mu N`$ equals the number of finite eigenvalues of $`(K,N)`$ below $`\mu`$, including the eigenvalue $`0`$ of the constants. Thus exactly $`0,\lambda_{h,1},\lambda_{h,2}`$ lie below $`\mu`$, and $`\lambda_{h,3}\ge\mu=1.96`$.

(f) Since $`x\mapsto x/(1+C_h^2x)`$ increases, $`\sigma_3(E)\ge\mu/(1+C_h^2\mu)\ge1.38885104936096627\ge1.388851`$ (Arb). ∎

Floating-point CR values for $`n=16`$, not used: $`\lambda_{h,1}=\lambda_{h,2}=0.74357`$, $`\lambda_{h,3}=1.96910`$, converging from below to $`0.745256`$ and $`2`$. Also, $`\mathop{\mathrm{Im}}z^3+1/4`$ is an exact eigenfunction with eigenvalue $`2`$, so $`\sigma_3(E)\le2`$; numerically $`\sigma_3(E)=2`$, but only $`1.388851\le\sigma_3(E)\le2`$ is proved here.

## 3. Symmetry, the first eigenspace of E, and its eigenvalue

Let $`s(x,y)=(-x,y)`$ and let $`R`$ be the rotation by $`2\pi/3`$; they generate the symmetry group $`D_3`$ of $`E`$. On functions put $`(\mathcal Rf)(p)=f(R^{-1}p)`$ and $`(sf)(p)=f(sp)`$. Define the **sector**

```math
\mathcal S=\{f\in L^2(\partial E):\ sf=-f,\ f+\mathcal Rf+\mathcal R^2f=0\}.
```

$`\mathcal S`$ is a closed $`\Lambda`$-invariant subspace by (F2) and lies in $`\{\int_{\partial E}f=0\}`$. For $`F(z)=\sum_kc_ka_kz^k`$ with $`k\in\mathcal K:=\{k\ge1:3\nmid k\}`$, $`a_k=1`$ for odd $`k`$ and $`a_k=-i`$ for even $`k`$, the trace of $`w=\mathop{\mathrm{Re}}F`$ lies in $`\mathcal S`$: $`\mathop{\mathrm{Re}}z^k`$ ($`k`$ odd) and $`\mathop{\mathrm{Im}}z^k`$ ($`k`$ even) are odd under $`z\mapsto-\bar z`$, and $`\sum_j\omega^{jk}=0`$ for $`3\nmid k`$, $`\omega=e^{2\pi i/3}`$.

**Trial function** (`certify/cert_E.py`). $`\tilde w_1=\mathop{\mathrm{Re}}F`$ with $`k\in\mathcal K`$, $`k\le25`$ ($`17`$ terms). Its coefficients are the exact rationals stored in `certify/trial_coeffs.json`. They were produced once by the non-rigorous helper `certify/make_trial_coeffs.py`; their origin is irrelevant for rigour. All quantities below are integrals of polynomials in the edge parameter $`t\in[0,1]`$, with $`z=V_k+t(V_{k+1}-V_k)`$ and $`ds=\sqrt3\,dt`$, computed exactly in Arb at 320 bits:

```math
n_0=\int_{\partial E}\tilde w_1^2,\qquad n_1=\int_{\partial E}\tilde w_1\,\partial_\nu\tilde w_1=\int_E|\nabla\tilde w_1|^2,\qquad n_2=\int_{\partial E}(\partial_\nu\tilde w_1)^2,
```

with $`\partial_\nu\mathop{\mathrm{Re}}F=\mathop{\mathrm{Re}}(F'(z)\nu)`$ and $`\nu=-i(V_{k+1}-V_k)/\sqrt3`$. The results are $`\tilde\lambda:=n_1/n_0\in0.745255581581972542092411648839\pm2\cdot10^{-31}`$ and $`\varepsilon^2:=n_2/n_0-\tilde\lambda^2\in[1.604598889\cdot10^{-24}\pm2.3\cdot10^{-34}]`$, so $`\varepsilon^2\le1.6046\cdot10^{-24}`$.

**Lemma 3.** (i) $`\sigma_1(E)=\sigma_2(E)<\sigma_3(E)`$. The first eigenspace $`W`$ is two-dimensional: $`W=\mathop{\mathrm{span}}\{f^*,\mathcal Rf^*\}`$ for any nonzero $`f^*\in W\cap\mathcal S`$, and $`W\cap\mathcal S`$ is one-dimensional.
(ii) $`\Lambda`$ restricted to $`\mathcal S`$ has the simple lowest eigenvalue $`\sigma_1(E)`$, and the rest of its spectrum lies in $`[\rho,\infty)`$.
(iii) $`\sigma_1(E)\in[\sigma_{\mathrm{lo}},\sigma_{\mathrm{hi}}]=[0.7452555815819725420924091,\ 0.7452555815819725420924117]`$.

*Proof.* (i) Since $`\tilde\lambda<\rho`$ is the Rayleigh quotient of $`\tilde w_1|_{\partial E}\in\mathcal S`$, the lowest eigenvalue $`\sigma^*`$ of $`\Lambda|_{\mathcal S}`$ satisfies $`\sigma^*\le\tilde\lambda<\rho`$. Let $`f^*\in\mathcal S`$ be an eigenfunction. Then $`\mathcal Rf^*`$ is an eigenfunction for $`\sigma^*`$, and it is not a multiple of $`f^*`$: $`\mathcal Rf^*=cf^*`$ forces $`c^3=1`$ with $`c`$ real, so $`c=1`$, and then $`3f^*=f^*+\mathcal Rf^*+\mathcal R^2f^*=0`$. So $`\sigma^*`$ has multiplicity at least $`2`$, $`\sigma^*>0`$ because $`f^*`$ has mean zero, and $`\sigma^*<\rho\le\sigma_3(E)`$ by Lemma 2. Hence $`\sigma_1=\sigma_2=\sigma^*<\sigma_3`$ and $`W=\mathop{\mathrm{span}}\{f^*,\mathcal Rf^*\}`$.

In this basis $`s`$ acts by $`\begin{pmatrix}-1&1\\0&1\end{pmatrix}`$, whose $`(-1)`$-eigenspace is one-dimensional. Indeed, $`(s\mathcal Rf)(p)=f(R^{-1}sp)=f(sRp)=(\mathcal R^{-1}sf)(p)`$ because $`sRs=R^{-1}`$; so $`sf^*=-f^*`$ and $`s(\mathcal Rf^*)=\mathcal R^{-1}(-f^*)=-\mathcal R^2f^*=f^*+\mathcal Rf^*`$.

(ii) Every eigenvalue of $`\Lambda|_{\mathcal S}`$ is some $`\sigma_k`$ with $`k\ge1`$. Its $`\sigma_1`$-eigenspace is $`W\cap\mathcal S`$, one-dimensional by (i). Any other eigenvalue differs from $`\sigma_1=\sigma_2`$, so it equals some $`\sigma_k`$ with $`k\ge3`$ and is at least $`\sigma_3\ge\rho`$. As $`\Lambda|_{\mathcal S}`$ has compact resolvent, $`\sigma(\Lambda|_{\mathcal S})\subset\{\sigma_1\}\cup[\rho,\infty)`$ with $`\sigma_1`$ simple.

(iii) The upper bound is $`\sigma_1=\sigma^*\le\tilde\lambda`$. For the lower bound, (F4) applied to $`\Lambda|_{\mathcal S}`$ with the normalized trace of $`\tilde w_1`$, which lies in $`D(\Lambda)`$ by (F2), gives $`\sigma_1\ge\tilde\lambda-\varepsilon^2/(\rho-\tilde\lambda)`$, evaluated in Arb. ∎

Hence $`\sigma_1(E)\mathop{\mathrm{Per}}(E)=3\sqrt3\,\sigma_1(E)\in[3.87246159577280656925872,\ 3.87246159577280656925874]`$, rounded outward.

## 4. The exact first eigenfunctions and their moments

Let $`\tilde f_1=\tilde w_1|_{\partial E}`$, $`f_1=P_W\tilde f_1`$ (orthogonal projection onto $`W`$; $`P_W`$ commutes with $`D_3`$, so $`f_1\in W\cap\mathcal S`$), $`g_1=\tilde f_1-f_1`$, and let $`q=\Lambda\tilde f_1-\tilde\lambda\tilde f_1`$ be the residual, with $`\|q\|^2=\varepsilon^2n_0`$.

**Lemma 4.** $`\|g_1\|_{L^2(\partial E)}\le\delta_0:=\|q\|/(\rho-\tilde\lambda)`$ and $`\|\nabla G_1\|_{L^2(E)}\le\delta_1:=\sqrt\rho\,\|q\|/(\rho-\tilde\lambda)`$, where $`G_1=Hg_1`$. In Arb, $`\delta_0\le3.2534\cdot10^{-12}`$ and $`\delta_1\le3.8341\cdot10^{-12}`$.

*Proof.* $`g_1`$ lies in the spectral subspace of $`\Lambda|_{\mathcal S}`$ for $`[\rho,\infty)`$ by Lemma 3(ii), and $`q=(\sigma_1-\tilde\lambda)f_1+(\Lambda-\tilde\lambda)g_1`$ is an orthogonal sum. Hence $`\|q\|^2\ge\|(\Lambda-\tilde\lambda)g_1\|^2\ge(\rho-\tilde\lambda)^2\|g_1\|^2`$. Also

```math
\int_E|\nabla G_1|^2=\langle\Lambda g_1,g_1\rangle\le\sup_{s\ge\rho}\frac{s}{(s-\tilde\lambda)^2}\,\|(\Lambda-\tilde\lambda)g_1\|^2=\frac{\rho}{(\rho-\tilde\lambda)^2}\|(\Lambda-\tilde\lambda)g_1\|^2,
```

because $`s/(s-\tilde\lambda)^2`$ decreases for $`s>\tilde\lambda>0`$. ∎

**The exact orthonormal equivariant pair.** Put $`f_2=(2/\sqrt3)(\mathcal Rf_1+f_1/2)\in W`$ and $`N_1=\|f_1\|`$. Since $`f_1+\mathcal Rf_1+\mathcal R^2f_1=0`$ and $`\mathcal R`$ is unitary, $`\langle\mathcal Rf_1,f_1\rangle=-\tfrac12\|f_1\|^2`$. Hence $`\|f_2\|^2=\tfrac43(\|f_1\|^2+\langle\mathcal Rf_1,f_1\rangle+\tfrac14\|f_1\|^2)=\|f_1\|^2`$. Moreover

```math
sf_2=\tfrac2{\sqrt3}\big(\mathcal R^{-1}sf_1+\tfrac12sf_1\big)=\tfrac2{\sqrt3}\big(-\mathcal R^2f_1-\tfrac12f_1\big)=\tfrac2{\sqrt3}\big(f_1+\mathcal Rf_1-\tfrac12f_1\big)=f_2,
```

so $`f_2`$ is even under $`s`$ and $`\langle f_1,f_2\rangle=0`$. Let $`w_a=Hf_a/N_1`$ $`(a=1,2)`$. This is an $`L^2(\partial E)`$-orthonormal basis of the first eigenspace, and $`\int_E\nabla w_a\cdot\nabla w_b=\langle\Lambda f_a,f_b\rangle/N_1^2=\sigma_1\delta_{ab}`$ exactly.

The approximate partner is $`\tilde w_2=\mathop{\mathrm{Re}}F_2`$ with $`F_2(z)=(2/\sqrt3)(F(\bar\omega z)+F(z)/2)`$. It satisfies $`\tilde w_2-N_1w_2=Hg_2`$ with $`g_2=(2/\sqrt3)(\mathcal Rg_1+g_1/2)`$. Since $`g_1`$ also satisfies $`g_1+\mathcal Rg_1+\mathcal R^2g_1=0`$, $`\|g_2\|=\|g_1\|`$ and $`\|\nabla Hg_2\|=\|\nabla G_1\|`$. Finally $`N_1^2=\|\tilde f_1\|^2-\|g_1\|^2\in[n_0-\delta_0^2,\ n_0]`$.

**Moments.** For the exact pair define, for $`a,b\in\{1,2\}`$ and $`k\in\{0,1,2\}`$,

```math
X_{ab}=\int_E(\partial_xw_a\partial_xw_b-\partial_yw_a\partial_yw_b),\qquad Y_{ab}=\int_E(\partial_xw_a\partial_yw_b+\partial_yw_a\partial_xw_b),
```

```math
(B_k)_{ab}=\int_{e_k}w_aw_b,\qquad (b_k)_a=\int_{e_k}w_a.
```

Exact identities: $`\sum_kB_k=I`$, $`\sum_kb_k=0`$ and $`\int_E\nabla w_a\cdot\nabla w_b=\sigma_1\delta_{ab}`$.

**Lemma 5.** The enclosures printed in `logs/certify.log` (step 2) contain $`X`$, $`Y`$, $`B_k`$ and $`b_k`$.

*Proof.* The same moments of $`(\tilde w_1,\tilde w_2)`$ are integrals of polynomials: the edge moments directly; for the gradient moments use $`F_a'F_b'=(u_xv_x-u_yv_y)-i(u_xv_y+u_yv_x)`$ for $`u=\mathop{\mathrm{Re}}F_a`$, $`v=\mathop{\mathrm{Re}}F_b`$, together with Green's formula $`\int_E\Phi\,dA=\frac1{2i}\oint_{\partial E}\bar z\,\Phi(z)\,dz`$ for analytic $`\Phi`$.

The bilinear forms $`(p,q)\mapsto\int_E(p_xq_x-p_yq_y)`$ and $`\int_E(p_xq_y+p_yq_x)`$ are bounded by $`\|\nabla p\|\|\nabla q\|`$ (pointwise Cauchy–Schwarz). Also $`|\int_{e_k}pq|\le\|p\|_{e_k}\|q\|_{e_k}`$ and $`|\int_{e_k}p|\le|e_k|^{1/2}\|p\|_{e_k}=3^{1/4}\|p\|_{e_k}`$. Writing $`N_1w_a=\tilde w_a-Hg_a`$,

```math
\big|X(N_1w_a,N_1w_b)-X(\tilde w_a,\tilde w_b)\big|\le\delta_1(\|\nabla\tilde w_a\|+\|\nabla\tilde w_b\|)+\delta_1^2,
```

```math
\Big|\int_{e_k}(N_1^2w_aw_b-\tilde w_a\tilde w_b)\Big|\le\delta_0(\|\tilde w_a\|_{e_k}+\|\tilde w_b\|_{e_k})+\delta_0^2,\qquad\Big|\int_{e_k}(N_1w_a-\tilde w_a)\Big|\le3^{1/4}\delta_0,
```

and the same bound as for $`X`$ holds for $`Y`$. Then divide by $`N_1^2`$ (respectively $`N_1`$) using the enclosure of $`N_1^2`$. All of this is done in Arb. ∎

The enclosures display the $`D_3`$ structure predicted by Schur's lemma, e.g. $`X\approx0.50767656753\,\mathrm{diag}(1,-1)`$; this structure is not used.

## 5. Local region: 0 < ‖S‖ ≤ 3/5

For $`S=r\hat S(\varphi)`$ and $`A=\exp(S)`$ let $`j_k=|A\tau_k|`$, so the edge $`Ae_k`$ has length $`\sqrt3\,j_k`$. Let $`\bar j=(j_0+j_1+j_2)/3`$, $`P=\mathop{\mathrm{Per}}(T_S)=3\sqrt3\,\bar j`$, $`G=A^{-1}A^{-T}=\exp(-2S)=\cosh2r\,I-\sinh2r\,\hat S`$ and $`t_k=\tau_k^T\hat S\tau_k`$, so that $`j_k^2=\cosh2r+t_k\sinh2r`$. For $`v=c_1w_1+c_2w_2-m`$ $`(m\in\mathbb R)`$ and $`u=v\circ A^{-1}`$ on $`T_S`$ (with $`\det A=1`$),

```math
\int_{T_S}|\nabla u|^2=c^T\mathcal A c,\qquad \mathcal A=\sigma_1\cosh2r\,I-\sinh2r\,(\cos\varphi\,X+\sin\varphi\,Y),
```

```math
\int_{\partial T_S}(u-\bar u)^2=c^T\mathcal Dc,\qquad \mathcal D=\mathcal B-\beta\beta^T/P,\qquad \mathcal B=\sum_kj_kB_k,\qquad \beta=\sum_kj_kb_k,
```

where $`m`$ is chosen to make the boundary mean of $`u`$ vanish.

**Lemma 6.** If $`M'=\bar j\mathcal A-\sigma_1\mathcal D`$ has a negative eigenvalue, then $`\sigma_1(T_S)\mathop{\mathrm{Per}}(T_S)<\sigma_1(E)\mathop{\mathrm{Per}}(E)`$.

*Proof.* Take $`c`$ with $`c^TM'c<0`$, i.e. $`c^T\mathcal Ac<(\sigma_1/\bar j)c^T\mathcal Dc=(3\sqrt3\sigma_1/P)c^T\mathcal Dc`$. Since $`\mathcal A\succeq0`$ and $`\mathcal D\succeq0`$ (an energy and a boundary $`L^2`$-norm), $`c^T\mathcal Dc>0`$ and $`u`$ is admissible in (F1). Hence $`\sigma_1(T_S)\le c^T\mathcal Ac/c^T\mathcal Dc<3\sqrt3\,\sigma_1(E)/\mathop{\mathrm{Per}}(T_S)`$. ∎

**Removable singularity.** Using $`\sum_kB_k=I`$, $`\sum_kb_k=0`$ and $`\sum_k(j_k-\bar j)=0`$, exactly

```math
\frac{M'}{r}=\sigma_1\bar j\,\frac{\cosh2r-1}{r}I-\bar j\,\frac{\sinh2r}{r}(\cos\varphi\,X+\sin\varphi\,Y)-\sigma_1\sum_k\frac{j_k-\bar j}{r}\Big(B_k-\frac I3\Big)+\sigma_1r\,\frac{\gamma\gamma^T}{P},\qquad \gamma=\sum_k\frac{j_k-\bar j}{r}b_k,
```

```math
\frac{j_k-j_m}{r}=\frac{\sinh2r}{r}\cdot\frac{t_k-t_m}{j_k+j_m}.
```

For $`r\in[0,r_b]`$ the increasing functions $`\sinh2r/r`$ and $`(\cosh2r-1)/r=2\sinh^2r/r`$ are enclosed by $`[2,\sinh2r_b/r_b]`$ and $`[0,2\sinh^2r_b/r_b]`$.

**Computation** (`certify/cert_local.py`). $`[0,3/5]\times[0,2\pi]`$ is covered by $`60\times120`$ boxes, adaptively bisected on failure. The $`r`$-intervals have rational endpoints, and the $`\varphi`$-intervals $`[2\pi k/120,2\pi(k+1)/120]`$ are enclosed outward. On each box, with $`\sigma_1\in[\sigma_{\mathrm{lo}},\sigma_{\mathrm{hi}}]`$ and the Lemma 5 enclosures, Arb certifies $`\det(M'/r)<0`$ or $`\mathop{\mathrm{tr}}(M'/r)<0`$. Either implies $`\lambda_{\min}(M')<0`$ for every $`r>0`$ in the box. Result: $`8412`$ boxes, all verified, maximum bisection depth $`2`$. Hence $`\sigma_1(T_S)\mathop{\mathrm{Per}}(T_S)<\sigma_1(E)\mathop{\mathrm{Per}}(E)`$ for $`0<\|S\|\le3/5`$.

Uncertified floating-point remark, not used: as $`r\to0`$, $`M'/r`$ tends to a traceless matrix with eigenvalues near $`\pm1.18`$. The upper bound $`\mathop{\mathrm{Per}}(T_S)\lambda_{\min}(\mathcal A,\mathcal D)`$ behaves like $`\sigma_1\mathop{\mathrm{Per}}(E)-6.11r`$, so the maximum at $`E`$ is conical; floating-point values of $`\sigma_1\mathop{\mathrm{Per}}(T_S)`$ show the same slope.

## 6. Far region: ‖S‖ ≥ 11/20

**Lemma 7.** For every $`S`$,

```math
\sigma_1(T_S)\mathop{\mathrm{Per}}(T_S)\le B(r):=12|E|\Big(\frac{e^{-2r}}{W_E^2}+\frac{d_E\,e^{-4r}}{W_E^3}\Big),
```

with $`W_E=3/2`$ (minimal width of $`E`$) and $`d_E=\sqrt3`$ (diameter of $`E`$). $`B`$ is decreasing.

*Proof.* Let $`d_\pm`$ be unit eigenvectors of $`S`$ with eigenvalues $`\pm r`$. The width of $`T_S`$ in direction $`d_+`$ is $`W=e^r\,\mathrm{width}_E(d_+)\ge e^rW_E`$; in direction $`d_-`$ it is $`W_\perp=e^{-r}\mathrm{width}_E(d_-)\le e^{-r}d_E`$. Take $`u(y)=d_+\cdot y-c`$ with $`c`$ the boundary mean. Then $`\int_{T_S}|\nabla u|^2=|T_S|=|E|`$. The boundary of the convex $`T_S`$ consists of two arcs from a lowest to a highest point of $`d_+\cdot y`$, on each of which $`d_+\cdot y`$ is monotone with slope at most $`1`$ in absolute value. So

```math
\int_{\partial T_S}u^2\,ds\ge2\int_{u_{\min}}^{u_{\max}}(t-c)^2\,dt\ge\frac{W^3}{6}.
```

$`T_S`$ lies in a $`W\times W_\perp`$ rectangle, so $`\mathop{\mathrm{Per}}(T_S)\le2(W+W_\perp)`$ (perimeter is monotone on convex sets). Hence $`\sigma_1\mathop{\mathrm{Per}}\le2(W+W_\perp)\cdot6|E|/W^3=12|E|(W^{-2}+W_\perp W^{-3})\le B(r)`$. ∎

**Computation** (`certify/cert_far.py`). $`B(11/20)\in[3.19262378424102\pm5\cdot10^{-15}]<3\sqrt3\,\sigma_{\mathrm{lo}}`$, and $`3\sqrt3\,\sigma_{\mathrm{lo}}\ge3.87246159577280656925872`$ (Arb). Hence $`\sigma_1(T_S)\mathop{\mathrm{Per}}(T_S)<\sigma_1(E)\mathop{\mathrm{Per}}(E)`$ for $`\|S\|\ge11/20`$.

## 7. Proof of the theorem

By Lemma 1 every triangle is similar to some $`T_S`$; $`S=0`$ is the equilateral case. If $`0<\|S\|\le3/5`$, Lemma 6 and the computation of §5 give strict inequality; if $`\|S\|\ge11/20`$, Lemma 7 and §6 give strict inequality. Since $`11/20<3/5`$, every $`S\ne0`$ is covered. So $`\sigma_1(T)\mathop{\mathrm{Per}}(T)<\sigma_1(E)\mathop{\mathrm{Per}}(E)`$ for every non-equilateral $`T`$, and equality holds for equilateral $`T`$ by scale invariance. ∎

**Corollary.** $`\sigma_1(T)\mathop{\mathrm{Per}}(T)\to0`$ as $`T`$ degenerates ($`\|S\|\to\infty`$), because $`B(r)\to0`$.

## 8. What the computer does

| Step | Script | Arithmetic | Output |
| --- | --- | --- | --- |
| 1 | `certify/cert_rho.py` | exact integers (FLINT charpoly); Arb for the constants | third eigenvalue at least 1.388851 |
| 2 | `certify/cert_E.py` | Arb at 320 bits; exact rational trial coefficients | first-eigenvalue enclosure, eigenvector errors, moments |
| 3 | `certify/cert_local.py` | Arb at 128 bits; outward-enclosed boxes | local region |
| 4 | `certify/cert_far.py` | Arb | far region |

No floating-point value enters any certified step. The trial coefficients (`certify/trial_coeffs.json`) and $`\mu`$ are exact rational inputs, so the certified log is identical across platforms. It was checked byte for byte, apart from the environment line, under Python 3.9.23 with python-flint 0.6.0 (x86_64) and Python 3.12.14 with python-flint 0.9.0 (arm64). In review, the local check still succeeded with every moment enclosure of Lemma 5 widened by $`\pm0.03`$; the actual radii are about $`10^{-11}`$. Trusted base: FLINT/Arb and the python-flint bindings, and the classical results (F1)–(F3).
