# AIM114 transfer extension: independent proof referee 2

- **Phase:** final proof-source audit, mathematical fidelity, actual integral semantics, degenerate cases, and reuse/quality.
- **Reviewer:** `probability_review`, independent OpenAI Codex AI subagent; not the transfer implementation author.
- **Date:** 2026-10-05.
- **Verdict:** **APPROVE** all five public transfer declarations at the reviewed hashes.
- **Independent mechanical results:** module build, fresh source re-elaboration, and five transitive-axiom checks passed locally on macOS.
- **Limit:** no authoritative isolated-Linux verification or Comparator execution of this extension was inspected or performed by this reviewer. This report does not certify the unformalized spectral-law identification or the full counterexample.

## Exact evidence

| File | SHA-256 |
|---|---|
| `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| `AIM/P114/TransferProof.lean` | `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c` |
| `TransferChallenge.lean` | `48d4e6a969b304dd89145bf8be6df2697db220b6e8a51ed458c6631047a544d1` |
| `TRANSFER_TARGETS.md` | `6deb2147a2742f8cefbbdec369932b654d6153227d59b6686c4887bc71b69538` |

Definitions, Challenge, and target-document hashes match my [approved pre-proof boundary](transfer-statement-referee-2.md). That report records the unchanged original manuscript and source-problem hashes and the complete theorem-to-source comparison. I read the final proof file before executing it and made no proof edits.

The [independent hash manifest](../verification/referee-2-transfer-hashes.json) also records the Lakefile, pinned dependency manifest, and toolchain inputs. The runner rehashed all inputs after each command and found no changes. The [source audit](../verification/referee-2-transfer-source-audit.log) compares all five final signatures with Challenge, allowing whitespace and the harmless bound-variable renamings `hB -> _hB` and `hk -> _hk`. They agree. This source comparison is not being represented as an actual Comparator run.

## Independently reproduced commands

Working directory: `/Users/sholden/Projects/AIM/research/lean/114`.

| Command | Result | Log |
|---|---|---|
| `/Users/sholden/.elan/bin/lake build AIM.P114.TransferProof` | Exit 0; successful 3230-job build | [build](../verification/referee-2-transfer-build.log) |
| `/Users/sholden/.elan/bin/lake env lean AIM/P114/TransferProof.lean` | Exit 0; fresh re-elaboration without diagnostics | [re-elaboration](../verification/referee-2-transfer-reelaboration.log) |
| `/Users/sholden/.elan/bin/lake env lean /tmp/aim114-review/referee-2-transfer-axioms.lean` | Exit 0; all five axiom lists printed | [axioms](../verification/referee-2-transfer-axioms.log) |

The temporary axiom probe's complete source is preserved in its log. It imports only `AIM.P114.TransferProof` and runs `#print axioms` for the five public declarations. Every one reports exactly

```text
[propext, Classical.choice, Quot.sound]
```

No `sorryAx` or custom axiom occurs. The proof source imports only `TransferDefinitions`; neither imports a Challenge. These are fresh independent results, not copies of the implementer's reports.

## Proof-path audit

### Actual prime-root weight

The private positivity lemma uses the infinitude of the primes and membership of their `Nat.nth` enumeration to prove each prime-root length is strictly positive. The finite-sum comparison uses the monotonicity of that same enumeration and monotonicity of square root. It therefore bounds the actual core sum by `3m` times the actual next-prime root; it does not assume an abstract length inequality as a theorem hypothesis.

For `m>=1`, the pendant length and total denominator are positive. The main weight inequality multiplies only by positive denominators. After cancellation-free cross multiplication, its sole estimate is the core-sum bound multiplied by `m^5`; exact algebra identifies the resulting `3m^6` root term with three times the pendant length. This proves the source's exact fraction bound without an unjustified division or approximation of prime sizes.

### Probability status and expectation error

The probability proof computes total mass of the actual sum of measures. The assumptions `0<=w<=1` justify combining the two `ENNReal.ofReal` weights without truncating negative values. Their sum is one, including the endpoints `w=0,1`.

