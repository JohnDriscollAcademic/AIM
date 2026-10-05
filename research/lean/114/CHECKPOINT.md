# Paused checkpoint — 2026-10-05

Paused immediately at the user's explicit request. All working agents were
interrupted. Do not resume mathematical work, builds, CI, or publication until
the user requests resumption. This is a local work-in-progress checkpoint,
not a completed or newly Linux-verified submission.

## Published state

- AIM PR 33: https://github.com/MColbrook/AIM/pull/33
- Public head at pause: `740591a3d2a0ec4c4937b61ff382dcdf069494ad`.
- Public scope: original three supporting Lean results; the full informal
  counterexample has two independent AI mathematical audits.
- Historical successful isolated Linux run:
  https://github.com/sidneyholden1/AIM/actions/runs/37344385173
  at `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`, covering only those three.
- Companion catalogue PR 34: https://github.com/MColbrook/AIM/pull/34,
  public head `70212479ac5e4b5808fb6a4dfb86d0f03d675339`; 57 tests passed.
- Neither PR was merged. No changes from this continuation have been pushed.
- No expanded Linux workflow was started in this continuation.

## Saved completed proofs and local checks

The original Definitions and Proof files remain unchanged.

1. **Transfer: five new results.** Actual prime-root length fraction, genuine
   convex probability mixture, bounded integral error, and actual second/fourth
   moment contamination error tending to zero. Implementation:
   `AIM/P114/TransferProof.lean`, SHA-256
   `c8788e2afe2c5728840485801dfe59488f2c8388f9ad5e20bb753984ee96056c`.
   Both independent boundary and final proof reviews APPROVE. Author and both
   referee builds, fresh elaboration, and axiom checks passed.
2. **Mixture: three new results.** Actual standard Gaussian fourth moment;
   actual normalized product-space pushforward with integrable moments 0, 1,
   and `3 EV²/(EV)²`; inequality to standard Gaussian from intrinsic bounded
   nonconstant mixing variance. Implementation `AIM/P114/MixtureProof.lean`,
   SHA-256 `2a5d65beeeb576efad8eaf9940ebe0b5cd81cd52e402807e004444ca2e9e6bcf`.
   Both independent boundary and final proof reviews APPROVE. Author and both
   referee builds, fresh elaboration, and axiom checks passed.
3. **Inertia: two new results.** Actual quadratic-form completion of squares
   by an explicit linear equivalence, and its actual Mathlib positive index.
   Implementation `AIM/P114/InertiaProof.lean`, SHA-256
   `d0acd2dfda515f792ca12195be04b1b07d0ca76e75e7cb20b1afd0e09e06345d`.
   Both boundary reviews APPROVE. Author build, fresh elaboration and axioms
   passed. Root's independent final commands also passed, with retained
   `referee-1-inertia-*` logs, but its final written proof report was not yet
   saved. Referee 2's final APPROVE report arrived during checkpointing and is saved
   as `reviews/inertia-proof-referee-2.md`, with its independent logs. Root's
   final written report remains to be completed on resumption.

Every inspected new theorem has exactly `propext`, `Classical.choice`, and
`Quot.sound`. These are local results, not an expanded isolated-Linux certificate.

The combined `Challenge.lean`, `Solution.lean`, `comparator.json`, and
`formalization.yaml` currently contain **11** results: original 3 + Transfer 5
+ Mixture 3. Combined build and axiom print passed. **The two Inertia results
are implemented but not yet integrated into those combined files.** Thus 13
proofs exist, but the current combined project advertises 11. README and
NUMERICAL_TARGETS likewise currently describe 11; bring all these into agreement
before publication.

Metadata validator and project selection passed for the 11-result package.
All 43 metadata/project-selection tests and 12 harness tests passed. The PR 34
catalogue validator passed against this actual checkout with local Lean caches.
The original main catalogue scanner still traverses caches; final validation
with it should use a clean submitted-file snapshot, as in the earlier work.

