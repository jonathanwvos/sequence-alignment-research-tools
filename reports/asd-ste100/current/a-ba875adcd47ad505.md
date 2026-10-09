# Theseus: fast and optimal affine-gap sequence-tograph alignment

- Work ID: `w-ba875adcd47a`
- Asset ID: `a-ba875adcd47ad505`
- Source PDF: `literature/academic-papers-processed/Theseus: fast and optimal affine-gap sequence-tograph alignment.pdf`
- SHA-256: `ba875adcd47ad505c44f9bc5d76aaa26a98b17d596df74019018634db0c06a20`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors introduce Theseus, a sequence-to-graph aligner based on wavefront alignment (WFA) with affine gap costs. (PDF p. 1).
- Theseus introduces a Unified Coordinate System (UCS) to operate over sparse wavefronts across graph vertices. (PDF p. 3).

## Objectives

- Compute exact optimal affine-gap alignments of sequences to pangenome graphs in sub-quadratic time. (PDF p. 2).

## Arguments

- Wavefront propagation limits computation to active alignment frontiers, avoiding full graph dynamic programming. (PDF p. 5).

## Analysis

- Alignment throughput, memory usage, and peak memory consumption are measured across partial order alignment graphs. (PDF p. 8).

## Methods

- The Unified Coordinate System tracks and updates sparse diagonal wavefronts across active graph vertices. (PDF p. 7).
- A memory-efficient backtrace algorithm recovers optimal alignment paths directly from wavefront checkpoints. (PDF p. 3).

## Applications

- Partial order multiple sequence alignment and long-read mapping to variation graphs. (PDF p. 8).

## Optimization

- Active diagonal pruning restricts computation strictly to viable frontier states in active graph nodes. (PDF p. 5).

## Evaluation and testing

- Theseus is benchmarked against GraphAligner, Singletrack, and SPOA across diverse MSA datasets. (PDF p. 8).

## Results

- Theseus achieves 1.6x to 17.6x speedups over state-of-the-art sequence-to-graph aligners while maintaining exact optimality. (PDF p. 10).

## Limitations and uncertainty

- Dense variant bubbles and complex cyclic graph topologies increase active diagonal states in the UCS. (PDF p. 5).

## References

