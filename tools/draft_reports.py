#!/usr/bin/env python3
"""Draft source-grounded literature reports in bounded Codex batches.

The CLI receives selected PDF text, returns structured claims, and cannot write to
this workspace. This script validates its response and renders the Markdown.
Existing reports are never overwritten unless --force is supplied.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
CATALOG = BASE / "catalog"
CACHE = ROOT / "literature" / ".cache" / "paper-text"
REPORTS = BASE / "reports" / "asd-ste100" / "current"
SCHEMA = Path(__file__).with_name("report.schema.json")
FIELDS = (
    ("summary", "Executive summary"), ("objectives", "Objectives"),
    ("arguments", "Arguments"), ("analysis", "Analysis"),
    ("methods", "Methods"), ("applications", "Applications"),
    ("optimization", "Optimization"), ("evaluation", "Evaluation and testing"),
    ("results", "Results"), ("limitations", "Limitations and uncertainty"),
)
HEADING = re.compile(r"(?im)^\s*(?:\d+(?:\.\d+)*[. ]+)?(?:methods?|materials and methods|results?|discussion|conclusions?|implementation|evaluation|experiments?|benchmarks?|complexity|limitations?)\b")
REF_HEADING = re.compile(r"(?im)^\s*(?:references|bibliography|literature cited|works cited)\s*$")


def selected_pages(asset: dict) -> str:
    ocr = CACHE / (asset["sha256"] + ".ocr.txt")
    source = ocr if ocr.exists() else CACHE / (asset["sha256"] + ".raw.txt")
    text = source.read_text(encoding="utf-8")
    references = [m for m in REF_HEADING.finditer(text) if m.start() > len(text) * 0.05]
    if references:
        text = text[:references[-1].start()]
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    candidate = set(range(min(3, len(pages))))
    candidate.update(range(max(0, len(pages) - 2), len(pages)))
    for i, page in enumerate(pages):
        if HEADING.search(page):
            candidate.add(i)
    chosen = []
    size = 0
    for i in sorted(candidate):
        page = pages[i].strip()
        if not page:
            continue
        page = page[:8500]
        if size + len(page) > 62000 and chosen:
            continue
        chosen.append(f"[PDF PAGE {i + 1}]\n{page}")
        size += len(page)
    return "\n\n".join(chosen)


def prompt_for(assets: list[dict], works: dict[str, dict]) -> str:
    packets = []
    for asset in assets:
        work = works[asset["work_id"]]
        packets.append(json.dumps({
            "asset_id": asset["asset_id"], "title": work["title"],
            "authors": work["authors"], "year": work["year"],
            "source": asset["path"], "selected_pdf_pages": selected_pages(asset),
        }, ensure_ascii=False))
    return ("You are writing research notes from local PDF text for a sequence-alignment literature review. "
            "Return only JSON that conforms to the supplied schema. Do not use tools or outside knowledge. "
            "Write one report object for each supplied asset_id, in the same order. "
            "Use only the numbered PDF page excerpts below. Every substantive claim needs its PDF page number. "
            "Use null only when an item is explicitly uncertain and identify that uncertainty in the text. "
            "Do not copy long passages. Paraphrase accurately. Keep sentences short and use direct, controlled English "
            "consistent with ASD-STE100 Issue 9. Treat specialized scientific words as technical terms. "
            "Do not claim formal STE compliance. Distinguish the authors' claims from your interpretation. "
            "Describe the specific algorithm, analysis, benchmark, test framework, and optimization where the source supports them. "
            "If a section is not supported, return an empty array. Avoid generic filler and do not classify the paper. "
            "Each field should have one to four concise claims; summary can have two to four. "
            "The complete reference list is added separately; do not invent it.\n\n"
            + "\n\n".join(packets))


def render(asset: dict, work: dict, claims: dict, references: list[dict]) -> str:
    lines = [f"# {work['title']}", "", f"- Work ID: `{work['id']}`",
             f"- Asset ID: `{asset['asset_id']}`", f"- Source PDF: `{asset['path']}`",
             f"- SHA-256: `{asset['sha256']}`", "- ASD-STE100 Issue 9 review: **Pending manual review**", ""]
    for key, heading in FIELDS:
        lines += [f"## {heading}", ""]
        items = claims[key]
        if not items:
            lines += ["Not stated in the extractable source pages.", ""]
            continue
        for item in items:
            wording = item["text"].strip().rstrip(".") + "."
            page = item["page"]
            lines.append(f"- {wording} (PDF p. {page})." if page else f"- {wording} (Page not verified).")
        lines.append("")
    lines += ["## References", ""]
    if references:
        for i, ref in enumerate(references, 1):
            lines.append(f"{i}. {ref['raw']} (PDF p. {ref['page']})")
    elif asset.get("reference_section_raw"):
        lines += ["The reference entries need manual separation. The complete extracted reference section follows.", "",
                  "```text", asset["reference_section_raw"].strip(), "```"]
    else:
        lines.append("No complete reference list was extractable from this PDF. Manual review is required.")
    lines.append("")
    return "\n".join(lines)


def run_batch(assets: list[dict], works: dict[str, dict], refs: dict[str, list[dict]], model: str | None) -> tuple[int, str]:
    prompt = prompt_for(assets, works)
    with tempfile.TemporaryDirectory(prefix="vala-reports-") as temp:
        output = Path(temp) / "response.json"
        command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "-s", "read-only",
                   "-C", str(ROOT), "--output-schema", str(SCHEMA),
                   "--output-last-message", str(output), "-"]
        if model:
            command[2:2] = ["-m", model]
        result = subprocess.run(command, input=prompt, text=True, capture_output=True, timeout=1000)
        if result.returncode or not output.exists():
            useful = [line for line in (result.stdout + "\n" + result.stderr).splitlines()
                      if "WARN codex_skills_extension" not in line and "unknown variant `CHAT`" not in line]
            return 0, f"Codex exit {result.returncode}; " + "\n".join(useful[-18:])[-2500:]
        try:
            payload = json.loads(output.read_text())
            returned = {entry["asset_id"]: entry for entry in payload["reports"]}
            if set(returned) != {asset["asset_id"] for asset in assets}:
                raise ValueError("Model returned unexpected report IDs")
            REPORTS.mkdir(parents=True, exist_ok=True)
            for asset in assets:
                claims = returned[asset["asset_id"]]
                if not any(claims[key] for key, _ in FIELDS):
                    raise ValueError(f"No claims for {asset['asset_id']}")
                max_page = max(1, asset["pages_extracted"])
                for key, _ in FIELDS:
                    for claim in claims[key]:
                        if not claim["text"].strip() or claim["page"] is not None and not 1 <= claim["page"] <= max_page:
                            raise ValueError(f"Invalid evidence in {asset['asset_id']} {key}")
                path = REPORTS / f"{asset['asset_id']}.md"
                path.write_text(render(asset, works[asset["work_id"]], claims, refs[asset["asset_id"]]), encoding="utf-8")
            return len(assets), "ok"
        except (KeyError, ValueError, json.JSONDecodeError) as error:
            return 0, f"{error}: {output.read_text()[:1200]}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="Maximum PDFs to draft in this run")
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--asset-id", action="append")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--model")
    args = parser.parse_args()
    index = json.loads((CATALOG / "index.json").read_text())
    refs = defaultdict(list)
    for ref in json.loads((CATALOG / "references.json").read_text())["references"]:
        refs[ref["citing_asset_id"]].append(ref)
    works = {w["id"]: w for w in index["works"]}
    assets = [a for a in index["assets"] if
              (not args.asset_id or a["asset_id"] in args.asset_id) and
              (args.force or not (REPORTS / f"{a['asset_id']}.md").exists())]
    unreadable = [a for a in assets if a["text_characters"] < 400]
    assets = [a for a in assets if a["text_characters"] >= 400]
    if args.limit:
        assets = assets[:args.limit]
    batches = [assets[i:i + args.batch_size] for i in range(0, len(assets), args.batch_size)]
    successes = 0
    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(run_batch, batch, works, refs, args.model): batch for batch in batches}
        for future in as_completed(futures):
            batch = futures[future]
            try:
                count, message = future.result()
            except Exception as error:
                count, message = 0, str(error)
            successes += count
            if not count:
                failures.append({"assets": [a["asset_id"] for a in batch], "error": message})
            print(f"Drafted {successes}/{len(assets)}; last batch: {message[:180]}", flush=True)
    audit = {"drafted_this_run": successes,
             "unreadable_assets": [a["asset_id"] for a in unreadable],
             "failures": failures}
    (CATALOG / "draft-audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    if failures:
        raise SystemExit(f"{len(failures)} report batches failed")


if __name__ == "__main__":
    main()
