# Independent proof review 1: AIM 114 supporting lemmas

- Phase: post-proof review of fidelity, correctness, proof quality, reuse, documentation, and attribution.
- Date: 2026-10-05.
- Reviewer: Codex AI subagent `spectral_review`, independent of the manuscript author and proof implementer. This is an AI review, not human peer review.
- Verdict: **APPROVE the three supporting proofs at the recorded hashes.** No blocking issue found. This approval and the successful macOS checks below do not establish the full AIM 114 counterexample or replace the required authoritative Linux verification.

## Reviewed source and frozen boundary

The canonical original problem is AIM 114 at upstream commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. The complete six-page source manuscript and its mathematical scope were reviewed in [the spectral report](../../../solutions/114-nodal-surplus-counterexample/reviews/spectral-review.md). Its source SHA-256 remains `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`. My prior [statement approval](statement-referee-1.md) found no mathematical mismatch in the three supporting signatures.

The final files actually inspected have these hashes:

| File | SHA-256 |
| --- | --- |
| `AIM/P114/Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` |
| `Solution.lean` | `40cecf7e29a88f5756d10385648ca2fee0b33da8124c1d31bdde08b52321f0b4` |
| `AIM/P114/Definitions.lean` | `0c29c3c5b0cec95e1463ca190792b26a8d42733cdcca5b99796f84bd03a854ff` |
| `Challenge.lean` | `762965dcaab9eff7d0fca577597a1b900a7acde8899928eceb38d9a0c0c740fe` |
| `NUMERICAL_TARGETS.md` | `a248e229221f1e857a46b7aa542cef687a546a63ec2a4a5607a53c087951b889` |
| `comparator.json` | `ab020c73ee0d63c891ebc96dba9cdc7ff00c9ce48d59b006e12f8fe3de164a30` |
| `formalization.yaml` | `3f741e4470ca5864a4979a2aa72a797f23f718d283d5e144c7b747992b8d65ce` |

The approved definitions, Challenge signatures, and numerical-target document are unchanged. The implementation repeats the three approved theorem signatures, with no extra assumptions or weakened conclusions. Comparator lists exactly those three declarations, no replaceable definition holes, and only the three permitted axioms. The manifest clearly describes partial coverage and records post-proof review as pending at this reviewed snapshot; subsequent administrative updates to its review status are expected.

The [independent hash record](../verification/referee-1-source-sha256.json) additionally binds the toolchain file, Lakefile, dependency manifest, and my verification logs.

## Independent commands and observed results

I ran the following from `research/lean/114`, using `/Users/sholden/.elan/bin/lake` rather than relying on the implementer's PASS report. Each command exited zero. The logs record the exact absolute command, working directory, timestamp, output, and exit code.

