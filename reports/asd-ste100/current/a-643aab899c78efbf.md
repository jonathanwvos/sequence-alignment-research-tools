# Compressed Dictionary Matching on Run-Length Encoded Strings

- Work ID: `w-643aab899c78`
- Asset ID: `a-643aab899c78efbf`
- Source PDF: `literature/academic-papers-processed/Compressed Dictionary Matching on Run-Length Encoded Strings - Bille et al.pdf`
- SHA-256: `643aab899c78efbf1ed61f39abe5f535a6da8a111ab35892780461e8a8911922`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors report all occurrences of multiple patterns in a text when both inputs use run-length encoding. (PDF p. 1).
- Their algorithm processes compressed inputs without decompression through a compressed Aho–Corasick representation. (PDF p. 2).
- Let R_P and R_S denote pattern and text run counts. The main bound is O((R_P + R_S) log log R_P + occ) expected time and O(R_P) space. (PDF p. 1).

## Objectives

- The authors seek dictionary matching time and space bounds in terms of compressed input size. (PDF p. 1).
- They also seek a deterministic algorithm with nearly the same time bound. (PDF p. 2).

## Arguments

- The authors argue that the expected time bound is within a log log R_P factor of optimal because an algorithm must read the input. (PDF p. 2).
- Direct simulation of failure links can require work proportional to uncompressed text length. This prevents the required compressed-time bound. (PDF p. 2).
- One output link per explicit node is insufficient because relevant patterns can end inside the last processed run. (PDF p. 2).

## Analysis

- The bounds assume a word-RAM with logarithmic word length. Space counts words and excludes read-only input. (PDF p. 2).
- Grouping automaton nodes permits total text processing in O(R_S log log R_P) time before occurrence reporting. (PDF p. 2).
- The deterministic method spends O((R_P + R_S) log log(R_P + R_S)) time and O(R_P + R_S) space on alphabet reduction. (PDF p. 13).

## Methods

- The run-length encoded trie treats each character-and-run-length pair as one letter. The algorithm simulates Aho–Corasick one text run at a time. (PDF p. 2).
- The method groups nodes to process failure transitions without traversing all implicit automaton states. (PDF p. 2).
- Occurrences that end in a specified text run are found through truncate match reporting. This problem is reduced to colored ancestor threshold reporting on weighted trees. (PDF p. 3).
- Compressed sorting and compact trie construction preprocess k patterns in O(R_P + k log log k) expected time and O(R_P) space. (PDF p. 3).

## Applications

- The algorithm reports every occurrence of every dictionary pattern in a run-length encoded text. (PDF p. 1).

## Optimization

- Alphabet reduction maps shared symbols to ranks and maps symbols unique to either input to separate replacement symbols. The reduced alphabet has size O(min(R_P, R_S) + 1). (PDF p. 13).
- The deterministic version replaces dictionaries with predecessor structures and uses direct addressing where the reduced alphabet permits it. (PDF p. 13).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- Theorem 1 gives O((R_P + R_S) log log R_P + occ) expected time and O(R_P) auxiliary space. (PDF p. 1).
- Theorem 2 gives O((R_P + R_S) log log(R_P + R_S) + occ) deterministic time and O(R_P + R_S) auxiliary space. (PDF p. 2).
- After deterministic preprocessing, text parsing and occurrence reporting take O(R_S log log R_P + occ) time. (PDF p. 14).

## Limitations and uncertainty

- The smaller space bound belongs to the randomized method and uses expected-time preprocessing. (PDF p. 2).
- The deterministic version needs additional space proportional to the text run count because it sorts text runs. (PDF p. 2).
- The runtime includes occ, the number of reported occurrences. Compression does not remove this output cost. (PDF p. 1).

## References

