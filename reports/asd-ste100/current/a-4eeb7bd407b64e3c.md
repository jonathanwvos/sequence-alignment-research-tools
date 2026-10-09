# Algorithms for Computing the Longest Parameterized Common Subsequence

- Work ID: `w-4eeb7bd407b6`
- Asset ID: `a-4eeb7bd407b64e3c`
- Source PDF: `literature/academic-papers-processed/Algorithms for Computing the Longest Parameterized Common Subsequence - Iliopoulos et al.pdf`
- SHA-256: `4eeb7bd407b64e3c48645d7befae8913267ae6c04a96acfdf12abac1a4aba021`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors introduce LPCS to combine four gap-constrained LCS variants in one model. (PDF p. 3).
- They give LPCS time bounds of O(n²) and O(n + R log n). They give RELAG and RIFIG a time bound of O(n + R). (PDF p. 8).

## Objectives

- Find the maximum common subsequence length under bounds on successive index distances and on the difference between these distances in the two strings. (PDF p. 3).

## Arguments

- FIG, ELAG, RIFIG, and RELAG are special cases of LPCS. Setting D = 0 requires equal index distances in both strings. (PDF p. 3).

## Analysis

- R counts position pairs with equal symbols. It measures the number of matches that the sparse algorithms process. (PDF p. 3).
- AlgRELAG processes each position in the union of the match set and its shifted copy in constant amortized time. This gives O(n + R) total time. (PDF p. 8).

## Methods

- AlgRELAG scans each diagonal in increasing row order. It processes matches and matches shifted by −K1 in both coordinates. (PDF p. 8).
- A one-dimensional vector stores diagonal values. A max-queue supplies the values needed to extend a subsequence at each match. (PDF p. 8).

## Applications

- The authors trace the motivation for gap constraints to computational molecular biology. They refer to earlier work for application details. (PDF p. 2).

## Optimization

- The max-queue uses a window of K2 − K1 + 1. Dummy insertions remove expired entries before a maximum query. (PDF p. 8).
- Each queue element is inserted and removed once. The algorithm clears only modified vector cells after each diagonal. (PDF p. 8).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- The authors state that the O(n²) LPCS algorithm improves earlier bounds for FIG, ELAG, and RELAG. (PDF p. 8).
- For sparse matches, the authors provide O(n + R) algorithms for the rigid variants and O(n + R log n) algorithms for FIG and ELAG. The latter method extends to LPCS. (PDF p. 8).

## Limitations and uncertainty

- The O(n + R) construction and sorting of the match sets assume an alphabet of polynomially bounded integers. (PDF p. 8).
- Interpretation: the benefit of bounds expressed through R depends on match density. The authors highlight the case R = o(n²). (PDF p. 8).

## References

1. Arlazarov, V.L., Dinic, E.A., Kronrod, M.A., Faradzev, I.A.: On economic con- struction of the transitive closure of a directed graph (english translation). Soviet Math. Dokl. 11, 1209–1210 (1975) (PDF p. 9)
2. Brenda, S.: Baker. Parameterized diﬀ. In: Symposium of Discrete Algorithms (SODA), pp. 854–855 (1999) (PDF p. 9)
3. Baker, B.S., Giancarlo, R.: Sparse dynamic programming for longest common sub- sequence from fragments. Journal of Algorithms 42(2), 231–254 (2002) (PDF p. 9)
4. Bergroth, L., Hakonen, H., Raita, T.: A survey of longest common subsequence algorithms. In: String Processing and Information Retrieval (SPIRE), pp. 39–48. IEEE Computer Society, Los Alamitos (2000) (PDF p. 9)
5. Cormen, T.H., Leiserson, C.E., Rivest, R.L.: Introduction to algorithms. MIT Press, McGraw Hill, Cambridge (1992) (PDF p. 9)
6. Crochemore, M., Landau, G.M., Ziv-Ukelson, M.: A sub-quadratic sequence align- ment algorithm for unrestricted cost matrices. In: Symposium of Discrete Algo- rithms (SODA), pp. 679–688 (2002) (PDF p. 9)
7. Hadlock, F.: Minimum detour methods for string or sequence comparison. Con- gressus Numerantium 61, 263–274 (1988) (PDF p. 9)
8. Hirschberg, D.S.: Algorithms for the longest common subsequence problem. Journal of ACM 24(4), 664–675 (1977) (PDF p. 9)
9. Hunt, J.W., Szymanski, T.G.: A fast algorithm for computing longest subse- quences. Commun. ACM 20(5), 350–353 (1977) (PDF p. 9)
10. Iliopoulos, C.S., Rahman, M.S.: Algorithms for computing variants of the longest common subsequence problem. Theoretical Computer Science (to Appear) (PDF p. 9)
11. Jiang, T., Li, M.: On the approximation of shortest common supersequences and longest common subsequences. SIAM Journal of Computing 24(5), 1122–1139 (1995) (PDF p. 9)
12. Levenshtein, V.I.: Binary codes capable of correcting deletions, insertions, and reversals. Problems in Information Transmission 1, 8–17 (1965) (PDF p. 9)
13. Maier, D.: The complexity of some problems on subsequences and supersequences. Journal of the ACM 25(2), 322–336 (1978) (PDF p. 9)
14. Masek, W.J., Paterson, M.: A faster algorithm computing string edit distances. J. Comput. Syst. Sci. 20(1), 18–31 (1980) (PDF p. 9)
15. Mäkinen, V., Navarro, G., Ukkonen, E.: Transposition invariant string matching. Journal of Algorithms 56, 124–153 (2005) (PDF p. 9)
16. Myers, E.W.: An O(ND) diﬀerence algorithm and its variations. Algorithmica 1(2), 251–266 (1986) (PDF p. 9)
17. Nakatsu, N., Kambayashi, Y., Yajima, S.: A longest common subsequence algo- rithm suitable for similar text strings. Acta Inf. 18, 171–179 (1982) (PDF p. 9)
18. Rahman, M.S., Iliopoulos, C.S.: Algorithms for computing variants of the longest common subsequence problem. In: Asano, T. (ed.) ISAAC 2006. LNCS, vol. 4288, pp. 399–408. Springer, Heidelberg (2006) (PDF p. 9)
19. Wagner, R.A., Fischer, M.J.: The string-to-string correction problem. Journal of ACM 21(1), 168–173 (1974) (PDF p. 9)
