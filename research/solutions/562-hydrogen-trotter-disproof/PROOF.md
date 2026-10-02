# Disproof of the proposed fixed-time hydrogen Trotter lower bound

**Target:** Problem 562 at `61dec31d3c3ffe6e15aae8ad84ecf0968a18866d`; [unchanged original statement](statement.md). The current catalogue record is [archive 651](../../resolved/651-hydrogen-trotter-lower-bound.md).

**Status:** Solved — disproof supported by a [documented AI audit](REVIEW.md) of the complete supplied argument, under the repository's independent-audit convention.

**Prepared:** 2026-10-02 by OpenAI Codex, adapting the argument supplied by the contributor. The supplied material does not identify its author. Codex checked the argument and prepared this repository version; the review record describes the scope and provenance of that AI audit.

Here $`\psi`$ is exactly the normalized state $`\psi_0`$ in the target. The operator order, signs, final time and initial state are unchanged.

## Result

Let
```math
H=-\Delta-|x|^{-1},\qquad
\psi(x)=(8\pi)^{-1/2}e^{-|x|/2},\qquad
S_n=\bigl(e^{-i|x|^{-1}/n}e^{-i\Delta/n}\bigr)^n.
```
There is a constant $`C<\infty`$, independent of $`n`$, such that
```math
\boxed{\|S_n\psi-e^{iH}\psi\|_{L^2(\mathbb R^3)}\le Cn^{-3/8}.}
```
Consequently,
```math
n^{1/4}\|S_n\psi-e^{iH}\psi\|_2\longrightarrow0,
```
so the proposed eventual lower bound $`c n^{-1/4}`$, with $`c>0`$, is false. The exponent $`3/8`$ is not asserted to be sharp.

The proof uses an auxiliary approximate eigenvector of one splitting step. This does not modify either the initial state in the assertion or the splitting scheme.

Throughout, constants denoted by $`C`$ may change between inequalities but do not depend on $`0<h\le1`$, $`R\ge1`$, or $`0<\delta\le1`$.

## 1. Shift the free operator by the ground-state energy

Set
```math
h=\frac1n,\qquad V(x)=\frac1{|x|},\qquad
K=-\Delta+\frac14,\qquad \lambda_h=e^{-ih/4}.
```
The ground-state equation gives
```math
K\psi=V\psi.
```
Both sides belong to $`L^2(\mathbb R^3)`$. Write
```math
U_h=e^{ihK},\qquad W_h=e^{ihV},\qquad
T_h=\lambda_hW_h^{-1}U_h.
```
Then
```math
T_h=e^{-ihV}e^{-ih\Delta},\qquad S_n=T_h^n,
\qquad e^{iH}\psi=\lambda_h^n\psi.
```
All these evolution factors are unitary.

Define the two Taylor remainders
```math
d_h=(U_h-I-ihK)\psi,\qquad
q_h=(W_h-I-ihV)\psi.
```
Since $`K\psi=V\psi`$,
```math
U_h\psi-W_h\psi=d_h-q_h. \tag{1}
```

## 2. Bounds on the free remainder

Use the unitary Fourier transform
```math
\widehat f(\xi)=(2\pi)^{-3/2}\int_{\mathbb R^3}e^{-ix\cdot\xi}f(x)\,dx.
```
A direct radial integration gives
```math
\widehat\psi(\xi)=\frac1{2\pi\bigl(|\xi|^2+\tfrac14\bigr)^2}.
```
Put $`a(\xi)=|\xi|^2+\tfrac14`$. Thus
```math
\widehat d_h(\xi)=\frac{e^{iha(\xi)}-1-iha(\xi)}{2\pi a(\xi)^2}. \tag{2}
```
For every real $`z\ge0`$,
```math
|e^{iz}-1-iz|\le\frac{z^2}{2},\qquad
|e^{iz}-1-iz|\le2z.
```
Therefore
```math
|\widehat d_h(\xi)|\le C\min\left\{h^2,\frac h{a(\xi)}\right\}. \tag{3}
```
These inequalities imply
```math
\|d_h\|_2\le Ch^{5/4}, \tag{4}
```
```math
\|\mathbf1_{\{|\xi|>R\}}\widehat d_h\|_2\le ChR^{-1/2}, \tag{5}
```
and
```math
\||\xi|\mathbf1_{\{|\xi|\le R\}}\widehat d_h\|_2\le ChR^{1/2}. \tag{6}
```

