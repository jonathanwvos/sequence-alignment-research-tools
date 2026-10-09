#!/usr/bin/env python3
"""Build the local literature catalog from the processed PDFs and bibliography.

The processed directory is the only PDF input. The program never changes a PDF.
Run ``python3 literature/tools/build_corpus.py`` to rebuild, or add ``--check``
to validate existing outputs without writing anything.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import quote


LITERATURE = Path(__file__).resolve().parents[1]
ROOT = LITERATURE.parents[2]
PDF_DIR = ROOT / "literature" / "academic-papers-processed"
BIBLIOGRAPHY = ROOT / "docs" / "Literature Review" / "Bibliography.md"
CATALOG = LITERATURE / "catalog"
CACHE = ROOT / "literature" / ".cache" / "paper-text"
REPORT_DIR = LITERATURE / "reports" / "asd-ste100" / "current"
DOI = re.compile(r"\b10\.\d{4,9}/[^\s<>\[\]{}]+", re.I)
REF_HEADING = re.compile(
    r"(?im)^\s*(?:\d+[. ]+)?(?:references?|bibliography|literature cited|works cited)\s*[:;.]?\s*$"
)
NUMBERED = re.compile(r"^\s*(?:\[[A-Za-z0-9+\-]{1,12}\]|\d{1,4}[.)]?)\s+(?=[A-ZÀ-Ž])")
YEAR = re.compile(r"\b(19\d{2}|20[012]\d)\b")


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = value.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def clean_doi(value: str) -> str:
    return value.rstrip(".,;:)]}").lower()


def filename_title(path: Path) -> str:
    stem = re.sub(r"\s+", " ", path.stem).strip()
    pieces = stem.rsplit(" - ", 1)
    if len(pieces) == 2 and len(pieces[1].split()) <= 12:
        stem = pieces[0]
    return re.sub(r"\s+\((?:copy \d+|annotated|accepted manuscript)\)$", "", stem, flags=re.I)


def filename_authors(path: Path) -> str | None:
    pieces = re.sub(r"\s+", " ", path.stem).rsplit(" - ", 1)
    if len(pieces) == 2 and len(pieces[1].split()) <= 12:
        return pieces[1]
    return None


def bibliography_entries() -> list[dict]:
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    section = ""
    entries = []
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("## "):
            section = line[3:].strip()
        numbered = re.match(r"^###\s+(\d+)\.\s+(.+)$", line)
        annotated = re.match(
            r"^###\s+(?:Source\s+(\d+):|Manuscript reference\s+(\d+)(?:\s+\([^)]*\))?)\s*(.*)$",
            line,
            re.I,
        )
        if not numbered and not annotated:
            continue
        rank = int(numbered.group(1) if numbered else annotated.group(1) or annotated.group(2))
        heading = numbered.group(2) if numbered else annotated.group(3) or line[4:].strip()
        prose = "\n".join(lines[index + 1 : index + 5])
        citation = next((line.strip() for line in lines[index + 1 : index + 5] if line.strip()), "")
        citation_core = citation.split("DOI:", 1)[0]
        page_ranges = re.findall(r"\b(\d{1,5})\s*[–—-]\s*\d{1,5}\b", citation_core)
        first_author = re.match(r"([A-Za-zÀ-ž'’-]+)", citation)
        title = re.search(r"\*\*([^*]+)\*\*", prose)
        citation_parts = re.split(r"(?<=\.)\s+", citation, maxsplit=2)
        title_text = (
            title.group(1).strip().rstrip(".") if title else
            citation_parts[1].strip().rstrip(".") if len(citation_parts) > 1 else
            heading
        )
        doi = DOI.search(prose)
        year = YEAR.search(heading) or YEAR.search(citation)
        entries.append({
            "rank": rank,
            "id": "b-" + hashlib.sha256(
                (clean_doi(doi.group()) if doi else normalized(title_text)).encode()
            ).hexdigest()[:12],
            "title": title_text,
            "heading": heading,
            "section": section,
            "doi": clean_doi(doi.group()) if doi else None,
            "year": int(year.group(1)) if year else None,
            "citation": citation,
            "first_author": normalized(first_author.group(1)) if first_author else None,
            "first_page": int(page_ranges[-1]) if page_ranges else None,
        })
    return entries


def extract(path: Path, digest: str) -> tuple[str, str | None]:
    CACHE.mkdir(parents=True, exist_ok=True)
    ocr_cached = CACHE / f"{digest}.ocr.txt"
    if ocr_cached.exists():
        return ocr_cached.read_text(encoding="utf-8"), None
    cached = CACHE / f"{digest}.raw.txt"
    if cached.exists():
        return cached.read_text(encoding="utf-8"), None
    try:
        result = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", "-raw", str(path), "-"],
            text=True, capture_output=True, timeout=100, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return "", f"PDF text extraction failed: {error}"
    if result.returncode:
        return "", f"pdftotext returned {result.returncode}: {result.stderr[:180]}"
    cached.write_text(result.stdout, encoding="utf-8")
    return result.stdout, None


def reference_start(text: str) -> int | None:
    headings = [m for m in REF_HEADING.finditer(text) if m.start() > len(text) * 0.05]
    if headings:
        return headings[-1].end()
    # Some older journals print numbered references without a heading.
    for match in re.finditer(r"(?m)^\s*1[.)]\s+[A-ZÀ-Ž]", text):
        if match.start() < len(text) * 0.30:
            continue
        nearby = text[match.start():match.start() + 5000]
        if (re.search(r"(?m)^\s*2[.)]\s+[A-ZÀ-Ž]", nearby) and
            re.search(r"(?m)^\s*3[.)]\s+[A-ZÀ-Ž]", nearby)):
            return match.start()
    return None


def extract_reference_entries(text: str) -> tuple[list[dict], str | None]:
    start = reference_start(text)
    if start is None:
        return [], "No reference list found in extracted text"
    page = text[:start].count("\f") + 1
    lines = text[start:].splitlines(keepends=True)
    chunks: list[tuple[int, list[str]]] = []
    current: list[str] = []
    current_page = page
    numbered = sum(bool(NUMBERED.match(line)) for line in lines) >= 2
    blank = False
    for line in lines:
        page += line.count("\f")
        value = line.replace("\f", "").strip()
        if not value:
            blank = True
            continue
        starts = bool(NUMBERED.match(value)) if numbered else (
            bool(NUMBERED.match(value)) or
            bool(re.match(r"^[A-ZÀ-Ž][A-Za-zÀ-ž'’.-]+(?:,?\s+[A-Z][A-Za-zÀ-ž.'’-]*){1,5}", value))
            and (bool(YEAR.search(value[:140])) or blank)
        )
        if starts and current:
            chunks.append((current_page, current))
            current = []
        if not current:
            current_page = page
        current.append(value)
        blank = False
    if current:
        chunks.append((current_page, current))
    if not chunks:
        return [], "Reference heading found, but no entries extracted"
    if len(chunks) == 1 and len(" ".join(chunks[0][1])) > 1800:
        return [], "Reference list could not be separated into entries"
    entries = []
    for page_number, parts in chunks:
        raw = re.sub(r"\s+", " ", " ".join(parts)).strip()
        raw = NUMBERED.sub("", raw)
        if not raw:
            continue
        doi = DOI.search(raw)
        year = YEAR.search(raw)
        entries.append({
            "page": page_number,
            "raw": raw,
            "doi": clean_doi(doi.group()) if doi else None,
            "year": int(year.group(1)) if year else None,
        })
    return entries, None


def source_pdf(path: Path) -> dict:
    if path.is_symlink():
        raise ValueError(f"Symlinked PDF is not allowed: {path}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    text, error = extract(path, digest)
    first = text.split("\f", 1)[0]
    doi_match = DOI.search(first[:6000])
    year_guess = None
    year_source = None
    for line in first.splitlines()[:65]:
        if re.search(r"published|publication|available online|posted online|first posted|copyright|©|\b(?:nature|science|journal|bioinformatics|arxiv|biorxiv)\b", line, re.I):
            years = [int(y) for y in YEAR.findall(line) if 1950 <= int(y) <= 2026]
            if years:
                year_guess = years[0]
                year_source = "PDF front matter"
                break
    references, reference_error = extract_reference_entries(text) if text else ([], "No extractable PDF text")
    return {
        "asset_id": "a-" + digest[:16],
        "sha256": digest,
        "path": path.relative_to(ROOT).as_posix(),
        "title_guess": filename_title(path),
        "authors_guess": filename_authors(path),
        "doi_guess": clean_doi(doi_match.group()) if doi_match else None,
        "year_guess": year_guess,
        "year_source": year_source,
        "text_characters": len(text.strip()),
        "extraction_method": "ocr" if (CACHE / f"{digest}.ocr.txt").exists() else "pdftotext",
        "pages_extracted": max(0, text.count("\f")),
        "extract_error": error,
        "reference_error": reference_error,
        "reference_section_raw": (
            text[reference_start(text):].strip()
            if reference_error and reference_start(text) is not None else None
        ),
        "references": references,
    }


def bibliography_match(asset: dict, entries: list[dict]) -> tuple[dict | None, str | None]:
    if asset["doi_guess"]:
        hits = [entry for entry in entries if entry["doi"] == asset["doi_guess"]]
        if len(hits) == 1:
            return hits[0], "doi"
    title = normalized(asset["title_guess"])
    exact = [entry for entry in entries if normalized(entry["title"]) == title]
    if len(exact) == 1:
        return exact[0], "title"
    partial = [entry for entry in entries if len(normalized(entry["title"])) > 24
               and normalized(entry["title"]) in title]
    if len(partial) == 1:
        return partial[0], "title"
    return None, None


def get_overrides() -> dict:
    path = CATALOG / "overrides.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {
        "assets": {}, "works": {}, "reference_matches": {},
    }


def build() -> tuple[dict, dict, dict]:
    paths = sorted(
        (path for path in PDF_DIR.iterdir() if path.is_file() and path.suffix.lower() == ".pdf"),
        key=lambda path: path.name.casefold(),
    )
    if not paths:
        raise ValueError("No processed PDFs found")
    entries = bibliography_entries()
    overrides = get_overrides()
    identities_path = CATALOG / "identities.json"
    identities = json.loads(identities_path.read_text()) if identities_path.exists() else {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        assets = list(pool.map(source_pdf, paths))
    works: dict[str, dict] = {}
    title_to_id: dict[str, str] = {}
    doi_to_id: dict[str, str] = {}
    duplicate_candidates = []
    for entry in entries:
        works[entry["id"]] = {
            "id": entry["id"], "title": entry["title"], "authors": None,
            "year": entry["year"], "doi": entry["doi"], "type": "paper",
            "bibliography": {"rank": entry["rank"], "section": entry["section"],
                             "citation": entry["citation"], "first_author": entry["first_author"],
                             "first_page": entry["first_page"]},
            "assets": [], "report_paths": [],
        }
        title_to_id[normalized(entry["title"])] = entry["id"]
        if entry["doi"]:
            doi_to_id[entry["doi"]] = entry["id"]
    for asset in assets:
        match, method = bibliography_match(asset, entries)
        explicit = overrides.get("assets", {}).get(asset["sha256"], {})
        title_key = normalized(re.sub(r"\s+-\s+supplementary$", "", asset["title_guess"], flags=re.I))
        work_id = explicit.get("work_id")
        if not work_id and match:
            work_id = match["id"]
        if not work_id and asset["doi_guess"] in doi_to_id:
            work_id = doi_to_id[asset["doi_guess"]]
        if not work_id and title_key in title_to_id:
            work_id = title_to_id[title_key]
        if not work_id:
            work_id = identities.get(asset["sha256"], "w-" + asset["sha256"][:12])
        identities[asset["sha256"]] = work_id
        work = works.setdefault(work_id, {
            "id": work_id, "title": asset["title_guess"], "authors": asset["authors_guess"],
            "year": asset["year_guess"], "doi": asset["doi_guess"], "type": "paper",
            "bibliography": None, "assets": [], "report_paths": [],
        })
        work["assets"].append(asset["asset_id"])
        asset["work_id"] = work_id
        asset["bibliography_match_method"] = method
        asset["report_path"] = f"literature/reports/asd-ste100/current/{asset['asset_id']}.md"
        work["report_paths"].append(asset["report_path"])
        if not work["authors"]:
            work["authors"] = asset["authors_guess"]
        if not work["year"]:
            work["year"] = asset["year_guess"]
        if not work["doi"]:
            work["doi"] = asset["doi_guess"]
        title_to_id.setdefault(title_key, work_id)
        if asset["doi_guess"]:
            doi_to_id.setdefault(asset["doi_guess"], work_id)
    for work in works.values():
        work.update(overrides.get("works", {}).get(work["id"], {}))
        if len(work["assets"]) > 1:
            duplicate_candidates.append({"work_id": work["id"], "assets": work["assets"]})
        if not work["assets"]:
            work["missing_local_pdf"] = True
        else:
            work["missing_local_pdf"] = False
        work["pdf_href"] = (
            quote((ROOT / next(a["path"] for a in assets if a["asset_id"] == work["assets"][0])).relative_to(LITERATURE).as_posix(), safe="/")
            if work["assets"] else None
        )
    references = []
    candidates = []
    edges_by_pair = {}
    for asset in assets:
        for position, reference in enumerate(asset.pop("references")):
            ref_id = asset["asset_id"] + f"-r{position + 1:04d}"
            raw_key = normalized(reference["raw"])
            matches = []
            doi = reference["doi"]
            if doi and doi in doi_to_id:
                matches = [(doi_to_id[doi], "doi")]
            else:
                for work in works.values():
                    title = normalized(work["title"])
                    if len(title) >= 24 and title in raw_key:
                        matches.append((work["id"], "title"))
                if not matches:
                    for work in works.values():
                        bib = work["bibliography"]
                        if not bib or not bib.get("first_author") or not bib.get("first_page") or not work["year"]:
                            continue
                        surname = bib["first_author"]
                        page = str(bib["first_page"])
                        if (f" {surname} " in f" {raw_key} " and
                            str(work["year"]) in raw_key and
                            re.search(rf"\b{re.escape(page)}\b", raw_key)):
                            matches.append((work["id"], "author_year_page"))
            matches = list(dict.fromkeys((id_, method) for id_, method in matches if id_ != asset["work_id"]))
            override = overrides.get("reference_matches", {}).get(ref_id)
            if override is not None:
                cited = override.get("work_id")
                status = "reviewed" if cited else "rejected"
            elif len(matches) == 1:
                cited = matches[0][0]
                status = "automatic"
            else:
                cited = None
                status = "ambiguous" if matches else "external_or_unmatched"
            record = {
                "id": ref_id, "citing_asset_id": asset["asset_id"],
                "citing_work_id": asset["work_id"], "page": reference["page"],
                "raw": reference["raw"], "doi": doi, "year": reference["year"],
                "cited_work_id": cited, "match_status": status,
                "match_method": matches[0][1] if cited and matches else ("review" if status == "reviewed" else None),
                "candidates": [id_ for id_, _ in matches] if status == "ambiguous" else [],
            }
            references.append(record)
            if status == "ambiguous":
                candidates.append(record)
            if cited:
                pair = (cited, asset["work_id"])
                edge = edges_by_pair.setdefault(pair, {
                    "source": cited, "target": asset["work_id"], "reference_ids": [],
                })
                edge["reference_ids"].append(ref_id)
    index = {
        "schema_version": 1,
        "source_directory": "literature/academic-papers-processed",
        "bibliography_path": "docs/Literature Review/Bibliography.md",
        "assets": assets,
        "works": sorted(works.values(), key=lambda w: (w["bibliography"] is None, (w["bibliography"] or {}).get("rank", 999), w["title"].casefold())),
        "edges": list(edges_by_pair.values()),
    }
    audit = {
        "pdf_count": len(assets), "work_count": len(works),
        "bibliography_count": len(entries),
        "missing_bibliography": [w["id"] for w in works.values() if w["bibliography"] and not w["assets"]],
        "duplicate_candidates": duplicate_candidates,
        "extraction_issues": [{"asset_id": a["asset_id"], "path": a["path"], "issue": a["extract_error"] or a["reference_error"] or "Sparse text"}
                              for a in assets if a["extract_error"] or a["reference_error"] or a["text_characters"] < 500],
        "ambiguous_references": [r["id"] for r in candidates],
        "reference_count": len(references),
        "matched_reference_count": sum(r["cited_work_id"] is not None for r in references),
    }
    return index, {"schema_version": 1, "references": references}, {"audit": audit, "identities": identities}


def import_review(path: Path) -> None:
    """Merge exported browser corrections after validating every identifier."""
    proposed = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(proposed, dict) or not set(proposed).issubset({"assets", "works", "reference_matches"}):
        raise ValueError("Review JSON must contain only assets, works, and reference_matches")
    current_index = json.loads((CATALOG / "index.json").read_text())
    current_refs = json.loads((CATALOG / "references.json").read_text())["references"]
    shas = {asset["sha256"] for asset in current_index["assets"]}
    works = {work["id"] for work in current_index["works"]}
    ref_ids = {ref["id"] for ref in current_refs}
    for key in ("assets", "works", "reference_matches"):
        if not isinstance(proposed.get(key, {}), dict):
            raise ValueError(f"{key} must be an object")
    for sha, value in proposed.get("assets", {}).items():
        if sha not in shas or not isinstance(value, dict) or value.get("work_id") not in works:
            raise ValueError(f"Invalid asset correction: {sha}")
    for work_id, value in proposed.get("works", {}).items():
        if work_id not in works or not isinstance(value, dict):
            raise ValueError(f"Invalid work correction: {work_id}")
    for ref_id, value in proposed.get("reference_matches", {}).items():
        if ref_id not in ref_ids or not isinstance(value, dict) or value.get("work_id") not in works | {None}:
            raise ValueError(f"Invalid reference correction: {ref_id}")
    existing = get_overrides()
    for key in ("assets", "works", "reference_matches"):
        existing.setdefault(key, {}).update(proposed.get(key, {}))
    (CATALOG / "overrides.json").write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n")
    print(f"Imported {sum(len(proposed.get(key, {})) for key in ('assets', 'works', 'reference_matches'))} review decisions")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate generated outputs without writing")
    parser.add_argument("--import-review", type=Path, metavar="JSON", help="Merge exported browser corrections")
    args = parser.parse_args()
    if args.check and args.import_review:
        parser.error("--check and --import-review cannot be combined")
    if args.import_review:
        import_review(args.import_review)
    index, references, additional = build()
    audit = additional["audit"]
    if args.check:
        expected = json.loads((CATALOG / "index.json").read_text())
        if index != expected:
            raise SystemExit("Catalog is out of date")
        print(f"Catalog is current: {audit['pdf_count']} PDFs, {audit['bibliography_count']} bibliography entries")
        return
    CATALOG.mkdir(parents=True, exist_ok=True)
    for name, data in (
        ("index.json", index), ("references.json", references),
        ("audit.json", audit), ("identities.json", additional["identities"]),
    ):
        (CATALOG / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Indexed {audit['pdf_count']} PDFs as {audit['work_count']} works; "
          f"{audit['reference_count']} references, {audit['matched_reference_count']} local matches; "
          f"{len(audit['missing_bibliography'])} bibliography gaps")


if __name__ == "__main__":
    main()
