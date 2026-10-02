# Contributing

Suggestions, corrections and resolution reports are welcome through [issues](https://github.com/MColbrook/AIM/issues) or pull requests.

## Adding or revising a problem

Give a precise statement, primary references, and a dated search for later proofs or counterexamples. Explain its applications or mathematical significance; say when no direct application is known. Further additions exclude numerical linear algebra.

## Reporting a resolution

Include the problem ID and repository commit, a proof or counterexample link, and an explanation of how it matches the full target. Identify what was reviewed and by whom, including whether the review was human or AI.

## Status and evidence

Use the [status labels](README.md#problem-status), keeping the page badge and metadata consistent.

- **Partially resolved** entries need nonempty `**Known cases:**` and `**Remaining target:**` notes in **Status review**.
- A complete claim awaiting independent review is **Solution claimed**.
- **Solved** requires a published resolution or a documented independent audit of the complete argument.
- **Lean verified** requires a local `verification_record` linked from the page: pinned proof revision, Lean and dependency versions, theorem-to-target comparison, reproduction commands, a dated successful log, and transitive axiom output. Only `propext`, `Classical.choice` and `Quot.sound` are acceptable; no `sorryAx` or unproved custom axioms.

Only `Open` and `Partially resolved` count as open targets. Mark a completed problem `Solved` in its existing page and `data/*.json` row, keeping its ID and linking to the proof and review; the generator includes it in the solved lists. Other retained statuses use `research/` and `catalogue.json`. Update `last_checked` only after an actual literature or evidence review.

Retained entries need a subject `group`; solved entries also need an `outcome` and direct `proof` and `review` links for the generated lists.

## Updating the catalogue

Problem pages need **Area**, **Status**, **Last checked**, and the sections **Problem statement**, **Application**, **References**, and **Status review**. Put the status badge before the first section. Use `math` fences for display equations and dollar-backtick delimiters for inline equations, with core TeX operators such as `\mathop{\mathrm{Per}}`.

Update the page and its `data/*.json` row. Add new IDs to a publication batch in `catalogue.json`; problem-page IDs must remain consecutive, including solved entries. Repair references when renumbering. Edit the generator for README or index wording.

```sh
python3 scripts/catalogue.py --write
python3 scripts/catalogue.py --check
```

The checks validate structure and links, not mathematical correctness. Run `python3 scripts/test_catalogue.py` when changing catalogue machinery.

Optional rendering QA: install `scripts/requirements-math.txt` and `mathjax-full@3.2.2`, set `NODE_PATH` to its `node_modules` directory, and run `python3 scripts/check_math.py`.
