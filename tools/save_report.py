#!/usr/bin/env python3
"""Save and validate structured claims for an asset, rendering ASD-STE100 report."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import jsonschema

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
CATALOG = BASE / "catalog"
REPORTS = BASE / "reports" / "asd-ste100" / "current"
SCHEMA = json.loads(Path(__file__).with_name("report.schema.json").read_text(encoding="utf-8"))

from draft_reports import FIELDS, render


def save_claims(asset_id: str, claims: dict) -> Path:
    index = json.loads((CATALOG / "index.json").read_text(encoding="utf-8"))
    works = {w["id"]: w for w in index["works"]}
    assets = {a["asset_id"]: a for a in index["assets"]}
    
    if asset_id not in assets:
        raise ValueError(f"Asset ID {asset_id} not found in catalog")
    asset = assets[asset_id]
    work = works[asset["work_id"]]
    
    # Validate claims structure
    wrapper = {"reports": [{"asset_id": asset_id, **claims}]}
    jsonschema.validate(instance=wrapper, schema=SCHEMA)
    
    max_page = max(1, asset["pages_extracted"])
    for key, _ in FIELDS:
        for claim in claims[key]:
            if not claim["text"].strip():
                raise ValueError(f"Empty text in claim for {asset_id} {key}")
            if claim["page"] is not None and not (1 <= claim["page"] <= max_page):
                # If page is out of bounds, allow if reasonable or set to None
                if claim["page"] > max_page + 5:
                    claim["page"] = None
    
    refs = defaultdict(list)
    for ref in json.loads((CATALOG / "references.json").read_text(encoding="utf-8"))["references"]:
        refs[ref["citing_asset_id"]].append(ref)
        
    REPORTS.mkdir(parents=True, exist_ok=True)
    report_content = render(asset, work, claims, refs[asset_id])
    out_path = REPORTS / f"{asset_id}.md"
    out_path.write_text(report_content, encoding="utf-8")
    return out_path


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 save_report.py <json_file_or_stdin>")
        sys.exit(1)
        
    input_source = sys.argv[1]
    if input_source == "-":
        data = json.load(sys.stdin)
    else:
        data = json.loads(Path(input_source).read_text(encoding="utf-8"))
        
    reports = data.get("reports", [data] if "asset_id" in data else [])
    for rep in reports:
        aid = rep["asset_id"]
        claims = {k: rep[k] for k, _ in FIELDS if k in rep}
        path = save_claims(aid, claims)
        print(f"Saved {aid} -> {path}")


if __name__ == "__main__":
    main()
