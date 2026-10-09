# Next Generation Sequence Analysis and Computational Genomics Using Graphical Pipeline Workflows

- Work ID: `w-3297ac3ea9fc`
- Asset ID: `a-3297ac3ea9fcee6b`
- Source PDF: `literature/academic-papers-processed/Next Generation Sequence Analysis and Computational Genomics Using Graphical Pipeline Workflows.pdf`
- SHA-256: `3297ac3ea9fcee6b873d189fd8554095aae466e26e7bb389f6f378b31e2be656`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The Graphical Pipeline for Computational Genomics integrates workflows from raw DNA sequencing reads through variant calling and annotation. (PDF p. 2).
- The system connects command-line tools as graphical modules in the LONI environment. (PDF p. 23).
- The authors evaluate workflows with simulated reads and a complete Illumina flowcell. They also compare shared modules with Galaxy. (PDF p. 20).

## Objectives

- The authors aim to reduce the computational burden of NGS analysis through flexible graphical workflows. (PDF p. 2).
- The system targets researchers who analyze whole-genome, exome, and targeted sequencing data. (PDF p. 22).

## Arguments

- The authors argue that reusable graphical workflows save the effort needed to implement and test command lines for individual analysis steps. (PDF p. 22).
- They distinguish technical protocol validation from scientific validation. The latter requires comparisons of mapping, variant calling, and quality control methods for specific data. (PDF p. 25).

## Analysis

- Interpretation: the Galaxy comparison measures module execution in the tested environments. It does not establish a new sequence-alignment algorithm or an alignment-accuracy advantage. (PDF p. 20).
- The authors identify data upload and unpredictable queue delays as additional costs in their Galaxy comparison. (PDF p. 20).

## Methods

- Workflow design proceeds from analysis classes to tools, test data, and executable syntax. Modules are defined and validated independently before integration. (PDF p. 23).
- The BWA paired-end workflow indexes the reference, aligns each read separately with BWA-aln, and combines the results into SAM output. (PDF p. 21).
- Advanced quality control locally realigns reads near indels and recalibrates base quality scores. It produces a cleaned BAM file, quality metrics, and visualization tracks. (PDF p. 16).
- CNVseq compares read counts in sliding windows between test and reference individuals. ERDS uses a hidden Markov model with expected read depth estimated by expectation maximization and corrected for GC bias. (PDF p. 19).

## Applications

- The workflows support sequence alignment, quality control, SNP analysis, CNV identification, annotation, and visualization. (PDF p. 2).
- Users can share workflow protocols and replace modules to compare alternative tools on new datasets. (PDF p. 25).

## Optimization

- The authors report that GPCG removes the data-upload step required in their Galaxy comparison. This saved about three hours in that test. (PDF p. 22).
- The graphical workflow manages input files and output names across flowcell lanes. Users can set BWA options through the module interface. (PDF p. 21).

## Evaluation and testing

- Simulation uses dwgsim from DNAA v0.1.2 to generate 30 million reads of 100 bases from hg18. It uses default parameters and the default empirical error model. (PDF p. 23).
- The Galaxy comparison uses the same input files for shared conversion, paired-end alignment, and PICARD modules. The authors could not compare complete workflows. (PDF p. 20).
- The real-data test uses eight flowcell lanes with about 130 million paired-end reads per lane. (PDF p. 23).
- Real reads are 100 bases long and align to NCBI36.1/hg18 with BWA-PE. The reported test server has two six-core Xeon X5650 processors at 2.67 GHz, 96 GB RAM, and RHEL 5. (PDF p. 24).

## Results

- BWA paired-end alignment took 132 minutes in GPCG and 240 minutes in Galaxy. Bowtie paired-end alignment took 205 and 270 minutes, respectively. (PDF p. 20).
- All tested shared modules ran faster in GPCG. Duplicate marking took 2 minutes in GPCG and 20 minutes in Galaxy. (PDF p. 20).
- The real-data BWA alignment averaged six hours per lane and about 48 hours for the full flowcell. It produced one SAM file per lane. (PDF p. 21).

