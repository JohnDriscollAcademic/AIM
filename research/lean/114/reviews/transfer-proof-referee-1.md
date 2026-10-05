# Independent proof review 1: prescribed-length moment transfer

- Date: 2026-10-05.
- Reviewer: Codex AI subagent `spectral_review`, independent of the implementer. This is an AI review.
- Verdict: **APPROVE the five proofs at the exact boundary reviewed below.**

## Scope and fidelity

I read the complete `TransferDefinitions.lean`, `TransferChallenge.lean`, `TransferProof.lean`, and `TRANSFER_TARGETS.md`, and compared the five actual theorem types with my approved preproof boundary. The three boundary files are byte-for-byte unchanged from that approval. Renaming two unused hypothesis binders to `_hB` and `_hk` does not alter their types or remove the hypotheses.

The mathematical source is Sidney Holden's v0.3 manuscript, Section 5, PDF SHA-256 `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`; the preserved original AIM 114 target is upstream commit `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. These results concern the actual prescribed prime-root lengths and actual integrals of the contaminated probability law. They do not identify this law with a quantum-graph spectral distribution.

## Actual proof paths

1. `core_weight_bound` obtains positivity from membership of the indexed integer in the primes, uses monotonicity of the nth-prime sequence and square root to bound all `3m` core lengths by the next prime root, and cross-multiplies only after proving both denominators positive. The cancellation uses the exact pendant multiplier `m^6`. It assumes neither rational independence nor the desired weight bound.
2. `contaminated_law_probability` computes the mass of the whole space from the two probability hypotheses. The two `ENNReal.ofReal` coefficients sum to one under the stated closed-unit-interval hypotheses. Endpoints cause no problem.
3. `contamination_integral_bound` first derives integrability for each input law using the almost-everywhere interval bounds and measurability. It then bounds both expectations in `[0,B]`, rewrites the integral of the sum/scalar measures with the required integrability proofs, and proves the error is `w` times the absolute difference of the two expectations. This is not a proof exploiting the default value of a nonintegrable Bochner integral. The unused separate `B >= 0` hypothesis is harmless: the probability and interval hypotheses already imply it.
4. `surplus_moment_contamination_bound` proves the normalized centered square is at most `m`, then bounds its `k`th power by `m^k`. It applies the preceding integral estimate and the actual prime-root weight bound. The finite-index estimate actually holds for every natural `k`; leaving the reviewed `k=1 or k=2` hypothesis unused in this theorem is a valid strengthening of the internal calculation, not a weakened advertised result.
5. `surplus_moment_contamination_tendsto` uses that exponent restriction to compare the explicit error with `3/m` for all `m>=1`, and applies a norm squeeze with the standard reciprocal-natural limit. Thus it proves convergence of the actual signed difference of integrals, not merely convergence of a formal error bound. The `m=0` values are irrelevant to the eventual estimate.

The hypotheses are nonvacuous (Dirac laws at zero satisfy the required support bounds). No conclusion is assumed under a renamed hypothesis. The proof imports only the concrete definitions, uses Mathlib results through explicit proof terms, contains no Challenge import, custom axiom, `sorry`, or native decision procedure, and does not turn spectral assumptions into definitions of the desired conclusions. Credit to Sidney Holden is retained in the definitions and target document; the ordinary Mathlib facts are referenced in the source by their theorem names.

## Independent local verification

I ran these commands myself from `research/lean/114`, using the pinned project and `/Users/sholden/.elan/bin/lake`:

| Command | Result | Retained log |
| --- | --- | --- |
| `lake build AIM.P114.TransferProof` | Exit 0; build successful | `verification/referee-1-transfer-build.log` |
| `lake env lean AIM/P114/TransferProof.lean` | Exit 0; fresh direct re-elaboration successful | `verification/referee-1-transfer-proof-reelaboration.log` |
| `lake env lean /tmp/aim114-review/referee-1-transfer-axioms.lean` | Exit 0; all five declarations inspected | `verification/referee-1-transfer-axioms.log` |

Every advertised theorem has exactly the transitive axioms `propext`, `Classical.choice`, and `Quot.sound`. Neither `sorryAx` nor any native-evaluation axiom appears. These are local checks, not a claim that the new extension has already passed the separate Linux export/comparator workflow. A combined eleven-declaration boundary and new immutable Linux evidence must be checked separately if the package advertises the extended scope.

## Exact reviewed hashes

Also retained in `verification/referee-1-transfer-source-sha256.json`.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| `TransferChallenge.lean` | `48d4e6a969b304dd89145bf8be6df2697db220b6e8a51ed458c6631047a544d1` |
| `TRANSFER_TARGETS.md` | `6deb2147a2742f8cefbbdec369932b654d6153227d59b6686c4887bc71b69538` |
| `AIM/P114/TransferProof.lean` | `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c` |

## Limitations

This approval closes the explicit length-fraction estimate and conditional moment-contamination calculation. It does not prove joint rational independence of the lengths, graph admissibility, the spectral edge-mixture representation, the spectral support theorem, convergence of the pendant law, or the full counterexample. Those limits agree with the frozen target document and my prior source review.
