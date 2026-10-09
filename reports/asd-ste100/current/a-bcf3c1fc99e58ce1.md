# Exact global alignment using A* with chaining seed heuristic and match pruning

- Work ID: `b-1a7c57c58ad5`
- Asset ID: `a-bcf3c1fc99e58ce1`
- Source PDF: `literature/academic-papers-processed/Exact global alignment using A* with chaining seed heuristic and match pruning.pdf`
- SHA-256: `bcf3c1fc99e58ce12c8936cde14d774c8be7bbbc86ad4048e987854bcd411704`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- A*PA computes exact global pairwise alignment under unit edit costs with A* search. (PDF p. 1).
- Its seed heuristics combine ordered matches, gap costs, and one-edit matches. Match pruning and diagonal transition reduce search work. (PDF p. 2).
- The authors report near-linear empirical scaling on selected random inputs and median speed gains on long human ONT reads. (PDF p. 1).

## Objectives

- Develop a practical exact aligner with near-linear empirical runtime for long related sequences. (PDF p. 1).
- Improve seed heuristic accuracy for long sequences with errors while preserving alignment correctness. (PDF p. 1).

## Arguments

- A missing seed match supplies a lower bound on alignment cost because every seed must be aligned somewhere. (PDF p. 1).
- Ordered chains prevent the heuristic from combining matches that cannot occur together on an alignment path. (PDF p. 2).
- Gap-chaining uses the maximum of seed cost and gap cost. Adding these costs could count an indel twice and break admissibility. (PDF p. 5).

## Analysis

- An optimal alignment is a shortest path in a graph with zero-cost matches and unit-cost substitutions, insertions, and deletions. (PDF p. 4).
- A* expands states by g + h. An admissible heuristic bounds the remaining cost from below and guarantees an optimal result when the target is expanded. (PDF p. 5).
- The authors state that correctness proofs cover the heuristics and optimizations in Supplementary Section B. (PDF p. 2).
- The search has near-linear and quadratic operating modes. When edits exceed heuristic capacity, the explored band expands and search becomes quadratic. (PDF p. 9).

## Methods

- The first sequence is divided into consecutive nonoverlapping seeds of length k. Seed matches are found in the second sequence before search. (PDF p. 4).
- The seed heuristic counts unmatched remaining seeds. The chaining seed heuristic requires matches to follow the same order in both sequences. (PDF p. 2).
- The gap-chaining seed heuristic uses the larger of skipped-seed cost and the length difference between connected regions. With seed potential r = 2, matches can contain one edit. (PDF p. 5).
- Contours mark boundaries between states with different maximum chain lengths. They support efficient chain calculations for heuristic evaluation. (PDF p. 5).

## Applications

- A*PA aligns long human ONT reads with sequencing errors, including comparisons that also contain genetic variation. (PDF p. 9).

## Optimization

- After A* expands the start or end of a match, match pruning removes that match from later heuristic calculations. This raises costs for states behind the search front. (PDF p. 2).
- Diagonal transition skips states known not to be farthest reaching on their diagonal. It reduces work in regions with quadratic search. (PDF p. 2).
- One-edit seed matches almost double the divergence range handled efficiently, but increase match precomputation time. (PDF p. 9).
- Chaining alone often costs more than it saves because of contour overhead. Gap-chaining and diagonal transition give stronger gains on human data with long indels. (PDF p. 9).

## Evaluation and testing

- Synthetic experiments use uniform random sequences up to 10 million bases. Runtime scaling is reported at 4% and 12% divergence against EDLIB and BIWFA. (PDF p. 1).
- Human-read experiments use ONT reads longer than 500 kb, with and without genetic variation. (PDF p. 4).
- Human-read runtime plots use gap-chaining with diagonal transition, k = 15, and r = 2. Each alignment has a 100-second limit. (PDF p. 9).
- Component experiments assess match pruning, inexact matches, chaining, gap-chaining, and diagonal transition. (PDF p. 9).

## Results

- Best-fit runtime scales as n^1.06 at 4% divergence and n^1.24 at 12% divergence. At 10 million bases and 4% divergence, reported speedup exceeds 500-fold over EDLIB and BIWFA. (PDF p. 1).
- Median runtime on human ONT reads is more than threefold faster without genetic variation and 1.7-fold faster with genetic variation. (PDF p. 9).
- Six alignments time out without genetic variation and three time out with genetic variation. EDLIB has lower mean runtime in the genetic variation experiment because slow A*PA alignments dominate the total. (PDF p. 9).

## Limitations and uncertainty

- High divergence and long indels can trigger quadratic search. Repetitive regions can also generate a quadratic number of seed matches. (PDF p. 9).
- A* has high per-state overhead from irregular state access. Reported advantages require sufficiently long sequences and enough errors to slow competing methods. (PDF p. 10).
- The near-linear scaling is empirical, not an asymptotic guarantee. The authors identify further theoretical analysis as future work. (PDF p. 10).
- Non-unit costs, affine costs, and semi-global alignment are proposed extensions of the chaining seed heuristic. (PDF p. 10).

