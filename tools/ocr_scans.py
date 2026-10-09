#!/usr/bin/env python3
"""OCR processed PDFs with sparse text, without changing the source PDFs.

Use --binary and --tessdata for a user-local Tesseract installation. The OCR
text is cached under literature/.cache/paper-text, which Git ignores.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
CACHE = ROOT / "literature" / ".cache" / "paper-text"


def page_count(path: Path) -> int:
    result = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, timeout=20, check=True)
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, re.M)
    if not match:
        raise ValueError(f"Cannot determine pages in {path}")
    return int(match.group(1))


def ocr_one(asset: dict, binary: Path, tessdata: Path) -> tuple[str, int, str]:
    pdf = ROOT / asset["path"]
    pages = page_count(pdf)
    output = CACHE / (asset["sha256"] + ".ocr.txt")
    if output.exists():
        return asset["asset_id"], pages, "cached"
    env = dict(os.environ, TESSDATA_PREFIX=str(tessdata))
    chunks = []
    with tempfile.TemporaryDirectory(prefix="vala-ocr-page-") as temp:
        prefix = Path(temp) / "page"
        for page in range(1, pages + 1):
            image = prefix.with_suffix(".png")
            render = subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "170",
                 "-gray", "-png", "-singlefile", str(pdf), str(prefix)],
                capture_output=True, text=True, timeout=120,
            )
            if render.returncode or not image.exists():
                raise RuntimeError(f"PDF page {page} failed to render: {render.stderr[:150]}")
            result = subprocess.run([str(binary), str(image), "stdout", "-l", "eng", "--psm", "1"],
                                    capture_output=True, text=True, timeout=120, env=env)
            if result.returncode:
                raise RuntimeError(f"OCR failed for page {page}: {result.stderr[:150]}")
            chunks.append(result.stdout)
    if sum(len(chunk.strip()) for chunk in chunks) < 400:
        raise ValueError(f"OCR text remains sparse for {pdf}")
    CACHE.mkdir(parents=True, exist_ok=True)
    output.write_text("\f".join(chunks) + "\f", encoding="utf-8")
    return asset["asset_id"], pages, "ocr"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", type=Path, default=Path("/usr/bin/tesseract"))
    parser.add_argument("--tessdata", type=Path, default=Path("/usr/share/tesseract-ocr/5/tessdata"))
    parser.add_argument("--jobs", type=int, default=3)
    args = parser.parse_args()
    if not args.binary.exists() or not args.tessdata.exists():
        parser.error("Tesseract binary and English language data are required")
    data = json.loads((BASE / "catalog" / "index.json").read_text())
    assets = [a for a in data["assets"] if a["text_characters"] < 400]
    failures = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(ocr_one, a, args.binary, args.tessdata): a for a in assets}
        for future in as_completed(futures):
            a = futures[future]
            try:
                asset_id, pages, method = future.result()
                print(f"{asset_id}: {pages} pages {method}", flush=True)
            except Exception as error:
                failures.append({"asset_id": a["asset_id"], "error": str(error)})
                print(f"{a['asset_id']}: ERROR {error}", flush=True)
    if failures:
        raise SystemExit(json.dumps(failures, indent=2))


if __name__ == "__main__":
    main()
