# Improvement in accuracy of multiple sequence alignment using novel group-to-group sequence alignment algorithm with piecewise linear gap cost

- Work ID: `w-c1d2de4c1a0e`
- Asset ID: `a-c1d2de4c1a0ef5a9`
- Source PDF: `literature/academic-papers-processed/Improvement in accuracy of multiple sequence alignment using novel group-to-group sequence alignment algorithm with piecewise linear gap cost - Yamada et al.pdf`
- SHA-256: `c1d2de4c1a0ef5a9bc63c9239b163c2b03431995a8396fb87d09318b1a94b959`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- PRIME uses group-to-group alignment with a piecewise linear gap cost to improve multiple sequence alignment. (PDF p. 1).
- The method combines gap profiles with randomized iterative refinement of a weighted sum-of-pairs objective. (PDF p. 8).
- The authors report accuracy comparable to leading programs on BAliBASE 3.0 and PREFAB 4.0. (PDF p. 1).

## Objectives

- The authors aim to reduce excessive penalties for long insertions and deletions in group-to-group alignment. (PDF p. 2).
- They seek accurate alignment without incorporating all-by-all pairwise alignment information into the alignment scoring system. (PDF p. 2).

## Arguments

- The authors argue that affine-like gap costs can reduce global alignment accuracy when sequences contain long indels. (PDF p. 2).
- A piecewise linear concave gap cost changes the gap extension penalty with gap length. (PDF p. 2).
- Exact group-to-group optimization requires alternative partial paths. Their number can grow exponentially, which motivates omission of the candidate list. (PDF p. 3).

## Analysis

- The authors attribute the larger benefit on full-length sequences to better treatment of long terminal gaps. Trimming non-homologous ends reduces the difference between gap costs. (PDF p. 10).
- Interpretation: the claim about avoiding pairwise alignment information concerns alignment scoring. PRIME still uses pairwise alignment to calculate its initial distance matrix. (PDF p. 8).
- The authors interpret similar benchmark accuracy as evidence that piecewise linear gap costs can provide benefits comparable to pairwise alignment information. (PDF p. 2).

## Methods

- An insertion length profile stores information for each group column. Dynamic gap information tracks gaps inserted during dynamic programming. (PDF p. 2).
- Gap extension calculations account for dynamic gaps that overlap only part of a target gap. The method evaluates residue-to-gap alignments in both group directions. (PDF p. 8).
- PRIME constructs a progressive initial alignment, then repeatedly updates distances, a phylogenetic tree, and pair weights. (PDF p. 8).
- Each refinement splits the alignment at a randomly selected tree branch and realigns the two groups. Refinement stops when the weighted sum-of-pairs score no longer improves. (PDF p. 8).

## Applications

- The group-to-group algorithm serves as a component of progressive alignment and iterative refinement. (PDF p. 2).
- The method targets protein families with long internal or terminal indels. (PDF p. 1).

## Optimization

- PRIME optimizes a weighted sum-of-pairs objective with a simpler dynamic programming method. It omits candidate lists and anchoring heuristics. (PDF p. 8).
- Substitution matrix selection and gap cost parameters were tuned on BAliBASE 2.01. (PDF p. 8).
- Running gap state profiles support efficient calculation of gap extension penalties from dynamic gap information. (PDF p. 8).

## Evaluation and testing

- Tests use BAliBASE 3.0 and PREFAB 4.0. PREFAB tests include pairwise controls with affine and piecewise linear gap costs. (PDF p. 8).
- BAliBASE evaluation compares sum-of-pairs and column scores for full-length and homologous-region sets. Friedman rank sums assess consistency across tests. (PDF p. 10).
- PREFAB quality scores measure recovery of reference residue pairs for two proteins with known structures. (PDF p. 10).
- Timing tests use a 933 MHz Pentium III with 1 GB of memory and RedHat Linux 7.3. (PDF p. 10).

