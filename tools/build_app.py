#!/usr/bin/env python3
"""Generate the unified offline literature app and compatibility entry pages."""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote

BASE = Path(__file__).resolve().parents[1]
REPO_ROOT = BASE.parents[2]
CATALOG = BASE / "catalog"
TEMPLATE = Path(__file__).with_name("app-template.html")


def normalized(value: str) -> str:
    import unicodedata
    value = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", " ", "".join(c for c in value if not unicodedata.combining(c))).strip()


def inline(value: str) -> str:
    value = html.escape(value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    return value


def markdown(value: str) -> str:
    out = []
    list_type = None
    in_code = False
    in_refs = False
    for raw in value.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            if list_type:
                out.append(f"</{list_type}>")
                list_type = None
            out.append("</pre>" if in_code else "<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(raw) + "\n")
            continue
        if not line:
            if list_type:
                out.append(f"</{list_type}>")
                list_type = None
            continue
        if line.startswith("# "):
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("## "):
            if in_refs:
                out.append("</details>")
                in_refs = False
            if line == "## References":
                out.append("<details class='reference-details'><summary>Complete references</summary>")
                in_refs = True
            else:
                out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("- ") or re.match(r"^\d+\. ", line):
            kind = "ul" if line.startswith("- ") else "ol"
            if list_type != kind:
                if list_type:
                    out.append(f"</{list_type}>")
                out.append(f"<{kind}>")
                list_type = kind
            content = line[2:] if kind == "ul" else re.sub(r"^\d+\. ", "", line)
            out.append(f"<li>{inline(content)}</li>")
        else:
            if list_type:
                out.append(f"</{list_type}>")
                list_type = None
            out.append(f"<p>{inline(line)}</p>")
    if list_type:
        out.append(f"</{list_type}>")
    if in_refs:
        out.append("</details>")
    return "\n".join(out)


def legacy_map(assets: list[dict]) -> dict[str, str]:
    path = BASE / "reports" / "asd-ste100" / "REPORT_INDEX.md"
    if not path.exists():
        return {}
    by_title = {}
    for asset in assets:
        by_title.setdefault(normalized(asset["title_guess"]), asset["asset_id"])
    mapping = {}
    for title, slug in re.findall(r"\|\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*\|", path.read_text()):
        asset_id = by_title.get(normalized(title))
        if asset_id:
            mapping[Path(slug).stem] = asset_id
    return mapping


def build() -> str:
    data = json.loads((CATALOG / "index.json").read_text())
    refs = json.loads((CATALOG / "references.json").read_text())
    audit = json.loads((CATALOG / "audit.json").read_text())
    classified_path = BASE / "paper-classifications" / "papers.json"
    classified = json.loads(classified_path.read_text()) if classified_path.exists() else {"papers": []}
    reports = {}
    for asset in data["assets"]:
        report_path = Path(asset["report_path"])
        path = BASE / Path(*report_path.parts[1:])
        if path.exists():
            reports[asset["asset_id"]] = markdown(path.read_text(encoding="utf-8"))
        asset["pdf_href"] = quote("../../../" + Path(asset["path"]).as_posix(), safe="/")
    for work in data["works"]:
        if work.get("pdf_href"):
            work["pdf_href"] = "../../../literature/" + work["pdf_href"]
    payload = {
        "index": data, "references": refs["references"], "audit": audit,
        "reports": reports,
        "classifications": {p["id"]: p for p in classified["papers"]},
        "legacyMap": legacy_map(data["assets"]),
    }
    embedded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return TEMPLATE.read_text(encoding="utf-8").replace("__LITERATURE_DATA__", embedded)


def wrapper(target: str, title: str) -> str:
    return ("<!doctype html><html lang='en'><meta charset='utf-8'>"
            f"<title>{html.escape(title)}</title><script>location.replace({json.dumps(target)});</script>"
            f"<p><a href='{html.escape(target, quote=True)}'>Open the {html.escape(title)}</a></p></html>\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = build()
    path = BASE / "index.html"
    if args.check:
        if not path.exists() or path.read_text() != output:
            raise SystemExit("Offline app is out of date")
        print("Offline app is current")
        return
    report_viewer = BASE / "reports" / "asd-ste100" / "index.html"
    legacy_viewer = report_viewer.with_name("legacy.html")
    if report_viewer.exists() and not legacy_viewer.exists():
        shutil.copy2(report_viewer, legacy_viewer)
    path.write_text(output, encoding="utf-8")
    (BASE / "paper-publications.html").write_text(wrapper("index.html#view=graph", "citation graph"), encoding="utf-8")
    (BASE / "paper-classifications" / "index.html").write_text(wrapper("../index.html#view=classifications", "classifications"), encoding="utf-8")
    report_viewer.write_text(wrapper("../../index.html#view=reports", "reports"), encoding="utf-8")
    print(f"Built {path} with {len(json.loads((CATALOG / 'index.json').read_text())['assets'])} PDFs")


if __name__ == "__main__":
    main()
