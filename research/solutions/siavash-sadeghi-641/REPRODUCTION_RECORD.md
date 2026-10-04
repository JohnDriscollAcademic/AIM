# Reproduction record: AIM 641

4 October 2026; Siavash Sadeghi submission; checks run by Codex (AI).

Python 3.12.14; NumPy 2.3.5 and SciPy 1.18.1 for the upwind experiment; SymPy 1.14.0 for exact algebra where applicable. Packages unrelated to this target are not required.

The exact verifier and independent 3,432-monomial expansion pass in both normal and optimized Python. The printed table agrees in all 45 rows. Regression tests reject fractional coefficient damage, missing and duplicate records, shifted-array corruption and a changed printed row, including optimized execution. Replaced removable assert checks with explicit failures and removed the independent checker's truncating int conversion.

See README for commands and the included check logs where applicable. PDF source is `aim641_report.tex`; compile twice. `compile_check_log.txt` records the two successful passes and final diagnostics. The existing local MiKTeX compiler was used after the built-in editor compiler reported an environment failure. Final PDF pages were rendered with Poppler and visually reviewed.

The repository catalogue check was run at the pinned main commit with the research files added. Its purpose is structural validation, not mathematical certification. No catalogue machinery changes are part of this submission.
