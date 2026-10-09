#!/usr/bin/env python3
"""Apply queued citation removals to the manuscript and rendered PDF.

Without --apply this command validates the review JSON and prints a dry run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from build import DOCS, PDF, TEX, build, digest, manuscript_bibliography

CITATION = re.compile(r"\\draftcite\{(\d+)\}")


def remove_one(text: str, offset: int, token: str) -> str:
    """Remove one citation and an adjacent separator only when it joins citations."""
    start, end = offset, offset + len(token)
    before, after = text[:start], text[end:]
    next_citation = re.match(r"[ \t]*,[ \t]*(?=\\draftcite\{\d+\})", after)
    previous_citation = re.search(r"\\draftcite\{\d+\}[ \t]*(,[ \t]*)$", before)
    if next_citation:
        end += next_citation.end()
    elif previous_citation:
        start -= len(previous_citation.group(1))
    elif before.endswith("(") and after.startswith(")"):
        start -= 1
        end += 1
        if start and text[start - 1] in " \t":
            start -= 1
    elif start and text[start - 1] in " \t~":
        start -= 1
    return text[:start] + text[end:]


def planned_text(text: str, review: dict) -> str:
    source = review.get("source") or {}
    if source.get("tex_sha256") != hashlib.sha256(text.encode("utf-8")).hexdigest():
        raise ValueError("LaTeX source differs from the reviewed snapshot; export a fresh review")
    if review.get("applied"):
        raise ValueError("This review JSON has already been applied")
    removals = review.get("removals")
    if not isinstance(removals, list):
        raise ValueError("Review JSON has no valid removals list")
    boundary = text.find(r"\begin{thebibliography}")
    if boundary < 0:
        raise ValueError("Manuscript bibliography not found")
    by_key = {entry["tex_key"]: entry["pdf_number"] for entry in manuscript_bibliography()}
    seen = set()
    for item in removals:
        offset, token = item.get("tex_offset"), item.get("token")
        match = CITATION.fullmatch(token) if isinstance(token, str) else None
        if (not isinstance(offset, int) or isinstance(offset, bool) or offset < 0
                or offset >= boundary or not match or text[offset:offset + len(token)] != token):
            raise ValueError(f"Invalid or stale citation removal target: {item!r}")
        if offset in seen or item.get("tex_key") != f"ref{match.group(1)}" or by_key.get(item["tex_key"]) != item.get("pdf_number"):
            raise ValueError(f"Ambiguous citation removal target at source offset {offset}")
        seen.add(offset)
    updated = text
    for item in sorted(removals, key=lambda value: value["tex_offset"], reverse=True):
        updated = remove_one(updated, item["tex_offset"], item["token"])
    return updated


def atomic_write(path: Path, data: bytes) -> None:
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".citation-review-", delete=False) as output:
        temporary = Path(output.name)
        output.write(data)
    try:
        shutil.copymode(path, temporary)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def apply(review_path: Path, review: dict, updated: str) -> Path:
    original_tex, original_pdf = TEX.read_bytes(), PDF.read_bytes()
    with tempfile.TemporaryDirectory(prefix="vala-citation-render-") as temporary:
        result = subprocess.run(
            ["tectonic", "-C", "-o", temporary, "-"], input=updated,
            cwd=DOCS, text=True, capture_output=True,
        )
        rendered = Path(temporary) / "texput.pdf"
        if result.returncode or not rendered.is_file():
            raise RuntimeError("PDF render failed; manuscript unchanged.\n" + "\n".join(result.stderr.splitlines()[-15:]))
        new_pdf = rendered.read_bytes()
    if digest(TEX) != review["source"]["tex_sha256"] or digest(PDF) != review["source"]["pdf_sha256"]:
        raise ValueError("Manuscript changed during rendering; nothing was applied")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = DOCS / ".citation-review-backups" / f"{stamp}-{review['source']['tex_sha256'][:8]}"
    backup.mkdir(parents=True, exist_ok=False)
    shutil.copy2(TEX, backup / TEX.name)
    shutil.copy2(PDF, backup / PDF.name)
    shutil.copy2(review_path, backup / review_path.name)
    try:
        atomic_write(TEX, updated.encode("utf-8"))
        atomic_write(PDF, new_pdf)
        build()
        review["applied"] = {
            "at_utc": datetime.now(timezone.utc).isoformat(),
            "removed_count": len(review["removals"]),
            "tex_sha256": digest(TEX), "pdf_sha256": digest(PDF),
            "backup": str(backup),
        }
        atomic_write(review_path, (json.dumps(review, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    except Exception:
        atomic_write(TEX, original_tex)
        atomic_write(PDF, original_pdf)
        build()
        raise
    return backup


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review_json", type=Path, help="JSON exported from the paper review viewer")
    parser.add_argument("--apply", action="store_true", help="edit the LaTeX manuscript, PDF, and review JSON")
    args = parser.parse_args()
    review_path = args.review_json.resolve()
    review = json.loads(review_path.read_text(encoding="utf-8"))
    if review.get("version") != 1:
        raise SystemExit("Unsupported review JSON version")
    if review.get("applied"):
        raise SystemExit("This review JSON has already been applied; export a new review from the refreshed viewer")
    if review.get("source", {}).get("pdf_sha256") != digest(PDF):
        raise SystemExit("Rendered PDF differs from the reviewed snapshot; export a fresh review")
    updated = planned_text(TEX.read_text(encoding="utf-8"), review)
    count = len(review["removals"])
    if not count:
        print("No citations queued for removal; manuscript unchanged")
        return
    if not args.apply:
        print(f"Dry run: {count} citation occurrence(s) ready to remove. Add --apply to update the manuscript and PDF.")
        return
    backup = apply(review_path, review, updated)
    print(f"Removed {count} citation occurrence(s) from the LaTeX manuscript and PDF; marked JSON as applied.")
    print(f"Original files backed up at {backup}")


if __name__ == "__main__":
    main()
