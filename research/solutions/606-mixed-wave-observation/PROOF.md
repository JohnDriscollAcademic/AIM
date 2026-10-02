# Sharp observation time for mixed finite element waves

**Problem:** AIM 606, at repository commit [`37a25361f243be77daea0ae0b3c5167b57f1b5f3`](https://github.com/MColbrook/AIM/tree/37a25361f243be77daea0ae0b3c5167b57f1b5f3).

**Status:** Solution claimed; awaiting independent review.

**Date:** 2026-10-02.

**Author:** Marcus Webb, with assistance from OpenAI Codex.

**AI assistance:** Collaborating Codex agents developed the argument, drafted the proof, and performed the recorded AI reviews. Independent human mathematical review remains outstanding.

This note claims that the threshold in Problem 606 equals $`2`$ for every admissible potential. It proves uniform observation for every $`T>2`$ and failure for every $`0<T<2`$. It makes no assertion about observation at the endpoint $`T=2`$.

The published uniform separation and modal estimates of Castro and Micu [1] are inputs. The additional argument is a uniform asymptotic gap obtained from an exact matrix identity, followed by a Fourier estimate with finitely many exceptional frequencies. A concentrating spectral block proves sharpness without any assumption that the sampled potentials converge. The Fourier estimates are proved below; [2] records their classical origin.

## 1. Statement

Let $`a:[0,1]\to[0,\infty)`$ be bounded and measurable, with its pointwise representative fixed. Set

```math
A=\sup_{x\in[0,1]}a(x)<\infty.
```

The pointwise supremum is used because the matrices sample specified point values. For each integer $`N\ge1`$, set $`h=(N+1)^{-1}`$ and define the $`N\times N`$ matrices

```math
M_h=\frac h4\mathop{\mathrm{tridiag}}(1,2,1),\qquad
K_h=\frac1h\mathop{\mathrm{tridiag}}(-1,2,-1),\qquad
L_h=h\mathop{\mathrm{diag}}\bigl(a(h),\ldots,a(Nh)\bigr).
```

For a solution $`U_h=(u_1,\ldots,u_N)^T`$ of

```math
M_h\ddot U_h+(K_h+L_h)U_h=0,
```

write

```math
\mathcal E_h=(U_h(0))^*(K_h+L_h)U_h(0)
             +(\dot U_h(0))^*M_h\dot U_h(0),
```

and

```math
\mathcal O_{h,T}(U_h)
 =\int_0^T\left(\left|\frac{u_1(t)}h\right|^2
                     +\left|\frac{\dot u_1(t)}2\right|^2\right)dt.
```

**Theorem.** For every $`T>2`$ there is $`c(a,T)>0`$ such that

```math
\mathcal O_{h,T}(U_h)\ge c(a,T)\mathcal E_h
```

for every $`N\ge1`$ and every solution. For every $`0<T<2`$ there are meshes $`h_m\to0`$ and nonzero solutions $`U_m`$ with

```math
\frac{\mathcal O_{h_m,T}(U_m)}{\mathcal E_{h_m}(U_m)}\longrightarrow0.
```

Consequently, the infimum of the times admitting a mesh-independent observation constant is $`T_*(a)=2`$.

## 2. Spectral notation and published inputs

Let $`0<\lambda_{h,1}<\cdots<\lambda_{h,N}`$ be the square roots of the generalized eigenvalues of $`(K_h+L_h,M_h)`$. Choose real eigenvectors $`\phi_{h,j}\in\mathbb R^N`$ satisfying

```math
(K_h+L_h)\phi_{h,j}=\lambda_{h,j}^2M_h\phi_{h,j},
\qquad
\phi_{h,j}^TM_h\phi_{h,k}=\delta_{jk}.
```

Let $`\phi_{h,j,1}`$ denote the first component and put

```math
q_{h,j}=\frac{\phi_{h,j,1}}{h\lambda_{h,j}},
\qquad
r_{h,j}=\frac{\phi_{h,j,1}}2.
```

We use the following results from [1], with numbering from the published article:

- Lemma 4 gives simplicity, positivity and the indicated orthonormal basis.
- Theorem 9 gives $`g>0`$ and $`h_0>0`$ such that the signed frequencies $`\{\pm\lambda_{h,j}:1\le j\le N\}`$ have mutual distance at least $`g`$ for $`h<h_0`$.
- Equation (48), established at the end of Section 4, gives $`c_{\mathrm{mod}}>0`$ such that $`q_{h,j}^2+r_{h,j}^2\ge c_{\mathrm{mod}}`$ for $`h<h_0`$. Its normalized coefficients have an extra factor $`1/\sqrt2`$, absorbed here into the constant.
- Lemma 5, equation (31), gives a constant $`C_0`$ with

```math
(\lambda_{h,j}^2+h^{-2})
\left|\frac{\phi_{h,j,1}}{\lambda_{h,j}}\right|^2
\le C_0\left(1+\frac{A^2}{\lambda_{h,j}^2}\right)
\qquad(h<h_0).
\tag{2.1}
```

These estimates concern the finite matrices and use only the bounds $`0\le a(jh)\le A`$. No continuity or convergence of the sampled potentials is needed. The separate continuity assumption in the convergence results of [1] is not used here.

The first component of every eigenvector is nonzero. Indeed, if it vanished, the first row of the eigenvalue equation would force the second component to vanish because its coefficient is $`-h^{-1}-\lambda_{h,j}^2h/4\ne0`$. Induction through the tridiagonal rows would force the entire vector to vanish. For $`N=1`$ the assertion follows directly.

## 3. Uniform asymptotic separation

The exact identity

```math
hI=M_h+\frac{h^2}{4}K_h
```

and $`0\le L_h\le AhI`$ imply the quadratic-form inequalities

```math
K_h\le K_h+L_h
\le\left(1+\frac{Ah^2}{4}\right)K_h+AM_h.
```

The zero-potential frequencies are

```math
\omega_{h,j}=\frac2h\tan\theta_{h,j},
\qquad
\theta_{h,j}=\frac{\pi jh}{2}.
```

The finite-dimensional min--max principle gives

```math
\omega_{h,j}\le\lambda_{h,j}
\le\sqrt{\left(1+\frac{Ah^2}{4}\right)\omega_{h,j}^2+A}.
\tag{3.1}
```

In particular $`\lambda_{h,j}\ge\omega_{h,j}\ge\pi j`$. Rationalizing the upper bound yields

```math
0\le\lambda_{h,j}-\omega_{h,j}
\le\frac{A}{2\omega_{h,j}}+\frac{Ah^2\omega_{h,j}}8.
\tag{3.2}
```

For $`1\le j<N`$, integration of the increasing function $`\sec^2\theta`$ gives

```math
\omega_{h,j+1}-\omega_{h,j}\ge\pi\sec^2\theta_{h,j}.
```

Using the lower bound in (3.1) at $`j+1`$ and (3.2) at $`j`$ therefore gives

```math
\begin{aligned}
\lambda_{h,j+1}-\lambda_{h,j}
&\ge\pi\sec^2\theta_{h,j}
       -\frac{A}{2\omega_{h,j}}
       -\frac{Ah}{4}\tan\theta_{h,j}\\
&\ge\pi-\frac{A}{2\pi j}-\frac{A^2h^2}{64\pi}.
\end{aligned}
\tag{3.3}
```

The last line completes the square in $`\pi\tan^2\theta-(Ah/4)\tan\theta`$. Since $`j<N`$ implies $`h\le(j+2)^{-1}`$, we also have

```math
\lambda_{h,j+1}-\lambda_{h,j}
\ge\pi-\frac{A}{2\pi j}-\frac{A^2}{64\pi(j+2)^2}.
\tag{3.4}
```

For any $`0<\gamma<\pi`$, choose $`J`$ so that the right side of (3.4) is at least $`\gamma`$ for $`j\ge J`$. Deleting the frequencies with $`|j|<J`$ from the signed set leaves a set with gap at least $`\gamma`$, uniformly in the mesh whenever $`N\ge J`$. The separation across the two remaining tails is at least $`2\lambda_{h,J}\ge2\pi J>\gamma`$.

## 4. Fourier bounds with finitely many exceptional frequencies

We give the quantitative uniformity needed for the family of finite spectral sets.

**Lemma 4.1 (separated frequencies).** A finite real frequency set with gap at least $`\gamma>0`$ admits a uniform lower Fourier bound on every interval of length $`S>2\pi/\gamma`$. A set with gap at least $`g>0`$ admits a uniform upper Fourier bound on every interval of length $`s>0`$. The constants depend only on the stated gaps and interval lengths.

**Proof.** For $`\alpha=\pi/S`$, let

```math
w(t)=\begin{cases}
\cos(\alpha t),&|t|\le S/2,\\
0,&|t|>S/2.
\end{cases}
```

Direct integration gives

```math
\widehat w(\xi)
=\int_{\mathbb R}w(t)e^{i\xi t}\,dt
=\frac{2\alpha\cos(\xi S/2)}{\alpha^2-\xi^2},
\qquad
\widehat w(0)=\frac2\alpha,
```

with the values at $`\xi=\pm\alpha`$ obtained by continuity. For an ordered $`\gamma`$-separated set, the distance to the $`n`$th next frequency on either side is at least $`n\gamma`$. When $`\alpha\le\gamma/2`$, the absolute off-diagonal row sum of the weighted Gram matrix is at most

```math
4\alpha\sum_{n=1}^{\infty}\frac1{n^2\gamma^2-\alpha^2}
\le\frac{4\alpha}{\gamma^2}
       \sum_{n=1}^{\infty}\frac1{n^2-1/4}
=\frac{8\alpha}{\gamma^2}.
```

The final series equals $`2`$ by telescoping. Applying $`2|z_jz_k|\le|z_j|^2+|z_k|^2`$ to the off-diagonal quadratic form and using $`0\le w\le1`$, we obtain

```math
\int_{-S/2}^{S/2}\left|\sum_jc_je^{i\nu_jt}\right|^2dt
\ge\left(\frac2\alpha-\frac{8\alpha}{\gamma^2}\right)
      \sum_j|c_j|^2.
\tag{4.1}
```

The coefficient is positive when $`S>2\pi/\gamma`$.

For the upper bound on an interval of length $`s`$, put $`L=\max\{2s,4\pi/g\}`$ and use the same kernel on an interval of length $`L`$, with $`\alpha=\pi/L`$. The weight is at least $`1/\sqrt2`$ on $`[-s/2,s/2]`$. The upper weighted Gram estimate gives

```math
\int_{-s/2}^{s/2}\left|\sum_jc_je^{i\nu_jt}\right|^2dt
\le\sqrt2\left(\frac2\alpha+\frac{8\alpha}{g^2}\right)
     \sum_j|c_j|^2.
\tag{4.2}
```

Translation of the interval changes only the coefficient phases. Both bounds are independent of the number and magnitude of the frequencies. $`\square`$

**Lemma 4.2 (finite insertion).** Let a finite real frequency set $`\Lambda`$ have mutual separation at least $`g>0`$. Suppose deletion of at most $`m`$ frequencies leaves a nonempty set with gap at least $`\gamma>0`$. For each $`T>2\pi/\gamma`$, there is $`c=c(g,\gamma,m,T)>0`$ such that

```math
\int_I\left|\sum_{\lambda\in\Lambda}b_\lambda e^{i\lambda t}\right|^2dt
\ge c\sum_{\lambda\in\Lambda}|b_\lambda|^2
\tag{4.3}
```

on every interval $`I`$ of length $`T`$.

**Proof.** Choose $`S`$ strictly between $`2\pi/\gamma`$ and $`T`$. Lemma 4.1 gives a lower bound on length $`S`$ for the remaining set. If $`m=0`$, this proves the assertion. Otherwise set $`\varepsilon=(T-S)/(2m)`$. We show that each insertion preserves a uniform positive lower constant when the interval length increases by $`2\varepsilon`$.

Suppose the existing set has lower constant $`c_s>0`$ on $`I_s=[-s/2,s/2]`$. Insert $`\lambda_0`$ and write

```math
F(t)=b_0e^{i\lambda_0t}
       +\sum_{\lambda\ne\lambda_0}b_\lambda e^{i\lambda t}.
```

For $`|\sigma|\le\varepsilon`$, the sum

```math
G_\sigma(t)=e^{-i\lambda_0\sigma}F(t+\sigma)-F(t)
```

has no $`\lambda_0`$ coefficient. Apply the existing lower bound on $`I_s`$ and integrate in $`\sigma`$. Since $`I_s+\sigma\subset I_{s+2\varepsilon}`$,

```math
\begin{aligned}
c_s\sum_{\lambda\ne\lambda_0}|b_\lambda|^2
\int_{-\varepsilon}^{\varepsilon}
 \left|e^{i(\lambda-\lambda_0)\sigma}-1\right|^2d\sigma
\le8\varepsilon\|F\|_{L^2(I_{s+2\varepsilon})}^2.
\end{aligned}
\tag{4.4}
```

Global separation implies that each integral on the left is at least

```math
d(g,\varepsilon)
=4\varepsilon\inf_{|x|\ge g\varepsilon}
       \left(1-\frac{\sin x}{x}\right)>0.
```

Positivity follows from continuity, $`\sin x/x<1`$ for $`x\ne0`$, and $`\sin x/x\to0`$ at infinity. Thus (4.4) bounds the old coefficient sum by $`8\varepsilon/(c_sd)`$ times $`\|F\|^2`$. The upper bound (4.2) controls the old sum's $`L^2(I_{s+2\varepsilon})`$ norm by the same coefficient sum. Finally,

```math
(s+2\varepsilon)|b_0|^2
\le2\|F\|_{L^2(I_{s+2\varepsilon})}^2
   +2\left\|\sum_{\lambda\ne\lambda_0}
                b_\lambda e^{i\lambda t}\right\|_{L^2(I_{s+2\varepsilon})}^2
```

controls the inserted coefficient. Every resulting constant depends only on $`c_s,g,s,\varepsilon`$. After at most $`m`$ insertions, enlarge the interval to length $`T`$ if necessary. This proves (4.3). $`\square`$

## 5. Observation for every time greater than two

Fix $`T>2`$ and choose $`0<\gamma<\pi`$ with $`2\pi/\gamma<T`$. Section 3 supplies $`J`$ independently of the mesh. On sufficiently fine meshes, the global gap $`g`$ from [1] holds, $`N\ge J`$, and deleting at most $`2(J-1)`$ central frequencies leaves gap $`\gamma`$. Lemma 4.2 supplies a scalar Fourier lower constant $`c_F>0`$ for the entire signed frequency set on $`[0,T]`$, independent of $`h`$.

Suppressing $`h`$ in the spectral notation, every solution has a unique expansion

```math
U_h(t)=\sum_{j=1}^N\sum_{\sigma\in\{-1,1\}}
 b_{\sigma,j}e^{i\sigma\lambda_jt}
 \frac{\phi_j}{\sqrt2\lambda_j}.
\tag{5.1}
```

Orthogonality shows directly that

```math
\mathcal E_h=\sum_{j=1}^N\sum_{\sigma\in\{-1,1\}}|b_{\sigma,j}|^2.
```

The two observation components are

```math
\frac{u_1(t)}h
 =\frac1{\sqrt2}\sum_{\sigma,j}q_jb_{\sigma,j}e^{i\sigma\lambda_jt},
\qquad
\frac{\dot u_1(t)}2
 =\frac{i}{\sqrt2}\sum_{\sigma,j}\sigma r_jb_{\sigma,j}e^{i\sigma\lambda_jt}.
```

Apply the scalar Fourier lower bound to each sum and add. The modal lower bound from Section 2 gives

```math
\mathcal O_{h,T}(U_h)
\ge\frac{c_F}{2}\sum_{\sigma,j}(q_j^2+r_j^2)|b_{\sigma,j}|^2
\ge\frac{c_Fc_{\mathrm{mod}}}{2}\mathcal E_h.
\tag{5.2}
```

There are only finitely many coarser meshes. For each of them the signed frequencies are distinct and $`\phi_{h,j,1}\ne0`$. If the first observation vanished on a nonempty time interval, linear independence of the finite exponential family in (5.1) would force every coefficient to vanish. Its finite-dimensional observation Gramian is therefore positive definite. Taking the minimum over these finitely many constants and the constant in (5.2) proves the theorem's upper assertion for all $`N\ge1`$.

## 6. Failure for every time less than two

Fix $`0<T<2`$ and set $`t_0=(T+2)/2`$. For each integer $`m\ge1`$, normalize the coefficient vector of

```math
R_m(t)=\left(\frac{1+e^{i\pi(t-t_0)}}2\right)^m
```

to obtain

```math
P_m(t)=\sum_{\ell=0}^mc_{m,\ell}e^{i\pi\ell t},
\qquad
\sum_{\ell=0}^m|c_{m,\ell}|^2=1.
```

The unnormalized coefficient vector has $`\ell^1`$ norm $`1`$, so its $`\ell^2`$ norm is at least $`(m+1)^{-1/2}`$. Consequently, with $`\rho=\cos(\pi(2-T)/4)<1`$,

```math
\sup_{0\le t\le T}|P_m(t)|\le\sqrt{m+1}\,\rho^m,
\qquad
\sum_{\ell=0}^m|c_{m,\ell}|\le\sqrt{m+1}.
\tag{6.1}
```

Choose

```math
J_m=(m+1)^2,\qquad N_m+1=(m+1)^6,\qquad h_m=(m+1)^{-6},
```

and the spectral block $`j=J_m,\ldots,J_m+m`$, which lies within $`1,\ldots,N_m`$. On that block $`\theta_{h_m,j}=O(m^{-4})`$. The estimate $`\tan\theta-\theta=O(\theta^3)`$, together with (3.1)–(3.2), gives

```math
\delta_m:=\max_{0\le\ell\le m}
 \left|\lambda_{h_m,J_m+\ell}-\pi(J_m+\ell)\right|
 =O_A(m^{-2}),
\qquad
\max_{0\le\ell\le m}\lambda_{h_m,J_m+\ell}=O_A(m^2).
\tag{6.2}
```

Indeed, the three upper-bound terms have orders

```math
\omega_{h_m,j}-\pi j=O(h_m^2j^3)=O(m^{-6}),\qquad
\frac{A}{2\omega_{h_m,j}}=O_A(m^{-2}),\qquad
\frac{Ah_m^2\omega_{h_m,j}}8=O_A(m^{-10}).
```

These bounds require only $`0\le a(jh_m)\le A`$.

Define the exact discrete solution

```math
U_m(t)=\sum_{\ell=0}^m
 \frac{h_mc_{m,\ell}}{\phi_{h_m,J_m+\ell,1}}
 \phi_{h_m,J_m+\ell}e^{i\lambda_{h_m,J_m+\ell}t}.
\tag{6.3}
```

Every denominator is nonzero. Its first observation is

```math
F_m(t):=\frac{u_1(t)}{h_m}
 =\sum_{\ell=0}^mc_{m,\ell}e^{i\lambda_{h_m,J_m+\ell}t}.
```

Since $`|e^{ix}-e^{iy}|\le|x-y|`$, (6.1)–(6.2) imply

```math
\begin{aligned}
\|F_m-e^{i\pi J_mt}P_m\|_{L^2(0,T)}
&\le T^{3/2}\delta_m\sum_{\ell=0}^m|c_{m,\ell}|\\
&=O_{A,T}(m^{-3/2}).
\end{aligned}
```

It follows that $`\|F_m\|_{L^2(0,T)}\to0`$. The second observation satisfies

```math
\begin{aligned}
\left\|\frac{\dot u_1}2\right\|_{L^2(0,T)}
&=\left\|\frac{ih_m}{2}\sum_{\ell=0}^m
 \lambda_{h_m,J_m+\ell}c_{m,\ell}
 e^{i\lambda_{h_m,J_m+\ell}t}\right\|_{L^2(0,T)}\\
&\le\frac{\sqrt T h_m}{2}
 \max_{0\le\ell\le m}\lambda_{h_m,J_m+\ell}
 \sum_{\ell=0}^m|c_{m,\ell}|\\
&=O_{A,T}(m^{-7/2})\longrightarrow0.
\end{aligned}
```

On the other hand, $`\lambda_{h,j}\ge\pi`$ and (2.1) give $`q_{h,j}^2\le Q_A^2`$ uniformly on sufficiently fine meshes, for some finite $`Q_A>0`$. The energy of (6.3) is

```math
\begin{aligned}
\mathcal E_{h_m}(U_m)
&=2\sum_{\ell=0}^m
 \frac{h_m^2\lambda_{h_m,J_m+\ell}^2|c_{m,\ell}|^2}
      {|\phi_{h_m,J_m+\ell,1}|^2}\\
&=2\sum_{\ell=0}^m\frac{|c_{m,\ell}|^2}{q_{h_m,J_m+\ell}^2}
\ge\frac2{Q_A^2}.
\end{aligned}
```

Thus $`\mathcal O_{h_m,T}(U_m)/\mathcal E_{h_m}(U_m)\to0`$, proving failure of uniform observation for $`T<2`$.

The argument uses complex solutions, as allowed by the Hermitian energy notation. It also proves the same failure for real solutions: the real and imaginary parts' energies and observations add, so at least one nonzero part has a ratio no larger than that of the complex solution.

Together with Section 5, this establishes the claimed threshold $`T_*(a)=2`$. $`\square`$

## References

1. C. Castro and S. Micu, [A mixed finite elements approximation of inverse source problems for the wave equation with variable coefficients using observability](https://doi.org/10.1007/s00211-025-01489-0), *Numerische Mathematik* **157** (2025), 1847–1895. Published Lemmas 4–5, Theorem 9, equation (48), and Section 4. [Preprint](https://arxiv.org/abs/2501.11352).
2. A. E. Ingham, [Some trigonometrical inequalities with applications to the theory of series](https://doi.org/10.1007/BF01180426), *Mathematische Zeitschrift* **41** (1936), 367–379. Historical reference for the separated-frequency Fourier estimates; the estimates used here are proved in Section 4.
