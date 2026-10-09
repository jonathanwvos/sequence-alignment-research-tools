# Pangenome graph construction from genome alignments with Minigraph-Cactus

- Work ID: `b-351e21b9af65`
- Asset ID: `a-7b2edfe5655ff8a8`
- Source PDF: `literature/academic-papers-processed/Pangenome graph construction from genome alignments with Minigraph-Cactus.pdf`
- SHA-256: `7b2edfe5655ff8a8c529fa9c56abc57f60643cde822a79c91e7371a7e2855913`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Minigraph-Cactus constructs pangenome graphs directly from genome assemblies. The authors demonstrate construction with 90 human haplotypes and with Drosophila melanogaster. (PDF p. 2).
- The pipeline combines minigraph structural-variant graphs with Cactus base alignment. Input haplotypes become paths through a graph that also contains small variants. (PDF p. 4).
- The authors report improved read mapping and variant analysis while retaining compatibility with existing pangenome tools. (PDF p. 9).

## Objectives

- Represent variation at base resolution while scaling graph construction to dozens or hundreds of vertebrate haplotypes. (PDF p. 4).
- Retain enough variation for analysis while producing graphs that current mapping and genotyping tools can use. (PDF p. 9).
- Measure how reference assembly quality and completeness affect pangenome analysis. (PDF p. 2).

## Arguments

- The authors argue that reference-based variant calls cannot adequately represent nested variation. Direct construction from assemblies avoids this intermediate representation. (PDF p. 3).
- The authors argue that one phylogenetic tree cannot represent all ancestry within a species because recombination changes relationships across the genome. (PDF p. 4).
- Keeping duplicated gene copies separate increases graph size but reduces path complexity and cycles. (PDF p. 4).

## Analysis

- Mapping every assembly back to the same completed structural-variant graph reduces inconsistent placements caused by mapping against successive graph versions. (PDF p. 4).
- Reference backbone choice affects graph topology and completeness, even when both GRCh38 and CHM13 are included as inputs. (PDF p. 9).
- Interpretation: the reported human variant-calling accuracy measures the full mapping and calling workflow. It does not isolate base-alignment accuracy. (PDF p. 14).

## Methods

- The workflow builds a minigraph structural-variant graph, maps assemblies to it, splits mappings by chromosome, performs Cactus alignment, and joins and processes the outputs. (PDF p. 3).
- Cactus joins exact matching bases into a sequence graph. It uses cactus-graph topology to filter short suspect chains, then aligns unaligned sequences between shared anchors. (PDF p. 4).
- The revised base aligner uses abPOA for alignments anchored at block ends. A greedy refinement step resolves overlaps between these alignments and determines rearrangement breakpoints. (PDF p. 13).
- hal2vg converts HAL alignments into sequence graphs. The vg deconstruct exporter uses snarls and indexed haplotype paths to produce phased VCF records. (PDF p. 14).

## Applications

- Graph outputs support short-read mapping with Giraffe, long-read mapping with GraphAligner and structural-variant genotyping with PanGenie. (PDF p. 9).
- HAL outputs support genome browser assembly hubs and annotation transfer between genomes. (PDF p. 4).
- The D. melanogaster study applies the graphs to short-read mapping, small-variant calling and structural-variant genotyping. (PDF p. 15).

## Optimization

- Chromosome decomposition increases parallelism and reduces peak memory per job. Toil supports local, cluster and cloud execution. (PDF p. 4).
- Replacing all-pairs interstitial alignment with abPOA changes scaling with sequence number from quadratic to linear. The authors also remove superlinear bottlenecks from alignment refinement. (PDF p. 13).
- The abPOA scoring uses LASTZ defaults with an added long-gap state. Short-gap open and extension costs are 400 and 30. Long-gap costs are 1,200 and 1, chosen through Alignathon experiments. (PDF p. 13).
- Heuristic filters remove uncertain chromosome assignments, mappings that imply deletions of at least 10 Mb, and weak overlapping mappings. (PDF p. 13).

## Evaluation and testing

- Human tests use 30× Illumina reads from HG001, HG002 and HG005. Giraffe pangenome mappings are compared with BWA-MEM and Giraffe mappings to linear references. (PDF p. 14).
- Projected mappings feed DeepVariant. Small-variant calls are evaluated with GIAB and CMRG truth sets using hap.py. CHM13-based tests exclude selected GRCh38 duplication and collapse regions. (PDF p. 14).
- The authors test the revised base aligner with unit and system tests. Long-read evaluation uses GraphAligner on HG002, HG003 and HG004 Hi-Fi reads and measures identity and split mappings. (PDF p. 14).
- The Drosophila mapping benchmark uses 100 independent DGRP samples with Illumina coverage above 15×. It compares Giraffe on the filtered pangenome with BWA-MEM on dm6. (PDF p. 8).

## Results

- For HG002 in the CMRG benchmark, CHM13-based and GRCh38-based pangenome workflows achieve F1 scores of 0.9830 and 0.9823. Dragen and BWA-MEM with DeepVariant achieve 0.9777 and 0.9756. (PDF p. 6).
- In Drosophila, an average of 41.1% of reads align perfectly to the pangenome, compared with 31.0% for BWA-MEM on dm6. The fraction with mapping quality above zero decreases from 81.1% to 80.0%. (PDF p. 8).
- Short-read genotyping detects 47.8% of the structural variants represented in the Drosophila pangenome across the 100 samples. (PDF p. 9).
- The 90-human pangenome alignments require nearly three days of cluster computation. (PDF p. 10).