## Unimplemented actual-variance boundary

The next candidate fixes the mixing variance to the actual three-Cauchy
triangle probability. Its five statements concern value at zero, strict
bounds for nonzero arguments, global continuity, the mixture hypotheses under
any full-support probability law with no atom at zero, and the resulting actual
mixture's inequality to standard Gaussian.

- `AIM/P114/VarianceDefinitions.lean` SHA-256
  `39448627e15c3dc5b6d0a9c825928abe8f79a6b92fed300cf40313bc9b5ef3aa`
- `VarianceChallenge.lean` SHA-256
  `6b77c1f2e4debf3ac27f7264ab36ee8431a59c060e3e98ac99824160a21be0b5`
- `VARIANCE_TARGETS.md` SHA-256
  `a215fb1019cd18812094ad0adac10aef5427e2346af39e9004db38e01cca14fb`

Definition and Challenge typechecks passed; the retained log is
`verification/variance-boundary-typecheck.log`. **No VarianceProof exists.**
Root read the full candidate and found no mathematical defect but had not
saved its approval or independently typechecked it. Referee 2's review was
pending when interrupted. Obtain both actual written approvals at the frozen
hashes before implementing any proof.

Useful exact witnesses identified by the implementer: for nonzero r, the
triangle event contains `((r,r),0)`; a strict complement contains
`((0,0),3/abs(r))`. Full support and atomlessness must be proved from the actual
Cauchy density, not assumed. Continuity needs a separate null-boundary argument
at zero and at nonzero r. The stable ratio law itself remains unconstructed.

## Resumption sequence and provenance

- Finish independent Inertia proof reports; integrate its exact two reviewed
  signatures and proofs into the combined project, metadata and scope docs.
- Resume the actual-variance boundary reviews before implementation. Keep
  that candidate separate from claims about completed proofs.
- Run a fresh isolated Linux verification at a committed expanded proof
  revision once the selected expanded scope is ready. Retain original
  artifacts, immutable source and input hashes, then independently audit them.
  The older run is historical evidence only.
- Update PR 33's description and canonical-page verification links only to
  reflect the actually verified expanded scope. No merging is authorized.
- The full spectral-to-phase theorem, graph admissibility/rational independence,
  stable-vector and random-evaluation limit still remain. The original problem
  statement and the separate universal variance question are unchanged.
- `FORMALIZATION_ROADMAP.md` and `PROBABILITY_ROADMAP.md` retain concrete next
  steps and library evidence. The latter proposes a finite-grid route instead
  of building a complete Skorokhod/Donsker library; it is a proposal, not proof.

Mathematical authorship: Sidney Holden. AI implementation/review attribution
must remain explicit. Original PDF and expanded informal proof are unchanged.
The source package README/REVIEW were updated for the new scope, and their
provenance hashes were refreshed. No files in the NLA checkout were changed.

Worktree: `/Users/sholden/Projects/AIM`, branch
`codex/114-nodal-surplus-counterexample`. Lean is
`/Users/sholden/.elan/bin/lake`; metadata Python is `.venv/bin/python`.
Dependencies are pinned; do not run `lake update`. Git HTTPS operations need
the existing credential-helper workaround because global Git config rewrites
HTTPS to unavailable SSH. On an authorized later push use:

```sh
GIT_CONFIG_GLOBAL=/dev/null git -c credential.helper= -c 'credential.helper=!/Users/sholden/.local/bin/gh auth git-credential' push origin codex/114-nodal-surplus-counterexample
```

Agents at pause: `lean_feasibility` (mixture implementer, actual-variance
candidate), `spectral_review` (transfer/mixture referee, inertia implementer),
`probability_review` (independent referee); root implemented Transfer and
independently reviewed Inertia. Root and probability reviewer are the two
independent Inertia referees; its implementer cannot review its own proof.
