# Approved-material reference scan

## Executive summary

The Approved set contains 115 resources. It contains 109 papers and six code repositories.

The paper scan found 27 cited works that are already in the canonical paper index but do not have a summary report. Seventeen are directly relevant to VALA. Ten are supporting references for search, seeding, mapping, or graph context.

The scan also found 33 additional algorithm or complexity references by exact title. These references are not in the canonical paper index. Most are relevant to VALA. They require metadata verification and source acquisition before they enter the main report set.

Do not promote a reference only because a textbook cites it. Promote it when its method changes a VALA decision marker or when an approved method paper independently supports it.

## Scan scope

- Approved resources: 115.
- Approved papers: 109.
- Approved code repositories: 6.
- PDFs with extractable text: 109.
- Distinct PDF files: 109.
- Reference sections found by an explicit heading: 58.
- PDFs scanned by the final 28 percent because no heading was extracted: 51.
- Existing report-paper titles found again in the approved reference regions: at least 71 of 132.

The citation count below is the number of Approved papers with an exact normalized title or DOI hit. It is not a general citation count. Two-column layouts and incomplete OCR can cause undercounting.

## Direct canonical gaps

Create summary reports for these works first. They change core alignment, LCS, edit-distance, traceback, storage, recurrence, encoding, exactness, or complexity decisions.

| Reference | Year | Approved-paper hits | VALA relevance |
|---|---:|---:|---|
| A General Method Applicable to the Search for Similarities in the Amino Acid Sequence of Two Proteins | 1970 | 20 | Foundational global dynamic programming and traceback. |
| The Longest Common Subsequence Problem Revisited | 1987 | 15 | Sparse LCS and match-pair processing. |
| An Improved Algorithm for Matching Biological Sequences | 1982 | 13 | Affine-gap dynamic programming. |
| Optimal Alignments in Linear Space | 1988 | 7 | Linear-space affine alignment and traceback. |
| A New Approach to Text Searching | 1992 | 7 | Bit-parallel approximate matching and encoding. |
| Striped Smith--Waterman Speeds Database Searches Six Times over Other SIMD Implementations | 2007 | 5 | SIMD layout and local-alignment speed. |
| Introducing Difference Recurrence Relations for Faster Semi-Global Alignment of Long Sequences | 2018 | 4 | Difference recurrence and semi-global alignment. |
| Algorithms for Approximate String Matching | 1985 | 3 | Output-sensitive approximate matching. |
| Optimal Sequence Alignment Using Affine Gap Costs | 1986 | 3 | Affine-gap scoring and exact alignment. |
| A Bit-String Longest-Common-Subsequence Algorithm | 1986 | 2 | Bit encoding for exact LCS. |
| Fast String Matching with k Differences | 1988 | 2 | Bounded-error search and wavefront-like frontiers. |
| Multiple Sequence Alignment Using Partial Order Graphs | 2002 | 1 | Graph representation for alignment. |
| A Subquadratic Sequence Alignment Algorithm for Unrestricted Scoring Matrices | 2003 | 1 | General scoring and subquadratic acceleration. |
| Edit Distance Cannot Be Computed in Strongly Subquadratic Time (Unless SETH Is False) | 2015 | 1 | Exact edit-distance complexity boundary. |
| Edlib: A C/C++ Library for Fast, Exact Sequence Alignment Using Edit Distance | 2017 | 1 | Exact bit-vector implementation baseline. |
| Block Aligner: An Adaptive SIMD-Accelerated Aligner for Sequences and Position-Specific Scoring Matrices | 2023 | 1 | Adaptive SIMD and position-specific scores. |
| Exact Global Alignment Using A* with Chaining Seed Heuristic and Match Pruning | 2024 | 1 | Exact A* search, chaining, pruning, and heuristic design. |

## Supporting canonical gaps

These works are relevant to implementation context. They are not direct substitutes for VALA's exact core unless VALA adopts their search or mapping model.

