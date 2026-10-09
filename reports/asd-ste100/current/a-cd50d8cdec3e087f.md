# Fast and accurate de novo genome assembly from long uncorrected reads

- Work ID: `b-b98018c80db9`
- Asset ID: `a-cd50d8cdec3e087f`
- Source PDF: `literature/academic-papers-processed/Fast and accurate de novo genome assembly from long uncorrected reads.pdf`
- SHA-256: `cd50d8cdec3e087f79bf95024d1459feab757b3bf53d2fe730a0deb28dac8381`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Racon generates consensus sequences from raw reads, backbone sequences, and mappings. It uses SIMD-accelerated partial-order alignment. (PDF p. 1).
- Combined with minimap and miniasm, Racon supports genome assembly without prior read correction. (PDF p. 1).
- The authors report comparable assembly quality and substantial runtime reductions against Canu and FALCON on six long-read data sets. (PDF p. 2).

## Objectives

- Provide a fast consensus module that improves the sequence accuracy of assemblies built from uncorrected long reads. (PDF p. 1).
- Support multiple sequencing technologies and assembly pipelines through sequencer-independent input formats. (PDF p. 1).

## Arguments

- The authors argue that miniasm's speed is useful only if consensus generation can improve its sequence accuracy without a large runtime cost. (PDF p. 1).
- The authors attribute Racon's efficiency and robustness to SIMD acceleration of the partial-order alignment framework. (PDF p. 5).

## Analysis

- Sequence-to-graph alignment costs O((2np + 1)n|V|), where np is the average predecessor count, n is sequence length, and |V| is the graph node count. (PDF p. 7).
- The authors report linear runtime scaling with genome size at fixed read coverage. (PDF p. 2).
- Consensus generation dominates runtime for small genomes. Mapping and polishing can require substantial resources as the problem grows. (PDF p. 3).

## Methods

- The evaluated pipeline uses minimap for overlaps, miniasm for raw contigs, minimap for read-to-contig mappings, and Racon for consensus. Mapping and consensus can be repeated. (PDF p. 1).
- Consensus mode retains at most one mapping per read and removes mappings with excessive query-to-target length differences. Edlib alignments locate read chunks within backbone windows. (PDF p. 5).
- POA consensus construction processes graph nodes in topological order. It selects the highest-weight incoming edge at each node, records predecessor scores, and traces back from the highest-scoring node. (PDF p. 7).
- Error-correction mode uses read overlaps, retains multiple overlaps, and assigns threads per read rather than per window. (PDF p. 3).

## Applications

- Racon provides consensus generation and optional repeated polishing for PacBio and ONT assemblies. (PDF p. 1).
- Racon also corrects reads and can serve as a consensus or polishing module in other assembly pipelines. (PDF p. 5).

## Optimization

- SPOA places SIMD vectors along the query dimension of the dynamic programming matrix. It processes graph predecessors for each row and updates eight 16-bit cells per SIMD operation. (PDF p. 7).
- The implementation uses SSE 4.1 or later with 128-bit registers. It supports eight 16-bit values or four 32-bit values and vectorizes global, local, and semi-global alignment. (PDF p. 9).
- Optional overlapping windows extend each window by 10% at both ends. Adjacent results are aligned and clipped before consensus assembly. (PDF p. 3).

## Evaluation and testing

- Six public data sets cover Lambda phage, E. coli, yeast, and C. elegans with ONT or PacBio reads. (PDF p. 9).
- Dnadiff measures assembly size, aligned reference and query bases, and average identity. The tests also measure total pipeline time and maximum memory. (PDF p. 9).
- Corrected reads are aligned to the reference with GraphMap using anchorgotoh. Match, mismatch, insertion, and deletion counts measure correction quality. (PDF p. 9).
- Tests use Ubuntu systems with two six-core Xeon E5645 CPUs at 2.40 GHz and 12 threads where possible. Racon uses default settings except for a higher base-quality threshold on the ONT yeast data. (PDF p. 9).

## Results

- The miniasm+Racon pipeline is 5–301 times faster than Canu and 9–218 times faster than FALCON in the reported comparisons. (PDF p. 2).
- For PacBio E. coli, two Racon iterations reach 99.90% average identity. Canu reaches 99.99%, and FALCON reaches 99.90%. (PDF p. 2).
- On ONT E. coli, Nanopolish after Racon reaches 99.80% identity. Nanopolish takes 248.28 CPU hours after Racon versus 1561.80 CPU hours on raw miniasm contigs. (PDF p. 3).
- On ONT E. coli reads, Racon correction reduces the median error rate from 12.95% to 1.33% in 10 CPU hours. Nanocorrect reaches 0.60% in 8100 CPU hours. (PDF p. 4).

## Limitations and uncertainty

