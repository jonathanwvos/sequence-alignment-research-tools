# MAFFT version 5: improvement in accuracy of multiple sequence alignment

- Work ID: `b-3e037d156eff`
- Asset ID: `a-bafd9dc137b30dfc`
- Source PDF: `literature/academic-papers-processed/MAFFT version 5: improvement in accuracy of multiple sequence alignment - Katoh et al.pdf`
- SHA-256: `bafd9dc137b30dfc2bae0c6b801d39aaca7573423a9e02b40cd0caa5f9eeb096`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- MAFFT 5.3 adds G-INS-i, H-INS-i, and F-INS-i. These options combine pairwise alignment information with iterative refinement. (PDF p. 1).
- The authors report improved accuracy for alignments with dozens of sequences. Adding close homologues also improved many alignments of distantly related sequences. (PDF p. 6).

## Objectives

- Improve alignment accuracy through parameter selection and pairwise alignment information while keeping computation practical. (PDF p. 3).
- Measure how additional homologues affect the accuracy of alignments of distantly related sequences. (PDF p. 3).

## Arguments

- The authors expect additional homologues to reduce noise in alignment. They test this expectation with extended reference datasets. (PDF p. 3).
- The authors argue that support for many sequences matters because added homologues can improve alignment accuracy. (PDF p. 7).

## Analysis

- The importance value combines each gap-free segment's score with weighted frequencies of residue participation in such segments. (PDF p. 3).
- The refinement objective adds importance values to the weighted sum-of-pairs score. The importance weight is 2.7 in the reported version. (PDF p. 4).
- The authors suggest that position-specific gap penalties help exploit added homologues. Disabling this feature reduced the observed improvement. (PDF p. 7).

## Methods

- G-INS-i uses global pairwise alignments with an FFT approximation. H-INS-i uses FASTA with Smith–Waterman optimization. F-INS-i uses FASTA without that optimization. (PDF p. 3).
- Pairwise scores produce a distance matrix and a modified UPGMA guide tree. Pairwise alignments are split into gap-free segments with stored scores, lengths, positions, and importance values. (PDF p. 3).
- Dynamic programming aligns groups using substitution scores and importance values. Iterative refinement then optimizes the WSP+I objective. (PDF p. 4).

## Applications

- The mafftE.rb script collects homologues from a local database or SwissProt through NCBI-BLAST and aligns them with the input sequences. (PDF p. 4).

## Optimization

- Golden section search tuned gap-opening and offset parameters on TWIf+0 with FFT-NS-2. Five scoring matrices were compared. (PDF p. 4).
- The selected parameters were Sop = 1.53 and Sa = 0.123 with BLOSUM62. The authors report an accuracy gain of about five percentage points over the previous settings. (PDF p. 5).
- Highly conserved regions are anchored and excluded from repeated alignment. Their detection uses sequence similarity without the importance matrix. (PDF p. 4).
- FASTA banded alignment and the FFT approximation reduce pairwise alignment time. The FFT benefit is limited to highly conserved sequences. (PDF p. 5).

## Evaluation and testing

- HOM+0 contains 55 structural reference alignments from HOMSTRAD. Extended sets add up to 20, 50, or 100 BLAST homologues at E < 10^-10. Added sequences are removed before column accuracy is scored. (PDF p. 4).
- SABmark 1.65 tests use fD and separate family pairs from superfamily pairs. PREFAB version 3 uses Q, the fraction of reference residue pairs recovered. (PDF p. 4).
- ROSE simulations vary sequence length or sequence count at 100 and 250 PAM. Length tests use 40 sequences. Count tests use average length 300. (PDF p. 2).
- Comparisons include TCoffee 2.02, CLUSTAL W 1.83, PROBCONS 1.06, and MUSCLE 3.41. Tests ran on a 2.8 GHz Xeon with 1 GB RAM, SuSE Linux 9.0, and gcc 3.3.1 with -O3. (PDF p. 4).

## Results

- On HOM+50, G-INS-i reached 53.85% column accuracy in 514.2 seconds. TCoffee reached 49.71% in 28,250 seconds. Both Wilcoxon and Friedman tests supported the G-INS-i gain over HOM+0. (PDF p. 5).
- On TWI+50, G-INS-i reached 29.58% fD for superfamily pairs and 51.11% for family pairs. Its gains over TWI+0 were 8.85 and 9.43 percentage points. (PDF p. 6).
- The new options improved accuracy over FFT-NS-i by at most six percentage points in the reported benchmarks. (PDF p. 5).
- PROBCONS exceeded the new options by one to three percentage points on BAliBASE. The new options exceeded PROBCONS by one to three points on SABmark SUP. (PDF p. 6).

## Limitations and uncertainty

