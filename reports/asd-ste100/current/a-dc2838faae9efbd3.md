# Speeding-up Hirschberg and Hunt-Szymanski LCS Algorithms

- Work ID: `w-dc2838faae9e`
- Asset ID: `a-dc2838faae9efbd3`
- Source PDF: `literature/academic-papers-processed/Speeding-up Hirschberg and Hunt-Szymanski LCS Algorithms - Crochemore et al.pdf`
- SHA-256: `dc2838faae9efbd395d1ee28858b531afdd300732978b9a7b8bc3604eb00ce48`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors present bit-parallel formulations of the Hirschberg and Hunt-Szymanski LCS algorithms. (PDF p. 1).
- Bit-vector operations speed up the calculation of k-match lists and threshold updates. (PDF p. 11).

## Objectives

- Accelerate classic longest common subsequence algorithms by exploiting word-level parallelism. (PDF p. 1).

## Arguments

- Bit-parallel operations allow testing multiple character match states simultaneously within single machine words. (PDF p. 11).

## Analysis

- Execution time is evaluated as a function of text length and alphabet size. (PDF p. 13).

## Methods

- The BV-KMATCHLIST algorithm identifies all match points using bitwise AND, OR, and shift operations. (PDF p. 12).
- The BV-HS algorithm maintains threshold arrays with bit vectors to locate insertion positions in O(1) word operations. (PDF p. 12).

## Applications

- Fast sequence comparison, file diffing, and text pattern matching. (PDF p. 3).

## Optimization

- Machine word bit-parallelism reduces inner loop instruction counts in threshold searches. (PDF p. 12).

## Evaluation and testing

- The bit-vector implementations are benchmarked against standard Hirschberg and Hunt-Szymanski algorithms. (PDF p. 13).

## Results

- The bit-parallel variants achieve substantial speedups over standard algorithms across all tested alphabet sizes. (PDF p. 13).

## Limitations and uncertainty

- Direct single-word performance gains require sequence lengths bounded by the machine word size. (PDF p. 12).

## References

1. A. Apostolico, Improving the worst-case performance of the Hunt-Szymanski strategy for the longest common subsequence of two strings, Inform. Process. Lett., 23, 63–69, 1986. (PDF p. 13)
2. A. Apostolico and C. Guerra, The longest common subsequence problem revisited, Algorithmica, 2, 315–336, 1987. (PDF p. 13)
3. R. A. Baeza-Yates and G. H. Gonnet, A new approach to text searching, Comm. Assoc. Comput. Mach., 35, 74–82, 1992. (PDF p. 13)
4. M. Crochemore, C. S. Iliopoulos, Y. J. Pinzon and J. F. Reid, A fast bit-vector algorithm for the longest common subsequence problem, Proceedings of the 11th Australasian Workshop on Combi- natorial Algorithms AWOCA’00, 74–82, 2000. (PDF p. 13)
5. M. Crochemore, C. S. Iliopoulos, Y. J. Pinzon and J. F. Reid, A fast bit-vector algorithm for the longest common subsequence problem, Inform. Process. Lett., 80(6), 2001, pp. 279-285, 2001. (PDF p. 13)
6. V. Dan³ cı́k, Expected length of the longest common subsequences, PhD thesis, University of War- wick, 1994. (PDF p. 13)
7. M. Crochemore, C.S. Iliopoulos, Y.J. Pinzon / Speeding-up Hirschberg and Hunt-Szymanski LCS Algorithms (PDF p. 14)
8. D.S. Hirschberg, A linear space algorithm for computing maximal common subsequences, Comm. Assoc. Comput. Mach., 18:6, 341–343, 1975. (PDF p. 14)
9. D.S. Hirschberg, Algorithms for the longest common subsequence problem, J. Assoc. Comput. Mach., 24:4, 664–675, 1977. (PDF p. 14)
10. J.W. Hunt and T.G. Szymanski, A fast algorithm for computing longest common subsequences, Comm. Assoc. Comput. Mach., 20, 350–353, 1977. (PDF p. 14)
11. V.I. Levenshtein, Binary codes capable of correcting deletions, insertions and reversals, Sov. Phys. Dokl., 6, 707–710, 1966. (PDF p. 14)
12. U. Manber, E. Myers and S. Wu, A subquadratic algorithm for approximate limited expression matching, Algorithmica, 15, 50–67, 1996. (PDF p. 14)
13. W.J. Masek and M.S. Paterson, A faster algorithm computing string edit distances, J. Comput. System Sci., 20, 18-31, 1980. (PDF p. 14)
14. E. Myers, A fast bit-vector algorithm for approximate string matching based on dynamic program- ming, J. Assoc. Comput. Mach., 46:3, 395–415, 1999. (PDF p. 14)
15. G. Navarro and M. Raf£not, A bit-parallel approach to suf£x automata: fast extended string match- ing, Combinatorial Pattern Matching, LNCS 1448, 14–33, 1998. (PDF p. 14)
16. N. Nakatsu, Y. Kambayashi, S. Yajima, A Longest common subsequence algorithm suitable for similar test strings, Acta Informatica, 18, 171–179, 1982. (PDF p. 14)
17. M. Paterson, V. Dan³ cı́k, Longest common subsequence, Proceedings of the 19th Intern. Symp. on Mathematical Foundations of Computer Science, LNCS 841, 127–142, 1994. (PDF p. 14)
18. D. Sankoff and J.B. Kruskal (eds), Time warps, string edits, and macromolecules: the theory and practice of sequence comparison, Addison-Wesley, Reading, MA, 1983. (PDF p. 14)
19. D. Sankoff and P.H. Sellers, Shortcuts, diversions and maximal chains in partially ordered sets, Discrete Mathematics, 4, 287–293, 1973. (PDF p. 14)
20. R.A. Wagner and M.J. Fisher, The string-to-string correction problem, J. Assoc. Comput. Mach., 21:1, 168–173, 1974. (PDF p. 14)
21. S. Wu and U. Manber, Fast text searching allowing errors, Comm. Assoc. Comput. Mach., 35, 83– 91, 1992. (PDF p. 14)