- Miniasm stores all overlaps in RAM. Long repetitive genomes can exhaust memory and cause the pipeline to fail. (PDF p. 5).
- Overlapping windows improve identity by up to 0.06 percentage points in all but one tested case, but add about 10–15% runtime and a window-overlap parameter. (PDF p. 3).
- The faster pipeline can require more memory. On C. elegans, miniasm+Racon uses 50.38 GB, compared with 10.16 GB for Canu and 7.59 GB for FALCON. (PDF p. 3).
- Interpretation: accuracy gains are not uniform across data sets. For ONT yeast, two Racon iterations reach 98.04% identity, below Canu at 98.61% and FALCON at 98.22%. (PDF p. 2).

## References

1. Berlin K, Koren S, Chin C-S, Drake JP, Landolin JM, Phillippy AM. 2015. Assembling large genomes with single-molecule sequencing and locali- ty-sensitive hashing. Nat Biotechnol 33: 623–630. (PDF p. 10)
2. Chaisson MJ, Tesler G. 2012. Mapping single molecule sequencing reads us- ing basic local alignment with successive refinement (BLASR): applica- tion and theory. BMC Bioinformatics 13: 238. Chin C-S, Alexander DH, Marks P, Klammer AA, Drake J, Heiner C, Clum A, (PDF p. 10)
3. Copeland A, Huddleston J, Eichler EE, et al. 2013. Nonhybrid, finished microbial genome assemblies from long-read SMRT sequencing data. Nat Methods 10: 563–569. Chin C-S, Peluso P, Sedlazeck FJ, Nattestad M, Concepcion GT, Clum A, (PDF p. 10)
4. Dunn C, O’Malley R, Figueroa-Balderas R, Morales-Cruz A, et al. 2016. Phased diploid genome assembly with single molecule real-time se- quencing. Nat Methods 13: 1050–1054. (PDF p. 10)
5. Delcher AL, Salzberg SL, Phillippy AM. 2003. Using MUMmer to identify similar regions in large sequence sets. Curr Protoc Bioinformatics Chapter 10: Unit 10.3. (PDF p. 10)
6. Gotoh O. 1982. An improved algorithm for matching biological sequences. J Mol Biol 162: 705–8. Istace B, Friedrich A, d’Agata L, Faye S, Payen E, Beluche O, Caradec C, (PDF p. 10)
7. Davidas S, Cruaud C, Liti G, et al. 2016. de novo assembly and popula- tion genomic survey of natural yeast isolates with the Oxford Nanopore MinION sequencer. bioRxiv doi: 10.1101/066613. (PDF p. 10)
8. Koren S, Walenz BP, Berlin K, Miller JR, Phillippy AM. 2017. Canu: scalable and accurate long-read assembly via adaptive k-mer weighting and re- peat separation. Genome Res (this issue). doi: 10.1101/gr.215087.116. (PDF p. 10)
9. Lee C. 2003. Generating consensus sequences from partial order multiple sequence alignment graphs. Bioinformatics 19: 999–1008. (PDF p. 10)
10. Lee C, Grasso C, Sharlow MF. 2002. Multiple sequence alignment using par- tial order graphs. Bioinformatics 18: 452–464. (PDF p. 10)
11. Li H. 2016. Minimap and miniasm: fast mapping and de novo assembly for noisy long sequences. Bioinformatics 32: 2103–2110. (PDF p. 10)
12. Loman NJ, Quick J, Simpson JT. 2015. A complete bacterial genome assem- bled de novo using only nanopore sequencing data. Nat Methods 12: 733–735. (PDF p. 10)
13. Loose M, Malla S, Stout M. 2016. Real-time selective sequencing using nano- pore technology. Nat Methods 13: 751–754. (PDF p. 10)
14. Myers G. 1999. A fast bit-vector algorithm for approximate string matching based on dynamic programming. J ACM 46: 395–415. (PDF p. 10)
15. Rognes T, Seeberg E. 2000. Six-fold speed-up of Smith-Waterman sequence database searches using parallel processing on common microproces- sors. Bioinformatics 16: 699–706. Šošić M, Šikić M. 2016. Edlib: A C/C++ library for fast, exact sequence align- ment using edit distance. bioRxiv doi: 10.1101/070649. Sović I, Križanović K, Skala K, Šikić M. 2016a. Evaluation of hybrid and non- hybrid methods for de novo assembly of nanopore reads. Bioinformatics 32: 2582–2589. Sović I, Šikić M, Wilm A, Fenlon SN, Chen S, Nagarajan N. 2016b. Fast and sensitive mapping of error-prone nanopore sequencing reads with GraphMap. Nat Commun 7: 11307. (PDF p. 10)
16. Ye C, Ma Z. 2016. Sparc: a sparsity-based consensus algorithm for long erro- neous sequencing reads. PeerJ 4: e2016. (PDF p. 10)
17. Received August 5, 2016; accepted in revised form January 17, 2017. Vaser et al. (PDF p. 10)
18. Genome Research www.genome.org (PDF p. 10)
