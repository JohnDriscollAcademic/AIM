# AIM114 prescribed-length extension: independent statement referee 2

- **Phase:** pre-implementation mathematical-boundary review and independent type-checking.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the length boundary author or implementer.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** the three proposed declarations at the exact hashes below.
- **Independent mechanical result:** Definitions build and Challenge type-check exited zero; the three deliberate placeholders establish no theorem.

## Reviewed bytes and checks

| File | SHA-256 |
|---|---|
| `AIM/P114/LengthDefinitions.lean` | `0926ae9ca8ae094629c374defd9829436fddf313c63698d227ffd5eb9af70c20` |
| `LengthChallenge.lean` | `0ee1d8866b88d3e389209a16d21ff51291fcfce759bbdff15cbc4c18ce774809` |
| `LENGTH_TARGETS.md` | `765439e1e49999c292a0c30a37ee1a1925e8b808770dcde9f30000bd835ee3dd` |
| Imported `AIM/P114/GraphDefinitions.lean` | `07bc41002c2ee24e98c3686748709fb576f9dd93922ebbd9b29c5297f93a71ca` |
| Imported `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| Submitted v0.3 PDF | `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6` |
| Frozen source problem `statement.md` | `ba20eb2a450b42a26626be50124d93e2b82ca28f81eca942fbe13ccba4ca718f` |

I read all candidate files and compared them with the source's exact equation (1), the following rational-independence argument, and the previously reviewed actual graph and prime-root definitions. I searched the pinned library for the character-independence, fixed-field, nonzero rescaling, irrationality, and squarehood APIs proposed for reuse. No proof implementation was provided or used as evidence, and I made no proof changes.

From `/Users/sholden/Projects/AIM/research/lean/114`, I independently executed

```text
/Users/sholden/.elan/bin/lake build AIM.P114.LengthDefinitions
/Users/sholden/.elan/bin/lake env lean LengthChallenge.lean
```

The build completed successfully with 3252 jobs. Challenge exited zero with exactly three intentional `sorry` warnings. The [independent log](../verification/referee-2-length-boundary-typecheck.log) records both commands, exact source hashes, outputs, exit codes, and confirmation that all five reviewed source/boundary inputs remained unchanged. This is a well-formedness check, not mathematical proof or authoritative Linux verification.

## Exact edge assignment

The function is defined on the actual multigraph edge type, retaining separate identifiers for the parallel edges. A core identifier `some(i,j)` receives `primeRootLength (3*i.val+j.val)`, and the pendant identifier `none` receives the previously defined `pendantLength m`. Since prime indexing in the imported definition starts at zero, this assigns the source's first `3m` prime roots module by module and reserves prime index `3m` for the pendant. Its multiplier is the exact real expression `m^6`.

For a core label, `0<=i<m` and `0<=j<3`, so `3i+j<3m`. The label map is injective by quotient/remainder modulo three. Thus the core uses distinct prime indices and none equals the pendant's index. This is an actual edge-to-length map, not a free family assumed to correspond to the graph or a renumbered family with an omitted parallel edge.

## Three target statements

**`prime_root_lengths_linearIndependent`.** The statement uses Mathlib's actual `LinearIndependent ℚ` on the natural-number-indexed real sequence of prime square roots. This means every finitely supported rational relation has zero coefficients. It is full joint independence of all finite subfamilies, not merely irrationality of each root, pairwise irrational ratios, or independence of finitely many sampled indices. The proposition is mathematically true and is a useful valid strengthening of the finite source claim. Its body will need an actual proof of that strong conclusion; no multiquadratic automorphism or character-independence assumption appears in the signature.

**`counterexample_metric_lengths_positive`.** Every actual source edge is included. Each indexed prime is positive, hence its real square root is positive. For `m>=3`, the real multiplier `m^6` is also positive, so the pendant is positive. The source range is correctly retained; the theorem does not accidentally include `m=0`, when the pendant would have length zero.

**`counterexample_metric_lengths_linearIndependent`.** The statement is joint rational independence of the entire actual finite edge family, including the exact pendant scaling. Restriction of the independent prime-root sequence to the proved injective edge-index map gives the unscaled family. Rescaling only the pendant by the nonzero rational `m^6`, and all other entries by one, preserves rational linear independence. The theorem must prove that the rational scalar's action matches the actual real multiplier in the definition; it cannot replace the pendant by an unscaled root. The explicit `m>=3` condition ensures that scalar is nonzero and matches the source graph range.

The source's statement that rationally independent lengths define the spectral-frequency surplus law requires exactly this joint independence. The proposed declaration supplies the appropriate length property, without asserting the still-unformalized spectral implication.

## Assessment of the proposed arithmetic route

The proposed character proof is mathematically coherent. Placing each actual prime root into the relative algebraic closure by its polynomial equation keeps the chosen roots tied to their real values. An automorphism sends such a root to its positive or negative, so the ratio character takes values in `{1,-1}`. These values are rational and fixed by automorphisms, making the ratio multiplicative under composition. This multiplicativity is a proof obligation, not automatic for ratios of arbitrary algebraic elements.

If two prime-root characters were equal, their root ratio would be fixed by every rational automorphism and hence rational by the Galois fixed-field theorem. Multiplying that ratio by the second prime makes the product of the two roots rational, whose square is the product of two distinct primes. Squarefreeness excludes such a rational square. The proof must establish distinct prime indices, prime coprimality, and the rational-to-natural squarehood transfer rather than assuming distinct characters.

Applying every automorphism to an actual finite rational relation then produces a relation between distinct characters with coefficients equal to the original rational coefficients times the roots. Dedekind's character-independence theorem kills those coefficients, and nonzero roots kill the original coefficients. This argument proves joint independence despite relying only on pairwise character distinctness, because the established character theorem supplies the full finite-relation conclusion. It does not make the invalid inference that pairwise irrationality alone implies joint linear independence.

The relevant APIs named in the scope document are present in the pinned library: `InfiniteGalois.mem_range_algebraMap_iff_fixed`, `linearIndependent_monoidHom`, `LinearIndependent.units_smul`, and rational/natural squarehood equivalence. Their existence does not discharge the application hypotheses or transport through the real/complex/algebraic-closure embeddings; those remain substantial implementation obligations. The new boundary makes no unsupported claim that this proof has already been constructed.

## Scope and disposition

The three statements have no hidden assumptions asserting independence, prescribed sign automorphisms, or the desired spectral law. Their source-range hypotheses are satisfiable, and the exact explicit definitions prevent replacing the lengths with an unrelated independent family. Mathematical authorship and the frozen source revision are correctly identified in the scope document.

This extension would complete the positivity and joint rational-independence conditions for lengths attached to the actual combinatorial graph. It would not define the metric realization or Kirchhoff Laplacian, enumerate eigenvalues, prove generic-index spectral frequencies, identify the spectral measure with the module model, construct the stable response law, or prove the empirical-process and random-evaluation limit. Those dependencies remain explicit, and the independent universal linear-variance question is untouched.

**Requested mathematical changes: none.** Approval is specific to the listed bytes. Implementation, independent final proof and axiom review, combined-target integration, and the authoritative Linux verification workflow remain later gates. This report does not prove any of the three declarations or certify the complete AIM114 counterexample.
