# Bounded Weighted Edit Distance

- Work ID: `w-defc75310e7c`
- Asset ID: `a-defc75310e7c6abe`
- Source PDF: `literature/academic-papers-processed/Bounded Weighted Edit Distance.pdf`
- SHA-256: `defc75310e7c6abe3d3bc4c9e937b70cfb282f5435c416770a74291c4daf066c`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors give a dynamic algorithm for bounded weighted edit distance with arbitrary normalized edit costs. A fixed threshold k controls preprocessing and update costs. (PDF p. 1).
- The algorithm uses Õ(nk^γ) preprocessing and Õ(k^(3−γ)) time per update, for γ in [0,1]. It returns infinity when the distance exceeds k. (PDF p. 1).
- Conditional lower bounds establish fine-grained optimality of the trade-off for γ in [0.5,1). (PDF p. 1).

## Objectives

- Determine how quickly weighted edit distance can be maintained when strings change and the distance is small. (PDF p. 3).
- Support substring deletion and copy-paste updates while answering distance queries for strings specified through edits to the maintained string. (PDF p. 5).

## Arguments

- Large weights can make one character update change the weighted distance substantially. The authors use this fact to explain why an existing method for small integer weights does not extend to arbitrary weights. (PDF p. 3).
- A conditional dynamic lower bound supports fixing k during preprocessing. Bounds based on the current distance alone cannot provide the same improvements in the stated regime. (PDF p. 14).

## Analysis

- Weights depend on edit type and characters, not position. Equal characters have cost zero, and each nontrivial edit has cost at least one. (PDF p. 2).
- Assuming APSP, for κ in [0.5,1] and δ > 0, no O(n^(0.5+1.5κ−δ)) algorithm decides whether weighted distance is at most k ≤ n^κ, even when unweighted distance is at most four. (PDF p. 3).
- The notation Õ hides factors that are polylogarithmic in n. (PDF p. 1).

## Methods

- The algorithm maintains a data structure for aligning X with itself. A query supplies edits that transform X into Y, instead of requiring Y to be stored in this structure. (PDF p. 5).
- For the original two-string problem, a dynamic unweighted edit-distance algorithm can supply the required edits in Õ(k²) time per update. (PDF p. 5).
- The general trade-off combines earlier techniques with a shifted variant of self-edit distance. (PDF p. 5).
- The static lower-bound reduction constructs strings that become equal after removing two special symbols from each. Expensive edits to these symbols force alignments whose costs encode a batched weighted-distance instance. (PDF p. 13).

## Applications

- The authors connect the query algorithm to approximate pattern matching under weighted edit distance. They state that their trade-off gives a faster method when the pattern is far from periodic. (PDF p. 5).

## Optimization

- The parameter γ trades greater preprocessing cost for lower update or query cost. It ranges from zero to one. (PDF p. 1).
- Self-alignment preprocessing supports reuse across different query strings Y specified through edits to X. (PDF p. 5).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- The extended data structure supports character edits, substring deletions, and copy-pastes in Õ(k²) time after Õ(nk^γ) preprocessing. (PDF p. 5).
- Given u edits from X to Y, it computes the weighted distance up to threshold k in Õ(u + k^(3−γ)) time. The theorem assumes O(1)-time access to the weight oracle. (PDF p. 5).
- The dynamic lower-bound proof applies and reverses a constant number of edits for each embedded hard instance. It uses self-reducibility of Negative Triangle to constrain the preprocessing/update trade-off. (PDF p. 14).

## Limitations and uncertainty

- The threshold k must be fixed during preprocessing. Distances above k are reported as infinity rather than computed exactly. (PDF p. 1).
- Fine-grained optimality is not established for γ below 0.5. This gap follows from an unresolved range in the static weighted-distance problem. (PDF p. 5).
- Optimal update time at γ=1 remains open. The benefit of γ>1 is also unresolved. (PDF p. 5).
- The authors leave small fractional weights and update bounds based on the change in distance as open directions. (PDF p. 5).

## References