| Reference | Year | Approved-paper hits | VALA relevance |
|---|---:|---:|---|
| Basic Local Alignment Search Tool | 1990 | 8 | Heuristic local search and seed-and-extend. |
| PatternHunter: Faster and More Sensitive Homology Search | 2002 | 3 | Spaced seeds and sensitivity. |
| Fast Gapped-Read Alignment with Bowtie 2 | 2012 | 3 | Indexed seed-and-extend mapping. |
| Aligning Sequence Reads, Clone Sequences and Assembly Contigs with BWA-MEM | 2013 | 3 | MEM seeding and read mapping. |
| Minimap and Miniasm: Fast Mapping and De Novo Assembly for Noisy Long Sequences | 2016 | 2 | Minimizer-based long-read mapping. |
| Reducing Storage Requirements for Biological Sequence Comparison | 2004 | 1 | Minimizer storage and search reduction. |
| Adaptive Seeds Tame Genomic Sequence Comparison | 2011 | 1 | Adaptive seeding. |
| STAR: Ultrafast Universal RNA-seq Aligner | 2013 | 1 | Spliced-read mapping; domain-specific. |
| Fast and Sensitive Protein Alignment Using DIAMOND | 2015 | 1 | Protein database search; domain-specific. |
| Variation Graph Toolkit Improves Read Mapping by Representing Genetic Variation in the Reference | 2018 | 1 | Variation-graph mapping context. |

## Additional direct candidates

These exact titles occur in Approved reference regions and are not in the canonical paper index. Add them to the acquisition queue. Verify authors, year, venue, DOI, and exactness before report generation.

| Candidate | Approved-paper hits | Primary value to VALA |
|---|---:|---|
| The constrained longest common subsequence problem | 8 | Constrained-LCS problem definition and recurrence. |
| A simple algorithm for the constrained sequence problems | 8 | Constraint handling and exact dynamic programming. |
| Parallel algorithms for the longest common subsequence problem | 8 | Parallel decomposition and speed. |
| Quadratic conditional lower bounds for string problems and dynamic time warping | 4 | Complexity boundary for exact methods. |
| Two algorithms for LCS consecutive suffix alignment | 4 | Sparse and suffix-based alignment. |
| A bit-parallel, general integer-scoring sequence alignment algorithm | 3 | Bit encoding with general integer scores. |
| Tight hardness results for LCS and other sequence similarity measures | 3 | Fine-grained complexity boundary. |
| BitPal: a bit-parallel, general integer-scoring sequence alignment algorithm | 2 | Bit-parallel scoring implementation. |
| Increased bit-parallelism for approximate and multiple string matching | 2 | Encoding and machine-word parallelism. |
| New tabulation and sparse dynamic programming based techniques for sequence similarity problems | 2 | Sparse DP, tabulation, speed, and storage. |
| Multivariate fine-grained complexity of longest common subsequence | 2 | Parameter-sensitive complexity limits. |
| Sparse LCS common substring alignment | 2 | Sparse DP and common-substring anchors. |
| Algorithms for the constrained longest common subsequence problems | 2 | Exact constrained-LCS methods. |
| Longest common subsequence problem for unoriented and cyclic strings | 2 | Alternative sequence orientation and cyclic encoding. |
| A New Efficient Algorithm for Computing the Longest Common Subsequence | 2 | Exact LCS algorithm candidate. |
| Generalized string matching | 2 | Alternative matching model and metric scope. |
| Minimum detour methods for string or sequence comparison | 2 | Shortest-path heuristic related to A* alignment. |
| LCSk: A refined similarity measure | 1 | Alternative match criterion based on length-k substrings. |
| Vector algorithms for approximate string matching | 1 | Vector representation and approximate matching. |
| Astarix: Fast and optimal sequence-to-graph alignment | 1 | Exact graph alignment and A* heuristic. |
| Fast and optimal sequence-to-graph alignment guided by seeds | 1 | Seed-guided exact graph search. |
| Algorithms for colinear chaining with overlaps and gap costs | 1 | Chaining heuristic and gap-cost model. |
| Improved algorithms for approximate string matching | 1 | Approximate-search recurrence and speed. |
| TALCO: tiling genome sequence alignment using convergence of traceback pointers | 1 | Traceback convergence, tiling, and storage. |
| Incremental string comparison | 1 | Incremental recurrence and reuse. |
| Bit-parallel algorithm for the constrained longest common subsequence problem | 1 | Bit encoding for constrained LCS. |
| The substring inclusion constraint longest common subsequence problem can be solved in quadratic time | 1 | Constraint recurrence and exact complexity. |
| All highest scoring paths in weighted grid graphs and their application to finding all approximate repeats in strings | 1 | Exhaustive traceback over optimal paths. |

