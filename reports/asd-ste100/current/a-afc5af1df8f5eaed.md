# Sparse Dynamic Programming on DAGs with Small Width

- Work ID: `w-afc5af1df8f5`
- Asset ID: `a-afc5af1df8f5eaed`
- Source PDF: `literature/academic-papers-processed/Sparse Dynamic Programming on DAGs with Small Width - Mäkinen et al.pdf`
- SHA-256: `afc5af1df8f5eaede3e29480fcdc42e7266ba82b62c8ad06e98005e5ebd0b83c`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors formulate sparse dynamic programming and co-linear chaining on directed acyclic graphs parameterized by path width. (PDF p. 1).
- The algorithm runs in O(k |V| + N log N) time on DAGs decomposed into k minimum path covers. (PDF p. 3).

## Objectives

- Align sequences and co-linear fragment chains to pangenome DAGs efficiently when path width k is small. (PDF p. 2).

## Arguments

- Pangenome variation graphs typically exhibit small path width, allowing efficient parameterized chaining. (PDF p. 2).

## Analysis

- Complexity is analyzed in terms of the minimum path cover k of the graph using Dilworth theorem. (PDF p. 3).

## Methods

- The graph is decomposed into a minimum chain cover of size k using network flow or bipartite matching. (PDF p. 3).
- Balanced search trees maintain prefix maxima along each path chain during topological traversal. (PDF p. 18).

## Applications

- Sequence-to-DAG alignment and co-linear seed chaining in pangenomic variation graphs. (PDF p. 2).

## Optimization

- Path-decomposed range search structures replace quadratic all-pairs reachability checks. (PDF p. 18).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- Achieves near-linear chaining time on pangenome DAGs with small width k. (PDF p. 3).

## Limitations and uncertainty

- Runtime scales linearly with path width k and degrades on dense, highly tangled graph regions. (PDF p. 3).

## References

