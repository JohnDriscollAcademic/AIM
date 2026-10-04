# Independent mathematical audit of AIM523 / PR #29

**Repository evidence:** [proof](../../solutions/siavash-sadeghi-523/aim523_report.pdf), [source](../../solutions/siavash-sadeghi-523/aim523_report.tex), and [problem](../../../problems/523-nystrom-logarithmic-loss.md). Submitted in [PR #29](https://github.com/MColbrook/AIM/pull/29) at `38659d428822c0fbee141ed089abcfa6e44f1f8a`.

Date: **2026-10-04**.

Reviewer: **independent_523_pr29 (OpenAI Codex AI)**, acting as a fresh independent mathematical referee within the coordinator's review. This is an AI mathematical audit, not a human referee report, publication, or formally verified proof. No human audit or formal verification is claimed.

## Reviewed object and independence

The coordinator identified PR #29 head as `38659d428822c0fbee141ed089abcfa6e44f1f8a`. The exact reviewed source is:

`C:\Users\MatthewColbrook\.codex\visualizations\2026\10\01\01a0f88a-46a6-73c1-ae0f-23d167c70a94\active-solution-pr-review-2026-10-04\pr29\research\solutions\siavash-sadeghi-523\aim523_report.tex`

Its SHA256, calculated directly from the source bytes, is:

```text
65759199509f89955bdf6adf7bd27b3d6c02f1247da4a4f81fe45b6c12720142
```

This audit applies to those bytes. The head identifier is the coordinator's supplied snapshot identity; this reviewer did not fetch or mutate Git state to establish it separately.

I read the manuscript itself, `CONTRIBUTING.md`, and `problems/523-nystrom-logarithmic-loss.md`. I did not read the authors' `REVIEW_REPORT.md`, `TARGET_AUDIT.md`, `REPRODUCTION_RECORD.md`, README verdicts, compile logs, or prior chat reasoning before making the mathematical assessment. The manuscript's own provenance sentence was not used as evidence of correctness. No compilation was performed, and no repository or manuscript file was changed. This audit is the only file written by this reviewer.

The additional local inputs were identified by these SHA256 values:

- `CONTRIBUTING.md`: `5df1c59e1330f88aaf1020eb3b49ff919761b86f234dad2e7ba27e3065a6c1b6`.
- `problems/523-nystrom-logarithmic-loss.md`: `40cb3bde0fb49822f6088838d3d211adc18b6d9aabc499958d995d6d933a9d17`.

## Decision

**The submitted argument is a valid counterexample to the complete displayed arbitrary smooth-amplitude formulation of the repository's AIM523 target. I found no mathematical gap that prevents that conclusion.**

It constructs one fixed smooth embedded closed curve, one fixed regular periodic parametrization, and one fixed smooth amplitude satisfying every stated derivative bound. At `s = 0`, for `epsilon = 1/2` and the admissible integer cutoff `N = 4 ceil(k)`, the target quantity grows at least as a positive constant times `sqrt(log k)`. Thus a constant independent of `k, N, epsilon` cannot exist, even if it depends on the fixed data and on `k0`.

This decision concerns the target that was actually provided and read. The amplitude is an arbitrary localized amplitude allowed by that statement. The manuscript does not identify it with a particular physical single-layer or double-layer Helmholtz kernel, and I do not make that additional identification. The distinction must remain visible in any resolution notice.

## Primary-reference and target verification

I browsed the primary [arXiv v3 PDF](https://arxiv.org/pdf/2507.22797v3) and [arXiv v4 PDF](https://arxiv.org/pdf/2507.22797v4), checking equations (9.3), (9.4), (9.6), Lemmas 11.1 and 11.3, and Conjecture 11.4. Both versions retain the conjecture. The [arXiv version history](https://arxiv.org/abs/2507.22797v3) dates v3 to 21 March 2026 and v4 to 28 September 2026. The normalization, the specialization `n = N` of the cutoff, and the angular integral in the local target agree with the displayed source equations. V4 gives the general square-root logarithmic estimate and the constant estimate for unit-parametrized convex curves with nonvanishing curvature. These source checks support the manuscript's bibliographic description.

The external GitHub link to the manuscript's cited repository commit `59a8f0c2957dd272f56bcf282dfe0c066a15f441` could not be retrieved through browsing. I therefore do not certify byte identity of that historical online page. This is not a mathematical blocker: the required local target was read and hashed, and the primary arXiv equations were independently retrieved. Limited searches using the paper identifier, conjecture number, Nyström, and logarithmic loss did not locate a later matching resolution. This is a dated search observation, not a claim that no such work exists.

The original paper introduces its amplitudes through physical Kress splittings. The independent conclusion here uses the repository's explicit universal smooth-amplitude formulation; a kernel-specific reading of the original conjecture requires a separate target comparison. Equation (9.6) supplies a class containing the constructed coefficient; it does not by itself make every member a physical Helmholtz kernel.

## Full target mapping

| Target requirement | What is supplied | Assessment |
| --- | --- | --- |
| Smooth embedded closed curve in the plane | A smooth closed curve with a retained straight horizontal arc | Admissible; smoothness does not prohibit a flat arc |
| Smooth `2 pi`-periodic parametrization with positive bounded speed | Local formula `gamma(t) = (t + t^2/2, 0)` and a global positive smooth reparametrization | Admissible; local speed is `1+t`, and a global finite strict upper bound can be chosen |
| Fixed data, rather than a curve or amplitude changing with frequency | Curve, parametrization, and both cutoffs are fixed | Satisfied |
| Smooth periodic amplitude with every required derivative uniformly bounded in `k` | `psi(theta) chi(t) chi(tau)`, extended smoothly by zero in the angular variable | Satisfied, because the amplitude is independent of `k` |
| Exact oscillatory coefficient and Fourier normalization | The factor `k`, `exp(-i m tau)`, and `1/sqrt(2 pi)` are retained | Satisfied; leading constants checked below |
| Functions on the curve and its Sobolev norm | Uses `H_k^0 = L^2(Gamma)` and arclength measure | Satisfied; no comparison of nonzero-order Sobolev norms is required |
| Claim for every real `s` | Failure at the permitted value `s=0` | Sufficient to disprove the universal claim |
| Claim for every positive `k0` and all `k > k0` | Lower bound holds for all sufficiently large real `k` | Sufficient for any fixed `k0`; an unbounded sequence also suffices |
| Uniformity in both cutoffs | Fixes `epsilon=1/2` and takes integer `N=4 ceil(k)` | Both are admissible and contain all modes used |
| Exclusion of `m=0` | Uses only positive integers with `m/k` in `[31/32, 33/32]` | Satisfied |
| A lower bound on the sum of norms, not merely a square sum or a pointwise value | At least `c k` modes individually have norm at least `c sqrt(log k)` | Gives the exact required failure after division by `k` |

In the source definition (9.4), the interval is `N-n < |m| <= (2-epsilon)N-n`. Taking `n=N` produces exactly `0 < |m| <= (1-epsilon)N`, as used in the repository and manuscript.

## Independent check of the construction

### 1. The smooth closed curve and its parametrization

The geometric existence sentence at source lines 69–73 is legitimate. A line segment can be retained in a smooth closed embedded curve while its ends are connected away from the middle. For example, a rounded racetrack can have smooth curvature transitions that vanish to all orders at its straight sections. It is unnecessary to use an analytic curve or strictly positive curvature.

Here is a more explicit reparametrization argument to verify the exact local polynomial, rather than just its approximate realization. Let `alpha(s)` be a regular arclength parametrization of such a curve of length `ell`, with `alpha(s)=(s,0)` on an interval containing `[-7/32,9/32]`. Choose a positive smooth `2 pi`-periodic function `v(t)` equal to `1+t` on `|t|<1/4`, and arrange `integral_0^{2 pi} v(t) dt = ell`. This is possible by adjusting a positive constant on the complementary part of the circle, choosing the completion length sufficiently large if necessary. One concrete form is `v(t)=eta(t)(1+t)+a(1-eta(t))`, with a cutoff supported inside a coordinate interval where `1+t>0`; the integral determines a positive `a` after choosing `ell` appropriately.

Put `h(t)=integral_0^t v(r) dr` on a lift. Then `h(t+2 pi)=h(t)+ell`, and `gamma(t)=alpha(h(t))` is periodic, smooth, and embedded. On the local chart, `h(t)=t+t^2/2`, so the submitted local formula holds exactly. Its speed is `v(t)>0`. Compactness supplies a positive minimum and finite maximum, and one may choose a fixed `c_max` strictly above that maximum. This proves the asserted global admissibility. There is no extra unit-speed constraint in the read repository target.

### 2. Fixed cutoffs and support margins

The periodic cutoff `chi` is interpreted on the coordinate chart centered at `0 mod 2 pi`; smooth support inside `(-1/4,1/4)` makes its periodic extension valid. The angular chart `omega(theta)=(-cos theta,sin theta)` has unit arclength Jacobian. A compactly supported smooth `psi` within this chart extends by zero to a smooth function on the full circle. All mixed amplitude derivatives are bounded independently of frequency.

For definiteness, one can take `theta_0 <= 1/8` and `delta_0=1/32`. For `rho in [31/32,33/32]`,

```math
tau_theta = rho / cos(theta) - 1.
```

Its minimum is at least `-1/32`. Its maximum is at most `(33/32) sec(1/8)-1 < 1/8`. Therefore every critical point has a fixed positive margin inside the plateau `[-1/8,1/8]`. This supplies the uniform support separation needed in the inner stationary-phase argument. The evaluation points `t=rho-1-delta` lie in `[-1/16,1/32]`, also strictly within that plateau.

The conversion of the Fourier integral from `[0,2 pi]` to this signed chart is valid because `m` is an integer: shifting the negative portion by `2 pi` leaves `exp(-i m tau)` unchanged. The proof's uniform continuous parameter `rho` is a convenience for the localized integral; the actual coefficients are used only at `rho=m/k` with integral `m`.

## Independent equation and constant check

### 3. Fourier signs and exact quadratic stationary phase

On the flat chart the kernel phase is `-k sigma(t) cos(theta) + k sigma(tau) cos(theta)`. Adding the Fourier phase gives

```math
q(tau)=cos(theta)(tau+tau^2/2)-rho tau,
qquad q'(tau)=cos(theta)(1+tau)-rho,
qquad q''(tau)=cos(theta)>0.
```

The unique critical point is the submitted `tau_theta`. Direct substitution gives

```math
q(tau_theta)=rho-cos(theta)/2-rho^2/(2 cos(theta)).
```

With `u=1+t`, subtracting `sigma(t) cos(theta)` gives exactly

```math
Psi(u,rho,theta)=rho-u^2 cos(theta)/2-rho^2/(2 cos(theta)).
```

Thus source equations `Lhat` and `Psi` have the correct signs. The inner stationary-phase multiplier is

```math
sqrt(2 pi/(k cos(theta))) exp(i pi/4).
```

Multiplication by the outer `k/sqrt(2 pi)` gives `sqrt(k) exp(i pi/4)/sqrt(cos(theta))`. This agrees with `stationtau`; no factor of `2 pi` is missing.

The phase is exactly quadratic and `chi` is identically one in a uniform neighborhood of every critical point. Hence all higher stationary-phase coefficients vanish. The remainder is smaller than every fixed power of `k`, uniformly for the compact parameter ranges. Uniformity follows from `cos(theta)` bounded away from zero and the fixed support margin. The outside multiplication by `k` merely requires choosing one more power in the inner remainder before renaming the exponent `B`. No derivative estimate on this remainder is needed for the claimed `s=0` conclusion.

### 4. The angular critical point and the curvature parameter

For `u=rho-delta` with the submitted range of `delta`, both `u` and `rho` are positive and `u<rho`. Differentiating gives

```math
Psi_theta=(sin(theta)/2)(u^2-rho^2/cos(theta)^2).
```

The bracket is strictly negative. The only stationary point on the support is therefore `theta=0`, and

```math
Psi_theta_theta(u,rho,0)=-A,
qquad A=(rho^2-u^2)/2=delta(rho-delta/2).
```

Useful explicit uniform constants are

```math
15/16 <= u <= 33/32,
qquad (61/64) delta <= A <= (33/32) delta.
```

These verify the `A asymp delta` assertion at source lines 119–121. For sufficiently large `k`, the interval `k^{-1/4} <= delta <= 1/32` is nonempty.

### 5. The degenerating angular stationary phase, including tails

Let `g=Psi(0)-Psi(theta)` and `b=psi(theta)/sqrt(cos(theta))`. Independently differentiating yields

```math
g''(theta)=rho^2/(2 cos(theta))-u^2 cos(theta)/2
           +rho^2 sin(theta)^2/cos(theta)^3.
```

Since `cos(theta)>0`, the first two terms are at least `(rho^2-u^2)/2=A`; the last is nonnegative. Thus the inequality at source lines 133–136 is correct on the whole support, not merely near zero. In particular `g'(0)=0` and `g'(theta)>=A theta` for `theta>=0`.

The Taylor expansion is

```math
g(theta)=A theta^2/2 + (u^2+5 rho^2)theta^4/48 + O(theta^6).
```

In particular, the submitted `O(theta^4)` remainder is uniform. After putting `Q=sqrt(kA)`, `zeta=Q theta`, and `phi(zeta)=k g(zeta/Q)`, one has

```math
phi(zeta)=zeta^2/2+O(zeta^4/(kA^2)),
qquad phi''(zeta)=g''(zeta/Q)/A>=1.
```

The bounds above give `kA^2 >= c k^{1/2}` and `Q >= c k^{3/8}`. On every fixed bounded `zeta` interval, the phase converges uniformly to `zeta^2/2`, and `b(zeta/Q)` converges uniformly to `b(0)=1`, uniformly over the entire allowed `rho,delta` set.

The tails are the potentially decisive issue in this argument. They are controlled as stated in the source. Write `a(zeta)=b(zeta/Q)`, extended by zero outside its support. Its supremum and total variation are bounded independently of `Q`, since scaling does not change the integral of the absolute derivative. For `zeta>=R>0`, `phi'(zeta)>=zeta>=R`, with `phi'` increasing. Integrating `a exp(-i phi)` by parts bounds the boundary term by `||a||_infinity/R`, the term with `a'` by `Var(a)/R`, and the remaining term by

```math
||a||_infinity integral_R^M phi''/(phi')^2 dzeta
 <= ||a||_infinity/phi'(R) <= ||a||_infinity/R,
```

where `M` is a support endpoint. If `R` exceeds the endpoint, the tail is zero. Thus the positive tail is at most `(2||a||_infinity+Var(a))/R`, uniformly. The negative tail has the same bound, also directly from evenness of `g` and `b`. The Fresnel limiting integral has a corresponding `O(1/R)` tail bound. Consequently bounded-interval convergence followed by `R -> infinity` establishes uniform convergence of the entire rescaled integral. It is not an unsupported use of stationary phase with a vanishing Hessian.

The resulting Fresnel constant is `sqrt(2 pi) exp(-i pi/4)`. For example, insert Gaussian damping `exp(-lambda zeta^2)` and evaluate `sqrt(pi/(lambda+i/2))`, then let `lambda` decrease to zero; the same tail estimate identifies this with the improper Fresnel integral. Returning to `theta` proves `uniformfresnel` with the stated uniform `o(1)`.

The two stationary-phase signatures cancel: `exp(i pi/4) exp(-i pi/4)=1`. The leading coefficient is therefore precisely

```math
sqrt(2 pi/A) exp(i k Psi(u,rho,0))(1+o(1)).
```

The earlier absolute rapidly decreasing error can be absorbed into this relative `o(1)`: `A` is uniformly bounded above, while the leading magnitude is `sqrt(2 pi/A)`. This checks source equation `nystromasymp` and ensures that the error cannot cancel the nonzero leading term.

## Independent norm and cutoff check

### 6. Arclength logarithm

For all sufficiently large `k`, the uniform asymptotic implies a uniform positive lower bound on the squared magnitude proportional to `1/A`, hence to `1/delta`. For instance, after making the relative error at most `1/2`, the bound `|Lhat|^2 >= pi/(2A) >= (16 pi/33)/delta` is available. The particular positive constant is not material.

On the chart, `ds=|gamma'(t)|dt=u dt`, with `u>=15/16`. The change of variable `t=rho-1-delta` has absolute Jacobian one. Hence for every integer `m` with `m/k in J`,

```math
||Lhat_{1,k,m}||_{L^2(Gamma)}^2
 >= c integral_{k^{-1/4}}^{1/32} ddelta/delta
 = c ((log k)/4-log 32)
 >= c' log k
```

for sufficiently large `k`. The fact that the integration interval depends on `m` is harmless: every interval lies inside the same fixed arc, and each estimate is an estimate of that individual coefficient's norm. The proof requires no disjointness between intervals for different modes.

### 7. Number of modes and integer cutoff

The interval `[31k/32,33k/32]` has length `k/16`. It contains at least `k/16-1` integers, hence at least `k/32` positive integers for all sufficiently large `k`. All these integers satisfy `m <= (33/32)k < 2 ceil(k)`.

The submitted choice has `(1-epsilon)N=2 ceil(k)`, and `N=4 ceil(k)` is a positive integer even if an integral quadrature cutoff were additionally required. It therefore includes all the counted modes. At `s=0`, `H_k^0=L^2(Gamma)` and the extra factor `<m/k>^s` is exactly one. Summing the individual norm lower bounds gives

```math
(1/k) sum_{0<|m|<=(1-epsilon)N} ||Lhat_{1,k,m}||_{H_k^0(Gamma)}
 >= c'' sqrt(log k) -> infinity.
```

No interchange of a norm and a sum, or conversion of a lower bound on a square sum into a lower bound on a sum, is being assumed. There are linearly many individual lower bounds. Constants concern the single fixed construction, so the permitted dependence of `C` on the data cannot avert divergence.

## Defects, qualifications, and scope

**No blocking mathematical defect was found in the reviewed source.** The brief geometric completion statement and the brief tail integration-by-parts statement can be made more explicit as above, but each is a valid standard argument with all required uniformity available from the source's choices. They do not require a repair to make the conclusion true.

The following limits are substantive and should accompany any status update:

1. The full repository formulation allows arbitrary smooth amplitudes. The manuscript proves a negative resolution of that formulation, not a constant bound and not the removal of the logarithm.
2. The example has a flat arc and a variable-speed parametrization. It gives no counterexample to the stated positive-curvature unit-speed case, and does not settle variants that additionally require arclength parametrization, strict curvature conditions, analyticity, or a particular physical kernel.
3. A lower bound for this coefficient quantity alone does not prove that every Helmholtz Nyström method needs logarithmic oversampling, or that the numerical convergence conclusion cannot be obtained by another estimate. The manuscript does not make those claims.
4. Failure at `s=0` fully negates the target quantified over all real `s`. The audit does not independently claim a lower bound for every nonzero Sobolev index.
5. The source is a conventional mathematical proof. The audit did not compile it, execute numerical experiments, reproduce authors' logs, or formally verify a theorem. Those activities would not substitute for the mathematical checks made here.
6. The separately supplied PR head and inaccessible historical GitHub page have the provenance limitations stated above. The exact audited source bytes and the exact locally read target are nevertheless recorded.

Under the repository's contribution policy, this is documented independent AI evidence for a complete negative resolution of the displayed general smooth-amplitude target. Any final catalogue entry should link the exact reviewed proof and this audit, identify the reviewer as AI, and preserve the physical-kernel limitation. A claim of independent human review or Lean/formal verification would be unsupported.

## Coordinator integrity addendum

After the mathematical assessment and report drafting, the coordinator supplied an additional byte-integrity check: all ten manifest entries match the exact raw Git blobs at PR head `38659d428822c0fbee141ed089abcfa6e44f1f8a`; the exported inspection snapshot changes only LF newlines to CRLF, with identical normalized content. This is the coordinator's integrity evidence, not a Git reproduction performed by this independent reviewer.

The two manuscript hashes must be distinguished:

- Exact raw Git blob SHA256: `ce1e45e24426750b64cd66c077deabd94c676f3627712352791565057ddb0576` (coordinator-verified).
- Inspected CRLF snapshot SHA256: `65759199509f89955bdf6adf7bd27b3d6c02f1247da4a4f81fe45b6c12720142` (calculated directly by this reviewer).

The mathematical audit applies to the inspected source text; the coordinator's comparison ties that text, modulo newline normalization, to the exact PR Git source. This removes the snapshot-to-Git content uncertainty without claiming that the two byte streams have the same SHA256. The online historical target-page retrieval limitation remains separate.
