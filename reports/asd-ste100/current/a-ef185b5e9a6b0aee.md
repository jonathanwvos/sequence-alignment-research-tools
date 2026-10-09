# Identification of Common Molecular Subsequences

- Work ID: `b-752559f16d4a`
- Asset ID: `a-ef185b5e9a6b0aee`
- Source PDF: `literature/academic-papers-processed/Identification of Common Molecular Subsequences - Smith, Waterman.pdf`
- SHA-256: `ef185b5e9a6b0aee0da9f96dc627ee19d7df661ee5e13e652c3ad9c78a8cef6d`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors give a matrix algorithm to find the most similar segment pair in two molecular sequences. (PDF p. 1).
- The method permits internal insertions and deletions. Traceback returns the selected segments and their alignment. (PDF p. 2).

## Objectives

- Find one segment from each sequence such that no other segment pair has a greater similarity score. Allow gaps of arbitrary length. (PDF p. 1).

## Arguments

- The authors argue that restricting the search to contiguous segments excludes the more general problem with internal insertions and deletions. (PDF p. 1).
- They claim that the algorithm provides a mathematically rigorous search and is simple to program. (PDF p. 3).

## Analysis

- Each matrix value represents the maximum similarity of segments that end at its two sequence positions. (PDF p. 1).
- The recurrence considers a paired residue, a gap in either sequence, and zero. Zero prevents negative segment scores. (PDF p. 2).

## Methods

- Initialize the first row and column to zero. Set H(i,j) to the maximum of H(i−1,j−1)+s(ai,bj), all H(i−k,j)−Wk, all H(i,j−l)−Wl, and zero. (PDF p. 1).
- Start traceback at the largest matrix value. Follow the contributing values until a zero is reached. (PDF p. 2).
- For the next-best segment pair, the authors prescribe traceback from the second-largest matrix element not associated with the first traceback. (PDF p. 2).

## Applications

- The method identifies similar molecular subsequences when an alignment includes mismatches and internal gaps. (PDF p. 3).

## Optimization

Not stated in the extractable source pages.

## Evaluation and testing

- The worked example uses a match score of 1, a mismatch score of −1/3, and a gap weight Wk = 1 + k/3. (PDF p. 2).
- The example scores have zero expected substitution score for random sequences with four equally probable letters. (PDF p. 2).

## Results

- The example matrix has a maximum score of 3.33 and marks its traceback path. (PDF p. 2).
- The resulting alignment contains both a mismatch and an internal deletion. (PDF p. 3).

## Limitations and uncertainty

Not stated in the extractable source pages.

## References

1. Beyer, W. A., Smith, T. F., Stein. M. L. & Ulam, S. M. (1979). Math. Biosci. 19, 9-25. (PDF p. 3)
2. Dayhoff. M. 0. (1969). Atlas of Protein Sequence and Structure, National Biomedical Research Foundation, Silver Springs, Maryland. (PDF p. 3)
3. Fitch, W. M. (1966). J. Mol. Biol. 16, 9-13. (PDF p. 3)
4. Needleman, S. B. & Wunsch, C. D. (1970). J. Mol. Biol. 48, 443-453. Reich&. T. A., Cohen, D. N. & Wong, A. K. C. (1973). J. Theoret. Biol. 42, 245-261. (PDF p. 3)
5. Sankoff, D. (1972). Proc. Nat. Acud. Sci., U.S.A. 61, 44. (PDF p. 3)
6. Sellers. P. H. (1974). J. Appl. Math. (Siam), 26, 787-793. (PDF p. 3)
7. Smith, T. F., Waterman, M. S. & Fitch, W. M. (1981). J. Mol. Evol. In the press. (PDF p. 3)
8. Waterman. M. S., Smith, T. F. & Beyer, W. A. (1976). Advan. Math. 20, 367-387. ,Votp added in proof: A weighting similar to that given above was independently developed by Walter Goad of Los Alamos Scientific Laboratory. (PDF p. 3)
