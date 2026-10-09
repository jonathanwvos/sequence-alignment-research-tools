# Processed-paper capability classifications

This folder classifies the research papers in `literature/academic-papers-processed` against the controlled indices in `literature/classification/dimensions.csv` and presents the results in a local static viewer. Textbooks and edited protocol handbooks are excluded at the user's direction; their exact filenames are listed in `SUMMARY.md` and the generated JSON metadata.

Open [index.html](index.html) directly in a browser. It embeds all classification data, so it works under `file://` without a web server. Each paper tab contains an encoded relative link to its local PDF. Search matches titles, filenames, dimensions, definitions and controlled values. The arrow keys move between visible papers, and `/` focuses search.

Files:

- `index.html`: generated self-contained viewer.
- `papers.json`: evidence-bearing records for every PDF.
- `classification-matrix.csv`: one row per PDF and one column per taxonomy field.
- `SUMMARY.md`: collection coverage, frequent values and duplicate-file groups.
- `build.py`: extraction, classification, output and validation logic.
- `viewer-template.html`: source template for the generated viewer.

Regenerate from the repository root with:

```sh
python3 literature/paper-classifications/build.py
```

The classifier weights title and abstract evidence most strongly, considers the opening pages, strips references where possible and accepts repeated non-reference body evidence. Each detected field preserves an evidence excerpt and a confidence label. Existing reports contribute summaries when their titles match, but classification values come from the PDFs.

This is a screening index. A missing value means unverified, not unsupported or inapplicable. Papers may describe several variants, surveys may discuss capabilities they do not implement, and image-only formulas may not be extractable. Use the viewer to open the source and verify the contract before selecting an implementation, comparison, or test.
