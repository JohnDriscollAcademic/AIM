# Independent proof review 1: actual Gaussian variance mixture

- Date: 2026-10-05.
- Reviewer: Codex AI subagent `spectral_review`, independent of the implementer. This is an AI review.
- Verdict: **APPROVE the three proofs at the exact boundary reviewed below.**

## Scope and source fidelity

I read the actual `MixtureDefinitions.lean`, `MixtureChallenge.lean`, `MixtureProof.lean`, and `MIXTURE_PROOF.md`. The definition, challenge, and target-document hashes are unchanged from my independent preproof approval. All three theorem types agree with that approved boundary, including every integrability conclusion in the moment theorem and the almost-everywhere nonconstancy premise in the nonequality theorem.

The source is Sidney Holden's v0.3 manuscript, PDF SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`; the canonical original AIM 114 target remains the one at upstream commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. This extension formalizes the inference from a measurable bounded nonconstant mixing variance to an actual standardized non-Gaussian law. It does not yet identify the manuscript's `v(-A/B)` with such a Lean object or prove the convergence of spectral laws to it. The target and proof descriptions state that limitation accurately.

## Actual proof paths and semantic audit

`normalizedVarianceMixture` is a genuine pushforward of the product of the arbitrary input probability measure and Mathlib's standard Gaussian measure. The mapped random variable is exactly `z * sqrt(V / integral V)`. The Gaussian factor is independent of the mixing coordinate by this product construction; independence and moment identities are not extra input certificates.

1. `standard_gaussian_fourth_moment` supplies four explicit derivative certificates for `exp(t^2/2)`, connects this function to Mathlib's Gaussian moment-generating function, and uses `iteratedDeriv_mgf_zero` to identify the fourth derivative at zero with the actual fourth-power integral. The zero-interior-domain condition is discharged using the Gaussian MGF domain. This is a real Gaussian moment calculation, not an assumed moment specification or a definition of a Gaussian by its moments.
2. `normalized_variance_mixture_moments` derives `integral V >= 1/4`, so the normalization is strictly positive. It proves measurability of the amplitude and product map, bounds the amplitude in `[0,2]` almost everywhere, and obtains integrability of all its natural powers. Gaussian finite-power integrability follows separately from `memLp_id_gaussianReal'`. Product integrability then gives integrability of powers of the mapped variable and transfers it to the pushforward. Thus the advertised moment identities cannot arise from the default value of a nonintegrable Bochner integral. Product-integral factorization, the almost-everywhere square-root identities, and the Gaussian moments prove mean zero, second moment one, and the stated exact fourth moment. Mapping a probability measure by the measurable map supplies the probability conclusion. Zero mean and unit second moment therefore really give unit variance.
3. `normalized_variance_mixture_not_gaussian` derives positive variance of `V` from its bounded `MemLp` property and its failure to be almost everywhere constant. Mathlib's zero-variance theorem would otherwise force almost-everywhere equality to its expectation. The original, previously independently reviewed `variance_mixture_kurtosis` result then makes the constructed law's fourth moment strictly greater than three. Equality with the standard Gaussian contradicts the fourth moment proved in the first declaration.

The hypotheses are nonvacuous: a two-point probability space with equal atom weights and mixing values `1/3` and `2/5` satisfies them. The proof's use of only a non-strict lower bound on the expectation is sufficient because `1/4` itself is positive. The amplitude bound of two is deliberately loose and valid. Almost-everywhere exceptional values cause no square-root or division problem because measurability is global and every algebraic use of positivity is restricted to the established almost-everywhere bounds.

The source imports concrete definitions and the original supporting proof module, not any Challenge. I found no custom axiom, `sorry`, native evaluation, assumed conclusion, or circular law specification. Reuse of the original scalar kurtosis theorem is legitimate and visible. The target document credits Sidney Holden; the source identifies the Mathlib MGF, Gaussian integrability, product-integral, and zero-variance results it uses.

## Independent local verification

I independently ran the following from `research/lean/114` using `/Users/sholden/.elan/bin/lake` and the pinned project:

| Command | Result | Retained log |
| --- | --- | --- |
| `lake build AIM.P114.MixtureProof` | Exit 0; build successful | `verification/referee-1-mixture-build.log` |
| `lake env lean AIM/P114/MixtureProof.lean` | Exit 0; fresh direct re-elaboration successful | `verification/referee-1-mixture-proof-reelaboration.log` |
| `lake env lean /tmp/aim114-review/referee-1-mixture-axioms.lean` | Exit 0; all three declarations inspected | `verification/referee-1-mixture-axioms.log` |

All three advertised theorems have exactly the transitive axioms `propext`, `Classical.choice`, and `Quot.sound`. These are local verification results. I do not claim that the extended package has already passed Linux export, kernel checking, or exact comparator verification; new operational evidence must bind the extended theorem list and immutable sources.

## Reviewed SHA-256 hashes

Also retained in `verification/referee-1-mixture-source-sha256.json`.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/MixtureDefinitions.lean` | `63573393a3e5521a4276e822717f307bbabd4c327540e22895c99a1c0fab7652` |
| `MixtureChallenge.lean` | `edd2f69de4e8ba1552189d57856ae4bd7f35a4b9c73a53c0d2e1de81c5a3570a` |
| `MIXTURE_TARGETS.md` | `85fd7a64932d5fcd567f4cceb13711da60fcc1ffdde70e118c7ee4e6143ef1f8` |
| `AIM/P114/MixtureProof.lean` | `2a5d65beeeb576efad8eaf9940ebe0b5cd81cd52e402807e004444ca2e9e6bcf` |
| `MIXTURE_PROOF.md` | `e6e736fea68fed8a2c23629991e5bb40aa87a84c670913360e18b668ea1229b1` |
| Reused `AIM/P114/Proof.lean` | `b4412ae1ae9f8f7bc26279c565e3e4799b203eb1a3f3d191b95aa4a239b69797` |

## Remaining obligations

The extension proves an actual probability-law result beyond the original scalar moment inequality. It still requires construction, bounds, and nonconstancy of the source-specific mixing variable; a process or other argument giving the pendant-law limit; moment convergence; and the quantum-graph spectral bridge. It is neither a proof of full AIM 114 nor of the source's variance universality assertion. No such broader claim is approved here.
