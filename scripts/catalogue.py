#!/usr/bin/env python3
"""Build and validate the Markdown catalogue; no third-party packages required."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote

from markdown_math import validate_math

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "title", "area", "file", "status", "last_checked"}
SECTIONS = ("Problem statement", "Application", "References", "Status review")
GENERATED_DOCUMENTS = ("README.md", "CATALOG.md", "RESOLVED.md")
LOCAL_CACHE_DIRECTORIES = frozenset({".git", ".lake", ".venv", "__pycache__"})
STATUS_DISPLAY = {
    "Open": "🔵 OPEN",
    "Partially resolved": "🟡 PARTIAL",
    "Solution claimed": "🟠 SOLUTION CLAIMED",
    "Solved": "✅ SOLVED",
    "Lean verified": "🏆 LEAN VERIFIED",
    "Needs verification": "⚪ NEEDS VERIFICATION",
    "Withdrawn": "⚫ WITHDRAWN",
}
OPEN_STATUSES = ("Open", "Partially resolved")
SOLVED_STATUSES = ("Solved", "Lean verified")
RETIRED_STATUSES = tuple(status for status in STATUS_DISPLAY if status not in OPEN_STATUSES)


def markdown_paths(root):
    """Visit source Markdown without descending into local dependency caches."""
    for directory, subdirectories, filenames in os.walk(root):
        subdirectories[:] = [name for name in subdirectories
                             if name not in LOCAL_CACHE_DIRECTORIES]
        for name in filenames:
            if Path(name).match("*.md"):
                yield Path(directory) / name


def status_display(status):
    return STATUS_DISPLAY.get(status, status)


def date_errors(value, identifier):
    try:
        checked = date.fromisoformat(value)
        if checked.isoformat() != value:
            return [f"{identifier}: date must use YYYY-MM-DD"]
        if checked > date.today():
            return [f"{identifier}: status check is in the future"]
    except (TypeError, ValueError):
        return [f"{identifier}: invalid ISO date"]
    return []


def valid_id(value):
    return (isinstance(value, str) and bool(re.fullmatch(r"[0-9]{3,}", value))
            and int(value) > 0 and value == f"{int(value):03d}")


def next_problem_id(manifest):
    """Allocate after the current consecutively numbered collection."""
    issued = [identifier for batch in manifest["batches"] for identifier in batch["ids"]]
    issued.extend(row["id"] for row in manifest["retired"])
    return max(map(int, issued), default=0) + 1


def load_manifest():
    errors = []
    try:
        manifest = json.loads((ROOT / "catalogue.json").read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        return {}, [f"catalogue.json: {exc}"]
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 2:
        return {}, ["catalogue.json: expected schema_version 2"]
    for key in ("groups", "batches", "retired"):
        if not isinstance(manifest.get(key), list):
            errors.append(f"catalogue.json: {key} must be an array")
    if errors:
        return {}, errors
    removed = manifest.get("removed_ids", [])
    if not isinstance(removed, list) or not all(valid_id(i) for i in removed):
        return {}, ["catalogue.json: removed_ids must be an array of valid IDs"]
    if removed:
        return {}, ["catalogue.json: deleted IDs cannot be reserved; renumber remaining entries consecutively"]
    for key in ("groups", "batches"):
        items = manifest[key]
        if not items:
            errors.append(f"catalogue.json: {key} must not be empty")
        seen = set()
        for item in items:
            if (not isinstance(item, dict) or
                    not isinstance(item.get("key"), str) or
                    not re.fullmatch(r"[a-z0-9-]+", item["key"]) or
                    not isinstance(item.get("title"), str) or not item["title"].strip()):
                errors.append(f"catalogue.json: invalid {key} record")
                continue
            if item["key"] in seen:
                errors.append(f"catalogue.json: duplicate {key} key {item['key']}")
            seen.add(item["key"])
            if key == "batches" and (not isinstance(item.get("ids"), list) or
                                     not item["ids"] or
                                     not all(valid_id(i) for i in item["ids"])):
                errors.append(f"catalogue.json: invalid IDs in batch {item['key']}")
    group_keys = {group["key"] for group in manifest["groups"]
                  if isinstance(group, dict) and isinstance(group.get("key"), str)}
    for item in manifest["retired"]:
        if not isinstance(item, dict) or not valid_id(item.get("id")):
            errors.append("catalogue.json: retired ID needs a valid id")
            continue
        for field in ("title", "status", "last_checked", "reason", "record"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"catalogue.json: invalid retired {field} for {item['id']}")
        if not isinstance(item.get("group"), str) or item["group"] not in group_keys:
            errors.append(f"catalogue.json: invalid retired group for {item['id']}")
        resolved = item.get("status") in SOLVED_STATUSES
        if resolved or "outcome" in item:
            if not isinstance(item.get("outcome"), str) or not item["outcome"].strip():
                errors.append(f"catalogue.json: invalid retired outcome for {item['id']}")
        for field in ("proof", "review"):
            if not resolved and field not in item:
                continue
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"catalogue.json: invalid retired {field} for {item['id']}")
                continue
            if re.fullmatch(r"https?://\S+", value):
                continue
            evidence = (ROOT / value).resolve()
            if Path(value).is_absolute() or ROOT not in evidence.parents or not evidence.is_file():
                errors.append(f"catalogue.json: invalid retired {field} link for {item['id']}")
        if not isinstance(item.get("record"), str) or not item["record"].strip():
            continue
        record = (ROOT / item["record"]).resolve()
        if (Path(item["record"]).is_absolute() or ROOT / "research" not in record.parents or
                record.suffix != ".md" or not record.is_file()):
            errors.append(f"catalogue.json: invalid retirement record for {item['id']}")
        if item.get("status") not in RETIRED_STATUSES:
            errors.append(f"catalogue.json: invalid retired status for {item['id']}")
        errors.extend(date_errors(item.get("last_checked"), item["id"]))
        if item.get("status") == "Lean verified":
            value = item.get("verification_record")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{item['id']}: Lean verified requires a verification_record")
            else:
                evidence = (ROOT / value).resolve()
                if (Path(value).is_absolute() or ROOT not in evidence.parents or
                        evidence.suffix != ".md" or not evidence.is_file() or
                        not evidence.read_text(encoding="utf-8").strip()):
                    errors.append(f"{item['id']}: invalid or empty Lean verification_record")
    return manifest if not errors else {}, errors


def load_entries(manifest):
    entries = []
    errors = []
    expected_files = {f"{group['key']}.json" for group in manifest["groups"]}
    for path in sorted((ROOT / "data").glob("*.json")):
        if path.name not in expected_files:
            errors.append(f"Unregistered metadata file: data/{path.name}")
    for group in manifest["groups"]:
        stem = group["key"]
        path = ROOT / "data" / f"{stem}.json"
        if not path.exists():
            errors.append(f"Missing {path.relative_to(ROOT)}")
            continue
        try:
            rows = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if not isinstance(rows, list):
            errors.append(f"{path.name}: expected an array")
            continue
        for row in rows:
            if not isinstance(row, dict) or not REQUIRED <= row.keys():
                errors.append(f"{path.name}: incomplete metadata row")
                continue
            if not all(isinstance(row[k], str) and row[k].strip() for k in REQUIRED):
                errors.append(f"{path.name}: all metadata fields must be nonempty strings")
                continue
            if not valid_id(row["id"]):
                errors.append(f"{path.name}: invalid ID {row['id']}")
                continue
            if row["status"] not in (*OPEN_STATUSES, "Solved"):
                errors.append(f"{row['id']}: invalid page status; use Open, Partially resolved or Solved")
            if row["status"] == "Solved":
                if not isinstance(row.get("outcome"), str) or not row["outcome"].strip():
                    errors.append(f"{row['id']}: Solved requires an outcome")
                for field in ("proof", "review"):
                    value = row.get(field)
                    if not isinstance(value, str) or not value.strip():
                        errors.append(f"{row['id']}: Solved requires a {field} link")
                    elif not re.fullmatch(r"https?://\S+", value):
                        evidence = (ROOT / value).resolve()
                        if Path(value).is_absolute() or ROOT not in evidence.parents or not evidence.is_file():
                            errors.append(f"{row['id']}: invalid {field} link")
            errors.extend(date_errors(row["last_checked"], row["id"]))
            entries.append({**row, "group": stem})
    return sorted(entries, key=lambda row: int(row["id"])), errors


def presentation_records(entries, manifest):
    """List resolutions separately while keeping their original pages and IDs."""
    opened = [row for row in entries if row["status"] in OPEN_STATUSES]
    solved = [{**row, "record": row["file"],
               "reason": "Resolution recorded on the problem page."}
              for row in entries if row["status"] == "Solved"]
    return opened, {**manifest, "retired": [*manifest["retired"], *solved]}


def table_text(value):
    return " ".join(value.splitlines()).replace("|", "\\|")


def subject_index(entries, manifest, document=""):
    lines = ["| Subject group | Open targets | Solved |", "| --- | ---: | ---: |"]
    for group in manifest["groups"]:
        title = group["title"]
        anchor = title.lower().replace(",", "").replace(" ", "-")
        count = sum(row["group"] == group["key"] for row in entries)
        solved = sum(row["group"] == group["key"] and row["status"] in SOLVED_STATUSES
                     for row in manifest["retired"])
        lines.append(f"| [{title}]({document}#{anchor}) | "
                     f"[{count}]({document}#{group['key']}-open) | "
                     f"[{solved}]({document}#{group['key']}-solved) |")
    return lines


def resolution_table(rows, dated=False):
    date_heading = " Last checked |" if dated else ""
    date_separator = " --- |" if dated else ""
    lines = [f"| ID | Problem | Status | Outcome |{date_heading} Proof | Review |",
             f"| --- | --- | --- | --- |{date_separator} --- | --- |"]
    for row in sorted(rows, key=lambda row: int(row["id"])):
        title = table_text(row["title"])
        outcome = table_text(row.get("outcome", row["reason"]))
        proof = f"[Proof]({row['proof']})" if row.get("proof") else "—"
        review = f"[Review]({row['review']})" if row.get("review") else "—"
        if row["status"] == "Lean verified":
            review += f" · [Lean evidence]({row['verification_record']})"
        date_cell = f" {row['last_checked']} |" if dated else ""
        lines.append(f"| {row['id']} | [{title}]({row['record']}) | "
                     f"{status_display(row['status'])} | {outcome} |{date_cell} {proof} | {review} |")
    return lines


def render_readme(entries, manifest):
    solved = sum(row.get("status") == "Solved" for row in manifest["retired"])
    claimed = sum(row.get("status") == "Solution claimed" for row in manifest["retired"])
    lean = sum(row["status"] == "Lean verified" for row in manifest["retired"])
    partial = sum(row["status"] == "Partially resolved" for row in entries)
    other = len(manifest["retired"]) - solved - claimed - lean
    summary = (f"**{len(entries)} open targets** ({len(entries) - partial} open, {partial} partial) · "
               f"**{solved} solved entries** · **{lean} Lean verified** · "
               f"**{claimed} solution claim{'s' if claimed != 1 else ''}**")
    if other:
        summary += f" · **{other} other retained entries**"
    lines = [
        "# AIM — Open Applied Problems", "",
        "A sourced collection of precise mathematical research problems in spectral theory, operator theory, applied mathematics, and related fields. Each entry has a self-contained statement, a discussion of applications or mathematical significance, references, and a dated literature-status review.", "",
        "This project is not affiliated with the [American Institute of Mathematics (AIM)](https://aimath.org/).", "",
        "After discussions with mathematicians from different areas, we started this collection with several motivations:", "",
        "- AI tools are increasingly being used to search the literature and tackle conjectures. We would like our community to help shape this work, solve problems and understand their consequences.",
        "- These changes can bring excitement, uncertainty or a sense of loss. We hope this project will create opportunities for mathematicians, especially early-career researchers, to gain recognition for understanding, explaining, improving and extending proofs.",
        "- We want to explore where applications, conceptual insight and asking the right questions fit into mathematical research.",
        "- We want to collect proposed proofs and established solutions in one place, making them easier to find, check and build on.", "",
        "Contributions made with or without AI are welcome.", "",
        "**[AIM, explained](https://mathematics-explained.com/)** is our companion website for explanations of the problems, known results, proofs and applications in this collection. Papers and videos are welcome; you do not need to solve a problem to contribute. The aim is to improve human understanding, with credit to explanation authors and their sources.", "",
        "If a problem here is resolved, we encourage you to improve the proof, explain its ideas, explore its applications, and publish your work. Cite the actual proof and its authors, and cite AIM where you use its curation or research. You are welcome to share your preprint and corrections with the repository so that others can find and build on your contribution.", "",
        summary + ". Counts reflect the statuses recorded in this collection.", "",
        f"**[Browse all {len(entries)} open targets →](CATALOG.md)** · **[Solved and claimed solutions →](RESOLVED.md)**", "",
        "## Browse by subject", "",
        *subject_index(entries, manifest, "CATALOG.md"), "",
    ]
    resolutions = [row for row in manifest["retired"] if row["status"] in SOLVED_STATUSES]
    if resolutions:
        lines += [
            "## Solved problems", "",
            "Complete resolutions recorded in this collection, including counterexamples to the stated conjectures. Follow the proof and review links for the argument and the scope of its review. The [resolution archive](RESOLVED.md) includes review dates and any outstanding claims.", "",
            *resolution_table(resolutions), "",
        ]
    lines += [
        "## Reading the collection", "",
        "Each [problem page](problems/) records its assumptions and quantifiers, an **Application** section, references, a status label, and its last review date. The Application section describes a supported use where one is clear, labels indirect connections, or states that no direct application has been identified. Changing a problem's status to Solved keeps its page and ID in place. Complete deletion closes the gap: subsequent entries and their links are renumbered, and deleted numbers are not reserved. Cite the repository commit alongside an ID because numbering can change.", "",
        "The collection includes foundational questions as well as directly applied ones, with a wide range of difficulty. Related entries may imply one another; the count does not assert logical independence. Further additions exclude numerical linear algebra (NLA).", "",
        "## Problem status", "",
        "The same labels appear on problem pages and index rows. Only Open and Partial count as open targets; each problem counts once.", "",
        "| Status | Meaning | Counted as open? |", "| --- | --- | --- |",
        "| 🔵 OPEN | The target is unresolved in the literature checked for the entry. | Yes |",
        "| 🟡 PARTIAL | Some substantive cases of the stated target are proved; the page identifies what remains. | Yes |",
        "| 🟠 SOLUTION CLAIMED | A source claims a complete resolution; independent proof review is outstanding. | No |",
        "| ✅ SOLVED | A publication or documented independent audit supports a complete resolution. | No |",
        "| 🏆 LEAN VERIFIED | A complete resolution has reviewed Lean kernel-checking evidence and matches the original target. | No |",
        "| ⚪ NEEDS VERIFICATION | A statement or status issue requires further review. | No |",
        "| ⚫ WITHDRAWN | The entry was removed for a documented reason; its ID and original statement are retained. | No |", "",
        "An informal audit, including an AI audit, does not establish Lean verification. Formal proofs of special cases do not settle the whole target. See the [status and evidence requirements](CONTRIBUTING.md#status-and-evidence) and the [resolution archive](RESOLVED.md).", "",
        "## What “open” means here", "",
        "An open target is unresolved in its cited literature, and targeted searches found no later resolution of its exact statement as of the entry's review date. Partial results and restrictions are explained on its page. These bounded checks cannot guarantee that no proof exists, and adding a batch does not revalidate earlier entries.", "",
        "See the [research methodology](research/METHODOLOGY.md), [source maps and exclusion records](research/README.md), and [publication batches](CATALOG.md#publication-batches) for the evidence behind the catalogue.", "",
        "## Contributing", "",
        "Suggestions, references, corrections, and resolution reports are welcome through [GitHub issues](https://github.com/MColbrook/AIM/issues) and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for admission criteria, status updates, and catalogue maintenance. A resolution report should link to the proof or counterexample and explain how it matches the exact target.", "",
        "## Citing this collection", "",
        "If you use this collection, please cite:", "",
        "```bibtex",
        "@misc{aim2026openproblems,",
        "  author = {Brunton, Steve and Colbrook, Matthew J. and de Hoop, Maarten V. and Stepaniants, George and Townsend, Alex and Ward, Rachel},",
        "  title  = {{AIM — Open Applied Problems}},",
        "  year   = {2026},",
        "  url    = {https://github.com/MColbrook/AIM},",
        "  note   = {GitHub repository}",
        "}",
        "```", "",
        "Machine-readable citation metadata is available in [CITATION.cff](CITATION.cff). Include your access date or the commit used when referring to a particular version. For an individual problem, give its ID and the repository commit and cite the original sources listed in the entry as well. When using a solution or explanation, cite its authors and the specific source and revision.", "",
    ]
    return "\n".join(lines)


def render_catalog(entries, manifest):
    lines = [
        "# Open and solved problems", "",
        "[Repository overview](README.md) · [Solved and claimed solutions](RESOLVED.md)", "",
        f"**{len(entries)} open targets**, grouped by subject with solved problems listed immediately below each open list. Open and Partial entries are counted once each; Solved and Lean verified entries count in the Solved column. Every linked page gives the precise statement, an application where one is identified or a note on its mathematical significance, references, known cases, and its own literature-review date. See the [status legend](README.md#problem-status) and the [resolution archive](RESOLVED.md).", "",
        "## Browse by subject", "",
        *subject_index(entries, manifest), "",
        "[Publication batches and review dates](#publication-batches)",
    ]
    for group in manifest["groups"]:
        title = group["title"]
        lines += ["", f"## {title}", "", f'<a name="{group["key"]}-open"></a>', "",
                  "### Open problems", "", "| ID | Problem | Status | Area |", "| --- | --- | --- | --- |"]
        for row in entries:
            if row["group"] == group["key"]:
                title_text = table_text(row["title"])
                area = table_text(row["area"])
                lines.append(f"| {row['id']} | [{title_text}]({row['file']}) | {status_display(row['status'])} | {area} |")
        retained = [row for row in manifest["retired"] if row["group"] == group["key"]]
        solved = [row for row in retained if row["status"] in SOLVED_STATUSES]
        lines += ["", f'<a name="{group["key"]}-solved"></a>', "", "### Solved problems", ""]
        lines += resolution_table(solved) if solved else ["No solved problems are currently recorded in this subject."]
        for status in ("Solution claimed", "Needs verification", "Withdrawn"):
            rows = [row for row in retained if row["status"] == status]
            if rows:
                lines += ["", f"### {status}", "", *resolution_table(rows)]
    lines += ["", "## Publication batches", "",
              "Adding a batch does not revalidate earlier entries. Counts below include only currently open targets; retired IDs retain their original batch membership.", "",
              "| Publication batch | Open targets | Entry review dates |", "| --- | ---: | --- |"]
    for batch in manifest["batches"]:
        rows = [row for row in entries if row["id"] in batch["ids"]]
        dates = sorted({row["last_checked"] for row in rows})
        date_text = (dates[0] if len(dates) == 1 else f"{dates[0]}–{dates[-1]}") if dates else "—"
        lines.append(f"| {batch['title']} | {len(rows)} | {date_text} |")
    lines += ["", "## Maintaining the collection", "",
              "This index, [README.md](README.md), and [RESOLVED.md](RESOLVED.md) are generated from [catalogue.json](catalogue.json) and [data/](data/). Run `python3 scripts/catalogue.py --write` after metadata changes, then `python3 scripts/catalogue.py --check`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.", ""]
    return "\n".join(lines)


def render_resolved(manifest):
    lines = [
        "# Solved and claimed solutions", "",
        "[Repository overview](README.md) · [Browse open targets](CATALOG.md)", "",
        "This archive lists previously admitted targets that are no longer counted as open. A solution claim is not a verified solution. Each linked record preserves the original statement, current ID, sources, review date, and the scope of the review actually performed.", "",
    ]
    sections = (
        ("Solved", "Documented resolutions of the exact target. Proof and review links give the argument and the kind of review performed; the problem link preserves the original statement and full status record."),
        ("Lean verified", "Complete resolutions with a reviewed Lean proof, statement comparison, and reproducible kernel-checking evidence. The evidence link records exactly what was checked."),
        ("Solution claimed", "A matching complete resolution has been announced, but independent proof review remains outstanding."),
        ("Needs verification", "Entries held for a material statement or status issue. This status does not assert a solution."),
        ("Withdrawn", "Entries removed for a documented reason, with their original statements and IDs retained. Withdrawal does not imply a solution."),
    )
    for status, description in sections:
        rows = sorted((row for row in manifest["retired"] if row["status"] == status),
                      key=lambda row: int(row["id"]))
        if not rows:
            continue
        lines += [f"## {status}", "", description, "", *resolution_table(rows, dated=True), ""]
    lines += [
        "## Reporting a solution", "",
        "Open a [GitHub issue](https://github.com/MColbrook/AIM/issues) or pull request with the problem ID, a direct proof or counterexample reference, and a comparison with the entry's assumptions and conclusion. State whether the result is a claim, a published result, or an independently reviewed argument, and identify the review evidence. See [CONTRIBUTING.md](CONTRIBUTING.md#reporting-a-resolution) for how to update the record and index.", "",
        "Candidates excluded before admission are documented in the [research records](research/README.md); they are not counted as resolved catalogue entries. This list is generated from solved problem metadata in `data/` and the `retired` records in [catalogue.json](catalogue.json).", "",
    ]
    return "\n".join(lines)


def validate_page(row, path):
    errors = []
    content = path.read_text(encoding="utf-8")
    first = content.splitlines()[0] if content else ""
    if not re.match(rf"^# {row['id']}(?:\.|\s+[—–-])\s+", first):
        errors.append(f"{row['id']}: incorrect heading ID")
    if row["title"] not in first:
        errors.append(f"{row['id']}: heading title differs from metadata")
    for section in SECTIONS:
        match = re.search(rf"^## {re.escape(section)}[ \t]*\n(.*?)(?=^## |\Z)",
                          content, re.MULTILINE | re.DOTALL)
        if not match:
            errors.append(f"{row['id']}: missing {section}")
        elif section == "Application":
            application = re.sub(r"<!--.*?-->", "", match[1], flags=re.DOTALL).strip()
            plain = application.strip("*_` .\n\t").lower()
            if not plain or re.fullmatch(r"(?:todo|tbd|n/?a|none|coming soon)[.!]?", plain):
                errors.append(f"{row['id']}: empty or placeholder Application")
    fields = (("Last checked", row["last_checked"]), ("Status", status_display(row["status"])))
    if "area" in row:
        fields += (("Area", row["area"]),)
    elif not re.search(r"^\*\*Area:\*\*[ \t]*\S.+$", content, re.MULTILINE):
        errors.append(f"{row['id']}: missing Area")
    for field, value in fields:
        matches = re.findall(rf"^\*\*{field}:\*\*[ \t]*(.+?)[ \t]*$", content, re.MULTILINE)
        consistent = (len(matches) == 1 and
                      (matches[0] == value if field == "Status" else matches[0].rstrip(".") == value.rstrip(".")))
        if not consistent:
            errors.append(f"{row['id']}: missing or inconsistent {field}")
    header = re.split(r"^## ", content, maxsplit=1, flags=re.MULTILINE)[0]
    if not re.search(r"^\*\*Status:\*\*", header, re.MULTILINE):
        errors.append(f"{row['id']}: Status must appear before the first section")
    if row["status"] == "Partially resolved":
        review = re.search(r"^## Status review[ \t]*\n(.*?)(?=^## |\Z)",
                           content, re.MULTILINE | re.DOTALL)
        for field in ("Known cases", "Remaining target"):
            if not review or not re.search(rf"^\*\*{field}:\*\*[ \t]*\S.+$", review[1], re.MULTILINE):
                errors.append(f"{row['id']}: Partial requires {field} in Status review")
    if len(re.findall(r"\]\(https?://", content)) < 1:
        errors.append(f"{row['id']}: no linked external reference")
    return errors


def validate(entries, manifest, documents=None):
    errors = []
    ids = [row["id"] for row in entries]
    retired = [row["id"] for row in manifest["retired"]]
    issued = ids + retired
    if len(set(issued)) != len(issued):
        errors.append("Duplicate ID in active or retired records")
    if not issued or set(issued) != {f"{i:03d}" for i in range(1, max(map(int, issued), default=0) + 1)}:
        errors.append("IDs must be consecutive across active and retired records; renumber after deletion")
    if set(ids) != {f"{i:03d}" for i in range(1, len(ids) + 1)}:
        errors.append("Active problem IDs must be consecutive from 001 with no gaps")
    batched = [identifier for batch in manifest["batches"] for identifier in batch["ids"]]
    if len(set(batched)) != len(batched) or set(batched) != set(issued):
        errors.append("Publication batches must partition all active and retired IDs exactly once")
    for key in ("title", "file"):
        values = [row[key] for row in entries]
        if len(set(values)) != len(values):
            errors.append(f"Duplicate {key} in metadata")
    indexed = set()
    for row in entries:
        path = ROOT / row["file"]
        if (path.parent != ROOT / "problems" or path.suffix != ".md" or
                path.is_symlink() or not path.name.startswith(row["id"] + "-")):
            errors.append(f"{row['id']}: invalid problem path")
            continue
        indexed.add(path)
        if not path.is_file():
            errors.append(f"Missing {row['file']}")
            continue
        errors.extend(validate_page(row, path))
    for row in manifest["retired"]:
        errors.extend(validate_page(row, ROOT / row["record"]))
    actual = set((ROOT / "problems").glob("*.md"))
    for extra in sorted(actual - indexed):
        errors.append(f"Unindexed problem file: {extra.relative_to(ROOT)}")
    generated = {ROOT / name: content for name, content in (documents or {}).items()}
    markdown = {path: path.read_text(encoding="utf-8") for path in markdown_paths(ROOT)
                if path not in generated}
    markdown.update(generated)
    for path, content in markdown.items():
        errors.extend(f"{path.relative_to(ROOT).as_posix()}: {error}" for error in validate_math(content))
        for target in re.findall(r"\]\(([^)\s]+)\)", content):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target_path).resolve()
            if target_path and not resolved.exists() and resolved not in generated:
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="rebuild README, open catalogue and resolution archive after validation")
    mode.add_argument("--check", action="store_true", help="check content and freshness of all generated documents")
    args = parser.parse_args()
    manifest, errors = load_manifest()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    entries, errors = load_entries(manifest)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    open_entries, display_manifest = presentation_records(entries, manifest)
    documents = dict(zip(GENERATED_DOCUMENTS, (
        render_readme(open_entries, display_manifest), render_catalog(open_entries, display_manifest),
        render_resolved(display_manifest))))
    errors.extend(validate(entries, manifest, documents))
    if args.check:
        for name, content in documents.items():
            path = ROOT / name
            if not path.is_file():
                errors.append(f"{name} is missing; run python3 scripts/catalogue.py --write")
            elif path.read_text(encoding="utf-8") != content:
                errors.append(f"{name} is stale; run python3 scripts/catalogue.py --write")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    if args.write:
        for name, content in documents.items():
            (ROOT / name).write_text(content, encoding="utf-8")
        print(f"Wrote {', '.join(documents)} with {len(open_entries)} open targets and {len(display_manifest['retired'])} retained entries.")
    else:
        print(f"Validated {len(entries)} unique problems, metadata, required sections, math delimiters, local links, and freshness of {', '.join(documents)}.")


if __name__ == "__main__":
    main()
