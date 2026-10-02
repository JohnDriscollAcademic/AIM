# AIM 637: independent audit of the stationary Elo counterexample

**Review date:** 2026-10-02. **Reviewer:** Codex review agent, a fresh AI review separate from the submitted proof and its self-review. This is neither a human audit nor proof-assistant verification.

**Disposition:** Accept the complete counterexample and classify AIM 637 as **Solved**, with outcome **Disproved**. The mathematical proof and a fresh reproduction of every proof-critical finite check agree. No unresolved mathematical gap was found at the revision below.

## Pinned scope and target

- Pull request: [#24](https://github.com/MColbrook/AIM/pull/24).
- Reviewed head: `09eb03055ae12f58be5423c1c34b06ee90020b89`.
- Proof: [`aim637_counterexample.tex`](../../solutions/siavash-sadeghi-637/aim637_counterexample.tex), with [`verify_exact.py`](../../solutions/siavash-sadeghi-637/verify_exact.py) and its analytic continuum argument.
- Exact target: [`problems/637-elo-density.md`](../../../problems/637-elo-density.md), read directly from the reviewed Git tree and compared with the pinned `fa98b7525fa3f78317536a8825f9cfa0ae1c369c` statement cited by the submission.

The target quantifies over all admissible binary-score logistic parameters, so one singular invariant law suffices. The choice is N=2, rho=(0,0), c=1/2, K=9/10, and Kc=9/20<1. The coordinate map x -> (x,-x) gives exactly the two equiprobable maps x-(9/10)tanh(x) +/- 9/10; reversing the ordered pair exchanges the fair scores and introduces no further branch. The coordinate embedding is bi-Lipschitz onto the zero-sum line, so scalar singularity answers the precise requested absolute-continuity question. No continuous score noise, truncation, lattice rounding or linearization is introduced.

## Independent mathematical checks

1. **Existence and the integrability used later.** Recomputed the exponential Lyapunov estimate PW <= (3/4)W+81 for W=exp(|x|). Outside [-2,2], both branches retain the sign of x, and tanh(2)>0.9 gives the stated contraction. Inside that interval the crude exp(4)<81 bound is valid. Tightness of the Cesaro laws, the Feller property and lower semicontinuity yield an invariant law with integral W <=325. Thus the quadratically growing h belongs to L2 of this law. This is sufficient for every later stationary expectation and martingale variance bound.

2. **Uniqueness.** The derivative d=0.1+0.9 tanh(x)^2 is positive and strictly below one at each finite x. A stationary synchronous coupling exists by tightness of its fixed marginals and the Feller property. Its bounded distance observable r/(1+r) strictly decreases off the diagonal. Invariance forces concentration on the diagonal. Uniform contraction on the whole noncompact line is not assumed.

3. **Certified scalar residual.** Independently transcribed the six rational coefficients from the paper and checked their correspondence with the exact verifier and `certificate.json`. The residual is g+0.7-h+Ph with g=log(d). Direct differentiation gives the bounds |h'|<=484, |h''|<=1280 on [-7,7], |d'|<=9/5, |d''|<=18/5 and |g''|<=360. The chain rule therefore gives |R''|<=18956/5<4000 on [-5,5]. The second-derivative interpolation error on a grid interval of length 1/1000 is at most 1/2000; combined with each node being below -9/10000 this leaves the rigorous continuum margin -1/2500. R is even, so the nonnegative grid covers the whole compact interval.

4. **Tails.** Recomputed (I-P)x^2=2K x tanh(x)-K^2(1+tanh(x)^2). For x>=5, tanh(x)>99/100 yields the lower bound 729/100. The log-cosh term is 1-Lipschitz and the average absolute branch displacement is exactly K; each even tanh power has range [0,1]. Substitution gives h-Ph>=2555547/500000>0.7. Since g<=0 and the residual is even, both infinite tails are covered analytically. Finite numerical tail samples are not needed for this implication.

5. **Exact arithmetic implementation.** Read the whole program before execution. Intervals use integer endpoints divided by 2^192. Signed products, reciprocal intervals, squares crossing zero, rational inputs and endpoint monotonicity all round outward. Exponential range reduction bounds its reduced upper endpoint by 1/8; the 41st-and-later terms are bounded by one dyadic unit using the checked integer factorial inequality. Logarithms normalize into [1,2] and use the positive atanh series; the checked bound 4(2/5)^201<2^-192 covers its remainder. Multiplication by negative normalization exponents preserves containment through interval arithmetic. Hyperbolic formulas and all proof decisions avoid floating point. Proof checks are explicit exceptions, and remain active under Python -O.

6. **Drift to typical contraction.** The sum of the martingale differences h(X[j+1])-Ph(X[j]) has variance bounded by n times integral h^2. Together with the endpoint terms, the summed drift bound implies that the probability of log(Phi_w'(X0))>-(0.7-epsilon)n tends to zero. Stationarity supplies the moment bounds. The argument does not require an unproved ergodicity assertion or a density.

7. **Full-measure Hausdorff carrier.** Checked the important distinction between the dimension of a carrier and the full topological support. Since log(d) is 18-Lipschitz and each branch is nonexpanding, the distortion across any interval of diameter delta is <=18n delta. Good words thus produce intervals of length <=delta exp(-(0.7-2epsilon)n), with at most M 2^n such intervals for each fixed starting compact interval. Their s-content is summable for s>log(2)/(0.7-2epsilon). Reverse Fatou gives the limsup carrier mass at least mu([-R,R]); taking a union over integer R makes the mass one. Intersecting the full-measure carriers as epsilon decreases gives dimension <=10 log(2)/7<1. No almost-sure convergence of the preceding contraction event is needed. This proves pure singularity, not merely failure of differentiability of a hypothetical density.

8. **Atoms and support.** A largest atom would generate a finite invariant set under the increasing bijection F+, contradicting F+(x)>x. For support, successive F+ iterates escape to +infinity with gaps tending to zero. A fixed iterate of F- translates such a tail across any specified point without increasing its gaps; support invariance and closure then imply full support. These arguments are compatible with singular continuity.

## Fresh reproduction

The complete package was exported byte-for-byte with `git show` from the pinned head into an isolated scratch directory. Neither the submitted proof/code nor the repository catalogue was modified during this audit. All 18 entries of the submitted `SHA256SUMS` matched those exported bytes.

Environment: CPython **3.12.14**, Windows AMD64, standard library only. The executable was the bundled `python.exe` under `codex-primary-runtime/dependencies/python`. From the exported package directory, the following commands all exited 0:

```text
python -B verify_exact.py --output reviewer-exact.json
python -B -O verify_exact.py --output reviewer-exact-optimized.json
python -B -m unittest -v test_verifiers
python -B -O -m unittest -v test_verifiers
python -B verify_numeric.py --exact reviewer-exact.json --output reviewer-numeric.json
```

- Each exact run checked all **5,001 grid nodes** and **14 analytic constants**, and returned `PASS`, `complete global certificate`, and `global_drift_inequality_certified: true`.
- The largest certified grid upper endpoint occurred at j=394. Its enclosure was `[-0.0010033787264028412967530, -0.0010033787264028412967529]`.
- The certified log(2) enclosure was `[0.6931471805599453094172321, 0.6931471805599453094172322]`, strictly below 0.7.
- Both test runs passed all **7 tests**, including signed arithmetic, zero-crossing/domain boundaries, parameter consistency, rejection of partial/malformed records, partial CLI scope and invalid ranges. Normal run: 0.500 s; optimized run: 1.567 s.
- The separately implemented 80-digit Decimal program passed **20,024 supporting checks**, including the midpoint grid, second derivatives, ten rigorous enclosures, finite-difference differentiation checks and tail samples. Its sampled maximum was at x=0.3945 with residual approximately -0.00100327395111, and the displayed dimension bound was 0.9902102579427790. These are supplementary calculations, not replacements for interval bounds or the proof.
- The normal and optimized exact JSON objects were identical, and both matched the submitted exact record. The fresh numerical JSON object also matched the submitted numerical record.

The freshly generated exact record has SHA-256 `37d6ad8d060d9f7ef8f523908f320fc5196d0ea008279e30c6e7a2a591724c8e` after LF normalization; the optimized record has the same hash. The fresh numerical record has SHA-256 `b343371d2c9a68ae3e930fa44c2e61a81ed72fff7a36add5d35464482ca64b93` after LF normalization. These equal the corresponding committed records, making the complete reproduced values available in the package.

## Source identity and references

Git-object SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `aim637_counterexample.tex` | `c71b984f8c8bc9061053a3adb9147e6e93efb9aec7f30095baea3b9665e89f58` |
| `verify_exact.py` | `9255b46c2e1e09d068dd21054dc784ba01ae05df7ff3ee334a6168e5cc359c11` |
| `verify_numeric.py` | `46e1b1be53ae33ccf9d4c605f88bd9b8f1ca907e3fe56337d62e70e8c196258d` |
| `test_verifiers.py` | `50a804492e813aab4314e4d28eb51af2896e91581333ecc1fe00381434bcebaa` |
| `certificate.json` | `b56ac50c6687555d3a35aded5fd460859ebb55e5311e0d11dade4fd0cbdfb879` |
| `SHA256SUMS` | `1753aaed7794a7655dd3e4be3fc781d03a8e5a5f812993bb6b02dc2e4a4c4d55` |

The principal external reference was freshly checked against [Cortez and Tossounian, arXiv v2](https://arxiv.org/abs/2410.09180v2) and its [full text, Section 6](https://arxiv.org/html/2410.09180v2#S6). It explicitly leaves binary-score density unresolved; its numerical histograms do not establish a density. Authors, title, volume 36(4), year 2026, pages 3395-3418 and DOI 10.1214/26-AAP2306 were confirmed by the [author's university publication record](https://researchers.unab.cl/en/publications/convergence-and-stationary-distribution-of-elo-rating-systems/). The DOI redirect was inaccessible through the browsing tool, so it was not represented as a successfully fetched publisher page. The source credits the earlier general stationary theory and proves all additional lemmas used here; no missing theorem citation is needed to complete its argument.

The accepted scope is the explicit counterexample. It does not classify every parameter, establish a result for N>2, or answer the small-update density problem. The disposition rests on the fresh argument/code review and reproductions above, not on the package's submitted self-review or a novelty claim.
