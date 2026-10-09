# MAFFT: A Novel Method for Rapid Multiple Sequence Alignment Based on Fast Fourier Transform

- Work ID: `b-10158df744de`
- Asset ID: `a-3ce9d7fdf2aace2e`
- Source PDF: `literature/academic-papers-processed/MAFFT: a novel method for rapid multiple sequence alignment based on fast Fourier transform - Katoh et al.pdf`
- SHA-256: `3ce9d7fdf2aace2e17bc48e50df0d418f58a2d26346566c4308fb51069313943`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- MAFFT uses FFT to identify homologous regions from amino acid volume and polarity values. It combines this procedure with a normalized scoring system. (PDF p. 1).
- The program provides progressive alignment through FFT-NS-2 and iterative refinement through FFT-NS-i. (PDF p. 1).
- The authors report substantial speed gains with accuracy comparable to the tested alternatives. (PDF p. 1).

## Objectives

- Reduce multiple alignment time through rapid detection of homologous segments. (PDF p. 1).
- Improve scoring for distant sequences and sequences with large insertions or terminal extensions. (PDF p. 1).

## Arguments

- The authors argue that an optimum alignment score does not guarantee biological correctness. The scoring system strongly affects accuracy. (PDF p. 1).
- The authors attribute improved handling of long insertions and extensions to matrix normalization without more complex alignment procedures. (PDF p. 7).

## Analysis

- For sequences of similar length N, FFT reduces correlation computation from O(N²) to O(N log N). Correlation peaks identify candidate positional offsets. (PDF p. 2).
- Power regression showed nearly linear time in sequence length for highly conserved inputs. Standard NW methods showed approximately quadratic time. (PDF p. 4).
- In the normalized matrix, the expected score per random residue pair is Sa. The expected score for identical sequences is 1 + Sa. (PDF p. 3).

## Methods

- Amino acids are converted to normalized volume and polarity vectors. FFT computes correlations for both components and adds them. (PDF p. 2).
- The method scans 30-site windows at the 20 highest correlation peaks. It accepts segments above 0.7 per site, merges adjacent segments, and splits segments longer than 150 sites. (PDF p. 2).
- Segment-level dynamic programming selects a consistent segment order. The resulting anchors divide the full alignment matrix into smaller regions. (PDF p. 3).
- FFT-NS-1 uses shared 6-tuples and UPGMA for its guide tree. FFT-NS-2 rebuilds the tree and aligns again. FFT-NS-i repeatedly splits and realigns groups until the score no longer improves. (PDF p. 4).

## Applications

- The method supports nucleotide alignment through four-component vectors for A, T, G, and C frequencies. (PDF p. 3).
- The authors test LSU rRNA datasets with 72 sequences and a 59-sequence subset that excludes fragments. (PDF p. 6).
- RNA polymerase tests use 76-sequence and 24-sequence datasets from Bacteria, Archaea, and Eucarya. The reference has 11 conserved blocks. (PDF p. 7).

## Optimization

- Anchors at homologous segment centers exclude parts of the dynamic programming matrix from computation. (PDF p. 3).
- A simple position-specific gap penalty reduces penalties where existing gaps start or end. The authors report lower computation cost with comparable accuracy. (PDF p. 4).
- The default protein scoring uses a normalized 200 PAM matrix, gap-opening parameter 2.4, and offset 0.06. (PDF p. 3).

## Evaluation and testing

- ROSE simulations test conserved sequences at 100 PAM and distant sequences at 250 PAM. Power regression estimates time dependence on length and sequence count. (PDF p. 4).
- Simulation accuracy is the fraction of correctly aligned residue pairs. Each condition is repeated 100 times and averaged. (PDF p. 5).
- BAliBASE tests cover 144 alignments in five categories. They measure sum-of-pairs and column scores and use Wilcoxon matched-pair and t-tests. (PDF p. 6).
- Ablations replace FFT with standard NW dynamic programming or replace the normalized matrix with an all-positive matrix. (PDF p. 4).

## Results

- On BAliBASE, FFT-NS-2 and NW-NS-2 have identical average scores of 0.845 for residue pairs and 0.652 for columns. Their total times are 227 and 243 seconds. (PDF p. 6).
- FFT-NS-i takes 1,466 seconds on BAliBASE, compared with 12,065 seconds for T-COFFEE. The reported accuracy differences are not statistically significant. (PDF p. 6).
- On 76 RNA polymerase sequences, FFT-NS-2 recovers all 11 blocks in 18.15 seconds. NW-NS-2 also recovers all blocks but takes 59.30 seconds. (PDF p. 7).
- On the 59-sequence LSU dataset, FFT-NS-i takes 181.7 seconds with pair and column scores of 0.817 and 0.552. T-COFFEE takes 35,860 seconds with scores of 0.806 and 0.559. (PDF p. 7).

