# Literature-review research tools

This directory is the consolidated, publication-facing snapshot of the tools and
derived material used to inspect the sequence-alignment corpus. Open
[`index.html`](index.html) to use the unified offline dashboard.

## Dashboard views

The dashboard contains five linked views and a manuscript review tool:

- [Catalog](index.html#view=catalog)
- [ASD-STE100 reports](index.html#view=reports)
- [Citation graph](index.html#view=graph)
- [Capability classifications](index.html#view=classifications)
- [Index review](index.html#view=audit)
- [Rendered paper and citation review](paper-review/index.html)

The older entry pages are retained as compatibility links:

- [`paper-publications.html`](paper-publications.html) opens the citation graph.
- [`paper-classifications/index.html`](paper-classifications/index.html) opens the classifications.
- [`reports/asd-ste100/index.html`](reports/asd-ste100/index.html) opens the reports.
- [`reports/asd-ste100/legacy.html`](reports/asd-ste100/legacy.html) preserves the earlier report viewer.

## Included material

- `index.html`: self-contained dashboard with the report, citation, audit, and
  classification payloads embedded in the page.
- `tools/`: report, catalog, OCR, and dashboard generation scripts.
- `catalog/`: work identities, extracted references, and audit data.
- `classification/`: controlled vocabulary, schemas, examples, and validation.
- `paper-classifications/`: classification builder and generated outputs.
- `reports/asd-ste100/current/`: 255 current AI-assisted reports for 255 PDF
  assets representing 252 locally held works. The catalog also records five
  bibliography works for which no local PDF is present.
- `paper-publications.json`: data from the earlier publication and citation
  viewer.
- `paper-review/`: rendered manuscript pages, citation previews, and a browser
  session for citation judgments and proposed additions.
- `MANIFEST.sha256`: checksums for every file in this snapshot.

The source PDFs are not duplicated here. They remain in
`literature/academic-papers-processed`, and the consolidated dashboard links to
that directory. Consequently, PDF links work when this directory remains in its
present repository location. The dashboard itself, including its embedded
reports and graphs, works without a web server.

## Reviewing manuscript citations

Open [the paper review viewer](paper-review/index.html). Hover over a highlighted
superscript to compare the PDF bibliography entry with the corresponding entry in
`Nature Vancouver References.md` and read an excerpt from the matched ASD report.
Click the superscript to record a judgment and note. Select words or click a
manuscript line, then open the reference-picker dropdown to browse all papers
alphabetically or type to filter the complete indexed corpus and numbered
reference list. Each selected source immediately becomes a citation chip for
that text; choose more sources to attach multiple references, or use a chip's
× button to remove one. **Add custom reference** handles sources not in the
picker. A paper already in the list saves its reference number; a
corpus-only paper saves its stable work ID and DOI for later bibliography
formatting. To remove an existing citation from the manuscript,
click that superscript and choose **Queue removal of this citation**. The marked
occurrence can be restored from the side panel. **Save review JSON** downloads
the additions, judgments, and removals. The static browser page does not write
to the manuscript. From the repository root, validate and then apply a saved
review with:

```sh
python3 'docs/Literature Review/Research Tools/paper-review/apply_review.py' /path/to/vala-manuscript-citation-review.json
python3 'docs/Literature Review/Research Tools/paper-review/apply_review.py' /path/to/vala-manuscript-citation-review.json --apply
```

The apply command checks the source hashes and exact citation positions, backs
up the original LaTeX, PDF, and JSON, removes only the selected occurrences,
rerenders the PDF with cached Tectonic resources, rebuilds the viewer, and marks
the JSON as applied. It does not remove bibliography entries or apply proposed
new citations. The viewer uses the rendered Draft 3 PDF as its source; rebuild it with
`python3 'docs/Literature Review/Research Tools/paper-review/build.py'` after
the PDF, LaTeX bibliography, or reference list changes. PDF page images and
source checksums make the saved locations reviewable against that exact version.
Ten of the 261 reference-list entries have no matched local ASD report; the
viewer identifies these rather than implying that a summary exists.

## Status of the ASD-STE100 reports

The reports are included because they document the screening and context-
acquisition process. They are supplementary research artefacts, not independent
academic sources. They were generated with AI assistance, subsequently reviewed,
and written in a controlled-language style based on ASD-STE100 Issue 9. The label
does not certify complete compliance with every ASD-STE100 rule.

When publishing the review, cite the underlying article for a scientific claim.
Describe these reports as AI-assisted working summaries and cite the archived
tool-and-data release only when discussing the review method or its
reproducibility.

## Maintenance

The active pipeline remains under the repository's top-level `literature/`
directory. This directory is a consolidated snapshot for the literature review;
regenerate the active dashboard there before refreshing this snapshot. Do not
commit source PDFs or licensed articles as part of a public supplementary
release unless their redistribution terms permit it.
