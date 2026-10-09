#!/usr/bin/env python3
"""Build the PDF-faithful, offline manuscript citation review viewer."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
LITERATURE = REPO / "literature"
DOCS = REPO / "docs" / "Literature Review"
PDF = DOCS / "VALA Literature Review Manuscript - Draft 3.pdf"
TEX = DOCS / "VALA Literature Review Manuscript - Draft 3.tex"
REFERENCES = DOCS / "Nature Vancouver References.md"
CATALOG = LITERATURE / "catalog" / "index.json"
REPORTS = LITERATURE / "reports" / "asd-ste100" / "current"
PAGES = HERE / "pages"
TEMPLATE = HERE / "template.html"
OUTPUT = HERE / "index.html"
DOI = re.compile(r"10\.\d{4,9}/[^\s<>{}]+", re.I)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(value: str) -> str:
    import unicodedata

    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def doi(value: str) -> str | None:
    match = DOI.search(value.replace(r"\_", "_"))
    return match.group().rstrip(".,;:)]}").lower() if match else None


def plain_tex(value: str) -> str:
    value = re.sub(r"\\url\{([^}]*)\}", r"\1", value)
    value = re.sub(r"\\(?:textbf|emph|textit)\{([^}]*)\}", r"\1", value)
    return value.replace(r"\_", "_").replace(r"\&", "&").strip()


def manuscript_bibliography() -> list[dict]:
    text = TEX.read_text(encoding="utf-8")
    section = text.split(r"\begin{thebibliography}", 1)[1].split(r"\end{thebibliography}", 1)[0]
    entries = []
    for match in re.finditer(r"\\bibitem\{ref(\d+)\}\s*(.*?)(?=\n\\bibitem|\Z)", section, re.S):
        citation = plain_tex(match.group(2).strip())
        entries.append({"pdf_number": len(entries) + 1, "tex_key": f"ref{match.group(1)}",
                        "citation": citation, "doi": doi(citation)})
    if not entries:
        raise ValueError("No manuscript bibliography entries found")
    return entries


def current_references() -> list[dict]:
    entries = []
    for line in REFERENCES.read_text(encoding="utf-8").splitlines():
        match = re.match(r'^(\d+)\. <a id="ref-\1"></a>(.*)$', line)
        if match:
            citation = match.group(2).strip()
            entries.append({"number": int(match.group(1)), "citation": citation, "doi": doi(citation)})
    if [entry["number"] for entry in entries] != list(range(1, len(entries) + 1)):
        raise ValueError("The current reference list is not consecutively numbered")
    return entries


def report_excerpt(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"(?m)^##\s+", text)
    wanted = {"Executive summary", "Methods", "Results", "Limitations and uncertainty"}
    output = []
    for section in sections[1:]:
        heading, _, body = section.partition("\n")
        if heading.strip() not in wanted:
            continue
        bullets = [line[2:].strip() for line in body.splitlines() if line.startswith("- ")]
        if bullets:
            output.append(f"<strong>{html.escape(heading.strip())}</strong>")
            output.extend(f"<p>{html.escape(item[:400])}</p>" for item in bullets[:2])
    return "".join(output)


def report_status(path: Path) -> str:
    match = re.search(r"(?m)^- ASD-STE100 Issue 9 review: \*\*(.*?)\*\*", path.read_text(encoding="utf-8"))
    return match.group(1) if match else "Review status not recorded"


def report_for_work(work: dict, assets: dict[str, dict], preferred_asset: str | None = None) -> dict | None:
    asset_ids = [preferred_asset] if preferred_asset else work["assets"]
    asset_id = next((item for item in asset_ids if item and (REPORTS / f"{item}.md").is_file()), None)
    if not asset_id:
        return None
    path = REPORTS / f"{asset_id}.md"
    return {
        "work_id": work["id"], "asset_id": asset_id, "title": work["title"],
        "excerpt_html": report_excerpt(path), "review_status": report_status(path),
        "pdf_href": "../../../../" + assets[asset_id]["path"],
    }


def match_report(reference: dict, works: list[dict], assets: dict[str, dict]) -> dict | None:
    known_asset = {
        154: "a-7f604cc5311c46ba",
        159: "a-0818806107a7d267",
        252: "a-d866b896a05eac3c",
    }.get(reference["number"])
    if known_asset:
        work = next(work for work in works if known_asset in work["assets"])
        return report_for_work(work, assets, known_asset)
    candidates = []
    for work in works:
        if not work["assets"]:
            continue
        if reference["doi"] and reference["doi"] == work.get("doi"):
            candidates.append((1.0, work))
            continue
        citation = normalized(reference["citation"])
        title = normalized(work["title"])
        if len(title) >= 20 and title in citation:
            candidates.append((0.95, work))
        else:
            score = SequenceMatcher(None, title, citation).ratio()
            if score > 0.6:
                candidates.append((score, work))
    if not candidates:
        return None
    score, work = max(candidates, key=lambda item: item[0])
    if score < 0.78:
        return None
    return report_for_work(work, assets)


def bibliography_payload() -> list[dict]:
    entries = current_references()
    works_data = json.loads(CATALOG.read_text(encoding="utf-8"))
    assets = {asset["asset_id"]: asset for asset in works_data["assets"]}
    for entry in entries:
        entry["report"] = match_report(entry, works_data["works"], assets)
    assigned = set()
    for item in manuscript_bibliography():
        exact = [entry for entry in entries
                 if normalized(entry["citation"]) == normalized(item["citation"])]
        doi_matches = [entry for entry in entries if item["doi"] and entry["doi"] == item["doi"]]
        candidates = exact if len(exact) == 1 else doi_matches
        if len(candidates) != 1 or candidates[0]["number"] in assigned:
            raise ValueError(f"Could not uniquely match PDF bibliography item {item['pdf_number']}")
        current = candidates[0]
        assigned.add(current["number"])
        item["current_number"] = current["number"]
        same_text = normalized(item["citation"]) == normalized(current["citation"])
        item["status"] = (
            "DOI conflict" if item["doi"] and current["doi"] and item["doi"] != current["doi"]
            else "Same DOI and text" if item["doi"] and item["doi"] == current["doi"] and same_text
            else "Same DOI; bibliography text differs" if item["doi"] and item["doi"] == current["doi"]
            else "Text matches; DOI unverified" if same_text
            else "Check bibliography text"
        )
        current["pdf_source"] = item
    return entries


def corpus_payload(references: list[dict]) -> list[dict]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    assets = {asset["asset_id"]: asset for asset in catalog["assets"]}
    by_work = {ref["report"]["work_id"]: ref["number"] for ref in references if ref["report"]}
    by_doi: dict[str, list[int]] = {}
    for ref in references:
        if ref["doi"]:
            by_doi.setdefault(ref["doi"], []).append(ref["number"])
    output = []
    for work in catalog["works"]:
        number = by_work.get(work["id"])
        if number is None and work.get("doi") and len(by_doi.get(work["doi"], [])) == 1:
            number = by_doi[work["doi"]][0]
        if number is None:
            title = normalized(work["title"])
            matches = [ref["number"] for ref in references
                       if len(title) >= 20 and title in normalized(ref["citation"])]
            if len(matches) == 1:
                number = matches[0]
        output.append({
            "id": work["id"], "title": work["title"], "authors": work.get("authors"),
            "year": work.get("year"), "doi": work.get("doi"),
            "reference_number": number, "has_local_pdf": bool(work["assets"]),
            "report": report_for_work(work, assets) if number is None else None,
        })
    return output


def pdf_text() -> list[dict]:
    bibliography_count = len(manuscript_bibliography())
    with tempfile.TemporaryDirectory(prefix="vala-paper-review-") as temp:
        prefix = Path(temp) / "paper"
        subprocess.run(
            ["pdftohtml", "-xml", "-i", "-hidden", str(PDF), str(prefix)],
            check=True, capture_output=True, text=True,
        )
        root = ET.parse(prefix.with_suffix(".xml")).getroot()
    pages = []
    for page in root.findall("page"):
        number = int(page.attrib["number"])
        lines = []
        for node in page.findall("text"):
            text = "".join(node.itertext()).strip()
            if not text:
                continue
            anchor = node.find("a")
            top, left = int(node.attrib["top"]), int(node.attrib["left"])
            width, height = int(node.attrib["width"]), int(node.attrib["height"])
            linked_number = (
                anchor is not None
                and anchor.get("href", "").startswith("paper.html#")
                and re.fullmatch(r"\d+(?:\s+\d+)*", text) is not None
            )
            numbers = list(re.finditer(r"\d+", text)) if linked_number else []
            if len(numbers) > 1 and all(1 <= int(part.group()) <= bibliography_count for part in numbers):
                # pdftohtml can merge adjacent superscripts (for example, "4 5")
                # into one linked text node. Keep separate hit boxes and source targets.
                for part in numbers:
                    lines.append({
                        "text": part.group(), "top": top,
                        "left": left + round(width * part.start() / len(text)),
                        "width": max(1, round(width * len(part.group()) / len(text))),
                        "height": height, "citation": int(part.group()),
                    })
                continue
            citation = (
                int(text) if linked_number and text.isdigit()
                and 1 <= int(text) <= bibliography_count
                else None
            )
            lines.append({
                "text": text, "top": top, "left": left,
                "width": width, "height": height,
                "citation": citation,
            })
        pages.append({"number": number, "width": int(page.attrib["width"]),
                      "height": int(page.attrib["height"]), "lines": lines})
    return pages


def link_source_citations(pages: list[dict]) -> None:
    by_key = {entry["tex_key"]: entry["pdf_number"] for entry in manuscript_bibliography()}
    body = TEX.read_text(encoding="utf-8").split(r"\begin{thebibliography}", 1)[0]
    source = []
    for match in re.finditer(r"\\draftcite\{(\d+)\}", body):
        key = f"ref{match.group(1)}"
        if key in by_key:
            source.append((by_key[key], match, key))
    rendered = [line for page in pages for line in page["lines"] if line["citation"] is not None]
    if len(source) != len(rendered) or any(number != line["citation"] for
                                           (number, _, _), line in zip(source, rendered)):
        raise ValueError("Rendered citations do not match LaTeX source order; refusing to assign removal targets")
    for line, (_, match, key) in zip(rendered, source):
        line["source"] = {"offset": match.start(), "token": match.group(0),
                          "tex_key": key, "tex_line": body.count("\n", 0, match.start()) + 1}


def images_current(pages: list[dict]) -> bool:
    return len(list(PAGES.glob("page-*.jpg"))) == len(pages) and all(
        (PAGES / f"page-{page['number']:02d}.jpg").is_file() for page in pages
    ) and all((PAGES / f"page-{page['number']:02d}.jpg").stat().st_mtime >= PDF.stat().st_mtime for page in pages)


def render_images(pages: list[dict], check: bool) -> None:
    if images_current(pages):
        return
    if check:
        raise SystemExit("Rendered page images are missing or out of date")
    PAGES.mkdir(exist_ok=True)
    subprocess.run(
        ["pdftoppm", "-jpeg", "-r", "120", "-jpegopt", "quality=85",
         str(PDF), str(PAGES / "page")],
        check=True, capture_output=True, text=True,
    )
    expected = {f"page-{page['number']:02d}.jpg" for page in pages}
    for obsolete in PAGES.glob("page-*.jpg"):
        if obsolete.name not in expected:
            obsolete.unlink()
    if not images_current(pages):
        raise RuntimeError("PDF page image generation did not produce the expected pages")


def build(check: bool = False) -> None:
    pages = pdf_text()
    link_source_citations(pages)
    render_images(pages, check)
    references = bibliography_payload()
    payload = {
        "source": {"pdf": PDF.name, "pdf_sha256": digest(PDF),
                   "tex_sha256": digest(TEX), "references_sha256": digest(REFERENCES),
                   "catalog_sha256": digest(CATALOG)},
        "pages": pages, "references": references, "corpus": corpus_payload(references),
    }
    embedded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    output = TEMPLATE.read_text(encoding="utf-8").replace("__REVIEW_DATA__", embedded)
    if check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != output:
            raise SystemExit("Paper review viewer is out of date")
        print(f"Paper review viewer is current: {len(pages)} pages")
        return
    OUTPUT.write_text(output, encoding="utf-8")
    linked = sum(line["citation"] is not None for page in pages for line in page["lines"])
    supported = sum(ref["report"] is not None for ref in payload["references"])
    print(f"Built {OUTPUT}: {len(pages)} pages, {linked} citation targets, "
          f"{supported}/{len(references)} references with ASD reports, "
          f"{len(payload['corpus'])} corpus works")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    build(parser.parse_args().check)
