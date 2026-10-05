# Independent final proof review 1: actual prescribed lengths

- Date: 2026-10-05.
- Reviewer: root Codex AI agent, independent of implementer `lean_feasibility`.
- Verdict: **APPROVE** all three frozen statements at the hashes below.
- Scope: mathematical/source audit and independent local Lean checks; expanded isolated Linux verification remains separate.

## Exact source and execution

| File | SHA-256 |
| --- | --- |
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `LengthChallenge.lean` | `0ee1d8866b88d3e389209a16d21ff51291fcfce759bbdff15cbc4c18ce774809` |
| `LENGTH_TARGETS.md` | `765439e1e49999c292a0c30a37ee1a1925e8b808770dcde9f30000bd835ee3dd` |
| `AIM/P114/LengthProof.lean` | `025f80e283f7b7b0a54ee74b55b45c234820b9ab0fa7b9ed828954268f650509` |

The boundary files are unchanged from my preproof approval. I read the complete implementation and independently ran `lake build AIM.P114.LengthProof`, `lake env lean AIM/P114/LengthProof.lean`, and a fresh import printing the axioms of all three results. A before/after SHA-256 check confirms that the source stayed fixed during these commands. All exited zero; separate [build](../verification/referee-1-length-build.log), [re-elaboration](../verification/referee-1-length-reelaboration.log), and [axiom](../verification/referee-1-length-axioms.log) logs are retained. All three results use exactly `propext`, `Classical.choice`, and `Quot.sound`, with no additional axiom, placeholder, native trust, or Challenge import.

## Full joint independence

The proof starts with the actual positive real square root of each nth prime. It embeds that same real number into the relative algebraic closure of Q in C, proving integrality using its square equation. No unspecified algebraic root or assumed sign-changing action replaces it. The closure's actual algebraic-closure and Galois instances come from Mathlib in characteristic zero.

Each rational automorphism sends a root to itself or its negative because its square is the fixed rational prime. The constructed ratio of the conjugate root to the root is therefore a multiplicative character: the proof explicitly uses this sign dichotomy to establish the group-composition law. Nonzero roots justify each division.

Character injectivity is proved rather than assumed. Equal characters make the ratio of two roots fixed by every rational automorphism. The infinite-Galois fixed-field theorem then places this ratio in Q. Multiplying by the second prime shows that the product of those roots would be rational, with square the product of two distinct primes. The arithmetic helper proves this impossible: the product is squarefree by prime coprimality, rational squarehood implies natural squarehood, and a squarefree natural square can only be one, contradicting both primes being at least two. Injectivity of nth-prime enumeration supplies distinct primes from distinct indices.

Dedekind independence of the resulting distinct characters is applied over the actual closure field. A finitely supported rational relation among the roots is transformed by every automorphism into a functional relation among the characters, with coefficients equal to the original rational coefficients times their roots. Character independence forces these products to vanish; nonzero roots force every rational coefficient to vanish. Finally, the proof transports the actual real relation into C and then its subtype closure. This establishes joint independence of the entire sequence, not just pairwise irrationality.

## Actual graph assignment

Positivity treats the pendant and core edges separately. The source restriction m>=3 makes the pendant multiplier positive. The index map assigns 3i+j to each actual core edge identifier and 3m to the pendant. Its injectivity proof uses the finite bounds on i and j, covers both pendant/core orders, and recovers both finite coordinates in the core/core case. Parallel edges remain distinct entries.

The independent prime-root sequence is restricted along this actual injection. Multiplication by rational units then scales only the pendant by m^6. The implementation proves equality with `counterexampleMetricLength`, including all scalar casts; it does not assert independence of an unrelated or abstract length family.

The three conclusions exactly discharge positivity and rational independence for the prescribed graph lengths. Summing the edge assignment to the separate core-length formula is a further bookkeeping identity, not one of these three declarations. The metric realization, Kirchhoff spectrum, spectral-to-phase theorem, stable ratio law, and process/random-evaluation limit remain unformalized. No complete counterexample or universal variance conclusion follows from this approval alone.