1. Amir Abboud, Arturs Backurs, and Virginia Vassilevska Williams. Tight hardness results for LCS and other sequence similarity measures. In FOCS 2015, pages 59–78. IEEE Computer Society, 2015. doi:10.1109/FOCS.2015.14. (PDF p. 14)
2. Amir Abboud, Thomas Dueholm Hansen, Virginia Vassilevska Williams, and Ryan Williams. Simulating branching programs with edit distance and friends: or: a polylog shaved is a lower bound made. In STOC 2016, pages 375–388. ACM, 2016. doi:10.1145/2897518.2897653. (PDF p. 14)
3. Alok Aggarwal, Maria M. Klawe, Shlomo Moran, Peter W. Shor, and Robert E. Wilber. Geometric applications of a matrix-searching algorithm. Algorithmica, 2:195–208, 1987. doi:10.1007/BF01840359. (PDF p. 14)
4. Stephen Alstrup, Gerth Stølting Brodal, and Theis Rauhe. Pattern matching in dynamic texts. In SODA 2000, pages 819–828. ACM/SIAM, 2000. URL: http://dl.acm.org/citation.cfm? id=338219.338645. (PDF p. 14)
5. Arturs Backurs and Piotr Indyk. Edit distance cannot be computed in strongly subquadratic time (unless SETH is false). SIAM J. Comput., 47(3):1087–1097, 2018. doi:10.1137/ 15M1053128. I. Boneh, E. Gorbachev, and T. Kociumaka 45:15 (PDF p. 14)
6. Itai Boneh, Egor Gorbachev, and Tomasz Kociumaka. Bounded weighted edit distance: Dynamic algorithms and matching lower bounds, 2025. arXiv:2507.02548v1. (PDF p. 15)
7. Karl Bringmann and Marvin Künnemann. Quadratic conditional lower bounds for string problems and dynamic time warping. In FOCS 2015, pages 79–97. IEEE Computer Society, 2015. doi:10.1109/FOCS.2015.15. (PDF p. 15)
8. Alejandro Cassis, Tomasz Kociumaka, and Philip Wellnitz. Optimal algorithms for bounded weighted edit distance. In FOCS 2023, pages 2177–2187. IEEE, 2023. doi:10.1109/FOCS57990. 2023.00135. (PDF p. 15)
9. Panagiotis Charalampopoulos, Tomasz Kociumaka, and Shay Mozes. Dynamic string alignment. In CPM 2020, volume 161 of LIPIcs, pages 9:1–9:13. Schloss Dagstuhl – Leibniz-Zentrum für Informatik, 2020. doi:10.4230/LIPIcs.CPM.2020.9. (PDF p. 15)
10. Panagiotis Charalampopoulos, Tomasz Kociumaka, and Philip Wellnitz. Faster approximate pattern matching: A unified approach. In FOCS 2020, pages 978–989. IEEE, 2020. doi: 10.1109/FOCS46700.2020.00095. (PDF p. 15)
11. Panagiotis Charalampopoulos, Tomasz Kociumaka, and Philip Wellnitz. Pattern matching under weighted edit distance. In FOCS 2025, 2025. (PDF p. 15)
12. Debarati Das, Jacob Gilbert, MohammadTaghi Hajiaghayi, Tomasz Kociumaka, and Barna Saha. Weighted edit distance computation: Strings, trees, and Dyck. In STOC 2023, STOC 2023, pages 377–390, New York, NY, USA, 2023. Association for Computing Machinery. doi:10.1145/3564246.3585178. (PDF p. 15)
13. Jittat Fakcharoenphol and Satish Rao. Planar graphs, negative weight edges, shortest paths, and near linear time. J. Comput. Syst. Sci., 72(5):868–889, 2006. doi:10.1016/j.jcss.2005. 05.007. (PDF p. 15)
14. Paweł Gawrychowski, Adam Karczmarz, Tomasz Kociumaka, Jakub Łącki, and Piotr Sankowski. Optimal dynamic strings. In SODA 2018, pages 1509–1528. SIAM, 2018. doi:10.1137/1.9781611975031.99. (PDF p. 15)
15. Egor Gorbachev and Tomasz Kociumaka. Bounded edit distance: Optimal static and dynamic algorithms for small integer weights. In 57th Annual ACM Symposium on Theory of Comput- ing, STOC 2025, pages 2157–2166, New York, NY, USA, 2025. Association for Computing Machinery. doi:10.1145/3717823.3718168. (PDF p. 15)
16. Russell Impagliazzo and Ramamohan Paturi. On the complexity of k-SAT. J. Comput. Syst. Sci., 62(2):367–375, 2001. doi:10.1006/jcss.2000.1727. (PDF p. 15)
17. Russell Impagliazzo, Ramamohan Paturi, and Francis Zane. Which problems have strongly exponential complexity? J. Comput. Syst. Sci., 63(4):512–530, 2001. doi:10.1006/jcss.2001. 1774. (PDF p. 15)
18. Dominik Kempa and Tomasz Kociumaka. Dynamic suffix array with polylogarithmic queries and updates. In STOC 2022, pages 1657–1670. ACM, 2022. doi:10.1145/3519935.3520061. (PDF p. 15)
19. Philip N. Klein. Multiple-source shortest paths in planar graphs. In SODA, pages 146–155. SIAM, 2005. URL: http://dl.acm.org/citation.cfm?id=1070432.1070454. (PDF p. 15)
20. Tomasz Kociumaka, Anish Mukherjee, and Barna Saha. Approximating edit distance in the fully dynamic model. In FOCS 2023, pages 1628–1638. IEEE, 2023. doi:10.1109/FOCS57990. 2023.00098. (PDF p. 15)
21. Gad M. Landau and Uzi Vishkin. Fast string matching with k differences. J. Comput. System Sci., 37(1):63–78, 1988. doi:10.1016/0022-0000(88)90045-1. (PDF p. 15)
22. Vladimir I. Levenshtein. Binary codes capable of correcting deletions, insertions and reversals. Dokl. Akad. Nauk SSSR, 163:845–848, 1965. URL: http://mi.mathnet.ru/eng/dan31411. (PDF p. 15)
23. Kurt Mehlhorn, Rajamani Sundar, and Christian Uhrig. Maintaining dynamic sequences under equality tests in polylogarithmic time. Algorithmica, 17:183–198, 1997. doi:10.1007/ bf02522825. (PDF p. 15)
24. Eugene W. Myers. An O(ND) difference algorithm and its variations. Algorithmica, 1(2):251– 266, 1986. doi:10.1007/BF01840446. ESA 2025 45:16 Bounded Weighted Edit Distance: Dynamic Algorithms and Matching Lower Bounds (PDF p. 15)
25. Saul B. Needleman and Christian D. Wunsch. A general method applicable to the search for similarities in the amino acid sequence of two proteins. J. Mol. Biol., 48(3):443–453, 1970. doi:10.1016/b978-0-12-131200-8.50031-9. (PDF p. 16)
26. Peter H. Sellers. On the theory and computation of evolutionary distances. SIAM J. Appl. Math., 26(4):787–793, 1974. doi:10.1137/0126070. (PDF p. 16)
27. Peter H. Sellers. The theory and computation of evolutionary distances: Pattern recognition. J. Algorithms, 1(4):359–373, 1980. doi:10.1016/0196-6774(80)90016-4. (PDF p. 16)
28. Alexander Tiskin. Semi-local string comparison: Algorithmic techniques and applications. Math. Comput. Sci., 1(4):571–603, 2008. doi:10.1007/s11786-007-0033-3. (PDF p. 16)
29. Alexander Tiskin. Fast distance multiplication of unit-Monge matrices. Algorithmica, 71(4):859– 888, 2015. doi:10.1007/S00453-013-9830-Z. (PDF p. 16)
30. Esko Ukkonen. Finding approximate patterns in strings. J. Algorithms, 6(1):132–137, 1985. doi:10.1016/0196-6774(85)90023-9. (PDF p. 16)
31. Virginia Vassilevska Williams and R. Ryan Williams. Subcubic equivalences between path, matrix, and triangle problems. Journal of the ACM, 65(5):27:1–27:38, 2018. doi:10.1145/ 3186893. (PDF p. 16)
32. Taras K. Vintsyuk. Speech discrimination by dynamic programming. Cybernetics, 4(1):52–57, 1968. doi:10.1007/BF01074755. (PDF p. 16)
33. Robert A. Wagner and Michael J. Fischer. The string-to-string correction problem. J. ACM, 21(1):168–173, 1974. doi:10.1145/321796.321811. (PDF p. 16)
