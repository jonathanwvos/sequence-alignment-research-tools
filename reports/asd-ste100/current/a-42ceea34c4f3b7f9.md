# Multiple sequence alignment with the Clustal series of programs

- Work ID: `w-42ceea34c4f3`
- Asset ID: `a-42ceea34c4f3b7f9`
- Source PDF: `literature/academic-papers-processed/Multiple sequence alignment with the Clustal series of programs - Chenna et al.pdf`
- SHA-256: `42ceea34c4f3b7f90771d15e2b8e281a755be646acafec362c4f9f9d8f91494f`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The Clustal programs construct multiple alignments of protein and nucleic acid sequences and calculate phylogenetic trees. (PDF p. 1).
- ClustalW uses progressive alignment with sequence weighting, position-specific gap penalties, and automatic selection of residue comparison matrices. (PDF p. 1).
- ClustalW and ClustalX version 1.83 add output options and a faster neighbour-joining implementation. (PDF p. 3).

## Objectives

- The developers aim to provide robust, portable programs that produce biologically accurate alignments within reasonable time limits. (PDF p. 1).
- ClustalX supports interactive alignment assessment through conserved-column highlighting and tools that identify possible alignment errors. (PDF p. 1).

## Arguments

- The authors attribute Clustal's use to accuracy, robustness, portability, and ease of use. (PDF p. 1).
- The authors state that users need access to alignment parameters because defaults are not optimal for every problem. (PDF p. 2).

## Analysis

- ClustalX produces the same alignments as the corresponding ClustalW release. Its interface adds tools for inspection and assessment. (PDF p. 1).
- The timing analysis separates neighbour-joining from complete alignment. Neighbour-joining time depends on sequence count, while complete alignment time also depends on sequence length. (PDF p. 3).

## Methods

- Clustal builds a multiple alignment through successive pairwise alignments in guide-tree order. The original implementation combined progressive alignment with memory-efficient dynamic programming. (PDF p. 1).
- ClustalW replaced the initial word-based comparison with dynamic programming and replaced UPGMA guide-tree construction with neighbour-joining. (PDF p. 1).
- ClustalV introduced profile alignment, which aligns existing alignments, and neighbour-joining trees derived from completed multiple alignments. (PDF p. 1).
- ClustalWWW displays conservation symbols and residue colours. It can calculate neighbour-joining trees and display them as cladograms or phylograms. (PDF p. 3).

## Applications

- Multiple alignments support the study of conserved sequence patterns and evolutionary relationships. (PDF p. 1).
- ClustalX permits realignment of selected sequences or blocks. Users can construct difficult alignments in stages. (PDF p. 2).
- DbClustal uses local alignment information to anchor global alignments of sequences found by database searches. (PDF p. 2).
- Residue-range output supports extraction of individual domains from alignments of multidomain proteins. (PDF p. 3).

## Optimization

- Parallel ClustalW and ClustalX implementations reportedly achieved speed increases of up to tenfold on 16 CPUs. (PDF p. 2).
- Version 1.83 uses a faster neighbour-joining implementation for both alignment guide trees and phylogenetic trees. (PDF p. 3).
- The Gonnet series became the default residue comparison matrices for protein alignment after parameter optimization. (PDF p. 3).

## Evaluation and testing

- Table 2 compares original and new neighbour-joining implementations at 200, 500, and 1,000 sequences. Tests ran on a Compaq Alpha EV67 with True64 UNIX. (PDF p. 3).
- The timing comparison measures neighbour-joining without distance-matrix calculation and also measures complete multiple alignment. (PDF p. 3).
- A separate example calculates a tree from more than 1,100 PFAM ring finger domain sequences. (PDF p. 3).

## Results

- ClustalW 1.83 calculated a tree for more than 1,100 ring finger domains in 22 seconds on a 1 GHz Pentium III. This time included distance-matrix calculation. (PDF p. 2).
- Version 1.83 added FASTA alignment output, percent identity matrices, and residue ranges in selected alignment output. (PDF p. 3).
- The authors report that the faster neighbour-joining implementation made large tree calculations feasible on smaller computer systems. (PDF p. 3).

## Limitations and uncertainty