## Limitations and uncertainty

- Galaxy's structure and available processes prevented a comparison at the complete-workflow level. (PDF p. 20).
- The first GPCG release includes only a selection of DNA-Seq tools. The authors propose adding tools and allowing users to integrate new processes. (PDF p. 22).
- The authors present broader scientific comparisons of alternative algorithms as a further validation tier. Technical reproducibility alone does not provide that evidence. (PDF p. 25).

## References

1. Dalca, A.V.; Brudno, M. Genome variation discovery with high-throughput sequencing data. Brief. Bioinform. 2010, 11, 3±14. (PDF p. 26)
2. Alkan, C.; Coe, B.P.; Eichler, E.E. Genome structural variation discovery and genotyping. Nat. Rev. Genet. 2011, 12, 363±376. (PDF p. 26)
3. Flicek, P.; Birney, E. Sense from sequence reads: Methods for alignment and assembly. Nat. Methods 2009, 6, S6±S12. (PDF p. 26)
4. Pepke, S.; Wold, B.; Mortazavi, A. Computation for chip-seq and rna-seq studies. Nat. Methods 2009, 6, S22±S32. (PDF p. 26)
5. Meaburn, E.; Schulz, R. Next generation sequencing in epigenetics: Insights and challenges. Semin. Cell Dev. Biol. 2011, 23, 192±199. (PDF p. 26)
6. Walsh, T.; McClellan, J.M.; McCarthy, S.E.; Addington, A.M.; Pierce, S.B.; Cooper, G.M.; Nord, A.S.; Kusenda, M.; Malhotra, D.; Bhandari, A.; et al. Rare structural variants disrupt multiple genes in neurodevelopmental pathways in schizophrenia. Science 2008, 320, 539±543. (PDF p. 26)
7. Rumble, S.M.; Lacroute, P.; Dalca, A.V.; Fiume, M.; Sidow, A.; Brudno, M. Shrimp: Accurate mapping of short color-space reads. PLoS Comput. Biol. 2009, 5, e1000386. (PDF p. 26)
8. Lin, H.; Zhang, Z.; Zhang, M.Q.; Ma, B.; Li, M. Zoom! Zillions of oligos mapped. Bioinformatics 2008, 24, 2431±2437. (PDF p. 26)
9. Li, R.; Yu, C.; Li, Y.; Lam, T.W.; Yiu, S.M.; Kristiansen, K.; Wang, J. Soap2: An improved ultrafast tool for short read alignment. Bioinformatics 2009, 25, 1966±1967. (PDF p. 26)
10. Chen, Y.; Souaiaia, T.; Chen, T. Perm: Efficient mapping of short sequencing reads with periodic full sensitive spaced seeds. Bioinformatics 2009, 25, 2514±2521. (PDF p. 26)
11. Langmead, B.; Trapnell, C.; Pop, M.; Salzberg, S.L. Ultrafast and memory-efficient alignment of short DNA sequences to the human genome. Genome Biol. 2009, 10, R25. (PDF p. 26)
12. Li, H.; Durbin, R. Fast and accurate short read alignment with burrows-wheeler transform. Bioinformatics 2009, 25, 1754±1760. (PDF p. 26)
13. Chen, K.; Wallis, J.W.; McLellan, M.D.; Larson, D.E.; Kalicki, J.M.; Pohl, C.S.; McGrath, S.D.; Wendl, M.C.; Zhang, Q.; Locke, D.P.; et al. Breakdancer: An algorithm for high-resolution mapping of genomic structural variation. Nat. Methods 2009, 6, 677±681. (PDF p. 26)
14. Olson, S.A. Emboss opens up sequence analysis. European molecular biology open software suite. Brief. Bioinform. 2002, 3, 87±91. (PDF p. 26)
15. Myers, E.W. Toward simplifying and accurately formulating fragment assembly. J. Comput. Biol. 1995, 2, 275±290. (PDF p. 26)
16. Pevzner, P.A.; Tang, H.; Waterman, M.S. An eulerian path approach to DNA fragment assembly. Proc. Natl. Acad. Sci. USA 2001, 98, 9748±9753. (PDF p. 26)
17. Myers, E.W.; Sutton, G.G.; Delcher, A.L.; Dew, I.M.; Fasulo, D.P.; Flanigan, M.J.; Kravitz, S.A.; Mobarry, C.M.; Reinert, K.H.; Remington, K.A.; et al. A whole-genome assembly of drosophila. Science 2000, 287, 2196±2204. (PDF p. 26)
18. Jaffe, D.B.; Butler, J.; Gnerre, S.; Mauceli, E.; Lindblad-Toh, K.; Mesirov, J.P.; Zody, M.C.; Lander, E.S. Whole-genome sequence assembly for mammalian genomes: Arachne 2. Genome Res. 2003, 13, 91±96. Genes 2012, 3 571 (PDF p. 26)
19. Zerbino, D.R.; Birney, E. Velvet: Algorithms for de novo short read assembly using de bruijn graphs. Genome Res. 2008, 18, 821±829. (PDF p. 27)
20. Li, R.; Zhu, H.; Ruan, J.; Qian, W.; Fang, X.; Shi, Z.; Li, Y.; Li, S.; Shan, G.; Kristiansen, K.; Yang, H.; Wang, J. De novo assembly of human genomes with massively parallel short read sequencing. Genome Res. 2010, 20, 265±272. (PDF p. 27)
21. Simpson, J.T.; Wong, K.; Jackman, S.D.; Schein, J.E.; Jones, S.J.; Birol, I. Abyss: A parallel assembler for short read sequence data. Genome Res. 2009, 19, 1117±1123. (PDF p. 27)
22. Miller, J.R.; Koren, S.; Sutton, G. Assembly algorithms for next-generation sequencing data. Genomics 2010, 95, 315±327. (PDF p. 27)
23. Ewing, B.; Green, P. Base-calling of automated sequencer traces using phred. Ii. Error probabilities. Genome Res. 1998, 8, 186±194. (PDF p. 27)
24. Brockman, W.; Alvarez, P.; Young, S.; Garber, M.; Giannoukos, G.; Lee, W.L.; Russ, C.; Lander, E.S.; Nusbaum, C.; Jaffe, D.B. Quality scores and snp detection in sequencing-by- synthesis systems. Genome Res. 2008, 18, 763±770. (PDF p. 27)
25. Li, M.; Nordborg, M.; Li, L.M. Adjust quality scores from alignment and improve sequencing accuracy. Nucleic Acids Res. 2004, 32, 5183±5191. (PDF p. 27)
26. Li, R.; Li, Y.; Fang, X.; Yang, H.; Wang, J.; Kristiansen, K. Snp detection for massively parallel whole-genome resequencing. Genome Res. 2009, 19, 1124±1132. (PDF p. 27)
27. DePristo, M.A.; Banks, E.; Poplin, R.; Garimella, K.V.; Maguire, J.R.; Hartl, C.; Philippakis, A.A.; del Angel, G.; Rivas, M.A.; Hanna, M.; et al. A framework for variation discovery and genotyping using next-generation DNA sequencing data. Nat. Genet. 2011, 43, 491±498. (PDF p. 27)
28. Ning, Z.; Cox, A.J.; Mullikin, J.C. Ssaha: A fast search method for large DNA databases. Genome Res. 2001, 11, 1725±1729. (PDF p. 27)
29. Martin, M.V.; Rollins, B.; Sequeira, P.A.; Mesen, A.; Byerley, W.; Stein, R.; Moon, E.A.; Akil, H.; Jones, E.G.; Watson, S.J.; et al. Exon expression in lymphoblastoid cell lines from subjects with schizophrenia before and after glucose deprivation. BMC Med. Genomics 2009, 2, 62. (PDF p. 27)
30. Drmanac, R.; Sparks, A.B.; Callow, M.J.; Halpern, A.L.; Burns, N.L.; Kermani, B.G.; Carnevali, P.; Nazarenko, I.; Nilsen, G.B.; Yeung, G.; et al. Human genome sequencing using unchained base reads on self-assembling DNA nanoarrays. Science 2010, 327, 78±81. (PDF p. 27)
31. Bentley, D.R.; Balasubramanian, S.; Swerdlow, H.P.; Smith, G.P.; Milton, J.; Brown, C.G.; Hall, K.P.; Evers, D.J.; Barnes, C.L.; Bignell, H.R.; et al. Accurate whole human genome sequencing using reversible terminator chemistry. Nature 2008, 456, 53±59. (PDF p. 27)
32. Koboldt, D.C.; Chen, K.; Wylie, T.; Larson, D.E.; McLellan, M.D.; Mardis, E.R.; Weinstock, G.M.; Wilson, R.K.; Ding, L. Varscan: Variant detection in massively parallel sequencing of individual and pooled samples. Bioinformatics 2009, 25, 2283±2285. (PDF p. 27)
33. Wheeler, D.A.; Srinivasan, M.; Egholm, M.; Shen, Y.; Chen, L.; McGuire, A.; He, W.; Chen, Y.J.; Makhijani, V.; Roth, G.T.; et al. The complete genome of an individual by massively parallel DNA sequencing. Nature 2008, 452, 872±876. (PDF p. 27)
34. Mokry, M.; Feitsma, H.; Nijman, I.J.; de Bruijn, E.; van der Zaag, P.J.; Guryev, V.; Cuppen, E. Accurate snp and mutation detection by targeted custom microarray-based genomic enrichment of short-fragment sequencing libraries. Nucleic Acids Res. 2010, 38, e116. Genes 2012, 3 572 (PDF p. 27)
35. Shen, Y.; Wan, Z.; Coarfa, C.; Drabek, R.; Chen, L.; Ostrowski, E.A.; Liu, Y.; Weinstock, G.M.; Wheeler, D.A.; Gibbs, R.A.; et al. A snp discovery method to assess variant allele probability from next-generation resequencing data. Genome Res. 2010, 20, 273±280. (PDF p. 28)
36. Hoberman, R.; Dias, J.; Ge, B.; Harmsen, E.; Mayhew, M.; Verlaan, D.J.; Kwan, T.; Dewar, K.; Blanchette, M.; Pastinen, T. A probabilistic approach for snp discovery in high-throughput human resequencing data. Genome Res. 2009, 19, 1542±1552. (PDF p. 28)
37. Malhis, N.; Jones, S.J. High quality snp calling using illumina data at shallow coverage. Bioinformatics 2010, 26, 1029±1035. (PDF p. 28)
38. Handsaker, R.E.; Korn, J.M.; Nemesh, J.; McCarroll, S.A. Discovery and genotyping of genome structural polymorphism by sequencing on a population scale. Nat. Genet. 2011, 43, 269±276. (PDF p. 28)
39. Kim, J.; Sinha, S. Indelign: A probabilistic framework for annotation of insertions and deletions in a multiple alignment. Bioinformatics 2007, 23, 289±297. (PDF p. 28)
40. Li, H.; Ruan, J.; Durbin, R. Mapping short DNA sequencing reads and calling variants using mapping quality scores. Genome Res. 2008, 18, 1851±1858. (PDF p. 28)
41. Hormozdiari, F.; Alkan, C.; Eichler, E.E.; Sahinalp, S.C. Combinatorial algorithms for structural variation detection in high-throughput sequenced genomes. Genome Res. 2009, 19, 1270±1278. (PDF p. 28)
42. Lee, S.; Hormozdiari, F.; Alkan, C.; Brudno, M. Modil: Detecting small indels from clone-end sequencing with mixtures of distributions. Nat. Methods 2009, 6, 473±474. (PDF p. 28)
43. Korbel, J.O.; Abyzov, A.; Mu, X.J.; Carriero, N.; Cayting, P.; Zhang, Z.; Snyder, M.; Gerstein, M.B. Pemer: A computational framework with simulation-based error models for inferring genomic structural variants from massive paired-end sequencing data. Genome Biol. 2009, 10, R23. (PDF p. 28)
44. Sindi, S.; Helman, E.; Bashir, A.; Raphael, B.J. A geometric approach for classification and comparison of structural variants. Bioinformatics 2009, 25, i222±i230. (PDF p. 28)
45. Pelak, K.; Shianna, K.V.; Ge, D.; Maia, J.M.; Zhu, M.; Smith, J.P.; Cirulli, E.T.; Fellay, J.; Dickson, S.P.; Gumbs, C.E.; et al. The characterization of twenty sequenced human genomes. PLoS Genet. 2010, 6, e1001111. (PDF p. 28)
46. Ye, K.; Schulz, M.H.; Long, Q.; Apweiler, R.; Ning, Z. Pindel: A pattern growth approach to detect break points of large deletions and medium sized insertions from paired-end short reads. Bioinformatics 2009, 25, 2865±2871. (PDF p. 28)
47. Xie, C.; Tammi, M.T. Cnv-seq, a new method to detect copy number variation using high-throughput sequencing. BMC Bioinformatics 2009, 10, 80. (PDF p. 28)
48. Medvedev, P.; Fiume, M.; Dzamba, M.; Smith, T.; Brudno, M. Detecting copy number variation with mated short reads. Genome Res. 2010, 20, 1613±1622. (PDF p. 28)
49. Nielsen, R.; Paul, J.S.; Albrechtsen, A.; Song, Y.S. Genotype and snp calling from next-generation sequencing data. Nat. Rev. Genet. 2011, 12, 443±451. (PDF p. 28)
50. Wang, K.; Li, M.; Hakonarson, H. Annovar: Functional annotation of genetic variants from high-throughput sequencing data. Nucleic Acids Res. 2010, 38, e164. (PDF p. 28)
51. Ge, D.; Ruzzo, E.K.; Shianna, K.V.; He, M.; Pelak, K.; Heinzen, E.L.; Need, A.C.; Cirulli, E.T.; Maia, J.M.; Dickson, S.P.; et al. Sva: Software for annotating and visualizing sequenced human genomes. Bioinformatics 2011, 27, 1998±2000. Genes 2012, 3 573 (PDF p. 28)
52. Neale, B.M.; Rivas, M.A.; Voight, B.F.; Altshuler, D.; Devlin, B.; Orho-Melander, M.; Kathiresan, S.; Purcell, S.M.; Roeder, K.; Daly, M.J. Testing for an unusual distribution of rare variants. PLoS Genet. 2011, 7, e1001322. (PDF p. 29)
53. Adzhubei, I.A.; Schmidt, S.; Peshkin, L.; Ramensky, V.E.; Gerasimova, A.; Bork, P.; Kondrashov, A.S.; Sunyaev, S.R. A method and server for predicting damaging missense mutations. Nat. Methods 2010, 7, 248±249. (PDF p. 29)
54. Yandell, M.; Huff, C.; Hu, H.; Singleton, M.; Moore, B.; Xing, J.; Jorde, L.B.; Reese, M.G. A probabilistic disease-gene finder for personal genomes. Genome Res. 2011, 21, 1529±1542. (PDF p. 29)
55. Zhang, J.; Chiodini, R.; Badr, A.; Zhang, G. The impact of next-generation sequencing on genomics. J. Genet. Genomics 2011, 38, 95±109. (PDF p. 29)
56. Torkamani, A.; Scott-Van Zeeland, A.A.; Topol, E.J.; Schork, N.J. Annotating individual human genomes. Genomics 2011, 98, 233±241. (PDF p. 29)
57. Mardis, E.R. The $1,000 genome, the $100,000 analysis? Genome Med. 2010, 2, 84. (PDF p. 29)
58. Milano, F. Power System Architecture. In Power System Modelling and Scripting; Milano, F., Ed.; Springer: Berlin/Heidelberg, Germany, 2010; pp. 19±30. (PDF p. 29)
59. Wang, D.; Zender, C.; Jenks, S. Efficient clustered server-side data analysis workflows using swamp. Earth Sci. Inform. 2009, 2, 141±155. (PDF p. 29)
60. Ye, X.-Q.; Wang, G.-H.; Huang, G.-J.; Bian, X.-W.; Qian, G.-S.; Yu, S.-C. Heterogeneity of mitochondrial membrane potential: A novel tool to isolate and identify cancer stem cells from a tumor mass? Stem Cell Rev. Rep. 2011, 7, 153±160. (PDF p. 29)
61. Yoo, J.; Ha, I.; Chang, G.; Jung, K.; Park, K.; Kim, Y. Cnvas: Copy number variation analysis system²The analysis tool for genomic alteration with a powerful visualization module. BioChip J. 2011, 5, 265±270. (PDF p. 29)
62. Chard, K.; Onyuksel, C.; Wei, T.; Sulakhe, D.; Madduri, R.; Foster, I. Build Grid Enabled Scientific Workflows Using Gravi and Taverna. In Proceedings of IEEE Fourth International Conference on eScience, 2008. eScience '08, Indianapolis, IN, USA 7±12 December 2008; pp. 614±619. (PDF p. 29)
63. Ludäscher, B.; Altintas, I.; Berkley, C.; Higgins, D.; Jaeger, E.; Jones, M.; Lee, E.A.; Tao, J.; Zhao, Y. Scientific workflow management and the kepler system. Concurr. Comput. Pract. Exp. 2006, 18, 1039±1065. (PDF p. 29)
64. Goecks, J.; Nekrutenko, A.; Taylor, J.; Team, T.G. Galaxy: A comprehensive approach for supporting accessible, reproducible, and transparent computational research in the life sciences. Genome Biol. 2010, 11, R86. (PDF p. 29)
65. Dinov, I.; Torri, F.; Macciardi, F.; Petrosyan, P.; Liu, Z.; Zamanyan, A.; Eggert, P.; Pierce, J.; Genco, A.; Knowles, J.; et al. Applications of the pipeline environment for visual informatics and genomics computations. BMC Bioinformatics 2011, 12, 304. (PDF p. 29)
66. Taylor, I.; Shields, M.; Wang, I.; Harrison, A. The Triana Workflow Environment: Architecture and Applications. In Workflows for e-Science; Taylor, I., Deelman, E., Gannon, D., Shields, M., Eds.; Springer: Secaucus, NJ, USA, 2007; pp. 320±339. (PDF p. 29)
67. Kwon, Y.; Shigemoto, Y.; Kuwana, Y.; Sugawara, H. Web API for biology with a workflow navigation system. Nucleic Acids Res. 2009, 37, W11±W16. Genes 2012, 3 574 (PDF p. 29)
68. Oinn, T.; Addis, M.; Ferris, J.; Marvin, D.; Senger, M.; Greenwood, M.; Carver, T.; Glover, K.; Pocock, M.; Wipat, A.; et al. Taverna: A tool for the composition and enactment of bioinformatics workflows. Bioinformatics 2004, 20, 3045±3054. (PDF p. 30)
69. Schatz, M. The missing graphical user interface for genomics. Genome Biol. 2010, 11, 128. (PDF p. 30)
70. Dinov, I.; Lozev, K.; Petrosyan, P.; Liu, Z.; Eggert, P.; Pierce, J.; Zamanyan, A.; Chakrapani, S.; van Horn, J.; Parker, D.; et al. Neuroimaging study designs, computational analyses and data provenance using the loni pipeline. PLoS One 2010, 5, e13070. (PDF p. 30)
71. Rex, D.E.; Ma, J.Q.; Toga, A.W. The loni pipeline processing environment. Neuroimage 2003, 19, 1033±1048. (PDF p. 30)
72. Service, R.F. Gene sequencing. The race for the $1000 genome. Science 2006, 311, 1544±1546. (PDF p. 30)
73. Mardis, E.R. Next-generation DNA sequencing methods. Annu. Rev. Genomics Hum. Genet. 2008, 9, 387±402. (PDF p. 30)
74. Mardis, E.R. The impact of next-generation sequencing technology on genetics. Trends Genet. 2008, 24, 133±141. (PDF p. 30)
75. Li, H.; Handsaker, B.; Wysoker, A.; Fennell, T.; Ruan, J.; Homer, N.; Marth, G.; Abecasis, G.; Durbin, R.; Subgroup, G.P.D.P. The sequence alignment/map format and samtools. Bioinformatics 2009, 25, 2078±2079. (PDF p. 30)
76. Leung, K.; Parker, D.S.; Cunha, A.; Dinov, I.D.; Toga, A.W. Irma: An image registration meta-algorithm²Evaluating alternative algorithms with multiple metrics. Lect. Notes Comput. Sci. 2008, 5069, 612±617. (PDF p. 30)
77. Leung, K.T.K. Principal Ranking Meta-Algorithms. Ph.D. these, University of California, Los Angeles, CA, USA, 2011. (PDF p. 30)
78. Rex, D.E.; Shattuck, D.W.; Woods, R.P.; Narr, K.L.; Luders, E.; Rehm, K.; Stolzner, S.E.; Rottenberg, D.E.; Toga, A.W. A meta-algorithm for brain extraction in mri. NeuroImage 2004, 23, 625±637. (PDF p. 30)
79. Ruffalo, M.; LaFramboise, T.; Koyutürk, M. Comparative analysis of algorithms for next-generation sequencing read alignment. Bioinformatics 2011, 27, 2790±2796. (PDF p. 30)
80. McKenna, A.; Hanna, M.; Banks, E.; Sivachenko, A.; Cibulskis, K.; Kernytsky, A.; Garimella, K.; Altshuler, D.; Gabriel, S.; Daly, M.; et al. The genome analysis toolkit: A mapreduce framework for analyzing next-generation DNA sequencing data. Genome Res. 2010, 20, 1297±1303. (PDF p. 30)
81. Gunter, C. Genomics: A picture worth 1000 genomes. Nat. Rev. Genet. 2010, 11, 814. (PDF p. 30)
82. Fiume, M.; Williams, V.; Brook, A.; Brudno, M. Savant: Genome browser for high-throughput sequencing data. Bioinformatics 2010, 26, 1938±1944. (PDF p. 30)
83. Hamada, M.; Wijaya, E.; Frith, M.C.; Asai, K. Probabilistic alignments with quality scores: An application to short-read mapping toward accurate snp/indel detection. Bioinformatics 2011, doi:10.1093/bioinformatics/btr537. (PDF p. 30)
84. Hamada, M.; Wijaya, E.; Frith, M.C.; Asai, K. Probabilistic alignments with quality scores: An application to short-read mapping toward accurate snp/indel detection. Bioinformatics 2011, 27, 3085±3092. (PDF p. 30)
85. Raffan, E.; Semple, R.K. Next generation sequencing²Implications for clinical practice. Br. Med. Bull. 2011, 99, 53±71. Genes 2012, 3 575 (PDF p. 30)
86. Haas, J.; Katus, H.A.; Meder, B. Next-generation sequencing entering the clinical arena. Mol. Cell. Probes 2011, 25, 206±211. © 2012 by the authors; licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution license (http://creativecommons.org/licenses/by/3.0/). (PDF p. 31)
