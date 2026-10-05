# AIM114 independent statement review 2

- **Phase:** mathematical-boundary review before proof implementation.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the three supporting theorem statements at the exact hashes below. This is not approval of a full formalization of AIM114.
- **Type-checking:** not performed or claimed by this reviewer. Successful type-checking of the frozen definitions and Challenge remains a separate required gate before implementation.

## Reviewed evidence

Repository source commit: `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`.

| File | SHA-256 |
|---|---|
| `research/solutions/114-nodal-surplus-counterexample/statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |
| `research/solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf` | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| `research/solutions/114-nodal-surplus-counterexample/PROOF.md` | `1a621098125651077fddba39f027e5b8948448d8389f5376d02c701809dd2604` |
| `research/lean/114/NUMERICAL_TARGETS.md` | `a248e229221f1e857a46b7aa542cef687a546a63ec2a4a5607a53c087951b889` |
| `research/lean/114/AIM/P114/Definitions.lean` | `0c29c3c5b0cec95e1463ca190792b26a8d42733cdcca5b99796f84bd03a854ff` |
| `research/lean/114/Challenge.lean` | `762965dcaab9eff7d0fca577597a1b900a7acde8899928eceb38d9a0c0c740fe` |

The frozen source statement matches the canonical problem bytes I read. I read the complete source argument and independently audited its probability sections; that separate report is [probability-review.md](../../../solutions/114-nodal-surplus-counterexample/reviews/probability-review.md). I read the mathematical-boundary guide and independent-review protocol. This review preceded proof implementation and did not rely on a proposed proof or another referee's verdict.

## Declaration-by-declaration comparison

### `AIM.P114.module_count_identity`

All variables are real and universally quantified. Strict-negative real indicators agree with the manuscript's edge sign counts and its negative-pivot count. Substituting `a=a_i`, `x=c_i1`, `y=c_i2`, and `z=r*c_i3` makes the common vertex value `(x+y+z)/a` exactly `F_wi` under `F_u=1`; the third edge sign is `z*F_wi`, as required.

Every argument on which `nonzeroSign` is evaluated is nonzero by the explicit hypotheses: `a`, `x`, `y`, `z`, and their three-term sum. Thus extending sign by `+1` at zero causes no discrepancy. No numerical tolerance or omitted degeneracy enters the statement.

An independent algebraic check writes each negative indicator of a nonzero number `q` as `(1-sign(q))/2`. Since `sign(F)=sign(x+y+z)*sign(a)`, summing three such indicators and subtracting `(1-sign(a))/2` gives exactly `1+centeredModule`. This establishes that the proposed identity is substantive and correct as a general real-variable lemma. It does not encode the graph eigenproblem, the equality between nodal surplus and inertia, the Schur complement, or the full global surplus formula. The scope document accurately distinguishes these.

### `AIM.P114.sign_second_moment`

The four equally weighted terms fix the third effective sign positive and run over both signs of each of the first two positive magnitudes. This is precisely the finite sign average used after the phase-sign reduction in the manuscript. The factor `1/4` and output `1/2-triangleIndicator/4` are correct.

Positivity of `x,y,z` excludes zeros in the individual arguments. The two endpoint exclusions eliminate all four possible signed-sum zeros: the all-positive sum is positive; the all-negative-first-two sum vanishes only at `z=x+y`; either mixed sum can vanish only at `z=|x-y|`. Both comparisons in `triangleIndicator` are strict, matching the manuscript event.

An independent enumeration gives one always-contributing square and the three indicators of `x>y+z`, `y>x+z`, and `z>x+y`. Their average equals the stated complement-of-triangle expression away from the excluded endpoints. The hypotheses are satisfiable, for example `x=y=z=1`, where the average is `1/4`. They do not assert the conclusion or disguise a probabilistic claim. The fair-sign distribution, independence of `sign(a)`, zero probability of triangle boundaries, and expectation identification remain unformalized and are explicitly identified as such.

### `AIM.P114.variance_mixture_kurtosis`

The statement quantifies over an arbitrary measurable space, a genuine probability measure, and a real-valued function. It uses actual Bochner integrals rather than abstract moment scalars. The assumptions that `V` and `V^2` are integrable suffice to expand the centered square; probability mass one handles the constant term. If `a=integral V`, the integral of `(V-a)^2` equals `integral(V^2)-a^2`. Its assumed positivity therefore implies `integral(V^2)>a^2`; positive `a` makes division by `a^2` legitimate and yields the advertised strict inequality with the exact factor 3.

The positive-variance assumption is not vacuous and is not the output inequality hidden inside a custom definition: it is the integral of the squared deviation from the actual mean. On a two-point probability space, a variable taking 1 and 2 with equal probabilities satisfies all hypotheses. Using the positive variance as an assumption is appropriate for this **supporting implication**, provided it is never represented as proof that the particular manuscript variable satisfies that assumption.

The theorem does not construct a normal variable, compute its moments, prove the factorization of Gaussian-mixture moments, prove non-Gaussianity, or show convergence from the graph surplus. These exclusions are correctly and prominently stated. The manuscript's bounded nonconstant positive `V=v(R)` satisfies the assumptions informally, but that identification is not part of this Lean statement.

## Original target, attribution, and disposition

The canonical AIM114 target has two distinct universal assertions. The complete informal manuscript disproves the Gaussian one only, while the three Lean statements prove local algebra and a general moment implication. They do not collectively establish even the counterexample half of the original problem. `NUMERICAL_TARGETS.md` preserves the canonical quantifiers and limiting order, inventories the missing graph/spectral/probability links, and explicitly prohibits promotion of the full counterexample based on these lemmas. This is an honest partial boundary.

Sidney Holden's mathematical authorship and the AI-assisted formalization role are distinguished. The definitions are small transparent formulas, with no custom axioms or theorem-shaped assumptions concealed in them. The intentional `sorry` placeholders in Challenge are disclosed as unproved statements, and the requirement that Solution not import Challenge is explicit.

**Requested mathematical changes: none.** Approval applies to the listed bytes only; mathematical boundary changes require another review. At proof completion, independent inspection of the actual proof paths, scope, API/reuse, final hashes, transitive axioms, and authoritative verification logs remains required. This report claims no Lean build, kernel replay, Comparator result, sandbox execution, or complete formal resolution of AIM114.
