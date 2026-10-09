# GraphAligner: Rapid and Versatile Sequence-to-Graph Alignment

- Work ID: `b-66704afd436c`
- Asset ID: `a-ffb0ee43bb629f16`
- Source PDF: `literature/academic-papers-processed/GraphAligner: Rapid and Versatile Sequence-to-Graph Alignment - Rautiainen, Marschall.pdf`
- SHA-256: `ffb0ee43bb629f168b4729c7347a0916381f4d68458f2284e50ddf4d68e5b469`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- GraphAligner aligns long reads to sequence graphs with a seed-and-extend method and bit-parallel banded dynamic programming. (PDF p. 9).
- The authors report a 13-fold runtime improvement over vg on variation graphs. Their human-read correction pipeline more than halves the error rate relative to FMLRC. (PDF p. 8).

## Objectives

- Provide a general graph alignment tool that can align noisy long reads to whole-human-genome de Bruijn graphs. (PDF p. 2).

## Arguments

- The authors argue that full dynamic programming is unsuitable for aligning many reads to large graphs, even with their earlier bit-parallel acceleration. (PDF p. 2).
- The minimizer seeding strategy relies on long reads spanning simple graph regions. Short reads can remain entirely within regions with dense variation. (PDF p. 2).

## Analysis

- The authors attribute most residual correction errors to uncorrected regions with insufficient short-read coverage. (PDF p. 8).
- The authors hypothesize that FMLRC's alignment method limits correction in complex genomes. They suggest that its two-pass approach could otherwise improve correction. (PDF p. 8).

## Methods

- Seeds match read sequences to graph node sequences. Each seed is extended independently with bit-parallel banded dynamic programming. (PDF p. 9).
- Worker threads align one read at a time. Separate input and output threads read sequences and write selected primary and supplementary alignments. (PDF p. 9).
- GraphAligner accepts GFA and vg formats. It supports graphs with overlapping or non-overlapping node sequences. (PDF p. 9).

## Applications

- A graph-based pipeline corrects long reads from E. coli, fruit fly, and human data. A clipped mode retains corrected read regions. (PDF p. 8).
- A genotyping pipeline sends GraphAligner alignments to vg pack and vg call. It uses the default vg genotyping method for sample HG002. (PDF p. 25).
- The authors report use of GraphAligner to map long-read RNA-seq data to splice graphs. (PDF p. 9).

## Optimization

- Minimizer seeding and banded graph alignment restrict the alignment work instead of computing the full dynamic programming table. (PDF p. 2).
- Bit-parallel extension and independent worker threads accelerate read alignment. (PDF p. 9).

## Evaluation and testing

- The linear benchmark uses 20-fold simulated GRCh38 coverage from pbsim. Reads shorter than 1,000 bases or containing non-ATCG characters are removed. (PDF p. 3).
- The variation benchmark uses a GRCh37 chromosome 22 graph with 2,212,133 Thousand Genomes variants. A mapping counts as correct when its longest alignment overlaps at least 10% of the source interval. (PDF p. 3).
- Comparisons use 40 threads, GraphAligner 1.0.11, minimap2 2.17-r941, and vg 1.23.0. Resource use is measured with /usr/bin/time -v. (PDF p. 24).
- Correction evaluation removes reads shorter than 500 bases, maps the remaining reads with minimap2, and obtains alignment statistics from samtools stats. (PDF p. 8).

## Results

- On the linear benchmark, GraphAligner maps 95.0% of reads correctly, compared with 95.1% for minimap2. CPU times are about 127 and 44 hours, with peak memory of 72.1 and 20.0 GB. (PDF p. 3).
- For HG00733 correction, GraphAligner obtains a 3.3510% error rate versus 7.1210% for FMLRC. CPU time falls from about 2,222 to 175 hours, and peak memory falls from 234.5 to 76.7 GB. (PDF p. 8).
- Clipped GraphAligner correction lowers the HG00733 error rate to 1.3503%. Read N50 also falls from 32,879 bases in standard correction to 7,973 bases. (PDF p. 8).

