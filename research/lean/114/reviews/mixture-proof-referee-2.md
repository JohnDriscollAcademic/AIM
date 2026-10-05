# AIM114 Gaussian-mixture extension: independent proof referee 2

- **Phase:** final proof-source, probability semantics, scope, correctness, and reuse/quality review.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the mixture implementation author.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the three Gaussian-mixture declarations at the exact reviewed hashes.
- **Independent mechanical results:** fresh module build, direct proof re-elaboration, and all three transitive-axiom checks passed locally on macOS.
- **Limits:** this review does not assert authoritative isolated-Linux verification, kernel replay, or a Comparator run for the extension. It does not formalize the graph-specific mixing variable or convergence of spectral surplus to this law.

## Reviewed bytes and independent execution

| File | SHA-256 |
|---|---|
| `AIM/P114/MixtureDefinitions.lean` | `63573393a3e5521a4276e822717f307bbabd4c327540e22895c99a1c0fab7652` |
| `AIM/P114/MixtureProof.lean` | `2a5d65beeeb576efad8eaf9940ebe0b5cd81cd52e402807e004444ca2e9e6bcf` |
| `MixtureChallenge.lean` | `edd2f69de4e8ba1552189d57856ae4bd7f35a4b9c73a53c0d2e1de81c5a3570a` |
| `MIXTURE_TARGETS.md` | `85fd7a64932d5fcd567f4cceb13711da60fcc1ffdde70e118c7ee4e6143ef1f8` |
| `MIXTURE_PROOF.md` | `e6e736fea68fed8a2c23629991e5bb40aa87a84c670913360e18b668ea1229b1` |
| Imported `AIM/P114/Definitions.lean` | `0c29c3c5b0cec95e1463ca190792b26a8d42733cdcca5b99796f84bd03a854ff` |
| Imported `AIM/P114/Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` |

The boundary hashes match my [pre-implementation approval](mixture-statement-referee-2.md), which records the frozen manuscript and canonical-target hashes. The imported scalar kurtosis proof remains identical to the source in my earlier [proof review](proof-referee-2.md). I read the actual final source and its explanatory document before running the independent checks. I made no proof edits and did not rely on the implementer's claimed results.

Working directory: `/Users/sholden/Projects/AIM/research/lean/114`.