## Results

- The most accurate BAliBASE full-length group includes both PRIME variants, MAFFT, ProbCons, and T-Coffee. (PDF p. 10).
- Piecewise PRIME performs better than affine PRIME on full-length data, but the difference is not statistically significant. (PDF p. 10).
- The two PRIME variants show little accuracy difference on the homologous-region set. (PDF p. 10).
- PREFAB main and long-gap sets show performance patterns similar to BAliBASE. All programs except POA have comparable performance on the weighting set. (PDF p. 10).

## Limitations and uncertainty

- PRIME omits the candidate list required for rigorous global optimization of group-to-group alignment. (PDF p. 3).
- The authors estimate that the new group-to-group method needs roughly twice the computation time of the previous method for each dynamic programming process. (PDF p. 3).
- About 20% of BAliBASE 3.0 sequences overlap the parameter-tuning set. The authors consider substantial overfitting unlikely. (PDF p. 8).
- Piecewise PRIME handles terminal non-homologous regions better than conventional global programs, but less well than programs that incorporate local alignment information. (PDF p. 10).

## References

1. Gotoh O: Multiple sequence alignment: algorithms and appli- cations. Adv Biophys 1999, 36:159-206. (PDF p. 17)
2. Notredame C: Recent progress in multiple sequence align- ment: a survey. Pharmacogenomics 2002, 3:131-144. (PDF p. 17)
3. Gotoh O, Yamada S, Yada T: Multiple sequence alignment. In Handbook of computational molecular biology, Computer and Information Science Series Edited by: Aluru S. Chapman & Hall/CRC; 2005:3–1-3– 36. (PDF p. 17)
4. Jiang T, Wang L: Algorithmic methods for multiple sequence alignment. In Current topics in computational molecular biology Edited by: Jiang T, Xu Y, Zhang MQ. Tsinghua University Press; 2002. (PDF p. 17)
5. Grasso C, Lee C: Combining partial order alignment and pro- gressive multiple sequence alignment increases alignment speed and scalability to very large alignment problems. Bio- informatics 2004, 20:1546-1556. (PDF p. 17)
6. Notredame C, Higgins DG, Heringa J: T-Coffee: A novel method for fast and accurate multiple sequence alignment. J Mol Biol 2000, 302:205-217. (PDF p. 17)
7. Thompson JD, Higgins DG, Gibson TJ: CLUSTAL W: improving the sensitivity of progressive multiple sequence alignment through sequence weighting, position-specific gap penalties and weight matrix choice. Nucleic Acids Res 1994, 22:4673-4680. (PDF p. 17)
8. Edgar RC: MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic Acids Res 2004, 32:1792-1797. (PDF p. 17)
9. Gotoh O: Significant improvement in accuracy of multiple protein sequence alignments by iterative refinement as assessed by reference to structural alignments. J Mol Biol 1996, 264:823-838. (PDF p. 17)
10. Katoh K, Misawa K, Kuma K, Miyata T: MAFFT: a novel method for rapid multiple sequence alignment based on fast Fourier transform. Nucleic Acids Res 2002, 30:3059-3066. (PDF p. 17)
11. Kececioglu J, Starrett D: Aligning alignments exactly. In Proceed- ings of the Eighth Annual International Conference on Research in Compu- tational Molecular Biology: 27–31 March 2004 Edited by: Bourne PE. San Diego, ACM; 2004:85-96. (PDF p. 17)
12. Gotoh O: Optimal alignment between groups of sequences and its application to multiple sequence alignment. Comput Appl Biosci 1993, 9:361-370. (PDF p. 17)
13. McClure MA, Vasi TK, Fitch WM: Comparative analysis of mul- tiple protein-sequence alignment methods. Mol Biol Evol 1994, 11:571-592. (PDF p. 17)
14. Thompson JD, Plewniak F, Poch O: A comprehensive compari- son of multiple sequence alignment programs. Nucleic Acids Res 1999, 27:2682-2690. (PDF p. 17)
15. Katoh K, Kuma K, Toh H, Miyata T: MAFFT version 5: improve- ment in accuracy of multiple sequence alignment. Nucleic Acids Res 2005, 33:511-518. (PDF p. 17)
16. Do CB, Mahabhashyam MSP, Brudno M, Batzoglou S: ProbCons: Probabilistic consistency-based multiple sequence align- ment. Genome Res 2005, 15:330-340. (PDF p. 17)
17. Miller W, Myers EW: Sequence comparison with concave weighting functions. Bull Math Biol 1988, 50:97-120. (PDF p. 17)
18. Gotoh O: Optimal sequence alignment allowing for long gaps. Bull Math Biol 1990, 52:359-373. (PDF p. 17)
19. Gotoh O: Further improvement in methods of group-to- group sequence alignment with generalized profile opera- tions. Comput Appl Biosci 1994, 10:379-387. (PDF p. 17)
20. Gotoh O: A weighting system and algorithm for aligning many phylogenetically related sequences. Comput Appl Biosci 1995, 11:543-551. (PDF p. 17)
21. Gotoh O: An improved algorithm for matching biological sequences. J Mol Biol 1982, 162:705-708. (PDF p. 17)
22. Bahr A, Thompson JD, Thierry JC, Poch O: BAliBASE (Bench- mark Alignment dataBASE): enhancements for repeats, transmembrane sequences and circular permutations. Nucleic Acids Res 2001, 29:323-326. (PDF p. 17)
23. Thompson JD, Koehl P, Ripp R, Poch O: BAliBASE 3.0: Latest developments of the multiple sequence alignment bench- mark. Proteins 2005, 61:127-136. (PDF p. 17)
24. PRIME [http://prime.cbrc.jp/] (PDF p. 17)
25. Thompson JD, Plewniak F, Poch O: BAliBASE: a benchmark alignment database for the evaluation of multiple alignment programs. Bioinformatics 1999, 15:87-88. (PDF p. 17)
26. Karplus K, Hu B: Evaluation of protein multiple alignments by SAM-T99 using the BAliBASE multiple alignment test set. Bioinformatics 2001, 17:713-720. (PDF p. 17)
27. O'Sullivan O, Suhre K, Abergel C, Higgins DG, Notredame C: 3DCoffee: combining protein sequences and structures within multiple sequence alignments. J Mol Biol 2004, 340:385-395. (PDF p. 17)
28. Subramanian AR, Weyer-Menkhoff J, Kaufmann M, Morgenstern B: DIALIGN-T: an improved algorithm for segment-based mul- tiple sequence alignment. BMC Bioinformatics 2005, 6:66. Additional File 2 p-values of the Friedman test of full length set. Each value is p-value of the Friedman test, indicating the significance of a difference in per- formance between programs of a row and a column. The upper right and lower left p-values are calculated using sum-of-pairs and column scores on all alignments of the whole full length set, respectively. PRIMEpcw denotes PRIMEpiecewise, and PRIMEafn, PRIMEaffine. The respective signs + and - denote that a program of a row performs significantly better and worse than that of a column. Click here for file [http://www.biomedcentral.com/content/supplementary/1471- 2105-7-524-S2.pdf] Additional File 3 p-values of the Friedman test of homologous region set. Each value is p-value of the Friedman test, indicating the significance of a difference in performance between programs of a row and a column. The upper right and lower left p-values are calculated using sum-of-pairs and column scores on all alignments of the whole homologous region set, respectively. PRIMEpcw denotes PRIMEpiecewise, and PRIMEafn, PRIMEaffine. The respective signs + and - denote that a program of a row performs signifi- cantly better and worse than that of a column. Click here for file [http://www.biomedcentral.com/content/supplementary/1471- 2105-7-524-S3.pdf] (PDF p. 17)
