# A D-stable Lotka–Volterra system with a positive periodic solution

**Target:** [Problem 489 at `823ea0c6f9151792238d8ccbe7d64ea7d66faf5d`](https://github.com/April-Hannah-Lena/AIM/blob/823ea0c6f9151792238d8ccbe7d64ea7d66faf5d/problems/489-lotka-volterra-d-stable-global-attraction.md), formerly problem 490 before the Robin renumbering; [preserved statement](statement.md).

**Status:** Solved — counterexample supported by a [complete documented AI audit](REVIEW.md) and reproduced exact certificates. Current catalogue record: [archive 650](../../resolved/650-lotka-volterra-d-stable-global-attraction.md).

**Prepared:** 2026-10-02 by OpenAI Codex, adapting the mathematical argument and certificates supplied by the contributor. The supplied package does not identify its author. [Provenance and reproduction record](reproduction.json).

## The counterexample

Take $`x^*=(1,1,1,1)^T`$ and the following **exact rational matrix**:

```math
A=\frac1{1000}\begin{pmatrix}
-224&-2551&-1969&454\\
6814&-682&-1358&-11601\\
7845&-808&-1695&-16707\\
328&3248&5200&-685
\end{pmatrix}.
```

Consider

```math
\dot x_i=x_i\sum_{j=1}^4 A_{ij}(x_j-1).
```

**Theorem.** Every matrix $`DA`$, with $`D`$ positive diagonal, is Hurwitz. Nevertheless, this Lotka–Volterra system has a nonconstant periodic solution satisfying

```math
\frac18<x_i(t)<4\qquad(i=1,2,3,4;\ t\in\mathbb R),
```

with a period $`T`$ satisfying

```math
7.86959<T<7.86961.
```

Thus D-stability does not imply convergence of every strictly positive solution to the coexistence equilibrium. The particular counterexample solution exists for all positive and negative times; failure of convergence, not failure of forward existence, disproves the requested universal assertion.

The proof below is computer-assisted. Its finite certificates are included, and all acceptance tests use integers or exact rational arithmetic. No numerical ODE integration, eigenvalue computation, optimization, or floating-point tolerance is used by the verifier. Numerical approximations printed by the verifier are diagnostics only.

## 1. Exact proof of D-stability

Let $`D=\mathop{\mathrm{diag}}\nolimits(d_1,d_2,d_3,d_4)`$ with $`d_i>0`$. Write

```math
\det(\lambda I-DA)=\lambda^4+c_1\lambda^3+c_2\lambda^2+c_3\lambda+c_4.
```

Expanding the principal minors of $`-A`$ gives the following expressions. Every displayed terminating decimal is exact:

```math
c_1=0.224d_1+0.682d_2+1.695d_3+0.685d_4,
```

```math
\begin{aligned}
c_2={}&17.535282d_1d_2+15.826485d_1d_3+0.004528d_1d_4\\
&+0.058726d_2d_3+38.147218d_2d_4+88.037475d_3d_4,
\end{aligned}
```

```math
\begin{aligned}
c_3={}&1.993385926d_1d_2d_3+0.595689522d_1d_2d_4\\
&+0.738658761d_1d_3d_4+0.723883582d_2d_3d_4,
\end{aligned}
```

```math
c_4=158.631786924646d_1d_2d_3d_4.
```

In particular, all $`c_j`$ are positive. Define the homogeneous polynomial

```math
P(d)=c_1c_2c_3-c_3^2-c_1^2c_4.
```

The quartic Hurwitz criterion will follow from $`P(d)>0`$. Here is a finite rational certificate valid for **every** positive $`d`$, rather than a sample of diagonal matrices.

For a nonnegative integer vector $`u=(u_1,u_2,u_3,u_4)`$, write $`d^u=\prod_i d_i^{u_i}`$. A four-digit string in the table denotes this exponent vector; for example, $`0123`$ means $`(0,1,2,3)`$. Each row denotes

```math
G(d)=a d^u+b d^v-c d^w.
```

| $`u`$ | $`v`$ | $`w`$ | $`a`$ | $`b`$ | $`c`$ |
|---|---|---|---:|---:|---:|
| 0123 | 2103 | 1113 | 40.1 | 0.0017 | 0.521 |
| 0213 | 2013 | 1113 | 4.19 | 0.0000686 | 0.0338 |
| 1023 | 1203 | 1113 | 12.2 | 8.98 | 20.2 |
| 0213 | 2031 | 1122 | 13.2 | 0.000627 | 0.181 |
| 0222 | 2022 | 1122 | 38.8 | 16 | 49.6 |
| 0132 | 2130 | 1131 | 99.2 | 49.1 | 139 |
| 0231 | 2031 | 1131 | 0.0662 | 18.2 | 2.19 |
| 1032 | 1230 | 1131 | 102 | 0.183 | 8.58 |
| 0222 | 2220 | 1221 | 43.6 | 56.4 | 99.1 |
| 0312 | 2310 | 1311 | 17.3 | 21.9 | 14.2 |
| 0321 | 2301 | 1311 | 0.0267 | 6.54 | 0.0186 |
| 1302 | 1320 | 1311 | 14.3 | 0.0733 | 0.0289 |
| 1023 | 3201 | 2112 | 28.8 | 1.02 | 10.7 |
| 1203 | 3021 | 2112 | 5.31 | 0.509 | 3.23 |
| 1212 | 3012 | 2112 | 10.5 | 0.0000419 | 0.0418 |
| 2013 | 2211 | 2112 | 0.00204 | 23.9 | 0.398 |
| 2022 | 2202 | 2112 | 0.213 | 11 | 3.02 |
| 2022 | 2220 | 2121 | 4.06 | 14.2 | 15.1 |
| 3012 | 3210 | 3111 | 0.000646 | 7.19 | 0.135 |
| 3021 | 3201 | 3111 | 1.9 | 1.14 | 2.93 |
| 3102 | 3120 | 3111 | 0.000555 | 6.49 | 0.119 |

Every row satisfies $`u+v=2w`$, $`a,b,c>0`$, and $`c^2\leq4ab`$. Consequently

```math
a d^u+b d^v\geq2\sqrt{ab}\,d^w\geq c d^w,
```

so every $`G`$ is nonnegative. Let $`G_1,\ldots,G_{21}`$ be these polynomials and expand

```math
P(d)=\sum_\alpha p_\alpha d^\alpha.
```

There are 38 nonzero coefficients. Direct rational arithmetic gives, coefficient by coefficient,

```math
[d^\alpha]\left(P-\sum_{\ell=1}^{21}G_\ell\right)
\geq \frac7{100}|p_\alpha|>0.
```

There are no additional exponents in the remainder. This is checked by `dstability.py`, which recomputes all principal minors from the integer matrix by the determinant permutation formula, expands $`P`$, checks each of the 21 inequalities, and checks all 38 coefficient inequalities. Thus

```math
P(d)\geq\frac7{100}\sum_\alpha|p_\alpha|d^\alpha>0
\qquad(d_1,d_2,d_3,d_4>0).
```

Because

```math
P=c_3(c_1c_2-c_3)-c_1^2c_4>0,
```

we also have $`c_1c_2-c_3>0`$. The first column of the quartic Routh table is

```math
1,\quad c_1,\quad\frac{c_1c_2-c_3}{c_1},\quad
\frac{P}{c_1c_2-c_3},\quad c_4,
```

which is strictly positive. Hence $`DA`$ is Hurwitz for every positive diagonal $`D`$.

For completeness, the sufficient quartic criterion can also be seen directly from imaginary-axis crossings. A cubic $`z^3+c_1z^2+c_2z+c_3`$ with positive coefficients and $`c_3<c_1c_2`$ is Hurwitz: start with $`c_3>0`$ small and increase it, noting that an imaginary-axis crossing can occur only at $`c_3=c_1c_2`$. For the quartic, start with its constant coefficient small and positive, and then increase it to $`c_4`$. Its three nonzero roots initially approach this stable cubic, while its root near zero moves into the negative half-plane. A nonzero imaginary root would require

```math
\omega^2=c_3/c_1,\qquad
c_4=\frac{c_3(c_1c_2-c_3)}{c_1^2},
```

which is excluded by $`P>0`$. A zero root is excluded by $`c_4>0`$. Therefore all roots remain in the open left half-plane.

## 2. A Fourier formulation of the periodic-orbit equation

Put $`y=x-\mathbf1`$. Seek a real $`2\pi`$-periodic function $`y(s)`$ and a positive frequency $`\omega`$ such that

```math
\omega\frac{d y_i}{ds}=(1+y_i)(Ay)_i.
```

Then $`x_i(t)=1+y_i(\omega t)`$ solves the original ODE and has period $`2\pi/\omega`$.

Write

```math
y_i(s)=\sum_{k\in\mathbb Z}c_{i,k}e^{iks},\qquad
c_{i,-k}=\overline{c_{i,k}}.
```

For each species use the norm

```math
\|c_i\|_W=|c_{i,0}|+
2\sum_{k\geq1}\bigl(|\mathop{\mathrm{Re}}\nolimits c_{i,k}|+|\mathop{\mathrm{Im}}\nolimits c_{i,k}|\bigr).
```

The zero coefficient is real. This norm controls the uniform norm of the corresponding function. It is also submultiplicative for convolution, because $`|\mathop{\mathrm{Re}}\nolimits z|+|\mathop{\mathrm{Im}}\nolimits z|`$ is submultiplicative on complex numbers. Thus these coefficient sequences form a real Banach algebra.

For $`z=(\omega,c_1,c_2,c_3,c_4)`$ use

```math
\|z\|=\max\{\,|\omega|,\|c_1\|_W,\ldots,\|c_4\|_W\,\}.
```

The Fourier equations, together with a phase condition, are

```math
F_{i,k}(z)=ik\omega c_{i,k}-(Ac_k)_i
-\sum_{j=1}^4 A_{ij}(c_i*c_j)_k=0,
\qquad F_{\rm phase}(z)=\mathop{\mathrm{Im}}\nolimits c_{1,1}=0.
```

The phase condition removes the freedom to translate the solution in time.

### Exact reference point and finite inverse

The exact reference point $`\bar z=(\bar\omega,\bar c)`$ has Fourier degree $`M=48`$, with

```math
\bar\omega=\frac{56183263666306}{2^{46}},\qquad
\bar c_{i,k}=0\quad (|k|>48).
```

The real and imaginary parts of all remaining coefficients are integers divided by $`2^{46}`$. They are provided both in `anchor_coefficients.csv` and in `fourier_certificate.npz`. In particular,

```math
\bar c_{i,0}=0,\qquad
\bar c_{1,1}=\frac{43193933282984}{2^{46}}>\frac35.
```

Retain modes $`|k|\leq N=128`$ in the finite part of the equations. Together with the frequency and phase condition, this gives $`1+4(2N+1)=1029`$ real coordinates. The order is frequency first, followed for each species by

```math
c_{i,0},\ \mathop{\mathrm{Re}}\nolimits c_{i,1},\ \mathop{\mathrm{Im}}\nolimits c_{i,1},\ldots,
\mathop{\mathrm{Re}}\nolimits c_{i,N},\ \mathop{\mathrm{Im}}\nolimits c_{i,N}.
```

The certificate provides a real $`1029\times1029`$ matrix $`R`$, whose entries are integers divided by $`2^{40}`$. It is a computed approximate inverse of the finite Jacobian, but **no approximation property is assumed**: the required inequalities are verified exactly below.

Define a coefficientwise preconditioner $`L`$ by applying $`R`$ to the finite equations (phase equation included) and multiplying the remaining Fourier equations by $`(ik\bar\omega)^{-1}`$. Define

```math
\mathcal T(z)=z-LF(z).
```

Although differentiation alone is unbounded on $`W`$, this map is bounded and continuously differentiable on the stated Banach space. Indeed, its tail is explicitly

```math
(\mathcal T(z))_{i,k}
=\left(1-\frac{\omega}{\bar\omega}\right)c_{i,k}
+\frac{(Ac_k)_i+\sum_j A_{ij}(c_i*c_j)_k}{ik\bar\omega},
\qquad |k|>N.
```

The finite part involves only finitely many derivative coordinates. This explicit formula is also the definition of $`\mathcal T`$ on sequences without a priori differentiability.

## 3. Exact contraction bounds

The verifier establishes, with $`r=10^{-7}`$,

```math
Y:=\|\mathcal T(\bar z)-\bar z\|<10^{-10},
```

```math
\|D\mathcal T(\bar z)\|\leq Z_1<\frac45,
```

and

```math
\|D\mathcal T(z)-D\mathcal T(\bar z)\|
\leq Z_2\|z-\bar z\|,\qquad Z_2<60000.
```

Here are the precise finite formulas and tail estimates used to obtain these bounds; they explain why verification covers the infinite Fourier system.

### Weighted finite matrix norms

Each finite species coordinate has weight 1 for its zero mode and weight 2 for every real or imaginary nonzero mode; frequency has weight 1. Given a real matrix $`H`$ with the five output blocks and five input blocks (frequency and four species), define

```math
\mathcal B(H)_{ab}
=\max_{j\in\text{input block }b}
\frac{\sum_{i\in\text{output block }a}w_i|H_{ij}|}{w_j}.
```

Then the norm of output block $`a`$ is at most
$`\sum_b\mathcal B(H)_{ab}`$ times the input max-block norm.

### Derivative at the reference point

Let

```math
K_{ij,k}=A_{ij}\delta_{k0}+A_{ij}\bar c_{i,k}
+\delta_{ij}(A\bar c_k)_i.
```

The coefficient derivative of $`F`$ is $`ik\bar\omega I-K*`$, and its frequency derivative is $`ik\bar c_k`$. The kernel $`K`$ has support $`|k|\leq M`$.

Let $`J`$ be the finite-to-finite derivative, including the frequency and phase coordinates. Let $`J_{ft}`$ be the derivative into the finite equations from the input modes $`N+1,\ldots,N+M`$ of each species. Higher input modes do not affect the finite equations. Set

```math
E=[\,I-RJ,\ -RJ_{ft}\,].
```

Input finite and tail coordinates of a species belong to the same norm block. The code computes $`\mathcal B(E)`$ exactly. Independently, it checks

```math
\|I-RJ\|<10^{-7}<1,
```

so $`R`$ is invertible by the finite-dimensional Neumann argument.

Define

```math
\tau_i=\frac{\sum_{j=1}^4\|K_{ij}\|_W}{(N+1)\bar\omega}.
```

The tail derivative at the reference point is $`(ik\bar\omega)^{-1}(K*h)_{i,k}`$. Therefore

```math
Z_1=\max\left\{
\sum_b\mathcal B(E)_{0b},\
\max_{1\leq i\leq4}\left[\sum_b\mathcal B(E)_{ib}+\tau_i\right]
\right\}
```

is a valid full-space bound. The exact result is less than $`4/5`$; its diagnostic decimal is approximately $`0.7910926956545301`$.

### Variation of the derivative

Let $`a_i=\sum_j|A_{ij}|`$, and let $`D_N`$ denote coefficient differentiation on the finite species modes: $`(D_Nh)_{i,k}=ik h_{i,k}`$, with zero frequency column. Put

```math
U=\mathcal B(R),\qquad V=\mathcal B(RD_N).
```

For output block $`a=0,1,2,3,4`$, define

```math
q_a=\sum_{j=1}^4 V_{aj}+\sum_{j=1}^4U_{aj}a_j,
```

and add $`\bar\omega^{-1}(1+a_a/(N+1))`$ when $`a\neq0`$. Twice the largest of these five quantities is the certified $`Z_2`$.

To verify this formula, write $`z-\bar z=(\delta\omega,\delta c)`$ and differentiate in a direction $`(h_\omega,h)`$. The derivative change consists of

```math
ik(\delta\omega h+h_\omega\delta c)
-\bigl[\delta c_i*(Ah)_i+h_i*(A\delta c)_i\bigr].
```

For each species the quadratic contribution has $`W`$-norm at most
$`2a_i\|z-\bar z\|\|h\|`$. The two frequency contributions are bounded in the finite part by the block norms of $`RD_N`$. In the tail, cancellation of the factor $`ik`$ bounds these by
$`2\bar\omega^{-1}\|z-\bar z\|\|h\|`$, while the quadratic terms acquire the additional factor $`1/(N+1)`$. These are exactly the displayed bounds. The exact result is less than $`60000`$; its diagnostic decimal is approximately $`56239.673468296154`$.

### Residual and exact arithmetic

Since $`\bar c`$ has degree 48, $`F(\bar z)`$ has no nonzero modes above degree 96. Thus it lies entirely in the finite part ($`N=128`$), and $`Y`$ is computed exactly from $`RF(\bar z)`$. Its diagnostic decimal is approximately $`3.6773449289201\times10^{-12}`$.

Writing $`Q=2^{46}`$, every entry of $`J`$ and $`J_{ft}`$ is an integer divided by $`1000Q`$, every residual coordinate is an integer divided by $`1000Q^2`$, and every entry of $`R`$ is an integer divided by $`2^{40}`$. Hence all finite quantities above are rational.

For speed, the verifier multiplies integer matrices by splitting signed integers into base-$`2^{26}`$ digits. The inner dimension is 1029, and

```math
1029(2^{26}-1)^2<2^{63}.
```

Thus every digit product and every partial sum fits exactly into signed 64-bit arithmetic. Digit products are recombined using arbitrary-precision Python integers. There is no floating-point matrix product in the delivered verifier. A slower independent Python-integer matrix product is also available.

### Banach's fixed-point theorem

On the closed ball $`\|z-\bar z\|\leq r=10^{-7}`$,

```math
\|D\mathcal T(z)\|<\frac45+60000\cdot10^{-7}=0.806<1.
```

Moreover,

```math
\|\mathcal T(z)-\bar z\|
\leq Y+0.806r
<10^{-10}+0.806\cdot10^{-7}
=0.807r<r.
```

The ball is complete, so $`\mathcal T`$ has a fixed point in it. Its finite equations vanish because $`R`$ is invertible; each tail equation vanishes because $`ik\bar\omega\neq0`$ there. Consequently all the Fourier equations and the phase condition hold.

At the fixed point, $`\omega>0`$. Their right-hand sides are in $`W`$, so the equations imply $`\sum_k|k|(|\mathop{\mathrm{Re}}\nolimits c_{i,k}|+|\mathop{\mathrm{Im}}\nolimits c_{i,k}|)<\infty`$. The Fourier series therefore defines a continuously differentiable periodic function satisfying the ODE, not merely a formal coefficient solution.

## 4. Positivity and nonconstancy

For the reference polynomial, define the exact derivative bound

```math
L_i=2\sum_{k=1}^{48}k\bigl(|\mathop{\mathrm{Re}}\nolimits\bar c_{i,k}|+|\mathop{\mathrm{Im}}\nolimits\bar c_{i,k}|\bigr).
```

Then $`|\bar y_i'(s)|\leq L_i`$. Evaluate $`1+\bar y_i(s)`$ at 4096 equally spaced points using integer interval arithmetic. Every point of the circle is within $`\pi/4096`$ of a grid point. The interval lower bound at a nearest grid point, minus $`L_i\pi/4096`$ and minus $`r`$, is therefore a valid lower bound for the actual periodic solution. The analogous addition gives upper bounds.

`positivity.py` performs these calculations without calling a trigonometric library. It brackets $`\pi`$ by the alternating rational series in Machin's identity,

```math
\pi=16\arctan(1/5)-4\arctan(1/239),
```

and uses Taylor polynomials for sine and cosine through degrees 35 and 34 respectively, with remainders bounded by $`4^{37}/37!`$ and $`4^{36}/36!`$. Fixed-point interval endpoints have denominator $`2^{80}`$, with outward rounding at every operation. Complex powers of the resulting sine/cosine intervals evaluate the reference Fourier polynomial.

The verified lower bounds, rounded down for display, are

```math
x_1>0.1283906,\quad x_2>0.1290749,\quad
x_3>0.1723087,\quad x_4>0.5566275.
```

In particular, every coordinate exceeds $`1/8`$. The verified upper bounds are all less than 4.

The norm ball controls any nonzero real Fourier coefficient to accuracy $`r/2`$. Thus

```math
\mathop{\mathrm{Re}}\nolimits c_{1,1}\geq\bar c_{1,1}-r/2>3/5,
```

which proves nonconstancy. Finally,

```math
\frac{2\pi}{\bar\omega+r}\leq T\leq
\frac{2\pi}{\bar\omega-r}
```

and the rational bounds for $`\pi`$ imply $`7.86959<T<7.86961`$.

At the chosen phase, the exact initial point is within $`10^{-7}`$ in each coordinate of

```math
\bar x(0)=\frac1{2^{46}}
\begin{pmatrix}
214389344493608\\53540179863294\\84576464474922\\141502453224204
\end{pmatrix}.
```

This rational vector is a **reference point**, not a claim that its rounded coordinates lie exactly on the periodic orbit. The exact counterexample initial condition is obtained from the fixed point of $`\mathcal T`$. Equivalently it is specified constructively by starting at the supplied rational reference point in Fourier space and repeatedly applying $`\mathcal T`$. Every iterate has finite Fourier support and rational coordinates; the contraction estimate proves convergence to the stated periodic solution.

## 5. Conclusion and extensions

The matrix $`A`$ is D-stable, and $`x^*=\mathbf1`$ is a strictly positive equilibrium. The certified nonconstant positive periodic solution exists for all time and cannot converge to $`x^*`$. This is a negative answer to the universal global-attraction assertion.

For every $`n>4`$, append the block $`-I_{n-4}`$ to $`A`$ and keep the additional population coordinates equal to 1. Positive diagonal scaling preserves the block structure and Hurwitz stability, while the first four coordinates retain the periodic orbit. Thus the construction supplies counterexamples in every dimension at least four.

It also gives a restricted exponential example with an everywhere Hurwitz Jacobian: in logarithmic coordinates $`z_i=\log x_i`$, the vector field is $`\dot z=A(e^z-\mathbf1)`$. Its Jacobian $`A\mathop{\mathrm{diag}}\nolimits(e^z)`$ is similar to $`\mathop{\mathrm{diag}}\nolimits(e^z)A`$, so it is Hurwitz at every point, but the positive periodic orbit gives a periodic orbit in logarithmic coordinates as well.

## 6. Reproducing the checks

Install NumPy in an appropriate Python environment and, in this directory, run

```sh
python verify.py
```

The script verifies the D-stability certificate, the full Fourier contraction certificate, and positivity/nonconstancy/period bounds. All three were run successfully on the supplied files. The output is recorded in `verification.log`; exact rational bounds are recorded in `fourier_bounds.json` and `positivity_bounds.json`.

`python verify.py --slow-matmul` uses the slower direct Python-integer multiplication for the large finite matrix product. The default method is already exact integer arithmetic with the explicit no-overflow bound above.

`fourier_certificate.npz` contains only integer arrays and integer metadata: the matrix numerator, $`M`$, $`N`$, denominator exponents, Fourier coefficient numerators, and inverse-matrix numerators. It is read with `allow_pickle=False`. `anchor_coefficients.csv` duplicates the Fourier coefficients in text form. `dstability_certificate.json` duplicates the complete rational table in Section 1. The verifier recomputes all claimed bounds instead of trusting the stored output files.

The supplied package included earlier verification logs and additional convolution and integer-product cross-checks. These checks were reproduced during this submission, including the complete direct Python-integer matrix product. The [current AI audit](REVIEW.md) records the separate review of the analytical argument, verifier implementation and new exact cross-checks. No human referee review or proof-assistant formalization is claimed.

## Literature context

The attached problem formulates the Hofbauer–Sigmund D-stability/global-attraction conjecture. Hong and Pego, [Exclusion and multiplicity for stable communities in Lotka–Volterra systems](https://doi.org/10.1007/s00285-021-01638-7), Journal of Mathematical Biology **83** (2021), Article 16, [arXiv:2102.00611](https://arxiv.org/abs/2102.00611), Section 2.4, state this conjecture and distinguish it from the diagonal-Lyapunov sufficient condition. That paper supplies context, not the counterexample or the certificates above.
