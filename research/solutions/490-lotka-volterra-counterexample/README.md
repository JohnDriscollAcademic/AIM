# D-stable Lotka–Volterra counterexample

The [proof](PROOF.md) gives an exact rational four-species interaction matrix that is D-stable but has a nonconstant strictly positive periodic solution. This disproves global attraction in [problem 489 at the pinned target revision](statement.md), formerly problem 490. The [current archive record is 650](../../resolved/650-lotka-volterra-d-stable-global-attraction.md).

**Status:** Solved under the repository's documented-independent-audit convention. Read the [complete AI audit](REVIEW.md) for the analytic argument, implementation checks and scope of the review. The supplied derivation does not identify its author. The package was adapted and reviewed by OpenAI Codex on 2026-10-02; human peer review and proof-assistant verification are not claimed.

The certificates establish Hurwitz stability for every positive diagonal scaling and the existence of an exact periodic orbit with all coordinates between $`1/8`$ and $`4`$, with period between $`7.86959`$ and $`7.86961`$. The orbit is specified by the unique fixed point in a certified Fourier ball, rather than by a rounded initial condition.

## Reproduce

From this directory, in a Python environment with pip:

```sh
python -m pip install -r requirements.txt
python verify.py
python verify.py --slow-matmul
python audit.py
python review_checks.py
```

Run without Python's `-O` flag. The main verifier rejects disabled assertions. Python 3.14.4 and NumPy 2.5.3 were used for the recorded runs; NumPy is the only external dependency and is pinned in [requirements.txt](requirements.txt). [environment.txt](environment.txt) and [reproduction.json](reproduction.json) record the environment, provenance, input hashes and commands.

Both matrix-product implementations were run successfully. The default splits signed integers into bounded 26-bit digits; the slow option uses arbitrary-precision Python integers throughout the large product. All acceptance bounds use exact integers or rational numbers. Printed decimal approximations are diagnostic.

The verifier recomputes and writes [fourier_bounds.json](fourier_bounds.json) and [positivity_bounds.json](positivity_bounds.json). Both files reproduced the supplied exact fractions byte-for-byte. It does not trust them as inputs.

## Evidence

| File | Purpose |
| --- | --- |
| [PROOF.md](PROOF.md) | Full D-stability, infinite-dimensional contraction, positivity and nonconvergence argument. |
| [REVIEW.md](REVIEW.md) | Separate AI mathematical and implementation audit of the supplied derivation. |
| [statement.md](statement.md) | Pinned target, preserving its content with repaired local navigation. |
| [dstability.py](dstability.py), [dstability_certificate.json](dstability_certificate.json) | All 15 principal minors, 21 AM–GM atoms and 38 coefficient inequalities. |
| [fourier.py](fourier.py), [fourier_certificate.npz](fourier_certificate.npz) | Exact Fourier anchor, finite inverse and full contraction bounds. |
| [anchor_coefficients.csv](anchor_coefficients.csv) | Text copy of all 196 reference coefficient pairs. |
| [positivity.py](positivity.py) | Outward-rounded integer interval bounds on positivity, nonconstancy and period. |
| [verify.py](verify.py), [verification.log](verification.log), [slow-verification.log](slow-verification.log) | Reproduced complete certificates using both integer-product methods. |
| [audit.py](audit.py), [audit.log](audit.log) | Reproduced supplied convolution and integer-product cross-checks. |
| [review_checks.py](review_checks.py), [review-checks.log](review-checks.log) | New exact CSV, residual, quadratic derivative and disabled-assertion checks written during this review. |
| [SHA256SUMS.txt](SHA256SUMS.txt) | Integrity hashes for the adapted package. |

To check integrity from this directory, run `sha256sum -c SHA256SUMS.txt`, or `shasum -a 256 -c SHA256SUMS.txt` on macOS. The source folder used to supply the argument is excluded from Git; all necessary proof and verification inputs are retained here.