1. Mohamed Ibrahim Abouelhoda. 2007. A chaining algorithm for mapping cDNA sequences to multiple genomic se- quences. In Proceedings of the 14th International Symposium on String Processing and Information Retrieval (LNCS), Vol. 4726. Springer, 1–13. (PDF p. 19)
2. Ravindra K. Ahuja, Thomas L. Magnanti, and James B. Orlin. 1993. Network Flows: Theory, Algorithms, and Applica- tions. Prentice-Hall, Inc., Upper Saddle River, NJ. (PDF p. 19)
3. Amihood Amir, Moshe Lewenstein, and Noa Lewenstein. 2000. Pattern matching in hypertext. J. Algor. 35, 1 (2000), 82–99. (PDF p. 19)
4. Arturs Backurs and Piotr Indyk. 2015. Edit distance cannot be computed in strongly subquadratic time (unless SETH is false). In Proceedings of the 47th Annual ACM on Symposium on Theory of Computing (STOC’15). ACM, 51–58. (PDF p. 19)
5. Djamal Belazzougui. 2014. Linear time construction of compressed text indices in compact space. In Proceedings of the Symposium on Theory of Computing (STOC’14). ACM, 148–193. http://doi.acm.org/10.1145/2591796.2591885. (PDF p. 19)
6. Djamal Belazzougui, Fabio Cunial, Juha Kärkkäinen, and Veli Mäkinen. 2013. Versatile succinct representations of the bidirectional Burrows-Wheeler transform. In Proceedings of the 21st Annual European Symposium on Algorithms (ESA’13) (LNCS), Vol. 8125. Springer, 133–144. DOI:http://dx.doi.org/10.1007/978-3-642-40450-4_12 (PDF p. 19)
7. Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars. 2008. Computational Geometry: Algorithms and Applications (3rd ed.). Springer-Verlag TELOS, Santa Clara, CA. (PDF p. 19)
8. Y. Chen and Y. Chen. 2008. An efficient algorithm for answering graph reachability queries. In Proceedings of the IEEE 24th International Conference on Data Engineering. IEEE, 893–902. (PDF p. 19)
9. Y. Chen and Y. Chen. 2014. On the graph decomposition. In Proceedings of the IEEE Fourth International Conference on Big Data and Cloud Computing. IEEE, 777–784. (PDF p. 19)
10. Deanna M. Church, Valerie A. Schneider, Karyn Meltz Steinberg, Michael C. Schatz, Aaron R. Quinlan, Chen-Shan Chin, Paul A. Kitts, Bronwen Aken, Gabor T. Marth, Michael M. Hoffman, et al. 2015. Extending reference assembly models. Genome Biol. 16, 1 (2015), 13. (PDF p. 19)
11. Edith Cohen, Eran Halperin, Haim Kaplan, and Uri Zwick. 2003. Reachability and distance queries via 2-hop labels. SIAM J. Comput. 32, 5 (2003), 1338–1355. DOI:http://dx.doi.org/10.1137/S0097539702403098 (PDF p. 19)
12. Maxime Crochemore and Ely Porat. 2010. Fast computation of a longest increasing subsequence and application. Info. Comput. 208, 9 (2010), 1054–1059. (PDF p. 19)
13. David Eppstein, Zvi Galil, Raffaele Giancarlo, and Giuseppe F. Italiano. 1992. Sparse dynamic programming I: Linear cost functions. J. ACM 39, 3 (July 1992), 519–545. http://doi.acm.org/10.1145/146637.146650. (PDF p. 19)
14. David Eppstein, Zvi Galil, Raffaele Giancarlo, and Giuseppe F. Italiano. 1992. Sparse dynamic programming II: Convex and concave cost functions. J. ACM 39, 3 (1992), 546–567. (PDF p. 19)
15. Stefan Felsner, Vijay Raghavan, and Jeremy Spinrad. 2003. Recognition algorithms for orders of small width and graphs of small Dilworth number. Order 20, 4 (Nov. 2003), 351–364. DOI:https://doi.org/10.1023/B:ORDE.0000034609. 99940.fb (PDF p. 19)
16. Paolo Ferragina and Giovanni Manzini. 2005. Indexing compressed text. J. ACM 52, 4 (July 2005), 552–581. http:// doi.acm.org/10.1145/1082036.1082039. (PDF p. 19)
17. Michael L. Fredman. 1975. On computing the length of longest increasing subsequences. Discrete Math. 11, 1 (1975), 29–35. (PDF p. 19)
18. D. R. Fulkerson. 1956. Note on Dilworth’s decomposition theorem for partially ordered sets. Proc. Amer. Math. Soc. 7, 4 (1956), 701–702. ACM Transactions on Algorithms, Vol. 15, No. 2, Article 29. Publication date: February 2019. 29:20 V. Mäkinen et al. (PDF p. 19)
19. Harold N. Gabow, Jon Louis Bentley, and Robert E. Tarjan. 1984. Scaling and related techniques for geometry prob- lems. In Proceedings of the 16th Annual ACM Symposium on Theory of Computing (STOC’84). ACM, New York, NY, 135–143. http://doi.acm.org/10.1145/800057.808675. (PDF p. 20)
20. Erik Garrison, Jouni Sirén, Adam M. Novak, Glenn Hickey, Jordan M. Eizenga, Eric T. Dawson, William Jones, Shilpa Garg, Charles Markello, Michael F. Lin, Benedict Paten, and Richard Durbin. 2018. Variation graph toolkit improves read mapping by representing genetic variation in the reference. Nature Biotechnol. 36 (Aug. 2018), 875. (PDF p. 20)
21. Steffen Heber, Max Alekseyev, Sing-Hoi Sze, Haixu Tang, and Pavel A. Pevzner. 2002. Splicing graphs and EST as- sembly problem. Bioinformatics 18, Suppl. 1 (2002), S181–S188. (PDF p. 20)
22. Wing-Kai Hon, Kunihiko Sadakane, and Wing-Kin Sung. 2009. Breaking a time-and-space barrier in constructing full-text indices. SIAM J. Comput. 38, 6 (2009), 2162–2178. DOI:http://dx.doi.org/10.1137/070685373 (PDF p. 20)
23. John E. Hopcroft and Richard M. Karp. 1973. An n5/2 algorithm for maximum matchings in bipartite graphs. SIAM J. Comput. 2, 4 (1973), 225–231. (PDF p. 20)
24. H. V. Jagadish. 1990. A compression technique to materialize transitive closure. ACM Trans. Database Syst. 15, 4 (Dec. 1990), 558–598. http://doi.acm.org/10.1145/99935.99944. (PDF p. 20)
25. Ruoming Jin, Ning Ruan, Yang Xiang, and Haixun Wang. 2011. Path-tree: An efficient reachability indexing scheme for large directed graphs. ACM Trans. Database Syst. 36, 1 (Mar. 2011), 7:1–7:44. http://doi.acm.org/10.1145/1929934. 1929941. (PDF p. 20)
26. Anna Kuosmanen, Topi Paavilainen, Travis Gagie, Rayan Chikhi, Alexandru I. Tomescu, and Veli Mäkinen. 2018. Using minimum path cover to boost dynamic programming on DAGs: Co-linear chaining extended. In Proceedings of the 22nd Annual International Conference on Research in Computational Molecular Biology (RECOMB’18) (Lecture Notes in Computer Science), Vol. 10812. Springer, 105–121. (PDF p. 20)
27. Antoine Limasset, Bastien Cazaux, Eric Rivals, and Pierre Peterlongo. 2016. Read mapping on de Bruijn graphs. BMC Bioinform. 17, 1 (2016), 237. (PDF p. 20)
28. Veli Mäkinen, Djamal Belazzougui, Fabio Cunial, and Alexandru I. Tomescu. 2015. Genome-Scale Algorithm Design. Cambridge University Press. (PDF p. 20)
29. Veli Mäkinen, Leena Salmela, and Johannes Ylinen. 2012. Normalized N50 assembly metric using gap-restricted co- linear chaining. BMC Bioinform. 13 (2012), 255. DOI:https://doi.org/10.1186/1471-2105-13-255 (PDF p. 20)
30. U. Manber and S. Wu. 1992. Approximate string matching with arbitrary costs for text and hypertext. In Proceedings of the IAPR Workshop on Structural and Syntactic Pattern Recognition. 22–33. (PDF p. 20)
31. Tobias Marschall et al. 2018. Computational pan-genomics: Status, promises and challenges. Brief. Bioinform. 19, 1 (2018), 118–135. (PDF p. 20)
32. Gene Myers and Webb Miller. 1995. Chaining multiple-alignment fragments in sub-quadratic time. In Proceedings of the 6th Annual ACM-SIAM Symposium on Discrete Algorithms. SIAM, 38–47. http://dl.acm.org/citation.cfm?id=313651. 313661. (PDF p. 20)
33. Gonzalo Navarro. 2000. Improved approximate pattern matching on hypertext. Theor. Comput. Sci. 237, 1–2 (2000), 455–463. (PDF p. 20)
34. Adam M. Novak, Erik Garrison, and Benedict Paten. 2016. A graph extension of the positional Burrows-Wheeler transform and its applications. In Proceedings of the International Workshop on Algorithms in Bioinformatics (LNCS), Vol. 9838. Springer, 246–256. (PDF p. 20)
35. S. C. Ntafos and S. Louis Hakimi. 1979. On path cover problems in digraphs and applications to program testing. IEEE Trans. Softw. Eng. 5, 5 (1979), 520–529. (PDF p. 20)
36. James B. Orlin. 2013. Max flows in O(nm) time, or better. In Proceedings of the 45th Annual ACM Symposium on the Theory of Computing (STOC’13). ACM, New York, NY, 765–774. (PDF p. 20)
37. Kunsoo Park and Dong Kyue Kim. 1995. String matching in hypertext. In Proceedings of the Annual Symposium on Combinatorial Pattern Matching (CPM’95) (LNCS), Vol. 937. Springer, 318–329. (PDF p. 20)
38. Rob Patro, Geet Duggal, Michael I. Love, Rafael A. Irizarry, and Carl Kingsford. 2017. Salmon provides fast and bias- aware quantification of transcript expression. Nature Methods 14, 4 (Apr. 2017), 417–419. DOI:http://dx.doi.org/10. 1038/nmeth.4197 (PDF p. 20)
39. Mikko Rautiainen and Tobias Marschall. 2017. Aligning sequences to general graphs in O(V + mE) time, Mikko Rautiainen and Tobias Marschall (Eds.). bioRxiv 216127. DOI:https://doi.org/10.1101/216127 (PDF p. 20)
40. Romeo Rizzi, Alexandru I. Tomescu, and Veli Mäkinen. 2014. On the complexity of minimum path cover with subpath constraints for multi-assembly. BMC Bioinform. 15, S-9 (2014), S5. (PDF p. 20)
41. Claus-Peter Schnorr. 1978. An algorithm for transitive closure with linear expected time. SIAM J. Comput. 7, 2 (1978), 127–133. (PDF p. 20)
42. Tetsuo Shibuya and Igor Kurochkin. 2003. Match chaining algorithms for cDNA mapping. In Proceedings of the Work- shop on Algorithms in Bioinformatics (WABI’03) (LNCS), Vol. 2812. Springer, 462–475. ACM Transactions on Algorithms, Vol. 15, No. 2, Article 29. Publication date: February 2019. Sparse Dynamic Programming on DAGs with Small Width 29:21 (PDF p. 20)
43. Jouni Sirén. 2017. Indexing variation graphs. In Proceedings of the 19th Workshop on Algorithm Engineering and Ex- periments (ALENEX’17). SIAM, 13–27. (PDF p. 21)
44. Jouni Sirén, Niko Välimäki, and Veli Mäkinen. 2014. Indexing graphs for path queries with applications in genome research. IEEE/ACM Trans. Comput. Biol. Bioinform. 11, 2 (2014), 375–388. (PDF p. 21)
45. J. Su, Q. Zhu, H. Wei, and J. X. Yu. 2017. Reachability querying: Can it be even faster? IEEE Trans. Knowl. Data Eng. 29, 3 (Mar. 2017), 683–697. (PDF p. 21)
46. Alexandru I. Tomescu, Travis Gagie, Alexandru Popa, Romeo Rizzi, Anna Kuosmanen, and Veli Mäkinen. 2015. Ex- plaining a weighted DAG with few paths for solving genome-guided multi-assembly. IEEE/ACM Trans. Comput. Biol. Bioinform. 12, 6 (2015), 1345–1354. (PDF p. 21)
47. Raluca Uricaru, Célia Michotey, Hélène Chiapello, and Eric Rivals. 2015. YOC, A new strategy for pairwise alignment of collinear genomes. BMC Bioinform. 16, 1 (Apr. 2015), 111. DOI:http://dx.doi.org/10.1186/s12859-015-0530-3 (PDF p. 21)
48. Peter van Emde Boas. 1977. Preserving order in a forest in less than logarithmic time and linear space. Info. Process. Lett. 6, 3 (1977), 80–82. (PDF p. 21)
49. Peter van Emde Boas, R. Kaas, and E. Zijlstra. 1977. Design and implementation of an efficient priority queue. Math. Syst. Theory 10 (1977), 99–127. (PDF p. 21)
50. Vijay V. Vazirani. 2001. Approximation Algorithms. Springer-Verlag. (PDF p. 21)
51. Michaël Vyverman, Bernard De Baets, Veerle Fack, and Peter Dawyndt. 2015. A long fragment aligner called AL- FALFA. BMC Bioinform. 16, 1 (May 2015), 159. DOI:http://dx.doi.org/10.1186/s12859-015-0533-0 (PDF p. 21)
52. Michaël Vyverman, Dieter De Smedt, Yao-Cheng Lin, Lieven Sterck, Bernard De Baets, Veerle Fack, and Peter Dawyndt. 2014. Fast and accurate cDNA mapping and splice site identification. In Proceedings of the International Conference on Bioinformatics Models, Methods and Algorithms (BIOSTEC’14). SCITEPRESS, 233–238. Retrieved from http://hdl.handle.net/1854/LU-6851320. (PDF p. 21)
53. Sebastian Wandelt and Ulf Leser. 2014. RRCA: Ultra-fast multiple in-species genome alignments. In Proceedings of trhe 1st International Conference on Algorithms for Computational Biology (AlCoB’14) (LNCS), Vol. 8542. Springer, 247–261. (PDF p. 21)
54. Hilmi Yildirim, Vineet Chaoji, and Mohammed J. Zaki. 2010. GRAIL: Scalable reachability index for large graphs. Proc. VLDB Endow. 3, 1–2 (Sept. 2010), 276–284. DOI:http://dx.doi.org/10.14778/1920841.1920879 Received May 2018; revised November 2018; accepted December 2018 ACM Transactions on Algorithms, Vol. 15, No. 2, Article 29. Publication date: February 2019. (PDF p. 21)
