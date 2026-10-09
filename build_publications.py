"""Build the offline publication browser and citation ontology.

Only citations whose title occurs in the citing PDF's reference section become
edges. Publication years come from the curated source registry, the literature
report viewer, or (when necessary) the PDF's front matter.
"""

from __future__ import annotations

import json
import re
import subprocess
import unicodedata
from collections import defaultdict
from datetime import date as calendar_date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
INDEX = ROOT / "paper-classifications" / "papers.json"
PDF_DIR = REPO_ROOT / "literature" / "academic-papers-processed"
SOURCES = ROOT / "classification" / "sources.json"
REPORT_INDEX = ROOT / "reports" / "asd-ste100" / "REPORT_INDEX.md"
REPORT_VIEWER = ROOT / "reports" / "asd-ste100" / "legacy.html"
TEMPLATE = ROOT / "paper-publications-template.html"
OUTPUT = ROOT / "paper-publications.html"
DATA_OUTPUT = ROOT / "paper-publications.json"


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(character for character in value if not unicodedata.combining(character))
    value = value.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl").replace("×", "x")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def title_key(value: str) -> str:
    return normalized(value).replace(" ", "")


def extract_pdf(path: Path, first_pages: int | None = None) -> str:
    command = ["pdftotext", "-enc", "UTF-8", "-raw"]
    if first_pages:
        command += ["-f", "1", "-l", str(first_pages)]
    command += [str(path), "-"]
    result = subprocess.run(command, capture_output=True, text=True, timeout=35, check=False)
    return result.stdout if result.returncode == 0 else ""


def bibliography(text: str) -> str:
    matches = list(re.finditer(
        r"(?im)^\s*(?:\d+[. ]+)?(?:references|bibliography|literature cited|works cited)\s*$",
        text,
    ))
    matches = [match for match in matches if match.start() > len(text) * .20]
    if not matches:
        return ""
    return text[matches[-1].end():]


def front_date(text: str) -> tuple[str | None, int | None]:
    # Use stated release dates and year-bearing publication lines on page one.
    # Received dates, download stamps, bibliographies and PDF metadata are not
    # evidence of publication.
    first_page = text.split("\f", 1)[0]
    exact = re.search(
        r"(?im)(?:advance access publication date|published online|available online|first published|publication date|posted online|published)\s*:?\s*"
        r"(\d{1,2}\s+[A-Za-z]+\s+20\d{2}|[A-Za-z]+\s+\d{1,2},?\s+20\d{2}|20\d{2}-\d{2}-\d{2})",
        first_page,
    )
    if exact:
        value = exact.group(1).replace(",", "")
        for fmt in ("%d %B %Y", "%B %d %Y", "%Y-%m-%d"):
            try:
                date = datetime.strptime(value, fmt).date()
                if date.year <= 2026:
                    return date.isoformat(), date.year
            except ValueError:
                pass

    for line in first_page.splitlines():
        if re.search(r"ACM Subject Classification|arXiv:\d{4}\.", line, re.I):
            continue
        if not re.search(r"©|copyright|\b(?:volume|vol\.|journal|proceedings|conference|workshop|bioinformatics|bioRxiv|arXiv)\b", line, re.I):
            continue
        if re.search(r"downloaded|received|revised|references|introduction|related work|algorithm|1970.s", line, re.I):
            continue
        years = [int(value) for value in re.findall(r"\b(19\d{2}|20[012]\d)\b", line)]
        years = [year for year in years if 1950 <= year <= 2026]
        if years:
            return None, years[-1]
    return None, None

def report_years() -> dict[str, int]:
    viewer = REPORT_VIEWER.read_text()
    block = re.search(r"const publicationYears\s*=\s*(\{.*?\});", viewer, re.S)
    if not block:
        raise ValueError("Could not find the report viewer's publication year registry")
    years = json.loads(block.group(1))
    mapping = {}
    for title, slug in re.findall(r"\|\s*\[([^\]]+)\]\(([^)]+\.md)\)\s*\|", REPORT_INDEX.read_text()):
        year = years.get(slug.removesuffix(".md"))
        if year:
            mapping[title_key(title)] = year
    return mapping


