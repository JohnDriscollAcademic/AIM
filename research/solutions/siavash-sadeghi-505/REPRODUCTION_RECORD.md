# Reproduction record: AIM 505

4 October 2026; Siavash Sadeghi submission; checks run by Codex (AI).

Python 3.12.14; NumPy 2.3.5 and SciPy 1.18.1 for the upwind experiment; SymPy 1.14.0 for exact algebra where applicable. Packages unrelated to this target are not required.

Repeated all four supplied meshes (10, 20, 40, 80); displayed numerical values agree with the original table. Added rejection of nonfinite or nonphysical accepted trajectories and strict JSON serialization. The numerical choice gamma=500*M is not the proof of the diagonal sequence.

See README for commands and the included check logs where applicable. PDF source is `aim505_report.tex`; compile twice. `compile_check_log.txt` records the two successful passes and final diagnostics. The existing local MiKTeX compiler was used after the built-in editor compiler reported an environment failure. Final PDF pages were rendered with Poppler and visually reviewed.

The repository catalogue check was run at the pinned main commit with the research files added. Its purpose is structural validation, not mathematical certification. No catalogue machinery changes are part of this submission.