- Default alignment parameters can be unsuitable for a specific alignment problem. (PDF p. 2).
- Large web submissions can exceed job runtime limits. The authors advise local execution when this occurs. (PDF p. 2).
- The authors state that the accelerated neighbour-joining implementations remove major code bottlenecks but do not provide a combinatorial improvement. (PDF p. 4).

## References

1. Higgins,D.G. and Sharp,P.M. (1988) CLUSTAL: a package for performing multiple sequence alignment on a microcomputer. Gene, 73, 237–244. (PDF p. 4)
2. Myers,E.W. and Miller,W. (1988) Optimal alignments in linear space. Comput. Applic. Biosci., 4, 11–17. (PDF p. 4)
3. Feng,D.F. and Doolittle,R.F. (1987) Progressive sequence alignment as a prerequisite to correct phylogenetic trees. J. Mol. Evol., 25, 351–360. (PDF p. 4)
4. Taylor,W.R. (1988) A flexible method to align large numbers of biological sequences. J. Mol. Evol., 28, 161–169. (PDF p. 4)
5. Wilbur,W.J. and Lipman,D.J. (1983) Rapid similarity searches of nucleic acid and protein data banks. Proc. Natl Acad. Sci. USA, 80, 726–730. (PDF p. 4)
6. Sneath,P.H.A. and Sokal,R.R. (1973) Numerical Taxonomy. WH Freeman, San Francisco, CA, pp. 230–234. (PDF p. 4)
7. Higgins,D.G. (1994) CLUSTAL V: multiple alignment of DNA and protein sequences. Methods Mol. Biol., 25, 307–318. (PDF p. 4)
8. Higgins,D.G., Bleasby,A.J. and Fuchs,R. (1992) CLUSTAL V: improved software for multiple sequence alignment. Comput. Appl. Biosci., 8, 189–191. (PDF p. 4)
9. Saitou,N. and Nei,M. (1987) The neighbor-joining method: a new method for reconstructing phylogenetic trees. Mol. Biol. Evol., 4, 406–425. (PDF p. 4)
10. Thompson,J.D., Higgins,D.G. and Gibson,T.J. (1994) CLUSTAL W: improving the sensitivity of progressive multiple sequence alignment through sequence weighting, position-specific gap penalties and weight matrix choice. Nucleic Acids Res., 22, 4673–4680. (PDF p. 4)
11. Thompson,J.D., Gibson,T.J., Plewniak,F., Jeanmougin,F. and Higgins,D.G. (1997) The CLUSTAL_X windows interface: flexible strategies for multiple sequence alignment aided by quality analysis tools. Nucleic Acids Res., 25, 4876–4882. (PDF p. 4)
12. Compagne,F. (2000) Clustalnet: the joining of Clustal and CORBA. Bioinformatics, 16, 606–612. (PDF p. 4)
13. Thompson,J.D., Plewniak,F., Thierry,J. and Poch,O. (2000) DbClustal: rapid and reliable global multiple alignments of protein sequences detected by database searches. Nucleic Acids Res., 28, 2919–2926. (PDF p. 4)
14. Maddison,D.R., Swofford,D.L. and Maddison,W.P. (1997) NEXUS: an extensible file format for systematic information, Syst. Biol., 46, 590–621. (PDF p. 4)
15. Benner,S.A., Cohen,M.A. and Gonnet,G.H. (1994) Amino acid substitution during functionally constrained divergent evolution of protein sequences. Protein Eng., 7, 1323–1332. (PDF p. 4)
16. Bateman,A., Birney,E., Cerruti,L., Durbin,R., Etwiller,L., Eddy,S.R., Griffiths-Jones,S., Howe,K.L., Marshall,M. and Sonnhammer,E.L. (2002) The Pfam protein families database. Nucleic Acids Res., 1, 276–280. (PDF p. 4)
17. Howe,K., Bateman,A. and Durbin,R. (2002) Quick Tree: building huge Neighbour-Joining trees of protein sequences. Bioinformatics, 11, 1546–1547. (PDF p. 4)
18. Perrière,G. and Gouy,M. (1996) WWW-Query: an on-line retrieval system for biological sequence banks. Biochimie, 78, 364–369. (PDF p. 4)
19. Nucleic Acids Research, 2003, Vol. 31, No. 13 (PDF p. 4)
