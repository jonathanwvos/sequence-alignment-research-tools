#!/usr/bin/env python3
"""Refresh report reference sections from the reviewed central catalog.

The source-grounded prose above the References heading is preserved verbatim.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from draft_reports import CATALOG, FIELDS, REPORTS, render


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    index = json.loads((CATALOG / "index.json").read_text(encoding="utf-8"))
    works = {work["id"]: work for work in index["works"]}
    refs = defaultdict(list)
    for ref in json.loads((CATALOG / "references.json").read_text(encoding="utf-8"))["references"]:
        refs[ref["citing_asset_id"]].append(ref)
    changed = 0
    missing = []
    marker = "## References\n"
    for asset in index["assets"]:
        path = REPORTS / f"{asset['asset_id']}.md"
        if not path.exists():
            missing.append(asset["asset_id"])
            continue
        current = path.read_text(encoding="utf-8")
        if current.count(marker) != 1:
            raise ValueError(f"Expected exactly one References heading: {path}")
        empty_claims = {key: [] for key, _ in FIELDS}
        section = marker + render(asset, works[asset["work_id"]], empty_claims, refs[asset["asset_id"]]).split(marker, 1)[1]
        refreshed = current.split(marker, 1)[0] + section
        refreshed = re.sub(
            r"(?m)^- Work ID: `[^`]+`$",
            f"- Work ID: `{asset['work_id']}`",
            refreshed,
            count=1,
        )
        if current != refreshed:
            changed += 1
            if not args.check:
                path.write_text(refreshed, encoding="utf-8")
    if missing:
        raise SystemExit(f"Missing reports: {len(missing)} ({', '.join(missing[:6])})")
    if args.check and changed:
        raise SystemExit(f"Outdated reference sections: {changed}")
    print(f"Reference sections current for {len(index['assets'])} reports; updated {changed}")


if __name__ == "__main__":
    main()
