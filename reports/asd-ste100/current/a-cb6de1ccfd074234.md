# Faster algorithms for RNA-folding using the Four-Russians method

- Work ID: `w-cb6de1ccfd07`
- Asset ID: `a-cb6de1ccfd074234`
- Source PDF: `literature/academic-papers-processed/Faster algorithms for RNA-folding using the Four-Russians method - Venkatachalam et al.pdf`
- SHA-256: `cb6de1ccfd074234de8cc7753cc5a6cdf9785e9da781c7975dc560c84d28b779`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The two-vector method accelerates Nussinov RNA folding by replacing groups of split-point calculations with precomputed table lookups. (PDF p. 4).
- The serial variants take O(n³/log n) time. The parallel method takes O(n²/log n) time with n processes. (PDF p. 6).
- The authors implement the parallel method in CUDA and organize memory access around tiles. (PDF p. 8).

## Objectives

- Simplify Four-Russians preprocessing and its correctness analysis by completing preprocessing before the main computation. (PDF p. 1).
- Improve serial and parallel runtime for the maximum non-crossing base-pair problem. (PDF p. 1).

## Arguments

- Neighboring DP values differ by at most one. Thus, a starting value and a binary difference vector can represent a row segment. (PDF p. 3).
- A precomputed lookup replaces O(q) work for q split terms with constant-time work. (PDF p. 4).
- The Frid–Gusfield method can repeat preprocessing for the same horizontal vector. Indexing by both vectors prevents this duplicate work. (PDF p. 6).

## Analysis

- The correctness argument uses monotonic DP values. Removing one endpoint can remove at most one matched pair, which bounds adjacent differences. (PDF p. 3).
- Partial and complete memoization retain the O(n³/log n) bound. They can store fewer preprocessed entries than exhaustive preprocessing. (PDF p. 6).
- The parallel algorithm assigns one process to each column and fills successive diagonals. Synchronization makes earlier row and column values available before each step. (PDF p. 6).

## Methods

- The recurrence compares an endpoint-pair solution with all split-point solutions. Only A–U and C–G pairs contribute to the matching count. (PDF p. 3).
- Preprocessing enumerates horizontal and vertical difference-vector pairs. It stores the maximum cumulative-sum combination and its index for traceback. (PDF p. 3).
- The main algorithm processes complete groups with table lookups. At most 2q residual terms per cell use the original recurrence. (PDF p. 4).
- Partial memoization processes all vertical vectors when a new horizontal vector appears. Complete memoization processes only vector pairs that are encountered. (PDF p. 6).

## Applications

- The implemented method finds RNA secondary structures that maximize disjoint, non-crossing complementary base pairs. (PDF p. 2).
- The authors propose future extensions to thermodynamic energy models, RNA co-folding, and folding with pseudoknots. (PDF p. 11).

## Optimization

- The CUDA implementation assigns one thread block to each q-by-q tile. Independent tiles on a diagonal are computed in parallel. (PDF p. 8).
- Horizontal difference vectors use row-major storage, and vertical vectors use column-major storage. This supports coalesced memory access. (PDF p. 8).
- Shared memory reuses row and column data within a tile. The implementation uses q threads per tile to reduce idle threads and synchronization stalls. (PDF p. 8).
- Serial speed gains saturate near q = 8 or 9. Larger vectors make preprocessing too expensive. The Frid–Gusfield implementation performs best at q = 3. (PDF p. 10).

## Evaluation and testing

- Correctness tests compare each accelerated DP table with the Nussinov DP table. (PDF p. 10).
- Serial runtime measurements average 10 sequences of approximately equal length. Programs are written in C++ and compiled with the highest optimization settings. (PDF p. 10).
- GPU tests use a GeForce GTX 550 Ti with 1 GB of memory and a Tesla C2070 with 5 GB of memory. (PDF p. 11).

## Results

