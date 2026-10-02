# Problem 022, case n = 3: the equilateral triangle maximizes the perimeter-normalized first Steklov eigenvalue

**Partial result, awaiting independent review.** AI-generated (Claude Opus 5.5, Anthropic, in Claude Code); submitted by GitHub user cthalhammer. No human has reviewed the argument or the code.

The package proves the triangle case of [problem 022](statement.md) (the regular-polygon Steklov conjecture) at commit `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`. For every triangle $`T`$, $`\sigma_1(T)\mathop{\mathrm{Per}}(T)\le\sigma_1(E)\mathop{\mathrm{Per}}(E)`$, with equality only for the equilateral triangle $`E`$. The proof is computer-assisted: exact integer arithmetic and Arb ball arithmetic. Nothing is claimed for polygons with four or more sides.

## Contents

| File | Purpose |
| --- | --- |
| [PROOF.md](PROOF.md) | Complete argument: Lemmas 1–7 and the theorem |
| [statement.md](statement.md) | Unchanged problem page at the pinned commit |
| [RESOLUTION_REPORT.md](RESOLUTION_REPORT.md) | Report in the form requested by CONTRIBUTING.md |
| [REVIEW_AND_CHECKS.md](REVIEW_AND_CHECKS.md) | Self-review, mutation tests, separate AI referee pass, cross-checks |
| `certify/` | The certified computation; `main.py` runs all four steps |
| `certify/trial_coeffs.json` | Exact rational trial coefficients, an input certificate |
| `certify/make_trial_coeffs.py` | Non-rigorous helper that produced the coefficients (not needed to verify) |
| `review/` | Review-only cross-checks and mutation tests (not part of the proof) |
| `numerics/` | Floating-point exploration (evidence only, not part of the proof) |
| `logs/` | Outputs of every script listed below |
| [ENVIRONMENT.txt](ENVIRONMENT.txt), `requirements*.txt`, `SHA256SUMS` | Environment, dependencies, checksums |

## Verifying

From this folder:

```sh
python3 -m pip install -r requirements.txt   # python-flint only
python3 certify/main.py                      # ~20 s; last line: ALL CERTIFIED CHECKS PASSED
```

`reproduce.sh` does the same and writes `logs/certify.log`. Each step raises an `AssertionError` (non-zero exit) if any check fails. The certified output does not depend on floating point: it was identical, apart from the environment line, under Python 3.9.23 with python-flint 0.6.0 and Python 3.12.14 with python-flint 0.9.0.

Optional review checks (need `requirements-review.txt`):

```sh
python3 review/mutation_tests.py      # every deliberately wrong input must be rejected
python3 review/selfcheck_local.py     # independent re-derivations of the local bound
```

## Proof outline

Every triangle is similar to $`T_S=\exp(S)E`$ for a traceless symmetric $`S`$.

1. A Crouzeix–Raviart finite-element lower bound with an exact integer inertia count gives $`\sigma_3(E)\ge1.388851`$ for circumradius $`1`$.
2. Temple's inequality in one symmetry sector of E encloses $`\sigma_1(E)`$ to 24 digits. It also shows the first eigenspace is two-dimensional, and residual bounds enclose the exact eigenfunctions' moments to about $`10^{-11}`$.
3. For $`0<\|S\|\le3/5`$, the exact first eigenspace of $`E`$, pulled back by $`\exp(S)`$, is a two-dimensional trial space. The resulting 2×2 matrix inequality is verified on 8412 boxes; the singular point at $`S=0`$ is factored out exactly.
4. For $`\|S\|\ge11/20`$, a linear trial function gives $`\sigma_1\mathop{\mathrm{Per}}\le3.193<3.872`$.