- FFT-NS-2 parameters were tuned on TWIf+0. The authors therefore stress comparisons on other datasets. (PDF p. 5).
- The best importance weight depends on homologue count, similarity, and other conditions. Further parameter investigation is needed. (PDF p. 5).
- The authors expect G-INS-i to perform poorly with large gaps because it uses global pairwise alignments. (PDF p. 5).
- Accepting every refinement without checking WSP+I can worsen the objective. This shortcut reduced accuracy for small alignments in the tests. (PDF p. 6).

## References

1. Katoh,K., Misawa,K., Kuma,K. and Miyata,T. (2002) MAFFT: a novel method for rapid multiple sequence alignment based on fast Fourier transform. Nucleic Acids Res., 30, 3059–3066. (PDF p. 7)
2. Grasso,C. and Lee,C. (2004) Combining partial order alignment and progressive multiple sequence alignment increases alignment speed and scalability to very large alignment problems. Bioinformatics, 20, 1546–1556. (PDF p. 7)
3. Bateman,A., Coin,L., Durbin,R., Finn,R.D., Hollich,V., Griffiths- Jones,S., Khanna,A., Marshall,M., Moxon,S., Sonnhammer,E.L., Studholme,D.J., Yeats,C. and Eddy,S.R. (2004) The pfam protein families database. Nucleic Acids Res., 32, D138–D141. (PDF p. 7)
4. Chandonia,J.M., Hon,G., Walker,N.S., Lo Conte,L., Koehl,P., Levitt,M. and Brenner,S.E. (2004) The ASTRAL compendium in 2004. Nucleic Acids Res., 32, D189–D192. (PDF p. 7)
5. Rawlings,N.D., Tolle,D.P. and Barrett,A.J. (2004) MEROPS: the peptidase database. Nucleic Acids Res., 32, D160–D164. (PDF p. 7)
6. Feng,D.F. and Doolittle,R.F. (1987) Progressive sequence alignment as a prerequisite to correct phylogenetic trees. J. Mol. Evol., 25, 351–360. (PDF p. 7)
7. Thompson,J.D., Higgins,D.G. and Gibson,T.J. (1994) CLUSTAL W: improving the sensitivity of progressive multiple sequence alignment through sequence weighting, position-specific gap penalties and weight matrix choice. Nucleic Acids Res., 22, 4673–4680. (PDF p. 7)
8. Berger,M.P. and Munson,P.J. (1991) A novel randomized iterative strategy for aligning multiple protein sequences. Comput. Appl. Biosci., 7, 479–484. (PDF p. 7)
9. Gotoh,O. (1993) Optimal alignment between groups of sequences and its application to multiple sequence alignment. Comput. Appl. Biosci., 9, 361–370. Table 4. Accuracy values of several methods for the PREFAB tests Method Identity (%) CPU 0–20 20–40 40–70 70–100 All time (s) G-INS-i 46.75 82.77 96.30 98.60 68.85 16 030 H-INS-i 48.22 83.32 95.83 98.64 69.70 15 060 F-INS-i 48.00 83.35 95.83 98.62 69.61 9007 H-INS-1 46.13a 82.16a 95.42b 98.60 68.27 9910 FFT-NS-i 45.72a 80.95a 93.83b 98.55 67.48 4176 FFT-NS-2 43.19a 79.52a 93.23b 98.47 65.74 930.4 FFT-NS-1 40.90a 77.50a 93.46a 98.59 63.92 666.2 TCoffee 2.02 45.30a 82.36b 95.20 98.62 67.96 973 600 PROBCONS 1.06 45.63b 82.10 95.01b 98.18 67.95 142 200 MUSCLE-i 42.77a 80.43a 95.43 98.28 66.05 13 260 MUSCLE-fast 38.44a 76.65a 93.42a 97.91 62.44 544.1 CLUSTAL W (default) 33.96a 74.14a 93.54b 97.85 59.45 12 970 CLUSTAL W (default), default. The highest accuracy value within each percent identity range is in bold letters. a The difference from the highest accuracy was found to be significant (P < 0.01) by both the Wilcoxon test and the Friedman test. b The Wilcoxon test showed a significant difference but the Friedman test did not.SeeTable 1forcommand-lineoptionsforeachstrategyin MAFFT.Options of other programs are as follows: TCoffee, default; PROBCONS, default; MUSCLE-i, muscle -maxiters 1000; MUSCLE-fast, muscle -sv -maxiters 1 -diags1 -distance1 kbit20_3; Nucleic Acids Research, 2005, Vol. 33, No. 2 517 Downloaded from https://academic.oup.com/nar/article/33/2/511/2549118 by University of Cape Town, Medical Library user on 30 March 2026 (PDF p. 7)
10. Jones,D.T., Taylor,W.R. and Thornton,J.M. (1992) The rapid generation of mutation data matrices from protein sequences. Comput. Appl. Biosci., 8, 275–282. (PDF p. 8)
11. Edgar,R.C. (2004) MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic Acids Res., 32, 1792–1797. (PDF p. 8)
12. Sokal,R.R. and Michener,C.D. (1958) A statistical method for evaluating systematic relationships. Univ. Kans. Scientif. Bull., 28, 1409–1438. (PDF p. 8)
13. Tateno,Y., Ikeo,K., Imanishi,T., Watanabe,H., Endo,T., Yamaguchi,Y., Suzuki,Y., Takahashi,K., Tsunoyama,K., Kawai,M., Kawanishi,Y., Naitou,K. and Gojobori,T. (1997) Evolutionary motif and its biological and structural significance. J. Mol. Evol., 44, S38–S43. (PDF p. 8)
14. Gotoh,O. (1995) A weighting system and algorithm for aligning many phylogenetically related sequences. Comput. Appl. Biosci., 11, 543–551. (PDF p. 8)
15. Hirosawa,M., Totoki,Y., Hoshida,M. and Ishikawa,M. (1995) Comprehensive study on iterative algorithms of multiple sequence alignment. Comput. Appl. Biosci., 11, 13–18. (PDF p. 8)
16. Needleman,S.B. and Wunsch,C.D. (1970) A general method applicable to the search for similarities in the amino acid sequence of two proteins. J. Mol. Biol., 48, 443–453. (PDF p. 8)
17. Stebbings,L.A. and Mizuguchi,K. (2004) HOMSTRAD: recent developments of the homologous protein structure alignment database. Nucleic Acids Res., 32, D203–D207. (PDF p. 8)
18. Van Walle,I., Lasters,I. and Wyns,L. (2004) Align-m—a new algorithm for multiple alignment of highly divergent sequences. Bioinformatics, 20, 1428–1435. (PDF p. 8)
19. Gotoh,O.(1996)Significantimprovementinaccuracyofmultipleprotein sequence alignments by iterative refinement as assessed by reference to structural alignments. J. Mol. Biol., 264, 823–838. (PDF p. 8)
20. Notredame,C., Higgins,D.G. and Heringa,J. (2000) T-Coffee: a novel method for fast and accurate multiple sequence alignment. J. Mol. Biol., 302, 205–217. (PDF p. 8)
21. Lassmann,T. and Sonnhammer,E.L. (2002) Quality assessment of multiple alignment programs. FEBS Lett., 529, 126–130. (PDF p. 8)
22. Raghava,G.P., Searle,S.M., Audley,P.C., Barber,J.D. and Barton,G.J. (2003) OXBench: a benchmark for evaluation of protein multiple sequence alignment accuracy. BMC Bioinformatics, 4, 47. (PDF p. 8)
23. Edgar,R.C. (2004) MUSCLE: a multiple sequence alignment method with reduced time and space complexity. BMC Bioinformatics, 5, 113. (PDF p. 8)
24. Thompson,J.D., Plewniak,F., Thierry,J. and Poch,O. (2000) DbClustal: rapid and reliable global multiple alignments of protein sequences detected by database searches. Nucleic Acids Res., 28, 2919–2926. (PDF p. 8)
25. Pearson,W.R. and Lipman,D.J. (1988) Improved tools for biological sequence comparison. Proc. Natl Acad. Sci. USA, 85, 2444–2448. (PDF p. 8)
26. O’Sullivan,O., Suhre,K., Abergel,C., Higgins,D.G. and Notredame,C. (2004) 3DCoffee: combining protein sequences and structures within multiple sequence alignments. J. Mol. Biol., 340, 385–395. (PDF p. 8)
27. Altschul,S.F., Madden,T.L., Schaffer,A.A., Zhang,J., Zhang,Z., Miller,W. and Lipman,D.J. (1997) Gapped BLAST and PSI-BLAST: a new generation of protein database search programs. Nucleic Acids Res., 25, 3389–3402. (PDF p. 8)
28. Press,W.H., Teukolsky,S.A., Vetterling,W.T. and Flannery,B.P. (1995) Numerical Recipes in C: The Art of Scientific Computing, 2nd edn. Cambridge University Press, Cambridge. (PDF p. 8)
29. Stoye,J., Evers,D. and Meyer,F. (1997) Generating benchmarks for multiple sequence alignments and phylogenetic reconstructions. Proc. Int. Conf. Intell. Syst. Mol. Biol., 5, 303–306. (PDF p. 8)
30. Thompson,J.D., Plewniak,F. and Poch,O. (1999) BAliBASE: a benchmark alignment database for the evaluation of multiple alignment programs. Bioinformatics, 15, 87–88. (PDF p. 8)
31. Nucleic Acids Research, 2005, Vol. 33, No. 2 Downloaded from https://academic.oup.com/nar/article/33/2/511/2549118 by University of Cape Town, Medical Library user on 30 March 2026 (PDF p. 8)