## Limitations and uncertainty

- The pipeline requires at least one chromosome-level reference assembly. Graph quality depends on input assembly quality and completeness. (PDF p. 9).
- The HPRC construction excludes roughly 200 Mb per assembly, mostly centromeric sequence. The clipping threshold also reflects the 10 Kb alignment length limit used with abPOA. (PDF p. 13).
- The graphs omit interchromosomal events and cannot support centromere studies. The authors identify graph updates and reduced dependence on heuristic filtering as future work. (PDF p. 9).
- Projection to linear-reference formats can lose information in complex regions. The authors identify dependence on VCF as a barrier to fully graph-based analysis. (PDF p. 9).

## References

1. Li, H. Identifying centromeric satellites with dna-brnn. Bioinformatics 35, 4408–4410 (2019). (PDF p. 15)
2. Numanagic, I. et al. Fast characterization of segmental duplications in genome assemblies. Bioinformatics 34, i706–i714 (2018). (PDF p. 15)
3. Gao, Y. et al. abPOA: an SIMD-based C library for fast partial order alignment using adaptive band. Bioinformatics 37, 2209–2211 (2021). (PDF p. 15)
4. Earl, D. et al. Alignathon: a competitive assessment of whole-genome alignment methods. Genome Res. 24, 2077–2089 (2014). (PDF p. 15)
5. Garrison, E. & Guarracino, A. Unbiased pangenome graphs. Bioinformatics 39, btac743 (2023). (PDF p. 15)
6. Eizenga, J. M. et al. Efficient dynamic variation graphs. Bioinformatics 36, 5139–5144 (2020). (PDF p. 15)
7. Sirén, J., Garrison, E., Novak, A. M., Paten, B. & Durbin, R. Haplotype-aware graph indexes. Bioinformatics 36, 400–407 (2020). (PDF p. 15)
8. Mose, L. E., Wilkerson, M. D., Hayes, D. N., Perou, C. M. & Parker, J. S. ABRA: improved coding indel detection via assembly-based realignment. Bioinformatics 30, 2813–2815 (2014). (PDF p. 15)
9. Zook, J. M. et al. Extensive sequencing of seven human genomes to characterize benchmark reference materials. Sci. Data 3, 160025 (2016). (PDF p. 15)
10. Krusche, P. et al. Best practices for benchmarking germline small-variant calls in human genomes. Nat. Biotechnol. 37, 555–560 (2019). (PDF p. 15)
11. Cleary, J. G. et al. Comparing variant call files for performance benchmarking of next-generation sequencing variant calling pipelines. Preprint at bioRxiv https://doi.org/10.1101/023754 (2015). (PDF p. 15)
12. Li, H. et al. A synthetic-diploid benchmark for accurate variant-calling evaluation. Nat. Methods 15, 595–597 (2018). 54. broadinstitute/picard. https://github.com/broadinstitute/picard (PDF p. 15)
13. Kuhn, R. M., Haussler, D. & Kent, W. J. The UCSC Genome Browser and associated tools. Brief. Bioinform. 14, 144–161 (2012). (PDF p. 15)
14. English, A. C., Menon, V. K., Gibbs, R. A., Metcalf, G. A. & Sedlazeck, F. J. Truvari: refined structural variant comparison preserves allelic diversity. Genome Biol. 23, 271 (2022). (PDF p. 15)
15. Smit, A. F. A., Hubley, R. & Green, P. RepeatMasker Open-4.0. http://www.repeatmasker.org (2013–2015). Nature Biotechnology Article https://doi.org/10.1038/s41587-023-01793-w (PDF p. 15)
16. Danecek, P. et al. Twelve years of SAMtools and BCFtools. Gigascience 10, giab008 (2021). Acknowledgements We thank A. D. Long for many suggestions and insights regarding the D. melanogaster data and the whole vg team for their work to create and maintain vg, upon which much of this work depends. B.P., A.N., J.M.E. and J.M. were partly supported by National Institutes of Health (NIH) grants R01HG010485, U24HG010262, U24HG011853, OT3HL142481, U01HG010961 (with H.L.) and OT2OD033761. H.L. was partly supported by NIH grant R01HG010040 and T.M. by U01HG010973. Computational infrastructure and support for running PanGenie were provided by the Centre for Information and Media Technology at Heinrich Heine University Düsseldorf. Authorcontributions G.H., J.M., H.L. and B.P. designed the method. G.H., J.M. and J.E. contributed to the results and analysis. G.H., J.M., A.N., J.E. and B.P. wrote the mansuscript. All authors contributed to the software. B.P. led the project. Competinginterests The authors declare no competing interests. Additionalinformation Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41587-023-01793-w. Correspondence and requests for materialsshould be addressed to Glenn Hickey or Benedict Paten. Peer review information Nature Biotechnology thanks the anonymous reviewers for their contribution to the peer review of this work. Reprints and permissions informationis available at www.nature.com/reprints. (PDF p. 16)
