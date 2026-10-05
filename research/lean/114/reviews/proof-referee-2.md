# AIM114 independent proof review 2

- **Phase:** post-implementation review of proof correctness and quality, probability scope, reuse, API, documentation, and attribution.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the implementation author.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the three supporting declarations at the exact hashes below. No blocking mathematical or proof-source defect was found.
- **Mechanical evidence:** fresh local build, direct re-elaboration of the proof source, and transitive-axiom output reproduced independently on macOS with pinned Lean 4.33.1.
- **Limit:** this report does not claim an authoritative Linux sandbox, kernel-replay/exporter, or Comparator run. Such checks are a distinct gate, and none was available for me to inspect at the time of this review. This package does not formally prove the AIM114 counterexample or resolve the universal variance target.

## Exact reviewed files

| File | SHA-256 |
|---|---|
| `AIM/P114/Definitions.lean` | `0c29c3c5b0cec95e1463ca190792b26a8d42733cdcca5b99796f84bd03a854ff` |
| `AIM/P114/Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` |
| `Challenge.lean` | `762965dcaab9eff7d0fca577597a1b900a7acde8899928eceb38d9a0c0c740fe` |
| `Solution.lean` | `40cecf7e29a88f5756d10385648ca2fee0b33da8124c1d31bdde08b52321f0b4` |
| `NUMERICAL_TARGETS.md` | `a248e229221f1e857a46b7aa542cef687a546a63ec2a4a5607a53c087951b889` |
| `comparator.json` | `ab020c73ee0d63c891ebc96dba9cdc7ff00c9ce48d59b006e12f8fe3de164a30` |
| `lakefile.toml` | `aa76173343a28a5f7696a9a7c2cbac1afa3a4138b061c6828a37d13e4f6ccefa` |
| `lake-manifest.json` | `f7f0c63c8e5bfc1b885e90ae8157be1f13f6a4385b6a5211c226fe026336cd48` |
| `lean-toolchain` | `3aac669c7a910ec2389f4e4f921b605adf6ebf2d1e0c9b9cd0be4d33f3f5db71` |

The mathematical-boundary hashes match my [pre-implementation statement review](statement-referee-2.md). I also read `formalization.yaml` at SHA-256 `3f741e4470ca5864a4979a2aa72a797f23f718d283d5e144c7b747992b8d65ce`; its verification/review status was still being updated, so this report does not certify any later administrative edits to that file. The immutable manuscript and source-problem hashes, complete boundary correspondence, and non-vacuity checks are recorded in my earlier statement report and [independent probability audit](../../../solutions/114-nodal-surplus-counterexample/reviews/probability-review.md).

I read the actual proof files before running the commands below. I did not use the implementer's build report, generated logs, or another reviewer's verdict as evidence of correctness. I made no proof-source changes.

## Fresh reproduction

Working directory: `/Users/sholden/Projects/AIM/research/lean/114`.

