# AIM 637 â€” singular stationary Elo ratings

**Siavash Sadeghi**

**Proposed computer-assisted disproof. Independent mathematical review pending.**

Target: **Absolute continuity of stationary Elo ratings**, active problem 637 in
[MColbrook/AIM at `fa98b75`](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/637-elo-density.md), reviewed 2026-10-02. The page is labeled Partial because several
other stationary properties are established; its binary-score density target
remains unresolved. See `TARGET_AUDIT.md` for eligibility and access limitations.

## Result

For two equally skilled players, choose exactly

- `N = 2`, `rho = (0,0)`;
- `c = 1/2`, `K = 9/10`, so `K*c = 9/20 < 1`.

The first coordinate is the Markov chain

```
X[n+1] = X[n] - (9/10)*tanh(X[n]) + (9/10)*epsilon[n+1]
```

with independent fair signs. Its unique invariant probability is singular
continuous, has full support on the real line, and has measure Hausdorff
dimension at most `10*log(2)/7 < 1` (approximately 0.99021025794).
The dimension refers to a full-probability Borel carrier, not the support.
This gives an admissible counterexample to the repository's universal claim.

## Read and reproduce

Start with [the proof](aim637_counterexample.pdf). The editable mathematical
source is `aim637_counterexample.tex`.

Both verification programs require only **Python 3.10+**, with no third-party
packages and no network access. From this directory:

```bash
python3 verify_exact.py --output exact_results_reproduced.json
python3 verify_numeric.py --exact exact_results_reproduced.json --output numeric_results_reproduced.json
python3 -m unittest -v test_verifiers
```

Expected: both print `"status": "PASS"`.

The exact run proves 5,001 finite inequalities with outward-rounded integer
intervals, and checks 14 rational constants. The paper's curvature bound and
analytic tails convert these into a global drift inequality. The martingale and
covering arguments then prove singularity. No simulation is needed for the proof.

The separate numerical program uses 80-digit Decimal arithmetic, a different
hyperbolic-function evaluation, and explicit derivatives at 10,001 points
including midpoints. It performs 20,024 supporting checks. It is supplementary
numerical evidence, **not** an interval proof or independent mathematical review.

Optional partial exact runs are available via `--start` and `--end`; their JSON
is explicitly marked **partial grid only** and does not certify the global claim.
The checks remain enabled under `python3 -O`.

On systems with LaTeX:

```bash
pdflatex -interaction=nonstopmode -halt-on-error aim637_counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error aim637_counterexample.tex
```

LaTeX output need not be byte-identical because PDF creation metadata can differ.
The JSON values are deterministic. Line endings may differ between platforms.

## Contents

| File | Purpose |
|---|---|
| `aim637_counterexample.pdf`, `.tex` | Full proof and editable source |
| `verify_exact.py` | Integer-interval global certificate |
| `exact_results.json` | Recorded exact verification, with sample enclosures |
| `verify_numeric.py` | Separately implemented high-precision numerical checks |
| `numeric_results.json` | Recorded supplementary results |
| `certificate.json` | Exact rational parameters and proof constants |
| `target_statement.md` | Paraphrased target and mathematical match |
| `TARGET_AUDIT.md` | Dated source/submission audit and its limitations |
| `RESOLUTION_REPORT.md` | Repository-resolution report and target match |
| `REVIEW_CHECKLIST.md` | Critical items for independent review |
| `REPRODUCTION_RECORD.md`, `environment.json` | Actual execution and packaging record |
| `REVIEW_REPORT.md` | Dated proof/code review, changes and limitations |
| `test_verifiers.py` | Arithmetic, input-validation and partial-run regressions |
| `compile_check_log.txt` | Final PDF build diagnostics |
| `SHA256SUMS` | Checksums for the delivered source/result files |

## Evidence and scope

This is a **Solution claimed** submission awaiting independent mathematical review.
The supplied proof and both programs were produced in an AI-assisted research
session. Codex reviewed the supplied proof and code and reproduced the results
for this submission; no independent human audit or formal verification is claimed.
See [the review report](REVIEW_REPORT.md) for the exact scope.

The PR adds only this package under `research/solutions/siavash-sadeghi-637/`.
It asks the maintainers to review the claim; catalogue status changes and any
associated renumbering remain for their review process. The current problem ID
is pinned to the revision above because later repository changes can renumber it.

The argument uses the original nonlinear binary-score process. It does not
round ratings, add score noise, impose a bounded state space, or replace the
chain by its linearization. It resolves the universal assertion negatively,
without classifying all parameter choices or making a claim about the small-
`K*c` regime or every `N > 2`.
