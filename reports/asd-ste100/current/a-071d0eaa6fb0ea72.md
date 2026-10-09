# New Processor Array Architectures for the Longest Common Subsequence Problem

- Work ID: `w-071d0eaa6fb0`
- Asset ID: `a-071d0eaa6fb0ea72`
- Source PDF: `literature/academic-papers-processed/New Processor Array Architectures for the Longest Common Subsequence Problem - Michailidis, Margaritis.pdf`
- SHA-256: `071d0eaa6fb0ea7286041b966faaef0d147e61717ce342cd7dba5bde65e458ed`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors propose linear and block processor arrays for a bit-level dynamic programming algorithm for longest common subsequences. (PDF p. 1).
- The arrays support preprocessing and subsequence computation on the same architecture. (PDF p. 1).
- The study develops performance models for a single processor and a linear processor array. (PDF p. 18).

## Objectives

- The study aims to reduce communication and execution time through a block processor array. (PDF p. 1).
- It aims to estimate processor-array performance on Pentium processors. (PDF p. 1).

## Arguments

- The authors argue that simple bit-level operations and fewer registers and communication channels make the arrays suitable for VLSI and multicomputer implementations. (PDF p. 18).

## Analysis

- The execution-time model adds preprocessing, computation, and communication costs. Communication includes startup time and transmission time per word. (PDF p. 15).
- The authors state that the first array uses m cells and n + m − 1 time steps. The block array uses b cells and n + b − 1 time steps. (PDF p. 18).
- Interpretation: the eight-processor LCS estimate is about 40% above the measured time. This weakens the authors' description of close agreement for that case. (PDF p. 17).

## Methods

- Preprocessing encodes string x in an m × |Σ| bit map. Each bit records whether a string position matches an alphabet symbol. The algorithm also constructs the negated map. (PDF p. 3).
- The first architecture implements dynamic programming matrices c and LCS with bit-parallel operations. The second processes the bit-level algorithm in blocks. (PDF p. 18).
- The cluster implementation broadcasts x and constructs local bit maps. Characters of y then enter the array, and each processor handles a block of w characters. (PDF p. 17).
- The implementation uses MPI_Bcast for broadcast and MPI_Recv and MPI_Send for communication between processors. (PDF p. 17).

## Applications

- The paper identifies data compression, word processing, syntactic pattern recognition, and molecular biology as applications of LCS and LCS-length computation. (PDF p. 1).
- The authors intend the validated model to predict execution time on programmable processors with fast communication, including DSP and transputer systems. (PDF p. 18).

## Optimization

- Block processing reduces the required cell count from m to b and the stated time-step count from n + m − 1 to n + b − 1. (PDF p. 18).
- The authors state that each cell needs only three registers and communication channels per step. They report fewer resources than the compared earlier designs. (PDF p. 18).

## Evaluation and testing

- Single-processor validation uses a Pentium 4 at 1.5 GHz. Measured sequential phase times determine the model's operation-time parameters. (PDF p. 15).
- Array experiments use eight Pentium 200 MHz processors, switched 100 Mb/s Fast Ethernet, and MPI version 1.2. (PDF p. 17).
- A ping-pong test measures communication parameters over different message sizes with 100 iterations. (PDF p. 17).
- The reported cluster LCS tests use a string of 300,000 characters, with m = 64 on two processors and m = 256 on eight processors. (PDF p. 17).

## Results

- The authors report a maximum difference below 3% between estimated and measured single-processor values. (PDF p. 17).
- For two processors, measured LCS time was 1376.261 seconds, compared with an estimate of 1396.819 seconds. (PDF p. 17).
- For eight processors, measured LCS time was 996.123 seconds, compared with an estimate of 1396.847 seconds. (PDF p. 17).

## Limitations and uncertainty

- Fast Ethernet communication dominated execution time. The authors did not extend cluster experiments to larger strings or more processors. (PDF p. 18).
- The authors describe cluster tests as validation for performance prediction on faster networks. The supplied results do not establish performance on those target systems. (PDF p. 18).

## References

