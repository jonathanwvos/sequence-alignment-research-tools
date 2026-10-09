# String editing under pattern constraints

- Work ID: `w-f5e286fcadce`
- Asset ID: `a-f5e286fcadce769d`
- Source PDF: `literature/academic-papers-processed/String editing under pattern constraints - Barish, Shibuya.pdf`
- SHA-256: `f5e286fcadce769dfb6e94810356dde63c42ac952e0132b8fb949f8cb230a77d`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors introduce algorithms for string editing under regular pattern constraints (StrEdit-SILC and StrEdit-SILCC). (PDF p. 2).
- They establish fixed-parameter tractable (FPT) algorithms parameterized by regular expression sizes and edit operations. (PDF p. 3).

## Objectives

- Find minimum-cost edit scripts transforming a string while ensuring intermediate or final substrings satisfy regular constraints. (PDF p. 2).

## Arguments

- Constrained string editing models biological sequence modifications that must preserve functional motifs or structural sites. (PDF p. 2).

## Analysis

- Computational complexity is analyzed using parameterized complexity theory and reductions to hitting set. (PDF p. 14).

## Methods

- Dynamic programming traverses cross-product graphs between input string positions and regular expression automata. (PDF p. 7).
- Graph transformations map constraint satisfaction to parameterized hitting set and shortest path instances. (PDF p. 14).

## Applications

- Biosequence engineering, motif-preserving alignment, and formal language-constrained sequence transformation. (PDF p. 2).

## Optimization

- Pruning affix patterns reduces intermediate state space before cross-product graph traversal. (PDF p. 8).

## Evaluation and testing

Not stated in the extractable source pages.

## Results

- Proves FPT tractability for several constrained string editing problems under realistic parameter bounds. (PDF p. 8).

## Limitations and uncertainty

- Computational complexity becomes intractable for general context-free language constraints without parameter bounds. (PDF p. 15).

## References

