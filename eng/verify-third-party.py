#!/usr/bin/env python3
"""Verify the third-party source snapshot inventory using only the Python standard library."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root (defaults to the parent of eng/)")
    parser.add_argument("--manifest", type=Path, default=None,
                        help="manifest path (defaults to dotnet/third_party/THIRD_PARTY_MANIFEST.json)")
    parser.add_argument("--readme", type=Path, default=None,
                        help="README path (defaults to dotnet/third_party/README.md)")
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_path = (args.manifest or root / "dotnet/third_party/THIRD_PARTY_MANIFEST.json").resolve()
    readme_path = (args.readme or root / "dotnet/third_party/README.md").resolve()
    errors: list[str] = []

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read manifest {manifest_path}: {exc}", file=sys.stderr)
        return 2

    entries = manifest.get("entries")
    if not isinstance(entries, list) or not entries:
        print("ERROR: manifest.entries must be a non-empty array", file=sys.stderr)
        return 2

    directories = [entry.get("directory") for entry in entries]
    paths = [entry.get("path") for entry in entries]
    if len(directories) != len(set(directories)):
        errors.append("manifest contains duplicate directory names")
    if len(paths) != len(set(paths)):
        errors.append("manifest contains duplicate paths")

    for entry in entries:
        directory = entry.get("directory", "<missing>")
        relative_path = entry.get("path")
        if not isinstance(relative_path, str) or not relative_path:
            errors.append(f"{directory}: missing path")
            continue
        if not (root / relative_path).is_dir():
            errors.append(f"{directory}: expected directory does not exist: {relative_path}")
        if entry.get("priority") not in {"P0", "P1"}:
            errors.append(f"{directory}: priority must be P0 or P1")
        upstream = entry.get("upstream", "")
        if not isinstance(upstream, str) or not upstream.startswith("https://"):
            errors.append(f"{directory}: upstream must be an https URL")
        if entry.get("upstream_commit") != "unknown":
            errors.append(f"{directory}: upstream_commit must remain 'unknown' until verified")
        if entry.get("build_status") != "not_verified":
            errors.append(f"{directory}: build_status must not imply an unperformed build")

    try:
        readme = readme_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read README {readme_path}: {exc}")
        readme = ""

    readme_entries = []
    for line in readme.splitlines():
        cells = line.split("|")
        if len(cells) < 2:
            continue
        cell = cells[1].strip()
        if len(cell) >= 2 and cell.startswith("`") and cell.endswith("`"):
            readme_entries.append(cell[1:-1])

    if readme_entries != directories:
        errors.append(
            "README directory table does not match manifest order/content "
            f"(README={readme_entries!r}, manifest={directories!r})"
        )

    if "pytorch" in directories or "`pytorch`" in readme:
        errors.append("removed PyTorch snapshot must not appear in the current directory inventory")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        print(f"Third-party inventory verification failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1

    print(
        f"Third-party inventory OK: {len(entries)} directories, "
        f"{sum(entry['priority'] == 'P0' for entry in entries)} P0, "
        f"{sum(entry['priority'] == 'P1' for entry in entries)} P1."
    )
    print("README inventory matches manifest; no upstream revisions or build results were fabricated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
