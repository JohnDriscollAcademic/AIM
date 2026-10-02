# Independent review of the D-stable Lotka–Volterra counterexample

**Reviewed:** 2026-10-02 by a separate OpenAI Codex AI review agent in the active-pull-request review. This review did not author the submitted proof or its certificates. It is not human peer review or proof-assistant verification.

**Decision:** Accept the mathematical package as a counterexample to the full AIM 489 target. The existing problem ID and page should be retained and marked **Solved**, with this review and the proof linked. No mathematical gap was found. The pull request's unrelated catalogue renumbering and hydrogen package are outside this decision.

**Pinned submission:** [PR #22](https://github.com/MColbrook/AIM/pull/22), head `7faf58307c22882ccd730eae421acb61fca3f43d`, directory `research/solutions/490-lotka-volterra-counterexample/`. The directory's historical number 490 is not the current problem ID. Its existing `Solved` assertions and archive-650 links are submission metadata, not evidence for this decision; those links need to follow the retained AIM 489 page during integration.

**Pinned target:** [AIM 489 at main revision fa98b7525fa3f78317536a8825f9cfa0ae1c369c](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/489-lotka-volterra-d-stable-global-attraction.md). The target requires forward existence and convergence for every strictly positive initial state, in every finite dimension, under D-stability alone.

## Evidence identity and reproduction

The complete proof, `dstability.py`, `fourier.py`, `positivity.py`, `verify.py`, `audit.py` and `review_checks.py` were read before execution. The solution directory alone was exported from the pinned head into a scratch directory. No supplied log was accepted in place of a fresh run. [The input hash manifest](489-input-hashes.json) records all 24 exported files. Important SHA-256 values are:

| File | SHA-256 |
|---|---|
| `PROOF.md` | `fe7c43ae3376ab1fe5dc60f27f5e90af9225b6bdf8a11906a684d5fe764c5966` |
| `fourier_certificate.npz` | `f18907b6bc041a87d4561a24605b4dc81c6cd79d092539f219ecf5d3a5dc2eec` |
| `dstability_certificate.json` | `b56fc79b8802e4a71a3a3cda6179958730c1519af0480f4c73a51858ad401d71` |
| `fourier.py` | `0a82a32f5cc89520598acb4b6cc67a42f9ceb9b4f52be8da28676db8082e6757` |
| `positivity.py` | `1d1253d2d29b02ae5cc0fd0fb1cdc4fdf63af90011c997d574f41cd67541de15` |

Fresh runs used Python 3.12.14 and NumPy 2.3.5 on Windows 11. Run the first four commands from an export of the pinned package; the last command receives that package's absolute path:

```sh
python -B verify.py
python -B verify.py --slow-matmul
python -B audit.py
python -B review_checks.py
python -B /path/to/489-independent-checks.py /path/to/exported/package
```

| Check | Result | Fresh evidence |
|---|---|---|
| Complete exact verifier | Passed, 43.1 seconds | [Log](489-verification.log) |
| Complete direct Python-integer matrix product | Passed, 128.5 seconds | [Log](489-slow-verification.log) |
| Supplied convolution and product cross-checks | Passed | [Log](489-supplied-audit.log) |
| Supplied CSV, residual and central-difference cross-checks | Passed | [Log](489-submission-checks.log) |
| New independent checks | Passed | [Script](489-independent-checks.py), [log](489-independent-checks.log) |

[The reproduction record](489-reproduction.json) records full commands, timings, environment and output identities. The fast and slow runs produced identical exact output fractions. Compared with the pinned JSON outputs, Windows changed only LF line endings to CRLF; parsing and LF-normalized SHA-256 values match exactly. An initial auxiliary identity check detected this text-format difference; the corrected check normalizes only those two regenerated output files. All implementation and certificate input hashes are checked byte-for-byte.

The newly written script independently recomputes all 15 principal minors using rational Gaussian elimination, checks the 21 printed AM–GM atoms against their machine representation, and reconstructs **all 1,453,977 entries** of the finite-plus-interface Jacobian by differentiating each scalar polynomial equation in each coordinate basis direction. That reconstruction uses signed-mode dictionaries and exact integer complex pairs, without the submitted derivative kernel or its real-coordinate formulas. Every entry agrees. This closes a stronger implementation check than the submission's sampled Jacobian-vector products.

## Match to the complete target

The proposed system uses the displayed exact rational four-by-four matrix, coexistence equilibrium $`x^*=\mathbf 1`$, and precisely $`\dot x_i=x_i(A(x-\mathbf 1))_i`$. The target permits this dimension and arbitrary real interaction signs. The proof constructs an actual nonconstant periodic orbit inside the positive orthant. A single such orbit refutes the universal convergence assertion, even though that orbit itself exists for every real time. No assertion about all other initial states is necessary.

The printed rational initial vector is correctly described as an approximation to the orbit. The exact initial state is defined by the fixed point of the certified Fourier map; treating the approximate vector as exact would be invalid, but the proof does not do so.

## D-stability on the entire positive orthant

For each principal index set, the corresponding principal minor of $`-DA`$ equals the principal minor of $`-A`$ times the product of the selected positive diagonal entries. All 15 minors were checked exactly and are positive. Thus all four characteristic coefficients are positive.

The remaining quartic condition is positivity of

```math
P=c_1c_2c_3-c_3^2-c_1^2c_4.
```

Every certificate atom $`ad^u+bd^v-cd^w`$ is nonnegative for every positive $`d`$: the verified identities $`u+v=2w`$ and inequalities $`c^2\leq4ab`$ reduce this to AM–GM. The exact 38-coefficient remainder is at least $`(7/100)|p_\alpha|`$ at each exponent, with no additional exponents. It is strictly positive on the positive orthant. The proof consequently establishes $`P>0`$ for all positive diagonal scalings, with no finite sampling assumption.

From $`P>0`$ one gets $`c_1c_2-c_3>0`$. The supplied elementary root-crossing argument verifies the quartic criterion independently of a cited Routh-table theorem: start the cubic with small positive constant coefficient; its only possible nonzero imaginary crossing occurs at $`c_3=c_1c_2`$. Then start the quartic with small positive constant coefficient. A nonzero imaginary crossing requires $`\omega^2=c_3/c_1`$ and $`c_4=c_3(c_1c_2-c_3)/c_1^2`$, which the strict certificate excludes. Zero roots are excluded by positive constant coefficients. Continuous dependence of polynomial roots completes the argument. Therefore every $`DA`$ is Hurwitz.

## Fourier fixed point, including infinitely many modes

The stated species norm is the two-sided sum of absolute real and imaginary Fourier parts restricted to conjugate-symmetric sequences. This is a complete real sequence space, bounds the uniform norm of its Fourier series, and is submultiplicative under convolution. The real zero-mode restriction is preserved. The maximum over frequency and species blocks gives the declared product norm.

Differentiation is unbounded in that norm, but the proof explicitly defines the preconditioned tail map after cancelling the derivative multiplier. That map is a bounded quadratic expression in the coefficient algebra and frequency. It is continuously differentiable without assuming differentiability of its inputs. The finite part evaluates only finitely many derivative coordinates.

At the anchor, the derivative kernel has support through mode 48. Consequently only input modes 129 through 176 can feed the finite equations; every higher input has zero finite output. The independently reconstructed matrix includes all those interface coordinates. The block-column norms correctly combine finite and interface coordinates of each species into one input block. The bound $`\lVert I-RJ\rVert<10^{-7}`$ makes the square product invertible, hence makes $`R`$ invertible.

The infinite output tail is bounded by the full convolution norm divided by $`129\bar\omega`$. The anchor has no tail coefficients, so its tail frequency derivative vanishes. The derivative-variation calculation includes both frequency bilinear terms, both quadratic convolution terms, and the tail cancellation of the index multiplier. Its two factors and row sums agree with the code. The residual has degree at most 96, below the finite cutoff 128, so no residual tail is dropped.

The maximum stored Jacobian numerator is `7191457749287168000`, strictly below $`2^{63}`$. The digit-product bound $`1029(2^{26}-1)^2<2^{63}`$ bounds every signed-64-bit partial sum in the accelerated multiplication. Recombination uses arbitrary-precision integers. The separate complete Python-integer multiplication additionally removes reliance on that acceleration. Floating-point values occur only in diagnostic printing.

The reproduced bounds are

```math
Y<10^{-10},\qquad Z_1<\frac45,\qquad Z_2<60000,
\qquad r=10^{-7}.
```

They imply a contraction factor below $`0.806`$ and image radius below $`0.807r`$. Iterates stay in the closed ball and successive differences are bounded by a geometric series. Completeness gives their limit, continuity gives the fixed-point equation, and the strict contraction gives uniqueness in the ball. This explicitly checks the hypotheses and conclusion of the contraction argument.

Invertibility of the finite preconditioner and nonzero tail multipliers imply all Fourier equations, not merely their projection. At the fixed point, positive frequency and membership of the nonlinear right-hand side in the coefficient algebra imply summability of the coefficients multiplied by their Fourier index. The differentiated series therefore converges uniformly and defines a classical continuously differentiable periodic solution of the original ODE.

## Strict positivity and nonconstancy

The positivity verifier's interval operations round both endpoints outward, including under negative multiplication. Alternating arctangent series bracket the two terms in Machin's identity for $`\pi`$. The Taylor recurrences and remainders for cosine and sine have orders 36 and 37; their intervening coefficients vanish. All angle intervals lie inside the asserted range of absolute value below four.

The grid estimate is extended to every phase using the exact derivative bound times $`\pi/4096`$, then the uniform fixed-point error $`r`$. Thus it certifies the actual solution between grid points. Reproduced coordinate lower bounds are approximately 0.1283906814, 0.1290749624, 0.1723087114 and 0.5566275627; every upper bound is below 3.09. All exact comparisons against $`1/8`$ and 4 pass. The nonzero first real Fourier coefficient remains above $`3/5`$, using its weighted error bound $`r/2`$. The exact period bracket lies inside $`7.86959<T<7.86961`$.

The orbit is therefore strictly positive and nonconstant for all time. If it converged forward to an equilibrium, taking integer-period subsequences from each phase would make every phase equal to that equilibrium. This contradicts the nonzero Fourier coefficient and completes the counterexample.

## Primary-source and reference check

Hong and Pego's authors, title, journal volume **83**, article **16** (2021), and DOI match the [publisher record](https://link.springer.com/article/10.1007/s00285-021-01638-7). Their [arXiv version 2](https://arxiv.org/pdf/2102.00611v2), §2.3 Definition 2.1 and §2.4, printed pp.6–7, uses the same D-stability definition and states the relevant global-attraction conjecture. It distinguishes D-stability from Volterra–Lyapunov stability. This is contextual evidence, not a source of the submitted counterexample.

The independent comparison with [Lu and Takeuchi, *Global Dynamical Behavior for Lotka–Volterra Systems*, RIMS Kôkyûroku 828 (1993), 171–178](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0828-16.pdf), equation (1), Definition 2 and the named conjecture on pp.171–172, confirms the same system and quantifiers. Its qualitative-stability sufficient theorem is stronger than the premise under review. The NSF-hosted Hong–Pego download returned an access error; the arXiv manuscript and publisher identity were accessible and checked instead.

No unverified specialized result is imported to construct the orbit. The finite certificate, algebra estimates, quartic root argument and contraction argument supply the mathematical steps. These primary references suffice for the contextual attribution used in the proof; no missing reference changes the correctness decision. This review does not assert novelty priority or a comprehensive new literature search.

## Integration conditions

Retain the submitted exact matrix, integer arrays, verifier implementations and proof mathematics. Repair obsolete archive and numbering links to the existing AIM 489 page and this fresh review; regenerate any package checksums after documentation changes. Do not renumber or remove unrelated problems. The accepted outcome is **counterexample: D-stability does not imply global attraction**, with an explicitly documented independent AI audit and reproduced exact certificates.