1. A. V. Aho, D. S. Hirschberg, and J. D. Ullman. Bounds on the complexity of the longest common subsequence problem. Journal of Association Computing Machineny, 23:1–12, 1976. (PDF p. 18)
2. A. Apostolico, M. Attalah, L. Larmore, and S. Mcfaddin. Efficient parallel algorithms for string editing and related problems. SIAM Journal on Computing, 19:968–988, 1990. NEW PROCESSOR ARRAY ARCHITECTURES 69 (PDF p. 18)
3. L. Bergroth, H. Hakonen, and T. Raita. A survey of longest common subsequence algorithms. In 7th Interna- tional Symposium on String Processing and Information Retrieval, pp. 39–48, 2000. (PDF p. 19)
4. M. Crochemore, C. S. Iliopoulos, Y. J. Pinzon, and J. R. Reid. A fast and practical bit-vector algorithm for the longest common subsequence problem. In 11th Australasian Workshop on Combinatorial Algorithms, pp. 75–86, 2000. (PDF p. 19)
5. M. Crochemore, C. S. Iliopoulos, Y. J. Pinzon, and J. R. Reid. A fast and practical bit-vector algorithm for the longest common subsequence problem. Information Processing Letters, 80:279–285, 2001. (PDF p. 19)
6. D. Gusfield. Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology. Cambridge University Press, Gambridge, England, 1997. (PDF p. 19)
7. D. S. Hirschberg. A linear space algorithm for computing maximal common subsequences. Communications of the ACM, 18:341–343, 1975. (PDF p. 19)
8. D. S. Hirschberg. An information theoretic lower bound for the longest common subsequence problem. Information Processing Letters, 7:40–41, 1978. (PDF p. 19)
9. R. Hughey. Parallel hardware for sequence comparison and alignment. CABIOS, 12:473–479, 1996. (PDF p. 19)
10. S. Y. Kung. VLSI Array Processors. Prentice-Hall, 1988. (PDF p. 19)
11. T. Lecroq, G. Luce, and J. F. Myoupo. A faster linear systolic algorithm for recovering a longest common subsequence. Information Processing Letters, 61:129–136, 1997. (PDF p. 19)
12. T. Lecroq, J. F. Myoupo, and D. Seme. A one-phase parallel algorithm for the sequence alignment problem. Parallel Processing Letters, 8:515–526, 1998. (PDF p. 19)
13. Y.-C. Lin. New systolic arrays for the longest common subsequence problem. Parallel Computing, 20:1323– 1334, 1994. (PDF p. 19)
14. Y.-C. Lin and J.-C. Chen. An efficient systolic algorithm for the longest common subsequence problem. The Journal of Supercomputing, 12:373–385, 1998. (PDF p. 19)
15. Y.-C. Lin and J.-C. Chen. Another efficient systolic algorithm for the longest common subsequence problem. Journal of the Chinese Institute of Engineers, 23:607–613, 2000. (PDF p. 19)
16. Y.-C. Lin and J.-W. Yeh. A scalable and efficient systolic algorithm for the longest common subsequence problem. Journal of Information Science and Engineering, 18:519–532, 2002. (PDF p. 19)
17. Y.-C. Lin and J.-W. Yeh. Deriving a systolic algorithm for the LCS problem. International Conference on Parallel and Distributed Processing Techniques and Applications, pp. 1890–1897, 1998. (PDF p. 19)
18. Y.-C. Lin and J.-W. Yeh. Deriving a fast systolic algorithm for the longest common subsequence problem. Parallel Algorithms and Applications, 17:1–18, 2002. (PDF p. 19)
19. G. Luce and J. F. Myoupo. Systolic-based parallel architecture for the longest common subsequences problem. Integration, the VLSI Journal, 25:53–70, 1998. (PDF p. 19)
20. M. Lu and H. Lin. Parallel algorithms for the longest common subsequence problem. IEEE Transactions on Parallel and Distributed Systems, 5:835–848, 1994. (PDF p. 19)
21. K. G. Margaritis and D. J. Evans. A VLSI processor array for flexible string matching. Parallel Algorithms and Applications, 11:45–60, 1997. (PDF p. 19)
22. W. J. Masek and M. S. Paterson. A faster algorithm computing string edit distances. Journal of Computer System Sciences, 20:18–31, 1980. (PDF p. 19)
23. J. H. Moreno and T. Lang. Matrix Computations on Systolic-Type Arrays. Kluwer Academic Publishers, 1992. (PDF p. 19)
24. N. Petkov. Systolic Parallel Processing. Elsevier Science Publishers, 1993. (PDF p. 19)
25. N. Ranganathan and R. Sastry. VLSI architectures for pattern matching. International Journal of Pattern Recognition and Artificial Intelligence, 8:815–843, 1994. (PDF p. 19)
26. Y. Robert and M. Tchuente. A systolic array for the longest common subsequence problem. Information Processing Letters, 21:191–198, 1985. (PDF p. 19)
27. D. Sankoff and J.B. Kruskal. Time Warps, String Edits and Macromolecules: The Theory and Practice of Sequence Comparison. Addison-Wesley, 1983. (PDF p. 19)
28. J. Setubal and J. Meidanis. Introduction to Computational Molecular Biology. PWS, Boston, MA, 1997. (PDF p. 19)
29. M. Snir, S. Otto, S. Huss-Lederman, D. W. Walker and J. Dongarra. MPI: The Complete Reference. The MIT Press, Cambridge, Massachusetts, 1996. (PDF p. 19)
30. C.-B. Yang and R. C. T. Lee. Systolic algorithms for the longest common subsequence problem. Journal of the Chinese Institute of Engineers, 10:691–699, 1987. (PDF p. 19)
