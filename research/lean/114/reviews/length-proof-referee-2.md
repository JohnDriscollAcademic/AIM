# AIM114 prescribed-length extension: independent proof referee 2

- **Phase:** final source, arithmetic fidelity, correctness, reuse, and independent mechanical reproduction.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the length boundary author or implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** all three declarations at the hashes below.
- **Independent results:** module build, fresh direct re-elaboration, and all three transitive-axiom checks passed locally on macOS.
- **Limits:** this is not authoritative isolated-Linux verification, kernel replay, or a Comparator run. These results establish the prescribed lengths' positivity and joint rational independence, not the spectral counterexample.

## Exact evidence and local reproduction

| File | SHA-256 |
|---|---|
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `AIM/P114/LengthProof.lean` | `025f80e283f7b7b0a54ee74b55b45c234820b9ab0fa7b9ed828954268f650509` |
| `LengthChallenge.lean` | `0ee1d8866b88d3e389209a16d21ff51291fcfce759bbdff15cbc4c18ce774809` |
| `LENGTH_TARGETS.md` | `765439e1e49999c292a0c30a37ee1a1925e8b808770dcde9f30000bd835ee3dd` |
| `LENGTH_PROOF.md` | `1632c7db66217c4834fd42943bd8fdc4e4eb20946082f5d79026ac49e49e3200` |
| Imported `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| Imported `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |

The three boundary hashes agree with my [independent pre-proof approval](length-statement-referee-2.md), which records the submitted manuscript and frozen canonical statement hashes and the direct boundary check. I read the final proof and explanation, checked the relevant pinned Mathlib statements, and made no proof edits. The following results are from my own executions, not copied implementer logs.

From `/Users/sholden/Projects/AIM/research/lean/114`, I ran:

