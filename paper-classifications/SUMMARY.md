# Processed-paper classification summary

Generated 24 September 2026 from the research-paper PDFs in `literature/academic-papers-processed`.

- PDFs classified: **255**
- Textbooks/protocol handbooks skipped at the user's direction: **0**
- Taxonomy fields available: **68** across **24** groups
- Papers with at least one screening warning: **12**
- Byte-identical duplicate groups: **0**

The counts below mean that an index was detected as relevant to a paper. They do not mean that undetected fields are unsupported or inapplicable.

## Coverage by index group

| Index group | Papers with a detected facet |
|---|---:|
| 01 Purpose | 215 |
| 02 Entities | 239 |
| 03 Representations | 108 |
| 04 Storage | 55 |
| 05 Preprocessing | 93 |
| 06 Entity comparator | 151 |
| 07 Sequence comparator | 148 |
| 08 Objective | 135 |
| 09 Alignment scope | 95 |
| 10 Scoring | 138 |
| 11 Solver | 160 |
| 12 Dynamic programming | 137 |
| 13 Reconstruction | 11 |
| 14 Graphs | 60 |
| 15 Graph operations | 40 |
| 16 Heuristics | 62 |
| 17 Guarantees | 123 |
| 18 Embeddings | 38 |
| 19 Learning | 29 |
| 20 Parallelism | 62 |
| 21 Numerics and resources | 154 |
| 22 Outputs | 58 |
| 23 Evaluation | 153 |
| 24 Reproducibility | 255 |

## Most frequent controlled values

| Dimension | Value | Papers |
|---|---|---:|
| `artifact.kind` | `paper` | 255 |
| `artifact.availability` | `local` | 255 |
| `task.role` | `alignment` | 172 |
| `entity.domain` | `dna` | 155 |
| `task.arity` | `sequence_sequence` | 154 |
| `entity.domain` | `protein` | 130 |
| `solver.family` | `dynamic_programming` | 121 |
| `entity.unit` | `amino_acid` | 98 |
| `entity.unit` | `character` | 93 |
| `evaluation.measure` | `recall` | 92 |
| `scoring.operation` | `insertion` | 82 |
| `entity.unit` | `base` | 79 |
| `scoring.operation` | `deletion` | 77 |
| `task.arity` | `multiple_sequences` | 77 |
| `resource.parameter` | `raw_lengths` | 72 |
| `entity_cmp.family` | `equality` | 71 |
| `dp.algebra` | `max_plus` | 70 |
| `guarantee.kind` | `exact` | 66 |
| `entity.domain` | `rna` | 65 |
| `objective.optimization` | `maximize` | 64 |
| `artifact.kind` | `source_code` | 60 |
| `sequence_cmp.family` | `lcs_length` | 59 |
| `objective.problem` | `lcs` | 59 |
| `artifact.availability` | `public` | 58 |
| `guarantee.evidence` | `stated_theorem` | 53 |
| `dp.algebra` | `min_plus` | 51 |
| `task.role` | `distance_estimation` | 48 |
| `objective.optimization` | `minimize` | 48 |
| `evaluation.measure` | `precision` | 48 |
| `sequence_cmp.family` | `edit_distance` | 47 |
| `scoring.operation` | `substitution` | 47 |
| `objective.problem` | `edit_distance` | 46 |
| `task.role` | `phylogeny` | 46 |
| `resource.parameter` | `sequence_count` | 46 |
| `entity.domain` | `structures` | 46 |
| `alignment.boundary` | `local` | 45 |
| `entity_cmp.family` | `substitution_table` | 43 |
| `alignment.multiplicity` | `one_to_one` | 41 |
| `entity.unit` | `kmer` | 39 |
| `sequence_cmp.family` | `percent_identity` | 39 |
| `alignment.boundary` | `global` | 38 |
| `sequence_cmp.family` | `alignment_score` | 37 |
| `evaluation.target` | `alignment_accuracy` | 36 |
| `embedding.use` | `alignment_training` | 34 |
| `representation.sequence` | `string` | 33 |
| `output.completeness` | `one_optimum` | 33 |
| `entity.unit` | `event` | 32 |
| `task.role` | `assembly` | 31 |
| `evaluation.target` | `runtime` | 30 |
| `evaluation.target` | `memory` | 30 |
| `task.role` | `read_mapping` | 30 |
| `dp.state` | `grid` | 28 |
| `scoring.gap` | `affine` | 28 |
| `evaluation.measure` | `throughput` | 28 |
| `guarantee.evidence` | `proof` | 25 |
| `solver.family` | `neural_inference` | 25 |
| `entity.alphabet` | `variable_finite` | 25 |
| `task.role` | `homology_search` | 25 |
| `scoring.substitution` | `blosum` | 25 |
| `parallel.backend` | `gpu` | 24 |

## Interpretation limits

This is an evidence-preserving screening index. It uses controlled lexical rules over extractable PDF text, removes reference sections where possible, and requires title/abstract/lead evidence or repeated body evidence. It can still classify a comparison target mentioned in an introduction, miss formulas or image-only text, or merge capabilities from several variants described by one paper. Review the evidence excerpt and source PDF before using a claim in an implementation or benchmark contract.

A blank matrix cell means **unverified by this screening pass**, not unsupported. Survey papers naturally receive broad classifications. Duplicate PDFs remain separate tabs because the requested unit was every file; identical SHA-256 groups are identified above.
