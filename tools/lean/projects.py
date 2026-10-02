#!/usr/bin/env python3
"""Discover AIM Lean projects and select only affected projects for CI."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess


PROJECT_ROOT = PurePosixPath("research/lean")


def registered_projects(documents: dict[str, object]) -> list[dict[str, str]]:
    """Use the catalogue's existing active pages and archived records as the registry."""
    catalogue = documents.get("catalogue.json")
    if not isinstance(catalogue, dict) or not isinstance(catalogue.get("retired"), list):
        raise ValueError("catalogue.json must contain a retired array")
    registry: dict[str, str] = {}

    def register(row: object, field: str, prefix: str, source: str) -> None:
        if not isinstance(row, dict):
            raise ValueError(f"Invalid catalogue entry in {source}")
        problem_id = row.get("id")
        if (not isinstance(problem_id, str) or not re.fullmatch(r"[0-9]{3,}", problem_id)
                or int(problem_id) <= 0 or problem_id != f"{int(problem_id):03d}"):
            raise ValueError(f"Invalid AIM problem ID in {source}: {problem_id!r}")
        canonical = row.get(field)
        if not isinstance(canonical, str):
            raise ValueError(f"Missing canonical {field} for {problem_id} in {source}")
        path = PurePosixPath(canonical)
        if (path.is_absolute() or ".." in path.parts or "\\" in canonical
                or path.as_posix() != canonical or path.suffix != ".md"
                or not canonical.startswith(prefix + "/")):
            raise ValueError(f"Invalid canonical path for {problem_id}: {canonical!r}")
        if problem_id in registry:
            raise ValueError(f"Duplicate AIM problem ID: {problem_id}")
        registry[problem_id] = canonical

    for source, rows in sorted(documents.items()):
        path = PurePosixPath(source)
        if path.parent != PurePosixPath("data") or path.suffix != ".json":
            continue
        if not isinstance(rows, list):
            raise ValueError(f"{source} must contain an array of problem entries")
        for row in rows:
            register(row, "file", "problems", source)
    for row in catalogue["retired"]:
        register(row, "record", "research", "catalogue.json")
    return [{"id": problem_id, "project": (PROJECT_ROOT / problem_id).as_posix(),
             "canonical": canonical}
            for problem_id, canonical in sorted(registry.items(), key=lambda item: int(item[0]))]


def discover(root: Path) -> list[dict[str, str]]:
    documents = {"catalogue.json": json.loads((root / "catalogue.json").read_text())}
    documents.update({path.relative_to(root).as_posix(): json.loads(path.read_text())
                      for path in sorted((root / "data").glob("*.json"))})
    registered = {entry["id"]: entry for entry in registered_projects(documents)}
    # Checking each ancestor prevents a symlinked research/lean (or research)
    # directory from redirecting project discovery outside the checkout.
    for relative in (PurePosixPath("research"), PROJECT_ROOT):
        path = root / relative
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise ValueError(f"Lean project parent must be an ordinary directory: {relative}")
    parent = root / PROJECT_ROOT
    if not parent.exists():
        return []
    result = []
    for project in sorted(parent.iterdir()):
        # A README may accompany projects, but every directory (including a
        # source-only draft) must have a valid, registered AIM problem ID.
        if project.is_symlink():
            raise ValueError(f"Lean project must be an ordinary directory: {project.relative_to(root)}")
        if not project.is_dir():
            if project.name in registered:
                raise ValueError(f"Lean project must be an ordinary directory: {project.relative_to(root)}")
            continue
        if project.name not in registered:
            raise ValueError(f"Unregistered AIM Lean project: {project.relative_to(root)}")
        result.append(registered[project.name])
    return sorted(result, key=lambda entry: int(entry["id"]))


def discover_at_ref(root: Path, ref: str) -> list[dict[str, str]]:
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", "-z", ref],
        cwd=root, text=True).split("\0")
    candidates = {PurePosixPath(path).parts[2] for path in paths
                  if path.startswith(PROJECT_ROOT.as_posix() + "/")
                  and len(PurePosixPath(path).parts) >= 4}
    # A base predating Lean infrastructure need not have any catalogue format
    # understood by this checker. There can be no removed project in that case.
    if not candidates:
        return []
    sources = ["catalogue.json", *[path for path in paths
               if PurePosixPath(path).parent == PurePosixPath("data")
               and path.endswith(".json")]]
    documents = {path: json.loads(subprocess.check_output(
        ["git", "show", f"{ref}:{path}"], cwd=root, text=True)) for path in sources}
    registered = {entry["id"]: entry for entry in registered_projects(documents)}
    unknown = candidates - registered.keys()
    if unknown:
        raise ValueError("Unregistered AIM Lean projects at base ref: " + ", ".join(sorted(unknown)))
    return [registered[problem_id] for problem_id in sorted(candidates, key=int)]


def require_retained_projects(projects: list[dict[str, str]],
                              base_projects: list[dict[str, str]]) -> None:
    current_paths = {entry["project"] for entry in projects}
    missing = [entry["project"] for entry in base_projects
               if entry["project"] not in current_paths]
    if missing:
        raise ValueError("Registered Lean projects removed or renamed; verification cannot "
                         "be skipped: " + ", ".join(missing))


def select(projects: list[dict[str, str]], changed: list[str]) -> list[dict[str, str]]:
    shared = ("tools/lean/", "docs/lean/schema/")
    if any(path in ("catalogue.json", ".github/workflows/lean-verification.yml")
           or any(path.startswith(prefix) for prefix in shared)
           or (PurePosixPath(path).parent == PurePosixPath("data") and path.endswith(".json"))
           for path in changed):
        return projects
    return [entry for entry in projects if any(
        path == entry["canonical"] or path == entry["project"]
        or path.startswith(entry["project"] + "/") for path in changed)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true")
    group.add_argument("--base-ref")
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()
    projects = discover(args.root)
    if not args.all:
        require_retained_projects(projects, discover_at_ref(args.root, args.base_ref))
        changed = subprocess.check_output(
            ["git", "diff", "--name-only", "--no-renames", "-z", args.base_ref, "HEAD", "--"],
            cwd=args.root, text=True).split("\0")
        projects = select(projects, changed)
    matrix = [{"id": entry["id"], "project": entry["project"]} for entry in projects]
    encoded = json.dumps({"include": matrix}, separators=(",", ":"))
    print(encoded)
    if args.github_output:
        with args.github_output.open("a") as stream:
            stream.write(f"matrix={encoded}\ncount={len(projects)}\n")


if __name__ == "__main__":
    main()
