# Literature capability indices

Version 1.0 · 23 September 2026

Use **independent facets**, with one record for a **paper version, algorithm variant, pipeline stage and configuration**. A paper can contribute several records. This makes the classification useful for approval, implementation specifications and test selection without confusing an application's purpose with its algorithm.

The starting vocabulary has **24 groups, 68 fields and 32 proposed test families**, with **15 worked partial classifications** and **19 research sources**. It covers the existing classical sequence literature and extends into compressed algorithms, graphs, differentiable optimization, embeddings, learned alignment, alignment-free comparison and parallel execution. It does not classify the entire local collection.

## Files and quick use

| File | Use |
|---|---|
| [dimensions.csv](dimensions.csv) | Filterable data dictionary: field, definition, allowed terms, screening/detail priority |
| [EXAMPLES.md](EXAMPLES.md) | Scan the worked classifications and their distinctions |
| [examples.json](examples.json) | Evidence-bearing versions of those examples |
| [screening.csv](screening.csv) | Spreadsheet view of the examples; unknown capabilities remain `unverified` |
| [record-template.json](record-template.json) | Copy for a new paper/variant; all facets initially unverified |
| [record.schema.json](record.schema.json) | JSON Schema for valid fields, values and evidence requirements |
| [test-families.csv](test-families.csv) | Test specifications selected by capability, not executable tests |
| [SOURCES.md](SOURCES.md) / [sources.json](sources.json) | Research links, reading depth, versions and local PDF hashes |
| [validate.py](validate.py) | Check schema, vocabulary, records, references and optionally local source hashes |

For rapid approval screening, fill the `screen` fields that affect relevance first. Record unavailable details as unverified and return to `detail` fields when preparing a specification. No paper must use every capability. Start with purpose, input shape, objective, output and guarantee; these determine whether the remaining details merit investigation.

A compact display can read:

> LCS · sequence/sequence · equality · divide-and-conquer DP · one subsequence

This is a display summary, not a unique identifier or execution string. Keep the detailed evidence behind it.

## The index groups

| Group                  | What to capture                                             | Representative terms or distinctions                                                                           |
| ---------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 01 Purpose             | Application and input arity                                 | Mapping vs comparison vs storage coding; one sequence, pair, profile, MSA, sequence/graph                      |
| 02 Entities            | Domain, alphabet assumptions, comparison unit               | DNA/RNA/protein/text/time series; binary/ordered/continuous/set-valued; base/codon/k-mer/run/vector            |
| 03 Representations     | Symbol and sequence representations; information preserved  | Character, bit set, one-hot, dense vector, tensor, profile, graph; lossless vs collapsed/quantized             |
| 04 Storage             | Compression, computation domain and container               | RLE, packed bits, grammar, LZ, BWT; direct compressed computation vs decompression; FASTA is a format          |
| 05 Preprocessing       | Transforms, indexes and reuse                               | Masking, translation, embeddings; minimizers, suffix/FM indexes, sketches; per pair vs reusable database       |
| 06 Entity comparator   | Function, codomain, context and properties                  | Equality, overlap, ordering, substitution lookup, cosine, learned score; Boolean vs real                       |
| 07 Sequence comparator | Aggregate function and established properties               | LCS length, edit score, DTW, OT, Jaccard/sketch estimate, likelihood; metric vs similarity                     |
| 08 Objective           | Mathematical target, optimization direction and constraints | LCS/LIS/substring, weighted alignment, DTW/OT, Viterbi; min/max/count; anchors/splicing/bands                  |
| 09 Alignment scope     | Boundaries, participation and assembly strategy             | Global/local/four-end policies; many-to-one; progressive/refined/joint MSA                                     |
| 10 Scoring             | Substitutions, gaps, operations and scale                   | BLOSUM/PAM/PSSM/learned; affine/two-piece; transpositions/frame shifts; cost vs reward                         |
| 11 Solver              | Computational mechanism                                     | DP, Four Russians, bit parallel, WFA, A*, OT/Sinkhorn, FFT, ILP, metaheuristics                                |
| 12 Dynamic programming | States, algebra, layout, schedule and differentiation       | Grid/frontier/graph product; min-plus/max-plus/sum-product; rolling rows, tabulation, smoothing                |
| 13 Reconstruction      | Recovery algorithm and tie behavior                         | Parent pointers, recomputation, divide-and-conquer; one/all/top-k/capped                                       |
| 14 Graphs              | Role, topology, labels and permitted paths                  | Reference vs edit-state vs match graph; DAG/cyclic/bidirected; arbitrary walks vs haplotypes                   |
| 15 Graph operations    | Construction, traversal and its purpose                     | Sequence-to-path/POA/de Bruijn/match-to-graph; DFS/topological/A*; scoring vs enumeration                      |
| 16 Heuristics          | Guidance, pruning and correctness safeguards                | Seeds/chaining/bands/X-drop/beam; admissible bounds, certificates, exact fallback                              |
| 17 Guarantees          | Result guarantee and evidence type                          | Exact objective, exact restricted domain, bounded approximation, probabilistic, heuristic; proof vs experiment |
| 18 Embeddings          | Level, origin and use                                       | Residue/context/sequence/graph; handcrafted/PLM; score, retrieval, alignment training                          |
| 19 Learning            | Regime, learned component and alignment form                | Supervised/self-supervised/frozen; embedding/gap/heuristic; hard/soft/latent                                   |
| 20 Parallelism         | Work decomposition, backend and communication               | Entity pairs vs dependent DP stages vs sequence pairs; SIMD/GPU; transfers/barriers                            |
| 21 Numerics/resources  | Arithmetic, cost model and complexity parameters            | Overflow/rounding; word RAM vs comparison; raw length, runs, score, nodes, outputs                             |
| 22 Outputs             | Native return type and completeness                         | Scalar, witness, all strings/positions/paths, CIGAR, soft matrix, posterior, gradient                          |
| 23 Evaluation          | Validation target and empirical measure                     | Optimal-score checks vs alignment accuracy; SP/TC, recall, runtime, RSS/VRAM, energy                           |
| 24 Reproducibility     | Artifacts and access                                        | Paper/version/errata, code, weights, data; local/public/subscription/unavailable                               |

