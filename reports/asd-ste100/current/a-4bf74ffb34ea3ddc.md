# Distinct squares in run-length encoded strings

- Work ID: `w-4bf74ffb34ea`
- Asset ID: `a-4bf74ffb34ea3ddc`
- Source PDF: `literature/academic-papers-processed/Distinct squares in run-length encoded strings - Liu.pdf`
- SHA-256: `4bf74ffb34ea3ddcbd2dd5e4c640a4982ca7f1f25eb6791c875b71b41b90418a`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Liu proves that the number of distinct square types in the covering set is less than (14/3)N. Here, N is the number of runs in the run-length encoding. (PDF p. 6).
- The covering set contains nontrivial squares that no earlier square can cover through successive right rotations. (PDF p. 2).

## Objectives

- The author seeks a bound on the number of rc-occurrences in terms of the number of runs. Each rc-occurrence represents one distinct square type in the covering set. (PDF p. 2).

## Arguments

- Two squares of equal length that start in the same run cannot both be c-squares. The earlier square covers the later square. (PDF p. 2).
- For each rc-occurrence, at most one shorter rc-occurrence can start later in the same run. (PDF p. 3).

## Analysis

- The proof separates rc-occurrences inside a square into occurrences that cross its midpoint and occurrences in its second half. (PDF p. 6).
- At most 2r(t) c-squares cross the midpoint of a nontrivial square t. Here, r(t) counts its runs. (PDF p. 6).
- The induction adds one run at the start of the string. It bounds occurrences in that run, occurrences across the longest square's midpoint, and occurrences in the remaining suffix. (PDF p. 6).

## Methods

- The rc-set retains the last c-square occurrence of each square type. This occurrence need not be the last occurrence of that type in the full string. (PDF p. 2).
- The proof uses an earlier method that groups squares across a run boundary by an interval of starting positions and a common length. Each group contributes one c-square. (PDF p. 6).

## Applications

- The author proposes using the bound to report squares in run-length encoded strings and leftmost occurrences of maximal periodic intervals. (PDF p. 7).

## Optimization

Not stated in the extractable source pages.

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- Theorem 2 bounds the number of rc-occurrences by less than (14/3)N. (PDF p. 6).
- The c-vocabulary has the same size as the rc-set. Thus, the same bound applies to the c-vocabulary. (PDF p. 7).

## Limitations and uncertainty

- The bound concerns c-vocabulary, which excludes trivial squares and squares covered by earlier occurrences. (PDF p. 2).
- The author leaves O(N)-time identification of c-vocabulary and O(N+z)-time reporting as future work. The conclusion does not provide these algorithms. (PDF p. 7).

## References

1. M. Crochemore, W. Rytter, Squares, cubes, and time-space efficient string searching, Algorithmica 13 (1995) 405–425. (PDF p. 7)
2. Maxime Crochemore, W. Rytter, Jewels of Stringology, World Scientific, Singapore, 2002. (PDF p. 7)
3. Maxime Crochemore, Lucian Ilie, Maximal repetitions in strings, Journal of Computer and System Sciences 74 (5) (2008) 796–807. (PDF p. 7)
4. Avieri S. Fraenkel, Jamie Simpson, How many squares can a string contain? Journal of Combinatorial Theory, Series A 82 (1998) 112–120. (PDF p. 7)
5. D. Gusfield, J. Stoye, Linear time algorithm for finding and representing all the tandem repeats in a string, Journal of Computer and System Sciences 69 (4) (2004) 525–546. (PDF p. 7)
6. Lucian Ilie, A simple proof that a word of length n has at most 2n distinct squares, Journal of Combinatorial Theory, Series A 112 (2005) 163–164. (PDF p. 7)
7. Lucian Ilie, A note on the number of squares in a word, Theoretical Computer Science 380 (2007) 373–376. (PDF p. 7)
8. J.J. Liu, G.S. Huang, Y.L. Wang, A fast algorithm for finding the positions of all squares in a run-length encoded string, Theoretical Computer Science 410 (2009) 3942–3948. (PDF p. 7)
9. D.E. Knuth, J.H. Morris, V.R. Pratt, Fast pattern-matching in strings, SIAM Journal on Computing 6 (2) (1977) 323–350. (PDF p. 7)
10. M.G. Main, R.J. Lorentz, An O(n log n) algorithm for recognizing repetitions, Technical Report CS-79-056, Washington State University, 1979. (PDF p. 7)
11. M.G. Main, R.J. Lorentz, An O(n log n) algorithm for finding all repetitions in a string, Journal of Algorithms 5 (3) (1984) 422–432. (PDF p. 7)
12. M.G. Main, Detecting Leftmost Maximal periodicities, Discrete Applied Mathematics 25 (1989) 145–153. (PDF p. 7)