For completeness, let $`\rho=|\xi|`$. Splitting the radial integral at $`\rho=h^{-1/2}`$ proves (4):
```math
\begin{aligned}
\|d_h\|_2^2
&\le C\left(h^4\int_0^{h^{-1/2}}\rho^2\,d\rho
+h^2\int_{h^{-1/2}}^\infty\rho^{-2}\,d\rho\right)\\
&\le Ch^{5/2}.
\end{aligned}
```
Using the second bound in (3) gives
```math
\|\mathbf1_{\{|\xi|>R\}}\widehat d_h\|_2^2
\le Ch^2\int_R^\infty\rho^{-2}\,d\rho
\le\frac{Ch^2}{R},
```
and
```math
\||\xi|\mathbf1_{\{|\xi|\le R\}}\widehat d_h\|_2^2
\le Ch^2\int_0^R\frac{\rho^4}{(\rho^2+\tfrac14)^2}\,d\rho
\le Ch^2R.
```

## 3. The remainder near resonant frequency shells

For $`0<\delta\le1`$, define
```math
\mathcal B_{h,\delta}
=\{\xi\in\mathbb R^3:|e^{iha(\xi)}-1|<\delta\}.
```
We claim that
```math
\boxed{\|\mathbf1_{\mathcal B_{h,\delta}}\widehat d_h\|_2
\le Ch^{5/4}\delta^{1/2}.} \tag{7}
```
This estimate includes every resonant shell, not just finitely many of them.

To prove it, substitute
```math
z=h(\rho^2+\tfrac14),\qquad
\rho^2\,d\rho=\frac{\sqrt{z-h/4}}{2h^{3/2}}\,dz
```
in the radial integral from (2). It gives the exact identity
```math
\begin{aligned}
\|\mathbf1_{\mathcal B_{h,\delta}}\widehat d_h\|_2^2
=\frac{h^{5/2}}{2\pi}
\int_{h/4}^\infty
\mathbf1_{\{|e^{iz}-1|<\delta\}}
\frac{|e^{iz}-1-iz|^2\sqrt{z-h/4}}{z^4}\,dz.
\end{aligned}
```
In particular,
```math
\|\mathbf1_{\mathcal B_{h,\delta}}\widehat d_h\|_2^2
\le Ch^{5/2}\int_0^\infty
\mathbf1_{\{|e^{iz}-1|<\delta\}}
\min\{z^{1/2},z^{-3/2}\}\,dz. \tag{8}
```

The condition $`|e^{iz}-1|<\delta`$ places $`z`$ within $`\pi\delta/2`$ of a nonnegative multiple of $`2\pi`$. Indeed, if $`d=\mathop{\mathrm{dist}}\nolimits(z,2\pi\mathbb Z)\in[0,\pi]`$, then
```math
|e^{iz}-1|=2\sin(d/2)\ge\frac{2d}{\pi}.
```
The interval adjacent to zero contributes at most
```math
\int_0^{\pi\delta/2}z^{1/2}\,dz\le C\delta^{3/2}.
```
For the interval around $`2\pi k`$, $`k\ge1`$, its length is at most $`\pi\delta`$ and $`z\ge (3\pi/2)k`$ throughout. Its contribution is therefore at most $`C\delta k^{-3/2}`$. Consequently,
```math
\int_0^\infty
\mathbf1_{\{|e^{iz}-1|<\delta\}}
\min\{z^{1/2},z^{-3/2}\}\,dz
\le C\left(\delta^{3/2}+\delta\sum_{k=1}^\infty k^{-3/2}\right)
\le C\delta.
```
Combining this with (8) proves (7).

## 4. Cancel the nonresonant remainder with a small correction

Fix $`R\ge1`$ and $`0<\delta\le1`$, to be chosen below. Let $`P`$ be the orthogonal Fourier projection onto
```math
G=\{\xi:|\xi|\le R\}\setminus\mathcal B_{h,\delta}.
```
Define $`\eta_h`$ through its Fourier transform by
```math
\widehat\eta_h(\xi)=
\begin{cases}
-\dfrac{\widehat d_h(\xi)}{e^{iha(\xi)}-1},&\xi\in G,\\[6pt]
0,&\xi\notin G.
\end{cases} \tag{9}
```
The denominator is at least $`\delta`$ in modulus wherever it is used. Therefore, by (4) and (6),
```math
\|\eta_h\|_2\le C\frac{h^{5/4}}\delta,\qquad
\|\nabla\eta_h\|_2\le C\frac{hR^{1/2}}\delta. \tag{10}
```
In particular, $`\eta_h\in H^1(\mathbb R^3)`$. Its defining property is the exact identity
```math
(U_h-I)\eta_h=-Pd_h. \tag{11}
```

Now put $`\phi_h=\psi+\eta_h`$. From (1) and (11),
```math
\begin{aligned}
(T_h-\lambda_h)\phi_h
&=\lambda_hW_h^{-1}(U_h-W_h)(\psi+\eta_h)\\
&=\lambda_hW_h^{-1}
\bigl((I-P)d_h-q_h-(W_h-I)\eta_h\bigr).
\end{aligned} \tag{12}
```
Thus the nonresonant part of the leading free remainder has been canceled exactly. By (5) and (7),
```math
\|(I-P)d_h\|_2\le C\bigl(hR^{-1/2}+h^{5/4}\delta^{1/2}\bigr). \tag{13}
```

