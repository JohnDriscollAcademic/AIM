# AIM 114: maintainer audit of the supporting Lean statements

Date: 2026-10-05. Reviewer: the coordinating OpenAI Codex AI agent processing PR 33. This is a source and statement audit, separate from the fresh spectral, probability, and formalization referees. It is not human peer review or an authoritative local Windows Lean verification.

## Scope and verdict

Reviewed PR head `61916d1e9959dc7ed282edb124b51e8118735844` against main `8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. I read the complete combined `Challenge.lean`, `Solution.lean`, comparator and manifest scope, and all actual definitions and proofs in `AIM/P114/`: the initial algebra, transfer, mixture, inertia, variance, graph, length and graph-length-bridge blocks. The accompanying informal argument was read separately; its success is not assumed by any of the supporting results.

**No blocking semantic mismatch found in the advertised 31-result supporting scope.** The actual propositions prove the concrete objects described by the package, with genuine hypotheses and with the remaining spectral and probabilistic links disclosed. This audit alone neither establishes kernel acceptance nor formalizes the complete counterexample. The separately inspected isolated Linux evidence supplies the mechanical result at its pinned input revision.

## Checks of the actual mathematical objects

- **Graph:** `Fin m` module vertices and three hub/pendant vertices, with `Option (Fin m × Fin 3)` edge IDs, retain both parallel edges. Endpoints are symmetric and non-looping; connectivity, cardinalities, incident-edge degrees and the no-degree-two condition are proved for the stated range. The cycle-rank result is explicitly the integer Euler expression; it does not silently claim a newly formalized homology theorem.
- **Lengths:** the sequence is the square roots of successive primes, with the actual pendant multiplied by the nonzero rational integer power `m^6`. The joint rational-independence proof constructs distinct characters of the relative algebraic closure, uses prime squarefreeness to distinguish them, and invokes character linear independence. It does not postulate the independence of the lengths. Positivity, the injective core index and scaled-pendant transport are proved.
- **Initial algebra:** nonzero sign hypotheses permit multiplication and division of signs. The local count identity follows by sign algebra, and the second moment averages the actual four effective sign cases with the boundary exclusions stated. The integral kurtosis inequality expands the variance under explicit integrability and strict variance hypotheses.
- **Inertia:** the core quadratic form includes the actual module pivots and off-diagonal coupling. An explicit invertible shear completes the square; Mathlib's quadratic-form equivalence and signature results give the positive-index count, including the zero-residual-pivot case. The result is a finite-form assertion, not a claim about the metric graph's spectral operator.
- **Variance:** the function is the actual triangle probability under the product of three standard Cauchy measures. Atomlessness and positive density give boundary nullity and positive probability of open triangle and complement witnesses. Dominated convergence proves continuity. The full-support/no-atom-at-zero hypotheses on an input ratio law yield boundedness and nonconstancy of this concrete function; the ratio law is not assumed already constructed from the graph.
- **Mixture:** the law is a concrete pushforward of the product of the mixing measure and the standard Gaussian. Gaussian moments are derived using the library's MGF and integrability results. Product integration proves the normalized law's moments, and strictly positive mixing variance forces its fourth moment above the standard Gaussian's. Neither a moment formula nor the final non-Gaussian conclusion is smuggled in as a hypothesis.
- **Transfer and bridge:** finite sums over the actual edge IDs agree with the explicit core and total prime-root lengths. Prime monotonicity and positive denominators prove the actual core-fraction bound. Convex probability mixtures, bounded integral error and the centered surplus support bound give vanishing second- and fourth-moment contamination under their explicit measure/support hypotheses. Those hypotheses still need identification with the graph's spectral law in a full formalization.

## Boundary and dependency checks

`Solution.lean` imports the proof modules, rather than the deliberate placeholders in the challenge files. All 31 advertised declarations occur in the comparator; its definition-replacement list is empty. Lean 4.33.1 and the immutable Mathlib, LeanCert, checker and metadata pins match the repository setup. Source-level inspection found no extra axiom or proof shortcut in the solution closure; the separate formal audit checks transitive axiom output and actual isolated artifacts.

The existing two-referee records for each statement and final proof block are historical submission evidence. The new formal referee independently checks their pinned scope and byte identity; they are not treated as a substitute for reading the current definitions and proofs.

## Acceptance consequence

Accept these results as **supporting partial formalization**. The metric-graph operator and spectral-to-phase law, the stable response/ratio construction, and the process convergence with endogenous evaluation are still outside the Lean certificate. AIM 114 can be classified Partial from the independently audited informal counterexample to the Gaussian assertion. The separate universal linear-variance assertion remains unresolved by this construction, and the full problem must not receive a Lean-verified label.
