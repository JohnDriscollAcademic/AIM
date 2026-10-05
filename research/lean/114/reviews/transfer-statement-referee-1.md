# Independent statement review 1: prescribed-length moment transfer

- Date: 2026-10-05.
- Phase: preproof review of the new definitions, five actual Challenge signatures, and target document.
- Reviewer: Codex AI subagent `spectral_review`, separate from the implementer; this is an AI review.
- Verdict: **APPROVE this mathematical boundary**, subject to successful type-checking and the required second independent approval before implementation.

## Source and scope

I compared the boundary with Section 5 of Sidney Holden's complete v0.3 manuscript, whose unchanged PDF SHA-256 is `74185c70e83d9c6448d6a97e74411bfe39e5f500e217bc07df605055bbb24aa6`, and with the original AIM 114 statement at upstream revision `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. Those full sources were read during my preceding mathematical and statement audits. I read the actual current `TransferDefinitions.lean`, `TransferChallenge.lean`, and `TRANSFER_TARGETS.md` together; approval is tied to the hashes recorded below, including the explicit natural-number binder in the final theorem.

This extension concerns the actual prescribed lengths and measure-integral moment errors, not merely free scalar inequalities. It leaves the quantum-graph spectral mixture theorem and support theorem outside Lean. Its objects and conclusions do not silently assume or encode the whole counterexample.

## Definition fidelity

`primeRootLength j` uses `Nat.nth Nat.Prime j`; because this is zero-based, core indices `0,...,3m-1` and pendant index `3m` agree exactly with source primes `p_1,...,p_(3m+1)`. The multiplier `m^6`, sum of `3m` core lengths, and core-over-total fraction are correct. The extension defines the fraction at zero by real division but only advertises its quantitative bound for `m>=1`.

`contaminatedLaw w μ ν` is the actual measure `ofReal(1-w) • μ + ofReal(w) • ν`. Its theorem hypotheses restrict the weights to the closed unit interval, so truncation inside `ENNReal.ofReal` cannot alter the intended formula. Here `μ` is the uncontaminated law and `ν` is the residual law, matching the manuscript's pendant/residual order.

`surplusEvenMoment m k s` is exactly `((s-(2m-1)/2)/sqrt(m))^(2k)` with real centering before division. `k=1,2` gives the required second and fourth powers. For even integer powers this is the same observable as the manuscript's absolute-value power. There is no off-by-one surplus center, wrong scaling, or natural-subtraction truncation.

## Signature audit

1. **`core_weight_bound`.** It quantifies over all natural `m>=1` and proves the source bound `0<=omega_m<=3/(m^5+3)` for the concrete prime-root sums. This correctly generalizes the purely algebraic length calculation beyond the graph's admissible `m>=3` without claiming a graph theorem for `m=1,2`. Ordered positive prime roots suffice; the result does not assume or claim their joint rational independence.

2. **`contaminated_law_probability`.** Both inputs are actual probability measures, and the output is an `IsProbabilityMeasure` instance for their weighted sum. The endpoints `w=0` and `w=1` are included. No extra nonempty-space assumption is required because a probability measure already excludes an empty sample space.

3. **`contamination_integral_bound`.** The measurable real function lies in `[0,B]` almost everywhere under each input probability measure, with `B>=0`. These hypotheses imply the needed integrability. They also place both expectations in `[0,B]`, yielding the sharper difference bound `w*B`, not a generally invalid bound for functions only satisfying `|f|<=B`. The claimed absolute integral error is therefore correct. `B=0` and either weight endpoint are valid nonproblematic cases.

4. **`surplus_moment_contamination_bound`.** The two measures are supported almost everywhere on the correct real interval `[0,2m-1]`, which is nonempty for `m>=1`. For the two advertised even moments, the centered normalized absolute value is at most `(2m-1)/(2 sqrt m)`, whose square is at most `m`. Raising to `k` gives the relaxed upper bound `m^k` used in the conclusion. Combining that bound with the first theorem yields exactly the displayed `3*m^k/(m^5+3)` error. No symmetry, exact mean, or spectral interpretation is needed for this bound, so their absence is a valid generalization.

5. **`surplus_moment_contamination_tendsto`.** The quantified inputs are sequences of actual probability measures. Their support bounds apply to every positive integer index; the zero index is immaterial to `atTop`. For `k=1,2`, the preceding error bound tends to zero, with decay of order `m^(k-5)`, so the signed difference of the integrals tends to zero by an absolute-value squeeze. The statement correctly does not assume or conclude convergence of the uncontaminated law or of either individual moment sequence.

These are nonvacuous hypotheses: for example, Dirac laws at zero satisfy the support assumptions for every `m>=1`. Their application to the graph laws is conditional on the separately documented spectral mixture and support facts. No hidden custom definition turns those missing facts into tautologies.

## Remaining gates and coverage

I did not execute a type-check for this report and do not certify a type-check from an implementer's claim. The Challenge placeholders are deliberate and must remain excluded from Solution. Both approvals and actual successful type-checking are required before implementing the five proofs. The combined Comparator boundary must include these exact five signatures if the final package advertises them; changing their mathematical assumptions or definitions reopens review.

This approval does not establish positive/rationally independent length admissibility in full, a quantum graph, spectral frequencies, the edge measure decomposition, weak convergence, the pendant moments, or non-Gaussianity. Those limitations are explicit and accurate in `TRANSFER_TARGETS.md`. The concrete length bound and actual integral transfer are nevertheless substantive additional parts of the submitted proof.

## Reviewed SHA-256 hashes

The exact hashes are recorded in the following audit entry after reading the files; approval binds those bytes.

| File | SHA-256 |
| --- | --- |
| `AIM/P114/TransferDefinitions.lean` | `e68aad72899cdb0827742bf90fd899c20682c460693faeaeec09c012a8426c08` |
| `TransferChallenge.lean` | `48d4e6a969b304dd89145bf8be6df2697db220b6e8a51ed458c6631047a544d1` |
| `TRANSFER_TARGETS.md` | `6deb2147a2742f8cefbbdec369932b654d6153227d59b6686c4887bc71b69538` |
