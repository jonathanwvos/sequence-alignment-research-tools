# Edit distance for a run-length-encoded string and an uncompressed string

- Work ID: `b-2147037060c3`
- Asset ID: `a-9cdbbea87795ea45`
- Source PDF: `literature/academic-papers-processed/Edit distance for a run-length-encoded string and an uncompressed string - Liu et al.pdf`
- SHA-256: `9cdbbea87795ea4586b6e2667dea29646136dd193d4b4323165511a35184e8af`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Liu and colleagues give an O(Mn)-time edit-distance algorithm for an RLE string with M runs and an uncompressed string of length n. (PDF p. 1).
- Choosing which string to process as RLE gives O(min{mN,Mn}) time. The authors improve the earlier O(mN+Mn) bound. (PDF p. 1).

## Objectives

- The authors aim to compute edit distance directly from one compressed string. The computation depends on its run count rather than its full length. (PDF p. 2).

## Arguments

- A run-level recurrence splits the uncompressed prefix at position u. It combines the previous run-row value with the distance between the current run and the remaining substring. (PDF p. 2).
- Adjacent entries in a run row differ by −1, 0, or 1. This restricts each new entry to three candidate values. (PDF p. 3).

## Analysis

- For a run of length l with symbol τ, its distance to a substring of length s is max{l,s}−min{l,c}. Here, c counts occurrences of τ in that substring. (PDF p. 3).
- Prefix counts provide c in constant time. A linear scan builds these counts in O(n) time for each required symbol. (PDF p. 3).
- Each of M run rows takes O(n) time to initialize and fill. Constant-time updates and candidate checks give O(Mn) total time. (PDF p. 4).

## Methods

- The algorithm builds arrays A[t]=D(i−1,t)+countτ(t), B[t]=A[t]−t, and C[t]=D(i−1,t)−t. They encode three cases of the run-to-substring distance. (PDF p. 3).
- Inverted lists retain the largest eligible index for A and B and the smallest eligible index for C. UpdateInvertedLists updates them in constant time as the column advances. (PDF p. 4).
- TestGuessing checks a proposed distance against three value and range conditions. The algorithm tries the previous entry minus one, then the previous entry. If both fail, it adds one. (PDF p. 4).

## Applications

- For two strings with lengths m and n and run counts M and N, the algorithm can use either orientation. Choosing the smaller product gives O(min{mN,Mn}) time. (PDF p. 5).

## Optimization

- Inverted lists replace linear searches through A, B, and C with constant-time candidate checks. (PDF p. 4).
- The authors state that diagonal table evaluation supports an EREW PRAM implementation. It uses O(min{M,n}) processors and O(M+n) time. (PDF p. 5).

## Evaluation and testing

- A worked example uses X=b1a4 and Y=aaaababa. For D(2,6), TestGuessing rejects 1 and accepts 2, so the entry equals 2. (PDF p. 5).

## Results

- Theorem 1 states that Algorithm 3 computes the edit distance between the RLE and uncompressed inputs in O(Mn) time. (PDF p. 5).
- The authors state that the main lemmas extend to weighted operations when each cost divided by the costs' greatest common divisor is O(1). (PDF p. 5).

## Limitations and uncertainty

- The main algorithm uses unit insertion, deletion, and substitution costs. The stated weighted extension requires bounded normalized costs. (PDF p. 5).
- The running-time bound still includes one uncompressed string length. (PDF p. 5).

## References

1. O. Arbell, G.M. Landau, J.S.B. Mitchell, Edit distance of run- length encoded strings, Information Processing Letters 83 (2002) 307–314. (PDF p. 5)
2. Z. Bar-Yossef, T.S. Jayram, R. Krauthgamer, R. Kumar, Ap- proximating edit distance efficiently, in: Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science, 2004. (PDF p. 5)
3. H. Bunke, J. Csirik, An improved algorithm for computing the edit distance of run length coded strings, Information Processing Letters 54 (1995) 93–96. (PDF p. 5)
4. M. Crochemore, G.M. Landau, M. Ziv-Ukelson, A subquadratic sequence alignment algorithm for unrestricted scoring matrices, SIAM Journal of Computing 32 (6) (2003) 1654–1673. (PDF p. 5)
5. Z. Galil, K. Park, Data structures and algorithms for approximate string matching, Journal of Complexity 4 (1988) 33–72. (PDF p. 5)
6. Z. Galil, K. Park, An improved algorithm for approximate string matching, SIAM Journal on Computing 19 (6) (1990) 989–999. (PDF p. 5)
7. D. Gusfield, Algorithms on Strings, Trees, and Sequences, Cam- bridge University Press, 1997. (PDF p. 5)
8. V.I. Levenshtein, Binary codes capable of correcting, deletions, insertions and reversals, Soviet Physics Doklady 10 (1996) 707– 710. (PDF p. 5)
9. K. Sayoood, E. Fow (Eds.), Introduction to Data Compression, second ed., Morgan Kaufmann, Los Altos, CA, 2000. (PDF p. 5)
10. J. Tarhio, E. Ukkonen, Approximate Boyer–Moore string match- ing, SIAM Journal on Computing 22 (2) (1993) 243–260. (PDF p. 5)
11. E. Ukkonen, Algorithms for approximate string matching, Infor- mation and Control 64 (1985) 100–118. (PDF p. 5)