## References

1. Backurs A, Indyk P. Edit distance cannot be computed in strongly sub- quadratic time (unless SETH is false). In: Proceedings of the Forty- Seventh Annual ACM Symposium on Theory of Computing, Portland, Oregon, USA. New York, NY, USA: Association for (PDF p. 10)
2. Computing Machinery. 51–8. 2015. https://doi: 10.1145/2746539. 2746612 Benson G, Levy A, Shalom BR. Longest common subsequence in k-length substrings. In: Similarity Search and Applications: 6th (PDF p. 10)
3. International Conference, SISAP 2013, A Coru~ na, Spain, October 2-4, 2013, Proceedings 6. 257–65. Berlin Heidelberg: Springer, 2013. https://doi: 10.1007/978-3-642-41062-8_ 26 Bowden R, Davies RW, Heger A et al. Sequencing of human genomes with nanopore technology. Nat Commun 2019;10:1869. https://doi: 10.1038/s41467-019-09637-5 Daily J. Parasail: SIMD C library for global, semi-global, and local pair- wise sequence alignments. BMC Bioinformatics 2016;17:81. https:// doi: 10.1186/s12859-016-0930-z Deorowicz S, Grabowski S. Efﬁcient algorithms for the longest common subsequence in k-length substrings. Inf Process Lett 2014;114: 634–8. https://doi: 10.1016/j.ipl.2014.05. 009 Dijkstra EW. A note on two problems in connexion with graphs. Numer Math 1959;1:269–71. https://doi: 10.1145/3544585.3544600 Gotoh O. An improved algorithm for matching biological sequences. J Mol Biol 1982;162:705–8. https://doi: 10.1016/0022-2836(82)90398-9 Hadlock FO. Minimum detour methods for string or sequence compari- son. Congr Numer 1988a;61:263–274. Hadlock FO. An efﬁcient algorithm for pattern detection and classiﬁca- tion. In: Proceedings of the First International Conference on Industrial and Engineering Applications of Artiﬁcial Intelligence and Expert Systems—IEA/AIE 88, Tullahoma, Tennessee, USA. New York, NY, USA: Association for Computing Machinery. 1988b. https://doi: 10.1145/55674.55676 Hart PE, Nilsson NJ, Raphael B. A formal basis for the heuristic deter- mination of minimum cost paths. IEEE Trans Syst Sci Cyber 1968; 4:100–7. https://doi: 10.1109/TSSC.1968.300136 Hart PE, Nilsson NJ, Raphael B. Correction to a formal basis for the heuristic determination of minimum cost paths. SIGART Bull 1972; 37:28–9. https://doi: 10.1145/1056777.1056779 Hirschberg DS. A linear space algorithm for computing maximal com- mon subsequences. Commun ACM 1975;18:341–3. https://doi: 10. 1145/360825.360861 Hirschberg DS. Algorithms for the longest common subsequence prob- lem. J ACM 1977;24:664–75. https://doi: 10.1145/322033.322044 Holte RC. Common misconceptions concerning heuristic search. In: Third Annual Symposium on Combinatorial Search, Atlanta, Georgia, USA. Washington DC, USA: Association for the Advancement of Artiﬁcial Intelligence 2010. https://doi: 10.1609/ socs.v1i1.18160 Hunt JW, Szymanski TG. A fast algorithm for computing longest com- mon subsequences. Commun ACM 1977;20:350–3. Ivanov P, Bichsel B, Vechev M. Fast and optimal sequence-to-graph alignment guided by seeds. In: RECOMB 2022, San Diego, CA, (PDF p. 10)
4. USA. Cham: Springer International Publishing 2022. https://doi: 10. 1007/978-3-031-04749-7_ 22 Koenig S, Likhachev M. Real-time adaptive A*. In: Proceedings of the Fifth International Joint Conference on Autonomous Agents and Multiagent Systems, Hakodate, Japan. New York, NY, USA: Association for Computing Machinery 281–8. 2006. https://doi: 10. 1145/1160633.1160682 Kucherov G. Evolution of biosequence search algorithms: a brief survey. Bioinformatics 2019;35:3547–52. https://doi: 10.1093/bioinformat ics/btz272 Levenshtein VI. Binary codes capable of correcting deletions, insertions, and reversals. Sov Phys Dokl 1966;10:707–10. Liu D, Steinegger M. Block aligner: an adaptive SIMD-accelerated aligner for sequences and position-speciﬁc scoring matrices. Bioinformatics 2023;39:btad487. https://doi: 10.1093/bioinformat ics/btad487 Marco-Sola S, Sammeth M, Guig R et al. The gem mapper: fast, accurate and versatile alignment by ﬁltration. Nat Methods 2012;9:1185–8. https://doi: 10.1038/nmeth.2221 Marco-Sola S, Moure JC, Moreto M et al. Fast gap-afﬁne pairwise alignment using the wavefront algorithm. Bioinformatics 2021;37: 456–63. https://doi: 10.1093/bioinformatics/btaa777 Marco-Sola S, Eizenga JM, Guarracino A et al. Optimal gap-afﬁne alignment in oðsÞ space. Bioinformatics 2023;39: https://doi: 10. 1093/bioinformatics/btad074 (PDF p. 10)
5. Groot Koerkamp and Ivanov Downloaded from academic.oup.com/bioinformatics/article/40/3/btae032/7587511 by guest on 23 September 2026 (PDF p. 10)
6. Medvedev P. Theoretical analysis of edit distance algorithms. Commun ACM 2023a;66:64–71. https://doi: 10.1145/3582490 Medvedev P. Theoretical analysis of sequencing bioinformatics algorithms and beyond. Commun ACM 2023b;66:118–25. https:// doi: 10.1145/3571723 Myers EW. An O(ND) difference algorithm and its variations. Algorithmica 1986;1:251–66. https://doi: 10.1007/BF01840446 Myers G. A fast bit-vector algorithm for approximate string matching based on dynamic programming. J ACM 1999;46:395–415. https:// doi: 10.1145/316542.316550 Myers G, Miller W. Chaining multiple-alignment fragments in sub- quadratic time. In: SODA, Vol. 95. 38–47.1995. Navarro G. A guided tour to approximate string matching. ACM (PDF p. 11)
7. Comput Surv 2001;33:31–88. https://doi: 10.1145/375360.375365 Needleman SB, Wunsch CD. A general method applicable to the search for similarities in the amino acid sequence of two proteins. J Mol Biol 1970;48:443–53. https://doi: 10.1016/0022-2836(70)90057-4 Nurk S, Koren S, Rhie A et al. The complete sequence of a human genome. Science 2022;376:44–53. https://doi: 10.1126/science.abj6987 Papamichail D, Papamichail G. Improved algorithms for approximate string matching (extended abstract). BMC Bioinformatics 2009;10 (Suppl. 1):S10. https://doi:10.1186/1471-2105-10-s1-s10 Paveti c F, Katani c I, Matula G et al. Fast and simple algorithms for computing both LCSk and LCSkþ. arXiv, arXiv:1705.07279, 2017, preprint: not peer reviewed. Pearl J. Heuristics: Intelligent Search Strategies for Computer Problem Solving. United States: Addison-Wesley Longman Publishing Co., Inc., 1984. Poole DL, Mackworth AK. Artiﬁcial Intelligence: Foundations of (PDF p. 11)
8. Computational Agents. 2nd edn. Cambridge University Press, 2017. Prjibelski AD, Korobeynikov AI, Lapidus AL. Sequence analysis. In: Ranganathan S, Gribskov M, Nakai K et al. (eds), Encyclopedia of Bioinformatics and Computational Biology. Oxford: Oxford (PDF p. 11)
9. Academic Press, 2019, 292–322. https://doi: 10.1016/B978-0-12- 809633-8.20106-4 Reinert K, Dadi TH, Ehrhardt M et al. The SeqAn Cþþ template library for efﬁcient sequence analysis: a resource for programmers. J Biotechnol 2017;261:157–68. https://doi: 10.1016/j.jbiotec.2017. 07.017 Sankoff D. Matching sequences under deletion/insertion constraints. (PDF p. 11)
10. Proc Natl Acad Sci USA 1972;69:4–6. https://doi: 10.1073/pnas.69. 1.4 Sellers PH. On the theory and computation of evolutionary distances. (PDF p. 11)
11. SIAM J Appl Math 1974;26:787–93. https://doi: 10.1137/0126070  So si c M,  Siki c M. Edlib: a C/Cþþ library for fast, exact sequence align- ment using edit distance. Bioinformatics 2017;33:1394–5. https:// doi: 10.1101/070649 Spouge JL. Speeding up dynamic programming algorithms for ﬁnding optimal lattice paths. SIAM J Appl Math 1989;49:1552–66. https:// doi: 10.1137/0149094 (PDF p. 11)
12. Spouge JL. Fast optimal alignment. Comput Appl Biosci 1991;7:1–7. https://doi: 10.1093/bioinformatics/7.1.1 Ukkonen E. Algorithms for approximate string matching. Inf Control 1985;64:100–18. https://doi: 10.1016/S0019- 9958(85)80046-2 Vintsyuk TK. Speech discrimination by dynamic programming. Cybern (PDF p. 11)
13. Syst Anal 1968;4:52–7. https://doi: 10.1007/BF01074755 Wagner RA, Fischer MJ. The string-to-string correction problem. J ACM 1974;21:168–73. https://doi: 10.1145/321796.321811 (PDF p. 11)
14. Wu S, Manber U. Fast text searching. Commun ACM 1992;35:83–91. https://doi: 10.1145/135239.135244 Wu S, Manber U, Myers G et al. An O(NP) sequence comparison algo- rithm. Inf Process Lett 1990;35:317–23. https://doi: 10.1016/0020- 0190(90)90035-v Exact global alignment using A* 11 Downloaded from academic.oup.com/bioinformatics/article/40/3/btae032/7587511 by guest on 23 September 2026 (PDF p. 11)