| Command | Observed result | Evidence |
| --- | --- | --- |
| `lake env lean --version` | Lean 4.33.1, `arm64-apple-darwin24.6.0`, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6` | [Environment log](../verification/referee-1-environment.log) |
| `lake build Solution` | Successful; 3229 jobs, including the Solution axiom output | [Build log](../verification/referee-1-build.log) |
| `lake env lean AIM/P114/Proof.lean` | Fresh elaboration of the proof source succeeded with no diagnostics | [Proof elaboration log](../verification/referee-1-proof-reelaboration.log) |
| `lake env lean Solution.lean` | All three axiom reports emitted successfully | [Axiom log](../verification/referee-1-axioms.log) |
| `python3 ../../solutions/114-nodal-surplus-counterexample/check_algebra.py` | All exact finite checks passed | [Algebra log](../verification/referee-1-algebra.log) |

The transitive axiom output for **each** of `module_count_identity`, `sign_second_moment`, and `variance_mixture_kurtosis` is exactly:

```text
[propext, Classical.choice, Quot.sound]
```

I inspected the actual proof source for `axiom`, `sorry`, `admit`, `native_decide`, unsafe implementation hooks, and imports of Challenge. The proof module imports only the reviewed definitions; Solution imports only the proof module. No forbidden proof construct is present. Challenge's deliberate placeholders remain isolated from Solution. These are local development checks against the pinned cached dependencies; I did not run the isolated Linux harness, Comparator, separate kernel replay, or its negative controls.

## Proof correctness and quality

### Module sign-count identity

The private helper `negativeIndicator_eq` proves the exact relation between the strict negative indicator and the selected sign extension, including its harmless zero case. The multiplication and division helpers explicitly require nonzero factors or divisor. Their proofs split into real order cases and use ordinary exact arithmetic tactics.

The main theorem applies these helpers to the three products and to `(x+y+z)/a`. Every nonzero premise required by a helper is supplied from the approved assumptions. It then closes the remaining polynomial identity with `ring`. This is the actual local edge-count/pivot computation, not an invocation of the desired conclusion under another name. Its proof does not assume a graph construction, spectral identity, or matrix inertia theorem.

### Four-sign second moment

The proof unfolds the four explicit squared values, simplifies the known signs of the positive magnitudes and their negatives, and splits according to the order of the first two magnitudes. It then separates the positions of `z` relative to the two excluded triangle endpoints. The remaining Boolean cases are discharged by exact rational normalization and linear inequalities.

This covers both possible orders of `x,y`, including equality, and both strict sides of each excluded endpoint. No floating-point test, sampled sign pattern, interval certificate, or external computation establishes the theorem. The exclusions remain the same as the source calculation; no assertion about their probability is added.

### Integral moment inequality

The proof sets `a` to the actual integral of `V`. It constructs integrability of `V^2-(2a)V`, expands the centered square pointwise, and applies Bochner integral additivity and scalar linearity with the required integrability proofs. Simplifying the constant integral uses the probability-measure assumption. This establishes

```text
integral (V-a)^2 = integral V^2 - a^2.
```

The positive centered second-moment assumption therefore gives `integral V^2 > a^2`. Positivity of the mean makes `a^2` strictly positive, justifying the final strict division inequality. This is a short direct proof of the approved claim. It does not use an unproved variance identity, hide nonintegrable functions behind a totalized integral, or assume its conclusion.

All three hypotheses sets are satisfiable, as detailed in the statement report. The last theorem assumes positive variance and proves a normalized moment inequality; it does not prove positive variance of the manuscript's `v(R)`, construct a Gaussian mixture, or prove non-Gaussian convergence. No such bridge appears implicitly in its proof.

## Reuse, API, and attribution

I searched the pinned Mathlib sources, including `Mathlib/Data/Real/Sign.lean` and `Mathlib/Probability/Moments/Variance.lean`. Mathlib provides `Real.sign`, whose zero value is zero, and `ProbabilityTheory.variance_eq_sub`, stated with a `MemLp` hypothesis. The submitted support definitions use a documented sign extension at zero and explicitly exclude that case in their mathematical uses. Its two arithmetic helpers are private. The integral proof avoids introducing a competing public variance API and directly proves the short expansion in the exact integrability language of the approved statement. These choices are reasonable for this small support package; no mandatory reuse rewrite is needed.

The namespace, result names, comments, and target document communicate their limited role. The manifest distinguishes Sidney Holden's mathematical authorship from the AI-generated implementation and does not claim human review, complete formalization, or endorsement of the final code. The use of Apache-2.0 for the new formalization is explicitly separated from the unchanged submitted PDF. No attribution issue found.

## Finite regression script and canonical page

I also read and ran `research/solutions/114-nodal-surplus-counterexample/check_algebra.py`, SHA-256 `4121434e0f21ca9432b5d15829a8c699e3eae17a5357a3e8987ee8a4f0e91cbb`.

The script uses exact `Fraction` arithmetic. Its symmetric elimination allows scalar pivots and nonsingular zero-diagonal two-by-two pivots; the latter block has one positive eigenvalue, and its displayed Schur-complement update is correct. It counts inertia by eliminating in a different order from the manuscript's module-first derivation. Exceptional sampled configurations are skipped explicitly, with an acceptance-count floor. The checks passed for 504 sign-average cases, 448 graph cases (`114,116,113,105` for `m=3,4,7,12`), and 24 boundary-response cases, together with the fixed inertia controls and integrand identities.

The script's header and output accurately limit the result to exact finite regression checks. It supplies no spectral-frequency limit, measure theorem, asymptotic independence, or uniform moment proof. This is an appropriate supplementary role.

The revised canonical page inspected in this review has SHA-256 `219ddfa1c95dd7e7789a3971cdd86490ccb856e7f2651412fc84d99c9dd5005f`. It retains the original problem statement, uses PARTIAL status, records the Gaussian counterexample, and explicitly leaves universal variance bounds unresolved. It identifies the reviews as AI audits and says that the supporting lemmas do not formalize the full graph counterexample. Those claims agree with the evidence I inspected. I did not independently rerun the page's fresh literature searches, so this report is not additional evidence for its search-history sentence.

## Remaining limitations

The complete graph construction, spectral law, secular-phase measures, inertia-to-surplus theorem, stable limit, functional CLT, random evaluation, and moment transfer remain unformalized. The three theorems are useful proved supporting steps, not a Lean proof of the counterexample or either complete AIM 114 assertion.

Authoritative isolated Linux verification, its exact revision and retained logs, and independent final review by the other referee remain separate gates. My successful macOS build and fresh elaboration must not be described as those checks. No proof or boundary file was changed during this review.
