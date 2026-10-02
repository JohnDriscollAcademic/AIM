# Reproduction record

**Siavash Sadeghi - review performed by Codex (AI), 2 October 2026.**

Original archive SHA-256:
`43f5194ee4af651bb9f3e89a1013c6bab2ed674f5456d5d53e4212049587c339`.
All 14 supplied manifest entries matched before execution. Originals were
preserved; this directory contains the reviewed submission.

Python 3.12.14 on Windows 11, standard library only. The original package and
the final reviewed programs both passed full exact and numerical runs in normal
and optimized (`-O`) modes. JSON values exactly match the supplied records.
Windows line endings initially caused a byte-comparison mismatch in the review
harness; parsed values and normalized text matched, so no result was changed.

## Commands, from this directory

```sh
python verify_exact.py --output exact_results_reproduced.json
python verify_numeric.py --exact exact_results_reproduced.json --output numeric_results_reproduced.json
python -m unittest -v test_verifiers
python -O verify_exact.py --output exact_results_optimized.json
python -O verify_numeric.py --exact exact_results_optimized.json --output numeric_results_optimized.json
python -O -m unittest -v test_verifiers
```

Each mode passed 5,001 rigorous grid checks, 14 analytic constant checks,
20,024 supplementary numerical checks, and all seven regression tests.
The final numerical runs used the supplied complete exact record; separate exact
runs reproduced its values. Partial runs retain their non-global status, and
invalid ranges and incomplete records are rejected. Timings are in environment.json.

The repository's `python scripts/catalogue.py --check` passed on the pinned base:
651 unique problems, metadata, sections, math delimiters, links and generated
indexes validated. This PR adds a research package and changes no catalogue machinery.

The built-in TeX compiler could not find its platform directories. The existing
MiKTeX installation compiled the final source twice with package installation
disabled. The final pass had no LaTeX or box warnings. All eight pages were
rendered with Poppler and visually inspected. See compile_check_log.txt.

The SHA256SUMS manifest covers every delivered package file except itself.
The final ZIP was CRC-tested and its entries compared byte-for-byte to this
directory. Reproduction output files and Python caches are excluded.