1. Alfred V. Aho and Margaret J. Corasick. Efficient string matching: An aid to bibliographic search. Commun. ACM, 18(6):333–340, 1975. (PDF p. 14)
2. Stephen Alstrup and Jacob Holm. Improved algorithms for finding level ancestors in dynamic trees. In Proc. 27th ICALP, pages 73–84, 2000. (PDF p. 14)
3. Stephen Alstrup, Thore Husfeldt, and Theis Rauhe. Marked ancestor problems. In Proc. 39th FOCS, pages 534–544, 1998. (PDF p. 14)
4. Amihood Amir and Gary Benson. Efficient two-dimensional compressed matching. In Proc. 2nd DCC, pages 279–288, 1992. (PDF p. 14)
5. Amihood Amir, Gary Benson, and Martin Farach. Optimal two-dimensional compressed matching. J. Algorithms, 24(2):354–379, 1997. (PDF p. 14)
6. Amihood Amir and Martin Farach. Adaptive dictionary matching. In Proc. 32nd FOCS, pages 760–766, 1991. (PDF p. 14)
7. Amihood Amir, Martin Farach, Zvi Galil, Raffaele Giancarlo, and Kunsoo Park. Dynamic dictionary matching. J. Comput. Syst. Sci., 49(2):208–222, 1994. (PDF p. 14)
8. Amihood Amir, Martin Farach, Ramana M. Idury, Johannes A. La Poutré, and Alejandro A. Schäffer. Improved dynamic dictionary matching. Inf. Comput., 119(2):258–282, 1995. (PDF p. 14)
9. Amihood Amir, Tsvi Kopelowitz, Avivit Levy, Seth Pettie, Ely Porat, and B. Riva Shalom. Mind the gap! - online dictionary matching with one gap. Algorithmica, 81(6):2123–2157, 2019. (PDF p. 14)
10. Amihood Amir, Gad M. Landau, and Dina Sokol. Inplace run-length 2d compressed search. Theor. Comput. Sci., 290(3):1361–1383, 2003. (PDF p. 14)
11. Amihood Amir, Avivit Levy, Ely Porat, and B. Riva Shalom. Dictionary matching with one gap. In Proc. 25th CPM, pages 11–20, 2014. (PDF p. 14)
12. Amihood Amir, Avivit Levy, Ely Porat, and B. Riva Shalom. Dictionary matching with a few gaps. Theor. Comput. Sci., 589:34–46, 2015. (PDF p. 14)
13. Amihood Amir, Moshe Lewenstein, and Ely Porat. Faster algorithms for string matching with k mismatches. J. Algorithms, 50(2):257–275, 2004. (PDF p. 14)
14. Arne Andersson and Stefan Nilsson. A new efficient radix sort. In Proc. 35th FOCS, pages 714–721, 1994. (PDF p. 14)
15. Alberto Apostolico, Gad M. Landau, and Steven Skiena. Matching for run-length encoded strings. J. Complex., 15(1):4–16, 1999. (PDF p. 14)
16. Tanver Athar, Carl Barton, Widmer Bland, Jia Gao, Costas S. Iliopoulos, Chang Liu, and Solon P. Pissis. Fast circular dictionary-matching algorithm. Math. Struct. Comput. Sci., 27(2):143–156, 2017. (PDF p. 14)
17. Arturs Backurs and Piotr Indyk. Which regular expression patterns are hard to match? In Proc. 57th FOCS, pages 457–466, 2016. (PDF p. 14)
18. Djamal Belazzougui. Succinct dictionary matching with no slowdown. In Proc. 21st CPM, pages 88–100, 2010. 14 (PDF p. 14)
19. Djamal Belazzougui. Worst-case efficient single and multiple string matching on packed texts in the word-ram model. J. Discrete Algorithms, 14:91–106, 2012. (PDF p. 15)
20. Omer Berkman and Uzi Vishkin. Finding level-ancestors in trees. J. Comput. Syst. Sci., 48(2):214– 230, 1994. (PDF p. 15)
21. Philip Bille, Inge Li Gørtz, Hjalte Wedel Vildhøj, and David Kofoed Wind. String matching with variable length gaps. Theoret. Comput. Sci., 443:25–34, 2012. (PDF p. 15)
22. Philip Bille and Mikkel Thorup. Regular expression matching with multi-strings and intervals. In Proc. 21st SODA, 2010. (PDF p. 15)
23. William I. Chang and Eugene L. Lawler. Sublinear approximate string matching and biological applications. Algorithmica, 12(4):327–344, 1994. (PDF p. 15)
24. Bernard Chazelle. Computing on a free tree via complexity-preserving mappings. Algorithmica, 2:337–361, 1987. (PDF p. 15)
25. Raphaël Clifford, Allyx Fontaine, Ely Porat, Benjamin Sach, and Tatiana Starikovskaya. Dictionary matching in a stream. In Proc. 23rd ESA, pages 361–372, 2015. (PDF p. 15)
26. Richard Cole, Lee-Ad Gottlieb, and Moshe Lewenstein. Dictionary matching and indexing with errors and don’t cares. In Proc. 36th STOC, pages 91–100, 2004. (PDF p. 15)
27. Beate Commentz-Walter. A string matching algorithm fast on the average. In Hermann A. Maurer, editor, Proc. 6th ICALP, volume 71, pages 118–132, 1979. (PDF p. 15)
28. Paul F. Dietz. Fully persistent arrays (extended array). In Proc. 1st WADS, pages 67–74, 1989. (PDF p. 15)
29. Paul F. Dietz. Finding level-ancestors in dynamic trees. In Proc. 2nd WADS, pages 32–40, 1991. (PDF p. 15)
30. Mohamed Y. Eltabakh, Wing-Kai Hon, Rahul Shah, Walid G. Aref, and Jeffrey Scott Vitter. The sbc-tree: an index for run-length compressed sequences. In Proc. 11th EDBT, pages 523–534, 2008. (PDF p. 15)
31. Paolo Ferragina and Fabrizio Luccio. Dynamic dictionary matching in external memory. Inf. Com- put., 146(2):85–99, 1998. (PDF p. 15)
32. Paolo Ferragina and S. Muthukrishnan. Efficient dynamic method-lookup for object oriented lan- guages (extended abstract). In Proc. 4th ESA, pages 107–120, 1996. (PDF p. 15)
33. Johannes Fischer, Travis Gagie, Pawel Gawrychowski, and Tomasz Kociumaka. Approximating LZ77 via small-space multiple-pattern matching. In Proc. 23rd ESA, pages 533–544, 2015. (PDF p. 15)
34. Johannes Fischer, Travis Gagie, Pawel Gawrychowski, and Tomasz Kociumaka. Approximating lz77 via small-space multiple-pattern matching. In Proc. 23rd ESA, pages 533–544, 2015. (PDF p. 15)
35. Michael L. Fredman, János Komlós, and Endre Szemerédi. Storing a sparse table with O(1) worst case access time. In Proc. 23rd FOCS, pages 165–169, 1982. (PDF p. 15)
36. Arnab Ganguly, Wing-Kai Hon, and Rahul Shah. A framework for dynamic parameterized dictionary matching. In Proc. 15th SWAT, pages 10:1–10:14, 2016. (PDF p. 15)
37. Shay Golan and Ely Porat. Real-time streaming multi-pattern search for constant alphabet. In Proc. 25th ESA, pages 41:1–41:15, 2017. (PDF p. 15)
38. Yijie Han. Deterministic sorting in o(nloglogn) time and linear space. J. Algorithms, 50(1):96–105, 2004. (PDF p. 15)
39. Wing-Kai Hon, Tsung-Han Ku, Rahul Shah, Sharma V. Thankachan, and Jeffrey Scott Vitter. Faster compressed dictionary matching. Theor. Comput. Sci., 475:113–119, 2013. (PDF p. 15)
40. Tomohiro I, Takaaki Nishimoto, Shunsuke Inenaga, Hideo Bannai, and Masayuki Takeda. Com- pressed automata for dictionary matching. Theor. Comput. Sci., 578:30–41, 2015. 15 (PDF p. 15)
41. Takuya Kida, Masayuki Takeda, Ayumi Shinohara, Masamichi Miyazaki, and Setsuo Arikawa. Mul- tiple pattern matching in LZW compressed text. In Proceedings of the 8th Data Compression Con- ference, pages 103–112, 1998. (PDF p. 16)
42. Donald E. Knuth, James H. Morris Jr., and Vaughan R. Pratt. Fast pattern matching in strings. SIAM J. Comput., 6(2):323–350, 1977. (PDF p. 16)
43. Tsvi Kopelowitz, Ely Porat, and Yaron Rozen. Succinct online dictionary matching with improved worst-case guarantees. In Proc. 27th CPM, pages 6:1–6:13, 2016. (PDF p. 16)
44. S. Muthukrishnan and Martin Müller. Time and space efficient method-lookup for object-oriented programs (extended abstract). In Proc. 7th SODA, pages 42–51, 1996. (PDF p. 16)
45. Gonzalo Navarro. A guided tour to approximate string matching. ACM Comput. Surv., 33(1):31–88, 2001. (PDF p. 16)
46. Milan Ružić. Constructing efficient dictionaries in close to sorting time. In Proc. 35th ICALP, pages 84–95, 2008. (PDF p. 16)
47. Yoshifumi Sakai. Computing the longest common subsequence of two run-length encoded strings. In Proc. 23rd ISAAC, pages 197–206, 2012. (PDF p. 16)
48. Dan E. Willard. Log-logarithmic worst-case range queries are possible in space theta(n). Inf. Process. Lett., 17(2):81–84, 1983. 16 (PDF p. 16)
