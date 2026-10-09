# Fast string matching with k differences

- Work ID: `w-00b0fc12dd2b`
- Asset ID: `a-00b0fc12dd2bfb6a`
- Source PDF: `literature/academic-papers-processed/Fast string matching with k differences.pdf`
- SHA-256: `00b0fc12dd2bfb6a221c65bfc51bf9fa4df75c4a16819fae9d3989494e0f41bb`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Landau and Vishkin find all pattern occurrences in a text with at most k mismatches, insertions, or deletions. (PDF p. 1).
- Their improved version uses O(m + nk²) time for a fixed alphabet and O(m log m + nk²) time for general input. It requires O(m) space. (PDF p. 1).

## Objectives

- Find all approximate occurrences of a pattern of length m in a text of length n under a bound of k differences. (PDF p. 1).

## Arguments

- The authors separate pattern preprocessing from text analysis. Both versions use O(nk²) text-analysis time. (PDF p. 3).
- The simpler quadratic preprocessing version can be useful when preprocessing occurs in advance or one pattern is searched across many texts. (PDF p. 3).

## Analysis

- CHECK-3 correctness is established by induction over text starting positions. Each iteration receives the information needed to test the next occurrence. (PDF p. 12).
- The CHECK-3 time analysis charges operations to discovered differences or examined triples. O(k) work on each of O(k) diagonals gives O(k²) time per iteration. (PDF p. 12).
- The authors state that their algorithms are asymptotically faster than O(mn) dynamic programming only when k² = o(m). (PDF p. 3).

## Methods

- CHECK-1 computes an edit-distance matrix for each candidate start. It reports an occurrence when the complete pattern matches an allowed text length with at most k differences. (PDF p. 5).
- CHECK-2 increases the allowed difference count and maintains the furthest pattern row reached on each diagonal. It extends each state through exact character matches. (PDF p. 7).
- The first preprocessing method stores longest common-prefix lengths for pairs of pattern suffixes in MAX-LENGTH. A diagonal recurrence fills this table in O(m²) time. (PDF p. 13).
- The second version builds a suffix tree. CHECK-4 answers MAX-LENGTH queries from the string depth of the lowest common ancestor of two suffix leaves. (PDF p. 15).

## Applications

- The authors motivate approximate matching by unreliable data with bounded replacement, omission, or insertion errors. (PDF p. 2).
- The paper identifies molecular biology as an application area through cited work. (PDF p. 3).

## Optimization

- CHECK-3 reuses a sequence of at most 2k + 2 triples and MAX-LENGTH information to reduce repeated character comparisons. (PDF p. 12).
- Replacing the quadratic table with a suffix tree reduces preprocessing space to O(m). Preprocessing takes O(m) time for a fixed alphabet or O(m log x) for x distinct pattern letters. (PDF p. 14).
- Linear-time and linear-space lowest-common-ancestor preprocessing permits each subsequent query to take O(1) time. (PDF p. 15).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- The simpler version has O(m² + nk²) time and O(m²) space bounds. (PDF p. 3).
- For CHECK-4, constant-time suffix queries preserve O(nk²) text-analysis time. The authors give O(m + k) = O(m) text-analysis space. (PDF p. 15).

## Limitations and uncertainty

- The fixed-alphabet assumption is required for linear-time pattern preprocessing. General alphabets add a logarithmic factor. (PDF p. 14).
- The excerpts give different auxiliary-space statements: CHECK-3 uses O(k²) storage on page 12, while page 15 states O(k) beyond MAX-LENGTH. The relationship between these statements is uncertain. (PDF p. 15).

## References