1. C.E. Shannon, A mathematical theory of communication, Bell Syst. Tech. J. 27 (3) (1948) 379–423, https://doi.org/10.1002/j.1538-7305.1948.tb01338.x. (PDF p. 15)
2. J.L. Peterson, Computer programs for detecting and correcting spelling errors, Commun. ACM 23 (12) (1980) 676–687, https://doi.org/10.1145/359038.359041. (PDF p. 15)
3. R.W. Hamming, Error detecting and error correcting codes, Bell Syst. Tech. J. 29 (2) (1950) 147–160, https://doi.org/10.1002/j.1538-7305.1950.tb00463.x. (PDF p. 15)
4. I.S. Reed, G. Solomon, Polynomial codes over certain ﬁnite ﬁelds, J. Soc. Ind. Appl. Math. 8 (2) (1960) 300–304, https://doi.org/10.1137/0108018. (PDF p. 15)
5. S.B. Wicker, V.K. Bhargava (Eds.), Reed-Solomon Codes and Their Applications, 1st ed., IEEE Press, Piscataway, NJ, 1994. (PDF p. 15)
6. F. Hao, R. Anderson, J. Daugman, Combining crypto with biometrics eﬀectively, IEEE Trans. Comput. 55 (9) (2006) 1081–1088, https://doi.org/10.1109/TC. 2006.138. (PDF p. 15)
7. E. Zielińska, W. Mazurczyk, K. Szczypiorski, Trends in steganography, Commun. ACM 57 (3) (2014) 86–95, https://doi.org/10.1145/2566590.2566610. (PDF p. 15)
8. I.J. Cox, M.L. Miller, Review of watermarking and the importance of perceptual modeling, in: Proc. SPIE 3016. Conference on Human Vision and Electronic Imaging II, 1997, pp. 92–99. (PDF p. 15)
9. S.G. Rizzo, F. Bertini, D. Montesi, Content-preserving text watermarking through unicode homoglyph substitution, in: Proc. 20th International Database Engi- neering and Applications Symposium (IDEAS), 2016, pp. 97–104. (PDF p. 15)
10. G. Fisk, M. Fisk, C. Papadopoulos, J. Neil, Eliminating steganography in internet traﬃc with active wardens, in: Proc. 5th International Workshop on Information Hiding (IH), 2002, pp. 18–35. (PDF p. 15)
11. C.B. Smith, S.S. Agaian, Denoising and the active warden, in: Proc. 2007 IEEE International Conference on Systems, Man and Cybernetics (SMC), 2007, pp. 3317–3322. (PDF p. 15)
12. R.D. Barish, T. Shibuya, String editing under pattern constraints, in: Proc. ICS 2022 Workshop on Algorithms, Bioinformatics, and Computation Theory (WABCT), 2022, pp. 13–24. (PDF p. 15)
13. J. Gallant, D. Maier, J. Astorer, On ﬁnding minimal length superstrings, J. Comput. Syst. Sci. 20 (1) (1980) 50–58, https://doi.org/10.1016/0022-0000(80) 90004-5. (PDF p. 15)
14. A. Blum, T. Jiang, M. Li, J. Tromp, M. Yannakakis, Linear approximation of shortest superstrings, J. ACM 41 (4) (1994) 630–647, https://doi.org/10.1145/ 179812.179818. (PDF p. 15)
15. V.I. Levenshtein, Binary codes capable of correcting deletions, insertions, and reversals, Sov. Phys. Dokl. 10 (8) (1966) 707–710. (PDF p. 15)
16. G. Navarro, A guided tour to approximate string matching, ACM Comput. Surv. 33 (1) (2001) 31–88, https://doi.org/10.1145/375360.375365. (PDF p. 15)
17. R.A. Wagner, M.J. Fischer, The string-to-string correction problem, J. ACM 21 (1) (1974) 168–173, https://doi.org/10.1145/321796.321811. (PDF p. 15)
18. S.B. Needleman, C.D. Wunsch, A general method applicable to the search for similarities in the amino acid sequence of two proteins, J. Mol. Biol. 48 (3) (1970) 443–453, https://doi.org/10.1016/0022-2836(70)90057-4. (PDF p. 15)
19. T.F. Smith, M.S. Waterman, Identiﬁcation of common molecular subsequences, J. Mol. Biol. 147 (1) (1981) 195–197, https://doi.org/10.1016/0022-2836(81) 90087-5. (PDF p. 15)
20. K. Abrahamson, Generalized string matching, SIAM J. Comput. 16 (6) (1987) 1039–1051, https://doi.org/10.1137/0216067. (PDF p. 15)
21. T. Akutsu, Approximate string matching with don’t care characters, in: Proc. 5th Annual Symposium on Combinatorial Pattern Matching (CPM), 1994, pp. 240–249. (PDF p. 15)
22. M.J. Fischer, M.S. Paterson, String-matching and other products, in: R.M. Karp (Ed.), Complexity of Computation, in: SIAM-AMS Proceedings, vol. 7, 1974, pp. 113–125. (PDF p. 15)
23. R.Y. Pinter, Eﬃcient string matching with don’t-care patterns, in: A. Apostolico, Z. Galil (Eds.), Combinatorial Algorithms on Words, in: NATO ASI Series (Series F: Computer and Systems Sciences), vol. 12, 1985, pp. 11–29. (PDF p. 15)
24. A.V. Aho, T.G. Peterson, A minimum distance error-correcting parser for context-free languages, SIAM J. Comput. 1 (4) (1972) 305–312, https://doi.org/10. 1137/0201022. (PDF p. 15)
25. J.R. Knight, E.W. Myers, Approximate regular expression pattern matching with concave gap penalties, Algorithmica 14 (1) (1995) 85–121, https://doi.org/10. 1007/BF01300375. (PDF p. 15)
26. F. Korn, B. Saha, D. Srivastava, S. Ying, On repairing structural problems in semi-structured data, Proc. VLDB Endow. 6 (9) (2013) 601–612, https://doi.org/10. 14778/2536360.2536361. Theoretical Computer Science 1022 (2024) 114889 16 R.D. Barish and T. Shibuya (PDF p. 15)
27. G. Lyon, Syntax-directed least-errors analysis for context-free languages: a practical approach, Commun. ACM 17 (1) (1974) 3–14, https://doi.org/10.1145/ 360767.360771. (PDF p. 16)
28. E.W. Myers, W. Miller, Approximate matching of regular expressions, Bull. Math. Biol. 51 (1) (1989) 5–37, https://doi.org/10.1016/S0092-8240(89)80046-1. (PDF p. 16)
29. G. Myers, Approximately matching context-free languages, Inf. Process. Lett. 54 (2) (1995) 85–92, https://doi.org/10.1016/0020-0190(95)00007-Y. (PDF p. 16)
30. B. Saha, The Dyck language edit distance problem in near-linear time, in: Proc. 55th Annual Symposium on Foundations of Computer Science (FOCS), 2014, pp. 611–620. (PDF p. 16)
31. R.A. Wagner, J.I. Seiferas, Correcting counter-automaton-recognizable languages, SIAM J. Comput. 7 (3) (1978) 357–375, https://doi.org/10.1137/0207029. (PDF p. 16)
32. J. Earley, An eﬃcient context-free parsing algorithm, Commun. ACM 13 (2) (1970) 94–102, https://doi.org/10.1145/362007.362035. (PDF p. 16)
33. B. Saha, Fast & space-eﬃcient approximations of language edit distance and RNA folding: an amnesic dynamic programming approach, in: Proc. 58th Annual Symposium on Foundations of Computer Science (FOCS), 2017, pp. 295–306. (PDF p. 16)
34. J. Guo, D. Hermelin, C. Komusiewicz, Local search for string problems: brute-force is essentially optimal, Theor. Comput. Sci. 525 (2014) 30–41, https:// doi.org/10.1016/j.tcs.2013.05.006. (PDF p. 16)
35. L. Bulteau, F. Hüﬀner, C. Komusiewicz, R. Niedermeier, Multivariate algorithmics for NP-hard string problems, Bull. Eur. Assoc. Theor. Comput. Sci. 114 (2014) 1–43. (PDF p. 16)
36. M. Chen, H. Jiang, N. Liu, L. Wang, B. Zhu, On the existence of parameterized algorithms for the shortest common supersequence and related problems, in: Proc. 18th International Conference on Algorithmic Aspects in Information and Management (AAIM), 2024, pp. 209–219. (PDF p. 16)
37. V.G. Timkovskii, Complexity of common subsequence and supersequence problems and related problems, Cybern. Syst. Anal. 25 (5) (1989) 565–580, https:// doi.org/10.1007/BF01075212. (PDF p. 16)
38. M.R. Alam, M.S. Rahman, The substring inclusion constraint longest common subsequence problem can be solved in quadratic time, J. Discret. Algorithms 17 (2012) 67–73, https://doi.org/10.1016/j.jda.2012.11.004. (PDF p. 16)
39. A.N. Arslan, O. Eğecioğlu, Algorithms for the constrained longest common subsequence problems, Int. J. Found. Comput. Sci. 16 (6) (2005) 1099–1109, https:// doi.org/10.1142/S0129054105003674. (PDF p. 16)
40. Y.C. Chen, K.M. Chao, On the generalized constrained longest common subsequence problems, J. Comb. Optim. 21 (3) (2011) 383–392, https://doi.org/10. 1007/s10878-009-9262-5. (PDF p. 16)
41. F.Y.L. Chin, A.D. Santis, A.L. Ferrara, N.L. Ho, S.K. Kim, A simple algorithm for the constrained sequence problems, Inf. Process. Lett. 90 (4) (2004) 175–179, https://doi.org/10.1016/j.ipl.2004.02.008. (PDF p. 16)
42. S. Deorowicz, Quadratic-time algorithm for a string constrained LCS problem, Inf. Process. Lett. 112 (11) (2012) 423–426, https://doi.org/10.1016/j.ipl.2012. 02.007. (PDF p. 16)
43. Z. Gotthilf, D. Hermelin, G.M. Landau, M. Lewenstein, Restricted LCS, in: Proc. 17th International Symposium on String Processing and Information Retrieval (SPIRE), 2010, pp. 250–257. (PDF p. 16)
44. Z. Gotthilf, D. Hermelin, M. Lewenstein, Constrained LCS: hardness and approximation, in: Proc. 19th Annual Symposium on Combinatorial Pattern Matching (CPM), 2008, pp. 255–262. (PDF p. 16)
45. Z. Gotthilf, M. Lewenstein, Approximating constrained LCS, in: Proc. 14th International Symposium on String Processing and Information Retrieval (SPIRE), 2007, pp. 164–172. (PDF p. 16)
46. C.S. Iliopoulos, M.S. Rahman, New eﬃcient algorithms for the LCS and constrained LCS problems, Inf. Process. Lett. 106 (1) (2008) 13–18, https://doi.org/10. 1016/j.ipl.2007.09.008. (PDF p. 16)
47. Y.T. Tsai, The constrained longest common subsequence problem, Inf. Process. Lett. 88 (4) (2003) 173–176, https://doi.org/10.1016/j.ipl.2003.07.001. (PDF p. 16)
48. G. Bernardini, H. Chen, A. Conte, R. Grossi, G. Loukides, N. Pisanti, S.P. Pissis, G. Rosone, String sanitization: a combinatorial approach, in: Proc. Joint European Conference on Machine Learning and Knowledge Discovery in Databases (ECML PKDD), 2019, pp. 627–644. (PDF p. 16)
49. G. Bernardini, H. Chen, G. Loukides, N. Pisanti, S.P. Pissis, L. Stougie, M. Sweering, String sanitization under edit distance, in: Proc. 31st Annual Symposium on Combinatorial Pattern Matching (CPM), 2020, pp. 1–14. (PDF p. 16)
50. G. Bernardini, H. Chen, A. Conte, R. Grossi, G. Loukides, N. Pisanti, S.P. Pissis, G. Rosone, M. Sweering, Combinatorial algorithms for string sanitization, ACM Trans. Knowl. Discov. Data 15 (1) (2021) 1–34, https://doi.org/10.1145/3418683. (PDF p. 16)
51. A.V. Aho, M.J. Corasick, Eﬃcient string matching: an aid to bibliographic search, Commun. ACM 18 (6) (1975) 333–340, https://doi.org/10.1145/360825. 360855. (PDF p. 16)
52. C.H. Papadimitriou, M. Yannakakis, Optimization, approximation, and complexity classes, in: Proc. 20th Annual ACM Symposium on Theory of Computing (STOC), 1988, pp. 229–234. (PDF p. 16)
53. C.H. Papadimitriou, M. Yannakakis, Optimization, approximation, and complexity classes, J. Comput. Syst. Sci. 43 (3) (1991) 425–440, https://doi.org/10.1016/ 0022-0000(91)90023-X. (PDF p. 16)
54. E.W. Dijkstra, A note on two problems in connexion with graphs, Numer. Math. 1 (1959) 269–271, https://doi.org/10.1007/BF01386390. (PDF p. 16)
55. E.M. McCreight, A space-economical suﬃx tree construction algorithm, J. ACM 23 (2) (1976) 262–272, https://doi.org/10.1145/321941.321946. (PDF p. 16)
56. R.B. Dial, Algorithm 360: shortest-path forest with topological ordering [H], Commun. ACM 12 (11) (1969) 632–633, https://doi.org/10.1145/363269.363610. (PDF p. 16)
57. K. Thompson, Programming techniques: regular expression search algorithm, Commun. ACM 11 (6) (1968) 419–422, https://doi.org/10.1145/363347.363387. (PDF p. 16)
58. J.A. Brzozowsk, Canonical regular expressions and minimal state graphs for deﬁnite events, in: Proc. Symposium on Mathematical Theory of Automata, New York, 1962, Polytechnic Press of Polytechnic Inst. of Brooklyn, Brooklyn, N.Y., 1963, pp. 529–561. (PDF p. 16)
59. J.M. Lewis, M. Yannakakis, The node-deletion problem for hereditary properties is NP-complete, J. Comput. Syst. Sci. 20 (2) (1980) 219–230, https://doi.org/ 10.1016/0022-0000(80)90060-4. (PDF p. 16)
60. M. Yannakakis, Node- and edge-deletion NP-complete problems, in: Proc. 10th Annual ACM Symposium on Theory of Computing (STOC), 1978, pp. 253–264. (PDF p. 16)
61. C. Lund, M. Yannakakis, The approximation of maximum subgraph problems, in: Proc. 20th International Colloquium on Automata, Languages and Programming (ICALP), 1993, pp. 40–51. (PDF p. 16)
62. U. Feige, S. Kogan, The hardness of approximating hereditary properties, Preprint; Department of Computer Science and Applied Mathematics, Weizmann Institute, 2005. (PDF p. 16)
63. M. Bläser, Computing small partial coverings, Inf. Process. Lett. 85 (6) (2003) 327–331, https://doi.org/10.1016/S0020-0190(02)00434-9. (PDF p. 16)
64. M.E. Allentoft, M. Collins, D. Harker, J. Haile, C.L. Oskam, M.L. Hale, P.F. Campos, J.A. Samaniego, M.T.P. Gilbert, E. Willerslev, G. Zhang, R.P. Scoﬁeld, R.N. Holdaway, M. Bunce, The half-life of DNA in bone: measuring decay kinetics in 158 dated fossils, Proc. R. Soc. B: Biol. Sci. 279 (1748) (2012) 4724–4733, https://doi.org/10.1098/rspb.2012.1745. (PDF p. 16)
65. A.W. Briggs, U. Stenzel, P.L.F. Johnson, R.E. Green, J. Kelso, K. Prüfer, M. Meyer, J. Krause, M.T. Ronan, M. Lachmann, S. Pääbo, Patterns of damage in genomic DNA sequences from a Neandertal, Proc. Natl. Acad. Sci. USA 104 (37) (2007) 14616–14621, https://doi.org/10.1073/pnas.0704665104. (PDF p. 16)
66. J. Dabney, M. Meyer, S. Pääbo, Ancient DNA damage, Cold Spring Harb. Perspect. Biol. 5 (7) (2013) 1–7, https://doi.org/10.1101/cshperspect.a012567. (PDF p. 16)
67. M. Hofreiter, D. Serre, H.N. Poinar, M. Kuch, S. Pääbo, D.N.A. Ancient, Nat. Rev. Genet. 2 (5) (2001) 353–359, https://doi.org/10.1038/35072071. (PDF p. 16)
68. S. Brown, T. Higham, V. Slon, S. Pääbo, M. Meyer, K. Douka, F. Brock, D. Comeskey, N. Procopio, M. Shunkov, A. Derevianko, M. Buckley, Identiﬁcation of a new hominin bone from Denisova Cave, Siberia using collagen ﬁngerprinting and mitochondrial DNA analysis, Sci. Rep. 6 (1) (2016) 1–8, https://doi.org/10. 1038/srep23559. (PDF p. 16)
69. M. Buckley, S. Warwood, B. van Dongen, A.C. Kitchener, P.L. Manning, A fossil protein chimera; diﬃculties in discriminating dinosaur peptide sequences from modern cross-contamination, Proc. R. Soc. B: Biol. Sci. 284 (1855) (2017) 1–8, https://doi.org/10.1098/rspb.2017.0544. Theoretical Computer Science 1022 (2024) 114889 17 R.D. Barish and T. Shibuya (PDF p. 16)
70. J. Hendy, F. Welker, B. Demarchi, C. Speller, C. Warinner, M.J. Collins, A guide to ancient protein studies, Nat. Ecol. Evol. 2 (2018) 791–799, https://doi.org/ 10.1038/s41559-018-0510-x. (PDF p. 17)
71. J.M. Asara, M.H. Schweitzer, L.M. Freimark, M. Phillips, L.C. Cantley, Protein sequences from mastodon and Tyrannosaurus rex revealed by mass spectrometry, Science 316 (5822) (2007) 280–285, https://doi.org/10.1126/science.1137614. (PDF p. 17)
72. M. Buckley, et al., Comment on “Protein sequences from mastodon and Tyrannosaurus rex revealed by mass spectrometry”, Science 319 (5859) (2008) 33, https:// doi.org/10.1126/science.1147046. (PDF p. 17)
73. M.V. Emery, K. Bolhofner, S. Winingear, R. Oldt, M. Montes, S. Kanthaswamy, J.E. Buikstra, L.C. Fulginiti, A.C. Stone, Reconstructing full and partial STR proﬁles from severely burned human remains using comparative ancient and forensic DNA extraction techniques, Forensic Sci. Int.: Genet. 46 (2020) 1–8, https://doi.org/10.1016/j.fsigen.2020.102272. (PDF p. 17)
74. K.E. Latham, J.J. Miller, DNA recovery and analysis from skeletal material in modern forensic contexts, Forensic Sci. Res. 4 (1) (2019) 51–59, https://doi.org/ 10.1080/20961790.2018.1515594. (PDF p. 17)
75. C.J.A. Sigrist, E. de Castro, L. Cerutti, B.A. Cuche, N. Hulo, A. Bridge, L. Bougueleret, I. Xenarios, New and continuing developments at PROSITE, Nucleic Acids Res. 41 (Database issue) (2013) D344–D347, https://doi.org/10.1093/nar/gks1067. (PDF p. 17)
76. A. Alexaki, et al., Eﬀects of codon optimization on coagulation factor IX translation and structure: implications for protein and gene therapies, Sci. Rep. 9 (1) (2019) 1–15, https://doi.org/10.1038/s41598-019-51984-2. (PDF p. 17)
77. V.P. Mauro, S.A. Chappell, A critical analysis of codon optimization in human therapeutics, Trends Mol. Med. 20 (11) (2014) 604–613, https://doi.org/10.1016/ j.molmed.2014.09.003. (PDF p. 17)
78. P. Montes, H. Memelli, C.B. Ward, J. Kim, J.S.B. Mitchell, S. Skiena, Optimizing restriction site placement for synthetic genomes, Inf. Comput. 213 (2012) 59–69, https://doi.org/10.1016/j.ic.2012.02.003. (PDF p. 17)
79. S. Sauret-Güeto, E. Frangedakis, L. Silvestri, M. Rebmann, M. Tomaselli, K. Markel, M. Delmans, A. West, N.J. Patron, J. Haseloﬀ, Systematic tools for reprogram- ming plant gene expression in a simple model, Marchantia polymorpha, ACS Synth. Biol. 9 (4) (2020) 864–882, https://doi.org/10.1021/acssynbio.9b00511. (PDF p. 17)
80. A.E. Borujeni, D. Cetnar, I. Farasat, A. Smith, N. Lundgren, H.M. Salis, Precise quantiﬁcation of translation inhibition by mRNA structures that overlap with the ribosomal footprint in N-terminal coding sequences, Nucleic Acids Res. 45 (9) (2017) 5437–5448, https://doi.org/10.1093/nar/gkx061. (PDF p. 17)
81. P. Gaspar, G. Moura, M.A.S. Santos, J.L. Oliveira, mRNA secondary structure optimization using a correlated stem-loop prediction, Nucleic Acids Res. 41 (6) (2013) 1–5, https://doi.org/10.1093/nar/gks1473. (PDF p. 17)
82. J.A. Doudna, E. Charpentier, The new frontier of genome engineering with CRISPR-Cas9, Science 346 (6213) (2014) 1–9, https://doi.org/10.1126/science. 1258096. (PDF p. 17)
83. M. Ikeda, S. Matsuyama, S. Akagi, K. Ohkoshi, S. Nakamura, S. Minabe, K. Kimura, M. Hosoe, Correction of a disease mutation using CRISPR/Cas9-assisted genome editing in Japanese black cattle, Sci. Rep. 7 (1) (2017) 1–9, https://doi.org/10.1038/s41598-017-17968-w. (PDF p. 17)
84. G. Darcis, C.S. Binda, B. Klaver, E. Herrera-Carrillo, B. Berkhout, A.T. Das, The impact of HIV-1 genetic diversity on CRISPR-Cas9 antiviral activity and viral escape, Viruses 11 (3) (2019) 1–14, https://doi.org/10.3390/v11030255. (PDF p. 17)
85. M.K. White, W. Hu, K. Khalili, The CRISPR/Cas9 genome editing methodology as a weapon against human viruses, Discov. Med. 19 (105) (2015) 255–262. (PDF p. 17)
86. M. Karpinski, R. Schmied, Improved inapproximability results for the shortest superstring and related problems, in: Proc. 19th Computing: The Australasian Theory Symposium (CATS), 2013, pp. 27–36. (PDF p. 17)