## Additional implementation candidates

These references are relevant when VALA evaluates vectorization, libraries, or biological local alignment. They are not immediate algorithm-definition sources.

| Candidate | Approved-paper hits | Primary value to VALA |
|---|---:|---|
| Faster Smith-Waterman database searches with inter-sequence SIMD parallelisation | 2 | SIMD lane organization and throughput. |
| SSW library: An SIMD Smith-Waterman C/C++ library for use in genomic applications | 2 | SIMD implementation baseline. |
| SWPS3: fast multi-threaded vectorized Smith-Waterman for IBM Cell/B.E. and x86/SSE2 | 1 | Threading and vectorization baseline. |
| BSAlign: A library for nucleotide sequence alignment | 1 | Library API and implementation comparison. |
| An overview of sequence comparison: Time warps, string edits, and macromolecules | 2 | Historical comparison of alignment metrics. |

## Code-repository references

The Approved code repositories add these relevant primary works.

| Repository | Reference | Decision |
|---|---|---|
| A*PA / A*PA2 | Exact Global Alignment Using A* with Chaining Seed Heuristic and Match Pruning | Add a paper report. The code report does not replace the method paper. |
| AStarix | Astarix: Fast and Optimal Sequence-to-Graph Alignment | Add a paper report. It changes graph search and heuristic design. |
| GWFA | Fast Sequence to Graph Alignment Using the Graph Wavefront Algorithm | Add a paper report. It changes graph, recurrence, and speed. |
| GWFA | Fast Parallel and Serial Approximate String Matching | Add to the direct candidate queue. It supplies the Landau--Vishkin basis. |
| PaSGAL | Accelerating Sequence Alignment to Graphs | Add a paper report. It changes graph DP, SIMD, and parallel execution. |
| GraphAligner | GraphAligner: Rapid and Versatile Sequence-to-Graph Alignment | No new report. The paper is already represented. |
| Rust pathfinding | No VALA-specific academic method paper was identified. | No addition. Keep as implementation background. |

## References not supported by this scan

These canonical-index entries were not found in the extracted reference regions of the Approved papers. Do not add them because of this scan alone.

- MMseqs2 Enables Sensitive Protein Sequence Searching for the Analysis of Massive Data Sets.
- Graph-Based Genome Alignment and Genotyping with HISAT2 and HISAT-genotype.
- Syncmers Are More Sensitive than Minimizers for Selecting Conserved k-mers in Biological Sequences.
- Effective Sequence Similarity Detection with Strobemers.
- Parameterized Syncmer Schemes Improve Long-Read Mapping.
- QuickEd: High-Performance Exact Sequence Alignment Based on Bound-and-Align.

## Decision rules

- Treat the direct canonical gaps as the first acquisition and reporting batch.
- Treat additional direct candidates as provisional until metadata is verified.
- Keep mapper, database-search, and SIMD-library papers as supporting evidence unless VALA adopts their execution model.
- Do not use textbook citations as independent proof of complexity or correctness.
- Do not create a second report for an identical paper or translated duplicate.
- Preserve exact and heuristic methods as separate evidence classes.

## Limitations

- PDF text extraction can reorder two-column bibliographies.
- OCR and line wrapping can hide a title or DOI.
- Citation counts can therefore be lower than the true count.
- This scan establishes relevance. It does not verify every theorem, complexity expression, license, or implementation claim.
