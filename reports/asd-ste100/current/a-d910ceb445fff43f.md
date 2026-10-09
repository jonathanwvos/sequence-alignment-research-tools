# Alignment of Whole Genomes

- Work ID: `b-c6835dd06cbe`
- Asset ID: `a-d910ceb445fff43f`
- Source PDF: `literature/academic-papers-processed/Alignment of whole genomes.pdf`
- SHA-256: `d910ceb445fff43fbf59ae6682c7509834c5d5efcbfba5646d7d32095a8b32c7`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- MUMmer aligns genome sequences through maximal unique matches, a longest increasing subsequence step, and local gap alignment. (PDF p. 3).
- The authors demonstrate the system on two tuberculosis strains, two Mycoplasma species, and human–mouse syntenic regions. (PDF p. 1).

## Objectives

- The system aims to produce base-to-base comparisons of closely related genomes and identify small mutations and large sequence changes. (PDF p. 1).

## Arguments

- The authors argue that conventional alignment methods require excessive time or memory for whole genomes. Large insertions also limit methods that assume few differences. (PDF p. 2).
- The authors use long exact matches that occur once in each genome as alignment anchors. They argue that these matches are very likely to belong to the global alignment. (PDF p. 3).

## Analysis

- McCreight’s algorithm constructs the suffix tree in linear time. The tree size is linear in the combined sequence length. (PDF p. 3).
- Overlapping MUMs can indicate tandem repeats. Differences in overlap length identify additional repeat bases in one genome. (PDF p. 5).

## Methods

- The system identifies maximal unique matches on both DNA strands. Each match occurs exactly once in each genome and cannot extend without a mismatch. (PDF p. 3).
- A variation of the longest increasing subsequence algorithm selects the longest set of matches with the same order in both genomes. (PDF p. 3).
- The system aligns small polymorphic gaps with dynamic programming equivalent to Smith–Waterman. This gives an optimal local alignment under specified insertion and mutation costs. (PDF p. 5).
- Post-processing detects transpositions from matches outside the selected order. Large gaps present in only one genome indicate insertions. (PDF p. 5).

## Applications

- The system can compare successive genome assemblies to show changes from gap closure, error correction, and added sequence. (PDF p. 2).
- The graphical interface supports genome inspection and links genes to database records. The authors used it to inspect silent mutations, premature stops, and intergenic differences. (PDF p. 5).

## Optimization

- Unique exact matches divide the alignment into smaller gap problems. This limits the regions that require Smith–Waterman alignment. (PDF p. 3).
- For large polymorphic regions, the authors propose recursive matching with a lower minimum MUM length. (PDF p. 5).

## Evaluation and testing

- The tuberculosis comparison used H37Rv and CDC1551. The authors report more than 99% identity when large repeats with different copy numbers are excluded. (PDF p. 5).
- The human–mouse test compared 222,930 bp from human chromosome 12p13 with 227,538 bp from mouse chromosome 6. The authors tested minimum MUM lengths of 15 and 10 bp. (PDF p. 7).
- The Mycoplasma comparison includes plots from FASTA, unique 25-base matches, and MUMs. The authors report less than 50% mean identity in the aligned gaps between MUMs. (PDF p. 7).

## Results

- The tuberculosis alignment took 55 seconds on a DEC Alpha 4100. Tree construction took 5 seconds, sorting and LIS extraction took 45 seconds, and gap alignment took 5 seconds. (PDF p. 5).
- The tuberculosis comparison found thousands of differences, mainly single-base changes, and several dozen large insertions unique to each genome. (PDF p. 5).
- The human–mouse alignment took 29 seconds of CPU time. Suffix tree construction used 1.6 seconds. (PDF p. 7).
- The human–mouse alignment covered 220,326 human bases and 223,751 mouse bases. MUMs covered 14,026 bases, or 6.3% of the human input. (PDF p. 8).

## Limitations and uncertainty

- The algorithm assumes close homology and a mapping between large parts of the input sequences. (PDF p. 2).
- Repeated sequences cannot form unique anchors. The system must process them through the gaps and surrounding matches. (PDF p. 5).
- The human–mouse output contains fewer details than the earlier combination of alignment tools. Complete inspection requires the Smith–Waterman output. (PDF p. 7).
- The authors make their proposed extension to the longest genome sequences conditional on sufficient computer memory. (PDF p. 8).

## References

