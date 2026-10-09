# Fast and sensitive multiple sequence alignments on a microcomputer

- Work ID: `w-bf6a6b1efd94`
- Asset ID: `a-bf6a6b1efd9420bc`
- Source PDF: `literature/academic-papers-processed/Fast and sensitive multiple sequence alignments on a microcomputer - Higgins, Sharp.pdf`
- SHA-256: `bf6a6b1efd9420bce16a6ef0c85c7cb71ee5634839b2e7a75824acdce7d5a1ff`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- CLUSTAL4 progressively aligns sequence groups in the branching order of an initial dendrogram. It preserves gaps from earlier alignment stages. (PDF p. 1).
- The program uses the Myers-Miller linear-space alignment method. It supports up to 100 sequences of at most 1200 residues on a microcomputer. (PDF p. 1).
- The authors report practical execution times and alignments that are difficult to improve manually. (PDF p. 3).

## Objectives

- The authors aim to align many long protein or nucleic acid sequences with useful speed and sensitivity on a microcomputer. (PDF p. 1).

## Arguments

- The earlier approximate progressive method worked well mainly for closely related sequences. Linear-space optimal pairwise alignment made a more sensitive approach practical within limited memory. (PDF p. 1).

## Analysis

- Each cluster-to-cluster position score is the arithmetic mean of all cross-cluster residue-pair weights. Direct calculation requires K times L weights for clusters with K and L sequences. (PDF p. 3).
- The authors observe approximately quadratic growth in alignment time with sequence length and approximately linear growth with sequence count. (PDF p. 3).
- For large sequence counts, the initial similarity matrix dominates execution time. A set of 90 sequences requires 4005 pairwise scores. (PDF p. 3).

## Methods

- UPGMA constructs the dendrogram from pairwise similarity scores. Each score counts exact matches in a Wilbur-Lipman alignment and subtracts a fixed penalty per gap. (PDF p. 1).
- Myers-Miller alignment recursively finds optimal alignment midpoints. This divide-and-conquer procedure uses memory proportional to sequence length. (PDF p. 2).
- Protein scoring uses a rescaled Dayhoff matrix converted to integer distances from 0 to 25. Nucleic acid distances are 0 for identity, 5 for transitions, and 10 for transversions. (PDF p. 2).
- The gap cost combines a fixed cost per gap with a cost per gap item. Earlier gaps remain fixed, and a new gap in a sequence group is scored as one gap. (PDF p. 2).

## Applications

- The authors propose automatic alignment of protein and nucleic acid sequences for evolutionary and structural comparisons. (PDF p. 1).

## Optimization

- Replacing real-number operations with 2-byte integers gives a reported 30-fold alignment speed increase on a 16-bit microcomputer without a maths coprocessor. (PDF p. 2).
- The program precomputes each cluster position's weight against each possible residue. This reduces repeated work during cluster alignment. (PDF p. 3).

## Evaluation and testing

- The FORTRAN 77 program was tested on a 10 MHz IBM AT compatible computer with 640 kbytes of memory, a hard disk, and no maths coprocessor. (PDF p. 1).
- The length benchmark used HIV pol protein fragments of 200 to 1000 residues. Its plotted alignment times exclude similarity-matrix and dendrogram calculations. (PDF p. 2).
- The sequence-count benchmark used 10 to 90 globin sequences truncated to 140 residues. It measured total time and the separate matrix, dendrogram, and alignment stages. (PDF p. 3).
- Sensitivity was assessed by how easily manual changes could improve the output alignments. (PDF p. 3).

## Results

- The authors report that execution time depends mainly on sequence length and is almost independent of other sequence characteristics. (PDF p. 3).
- The authors judge the alignments to be at least as good as outputs from the compared published methods. This judgement is qualitative. (PDF p. 3).

## Limitations and uncertainty

- Sensitivity evidence depends on manual judgement. The authors state that correct alignment of distant structural or evolutionary relationships is harder to demonstrate. (PDF p. 3).
- Interpretation: optimality of each two-group alignment does not establish optimality of the complete multiple alignment. The method follows a fixed dendrogram and preserves earlier gaps. (PDF p. 1).

## References

The reference entries need manual separation. The complete extracted reference section follows.

```text
Bains,W. (1986) MULTAN: a program lo align multiple DNA sequences.
Nucleic Acids Res.. 14, 159-177.
Barton,G.J. and Sternberg,M.J.E. (1987) A strategy for the rapid multiple
alignment of protein sequences. J. Mol. Biol., 198, 327—337.
Dayhoff.M.O. (1978) A model of evolutionary change in proteins. Matrices
for detecting distant relationships. In Dayhoff.M.O. (ed.). Atlas of Protein
Sequence and Structure. National Biomedical Research Foundation,
Washington DC, Vol. 5 Suppl. 3. pp. 345-358.
Feng,D.-F. and Doolittle,R.F. (1987) Progressive sequence alignment as a pre-
requisite to correct phylogenetic trees. J. Mol. Evol.. 25, 351—360.
Gotoh.O. (1982) An improved algorithm for matching biological sequences.
J. Mol. Biol., 162, 705-708.
Higgins,D.G. and Sharp.P.M. (1988) CLUSTAL: a package for performing
multiple sequence alignment on a microcomputer. Gene, 73, 237—244.
Hirschberg.D.S. (1975) A linear space algorithm for computing longest common
subsequences. Commun. Assoc. Comput. Much., 18, 341-343.
Myers.E.W. and Miller.W. (1988) Optimal alignments in linear space. CAB1OS,
4, 11-17.
Needleman.S.B. and Wunsch.C.D. (1970) A general method applicable to the
search for similarities in the amino acid sequence of two proteins. J. Mol.
Biol., 48, 443-453.
Santibanez.M. and Rohde.K. (1987) A multiple alignment program for protein
sequences. CABIOS, 3, 111-114.
Sneath.P.H.A. and Sokal.R.R. (1973) Numerical Taxonomy. Freeman. San
Francisco.
Sobel.E. and Martinez.H.M. (1986) A multiple sequence alignment program.
Nucleic Acids Res.. 14. 363-374.
Taylor,W.R. (1987) Multiple sequence alignment by a pairwise algorithm.
CABIOS, 3, 81-87.
Wilbur,W.J. and Lipman.D.J. (1983) Rapid similarity searches of nucleic acid
and protein data banks. Proc. Natl. Acad. Sci. USA. 80. 726-730.
Received on October 7, 1988; accepted on December 6, 1988
Circle No. 10 on Reader Enquiry Card
153
by
guest
on
October
30,
2015
http://bioinformatics.oxfordjournals.org/
Downloaded
from
```