The integral-bound proof first establishes integrability of `f` separately under each input law from its almost-everywhere bounds. It does this with `Integrable.mono'`, measurable `f`, and an integrable constant dominating the norm, using nonnegativity to replace the norm by `f`. It then places each genuine expectation in `[0,B]` using integral monotonicity and probability mass one. Consequently their difference has absolute value at most `B`.

Only after those integrability checks does the proof invoke `integral_add_measure` and `integral_smul_measure`. The scalar weights are finite; their `toReal` values are reduced using the nonnegative-weight hypotheses. Exact algebra turns the contaminated-law difference into `w` times the difference of the two expectations, and the nonnegative weight gives the target `w*B` estimate. The factor one is correct for a nonnegative observable in an interval of width `B`; no factor two was lost.

The parameter `_hB` remains in the final theorem type. The proof does not need it separately because the input bounds and the existence of either probability law already force compatibility with nonnegative `B`. This harmless redundancy does not weaken the approved proposition or hide an inconsistent assumption. The permitted `B=0` and weight endpoints are covered without special nonzero assumptions.

### Even moments on the surplus interval

The private pointwise estimate derives `|s-(2m-1)/2|<=m` from the source interval `0<=s<=2m-1`. Positivity of `sqrt(m)` is established before multiplying a division inequality. The square-root-square identity then shows the squared normalized centered value is at most `m`. Raising the two nonnegative sides to the natural power `k` proves the bound by `m^k` and proves nonnegativity of the even moment.

This pointwise argument is valid for every natural `k`. Thus `_hk` is not needed for the finite bound, while it is retained in the public signature to preserve the source's advertised second/fourth-moment scope. The limiting theorem does use `hk`. No endpoint `s=0` or `s=2m-1` is removed, and the proof handles `m=1`. It does not assert graph admissibility at `m=1,2`.

The public finite estimate proves `coreWeight m<=1` from the already established exact prime-root bound, supplies measurability of the actual polynomial/division integrand, transports the pointwise bounds under both laws, and applies the genuine contamination-integral theorem. Its final multiplication uses nonnegative `m^k`. It establishes the actual centered/scaled integral difference, not merely a bound between abstract moment variables.

### Vanishing moment error

The final proof works eventually on `m>=1`. The alternatives `k=1` or `k=2` imply `k+1<=5`, and monotonicity of powers for `m>=1` bounds the displayed error by `3/m`. Both denominator multiplications are guarded by positivity. The standard limit `3/m -> 0` and `squeeze_zero_norm'` then prove the signed moment difference tends to zero.

This last estimate is weaker than the original polynomial rate but is sufficient for precisely the advertised limit. It does not claim a stronger rate. Arbitrary measures at index zero do not affect the limit; no hidden support assertion at that index is used. The theorem neither assumes nor concludes convergence of the uncontaminated moments themselves.

## Reuse, fidelity, and remaining limits

The implementation uses the pinned Mathlib prime enumeration, real square-root order facts, finite sums, standard Bochner-integrability/linearity results, scalar-measure operations, and a standard reciprocal limit. Private helpers are confined to the package and express the reusable estimates clearly. There is no interval arithmetic, finite experimental sample, custom axiom, unsafe proof escape, or unproved spectral import. The two redundant source-facing hypotheses are transparently named and preserved in the signatures.

The frozen scope document continues to describe exactly what was proved: the prescribed prime-root weight and the contamination step for arbitrary laws with the source surplus support. Applying it to the actual quantum graph still requires the published edge-mixture representation and surplus-support theorem, neither of which is established here. Rational independence of prime-root lengths, the graph construction, the pendant law's probabilistic limit, and full nodal-surplus convergence remain outside this extension.

**Blocking findings: none.** Final integration into the combined Solution/Challenge/Comparator configuration and the repository's authoritative Linux verification remain distinct gates. No full AIM114 “Lean verified” claim follows from this transfer module, and the separate universal linear-variance question remains open.