1. Genomes Project Consortium, Auton A, Brooks LD et al. A global reference for human genetic variation. Nature 2015; 526:68. Aguado-Puig Q, Doblas M, Matzoros C et al. WFA-GPU: gap-affine pairwise read-alignment using GPUs. Bioinformatics 2023; 39:btad701. Alonso-Mar� ın A, Fernandez I, Aguado-Puig Q et al. BIMSA: accel­ erating long sequence alignment using processing-in-mem­ ory. Bioinformatics 2024;40:btae631. Altschul SF. Gap costs for multiple sequence alignment. J Theor Biol 1989;138:297–309. (PDF p. 10)
2. Bioinformatics, 2026, Vol, 42, Issue 9 Downloaded from academic.oup.com/bioinformatics/article/42/9/btag561/8742314 by guest on 23 September 2026 Chin C-S, Wagner J, Zeng Q et al. A diploid assembly-based benchmark for variants in the major histocompatibility com­ plex. Nat Commun 2020;11:4794. Compeau PE, Pevzner PA, Tesler G. How to apply de bruijn graphs to genome assembly. Nat Biotechnol 2011;29:987–91. Computational Pan-Genomics Consortium. Computational pan- genomics: status, promises and challenges. Brief Bioinform 2018;19:118–35. Darby CA, Gaddipati R, Schatz MC et al. Vargas: heuristic-free alignment for assessing linear and graph read aligners. Bioinformatics 2020;36:3712–8. Doblas M, Lostes-Cazorla O, Aguado-Puig Q et al. Gmx: Instruction set extensions for fast, scalable, and efficient ge­ nome sequence alignment. In: Proceedings of the 56th Annual IEEE/ACM International Symposium on Microarchitecture, Toronto, ON, Canada. New York, NY, United States: Association for Computing Machinery, 2023, 1466–80. Doblas M, Lostes-Cazorla O, Aguado-Puig Q et al. Quicked: high- performance exact sequence alignment based on bound-and- align. Bioinformatics 2025a;41:btaf112. Doblas M, Shih PJ, Lostes-Cazorla O et al. Smx: heterogeneous architecture for universal sequence alignment acceleration. In: Proceedings of the 58th IEEE/ACM International Symposium on Microarchitecture, Seoul, Korea. New York, NY, United States: Association for Computing Machinery, 2025b, 1656–71. Edgar RC. Muscle: multiple sequence alignment with high accu­ racy and high throughput. Nucleic Acids Res 2004;32:1792–7. Eizenga JM, Novak AM, Sibbesen JA et al. Pangenome graphs. Annu Rev Genomics Hum Genet 2020;21:139–62. Gao Y, Liu Y, Ma Y et al. Abpoa: an simd-based c library for fast partial order alignment using adaptive band. Bioinformatics 2021;37:2209–11. Garrison E, Sirén J, Novak AM et al. Variation graph toolkit improves read mapping by representing genetic variation in the reference. Nat Biotechnol 2018;36:875–9. Goodwin S, McPherson JD, McCombie WR. Coming of age: ten years of next-generation sequencing technologies. Nat Rev Genet 2016;17:333–51. Gotoh O. An improved algorithm for matching biological sequen­ ces. J Mol Biol 1982;162:705–8. Gotoh O. Multiple sequence alignment: algorithms and applica­ tions. Adv Biophys 1999;36:159–206. Haghi A, Marco-Sola S, Alvarez L et al. WFA-FPGA: an efficient ac­ celerator of the wavefront algorithm for short and long read genomics alignment. Future Generation Computer Systems 2023;149:39–58. Hart PE, Nilsson NJ, Raphael B. A formal basis for the heuristic determination of minimum cost paths. IEEE Trans Syst Sci Cyber 1968;4:100–7. Ivanov P, Bichsel B, Mustafa H et al. Astarix: fast and optimal sequence-to-graph alignment. In: International Conference on Research in Computational Molecular Biology, Padua, Italy. Cham, Switzerland and Springer-Verlag Berlin, Heidelberg: Springer, 2020, 104–19. Jain C, Zhang H, Gao Y et al. On the complexity of sequence-to- graph alignment. J Comput Biol 2020;27:640–54. Kavya VNS, Tayal K, Srinivasan R et al. Sequence alignment on directed graphs. J Comput Biol 2019;26:53–67. Lee C, Grasso C, Sharlow MF. Multiple sequence alignment using partial order graphs. Bioinformatics 2002;18:452–64. Li H, Feng X, Chu C. The design and construction of reference pangenome graphs with minigraph. Genome Biol 2020;21:265. Liao W-W, Asri M, Ebler J et al. A draft human pangenome refer­ ence. Nature 2023;617:312–24. L� opez-Villellas L, Pineda-S� anchez E, Badouh A et al. Risc-v for ge­ nome data analysis: opportunities and challenges. In: 2023 38th Conference on Design of Circuits and Integrated Systems (DCIS), M� alaga, Spain. New York City, NY, USA: IEEE, 2023, 1–6. L� opez-Villellas L, Langarita-Ben� ıtez R, Badouh A et al. Genarchbench: a genomics benchmark suite for arm hpc pro­ cessors. Future Generation Computer Systems 2024;157:313–29. L� opez-Villellas L, I~ niguez C, Jiménez-Blanco A et al. Singletrack: an algorithm for improving memory consumption and perfor­ mance of gap-affine sequence alignment. Bioinformatics 2026; 42:btag183. https://doi.org/10.1093/bioinformatics/btag183 Marco-Sola S, Ribeca P. Efficient alignment of illumina-like high- throughput sequencing reads with the genomic multi-tool (GEM) mapper. Curr Protoc Bioinformatics 2015;50:11–3. Marco-Sola S, Sammeth M, Guig� o R et al. The gem mapper: fast, accurate and versatile alignment by filtration. Nat Methods 2012;9:1185–8. Marco-Sola S, Moure JC, Moreto M et al. Fast gap-affine pairwise alignment using the wavefront algorithm. Bioinformatics 2021;37:456–63. Marco-Sola S, Eizenga JM, Guarracino A et al. Optimal gap-affine alignment in o (s) space. Bioinformatics 2023;39:btad074. Miga KH, Wang T. The need for a human pangenome refer­ ence sequence. Annu Rev Genomics Hum Genet 2021; 22:81–102. Miller JR, Koren S, Sutton G. Assembly algorithms for next- generation sequencing data. Genomics 2010;95:315–27. Myers G. A fast bit-vector algorithm for approximate string match­ ing based on dynamic programming. J ACM 1999;46:395–415. Navarro G. Improved approximate pattern matching on hyper­ text. Theor Comput Sci 2000;237:455–63. Needleman SB, Wunsch CD. A general method applicable to the search for similarities in the amino acid sequence of two pro­ teins. J Mol Biol 1970;48:443–53. Rautiainen M, Marschall T. Graphaligner: rapid and versatile sequence-to-graph alignment. Genome Biol 2020;21:253. Rautiainen M, M€ akinen V, Marschall T. Bit-parallel sequence-to- graph alignment. Bioinformatics 2019;35:3599–607. Tettelin H, Riley D, Cattuto C et al. Comparative genomics: the bacterial pan-genome. Curr Opin Microbiol 2008;11:472–7. Van Dijk LR, Manson AL, Earl AM et al. Fast and exact gap-affine partial order alignment with POASTA. Bioinformatics 2024;41: btae757. https://doi.org/10.1093/bioinformatics/btae757 Vaser R, Sovi� c I, Nagarajan N et al. Fast and accurate de novo ge­ nome assembly from long uncorrected reads. Genome Res 2017;27:737–46. Zhang B, Zhu W, Diao S et al. The poplar pangenome provides insights into the evolutionary history of the genus. Commun Biol 2019;2:215. Zook JM, Catoe D, McDaniel J et al. Extensive sequencing of seven human genomes to characterize benchmark reference materials. Sci Data 2016;3:160025–6. Bioinformatics, 2026, Vol, 42, Issue 9 11 Downloaded from academic.oup.com/bioinformatics/article/42/9/btag561/8742314 by guest on 23 September 2026 © The Author(s) 2026. Published by Oxford University Press. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Bioinformatics, 2026, 42, 1–11 https://doi.org/10.1093/bioinformatics/btag561 Original Paper Downloaded from academic.oup.com/bioinformatics/article/42/9/btag561/8742314 by guest on 23 September 2026 (PDF p. 10)
