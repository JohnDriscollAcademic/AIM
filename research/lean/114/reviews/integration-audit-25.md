# Combined 25-result integration audit

- Date: 2026-10-05.
- Auditor: Codex AI agent `spectral_review`.
- Verdict: **APPROVE the local integration and scope at the hashes below; proceed to fresh isolated Linux verification.**
- Independence: this is an operational integration audit, not an additional independent mathematical review of the Inertia or Graph blocks, which I implemented. Root and `probability_review` supplied the independent statement and final proof reviews of those blocks.

## Exact advertised coverage

I compared the original three signatures with `Challenge.lean` at immutable
revision `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e`, and each new block with
its separate approved Challenge. After whitespace normalization, every full
signature is preserved exactly in the combined Challenge. The count is:

| Block | Declarations |
| --- | ---: |
| Original sign and integral algebra | 3 |
| Prescribed lengths and transfer | 5 |
| Actual Gaussian mixture | 3 |
| Finite core inertia | 2 |
| Actual Cauchy variance function | 5 |
| Actual multigraph | 7 |
| Total | 25 |

The combined Challenge, `comparator.json.theorem_names`, the 25
`formalization.yaml.status.main_results`, and the 25 Solution axiom-print
commands select exactly the same set without duplicates. The Comparator
configuration has `definition_names: []`, distinct Challenge and Solution
modules, and only the permitted standard axioms. The actual pinned metadata
schema and coverage validator passes. All five extensions have both statement
and both final-proof approval reports; their recorded current mathematical
file hashes agree with the files included in this integration.

## Actual elaborated statements and definition closure

I independently built `Challenge` and `Solution`, then ran the retained local
audit program `verification/referee-1-integration-compare.lean`. It imports
Challenge and Solution into separate Lean environments. For every selected
declaration it requires an actual theorem in both environments and compares
the full elaborated `ConstantVal`, including its type and universe parameters.
It then follows the types' referenced constants, comparing complete constant
information and the dependency closure of their types and values, including
inductive constructors and recursor rules. Advertised theorem bodies alone
are exempted, as they must be because Challenge contains placeholders.

The traversal follows the relevant logic in the project's pinned Comparator
source; I fetched its three small source modules at the locked immutable
revision and verified their SHA-256 digests before inspecting them. Attribution
is retained in the local audit source. This supplemental program does not
export declarations, rerun the isolated kernel checker, or claim to replace
the authoritative Comparator workflow.

Results: all **25 actual theorem statements match**, and the complete visited
closure of **32,932 referenced constants matches**. The matched project
constants include the graph, endpoints, vertex/edge types, actual Cauchy
variance function and measure, Gaussian-mixture measure, concrete core
quadratic forms and equivalence, actual prime-root length fraction,
contaminated measure, and original sign definitions. Thus matching theorem
names do not conceal different definitions between these local environments.

The actual Solution environment reports **5,199 imported modules**, with no
module whose name ends in `Challenge`. The solution imports the six proof
modules, and the deliberate placeholders never enter that import closure.

## Local commands and axiom evidence

All commands below were run by this auditor. Logs retain exit codes.

| Command | Result | Evidence |
| --- | --- | --- |
| `lake build Challenge Solution` | Exit 0, successful combined build; only intentional Challenge warnings | `verification/referee-1-integration-build.log` |
| `lake env lean --run verification/referee-1-integration-compare.lean` | Exit 0, 25 statement and 32,932 closure comparisons pass | `verification/referee-1-integration-comparison.log` |
| `lake env lean Solution.lean` | Exit 0, fresh direct re-elaboration and 25 axiom reports | `verification/referee-1-integration-axioms.log` |
| `.venv/bin/python tools/lean/validate_manifest.py research/lean/114` | Exit 0, pinned schema and exact coverage pass | `verification/referee-1-integration-manifest.log` |

The actual transitive axiom sets equal the metadata's result-by-result sets:
24 results use `propext`, `Classical.choice`, and `Quot.sound`; the
parallel-edge theorem uses only `propext` and `Quot.sound`. There is no
`sorryAx`, custom axiom, or native-evaluation axiom in these closures.

## Source preservation and scope

The canonical problem's original title and complete **Problem statement**
section are unchanged from upstream commit
`8eff4c7f8516ce38dd5a8aa31d78b6f44b95cf88`. The unchanged section SHA-256 is
`750a9081ab8fa765cad49d26a1838428ce5685b25e0911e61b7c714c6f2d22fc`.
Both original universal assertions remain present, and ID 114 and its
canonical path are retained. All nine hashes in the manuscript package's
current provenance record match their files, including the untouched source
PDF and frozen statement snapshot.

I read the refreshed Lean README, exact-scope document, verification README,
metadata, canonical page, source-package README, combined review, and
provenance. They accurately separate the 25 supporting results from the
unformalized metric/spectral bridge, stable ratio law and its properties,
process convergence, random evaluation, and complete graph limit. The graph
block's Euler expression is not described as a formalized homology dimension.
The actual variance theorem retains intrinsic assumptions on a future ratio
law; it does not manufacture that law. Mathematical authorship and AI review
roles remain explicit.

The earlier Linux run at `4c780fd5f95407e9a6a7c55dcb7c0f4c04bfaa2e` certifies
only the initial three declarations. The current documents correctly label
expanded Linux verification as pending. This audit claims no success for an
unexecuted expanded Linux run. New candidate Length files are outside this
25-result boundary and are neither imported nor advertised here; later
integration of them requires an updated audit and fresh corresponding
mechanical evidence.

## Frozen integration hashes

| File | SHA-256 |
| --- | --- |
| `Challenge.lean` | `82f9549d7586ca765de58e195c20c292b798f739845087b73969351920cf8903` |
| `Solution.lean` | `18c976f941f59a69f208505294ee1f576c1b5a9fcf868aa3848a35f0a0753e8e` |
| `comparator.json` | `4449dd71aa3d02b7144fd88d260d500e5d56c56c95092ead6303c8a448276820` |
| `formalization.yaml` | `eed91e24dc0f2dbd492db5cf449c65e5d42d30918433f6161744686c6d515806` |

`verification/referee-1-integration-source-audit.json` additionally records
all six blocks' actual definition/proof files, separate Challenges, pins,
scope-document hashes, declaration lists, exact axiom sets, original-target
check, and provenance checks. Administrative changes made after this record
must be identified as later changes; these hashes are not claims about a
future branch head.