## Limitations and uncertainty

- The current seeding strategy can systematically miss short reads in regions with dense variation. (PDF p. 8).
- The vg comparison measures interval overlap, not full alignment correctness. Paths inconsistent with graph topology can still count as correct, and vg preprocessing time is excluded. (PDF p. 24).
- For E. coli, standard GraphAligner correction has a higher error rate than FMLRC: 0.5057% versus 0.3016%. (PDF p. 8).

## References

1. Computational Pan-Genomics Consortium. Computational pan-genomics: status, promises and challenges. Brief Bioinforma. 2016;19(1):118–35. (PDF p. 26)
2. Paten B, Novak AM, Eizenga JM, Garrison E. Genome graphs and the evolution of genome inference. Genome Res. 2017;27(5):665–76. (PDF p. 26)
3. Bankevich A, Nurk S, Antipov D, Gurevich AA, Dvorkin M, Kulikov AS, Lesin VM, Nikolenko SI, Pham S, Prjibelski AD, et al. SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing. J Comput Biol. 2012;19(5):455–77. (PDF p. 26)
4. Antipov D, Korobeynikov A, McLean JS, Pevzner PA. hybridSPAdes: an algorithm for hybrid assembly of short and long reads. Bioinformatics. 2015;32(7):1009–15. (PDF p. 26)
5. Wick RR, Judd LM, Gorrie CL, Holt KE. Unicycler: resolving bacterial genome assemblies from short and long sequencing reads. PLoS Comput Biol. 2017;13(6):1005595. (PDF p. 26)
6. Salmela L, Rivals E. LoRDEC: accurate and efficient long read error correction. Bioinformatics. 2014;30(24):3506–14. (PDF p. 26)
7. Miclotte G, Heydari M, Demeester P, Rombauts S, Van de Peer Y, Audenaert P, Fostier J. Jabba: hybrid error correction for long sequencing reads. Algorithm Mol Biol. 2016;11(1):10. (PDF p. 26)
8. Wang JR, Holt J, McMillan L, Jones CD. FMLRC: hybrid long read error correction using an FM-index. BMC Bioinformatics. 2018;19(1):50. (PDF p. 26)
9. Dolzhenko E, Deshpande V, Schlesinger F, Krusche P, Petrovski R, Chen S, Emig-Agius D, Gross A, Narzisi G, Bowman B, et al. ExpansionHunter: a sequence-graph based tool to analyze variation in short tandem repeat regions. Bioinformatics (Oxford, England). 2019;35:4754–6. (PDF p. 26)
10. Hickey G, Heller D, Monlong J, Sibbesen JA, Siren J, Eizenga J, Dawson E, Garrison E, Novak A, Paten B. Genotyping structural variants in pangenome graphs using the vg toolkit. Genome Biol. 2020;21:35. https://doi.org/ 10.1186/s13059-020-1941-7. (PDF p. 26)
11. Garg S, Rautiainen M, Novak AM, Garrison E, Durbin R, Marschall T. A graph-based approach to diploid genome assembly. Bioinformatics. 2018;34(13):105–14. (PDF p. 26)
12. Altschul SF, Gish W, Miller W, Myers EW, Lipman DJ. Basic local alignment search tool. J Mol Biol. 1990;215(3): 403–410. (PDF p. 26)
13. Li H. Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics. 2018;34(18):3094–100. (PDF p. 26)
14. Li H, Durbin R. Fast and accurate short read alignment with Burrows–Wheeler Transform. bioinformatics. 2009;25(14):1754–60. (PDF p. 26)
15. Sović I, Šikić M, Wilm A, Fenlon SN, Chen S, Nagarajan N. Fast and sensitive mapping of nanopore sequencing reads with graphmap. Nat Commun. 2016;7:11307. (PDF p. 26)
16. Garrison E, Sirén J, Novak AM, Hickey G, Eizenga JM, Dawson ET, Jones W, Garg S, Markello C, Lin MF, et al. Variation graph toolkit improves read mapping by representing genetic variation in the reference. Nat Biotechnol. 2018;46:875–9. (PDF p. 26)
17. Navarro G. Improved approximate pattern matching on hypertext. Theor Comput Sci. 2000;237(1):455–63. (PDF p. 26)
18. Equi M, Grossi R, Tomescu AI, Mäkinen V. On the complexity of exact pattern matching in graphs: determinism and zig-zag matching. arXiv preprint arXiv:1902.03560. 2019. (PDF p. 26)
19. Lee C, Grasso C, Sharlow MF. Multiple sequence alignment using partial order graphs. Bioinformatics. 2002;18(3): 452–64. (PDF p. 26)
20. Kavya VNS, Tayal K, Srinivasan R, Sivadasan N. Sequence alignment on directed graphs. J Comput Biol. 2019;26(1): 53–67. (PDF p. 26)
21. Limasset A, Cazaux B, Rivals E, Peterlongo P. Read mapping on de bruijn graphs. BMC Bioinformatics. 2016;17(1):237. (PDF p. 26)
22. Jain C, Zhang H, Gao Y, Aluru S. On the complexity of sequence to graph alignment. bioRxiv. 2019. https://doi.org/10.1101/522912. (PDF p. 26)
23. Rautiainen M, Mäkinen V, Marschall T. Bit-parallel sequence-to-graph alignment. Bioinformatics. 2019. https://doi.org/10.1093/bioinformatics/btz162. (PDF p. 26)
24. Myers G. A fast bit-vector algorithm for approximate string matching based on dynamic programming. J ACM (JACM). 1999;46(3):395–415. (PDF p. 26)
25. Liu B, Guo H, Brudno M, Wang Y. deBGA: read alignment with de bruijn graph-based seed and extension. Bioinformatics. 2016;32(21):3224–32. (PDF p. 26)
26. Durbin R. Efficient haplotype matching and storage using the positional Burrows–Wheeler Transform (pbwt). Bioinformatics. 2014;30(9):1266–72. (PDF p. 26)
27. Sirén J, Välimäki N, Mäkinen V. IEEE/ACM Trans Comput Biol Bioinforma (TCBB). 2014;11(2):375–88. (PDF p. 26)
28. Sirén J. Indexing variation graphs. In: 2017 Proceedings of the Ninteenth Workshop on Algorithm Engineering and Experiments (ALENEX). Society for Industrial and Applied Mathematics; 2017. p. 13–27. https://doi.org/10.1137/1. 9781611974768.2. (PDF p. 26)
29. Sirén J, Garrison E, Novak AM, Paten B, Durbin R. Haplotype-aware graph indexes. arXiv preprint arXiv:1805.03834. 2018. (PDF p. 26)
30. Mokveld T, Linthorst J, Al-Ars Z, Holstege H, Reinders M. CHOP: haplotype-aware path indexing in population graphs. bioRxiv. 2019. https://doi.org/10.1101/305268. (PDF p. 26)
31. Ghaffaari A, Marschall T. Fully-sensitive seed finding in sequence graphs using a hybrid index; 2019. p i81–9. https:// doi.org/10.1093/bioinformatics/btz341. (PDF p. 26)
32. Roberts M, Hayes W, Hunt BR, Mount SM, Yorke JA. Reducing storage requirements for biological sequence comparison. Bioinformatics. 2004;20(18):3363–9. Rautiainen and Marschall Genome Biology (2020) 21:253 Page 27 of 28 (PDF p. 26)
33. Ono Y, Asai K, Hamada M. PBSIM: PacBio reads simulator—toward accurate genome assembly. Bioinformatics. 2013;29(1):119–21. (PDF p. 27)
34. Clarke L, Fairley S, Zheng-Bradley X, Streeter I, Perry E, Lowy E, Tassé A-M, Flicek P. The international genome sample resource (IGSR): a worldwide collection of genome variation incorporating the 1000 genomes project data. Nucleic Acids Res. 2017;45(D1):854–9. (PDF p. 27)
35. Porubsky D, Ebert P, Audano PA, Vollger MR, Harvey WT, Munson KM, Sorensen M, Sulovari A, Haukness M, Ghareghani M, Human Genome Structural Variation Consortium, Paten B, Devine SE, Sanders AD, Lee C, Chaisson MJP, Korbel JO, Eichler EE, Marschall T. A fully phased accurate assembly of an individual human genome. bioRxiv. 2019. https://www.biorxiv.org/content/10.1101/855049v1.abstract. (PDF p. 27)
36. Wenger AM, Peluso P, Rowell WJ, Chang P-C, Hall RJ, Concepcion GT, Ebler J, Fungtammasan A, Kolesnikov A, Olson ND, et al. Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome. Nat Biotechnol. 2019;37(10):1155–62. (PDF p. 27)
37. Krusche P, Trigg L, Boutros PC, Mason CE, Francisco M, Moore BL, Gonzalez-Porta M, Eberle MA, Tezak Z, Lababidi S, et al. Best practices for benchmarking germline small-variant calls in human genomes. Nat Biotechnol. 2019;37(5):555–60. (PDF p. 27)
38. Lowy-Gallego E, Fairley S, Zheng-Bradley X, Ruffier M, Clarke L, Flicek P, Consortium GP, et al. Variant calling on the grch38 assembly with the data from phase three of the 1000 genomes project. Wellcome Open Res. 2019;4:50. https://doi.org/10.12688/wellcomeopenres.15126.2. (PDF p. 27)
39. Cleary JG, Braithwaite R, Gaastra K, Hilbush BS, Inglis S, Irvine SA, Jackson A, Littin R, Rathod M, Ware D, et al. Comparing variant call files for performance benchmarking of next-generation sequencing variant calling pipelines. BioRxiv. 2015023754. https://www.biorxiv.org/content/10.1101/023754v2.abstract. (PDF p. 27)
40. Zhang H, Jain C, Aluru S. A comprehensive evaluation of long read error correction methods. bioRxiv. 2019. https://doi.org/10.1101/519330. (PDF p. 27)
41. Song L, Florea L, Langmead B. Lighter: fast and memory-efficient sequencing error correction without counting. Genome Biol. 2014;15(11):509. (PDF p. 27)
42. Chikhi R, Limasset A, Medvedev P. Compacting de bruijn graphs from sequencing data quickly and in low memory. Bioinformatics. 2016;32(12):201–208. (PDF p. 27)
43. Chaisson MJ, Sanders AD, Zhao X, Malhotra A, Porubsky D, Rausch T, Gardner EJ, Rodriguez OL, Guo L, Collins RL, et al. Multi-platform discovery of haplotype-resolved structural variation in human genomes. Nat Commun. 2019;10. https://www.nature.com/articles/s41467-018-08148-z. (PDF p. 27)
44. Holt J, McMillan L. Merging of multi-string BWTs with applications. Bioinformatics. 2014;30(24):3524–31. (PDF p. 27)
45. Li H. Fast construction of FM-index for long sequence reads. Bioinformatics. 2014;30(22):3274–5. (PDF p. 27)
46. Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G, Abecasis G, Durbin R. The sequence alignment/map format and samtools. Bioinformatics. 2009;25(16):2078–9. (PDF p. 27)
47. Weirather JL, de Cesare M, Wang Y, Piazza P, Sebastiano V, Wang X-J, Buck D, Au KF. Comprehensive comparison of pacific biosciences and oxford nanopore technologies and their applications to transcriptome analysis. F1000Research. 2017;6:2078–2079. (PDF p. 27)
48. Rautiainen M, Durai DA, Chen Y, Xin L, Low HM, Göke J, Marschall T, Schulz MH. AERON: transcript quantification and gene-fusion detection using long reads. 2020. https://www.biorxiv.org/content/10.1101/2020.01.27.921338v1. abstract. (PDF p. 27)
49. Li H. Minimap and miniasm: fast mapping and de novo assembly for noisy long sequences. Bioinformatics. 2016;32(14):2103–10. (PDF p. 27)
50. Li H, Feng X, Chu C. The design and construction of reference pangenome graphs. arXiv preprint arXiv:2003.06079. 2020. (PDF p. 27)
51. Edmonds J, Johnson EL. Matching: a well-solved class of integer linear programs. In: Combinatorial Optimization—Eureka, You Shrink!. Berlin, Heidelberg: Springer; 2003. p. 27–30. https://doi.org/10.1007/3-540- 36478-1_3. (PDF p. 27)
52. Medvedev P, Brudno M. Maximum likelihood genome assembly. J Comput Biol. 2009;16(8):1101–16. (PDF p. 27)
53. Pevzner PA, Tang H, Waterman MS. An Eulerian path approach to DNA fragment assembly. Proc Natl Acad Sci. 2001;98(17):9748–53. (PDF p. 27)
54. Myers EW. The fragment assembly string graph. Bioinformatics. 2005;21(suppl_2):79–85. (PDF p. 27)
55. Koren S, Walenz BP, Berlin K, Miller JR, Bergman NH, Phillippy AM. Canu: scalable and accurate long-read assembly via adaptive k-mer weighting and repeat separation. Genome Res. 2017;27:215087. (PDF p. 27)
56. Limasset A, Rizk G, Chikhi R, Peterlongo P. Fast and scalable minimal perfect hashing for massive key sets. arXiv preprint arXiv:1702.03154. 2017. (PDF p. 27)
57. Gog S, Beller T, Moffat A, Petri M. From theory to practice: plug and play with succinct data structures. In: 13th International Symposium on Experimental Algorithms, (SEA 2014); 2014. p. 326–337. (PDF p. 27)
58. Kuosmanen A, Paavilainen T, Gagie T, Chikhi R, Tomescu A, Mäkinen V. Using minimum path cover to boost dynamic programming on dags: co-linear chaining extended. In: International Conference on Research in Computational Molecular Biology. Cham: Springer; 2018. p. 105–21. https://doi.org/10.1007/978-3-319-89929-9_7. (PDF p. 27)
59. Onodera T, Sadakane K, Shibuya T. Detecting superbubbles in assembly graphs. In: International Workshop on Algorithms in Bioinformatics. Berlin, Heidelberg: Springer; 2013. p. 338–48. https://doi.org/10.1007/978-3-642- 40453-5_26. (PDF p. 27)
60. Needleman SB, Wunsch CD. A general method applicable to the search for similarities in the amino acid sequence of two proteins. J Mol Biol. 1970;48(3):443–53. (PDF p. 27)
61. Ukkonen E. Algorithms for approximate string matching. Inf Control. 1985;64(1-3):100–18. (PDF p. 27)
62. Chao K-M, Pearson WR, Miller W. Aligning two sequences within a specified diagonal band. Bioinformatics. 1992;8(5):481–7. (PDF p. 27)
63. Suzuki H, Kasahara M. Acceleration of nucleotide semi-global alignment with adaptive banded dynamic programming. BioRxiv. 2017130633. https://www.biorxiv.org/content/10.1101/130633v2.abstract. Rautiainen and Marschall Genome Biology (2020) 21:253 Page 28 of 28 (PDF p. 27)
64. Zhang Z, Berman P, Wiehe T, Miller W. Post-processing long pairwise alignments. Bioinformatics. 1999;15(12): 1012–9. (PDF p. 28)
65. Viterbi A. Error bounds for convolutional codes and an asymptotically optimum decoding algorithm. IEEE Trans Inf Theory. 1967;13(2):260–9. (PDF p. 28)
66. Rautiainen M, Marschall T. GraphAligner. Bioconda. 2020. https://anaconda.org/bioconda/graphaligner. Accessed (PDF p. 28)
67. Aug 2020. (PDF p. 28)
68. Rautiainen M, Marschall T. GraphAligner. Github. 2020. https://github.com/maickrau/GraphAligner. Accessed 13 Aug 2020. (PDF p. 28)
69. Rautiainen M, Marschall T. GraphAligner version 1.0.11 source code. Zenodo. 2020. https://doi.org/10.5281/zenodo. 3760405. Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. (PDF p. 28)