1. [AHU-741 A. V. AHO, J. E. HOPCROFT,AND J. D. ULLMAN, “The Design and Analysis of Computer Algorithms,” Addison-Wesley, Reading, MA, 1974. [BM-771 R. S. BOYERAND J. S. MOORE,A fast string searching algorithm, Comm. ACM 20 (1977), 762-772. (PDF p. 15)
2. M. T. CHEN AND J. SEIFERAS,EfIicient and elegant subword tree construction, in “Combinatorial Algorithms on Words,” (A. Apostolico and Z. Galil, Eds.), NATO ASI, Series, Series F: Computer and System Sciences, Vol. 12, pp. 97-107, Springer-Verlag, Berlin/New York, 1985. (PDF p. 15)
3. Z. GALIL, Optimal parallel algorithms for string matching, in “Proc. 16th ACM Symposium on Theory of Computing 1984,” pp. 24&248; also, Inform. and Conlrol67 (1985), 144-157. (PDF p. 15)
4. Z. GALIL, Open problems in stringology, in “Combinatorial Algorithms on Words” (A. Apostolico and Z. Galil, Eds.), NATO (ASI) Series, Series F: Computer and System Sciences, Vol. 12, pp. 1-8, Springer-Verlag, Berlin/New York, 1985. (PDF p. 15)
5. LANDAU AND VISHKIN [GS-831 Z. GALIL AND J. 1. SEIFERAS, Time-space-optimal string matching, J. Cornput. Srsrrnr Sci. 26 (1983), 28s-294. [HT-841 D. HAREL AND R. E. TARJAN, Fast algorithms for finding nearest common ancestors, SIAM J. Compur. 13, No. 2 (1984), 338-355. II-851 A. G. IVANOV. Recognition of an approximate occurrence of words on a Turing machine in real time, Math. USSR-1x1. 24, No. 3 (1985), 479-522. [KMP-771 D. E. KNUTH, .I. H. MORRIS, AND V. R. PRATT, Fast pattern matching in strings, SIAM J. Compur. 6 (1977), 323-350. [KR-871 R. M. KARP AND M. 0. RABIN, Efficient randomized pattern-matching algorithms, IBM J. Res. Develop. 31, No. 2 (March 1987), 249-260. [LV-851 G. M. LANDAU AND U. VISHKIN, Efficient string matching in the presence of errors, in “Proc. 26th IEEE FOCS, 1985,” pp. 126136. (PDF p. 16)
6. G. M. LANDAU AND U. VISHKIN, Introducing eflicient parallelism into approximate string matching, in “Proc. 18th ACM Symposium on Theory of Computing, 1986”, pp. 22G-230. (PDF p. 16)
7. G. M. LANDAU AND U. VISHKIN, Efficient string matching with k mismatches, Theoref. Comput. Sci. 43 (1986), 239-249. [LVN-861 G. M. LANDAU, U. VISHKIN, AND R. NUSSINOV, An efIicient string matching algorithm with k differences for nucleotide and amino acid sequences, Nucleic Acid Res. 14, No. 1 (1986), 3146. [SK-831 D. SANKOFF AND J. B. KRUSKAL (Eds.), “Time Warps, String Edits, and Macromolecules: The Theory and Practice of Sequence Comparison, Addison-Wesley, Reading, MA, 1983. ,[SV-881 B. SCH~EBER AND U. VISHKIN, Parallel computation of lowest common ancestor in trees, SIAM J. Comput. to appear. (PDF p. 16)
8. E. UKKONEN, On approximate string matching, in “Proc. Int. Conf. Found. Comp. Theor.,” Lecture Notes in Computer Science 158, pp. 487495, Springer-Verlag, Berlin/New York, 1983. (PDF p. 16)
9. E. UKKONEN, Finding approximate pattern in strings, J. Algorithms 6 (1985), 132-137. (PDF p. 16)
10. U. VISHKIN, Optimal parallel pattern matching in strings, in “Proc. 12th ICALP,” Lecture Notes in Computer Science 194, pp. 497-508, Springer-Verlag, Berlin/New York, 1985; also, Inform. and Control 67 (1985), 91-113. (PDF p. 16)
11. P. WEINER, Linear pattern matching algorithm, in “Proc. 14th IEEE Symposium on Switching and Automata Theory, 1973,” pp. l-l 1. (PDF p. 16)
