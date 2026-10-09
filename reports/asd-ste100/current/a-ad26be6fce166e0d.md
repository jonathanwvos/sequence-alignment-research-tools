# An almost-linear time and linear space algorithm for the longest common subsequence problem

- Work ID: `w-ad26be6fce16`
- Asset ID: `a-ad26be6fce166e0d`
- Source PDF: `literature/academic-papers-processed/An almost-linear time and linear space algorithm for the longest common subsequence problem - Guo, Hwang.pdf`
- SHA-256: `ad26be6fce166e0d8b839ea07bae1aa1d4e43eb528b012940bc369b30d82e6c6`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors present a primal-dual LCS implementation with O(nL) time and claimed O(n) space. L is the LCS length, and both input lengths are O(n). (PDF p. 2).
- The implementation uses nucleotide lookup tables and ordered candidate updates to avoid processing every matching pair. (PDF p. 4).

## Objectives

- The authors aim to combine the time advantage of a nondynamic-programming approach with linear space for DNA sequences. (PDF p. 1).

## Arguments

- For DNA sequences, the set of matching position pairs can have quadratic size. Explicit storage of this set is therefore costly. (PDF p. 2).
- Only the matching pair with the smallest second-sequence index in each assignment interval needs to be retained. (PDF p. 4).

## Analysis

- The correctness argument shows that the second-sequence indices of the maximal pairs increase across the sets C1 through Ck. These indices define the assignment intervals. (PDF p. 4).
- Table X takes O(n) time to construct. Ordered scans and at most L backtrack updates take O(L) time per input symbol, which gives O(nL) total time. (PDF p. 4).

## Methods

- The primal-dual procedure assigns each matching pair to the first compatible conjugate-order set. The number of sets gives the LCS length. Predecessor links recover an LCS. (PDF p. 2).
- Table X stores the next occurrence of each nucleotide after each position in J. Table Y stores current candidate pairs and their next nucleotide positions. (PDF p. 3).
- For each symbol in I, the algorithm processes candidate positions from largest to smallest. It replaces or adds columns in Y and records predecessor links. (PDF p. 3).

## Applications

- When substitutions are excluded, an alignment with minimum edit distance produces an LCS of the two DNA sequences. (PDF p. 1).
- The authors extend the implementation to general alphabets. With alphabet size p as a variable, they state O(n(L+p)) time and O(np) space. (PDF p. 4).

## Optimization

- The algorithm scans two ordered rows together. Each comparison removes one entry from further consideration, so at most 2L entries need inspection per input symbol. (PDF p. 4).

## Evaluation and testing

- A worked example uses I = TGCATA and J = ATCTGAT. Tables show candidate replacements and predecessor links. (PDF p. 3).
- The example traces two alternative LCS solutions, each with length four. (PDF p. 4).

## Results

- The authors conclude that their implementation achieves O(nL) time and O(n) space for a fixed DNA alphabet. (PDF p. 4).

## Limitations and uncertainty

- The authors describe the time bound as almost linear when L is small relative to n. Interpretation: O(nL) is quadratic when L grows in proportion to n. (PDF p. 4).
- Interpretation: the space argument explicitly covers tables X and Y. The excerpt does not separately bound storage for all predecessor links retained for traceback. (PDF p. 4).

## References

1. A. Apostolico, Improving the worst-case performance of the Hunt–Szymanski strategy for the longest common subsequence of two strings, Inform. Process. Lett. 23 (1986) 63–69. (PDF p. 4)
2. D.S. Hirschberg, A linear space algorithm for computing maxi- mal common subsequences, Comm. ACM 18 (1975) 341–343. J.Y. Guo, F.K. Hwang / Information Processing Letters 94 (2005) 131–135 135 (PDF p. 4)
3. D.S. Hirschberg, Algorithms for the longest common subse- quence problem, J. ACM 24 (1977) 664–675. (PDF p. 5)
4. J.W. Hunt, T.G. Szymanski, A fast algorithm for computing longest common subsequences, Comm. ACM 20 (1977) 350– 353. (PDF p. 5)
5. V.I. Levenshtein, Binary codes capable of correcting deletions, insertions and reversals, Soviet Phys. Dokl. 6 (1966) 707–710. (PDF p. 5)
6. S.B. Needleman, C.D. Wunsch, A general method applicable to the search for similarities in the amino acid sequence of two proteins, J. Mol. Biol. 48 (1970) 443–453. (PDF p. 5)
7. P.A. Pevzner, M.S. Waterman, Generalized sequence alignment and duality, Adv. Appl. Math. 14 (2) (1993) 139–171. (PDF p. 5)