1. Fleischmann,R.D., Adams,M., White,O., Clayton,R., Kirkness,E., Kerlavage,A., Bult,C., Tomb,J.-F., Dougherty,B., Merrick,J., McKenney,K., Sutton,G., FitzHugh,W., Fields,C., Gocayne,J., Scott,J., Shirley,R., Liu,L.-I., Glodek,A., Kelley,J., Weidman,J., Phillips,C., Spriggs,T., Hedblom,E., Cotton,M., Utterback,T., Hanna,M., Nguyen,D., Saudek,D., Brandon,R., Fine,L., Fritchman,J., Fuhrmann,J., Geoghagen,N., Gnehm,C., McDonald,L., Small,K., Fraser,C., Smith,H. and Venter,J.C. (1995) Science, 269, 496–512. (PDF p. 8)
2. Fraser,C.M., Gocayne,J., White,O., Adams,M., Clayton,R., Fleischmann,R., Bult,C., Kerlavage,A., Sutton,G., Kelley,J., Fritchman,J., Weidman,J., Small,K., Sandusky,M., Fuhrmann,J., Nguyen,D., Utterback,T., Saudek,R., Phillips,C., Merrick,J., Tomb,J.-F., Dougherty,B., Bott,K., Hu,P.-C., Lucier,T., Peterson,S., Smith,H., Hutchison,C. and Venter,J.C. (1995) Science, 270, 397–403. (PDF p. 8)
3. Himmelreich,R., Hilbert,H., Plagens,H., Pirkl,E., Li,B.C. and Herrmann,R. (1996) Nucleic Acids Res., 24, 4420–4449. (PDF p. 8)
4. Cole,S.T., Brosch,R., Parkhill,J., Garnier,T., Churcher,C., Harris,D., Gordon,S.V., Eiglmeier,K., Gas,S., Barry,C.E., Tekaia,F., Badcock,K., Basham,D., Brown,D., Chillingworth,T., Connor,R., Davies,R., Devlin,K., Feltwell,T., Gentles,S., Hamlin,N., Holroyd,S., Hornsby,T., Jagels,K. and Barrell,B. (1998) Nature, 393, 537–544. (PDF p. 8)
5. Stephens,R., Kalman,S., Lammel,C., Fan,J., Marathe,R., Aravind,L., Mitchell,W., Olinger,L., Tatusov,R., Zhao,Q., Koonin,E. and Davis,R. (1998) Science, 282, 754–759. (PDF p. 8)
6. Needleman,S. and Wunsch,C. (1970) J. Mol. Biol., 48, 443–453. (PDF p. 8)
7. Smith,T. and Waterman,M. (1981) J. Mol. Biol., 147, 195–197. (PDF p. 8)
8. Pearson,W.R. (1995) Prot. Sci., 4, 1145–1160. (PDF p. 8)
9. Gusfield,D. (1997) Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology. Cambridge University Press, New York. (PDF p. 8)
10. Waterman,M. (1995) Introduction to Computational Biology: Maps, Sequences and Genomes. Chapman & Hall, New York. (PDF p. 8)
11. Lipman,D.J. and Pearson,W.R. (1985) Science, 227, 1435–1441. (PDF p. 8)
12. Benson,G. (1999) Nucleic Acids. Res., 27, 573–580. (PDF p. 8)
13. Chao,K.-M., Zhang,J., Ostell,J. and Miller,W. (1997) Comput. Appl. Biosci., 13, 75–80. (PDF p. 8)
14. Chao,K.-M., Zhang,J., Ostell,J. and Miller,W. (1995) Comput. Appl. Biosci., 11, 147–153. (PDF p. 8)
15. Altschul,S., Gish,W., Miller,W., Myers,E. and Lipman,D. (1990) J. Mol. Biol., 215, 403–410. (PDF p. 8)
16. Altschul,S., Madden,T., Schaffer,A., Zhang,J., Zhang,Z., Miller,W. and Lipman,D. (1997) Nucleic Acids Res., 25, 3389–3402. (PDF p. 8)
17. Weiner,P. (1973) Linear pattern matching algorithms. In Proc. 14th IEEE Symp. Switching & Automata Theory. pp. 1–11. (PDF p. 8)
18. McCreight,E.M. (1976) J. ACM, 23, 262–272. (PDF p. 8)
19. Brazma,A., Jonassen,I., Vilo,J. and Ukkonen,E. (1998) Genome Res., 8, 1202–1215. (PDF p. 8)
20. Chen,M.T. and Seiferas,J. (1985) In Apostolico,A. and Galil,Z. (eds), Combinatorial Algorithms on Words. Springer-Verlag, New York, pp. 97–107. (PDF p. 8)
21. Ukkonen,E. (1995) Algorithmica, 14, 249–260. (PDF p. 8)
22. Kurtz,S. (1998) Reducing the space requirement of suffix trees. Technical Report 98–03, Universität at Bielefeld, Bielefeld, Germany. (PDF p. 8)
23. Weiss,K.N. (1998) Genome Res., 8, 691–697. (PDF p. 8)
24. Taillon-Miller,P., Gu,Z., Li,Q., Hillier,L. and Kwok,P.-Y. (1998) Genome Res., 8, 748–754. (PDF p. 8)
25. Valway,S.E., Sanchez,M.P., Shinnick,T.F.,.Orme,I., Agerton,T., Hoy,D., Jones,J.S, Westmoreland,H. and Onorato,I.M. (1997) N. Engl. J. Med., 338, 633–639. (PDF p. 8)
26. Sreevatsan,S., Pan,X., Stockbauer,K.E., Connell,N.D., Kreiswirth,B.N., Whittam,T.S. and Musser,J.M. (1997) Proc. Natl Acad. Sci. USA, 94, 9869–9874. (PDF p. 8)
27. Himmelreich,R., Plagens,H., Hilbert,H., Reiner,B. and Herrmann,R. (1997) Nucleic Acids Res., 25, 701–712. (PDF p. 8)
28. Ansari-Lari,M., Oeltjen,J.C., Schwartz,S., Zhang,Z., Muzny,D.M., Lu,J., Gorrell,J.H., Chinault,A.C., Belmont,J.W., Miller,W. and Gibbs,R.A. (1998) Genome Res., 8, 29–40. (PDF p. 8)
29. Sonnhammer,E. and Durbin,R. (1995) Gene, 167, GC1–GC10. (PDF p. 8)
30. Huang,X., Hardison,R. and Miller,W. (1990) Comput. Appl. Biosci., 6, 373–381. (PDF p. 8)
31. Schwartz,S., Miller,W., Yang,C.-M. and Hardison R.C. (1991) Nucleic Acids Res., 19, 4663–4667. (PDF p. 8)
32. Oeltjen,J.C., Malley,T.M., Muzny,D.M., Miller,W., Gibbs,R.A. and Belmont,J.W. (1997) Genome Res., 7, 315–329. Downloaded from academic.oup.com/nar/article/27/11/2369/1258501 by guest on 26 September 2026 (PDF p. 8)