- The exhaustive two-vector method is fastest at every tested sequence length. Memoization checks cost more than the preprocessing work they avoid. (PDF p. 10).
- At 5000 bases, the two-vector method is 20 times faster than Nussinov on the tested desktop. Frid–Gusfield is seven times faster. (PDF p. 11).
- At 6000 bases, GPU runtimes are 4.97 seconds on GeForce and 2.50 seconds on Tesla. (PDF p. 10).
- The abstract reports about 57 seconds on a desktop and 15 seconds on a server for serial two-vector folding of 6000 bases. (PDF p. 1).

## Limitations and uncertainty

- The implemented objective counts base pairs. It does not use the more realistic thermodynamic objectives discussed by the authors. (PDF p. 2).
- Exhaustive preprocessing can include unused vector pairs. Memoized variants reduce this work but add lookup checks. (PDF p. 6).
- Extensions to energy models and pseudoknots remain future work. The authors also leave comparison with matrix-multiplication approaches for future study. (PDF p. 11).

## References

1. Akutsu T: Approximation and exact algorithms for RNA secondary structure prediction and recognition of stochastic context-free languages. J Comb Optim 1999, 3(2–3):321–336. (PDF p. 11)
2. Zakov S, Tsur D, Ziv-Ukelson M: Reducing the worst case running times of a family of RNA and CFG problems, using Valiant’s approach. In WABI. 2010:65–77. (PDF p. 11)
3. Arlazarov V, Dinic E, Kronrod M, Faradzev I: On economical construction of the transitive closure of a directed graph (in Russian). Dokl Akad Nauk 1970, 194(11):1209–1210. (PDF p. 11)
4. Frid Y, Gusfield D: A simple, practical and complete O(n3)-time algorithm for RNA folding using the Four-Russians Speedup. Algorithms Mol Biol 2010, 5:13. (PDF p. 11)
5. Chang DJ, Kimmer C, Ouyang M: Accelerating the Nussinov RNA folding algorithm with CUDA/GPU. In ISSPIT. IEEE; 2010:120–125. (PDF p. 11)
6. Rizk G, Lavenier D: GPU accelerated RNA folding algorithm. In International Conference on, Computational Science, vol. 5544. Edited by Gabrielle A, Nabrzyski J, Seidel E, Albada GD, Dongarra J, Sloot PMA. Berlin Heidelberg: Springer; 2009:1004–1013. (PDF p. 11)
7. Stojanovski M, Gjorgjevikj D, Madjarov G: Parallelization of dynamic programming in Nussinov RNA folding algorithm on the CUDA GPU. In ICT Innovations, vol. 150. Edited by Kocarev L. Berlin Heidelberg: Springer; 2011:279–289. (PDF p. 11)
8. Nussinov R, Pieczenik G, Griggs JR, Kleitman DJ: Algorithms for loop matchings. SIAM J Appl Math 1978, 35:68–82. (PDF p. 11)
9. Nussinov R, Jacobson AB: Fast algorithm for predicting the secondary structure of single-stranded RNA. PNAS 1980, 77(11):6309–6313. (PDF p. 11)
10. Zuker M, Stiegler P: Optimal computer folding of large RNA sequences using thermodynamics and auxiliary information. Nucleic Acids Res 1981, 9:133–148. (PDF p. 11)
11. Tinoco I, Borer PN, Dengler B, Levine MD, Uhlenbeck OC, Crothers DM, Gralla J: Improved estimation of secondary structure in ribonucleic-acids. Nat-New Biol 1973, 246(150):40–41. (PDF p. 11)
12. Mathews DH, Disney MD, Childs JL, Schroeder SJ, Zuker M, Turner: Incorporating chemical modification constraints into a dynamic programming algorithm for prediction of RNA secondary structure. PNAS 2004, 101(19):7287–7292. (PDF p. 11)
13. Markham NR, Zuker M: UNAFold. Bioinformatics 2008, 453:3–31. (PDF p. 11)
14. Zuker M: Mfold web server for nucleic acid folding and hybridization prediction. Nucleic Acids Res 2003, 31(13):3406–3415. (PDF p. 11)
15. Hofacker IL: Vienna RNA secondary structure server. Nucleic Acids Res 2003, 31(13):3429–3431. (PDF p. 11)
16. Reuter J, Mathews D: RNAstructure: software for RNA secondary structure prediction and analysis. BMC Bioinformatics 2010, 11:129. (PDF p. 11)
17. Durbin R, Eddy SR, Krogh A, Mitchison G: Biological Sequence Analysis. Probabilistic Models of Proteins and Nucleic Acids: Cambridge University Press; 1998. (PDF p. 11)
18. Dowell R, Eddy S: Evaluation of several lightweight stochastic context-free grammars for RNA secondary structure prediction. BMC Bioinformatics 2004, 5:71. (PDF p. 11)
19. Lu ZJ, Gloor JW, Mathews DH: Improved RNA secondary structure prediction by maximizing expected pair accuracy. RNA 2009, 15(10):1805–1813. (PDF p. 11)
20. Knudsen B, Hein J: Pfold: RNA secondary structure prediction using stochastic context-free grammars. Nucleic Acids Res 2003, 31(13):3423–3428. Venkatachalam et al. Algorithms for Molecular Biology 2014, 9:5 Page 12 of 12 http://www.almob.org/content/9/1/5 (PDF p. 11)
21. Do CB, Woods DA, Batzoglou S: CONTRAfold: RNA secondary structure prediction without physics-based models. Bioinformatics 2006, 22(14):e90–e98. (PDF p. 12)
22. Ding Y, Lawrence CE: A statistical sampling algorithm for RNA secondary structure prediction. Nucleic Acids Res 2003, 31(24):7280–7301. (PDF p. 12)
23. Hamada M, Kiryu H, Sato K, Mituyama T, Asai K: Prediction of RNA secondary structure using generalized centroid estimators. Bioinformatics 2009, 25(4):465–473. (PDF p. 12)
24. Andronescu M, Condon A, Hoos HH, Mathews DH, Murphy KP: Efficient parameter estimation for RNA secondary structure prediction. Bioinformatics 2007, 23(13):i19–i28. (PDF p. 12)
25. Andronescu M, Condon A, Hoos HH, Mathews DH, Murphy KP: Computational approaches for RNA energy parameter estimation. RNA 2010, 16(12):2304–2318. (PDF p. 12)
26. Zakov S, Goldberg Y, Elhadad M, Ziv-Ukelson M: Rich parameterization improves RNA, structure prediction. In Research in Computational Molecular Biology (RECOMB), Volume 6577, Lecture Notes in, Computer Science. Edited by Bafna V, Sahinalp SC: Springer; 2011:546–562. (PDF p. 12)
27. Wexler Y, Zilberstein CBZ, Ziv-Ukelson M: A study of accessible motifs and RNA folding complexity. J Comput Biol 2007, 14(6):856–872. (PDF p. 12)
28. Backofen R, Tsur D, Zakov S, Ziv-Ukelson M: Sparse RNA folding: time and space efficient algorithms. J Discrete Algorithms 2011, 9:12–31. (PDF p. 12)
29. Venkatachalam B, Frid Y, Gusfield D: Faster algorithms for RNA-folding using the Four-Russians method. UC Davis Technical report 2013. (PDF p. 12)
30. Frid Y, Gusfield D: A worst-case and practical speedup for the RNA co-folding problem using the Four-Russians idea. In WABI. 2010:1–12. (PDF p. 12)
31. Frid Y, Gusfield D: Speedup of RNA pseudoknotted secondary structure recurrence computation with the Four-Russians method. In COCOA, vol. 7402. Edited by Lin G; 2012:176–187. doi:10.1186/1748-7188-9-5 Cite this article as: Venkatachalam et al.: Faster algorithms for RNA-folding using the Four-Russians method. Algorithms for Molecular Biology 2014 9:5. Submit your next manuscript to BioMed Central and take full advantage of: • Convenient online submission • Thorough peer review • No space constraints or color ﬁgure charges • Immediate publication on acceptance • Inclusion in PubMed, CAS, Scopus and Google Scholar • Research which is freely available for redistribution Submit your manuscript at www.biomedcentral.com/submit (PDF p. 12)
