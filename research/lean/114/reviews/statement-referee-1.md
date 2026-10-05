# Statement boundary review 1: AIM 114 supporting lemmas

- Phase: independent review of definitions and Challenge signatures, before proof implementation.
- Date: 2026-10-05.
- Reviewer: Codex AI subagent `spectral_review`, independent of the mathematical author and proof implementer; this is an AI review.
- Verdict: **APPROVE the mathematical boundary at the hashes below**, subject to the separate required type-checking gate. Approval applies only to the three explicitly partial supporting results. It does not approve a complete formalization of AIM 114.
- Source problem: `problems/114-quantum-graph-nodal-clt.md` at upstream commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.

## Files actually read

| File | SHA-256 |
| --- | --- |
| `problems/114-quantum-graph-nodal-clt.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| `research/solutions/114-nodal-surplus-counterexample/statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| `research/solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf` | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| `research/solutions/114-nodal-surplus-counterexample/PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |
| `research/lean/114/NUMERICAL_TARGETS.md` | `a248e229221f1e857a46b7aa542cef687a546a63ec2a4a5607a53c087951b889` |
| `research/lean/114/Challenge.lean` | `762965dcaab9eff7d0fca577597a1b900a7acde8899928eceb38d9a0c0c740fe` |
| `research/lean/114/AIM/P114/Definitions.lean` | `0c29c3c5b0cec95e1463ca190792b26a8d42733cdcca5b99796f84bd03a854ff` |

The complete six-page PDF, the canonical problem, and the Markdown presentation were read. The companion [spectral review](../../../solutions/114-nodal-surplus-counterexample/reviews/spectral-review.md) documents my mathematical audit of the informal argument. I independently inspected the actual definitions and each Challenge formula; I did not infer correctness from the target document's descriptions.

## Correspondence of each signature

### `AIM.P114.module_count_identity`

This universally quantifies five nonvanishing conditions over four real inputs: `a`, `x`, `y`, `z`, and their three-term sum. Its left side is the sum of the three strict negative endpoint-product indicators minus the strict negative pivot indicator. Its right side is one plus the centered sign expression. Substitution `a=x_1+x_2+x_3`, `x=c_1`, `y=c_2`, `z=r*c_3` matches the local module step in manuscript Lemma 1.

The generalization from phase-derived inputs to arbitrary nonzero reals is valid. No relation between `a` and the other inputs is needed for this sign identity. The hypotheses ensure that every use of `nonzeroSign` agrees with ordinary sign: the definition's value `+1` at zero is never used. Division is by the explicitly nonzero `a`. The normalization and factor `1/2` are correct, and both sides are real quantities rather than natural-number subtraction. A positive choice of every input witnesses that the hypotheses are satisfiable.

This theorem does not encode spectral counting, matrix inertia, the Schur complement, or the global identity (9). Those missing links are accurately disclosed.

### `AIM.P114.sign_second_moment`

The four terms in `signSecondMoment` are exactly the four sign choices for the first two positive magnitudes with the third effective sign fixed positive. The divisor is four. Its conclusion is `1/2` minus one quarter of the indicator of the **strict** triangle event, matching the source sign average.

Positivity of all three magnitudes and the two excluded endpoints imply that every signed sum in the four terms is nonzero. In particular, a zero mixed sum would imply `z=|x-y|`, and a zero sum with both first inputs negated would imply `z=x+y`. Thus the modified sign at zero cannot affect the result. These hypotheses are not contradictory, and they appropriately leave degenerate boundaries outside this deterministic theorem.

Global sign reversal preserves the source module function when the sign arguments are nonzero, so fixing the third sign is the correct algebraic symmetry reduction. However, the theorem only establishes the four-term equality. It does not prove a probability law, fair-sign independence, or that the excluded boundaries have measure zero. The boundary document states that limitation explicitly.

### `AIM.P114.variance_mixture_kurtosis`

The quantified object is a real function on an arbitrary measurable space with a probability measure. Both `V` and `V^2` must be Bochner integrable. The mean is an actual integral, is strictly positive, and therefore has nonzero square. The variance assumption is the actual integral of the centered square and is strictly positive. The conclusion uses the correct quotient `3 * integral(V^2) / (integral V)^2`.

The probability-mass-one assumption is essential and is present. Together with the integrability hypotheses it permits expansion of the centered square and ensures that this centered square is integrable; the totalized integral does not conceal a missing existence condition. Subtracting the square of the mean then gives precisely the positive centered second moment. A two-point probability space with values one and three satisfies the assumptions, so this is not a vacuous implication.

This theorem deliberately stops at a strict moment inequality for the mixing variable. It neither constructs a Gaussian variable nor proves that the displayed quotient is a fourth moment of any law, and it does not discharge the positive-variance hypothesis for `v(R)`. These are material limits, correctly stated in the comments and target document. Omitting the manuscript's boundedness assumption is a valid generalization because the explicit integrability hypotheses suffice for this inequality.

## Definition and original-target audit

The custom definitions are concrete arithmetic expressions and strict real-valued indicators. None embeds a desired theorem as a definition, supplies an uninterpreted spectral oracle, or hides a full resolution hypothesis under a misleading name. All constants, signs, and endpoint conventions in the three signatures match the advertised supporting statements. Sidney Holden is credited as mathematical author, while Codex is identified for the formalization.

The original target concerns generic spectral-frequency nodal-surplus laws of metric Kirchhoff graphs. There is no such graph, operator, spectral law, Cauchy variable, empirical process, weak convergence, or Gaussian distribution in the reviewed Lean boundary. Thus there is a substantial and explicit gap between these supporting statements and the full counterexample. `NUMERICAL_TARGETS.md` preserves that gap and the separate unresolved universal variance assertion. This approval must not be reused as approval of a complete AIM 114 statement.

## Remaining gates and limits

No Lean build, type-check, transitive axiom command, Comparator run, sandbox run, or post-proof inspection was performed for this report. `Challenge.lean` intentionally contains `sorry` placeholders, which are not proof certificates. Proof implementation still requires the independent second boundary approval and successful type-checking required by AIM's protocol. The solution must not import Challenge, and all three advertised results must be checked with the approved definitions and complete signature comparison. Mathematical changes to any reviewed boundary reopen review.
