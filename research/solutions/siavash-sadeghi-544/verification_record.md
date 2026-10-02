# Verification record - 2 October 2026

**Contributor and submitter:** Siavash Sadeghi.

**Target:** original AIM 544 at `aa776a01d7d48a79f93251af11fde9454b0aea95`,
current AIM 534 at `fa98b7525fa3f78317536a8825f9cfa0ae1c369c`.
Only the numbered heading changed. The proof concerns verbose persistence.

## Reviewers and scope

The supplied proof and programs are AI-generated. Codex read the complete
proof, package documentation, machine-readable witness, current repository
README and contribution rules, and exact target. Separate Codex AI reviewers
examined (1) the mathematical argument and primary source, (2) both supplied
programs and the JSON witness, and (3) repository records for prior submissions.
These are separate AI reviews within this preparation workflow. No human
peer review, publication acceptance, repository acceptance, or formal
proof-assistant verification is claimed. No mathematical review is attributed
to Siavash Sadeghi.

The mathematical reviewer found no blocking flaw in the four-point witness,
the lower bound over arbitrary finite pullbacks, every-field/every-positive-
degree extension, diameter-bar lemma, equal-cardinality minimality, and
correspondence claim. Published Definitions 4.7 and 5.3 and Example 5.10 of
Mémoli-Zhou agree with the target conventions and credited known pair.
The detailed scope is in [mathematical_review.txt](mathematical_review.txt).
Acceptance by an independent mathematical reviewer remains outstanding.

## Computations actually run

All 11 original `SHA256SUMS` entries matched before editing. Both supplied
verifier programs remain byte-for-byte unchanged.

```text
python verify_boundary.py --output boundary_results.json
PASS: 6653 checks; 720 exact reductions; 5226 finite pullback-pair comparisons

python verify_ranks.py --output rank_results.json
PASS: 3650 checks; 356 exact matrix ranks; 3267 finite inequality instances

python verify_supplementary.py --output supplementary_results.json
PASS: 246 supplementary checks
```

All three also pass with `python -O`; each normal/optimized result pair is
byte-identical. The two original result files agree with the uploaded results
except for the Python/platform metadata. See [environment.txt](environment.txt)
and [verification_logs.txt](verification_logs.txt).

The boundary program checks degrees 1-6 over Q and four prime fields, two tie
orders, and every positive four-fiber vector with total size 4-8 over three
fields. Its matching algorithm uses actual bijections without added diagonal
points. The separate rank implementation checks degrees 1-5 over Q and F_3,
threshold homology, simplex ranks, and 3,267 bounded binomial inequalities.

The new supplementary program reads the JSON witness, tests its matrices,
maps and barcodes, checks genuine off-diagonal bars on a square metric and a
rational rescaling, compares 60 exact rational matchings with exhaustive
bijections, and exercises the diameter lemma on 20 finite metrics and their
pullbacks. It reuses `verify_boundary.py`; it is not a third independent
persistence implementation. All check conditions use explicit exceptions.

## Changes and document checks

Added the contributor/submitter name and precise AI review disclosure,
documented the original/current target identity, refreshed recorded outputs
and repository audit, and added the reproducible supplementary checks.
Clarified equal barcode cardinality on a common set and distinguished the
distance-2 third space from the source example's distance-1 space with the
same letter. The mathematical construction and original algorithms are
unchanged. Credit for the published two-space example is retained.

The PDF was built in two successful pdfLaTeX passes using the existing local
MiKTeX installation after the built-in editor compiler returned a platform-
directory error. All six pages were rendered with Poppler and inspected for
equations, matrices, legibility, page breaks, references, clipping, and overlap.
The final build log contains no LaTeX or box warnings; see
[compile_check_log.txt](compile_check_log.txt). No TeX installation was needed.

The current repository catalogue check passes for 651 active problems; the
original baseline also passed before refresh. See
[repository_catalogue_check_log.txt](repository_catalogue_check_log.txt).
No catalogue machinery changed, so its unit tests were not rerun.

The delivered archive is integrity-checked, freshly extracted, and all
manifest entries verified. All three programs are rerun from that extraction
in normal and optimized modes, reproducing the recorded outputs.

## Submission and limits

[target_audit.md](target_audit.md) records the dated repository search and its
access limitations. No overlapping submission was found in inspected public
records. This is a bounded search, not a guarantee about inaccessible or
subsequent work.

The package is prepared for a pull request under
`research/solutions/siavash-sadeghi-544/`, classified as **Solution claimed**
and with no catalogue status change proposed. The analytic argument supplies
the universal quantifier; the finite computations do not establish it.
