# ASD-STE100-style literature reports

> **Consolidated snapshot note:** `current/` contains the 255 reports used by
> the unified dashboard. The coverage figures and interaction instructions
> below describe the earlier 138-report collection preserved in `legacy.html`.

This directory contains one controlled-language report for each distinct local PDF source and one report for each retrieved reference-code repository.

The [`Approved-material reference scan`](APPROVED_REFERENCE_SCAN.md) records relevant works cited by resources marked Approved in the local review viewer.

## Static report viewer

Open [`index.html`](index.html) in a browser. Use the left and right arrow keys to move between reports. Use the Space key to cycle the current report through **Approved**, **Rejected**, **Uncertain**, and **Future work**. Use keys **1**, **2**, and **3** to assign the current resource to the respective implementation phase. The browser stores status and phase changes locally.

Use **Open PDF** or **Open code directory** above a report to open its related local resource in a new browser tab or the configured local file handler.

Use the sort control to restore index order or sort reports by publication date in either direction. Reports without a recorded publication year remain at the end of both date orders. The browser remembers the selected order locally.

The initial phase follows the report's VALA relevance: **Direct** is Phase 1, **Adjacent** is Phase 2, and **Background** or **Reference only** is Phase 3. A number-key assignment overrides this initial phase in the local browser.

## Reporting rules

- Use short sentences.
- Use one instruction per bullet.
- State evidence and uncertainty.
- Separate direct relevance from adjacent background.
- Do not treat a report as implementation approval.
- Verify formulas, proofs, data, licenses, and code before citation or integration.

## Coverage

- Distinct paper PDF hash groups: 132.
- Retained paper PDF files: 132.
- Reference-code reports: 6.
- Total reports: 138.

The retained corpus contains one PDF per content hash. Canonical copies are in `academic-papers` or `papers/open-access`. Byte-identical `inbox` copies were removed after hash verification.

## Approval use

Start with the report marked **Direct** when the paper addresses LCS, edit distance, or a closely related alignment method. Use **Adjacent** reports for domain or implementation context. Use **Background** reports only after the scope is accepted.

The reports are local working documents. They do not replace the canonical bibliography, the paper index, or a full technical reading.

## Change-profile schema

Each report starts with an executive summary and a method-focused abstract. An alignment-scope profile records whether the paper addresses LCS, local alignment, global alignment, or multiple-sequence alignment.

The complexity table contains only expressions found in the extractable paper text. A blank cell means that no explicit expression was found. The change profile covers traceback, graph model, metric, speed, storage, encoding, DP or recurrence, search, sequence count, exactness, and heuristic type.

`No change` means that no deviation is identified in the available local evidence. It does not certify implementation identity. Verify the paper or source code before approval.
