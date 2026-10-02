# Lean setup and verification

AIM uses the Lean setup from
[OpenProblemsInNLA at e375a6fc0a12df52c4f5a38b53df78b837e1c390](https://github.com/ajt60gaibb/OpenProblemsInNLA/tree/e375a6fc0a12df52c4f5a38b53df78b837e1c390).
The shared statement workspace and the isolated proof checker have different
jobs: a statement defines a proposition; a proof establishes it. Installing
the tools or passing the infrastructure smoke test does not resolve an AIM
problem.

## Pinned environment

| Component | Version or immutable revision |
| --- | --- |
| Lean | `leanprover/lean4:v4.33.1` |
| Mathlib | `0df444a360eaa60ab8c11dca51a86af692955474` (`v4.33.1`) |
| LeanCert | `621a43d7cf21f87872392a01e874f2f1dbddc926` |
| Comparator, exporter and sandbox source bundle | Forsythe `8d1b0c0545a77b40245e84705aa7d273e6c81e62` |
| Formalization metadata schema | v0.4 at `99c678e569c7c4c0772db297c5ddd5e4c9b6322e` |

All transitive Lean dependencies are locked in
[`lean-statements/lake-manifest.json`](../../lean-statements/lake-manifest.json).
The verifier additionally checks SHA-256 hashes for every downloaded checker
source in [`source-lock.json`](../../tools/lean/source-lock.json). Keep these
pins under review; do not run `lake update` as a routine setup step.

## Local development (macOS or Linux)

Install [elan](https://github.com/leanprover/elan#installation), Lean's toolchain
manager, and put its `bin` directory on your PATH. The usual macOS/Linux
installer is:

```sh
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /tmp/elan-init.sh
sh /tmp/elan-init.sh -y --default-toolchain none
. "$HOME/.elan/env"
```

From the AIM checkout, run:

```sh
cd lean-statements
lake exe cache get
lake build
```

Elan reads `lean-toolchain` and installs the pinned Lean version. Lake uses
the committed dependency manifest; `cache get` downloads Mathlib's compiled
cache. Open `lean-statements` as the project folder in VS Code with the
`leanprover.lean4` extension for interactive work. See the
[workspace guide](../../lean-statements/README.md) for adding statements.

For the Python metadata and project-selection checks, from the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r tools/lean/requirements.txt
python -m unittest discover -s tests -p 'test_lean_verification.py' -v
python -m unittest discover -s tools/lean -p 'test_*.py' -v
python tools/lean/projects.py --all
```

An empty project matrix is expected until an AIM proof project is added.
The shared workspace's smoke theorem is an infrastructure control, not a
catalogue entry.

## Complete proof projects

Use one self-contained project per current AIM problem ID:

```text
research/lean/022/
  lean-toolchain
  lakefile.toml
  lake-manifest.json
  LICENSE
  formalization.yaml
  NUMERICAL_TARGETS.md
  AIM/P022/Definitions.lean
  AIM/P022/Proof.lean
  Challenge.lean
  Solution.lean
  comparator.json
  reviews/
  verification/
```

This is an example layout, not a claim that problem 022 has been formalized.
Each project owns its pins. Use a TOML Lakefile with separate Challenge and
Solution libraries, a committed manifest with immutable HTTPS GitHub
dependencies, and the pinned toolchain above. The initial harness does not
accept local path dependencies or `lakefile.lean`.

Project discovery uses AIM's existing `data/*.json` and the retained records
in `catalogue.json`; it does not introduce a new problem-number registry.
Canonical-page edits recheck the associated project. Shared checker,
schema, workflow or catalogue edits recheck all projects. A source-only
project is still selected and fails on missing required metadata; a removed,
renamed, unregistered or symlinked project cannot silently skip checking.
Cite the canonical path and source commit alongside the ID, as required by
AIM's existing numbering policy.

Before implementing a proof, freeze the complete source problem and informal
argument, including their revision, authors and hashes. Write
`NUMERICAL_TARGETS.md` with every domain, quantifier, constant, endpoint,
normalization and subquestion. Obtain two independent statement reviews,
then type-check and freeze the actual definitions and `Challenge.lean`.
Changing the mathematical boundary reopens review. The solution must not
import the challenge or its deliberate proof placeholders.

The Comparator configuration must list every advertised result, have no
replaceable definition holes (`"definition_names": []`), and permit only
`propext`, `Classical.choice` and `Quot.sound`, or a subset. Numerical
certificates use `set_option leancert.trust "kernel"`, explicit
`leancert (trust := kernel)`, and `#assert_trust kernel`. Prefer exact algebra
and proved reductions before interval arithmetic. `native_decide`, `sorry`
or custom axioms do not provide an accepted proof certificate.

Supply a truthful [v0.4 manifest](schema/README.md) and follow the
[independent review protocol](REVIEW.md). Record original authors separately
from formalization authors and label AI reviews accurately. Validate metadata:

```sh
python3 tools/lean/validate_manifest.py research/lean/022
```

## Authoritative Linux checks

The [Lean verification workflow](../../.github/workflows/lean-verification.yml)
runs the original NLA harness on Ubuntu 24.04, including the actual sandbox,
kernel replay, Comparator and rejection controls. It uploads fresh logs as
GitHub Actions artifacts. The separate
[Lean statements workflow](../../.github/workflows/lean-statements.yml)
builds the starter workspace and checks its infrastructure certificate.
Neither workflow changes catalogue statuses.

For a manual reproduction on non-root Linux with the prerequisites in the
[harness guide](../../tools/lean/HARNESS.md), commit the unchanged project
inputs first, then run from the repository root:

```sh
tools/lean/bootstrap.sh /absolute/path/to/aim-lean-tools
tools/lean/selftest.sh /absolute/path/to/aim-lean-tools
tools/lean/verify.sh research/lean/022 /absolute/path/to/aim-lean-tools
```

The tool directory must be outside the project. The host needs Go >=1.24,
elan, Git, Python, a C compiler, Bubblewrap, permitted unprivileged namespaces
and a working user systemd session. GitHub Actions configures those using the
same pinned actions and Go version as NLA. An ordinary container or macOS
build is not an authoritative substitute. The checker fails if isolation is
unavailable. Use an isolated runner without credentials, as explained in the
harness guide.

For promotion to **Lean verified**, retain a dated successful result and logs,
transitive axiom output, exact proof revision, statement correspondence and
independent reviews in a linked local `verification_record`, as specified in
[CONTRIBUTING.md](../../CONTRIBUTING.md#status-and-evidence). A green build or
statement-equality certificate alone is insufficient. NLA's historical logs
do not certify AIM; every AIM proof needs its own run.
