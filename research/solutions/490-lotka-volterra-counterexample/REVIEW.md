# Audit of the D-stable Lotka–Volterra counterexample

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this submission-preparation session, separate from the supplied derivation and its originating checks.

**Decision:** Solved under the repository's documented-independent-audit convention. The argument supplies a counterexample to the complete recorded global-attraction assertion.

**Pinned target:** [Problem 489 at `823ea0c6f9151792238d8ccbe7d64ea7d66faf5d`](https://github.com/April-Hannah-Lena/AIM/blob/823ea0c6f9151792238d8ccbe7d64ea7d66faf5d/problems/489-lotka-volterra-d-stable-global-attraction.md), preserved in [statement.md](statement.md), with relative links repaired for its new location. This is [problem 490 at the earlier catalogue revision](https://github.com/MColbrook/AIM/blob/37a25361f243be77daea0ae0b3c5167b57f1b5f3/problems/490-lotka-volterra-d-stable-global-attraction.md). The matching problem currently numbered 490 is unrelated to this submission.

**Reviewed package:** [PROOF.md](PROOF.md), the three exact certificate modules and their finite data, the orchestration and supplied audit scripts. [reproduction.json](reproduction.json) records the original and adapted proof hashes, all supplied input hashes, versions and successful commands; [SHA256SUMS.txt](SHA256SUMS.txt) pins this review and the complete adapted package.

**Current catalogue record:** [Archive 650](../../resolved/650-lotka-volterra-d-stable-global-attraction.md). [ID mapping](../../solution_reviews/2026-10-02/490-id-mapping.json).

## Provenance and scope

The mathematical argument and finite certificates were supplied before this session; the material does not identify its author. I read the complete proof and all verifier implementations, checked the analytic reduction independently, reran both complete integer-arithmetic implementations, and wrote additional checks using a separate evaluation of the Fourier equations. I also prepared the repository formatting, documentation and catalogue transition. The supplied logs were supporting material, not a substitute for those new runs.

The core verifier modules and the certificate data are retained byte-for-byte. The proof's equations are preserved with the repository's protected Markdown math delimiters and core TeX operators. Bibliographic links and current provenance replace references to the originating conversation. Requirements are pinned to the tested NumPy version. The reference statement preserves its mathematical and status evidence; only relative navigation changes.

This is an AI mathematical and implementation audit of a previously supplied argument. The same reviewer prepared this submission; no additional reviewer of those edits, human peer review, publication, proof-assistant verification or novelty-priority determination is asserted. The review date records analysis of the supplied evidence, not a fresh literature search. Existing source assessments remain in the archive.

## Full-target comparison

The target quantifies over every finite dimension and every real D-stable interaction matrix. It requires both forward existence and convergence for every strictly positive initial population. The counterexample takes dimension four, the exact displayed rational matrix, and coexistence equilibrium $`x^\ast=\mathbf1`$. Its vector field is precisely $`\dot x_i=x_i(A(x-\mathbf1))_i`$, with the same sign convention as the target.

The D-stability certificate covers every positive constant diagonal matrix, without sampling or restricting its entries. The periodic-orbit certificate constructs a nonconstant solution with all four coordinates strictly between $`1/8`$ and $`4`$ for every real time. Thus its initial state is admissible and its solution exists globally. A nonconstant periodic solution cannot converge to the coexistence equilibrium. Failure of that convergence clause suffices to refute the full universal assertion.

The initial state is specified by a unique fixed point in an explicitly certified Fourier ball. The nearby rational vector printed in the proof is only a reference point. Neither numerical integration nor the assertion that rounded coordinates lie exactly on an orbit is used.

## D-stability for every positive diagonal scaling

I checked the relation between the characteristic coefficients and the principal minors of $`-A`$: each principal minor for an index set is multiplied by the corresponding product of positive diagonal entries. The determinant permutation formula in `dstability.py` recomputes the minors from the exact integer numerator matrix. All 15 principal minors are positive, so all four characteristic coefficients are positive.

For the quartic characteristic polynomial, the remaining Hurwitz determinant is

```math
P=c_1c_2c_3-c_3^2-c_1^2c_4.
```

Each of the 21 rational certificate atoms has the form $`a d^u+b d^v-c d^w`$, with $`u+v=2w`$, positive coefficients and $`c^2\le4ab`$. AM–GM makes each atom nonnegative on the entire positive orthant. The program expands the polynomial exactly and checks that the remainder has exactly its 38 nonzero exponent vectors and satisfies the coefficientwise bound

```math
[d^\alpha]\left(P-\sum_\ell G_\ell\right)
\ge\frac7{100}\lvert p_\alpha\rvert>0.
```

This is a strict positivity certificate for all positive diagonal entries. It is not based on a finite selection of diagonal scalings or approximate eigenvalues. Since $`P>0`$ and $`c_3,c_4>0`$, also $`c_1c_2-c_3>0`$. The first column of the quartic Routh table is strictly positive. I checked the equivalent imaginary-axis-crossing argument supplied in the proof: neither a zero root nor the possible nonzero imaginary-root condition can occur along the stated homotopy. Thus every $`DA`$ is Hurwitz.

## Banach space and the Fourier equations

The real coefficient space uses conjugate symmetry, a real zero mode, and the weighted sum of absolute real and imaginary parts. Its norm is the full two-sided coefficient norm restricted to real-valued functions. Complex multiplication is submultiplicative for the sum of absolute real and imaginary parts, and the convolution inequality follows by an absolutely convergent double sum. The resulting space is a real Banach algebra, and its norm bounds the uniform norm of the Fourier series.

The product space has the maximum of the frequency norm and the four species norms. Differentiation alone is unbounded on that space, but the explicitly defined preconditioned map has bounded finite coordinates and tail

```math
\mathcal T(z)_{i,k}
=\left(1-\frac{\omega}{\bar\omega}\right)c_{i,k}
+\frac{(Ac_k)_i+\sum_j A_{ij}(c_i*c_j)_k}{ik\bar\omega},
\qquad \lvert k\rvert>N.
```

This formula defines a continuously differentiable map on the full Banach space without assuming that its input series can be differentiated. It preserves the real conjugate-symmetric subspace. The finite phase equation is the imaginary part of the first coefficient of the first species; its position in the real-coordinate ordering agrees with the implemented phase row.

The reference degree is $`M=48`$, the finite cutoff is $`N=128`$, and the core has $`1029`$ real coordinates. The anchor and inverse matrix have exact integer numerators and denominators $`2^{46}`$ and $`2^{40}`$. No unverified approximation property of the inverse matrix is assumed.

## Finite derivative, all tail modes and derivative variation

I derived the kernel of the coefficient derivative as

```math
K_{ij,k}=A_{ij}\delta_{k0}+A_{ij}\bar c_{i,k}
+\delta_{ij}(A\bar c_k)_i.
```

The finite Jacobian represents $`ik\bar\omega I-K*`$, with the frequency column $`ik\bar c_k`$ and the phase row. The supplied real/imaginary formulas account for both positive and negative input modes. Because the kernel is supported in degrees at most $`M`$, the only tail inputs that can reach the finite equations are modes $`N+1`$ through $`N+M`$. Every higher input mode has zero finite output at the anchor.

The weighted block column sums correctly bound the induced norm from each input species block to each output block. Summing these bounds across input blocks bounds the maximum-of-blocks norm. Finite and tail inputs of a given species share a single input block, as required by the full-space norm. The code uses integer numerators with an explicit factor of two to account for the nonzero-mode weights.

The core-only bound $`\lVert I-RJ\rVert<10^{-7}`$ makes the square product $`RJ`$ invertible by the Neumann argument; hence $`R`$ itself is invertible. In the tail the leading derivative cancels at the anchor, leaving the convolution divided by $`ik\bar\omega`$. Since $`\lvert k\rvert\ge N+1`$, the bound using $`\sum_j\lVert K_{ij}\rVert/((N+1)\bar\omega)`$ covers all infinitely many remaining modes. The anchor's tail coefficients vanish, so its frequency derivative contributes no omitted tail term.

For derivative variation, I checked both bilinear frequency terms and both quadratic convolution terms. The latter have species bound $`2a_i\lVert z-\bar z\rVert\lVert h\rVert`$, where $`a_i=\sum_j\lvert A_{ij}\rvert`$. In the finite part the former use the explicitly computed norm of $`RD_N`$. In the tail, cancelling $`ik`$ leaves the frequency factor $`2/\bar\omega`$, while the quadratic contribution retains the extra divisor $`N+1`$. These are exactly the terms in the implemented bound $`Z_2`$. Projection of a convolution into finite coordinates cannot increase its coefficient norm.

## Exact arithmetic and new reproduction runs

I inspected every acceptance computation. Principal minors and polynomial coefficients use Python integers and `Fraction`. Fourier residuals and kernel construction use object arrays containing arbitrary-precision integers. The Jacobian's integer entries fit in signed 64-bit storage; assigning larger Python integers to that storage raises rather than silently accepting them in the tested environment.

The fast large product splits signed integers into base-$`2^{26}`$ digits. The strict integer bound

```math
1029(2^{26}-1)^2<2^{63}
```

controls the absolute sum of every dot product, and therefore every partial sum regardless of accumulation order. Minimum signed integers are explicitly rejected before taking absolute values. Digit products are recombined as arbitrary-precision Python integers. I also ran the complete slower object-array product, removing reliance on the accelerated multiplication route. Both runs reproduced the exact stored Fourier and positivity output fractions byte-for-byte.

The newly reproduced bounds include

```math
Y<10^{-10},\qquad Z_1<4/5,\qquad Z_2<60000,
\qquad r=10^{-7}.
```

Their diagnostic values are approximately $`3.6773449289201\times10^{-12}`$, $`0.7910926956545301`$, and $`56239.673468296154`$. These decimal strings are not acceptance thresholds. The reference residual has degree at most $`2M=96<N`$, so no residual tail is omitted.

The supplied audit's five exact convolution/Jacobian checks and 99 Python-integer product checks also passed. In addition, the new `review_checks.py` independently reconstructs the anchor from the CSV and directly evaluates the polynomial Fourier equations using Python-integer complex-pair sums. It checks all 196 coefficient pairs and all 1029 residual coordinates, then uses the exact central-difference identity for a quadratic polynomial to check three complete Jacobian-vector products, including an input supported only in the finite-to-tail interface. These directional cross-checks supplement the analytic implementation audit; they are not a claim to enumerate every Jacobian basis vector. The main verifier's rejection of Python `-O` was also checked.

## Existence of a classical periodic solution

The derivative bound on the closed ball is strictly less than $`0.806`$, while the image lies within radius strictly less than $`0.807r`$ of the anchor. The closed ball is complete, so Banach's fixed-point theorem gives a unique fixed point there. Invertibility of $`R`$ forces every finite equation, including the phase condition, to vanish. Each tail multiplier is nonzero, so every tail equation also vanishes.

Frequency is positive throughout the ball. At the fixed point the right-hand side of the ODE belongs to the coefficient algebra. The equations therefore imply summability of the Fourier coefficients after multiplication by the frequency index. The Fourier series has a uniformly convergent derivative and defines a classical continuously differentiable periodic solution. This establishes an actual orbit of the specified ODE, including all Fourier modes.

## Strict positivity, period and failure of convergence

The interval code brackets $`\pi`$ by alternating rational arctangent series in Machin's identity. I checked the orientation of both arctangent bounds and their linear combination. On arguments of absolute value below four, the sine and cosine recurrences have the stated degrees 35 and 34; the zero next Taylor coefficient justifies remainder orders 37 and 36. Integer multiplication, division and scaling round interval endpoints outward, including for negative arguments. All grid arguments are within the required range.

The complex-power recurrence evaluates the real reference polynomial at 4096 equally spaced points. Every point on the circle lies within $`\pi/4096`$ of a grid point. Subtracting the exact derivative bound times this distance, and then the uniform ball error $`r`$, controls the solution between grid points. Adding the same errors gives the upper bound. The lowest coordinate lower bound exceeds $`0.1283906>1/8`$, and every coordinate upper bound is below four.

The real first Fourier coefficient changes by at most $`r/2`$ in the weighted norm, and remains greater than $`3/5`$. Thus the orbit is nonconstant. Combining the rational bounds on $`\pi`$ and the frequency interval gives a period strictly between $`7.86959`$ and $`7.86961`$. Periodicity supplies a bounded solution for all real time in the interior of the positive orthant. If such a solution had a forward limit, taking successive periods from any fixed phase would force every phase to equal that limit, contradicting nonconstancy.

The dimension-four counterexample already resolves the recorded universal target. The stated extension by a negative identity block preserves D-stability and the periodic solution. The logarithmic-coordinate observation is also consistent: $`A\mathop{\mathrm{diag}}\nolimits(e^z)`$ is similar to $`\mathop{\mathrm{diag}}\nolimits(e^z)A`$. Neither extension is needed for the status decision.

## Review result and reproducibility

I found no unresolved mathematical or certificate-verification gap in the complete argument. The certificate establishes a counterexample, not just a finite Fourier approximation, a numerical cycle, or stability at selected diagonal scalings. The analytic tail estimates, exact inequalities and positivity control together justify the claimed resolution.

The [README](README.md) gives reproduction commands. The [default verification](verification.log), [arbitrary-precision verification](slow-verification.log), [supplied audit reproduction](audit.log), and [new review checks](review-checks.log) are logs from this session. [reproduction.json](reproduction.json) records their provenance and the pinned environment. Checksums establish file identity; catalogue validation checks structure and navigation. The analytic audit above explains why the reproduced computations prove the target's negation.
