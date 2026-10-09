# A Fast and Practical Bit-Vector Algorithm for the Longest Common Subsequence Problem

- Work ID: `b-f04112d9509c`
- Asset ID: `a-ba8851bc0ebf1e50`
- Source PDF: `literature/academic-papers-processed/A Fast and Practical Bit-Vector Algorithm for the Longest Common Subsequence Problem - Crochemore et al.pdf`
- SHA-256: `ba8851bc0ebf1e5081507940c7a42c31c1a6968c9db1b0069d9dc355b006b296`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors present a bit-vector algorithm for LCS length with O(nm/w) time and O(m/w) space, where m ≤ n and w is the machine word size. (PDF p. 1).
- The algorithm processes dynamic programming columns through word-level parallelism. For m ≤ w, the authors give linear time and constant additional working space. (PDF p. 1).
- The authors report faster performance than Allison–Dix for all values used in their experiment. (PDF p. 6).

## Objectives

- The authors aim to simplify bit-vector LCS computation and reduce its operation count while retaining O(nm/w) time. (PDF p. 2).

## Arguments

- Adjacent values in a dynamic programming column differ by zero or one. This permits a bit-vector encoding of column differences. (PDF p. 3).
- The authors argue that column-wise addition can track LCS length for every text prefix through carries. This can support early termination. (PDF p. 2).

## Analysis

- The state transition selects candidate matches within blocks of one bits and moves the corresponding dominant-match boundaries. (PDF p. 6).
- Carry propagation acts independently within blocks separated by zero bits. A carry out indicates an increase in LCS length. (PDF p. 6).
- A column takes O(1) time when m ≤ w. For longer patterns, the stated per-column bound is O(m/w). (PDF p. 3).

## Methods

- Preprocessing builds a match vector for each alphabet symbol. A bit is one exactly where that symbol occurs in the shorter string. (PDF p. 4).
- The algorithm maintains the complement of the column-difference vector. AND selects eligible matches, addition propagates carries, and an OR correction restores required bits. (PDF p. 6).
- LCS length can be obtained by counting carries during updates or by counting zero bits in the final complemented state. (PDF p. 6).
- The authors propose Hirschberg divide-and-conquer to recover an actual LCS. Bit-vector length computation locates recursive middle points. (PDF p. 7).

## Applications

- The paper identifies text editing and molecular sequence analysis as applications of LCS and edit-distance computation. (PDF p. 2).
- With unit insertion and deletion costs and substitution cost two, LCS length p and optimal edit cost d satisfy p = (n + m − d)/2. (PDF p. 2).

## Optimization

- The authors reduce the stated bit-wise operation count from five in the optimized Allison–Dix expression to four. Their expression uses addition instead of subtraction. (PDF p. 2).
- Column-wise processing gives the stated O(m/w) space bound instead of the O(n/w) bound attributed to the compared row-wise method. (PDF p. 2).
- Match-vector preprocessing can restrict attention to symbols present in the shorter string when the alphabet is large. (PDF p. 4).

## Evaluation and testing

- The authors implement the arbitrary-pattern-length algorithm in C++ and compare it with Allison–Dix using alphabet size 26 and the stated setting t = p. (PDF p. 6).
- All trials run on a SUN Ultra Enterprise at 300 MHz under Solaris Unix. (PDF p. 6).

## Results

- The authors report that their implementation outperforms Allison–Dix throughout the tested values. (PDF p. 6).
- For LCS reconstruction, the authors state that Hirschberg recursion retains O(nm/w) total time and uses linear space at each iteration. (PDF p. 7).

## Limitations and uncertainty

- The constant-time column update requires m ≤ w. Longer patterns require multiple words. (PDF p. 3).
- The described match-vector construction assumes a finite alphabet. The paper directs readers elsewhere for infinite alphabets. (PDF p. 4).
- Interpretation: the reported timing advantage supports the tested implementation and settings. The supplied experiment uses one platform and alphabet size 26. (PDF p. 6).

## References

1. A.V. Aho, D.S. Hirschberg, J.D. Ullman, Bounds on the complexity of the longest common subsequence problem, J. ACM 23 (1976) 1–12. (PDF p. 7)
2. L. Allison, T.L. Dix, A bit-string longest common subsequence algorithm, Inform. Process. Lett. 23 (1986) 305–310. (PDF p. 7)
3. K.P. Bogart, Introductory Combinatorics, Pitman, New York, 1983. (PDF p. 7)
4. R.A. Baeza-Yates, G.H. Gonnet, A new approach to text searching, Comm. ACM 35 (1992) 74–82. (PDF p. 7)
5. D.S. Hirschberg, A linear space algorithm for computing maximal common subsequences, Comm. ACM 18 (6) (1975) 341–343. (PDF p. 7)
6. D.S. Hirschberg, An information theoretic lower bound for the longest common subsequence problem, Inform. Process. Lett. 7 (1) (1978) 40–41. (PDF p. 7)
7. V.I. Levenshtein, Binary codes capable of correcting deletions, insertions and reversals, Sov. Phys. Dokl. 6 (1966) 707–710. (PDF p. 7)
8. U. Manber, E. Myers, S. Wu, A subquadratic algorithm for approximate limited expression matching, Algorithmica 15 (1996) 50–67. (PDF p. 7)
9. W.J. Masek, M.S. Paterson, A faster algorithm computing string edit distances, J. Comput. System Sci. 20 (1980) 18–31. (PDF p. 7)
10. E. Myers, A fast bit-vector algorithm for approximate string matching based on dynamic programming, J. ACM 46 (3) (1999) 395–415. (PDF p. 7)
11. E.M. Reingold, J. Nievergelt, N. Deo, Combinatorial Algo- rithms: Theory and Practice, Prentice-Hall, Englewood Cliffs, NJ, 1977. (PDF p. 7)
12. D. Sankoff, P.H. Sellers, Shortcuts, diversions and maximal chains in partially ordered sets, Discrete Math. 4 (1973) 287– 293. (PDF p. 7)
13. D. Sankoff, J.B. Kruskal (Eds.), Time Warps, String Edits, and Macromolecules: The Theory and Practice of Sequence Comparison, Addison-Wesley, Reading, MA, 1983. (PDF p. 7)
14. R.A. Wagner, M.J. Fischer, The string-to-string correction problem, J. ACM 21 (1) (1974) 168–173. (PDF p. 7)
15. A.H. Wright, Approximate string matching using within-word parallelism, Soft. Pract. Exper. 24 (1994) 337–362. (PDF p. 7)
16. S. Wu, U. Manber, Fast text searching allowing errors, Comm. ACM 35 (1992) 83–91. (PDF p. 7)