The vocabulary is a starting controlled vocabulary, not a closed theory of all sequence methods. Add a term when a source needs it; give it a definition and update the corresponding schema enum. Do not use a vague `other` tag to hide a scientifically meaningful difference. Exact formulae and restrictions belong in `contracts`, not an ever-growing list of tags.

## Distinctions that make the indices reliable

**Domain, representation and compression are separate.** A DNA sequence can use character symbols, a four-bit ambiguity set, a tensor representation and an RLE storage scheme. Lossless RLE retains `(symbol, count)`; homopolymer collapse discards counts. A compressed file need not imply an algorithm that works directly on compressed data. Minimap2's documented HPC seeding is a useful example of why these need separate fields. [Official documentation](https://github.com/lh3/minimap2)

`binary` can describe a two-symbol alphabet or a bit-level representation of a larger alphabet. `run` can describe a computational unit without changing the underlying biological entity. DNA **data storage coding** is an application in which payload bits are encoded into constrained DNA; record the code rate, channel/error model, GC/run constraints and decoding objective in the contracts. It is distinct from storing a biological DNA string compactly.

**Entity comparators and sequence comparators are different functions.** Record an entity function as `f(a_i,b_j; context) -> value`, then the sequence-level aggregation as `F(A,B; configuration) -> result`. Useful precise examples are:

| Function | Meaning | Required detail |
|---|---|---|
| `a == b` | Literal equality | Alphabet, case, unknown-symbol behavior |
| `(mask(a) & mask(b)) != 0` | Ambiguity-set overlap | Bit basis and whether the return is a Boolean or an overlap value |
| `a < b` | Ordered comparison, e.g. LIS | Strict/non-strict order and repeated-element assumptions |
| `M[a,b]` or `P[i,b]` | Substitution or position-specific score | Table/version, orientation, gap conventions |
| `dot(u,v)/(norm(u)*norm(v))` | Cosine similarity | Embedding source, normalization, zero-vector policy |
| `opt_path sum(local_scores)` | Sequence alignment objective | Legal transitions, boundaries, score signs and tie rules |

Set overlap is not generally transitive: `A` overlaps `N`, and `N` overlaps `C`, while `A` does not overlap `C`. Do not transfer equality-based proofs to a replacement comparator without checking their assumptions.