| Command | Result | Independent log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.LengthProof` | Exit 0; successful 3431-job build | [build](../verification/referee-2-length-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/LengthProof.lean` | Exit 0; fresh direct re-elaboration with no diagnostics | [re-elaboration](../verification/referee-2-length-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-length-axioms.lean` | Exit 0; all three axiom lists printed | [axioms](../verification/referee-2-length-axioms.log) |

The complete temporary axiom probe is retained in its log. Each of `prime_root_lengths_linearIndependent`, `counterexample_metric_lengths_positive`, and `counterexample_metric_lengths_linearIndependent` depends on exactly `[propext, Classical.choice, Quot.sound]`. There is no `sorryAx` or custom axiom.

The [hash manifest](../verification/referee-2-length-hashes.json) includes the reviewed files, toolchain, and dependency manifest. The runner confirmed all those hashes unchanged after every command. The [source-signature comparison](../verification/referee-2-length-source-audit.log) found all three theorem signatures identical to frozen Challenge after whitespace normalization. This comparison does not substitute for the authoritative Comparator. The proof imports the actual definitions and pinned Mathlib modules, with no Challenge import.

## Actual roots inside the relative algebraic closure

The construction first proves positivity of every actual `primeRootLength j` from primality of the indexed prime and positivity of the real square root. Its square is proved equal to the indexed prime by `Real.sq_sqrt`; this is an equality about the actual real function in the approved definitions.

`radical j` is the subtype element whose complex value is exactly that real root embedded into the complex numbers. Its membership in `algebraicClosure ℚ ℂ` follows from its square equation and `IsIntegral.of_pow`, with the positive exponent checked. Thus no arbitrary conjugate or unrelated abstract square root is substituted. The proof of `radical_sq` explicitly passes through subtype-value injectivity, and `radical_ne_zero` descends an alleged zero back to the positive real root.

The relative algebraic closure is an actual field with the standard Mathlib algebra structure. The supplied `IsAlgClosure` instance is the library theorem for this field; its Galois structure follows from normality and separability in characteristic zero. This is a proved instance, not a new axiom. It supplies the hypothesis required by the infinite Galois fixed-field theorem without a false finite-dimensionality assumption.

## Constructed characters and arithmetic distinctness

Every rational automorphism preserves the square equation, so the image of a root is either the root or its negative. `radicalCharacter j` is then explicitly constructed as the monoid homomorphism `σ ↦ σ(root)/root`. Its identity law uses the root's nonzero value. Multiplicativity under composition is proved by splitting the two possible signs of the second automorphism's image; the first automorphism preserves negation. It does not assume that arbitrary algebraic conjugate ratios are characters or posit a family of independently chosen sign flips.

`distinct_primes_not_rat_square` correctly transfers rational squarehood of a natural number to natural squarehood using `Rat.isSquare_natCast_iff`. Distinct primes are coprime, so their product is squarefree. If that product equals a natural square `k*k`, squarefreeness forces `k` to be a unit, hence one; primality of both factors then contradicts the product equation. The proof includes both primality hypotheses and the distinctness condition rather than applying squarefreeness to a prime square.

For distinct prime indices, an alleged rational ratio of their roots would make their product rational: multiply the ratio by the second prime. Squaring gives a rational square equal to the product of the two primes. Cast injectivity returns the square identity to the rationals before invoking the arithmetic lemma. Injectivity of the actual nth-prime function supplies distinct primes from distinct indices.

Equality of two constructed characters means every rational automorphism fixes the root ratio. The proof establishes this with explicit division identities and nonzero denominators, including nonzeroness of automorphism images. `InfiniteGalois.mem_range_algebraMap_iff_fixed` then produces an actual rational preimage of the ratio. The previous nonsquare argument excludes it. This proves injectivity of the character family, with no assumed automorphism separation property.

## Full joint independence

The main internal argument uses the actual Mathlib theorem `linearIndependent_monoidHom` over the algebraic closure, restricted along the proved injective character family. That theorem is full Dedekind independence of distinct multiplicative characters into an integral domain.

Given an arbitrary finite rational relation among the roots, the implementation applies every automorphism to the relation. Rational coefficients remain fixed. It constructs a function-valued relation among the characters with coefficients equal to the original rational coefficients multiplied by their roots. The finite-sum conversion and division cancellation are justified using the nonzero root lemma. Character independence forces each such coefficient to vanish; nonzero roots and injective rational casts force the original coefficients to vanish.

This is a proof of joint independence for every finite relation. Pairwise irrationality alone would not suffice, but that invalid inference is not used here: the established character-independence theorem is the additional ingredient. The public real theorem transports an arbitrary real finite relation into the relative closure through `Complex.ofReal` and subtype-value injectivity, invokes the internal result, and obtains the same rational coefficient equalities. All roots remain the prescribed real roots throughout.

## Actual edge indices, rescaling, and positive lengths

The exact graph edge type includes the pendant identifier `none` and each core identifier `some(i,j)`. Its private index map sends these to `3m` and `3i+j`, respectively. The injection proof handles both pendant/core directions using `i<m` and `j<3`; no core index reaches `3m`. For two core identifiers, the same bounds imply uniqueness of quotient and remainder modulo three, and `Fin.ext` recovers equality of the actual edge identifiers. Parallel edges therefore keep different prime indices.

The positive-length theorem handles every edge. Core positivity is the actual prime-root positivity lemma. Pendant positivity uses `m>=3` to prove positivity of the real multiplier `m^6`, then multiplies it by the positive root at index `3m`. The range excludes `m=0`, where the prescribed pendant would be zero.

The graph-family independence theorem restricts the already proved entire prime-root sequence along the actual injective edge-index map. It constructs rational units with pendant weight `(m:ℚ)^6` and every core weight one. The source range gives the pendant weight's nonzeroness. `LinearIndependent.units_smul` preserves independence, and the final per-edge equality explicitly simplifies rational scalar action into the actual real multiplier in `pendantLength`. It does not silently discard the factor `m^6` or replace the prescribed lengths with another independent family.

## Quality, attribution, and remaining scope

The proof is uniform in the graph size and all prime indices. Its helper declarations are private, address genuine intermediate obligations, and reuse the standard arithmetic, field-theoretic, and linear-independence APIs. There is no native-computation shortcut, proof placeholder, artificial independence hypothesis, or definition that encodes the desired conclusion as an assumption. `LENGTH_PROOF.md` accurately describes the implemented route and its limits; the approved target document preserves Sidney Holden's source authorship.

Together with the existing graph block, these declarations supply the actual graph with positive, jointly rationally independent prescribed lengths in the source range. They do not define a metric realization or Kirchhoff Laplacian, establish its spectral frequencies or genericity, identify the spectral surplus distribution with the module model, construct the stable response law, or prove the empirical-process and random-evaluation limit. Those remain separate obligations. The independent universal linear-variance assertion also remains open.

**Blocking findings: none.** Combined-target integration and authoritative Linux verification remain separate gates. This report approves the three exact supporting results and does not certify an end-to-end Lean counterexample to AIM114.
