# AIM 544 - a proposed exact counterexample

**Contributor and submitter:** Siavash Sadeghi.

**Target identity:** original AIM 544 at `aa776a01d7d48a79f93251af11fde9454b0aea95`,
now [AIM 534](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/problems/534-verbose-persistence-pullback-triangle.md) at `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.
The statement changed only in its numbered heading. Package filenames retain
the original ID to preserve the supplied revision reference.

**Claim:** the fixed-degree pullback matching distance of verbose Vietoris–Rips
barcodes does not satisfy the triangle inequality. Three four-point
ultrametric spaces give `D_1(X,Y)=0`, `D_1(Y,Z)=0`, `D_1(X,Z)=1` over every
field. A family with `k+3` points gives the same violation in every positive
degree `k`. This is the smallest possible common original cardinality.

**Evidence status:** Solution claimed; complete proposed disproof awaiting
independent mathematical acceptance. The supplied argument and programs are
AI-generated. Codex and separate AI reviewers examined the proof, programs,
source paper, and repository submissions during preparation. These reviews
are part of this AI-assisted workflow; no human peer review, publication
acceptance, or proof-assistant certificate is claimed. See
[verification_record.md](verification_record.md) for the review scope.

The first degree-one zero-distance pair is already in Mémoli–Zhou,
Example 5.10. The proposed disproof completes it using an equilateral third
space and a lower bound valid for every allowed common pullback. It is not a
claim to have newly invented the known pair.

## Read first

- `aim544_counterexample.pdf`: the proof, including the all-degree
  extension, common-cardinality minimality, precise attribution, and limits.
- `aim544_counterexample.tex`: editable mathematical source.
- `counterexample.json`: the distance matrices and explicit surjective maps.
- `target_audit.md`: target identity, source versions, prior-claim checks and
  access limitations.
- `resolution_report.md`: the resolution report matching the proof
  to the repository's exact assumptions.

## Reproduce

Python 3.10 or later; **no third-party packages** are required. From the
package directory:

```bash
python3 verify_boundary.py --output boundary_results.json
python3 verify_ranks.py --output rank_results.json
```

Recorded outputs:

```text
PASS: 6653 checks; 720 exact reductions; 5226 finite pullback-pair comparisons
PASS: 3650 checks; 356 exact matrix ranks; 3267 finite inequality instances
```

The checks also run with optimization enabled:

```bash
python3 -O verify_boundary.py
python3 -O verify_ranks.py
```

`verify_boundary.py` implements oriented boundary-column reduction over the
rationals and four prime fields. It retains every diagonal persistence pair
and never pads a matching with artificial diagonal points. Its general
matching routine is additionally checked against exhaustive bijections on
small inputs. It checks degrees 1–6, alternate tie orders, and every positive
four-fiber multiplicity vector on common sets of size at most eight in three
fields.

`verify_ranks.py` does not import the first program. It builds ordinary
boundary matrices at the filtration thresholds and obtains ranks using dense
row elimination over the rationals and the field with three elements. It
checks that positive homology vanishes and that rank increments agree with
the claimed barcode counts. It also tests finite cases of the binomial
inequality.

**The universal lower bound is an analytic proof in the PDF.** Neither
program enumerates all finite pullbacks or verifies all fields/degrees. Two
separate implementations do not constitute independent mathematical review.

## Build the PDF

A standard TeX distribution with pdfLaTeX, AMS packages, Latin Modern,
`geometry`, `microtype`, `booktabs`, `enumitem`, `fancyhdr`, `xcolor`, and
`hyperref` is sufficient:

```bash
pdflatex -interaction=nonstopmode -halt-on-error aim544_counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error aim544_counterexample.tex
```

Font files are not included. The supplied PDF was compiled without TeX box
warnings and all rendered pages were visually inspected. Exact checks
were also rerun from a fresh extraction of the delivered archive; see
`verification_record.md` for the actual scope.

`SHA256SUMS` records hashes of the delivered files other than itself. Code
uses explicit exception-based checks; it does not rely on Python assertions
that disappear under `-O`.

## Repository submission

This package is prepared for a pull request to
[MColbrook/AIM](https://github.com/MColbrook/AIM), under
`research/solutions/siavash-sadeghi-544/`, following its
[contribution instructions](https://github.com/MColbrook/AIM/blob/fa98b7525fa3f78317536a8825f9cfa0ae1c369c/CONTRIBUTING.md).
The [resolution report](resolution_report.md) identifies the pinned problem,
links the proof, compares every target condition, and discloses the reviewers.
The pull request contributes the proposed proof and supporting checks; it
does not alter the catalogue or claim an accepted solution. The current
prior-submission audit and its limitations are in [target_audit.md](target_audit.md).

## Supplementary witness and algorithm checks

```bash
python3 verify_supplementary.py --output supplementary_results.json
python3 -O verify_supplementary.py
```

Both modes pass 246 checks of the machine-readable witness, off-diagonal
and rational persistence examples, exhaustive small barcode matchings,
and diameter-bar examples. This program reuses `verify_boundary.py`.
The three programs together run 10,549 supporting checks. See
[verification_record.md](verification_record.md) for the full review,
[mathematical_review.txt](mathematical_review.txt) for the separate AI
proof review, and [verification_logs.txt](verification_logs.txt) for run logs.