## Limitations and uncertainty

- FFT offers little speed benefit on the distant sequences in BAliBASE. FFT-NS-2 takes nearly the same time as NW-NS-2 there. (PDF p. 6).
- BAliBASE favors small sets of short sequences. Its alignments average 9.2 sequences and 251.1 sites. (PDF p. 6).
- Fragments prevent column scoring for the full LSU dataset. T-COFFEE tests on the full LSU and large RNA polymerase datasets stop because of insufficient memory. (PDF p. 7).

## References

1. Needleman,S.B. and Wunsch,C.D. (1970) A general method applicable to the search for similarities in the amino acid sequence of two proteins. J. Mol. Biol., 48, 443±453. (PDF p. 8)
2. Sankoff,D. and Cedergren,R.J. (1983) Simultaneous comparison of three or more sequences related by a tree. In Sankoff,D. and Kruskal,J.B. (eds), Time Warps, String Edits and Macromolecules: The Theory and Practice of Sequence Comparison. Addison-Wesley, London, UK, pp. 253±264. (PDF p. 8)
3. Feng,D.F. and Doolittle,R.F. (1987) Progressive sequence alignment as a prerequisite to correct phylogenetic trees. J. Mol. Evol., 25, 351±360. (PDF p. 8)
4. Barton,G.J. and Sternberg,M.J. (1987) A strategy for the rapid multiple alignment of protein sequences. Con®dence levels from tertiary structure comparisons. J. Mol. Biol., 198, 327±337. (PDF p. 8)
5. Berger,M.P. and Munson,P.J. (1991) A novel randomized iterative strategy for aligning multiple protein sequences. Comput. Appl. Biosci., 7, 479±484. (PDF p. 8)
6. Gotoh,O. (1993) Optimal alignment between groups of sequences and its application to multiple sequence alignment. Comput. Appl. Biosci., 9, 361±370. (PDF p. 8)
7. Thompson,J.D., Higgins,D.G. and Gibson,T.J. (1994) CLUSTAL W: improving the sensitivity of progressive multiple sequence alignment through sequence weighting, position-speci®c gap penalties and weight matrix choice. Nucleic Acids Res., 22, 4673±4680. (PDF p. 8)
8. Thompson,J.D., Plewniak,F. and Poch,O. (1999) A comprehensive comparison of multiple sequence alignment programs. Nucleic Acids Res., 27, 2682±2690. (PDF p. 8)
9. Notredame,C., Higgins,D.G. and Heringa,J. (2000) T-Coffee: a novel method for fast and accurate multiple sequence alignment. J. Mol. Biol., 302, 205±217. (PDF p. 8)
10. Delcher,A.L., Kasif,S., Fleischmann,R.D., Peterson,J., White,O. and Salzberg,S.L. (1999) Alignment of whole genomes. Nucleic Acids Res., 27, 2369±2376. (PDF p. 8)
11. Pearson,W.R. and Lipman,D.J. (1988) Improved tools for biological sequence comparison. Proc. Natl Acad. Sci. USA, 85, 2444±2448. (PDF p. 8)
12. Altschul,S.F., Madden,T.L., Schaffer,A.A., Zhang,J., Zhang,Z., Miller,W. and Lipman,D.J. (1997) Gapped BLAST and PSI-BLAST: a new generation of protein database search programs. Nucleic Acids Res., 25, 3389±3402. (PDF p. 8)
13. Felsenstein,J., Sawyer,S. and Kochin,R. (1982) An ef®cient method for matching nucleic acid sequences. Nucleic Acids Res., 10, 133±139. (PDF p. 8)
14. Rajasekaran,S., Jin,X. and Spouge,J.L. (2002) The ef®cient computation of position-speci®c match scores with the fast Fourier transform. J. Comput. Biol., 9, 23±33. (PDF p. 8)
15. Thompson,J.D., Plewniak,F. and Poch,O. (1999) BAliBASE: a benchmark alignment database for the evaluation of multiple alignment programs. Bioinformatics, 15, 87±88. (PDF p. 8)
16. Miyata,T., Miyazawa,S. and Yasunaga,T. (1979) Two types of amino acid substitutions in protein evolution. J. Mol. Evol., 12, 219±236. (PDF p. 8)
17. Kimura,M. (1983) The Neutral Theory of Molecular Evolution. Cambridge University Press, Cambridge, UK. (PDF p. 8)
18. Grantham,R. (1974) Amino acid difference formula to help explain protein evolution. Science, 185, 862±864. (PDF p. 8)
19. Press,W.H., Teukolsky,S.A., Vetterling,W.T. and Flannery,B.P. (1995) Numerical Recipes in C: The Art of Scienti®c Computing, 2nd Edn. Cambridge University Press, Cambridge, UK. (PDF p. 8)
20. Gotoh,O. (1995) A weighting system and algorithm for aligning many phylogenetically related sequences. Comput. Appl. Biosci., 11, 543±551. (PDF p. 8)
21. Vogt,G., Etzold,T. and Argos,P. (1995) An assessment of amino acid exchange matrices in aligning protein sequences: the twilight zone revisited. J. Mol. Biol., 249, 816±831. (PDF p. 8)
22. Jones,D.T., Taylor,W.R. and Thornton,J.M. (1992) The rapid generation of mutation data matrices from protein sequences. Comput. Appl. Biosci., 8, 275±282. (PDF p. 8)
23. Kimura,M. (1980) A simple method for estimating evolutionary rates of base substitutions through comparative studies of nucleotide sequences. J. Mol. Evol., 16, 111±120. (PDF p. 8)
24. Dayhoff,M.O., Schwartz,R.M. and Orcutt,B.C. (1978) A model of evolutionary change in proteins. In Dayhoff,M.O. and Ech,R.V. (eds), Atlas of Protein Sequence and Structure. National Biomedical Research Foundation, MD, pp. 345±352. (PDF p. 8)
25. Sokal,R.R. and Michener,C.D. (1958) A statistical mehod for evaluating systematic relationships. University of Kansas Scienti®c Bulletin, 28, 1409±1438. (PDF p. 8)
26. Tateno,Y., Ikeo,K., Imanishi,T., Watanabe,H., Endo,T., Yamaguchi,Y., Suzuki,Y., Takahashi,K., Tsunoyama,K., Kawai,M., Kawanishi,Y., Naitou,K. and Gojobori,T. (1997) Evolutionary motif and its biological and structural signi®cance. J. Mol. Evol., 44 (Suppl. 1), S38±S43. (PDF p. 8)
27. Hirosawa,M., Totoki,Y., Hoshida,M. and Ishikawa,M. (1995) Comprehensive study on iterative algorithms of multiple sequence alignment. Comput. Appl. Biosci., 11, 13±18. (PDF p. 8)
28. Stoye,J., Evers,D. and Meyer,F. (1997) Generating benchmarks for multiple sequence alignments and phylogenetic reconstructions. Proc. Int. Conf. Intell. Syst. Mol. Biol., 5, 303±306. (PDF p. 8)
29. Morgenstern,B., Dress,A. and Werner,T. (1996) Multiple DNA and protein sequence alignment based on segment-to-segment comparison. Proc. Natl Acad. Sci. USA, 93, 12098±12103. (PDF p. 8)
30. Morgenstern,B. (1999) DIALIGN2: improvement of the segment-to- segment approach to multiple sequence alignment. Bioinformatics, 15, 211±218. (PDF p. 8)
31. Smith,R.F. and Smith,T.F. (1992) Pattern-induced multi-sequence alignment (PIMA) algorithm employing secondary structure-dependent gap penalties for use in comparative protein modelling. Protein Eng., 5, 35±41. (PDF p. 8)
32. Gotoh,O. (1996) Signi®cant improvement in accuracy of multiple protein sequence alignments by iterative re®nement as assessed by reference to structural alignments. J. Mol. Biol., 264, 823±838. (PDF p. 8)
33. Maidak,B.L., Cole,J.R., Lilburn,T.G., Parker,C.T.,Jr, Saxman,P.R., Farris,R.J., Garrity,G.M., Olsen,G.J., Schmidt,T.M. and Tiedje,J.M. (2001) The RDP-II (ribosomal database project). Nucleic Acids Res., 29, 173±174. (PDF p. 8)
34. Iwabe,N., Kuma,K., Kishino,H., Hasegawa,M. and Miyata,T. (1991) Evolution of RNA polymerases and branching patterns of the three major groups of archaebacteria. J. Mol. Evol., 32, 70±78. (PDF p. 8)
35. McClure,M.A., Vasi,T.K. and Fitch,W.M. (1994) Comparative analysis of multiple protein-sequence alignment methods. Mol. Biol. Evol., 11, 571±592. (PDF p. 8)
36. Smith,T.F. and Waterman,M.S. (1981) Identi®cation of common molecular subsequences. J. Mol. Biol., 147, 195±197. (PDF p. 8)
37. Karplus,K. and Hu,B. (2001) Evaluation of protein multiple alignments by SAM-T99 using the BAliBASE multiple alignment test set. Bioinformatics, 17, 713±720. (PDF p. 8)
38. Lecompte,O., Thompson,J.D., Plewniak,F., Thierry,J. and Poch,O. (2001) Multiple alignment of complete sequences (MACS) in the post- genomic era. Gene, 270, 17±30. (PDF p. 8)
39. Nucleic Acids Research, 2002, Vol. 30 No. 14 (PDF p. 8)
