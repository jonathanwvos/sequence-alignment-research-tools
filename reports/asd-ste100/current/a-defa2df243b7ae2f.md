# Heaviest Increasing-Common Subsequence Problems

- Work ID: `b-b40535e4409d`
- Asset ID: `a-defa2df243b7ae2f`
- Source PDF: `literature/academic-papers-processed/Heaviest Increasing-Common Subsequence Problems - Jacobson, Vo.pdf`
- SHA-256: `defa2df243b7ae2f1a9676da5496216299ce289f575366c57d2689e599c7f506`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors define heaviest increasing subsequence (HIS) and heaviest common subsequence (HCS) problems as weighted extensions of LIS and LCS. (PDF p. 1).
- They extend the Robinson–Schensted algorithm to HIS. A correspondence that preserves weights then gives an HCS algorithm. (PDF p. 12).

## Objectives

- Find increasing and common subsequences with maximum total weight. Weights can depend on symbols and their positions. (PDF p. 2).
- Refine the HCS algorithm for regular weight patterns, including weights that depend only on symbols. (PDF p. 12).

## Arguments

- The authors argue that the correspondence between increasing and common subsequences makes Hunt–Szymanski a special case of Robinson–Schensted. (PDF p. 3).
- The number of dominant matches can be much smaller than the total number of matches. This motivates algorithms whose cost depends on dominant matches. (PDF p. 2).

## Analysis

- The authors give an O(n log n) time bound for HIS and an O(r log n) bound for HCS, where r is the number of matches. (PDF p. 12).
- They report conditions under which their HCS algorithms take O(d log n) time, where d counts generalized dominant matches. (PDF p. 13).

## Methods

- The method maps common subsequence problems to increasing subsequence problems through a bijection that preserves weights. (PDF p. 3).
- Algorithm hcs2 builds position lists for symbols in the second sequence. It scans matching positions backwards and updates an ordered list of position and weight pairs. (PDF p. 12).
- Algorithm hcs4 combines the refinements for decreasing weights in each sequence. It applies when weights depend only on symbols. (PDF p. 12).

## Applications

- The minimal distance LCS problem supports screen updates. It selects an LCS that minimizes the total displacement of matched lines. (PDF p. 2).
- A heaviest stable set in a permutation graph with weighted nodes is a special case of HIS. (PDF p. 2).

## Optimization

- Algorithm hcs3 removes a position from its position list after insertion into L. This avoids repeated processing of that position. (PDF p. 13).
- Algorithm hcs3 restores a position to its position list when it leaves L or when its predecessor in L changes. (PDF p. 13).
- For position-independent weights, hcs4 omits a test required by the general algorithm. With constant weights, it reduces to Apostolico–Guerra LCS. (PDF p. 12).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- The authors obtain weighted generalizations of the Hunt–Szymanski and Apostolico–Guerra LCS algorithms. (PDF p. 12).
- The authors report that their derivation reveals a bug in the original Apostolico–Guerra algorithm description. (PDF p. 3).

## Limitations and uncertainty

- The O(d log n) result is conditional. The authors do not state it as an unrestricted bound for arbitrary HCS weights. (PDF p. 13).
- The authors leave extensions of tableau and plane partition results to future work. (PDF p. 13).

## References

1. A. V. Aho, D. S. Hirschberg, and J. D. Ullman. Bounds on the complexity of the longest common subsequence problem. JACM, 23(1):1-12, 1976. (PDF p. 14)
2. A. Apostolico and C Guerra. The longest common subsequence problem revisited. Algorithmica, 2:315-336, 1987. (PDF p. 14)
3. Francis Y. L. Chin and C. K. Poon. A fast algorithm for computing longest common subsequences of small alphabet size. Journal of Information Processing,13(4):463-469, 1990. (PDF p. 14)
4. Michael L. Fredman. On computing the length of longest increasing subsequences. Discrete Mathematics, lh29-35, 1975. (PDF p. 14)
5. E. Gansner. Matrix Correspondences and the Enumeration of Plane Partitions. PhD thesis, MIT, Cambridge, MA, 1978. (PDF p. 14)
6. M. Golumbic. Algorithmic Graph Theory and Perfect Graphs. Academic Press, 1980. (PDF p. 14)
7. Daniel S. Hirschberg. A linear space algorithm for computing maximal common sub- sequences. CACM, 18(6):341-343, 1975. (PDF p. 14)
8. Daniel S. Hirschberg. Algorithms for the longest common subsequence problem. JACM, 24(4):664-675, 1977. (PDF p. 14)
9. W. J. Hsu and M. W. Du. New algorithms for the LCS problem. JCSS, 29:133-152, 1984. (PDF p. 14)
10. J. W. Hunt and M. D. McIlroy. An algorithm for differential file comparison. Computer Science Technical Report 41, Bell Laboratories, 1975. (PDF p. 14)
11. James W. Hunt and Thomas G. Szymanski. A fast algorithm for computing longest common subsequences. CACM, 20(5):350-353, 1977. 66 (PDF p. 14)
12. D. Knuth. The Art of Computer Programming, volume 3. Addison-Wesley, Reading, MA, 1973. (PDF p. 15)
13. William J. Masek and Michael S. Patterson. A faster algorithm computing string edit distances. JCSS, 20:18-31, 1980. (PDF p. 15)
14. Eugene W. Myers. An O(ND) difference algorithm and its variations. Algorithmica, 1:251-266, 1986. (PDF p. 15)
15. N. Nakatsu, Y. Kambayashi, and S. Yajima. A longest common subsequence algorithm suitable for similar text strings. Acta Informatica, 18:171-179, 1982. (PDF p. 15)
16. G. De B. Robinson. On the representations of the symmetric group. American J. Math., 60:745-760, 1938. (PDF p. 15)
17. D. Sankoff and J.B. Kruskal. Time Warps, String Edits and Macromolecules: The Theory and Practice of Sequence Comparisons. Addison Wesley, Reading, MA, 1983. (PDF p. 15)
18. C. Schensted. Largest increasing and decreasing subsequences. Canadian J. Math., 13:179-191, 1961. (PDF p. 15)
19. D. Sleator and R. Tarjan. Self-adjusting binary trees. JACM, 32:652-686, 1985. (PDF p. 15)
20. R. Stanley. Theory and applications of plane partitions. Stud. Applied Math., 50:259- 279, 1971. (PDF p. 15)
21. K.-P. Vo. More <curses>: the <screen> library. Technical report, AT&T Bell Labo- ratories, 1986. (PDF p. 15)
22. K.-P. Vo and R. Whitney. Tableaux and matrix correspondences. J. o] Comb. Theory, Series A, 35:323-359, 1983. (PDF p. 15)
23. R. A. Wagner and M. J. Fischer. The string-to-string correction problem. YACM, 21(1):168-173, 1974. (PDF p. 15)
24. Sun Wu, Udi Manber, Gene Myers, and Webb Miller. An O(NP) sequence comparison algorithm. Information Processing Letters, 35(6):317-323, 1990. (PDF p. 15)
25. A. Young. The collected papers of alfred young. Math. Exp., 21, 1977. (PDF p. 15)