## 5. Estimate the two Coulomb terms

First,
```math
\|q_h\|_2\le Ch^{3/2}. \tag{14}
```
To check this without assuming $`V^2\psi\in L^2`$, observe that for $`r=|x|`$,
```math
|e^{ih/r}-1-ih/r|
\le
\begin{cases}
3h/r,&0<r\le h,\\
h^2/(2r^2),&r>h.
\end{cases}
```
Since $`\psi`$ is bounded, spherical integration yields
```math
\|q_h\|_2^2
\le C\left(h^2\int_0^h dr+h^4\int_h^\infty r^{-2}\,dr\right)
\le Ch^3.
```

Second, the Hardy inequality in three dimensions is
```math
\|f/|x|\|_2\le2\|\nabla f\|_2,\qquad f\in H^1(\mathbb R^3).
```
For smooth compactly supported $`f`$, it follows from
```math
\begin{aligned}
\|f/|x|\|_2^2
&=-2\mathop{\mathrm{Re}}\nolimits\int_{\mathbb R^3}
\overline f(x)\frac{x}{|x|^2}\cdot\nabla f(x)\,dx\\
&\le2\|f/|x|\|_2\|\nabla f\|_2,
\end{aligned}
```
using $`\mathop{\mathrm{div}}\nolimits(x/|x|^2)=|x|^{-2}`$; density gives the general case. Therefore (10) and the pointwise inequality $`|e^{ih/r}-1|\le h/r`$ give
```math
\|(W_h-I)\eta_h\|_2
\le h\|\eta_h/|x|\|_2
\le2h\|\nabla\eta_h\|_2
\le C\frac{h^2R^{1/2}}\delta. \tag{15}
```

Combining (12)--(15), and using unitarity of $`W_h`$, proves
```math
\|(T_h-\lambda_h)\phi_h\|_2
\le C\left(hR^{-1/2}+h^{5/4}\delta^{1/2}
+h^{3/2}+\frac{h^2R^{1/2}}\delta\right). \tag{16}
```

## 6. Iterate the approximate eigenvector and choose the parameters

For every vector $`\phi`$, telescoping gives
```math
T_h^n\phi-\lambda_h^n\phi
=\sum_{j=0}^{n-1}\lambda_h^jT_h^{n-1-j}(T_h-\lambda_h)\phi.
```
Since $`T_h`$ is unitary and $`|\lambda_h|=1`$,
```math
\|T_h^n\phi-\lambda_h^n\phi\|_2
\le n\|(T_h-\lambda_h)\phi\|_2.
```
Applying this to $`\phi_h=\psi+\eta_h`$, and then returning to the original initial state, gives
```math
\|T_h^n\psi-\lambda_h^n\psi\|_2
\le2\|\eta_h\|_2+n\|(T_h-\lambda_h)\phi_h\|_2.
```
Since $`n=h^{-1}`$, (10) and (16) imply
```math
\begin{aligned}
\|T_h^n\psi-\lambda_h^n\psi\|_2
\le C\left(
\frac{h^{5/4}}\delta+R^{-1/2}
+h^{1/4}\delta^{1/2}+h^{1/2}
+\frac{hR^{1/2}}\delta
\right).
\end{aligned} \tag{17}
```
Choose
```math
\boxed{\delta=h^{1/4},\qquad R=h^{-3/4}.}
```
The five terms on the right of (17) are, respectively,
```math
h,\qquad h^{3/8},\qquad h^{3/8},\qquad h^{1/2},\qquad h^{3/8}.
```
Because $`0<h\le1`$, (17) becomes
```math
\|S_n\psi-e^{iH}\psi\|_2\le Ch^{3/8}=Cn^{-3/8}.
```
Finally,
```math
0\le n^{1/4}\|S_n\psi-e^{iH}\psi\|_2
\le Cn^{-1/8}\longrightarrow0.
```
This rules out every positive eventual lower-bound constant $`c`$. QED.

## Relation to the local-error results

This proof does not dispute sharp one-step asymptotics of order $`h^{5/4}`$. Instead, it cancels most of the free remainder by an auxiliary comparison-vector correction, controls all remaining resonant shells, and bounds the Coulomb contribution of that correction by Hardy's inequality. The full $`n`$-step estimate is for the unchanged original ground state.

The cited background papers are:

- S. Becker, N. Galke, L. van Luijk and R. Salzmann, [Convergence rates for the Trotter splitting for unbounded operators](https://doi.org/10.1007/s10208-025-09730-w), [arXiv:2407.04045v2](https://arxiv.org/abs/2407.04045v2).
- D. Fang and X. Wu, [Trotterization with many-body Coulomb interactions: convergence for general initial conditions and state-dependent improvements](https://arxiv.org/abs/2604.07704v2), Section 6.

The proof above is self-contained and does not use a published global convergence-rate claim as an input.
