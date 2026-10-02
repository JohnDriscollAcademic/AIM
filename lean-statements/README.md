# AIM Lean workspace

This workspace uses the same pinned environment as
[OpenProblemsInNLA](https://github.com/ajt60gaibb/OpenProblemsInNLA/tree/e375a6fc0a12df52c4f5a38b53df78b837e1c390/lean-statements):

- Lean **4.33.1**.
- LeanCert `621a43d7cf21f87872392a01e874f2f1dbddc926`.
- Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`.

`lake-manifest.json` also pins every transitive dependency. Keep it committed;
use the existing pins when reproducing a build. Source provenance is recorded
in [NOTICE.md](NOTICE.md).

## Build locally

With `elan` installed, run from the repository root:

```bash
cd lean-statements
lake exe cache get
lake build
```

Elan selects the version in `lean-toolchain`. The first run may download the
toolchain, source dependencies and Mathlib cache. Open this directory as the
Lean project when working in an editor.

The default build checks the declaration controls and proves the small
infrastructure certificate `Real.log 2 < 7/10` using
`leancert (trust := kernel)`. It also checks that certificate's transitive
trust with `#assert_trust kernel` and prints its axioms. This certificate
does not formalize or solve any AIM problem.

`StatementControls.lean` tests rejection of target axioms, non-propositions,
free parameters, custom axioms, `sorryAx` and native-execution trust. Its
deliberate invalid declarations are confined to the controls. The certificate
solution imports neither these controls nor the trusted challenge.

## State an AIM problem

A declaration `def Target : Prop := ...` states a mathematical question. It
does not prove `Target`. The command `#assert_statement Target` checks that
the declaration is a safe definition of closed type `Prop` and that its axiom
closure uses only `propext`, `Classical.choice` and `Quot.sound`; independent
review must establish that its meaning matches the original problem.

Before adding a problem statement:

1. Preserve the complete canonical source and its revision and SHA-256 hash.
   Write an explicit specification covering all subquestions, assumptions,
   domains, quantifiers, constants and endpoint conventions.
2. Obtain two independent specification reviews before writing the statement.
   Define the proposition in `AIM/Statements/` with explicit mathematical
   definitions and no placeholder semantics.
3. Freeze a separate reviewed copy, record the source and complete local
   import-closure hashes together with the dependency pins, and obtain two
   independent reviews of the actual Lean boundary. Authors do not review
   their own work; disclose AI reviews as such.
4. Add checks for both closed propositions and a certificate that the live
   proposition equals its frozen copy. Configure Comparator to check that
   equality. A mathematical change requires a new specification and new
   reviews before refreshing the snapshot.

The starter workspace contains no AIM targets, frozen problem statements or
problem review records. The upstream per-problem metadata and freeze tooling
must be adapted to AIM's source layout before claiming the same automated
review gates for a new target. A proof of `Target` then requires its own
independently reviewed statement and proof verification.

## Verify the infrastructure on Linux

From a committed, unchanged checkout on non-root Linux with the prerequisites
in [the harness guide](../tools/lean/HARNESS.md), run:

```bash
tools/lean/bootstrap.sh /tmp/aim-lean-tools
tools/lean/verify.sh lean-statements /tmp/aim-lean-tools
```

Comparator checks the smoke certificate against `IdentityChallenge.lean`
using the separate `IdentitySolution.lean`, verifies the allowed axioms, and
replays the proof through Lean's kernel in the real sandbox. The challenge's
deliberate placeholder is never imported by the solution. A macOS build and
a configured CI workflow are distinct from a successful Linux verification
run; retain the logs and receipt from the actual run.