| Command | Result | Independent log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake env lean --version` | Exit 0; Lean 4.33.1, `arm64-apple-darwin24.6.0`, compiler commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6` | [environment](../verification/referee-2-environment.log) |
| `/Users/sholden/.elan/bin/lake build Solution` | Exit 0; successful 3229-job build | [build](../verification/referee-2-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/Proof.lean` | Exit 0; fresh direct proof-source re-elaboration, with no diagnostics | [re-elaboration](../verification/referee-2-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean Solution.lean` | Exit 0; all three transitive-axiom lists printed | [axioms](../verification/referee-2-axioms.log) |

For **each** of `AIM.P114.module_count_identity`, `AIM.P114.sign_second_moment`, and `AIM.P114.variance_mixture_kurtosis`, the independently reproduced axiom list is exactly:

```text
[propext, Classical.choice, Quot.sound]
```

No `sorryAx` or custom axiom occurs. The runner hashes every mathematical source and configuration input before the commands and checks those hashes after each command; all remained unchanged.

A separate [source audit log](../verification/referee-2-source-audit.log) records equality, up to whitespace, of every theorem signature in Challenge and Proof. This is only a source-level comparison, not a substitute for Comparator. It also records the actual package checkout heads: Mathlib `0df444a360eaa60ab8c11dca51a86af692955474` and LeanCert `621a43d7cf21f87872392a01e874f2f1dbddc926`, agreeing with the required pins. Solution imports only the proof module; the proof imports only Definitions. The deliberate Challenge placeholders do not enter either import chain.

## Actual proof paths

### Local module count

`negativeIndicator_eq` proves the real-valued indicator formula by unfolding the two transparent definitions. It is valid even at zero because the chosen extension has value `+1` there. `nonzeroSign_mul` proves multiplicativity on explicitly nonzero inputs by exhaustive sign cases and exact real arithmetic. `nonzeroSign_div` then combines the multiplication result with inverse-sign behavior, under a nonzero denominator.

The main theorem unfolds the local count and centered contribution, uses the hypotheses to show the common vertex value is nonzero, rewrites all three negative indicators, and closes the resulting identity by `ring`. In particular the division and sign rewrites do not silently invoke a false zero-case formula. The proof is an exact general real identity, not a finite sample check. It proves the local algebraic relation advertised in the source document and nothing about the spectral identification that precedes it.

### Four-sign second moment

The proof simplifies the signs of the individual positive and negative magnitudes and the positive three-term sum. It splits exhaustively according to the ordering of `x,y`, resolves the absolute value in the triangle inequality, and then splits the strict endpoint comparisons supplied by `houter` and `hinner`. The remaining conditional indicators and polynomial expressions are evaluated with `norm_num`, `simp`, and `linarith`.

The ordering split includes equality `x=y`; it does not discard that allowed case. The two endpoint exclusions are exactly the source boundary assumptions and prevent zero signed sums. The finite branch proof establishes the formula for all admissible positive real magnitudes, with the correct factor `1/4` and strict triangle event. There is no numerical rounding, interval approximation, enumerated magnitude grid, or probabilistic claim hidden in this case analysis.

### Integral kurtosis inequality

The proof defines `a` as the actual Bochner integral of `V`. From the explicit integrability hypotheses it derives integrability of `V^2-(2a)V` using `Integrable.const_mul` and `Integrable.sub`. A pointwise `ring` identity expands `(V-a)^2`. The proof then applies Mathlib's `integral_add`, `integral_sub`, and `integral_const_mul` with the required integrability witnesses. Integrability of the constant uses the probability measure's finite mass, and simplification correctly uses total mass one. The result is the genuine integral identity

```math
\int (V-a)^2\,d\mu=\int V^2\,d\mu-a^2.
```

The positive centered-moment assumption therefore gives a strictly positive difference. `sq_pos_of_pos hmean` establishes the strictly positive denominator, and `lt_div_iff₀` reduces the target to `3a^2 < 3 integral(V^2)`, which follows by linear arithmetic. This is a correct use of integration and positivity. In particular it does not treat a nonintegrable function's default Bochner integral as an expectation, assume the desired normalized inequality directly, or leave the centered-square expansion as an axiom.

The result remains an implication about a mixing variable. Its hypotheses do not construct or prove any property of the Cauchy-derived `v(R)`, and it does not compute a Gaussian fourth moment or establish a Gaussian-mixture law. Those are informal dependencies, accurately disclosed in `NUMERICAL_TARGETS.md`.

## Reuse, API, and documentation

I searched and read the pinned Mathlib source for the relevant integral and variance API. `Mathlib/MeasureTheory/Integral/Bochner/Basic.lean` provides precisely the additive and scalar identities used. `Mathlib/Probability/Moments/Variance.lean` has `variance_eq_integral` and `variance_eq_sub`; the latter is stated via `MemLp X 2` and the library variance API. Reusing the basic integration lemmas directly is appropriate for this short theorem stated with explicit integrals and integrability assumptions; no new competing variance framework was introduced.

I also inspected `Mathlib/Data/Real/Sign.lean`. Its `Real.sign` takes value zero at zero, unlike this package's deliberately specified extension. The small local `nonzeroSign` definition and its private helpers are transparent, project-scoped, and justified by the frozen statement's explicit nonzero hypotheses. They do not purport to replace the Mathlib API. The main declarations have descriptive names and source-specific docstrings, and the helper lemmas are private. Broad tactic imports are a maintainability choice, not a mathematical defect; no `native_decide`, unsafe proof escape, custom axiom, or non-kernel numerical certificate is used.

The definitions and metadata distinguish Sidney Holden's mathematical manuscript from the AI-generated formalization, preserve the source revision and PDF hash, and avoid claiming human review or author endorsement of the final Lean implementation. The source comments and scope document consistently call these supporting results rather than a proof of the graph counterexample. The Comparator configuration lists exactly the three advertised results, has no replaceable definition holes, and permits only the printed standard axioms.

## Disposition and remaining gates

**No blocking findings.** The final signatures and definitions remain identical to the approved boundary, and the three implemented proofs are correct at the reviewed hashes. My earlier warnings about incomplete scope remain fully applicable: the graph construction, spectral reduction, Cauchy/stable-law arguments, process limit, random evaluation, moment transfer, and identification of the particular non-Gaussian limit are not formalized here. The universal linear-variance assertion remains an unresolved separate target.

Local success and this referee approval do not satisfy the repository's authoritative isolated-Linux verification requirement. The future Linux run must inspect these exact mathematical inputs and independently check kernel replay, Comparator correspondence, permitted axioms, and the required rejection controls. No promotion of the full AIM114 page to “Lean verified” is justified by this package, even if those three supporting lemmas pass that workflow.