**An objective, a similarity and an evaluation metric are separate.** A method may optimize an alignment score and be evaluated using alignment recall. Percent identity needs a denominator and gap policy. Arbitrary scores, DTW variants, embedding similarities and OT constructions do not automatically satisfy the mathematical metric axioms. Even soft-DTW needs care about self-distance and nonnegativity. [Differentiable Divergences Between Time Series](https://arxiv.org/abs/2010.08354)

**“LCS”, “local”, “learned” and “sequence-to-graph” are independent labels.** They identify an objective, a boundary policy, how a component was obtained, and an input shape. A learned residue score can be used by an ordinary DP aligner. A differentiable training surrogate can differ from the hard inference objective. For every concrete record, state which stage and configuration its claims describe.

**Match matrices are not accumulated DP tables.** Computing `C[i,j]=f(a_i,b_j)` may expose independent comparisons. An accumulated table `D[i,j]` depends on predecessor states. Matrix/tensor storage alone establishes neither DP nor full-pipeline parallelism. Similarly, an anti-diagonal execution schedule is not the score-indexed wavefront algorithm: distinguish `dp.schedule=antidiagonal` from `dp.state=score_frontier`.

**Graph role precedes graph traversal.** Conventional pairwise DP can be interpreted as an implicit edit-state graph without accepting a biological graph as input. An explicit match graph, a guide tree, a profile HMM and a pangenome reference are different objects. Name the graph in `graph_identity_and_paths`; if a pipeline uses several graphs, give each claim a clear locator and note, or split stage records. A profile HMM's Viterbi optimum and its sum-product marginal are different objectives. An exact insertion into a fixed POA graph does not imply a globally optimal progressive MSA. [POASTA](https://doi.org/10.1093/bioinformatics/btae757)

**Heuristics do not automatically negate exactness.** An admissible A* heuristic or proved safe pruning can preserve the declared optimum. A band can be exact under a certificate or fallback. Conversely, an exact extension kernel does not certify the seeding and candidate selection of a whole mapper. Store restrictions, safeguards and evidence at the stage where they apply.

**Output is part of the algorithm contract.** A length, one witness, all distinct optimal strings and all optimal positional alignments have different costs and validation rules. For `AA` versus `A`, there is one distinct LCS string but two positional alignments. For `AG` versus `GA`, `A` and `G` are different valid LCS strings. Output enumeration can be exponential. A cap changes completeness; a score-only implementation does not acquire traceback support merely because its recurrence could be extended. The score-focused Accelign library makes that distinction concrete. [Accelign](https://doi.org/10.1186/s12859-026-06521-0)

## Evidence and record rules

Every nontrivial classification belongs to a source, page/section/equation, version and scope. `sources.json` supplies source IDs; records and individual claims reference them. Local paths are relative to the repository root and refer to the renamed processed PDFs. They are intentionally independent of older paths in `paper-index.csv`.

| Claim status | Meaning |
|---|---|
| `supported` | Evidence supports the listed value in this record's configuration |
| `conditional` | Supported only under the explicit `condition` |
| `unsupported` | Evidence explicitly rules out the listed capability for this version/configuration |
| `not_reported` | The inspected source scope did not report it; record that scope |
| `not_applicable` | The facet does not apply; explain why |
| `unverified` | Not yet checked or insufficient evidence |
| `conflicting` | Sources disagree; cite both and explain the conflict |

`basis=explicit` distinguishes an author's statement from `basis=inferred`, your reasoned interpretation. A tag's evidence status is independent of `guarantee.kind`: an explicitly stated heuristic method is well-supported evidence about a heuristic method. Abstract-only inspection cannot establish a negative capability claim from silence.

Unverified/not-reported/not-applicable claims have empty `values`. A missing claim also means unverified, never false. Supported, conditional, unsupported and conflicting claims require values, source IDs and a locator. Conditional claims require a condition. The full template starts every field as unverified. The examples omit most unknown fields for readability.

Multi-value tags do not imply that all combinations work. Split affine/local/GPU/precision variants when support differs. Use claim notes for alternative values and known interactions. Exact comparator formulae, all four free-end flags, gap formulae, numeric limits, graph path semantics, embedding weights/layers/pooling/windows, and training/evaluation data splits belong in `contracts`. Null means not specified yet. Where asymmetry matters, retain input orientation.

Keep these identities separate: bibliographic work → paper version → algorithm/stage/configuration → implementation revision → dataset/run. A source repository may gain capabilities after publication. A local modification needs a parent and a changed-contract explanation; it does not silently update the paper's capabilities. Confirm errata before treating a published algorithm as a correctness oracle.

## Using the indices for prioritization and comparison

Review priority is a vector, not a speed ranking. The template provides eight independent fields, initially `unassessed`:

| Priority field | High means |
|---|---|
| Relevance | Directly answers a current research question |
| Evidence readiness | Full specification, assumptions and corrections are accessible |
| Comparison compatibility | Same input/objective/scoring/boundary/output contract, or a proved reduction |
| Mechanism novelty | Adds a computational mechanism or capability absent from the reviewed set |
| Implementation effort | Substantial work; unlike the other fields, high is a cost |
| Dependency readiness | Required representations, data and infrastructure are available |
| Oracle readiness | Independent exact/reference checks are feasible |
| Resource fit | Expected workloads fit the available hardware and output budget |

Record the rationale instead of assigning arbitrary numerical weights. This supports separate queues for immediate comparable baselines, optimization alternatives, and later capability extensions. Suggested review order, subject to the existing portfolio: establish classical objective/output contracts first; then examine optimizations under compatible contracts; then graph, learned, MSA and representation extensions. These are review categories, not algorithm approval or a development schedule.

Before grouping methods for a comparison, resolve this contract:

1. Domain, alphabet, input orientation, normalization and information lost by encoding.
2. Entity comparator, objective, exact substitution/gap parameters and legal operations.
3. Boundary flags, anchors, bands, graph paths and other feasibility constraints.
4. Native output universe, tie policy, completeness and score-to-output relation.
5. Numeric policy, exactness/approximation conditions and failure/incomplete status.
6. Workload, preprocessing reuse, implementation version and resource accounting.

A known reduction can justify score comparison without implying witness equivalence. For the Masek–Paterson LCS cost specialization, insertion/deletion cost 1 and substitution cost 2 give `d(A,B)=|A|+|B|-2*LCS_length(A,B)`. Hirschberg Algorithm C returns a subsequence; Fredman instead studies LIS length in one ordered sequence. [Worked examples and sources](EXAMPLES.md)

Heuristic methods need quality-versus-resource evaluation under the same target; learned methods need held-out evaluation and leakage controls. These are proposed evaluation requirements for the user's comparison framework, not completed experiments or changes to the existing analysis pipeline.

Preserve VALA's existing four-token execution grammar, including `TENSOR__POINTWISE_AND__TTF_M1__UNIQUE_PATHS`. Store it unchanged in `implementation_identity.exec_str` when classifying that implementation. The taxonomy supplements this identity; it does not replace it. Encoding/operator/graph/trace facets can describe the four components, while revision, scoring and hardware remain separate. The [implementation portfolio](../IMPLEMENTATION_PORTFOLIO.md) continues to govern development approval and ownership.

## Complexity and test selection

Store each complexity claim by phase and measure, with parameter definitions and assumptions. Use unambiguous names: raw lengths `m,n`; run counts `rA,rB`; matching pairs `R`; optimal cost `s`; alphabet size `sigma`; word width `w`; embedding dimension `d`; graph sizes `V,E`; sequence count `q`; output size `z`. Preserve the paper's original notation in evidence notes. Record preprocessing and amortization; auxiliary space, total space, RSS and VRAM are different quantities.

Separate startup/loading, preprocessing, transfers, kernel computation, reconstruction and serialization. Record training cost separately from inference. Score-only memory bounds do not establish witness-reconstruction bounds. GCUPS is not a universal efficiency measure for methods that intentionally avoid evaluating the full grid.

Choose [test families](test-families.csv) from capabilities: encoding → T01–T03; comparators/objectives/outputs → T04–T12; pruning/graphs → T13–T18; differentiability/OT/learning → T19–T23; numeric/parallel/performance → T24–T26; sketches/MSA/LIS/restricted costs/pipelines → T27–T31; provenance → T32. Each example has a proposed selection. These are specifications for future tests; no algorithm or database jobs were executed for this classification work.

Validation of these metadata files uses Python's `jsonschema` package, available in the current environment:

```sh
python3 literature/classification/validate.py --check-sources
```

This checks structural validity, vocabulary agreement, evidence/source/test references, duplicate facet records, the screening projection, negative schema probes, local paths and source hashes. It does not verify a paper's scientific claims or prove an algorithm correct.
