# Algorithms for Two Versions of LCS Problem for Indeterminate Strings

- Work ID: `w-ccdc85fa0ac7`
- Asset ID: `a-ccdc85fa0ac74275`
- Source PDF: `literature/academic-papers-processed/Algorithms for Two Versions of LCS Problem for Indeterminate Strings - Iliopoulos et al.pdf`
- SHA-256: `ccdc85fa0ac74275b1e07636cd41f6fbef69c37f35be72ada00cced63a52266a`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors study LCS for indeterminate strings, where each position contains a nonempty set of symbols. Two positions match when their sets intersect. (PDF p. 3).
- They also study constrained ILCS. Its output must contain a given plain string Z as a subsequence. (PDF p. 3).

## Objectives

- Develop ILCS and CILCS algorithms whose bounds account for alphabet size, maximum set size ℓ, and match counts. (PDF p. 1).

## Arguments

- Precomputed match tables let dynamic programming algorithms for standard strings use constant-time tests for indeterminate matches. (PDF p. 5).
- Indeterminate equality is not transitive. It depends on a nonempty intersection between the two symbol sets. (PDF p. 3).

## Analysis

- Binary encoding costs O(n|Σ|) time and space. The authors divide the matrices into |Σ| by |Σ| blocks to obtain O(n²|Σ|^0.376) multiplication time. (PDF p. 5).
- For CILCS, initializing the triple-match table costs O(n²p). Filling it costs O(R3ℓ), where R3 counts triples compatible with the corresponding symbol of Z. (PDF p. 10).

## Methods

- Encode each position as a binary membership vector. Boolean matrix multiplication constructs the pairwise intersection table I. (PDF p. 5).
- For CILCS, construct symbol-position lists for both input strings and Z. Enumerate compatible triples to fill I3. (PDF p. 10).
- The tables I and I3 provide constant-time tests for pair matches and matches that also satisfy a constraint symbol. (PDF p. 10).

## Applications

- The authors motivate indeterminate strings through DNA polymorphism, including variation in protein coding regions and gene-family binding sites. (PDF p. 2).

## Optimization

- The authors use fast square matrix multiplication on blocks to accelerate intersection preprocessing. (PDF p. 5).
- They also give an alternative based on Boolean matrix multiplication on a word RAM. Its stated ILCS bound is O(n|Σ| + n²|Σ|/log²|Σ|). (PDF p. 5).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- Theorem 2 gives an ILCS time bound of O(n|Σ| + n²|Σ|^0.376). (PDF p. 5).
- Theorem 8 gives a CILCS time bound of O(nℓ + n²p + ℓ(R + R3)). Here p is the constraint length, R counts pair matches, and R3 counts triple matches. (PDF p. 10).

## Limitations and uncertainty

- R3 can reach n²p in the worst case. The authors suggest that smaller values can occur in practice. (PDF p. 11).
- The authors leave practical performance tests and comparisons between their algorithms for future work. (PDF p. 11).
- The exposition assumes equal input lengths. The authors state that their results extend to unequal lengths. (PDF p. 3).

## References

1. V. Arlazarov, E. Dinic, M. Kronrod, and I. Faradzev. On economic construction of the transitive closure of a directed graph (english translation). Soviet Math. Dokl., 11:1209–1210, 1975. (PDF p. 11)
2. A. N. Arslan and Ö. Eğecioğlu. Algorithms for the constrained longest common subsequence problems. Int. J. Found. Comput. Sci., 16(6):1099–1109, 2005. (PDF p. 11)
3. M. D. Atkinson and N. Santoro. A practical algorithm for boolean matrix multi- plication. Inf. Process. Lett., 29(1):37–38, 1988. (PDF p. 11)
4. J. Basch, S. Khanna, and R. Motwani. On diameter verification and boolean ma- trix multiplication. Technical Report, Department of Computer Science, Stanford University, (STAN-CS-95-1544), 1995. (PDF p. 11)
5. L. Bergroth, H. Hakonen, and T. Raita. A survey of longest common subsequence algorithms. In String Processing and Information Retrieval (SPIRE), pages 39–48. IEEE Computer Society, 2000. (PDF p. 11)
6. F. Y. L. Chin, A. D. Santis, A. L. Ferrara, N. L. Ho, and S. K. Kim. A simple algorithm for the constrained sequence problems. Inf. Process. Lett., 90(4):175– 179, 2004. (PDF p. 11)
7. D. Coppersmith and S. Winograd. Matrix multiplication via arithmetic progres- sions. J. Symb. Comput., 9(3):251–280, 1990. (PDF p. 12)
8. T. H. Cormen, C. E. Leiserson, and R. L. Rivest. Introduction to Algorithms. The MIT Press and McGraw-Hill Book Company, 1989. (PDF p. 12)
9. C. S. Iliopoulos and M. S. Rahman. Algorithms for computing variants of the longest common subsequence problem. Theoretical Computer Science, 2007. To Appear. (PDF p. 12)
10. V. Mkinen, G. Navarro, and E. Ukkonen. Transposition invariant string matching. Journal of Algorithms, 56:124–153, 2005. (PDF p. 12)
11. M. S. Rahman and C. S. Iliopoulos. Algorithms for computing variants of the longest common subsequence problem. In T. Asano, editor, ISAAC, volume 4288 of Lecture Notes in Computer Science, pages 399–408. Springer, 2006. (PDF p. 12)
12. M. S. Rahman and C. S. Iliopoulos. A new efficient algorithm for computing the longest common subsequence. In M.-Y. Kao and X.-Y. Li, editors, AAIM, volume 4508 of Lecture Notes in Computer Science, pages 82–90. Springer, 2007. (PDF p. 12)
13. W. Rytter. Fast recognition of pushdown automaton and context-free languages. Information and Control, 67(1-3):12–22, 1985. (PDF p. 12)
14. Y.-T. Tsai. The constrained longest common subsequence problem. Inf. Process. Lett., 88(4):173–176, 2003. (PDF p. 12)
15. P. van Emde Boas. Preserving order in a forest in less than logarithmic time and linear space. Inf. Process. Lett., 6:80–82, 1977. (PDF p. 12)
16. R. A. Wagner and M. J. Fischer. The string-to-string correction problem. J. ACM, 21(1):168–173, 1974. (PDF p. 12)
17. R. Williams. Matrix-vector multiplication in sub-quadratic time (some preprocess- ing required). In SODA, pages 1–11. ACM Press, 2007. (PDF p. 12)