| Command | Result | Independent log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.MixtureProof` | Exit 0; successful 3643-job build | [build](../verification/referee-2-mixture-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/MixtureProof.lean` | Exit 0; fresh direct re-elaboration, no diagnostics | [re-elaboration](../verification/referee-2-mixture-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-mixture-axioms.lean` | Exit 0; three transitive-axiom lists | [axioms](../verification/referee-2-mixture-axioms.log) |

The axiom log retains the complete temporary probe source, which imports the proof module and prints the axioms of each public result. All three declarations report exactly

```text
[propext, Classical.choice, Quot.sound]
```

The [hash manifest](../verification/referee-2-mixture-hashes.json) includes all reviewed sources and pinned dependency/toolchain inputs. Every command rechecked those hashes and found them unchanged. The [source audit](../verification/referee-2-mixture-source-audit.log) confirms that all three proof signatures equal their frozen Challenge signatures after whitespace normalization; it is explicitly a source comparison, not Comparator evidence. No Challenge appears in the solution import chain.

## Fourth moment of the actual standard Gaussian

The proof defines `g(t)=exp(t^2/2)` and supplies explicit `HasDerivAt` certificates for four successive derivatives. Exact ring normalization verifies the factors

```text
t,  1+t^2,  3t+t^3,  3+6t^2+t^4.
```

It then identifies `g` with Mathlib's actual standard Gaussian moment-generating function, using `mgf_fun_id_gaussianReal`. The hypothesis of `iteratedDeriv_mgf_zero` is discharged by the existing Gaussian exponential-integrability theorem. Rewriting the fourth iterated derivative using the four proved derivative identities yields 3 at zero. Thus the result is derived from an established Gaussian analytic theorem; the fourth moment is neither postulated nor imported as a custom axiom.

The private Gaussian second-moment result correctly combines the library's variance formula with its mean zero. The private integrable-power result uses finite-exponent `MemLp` for the actual Gaussian measure and proves integrability of every natural power via integrability of the norm power. This separately confirms the genuine finite-moment meaning required by the mixture construction, including the fourth power.

## The actual mixture, integrability, and moments

The input assumptions are those approved in the boundary: a probability space, measurable `V`, and almost-everywhere strict bounds `1/4<V<1/2`. `mixing_memLp_two` obtains real `L^2` membership from those bounds. `mixing_mean_lower` obtains actual integrability and integrates the lower bound to show `a=integral V >= 1/4`; the proof therefore establishes `a>0` before using denominator or square-root identities.

Writing `H=sqrt(V/a)`, the proof shows measurability of `H` and the product map `F(ω,z)=z H(ω)`. On the given full-measure set it proves `0<=V/a<=2` and then the looser sufficient bound `0<=H<=2`. Its use of `Real.sq_sqrt` is guarded by the derived nonnegativity. No pointwise nonnegativity assumption is imposed outside the given almost-everywhere set.

Boundedness yields integrability of every natural power of `H`. `Integrable.mul_prod` combines these integrable powers with the independently proved Gaussian powers, establishing integrability of every natural power of `F` under the product measure. `integrable_map_measure` then transfers that property to the actual pushforward. The advertised first, second, and fourth integrability conclusions are therefore proved, not inferred merely from formal integral expressions. The proof also establishes probability status of the pushforward from measurability of `F` and probability status of the product measure.

Only with this construction in place does the proof factor product integrals. The identity from `integral_prod_mul` applies to the actual product measure, so independence is supplied by construction. No unsupported conditional-independence assumption enters the proof. The square and fourth-power identities for `H` are established almost everywhere and passed through `integral_congr_ae`; they are not rewritten globally where `V` might violate its bounds on a null set.

The resulting factorization gives mean zero from the Gaussian first moment, second moment one from `integral H^2=(integral V)/a=1`, and fourth moment

```math
3\,\frac{\int V^2\,d\mu}{(\int V\,d\mu)^2}.
```

The source bounds also imply integrability of `V^2`, independently of this displayed expression; the proof's `mixing_memLp_two` helper supplies exactly that library fact when needed in the strict inequality. Hence there is no use of the Bochner integral's nonintegrable default value to impersonate a probabilistic moment. Zero mean and second moment one establish the stated normalization of the constructed law.

## Nonconstancy and nonequality of measures

The non-Gaussian theorem uses the actual `L^2` fact for `V`. Its intrinsic nonconstancy hypothesis excludes almost-everywhere equality to any constant. Mathlib's `ae_eq_integral_of_variance_eq_zero` would make `V` almost everywhere equal to its own mean if its variance were zero; combining the negation of that consequence with variance nonnegativity gives strictly positive variance.

The proof translates that variance into the integral of the centered square using the library's `variance_eq_integral`, then applies the previously reviewed exact integral kurtosis theorem with actual integrability witnesses and the proved positive mean. This yields a strict fourth-moment lower bound. The previously proved mixture theorem supplies equality with that fourth-moment expression. If the actual mixture measure equalled `gaussianReal 0 1`, substituting that equality and the independently proved Gaussian fourth moment would contradict the strict bound. The final conclusion is genuine nonequality of probability measures.

The proof does not assume any mixture moment identity, posit the desired law inequality, or rely on a numerical kurtosis experiment. The a.e. nonconstancy-to-positive-variance step, previously an input obligation of the scalar lemma, is now explicitly discharged in Lean for this bounded general mixing variable.

## Reuse, documentation, and scope

The implementation reuses the pinned Gaussian MGF, derivative-to-moment theorem, Gaussian `MemLp`, variance-zero characterization, map integrability, and product integration APIs. The new fourth-moment calculation is short exact differentiation on top of those APIs; the other helpers are private and limited to integrability and normalization. Source comments and `MIXTURE_PROOF.md` accurately explain the proof path. Sidney Holden's mathematical source and the AI formalization role remain distinguished by the approved scope document and package attribution.

This extension establishes an actual standardized Gaussian variance-mixture law with its first, second, and fourth moments and proves its nonequality to the standard Gaussian for bounded nonconstant mixing variables. The remaining application is substantive: it has not defined and constructed the stable pair, identified this `V` with the manuscript's `v(-A/B)`, proved its source-specific bounds/nonconstancy, or established the nodal-surplus convergence to the constructed law. Those are explicitly retained gaps. The independent universal linear-variance target is unchanged.

**Blocking findings: none.** Integration of these exact declarations into the combined target list and authoritative Linux verification remains required. This approval and the successful local checks certify neither that integration nor a full Lean proof of the quantum-graph counterexample.