def main() -> None:
    source_index = json.loads(INDEX.read_text())
    skipped = set(source_index["skipped_files"])
    curated = {title_key(source["title"]): source["year"] for source in json.loads(SOURCES.read_text())
               if isinstance(source.get("year"), int) and source.get("resource_type") != "repository"}
    reports = report_years()

    # The classification index keeps duplicate files. One ontology node denotes
    # one work, with all local copies retained as links.
    works = {}
    for paper in source_index["papers"]:
        if paper["filename"] in skipped:
            continue
        key = title_key(paper["title"])
        if key not in works:
            works[key] = {
                "id": paper["id"], "title": paper["title"], "authors": paper["authors"],
                "pdf_href": paper["pdf_href"].removeprefix("../"),
                "copies": [], "summary": paper["summary"], "year": None, "release_date": None,
                "year_source": "unverified", "citations": [],
            }
        works[key]["copies"].append(paper["filename"])

    for key, work in works.items():
        first = extract_pdf(PDF_DIR / work["copies"][0], 1)
        date, page_year = front_date(first)
        if date:
            work["release_date"] = date
            work["year"], work["year_source"] = page_year, "PDF stated online release"
        elif key in curated:
            work["year"], work["year_source"] = curated[key], "curated source registry"
        elif key in reports:
            work["year"], work["year_source"] = reports[key], "literature report index"
        else:
            work["year"] = page_year
            work["year_source"] = "PDF first page" if work["year"] else "unverified"

    # Search title strings only in explicit bibliographies. The normalized
    # substring rule is strict; uncertain OCR and abbreviated citations stay
    # unmatched, rather than creating an unsupported relationship.
    all_works = list(works.values())
    edges = []
    for citing in all_works:
        raw = extract_pdf(PDF_DIR / citing["copies"][0])
        refs = bibliography(raw)
        if not refs:
            continue
        normalized_refs = normalized(refs)
        for cited in all_works:
            if cited is citing or len(title_key(cited["title"])) < 24:
                continue
            needle = normalized(cited["title"])
            found = normalized_refs.find(needle)
            if found < 0:
                continue
            if citing["year"] and cited["year"] and cited["year"] > citing["year"]:
                continue
            evidence = normalized_refs[max(0, found - 110):found + len(needle) + 85]
            edges.append({"source": cited["id"], "target": citing["id"], "evidence": evidence})
            citing["citations"].append(cited["id"])

    outgoing = defaultdict(list)
    for edge in edges:
        outgoing[edge["source"]].append(edge["target"])
    for work in all_works:
        work["cited_by_count"] = len(outgoing[work["id"]])
        seen, queue = {work["id"]}, [work["id"]]
        for current in queue:
            for later in outgoing[current]:
                if later not in seen:
                    seen.add(later)
                    queue.append(later)
        work["downstream_count"] = len(seen) - 1
    all_works.sort(key=lambda work: (-work["downstream_count"], -work["cited_by_count"], work["year"] or 9999, work["title"].casefold()))
    data = {
        "generated": calendar_date.today().isoformat(), "source_index_generated": source_index["generated"], "method": "Exact normalized title matches within extracted PDF reference sections; year from curated registry, report index, or PDF first page.",
        "excluded_textbooks": sorted(skipped), "papers": all_works, "edges": edges,
    }
    DATA_OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    OUTPUT.write_text(TEMPLATE.read_text().replace("__ONTOLOGY_DATA__", embedded))
    dated = sum(work["year"] is not None for work in all_works)
    print(f"Wrote {OUTPUT}: {len(all_works)} works, {dated} dated, {len(edges)} citations")


if __name__ == "__main__":
    main()
