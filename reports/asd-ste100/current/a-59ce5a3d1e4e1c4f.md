# Improving the Worst Case Performance of the Hunt-Szymanski Strategy for the Longest Common Subsequence of Two Strings

- Work ID: `w-59ce5a3d1e4e`
- Asset ID: `a-59ce5a3d1e4e1c4f`
- Source PDF: `literature/academic-papers-processed/Improving the Worst Case Performance of the Hunt-Szymanski Strategy for the Longest Common Subsequence of Two Strings - Apostolico.pdf`
- SHA-256: `59ce5a3d1e4e1c4febd2190110c64434ff0da874835ee49e3be8fabfb2f54493`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The proposed longest common subsequence algorithm follows a schedule similar to Hunt–Szymanski while improving worst-case efficiency. (PDF p. 2).
- The author states that time depends on dominant matches rather than all matching position pairs, and never exceeds O(mn). (PDF p. 2).

## Objectives

- The author seeks to retain favorable Hunt–Szymanski behavior while avoiding poor performance on many other inputs. (PDF p. 2).
- The method aims to reduce dependence on r, the total number of matching position pairs. (PDF p. 2).

## Arguments

- At least one longest common subsequence uses a dominant match at every rank. Thus dominant matches suffice to solve the problem. (PDF p. 3).
- The author suggests that when r approaches mn, the number of dominant matches can become linear in the shorter input length. (PDF p. 2).

## Analysis

- The analysis uses input lengths m and n, with m no greater than n. It distinguishes all matches, counted by r, from dominant matches, counted by d. (PDF p. 3).
- The closing proof bounds batches of searches, insertions, and deletions on THRESH and AMATCHLIST structures. (PDF p. 13).
- For one row, all invoked AMATCHLIST structures contain at most n elements in total. The proof uses this fact to bound their combined work. (PDF p. 13).

## Methods

- The algorithm uses standard preprocessing and finger trees. (PDF p. 2).
- The formulation represents prefix longest common subsequence lengths in a matrix. Matching positions have ranks given by these prefix lengths. (PDF p. 3).

## Applications

- The method finds a maximum-length common subsequence of two strings over an alphabet. (PDF p. 3).

## Optimization

- The main reduction focuses computation on dominant matches, also called minimal candidates. (PDF p. 2).
- Once the dominant matches are available, a longest common subsequence can be recovered in O(m) time. (PDF p. 3).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- The abstract states an O(mn) worst-case time bound for the proposed algorithm. (PDF p. 2).
- The stated time bound depends on the dominant-match count d and does not always increase with the full match count r. (PDF p. 2).

## Limitations and uncertainty

- The supplied abstract gives the worst-case ceiling but does not state the complete time-bound formula in terms of d. (PDF p. 2).
- Simpler auxiliary data structures with the same performance are deferred to a future paper. (PDF p. 2).

## References

1. Apostolico. A. and C. Guerra The Longest Common Subsequence Problem Revisired, rypescript. Jan. 1985. (PDF p. 14)
2. Aho, A.D.. O.S. Hirschberg and J.D. Ullman. Bounds on the complexity of the maximal common subsequence problem, JACM 23. I, 1-12 (1976). [BTl Brown, MR.. and R.E. TaIjan. A representation of linear lists wilb. movable fingers. Proceedings of the ID-rh STOC J San Diego. Ca., 19-29 (197~). (PDF p. 14)
3. Brown, M.R., and R.E. Tarjan. A fast merging algorilhm,JACM 26,2,211-226 (1979). (PDF p. 14)
4. Hirschberg, D.S. Algorithms for the longest common subsequence problem, JACM 24, 4, 664-675 (1977). (PDF p. 14)
5. Hirschberg. D.S. A linear space algorithm forcompucing maximal common subsequences, CACM 18,6,341-343 (1975) (PDF p. 14)
6. Hum, I.W., and T.G. Szymanski. A fast algorithm for computing longest cornmon subse- quences, CACM 20,5, 350-353 (1977). (PDF p. 14)
7. Mehlhorn, K. Data Structures and Algorithms 1: Sorting and Searching, Springer-Verlag, EATCS Monographs on TCS (1984). [VE] van Emde Boas, P. Preserving order in a fores[ in less than logarithmic time and linear space. In!Proc.Lerr. 6,3, 80-82 (1977). (PDF p. 14)
