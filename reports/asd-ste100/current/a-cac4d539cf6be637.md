# A Relative Position based Algorithm to find out the Longest Common Subsequence from Multiple Biological Sequences

- Work ID: `w-cac4d539cf6b`
- Asset ID: `a-cac4d539cf6be637`
- Source PDF: `literature/academic-papers-processed/A Relative Position based Algorithm to find out the Longest Common Subsequence from Multiple Biological Sequences - Shukla, Agarwal.pdf`
- SHA-256: `cac4d539cf6be637e30a144b827ec1426a1f2981a13802f1e8b38bf6bb07d475`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors propose a heuristic for common subsequences of multiple biological sequences. It selects characters from their relative positions. (PDF p. 2).
- The method combines character scores, two pruning rules, and one processor per alphabet character. (PDF p. 3).
- Reported length ratios exceed 97% in the listed tests. These results do not show exact LCS recovery in every case. (PDF p. 6).

## Objectives

- The authors aim to reduce search work through pruning and support DNA, RNA, protein, and general sequences with a known alphabet. (PDF p. 1).

## Arguments

- After choosing a character, the method considers positions relative to that choice. The authors argue that earlier sequence portions no longer need processing. (PDF p. 2).
- The authors show a three-sequence example where the compared Rizvi–Agarwal heuristic returns TAT of length three. They identify ATAT of length four as an LCS. (PDF p. 2).

## Analysis

- For each candidate character, X sums its relative positions. Y scales the sum of pairwise absolute position differences by k divided by the number of sequence pairs. Z equals X+Y. (PDF p. 2).
- The authors claim O(n) time for the DNA case. They describe parallel runtime as O(K), where K is the time of the slowest processor. (PDF p. 7).
- Interpretation: the second pruning rule bounds candidate scores because Y is nonnegative. This score argument alone does not prove global LCS optimality. (PDF p. 3).

## Methods

- The method forms one position tuple for each alphabet character from its next occurrence in each sequence. (PDF p. 2).
- It selects the character with minimum Z. The stated tie rule uses minimum X when the two lowest Z values are equal. (PDF p. 3).
- Parallel execution assigns one processor to each alphabet character. The DNA example uses four processors. (PDF p. 2).

## Applications

- The authors use multiple biological sequence comparison as the main application and describe LCS as a measure of sequence similarity. (PDF p. 1).
- They state that the method can extend to protein sequences with 20 alphabet characters. (PDF p. 7).

## Optimization

- Pruning rule 1 removes a candidate when another candidate at the same level has a strictly smaller position in every sequence. (PDF p. 3).
- Pruning rule 2 first computes Z for the candidate with minimum X. It then removes candidates whose X is at least that Z value. (PDF p. 3).
- Relative positions allow the method to defer consideration of later sequence characters until processing reaches them. (PDF p. 2).

## Evaluation and testing

- Timing tables compare processing with and without pruning, relative and absolute positions, and the Rizvi–Agarwal algorithm. Sequence lengths range from 600 to 3000. (PDF p. 6).
- A separate timing comparison varies the sequence count across 3, 5, 7, and 9. (PDF p. 6).
- The paper defines precision as obtained subsequence length divided by actual LCS length, multiplied by 100. Its table covers lengths from 80 to 800. (PDF p. 6).

## Results

- At length 3000, the timing table reports 2.527 with pruning and 2.692 without pruning. The supplied table does not state time units. (PDF p. 6).
- For nine sequences, reported time is 1.318 with relative positions and 2.837 with absolute positions. (PDF p. 6).
- At length 3000, reported time is 2.527 for the proposed method and 2.841 for Rizvi–Agarwal. (PDF p. 6).
- The listed precision values range from 97.122% to 98.571% for the proposed method and from 93.258% to 97.143% for Rizvi–Agarwal. (PDF p. 6).

## Limitations and uncertainty

- The authors explicitly describe both compared algorithms as heuristic. Ratios below 100% show that the proposed method can miss the actual LCS length. (PDF p. 6).
- The supplied benchmark page does not identify hardware, dataset provenance, repetitions, or the method used to obtain actual LCS lengths. (PDF p. 6).
- Interpretation: the O(K) parallel claim does not quantify processor work as the number of sequences grows. (PDF p. 7).

## References

1. Apostolico A, Atallah M, Larmore L, Mcfaddin S: Efficient parallel algorithms for string editing and related problems. SIAM J Computing 1990, 19:968-988. (PDF p. 7)
2. Jiang, T. and Li, M.: On the approximation of shortest common supersequences and longest common subsequences. SIAM Journal of Computing, 1995, 24, 1122-1139. (PDF p. 7)
3. Babu KN, Systems W, Saxena S: Parallel algorithms for the longest common subsequence problem. 4th International Conference on High Performance Computing 1997:18-21. (PDF p. 7)
4. Bonizzoni, P., Vedova, G.D. and Mauri, G. Experimenting an approximation algorithm for the LCS. Discrete Applied Mathematics, 2001, 110, 13 - 24. (PDF p. 7)
5. Bergroth L, Hakonen H, Raita T: A survey of longest common subsequence algorithms. Seventh International Symposium on String Processing Information Retrieval 2000:39-48. (PDF p. 7)
6. Huang Kuo-Si, Yang Chang-Biau, Tseng Kuo-Tsung,et al. : Fast Algorithms for Finding the Common Subsequence of Multiple Sequences, International Computer Symposium, 2004 (PDF p. 7)
7. Rizvi SAM, Agarwal P: A New Index-Based Parallel Algorithm for finding Longest Common Subsequence in Multiple DNA Sequences. International Conference in Cognitive Systems, 2005 (PDF p. 7)
8. Chen Y, Wan A, Liu W, et al.: A fast parallel algorithm for finding the longest common subsequence of multiple biosequences. BMC Bioinformatics, 2006. (PDF p. 7)
9. Xiang X, Zhang D, Qin J, et al.: A New Algorithm for the Longest Common Subsequence Problem. International Conference on Computational Intelligence and Security Workshops, 2007. (PDF p. 7)
10. FASTA Database - http://www.neb.com/nebecomm/tech_reference/ restriction_enzymes/dna_sequences_maps.asp (PDF p. 7)
