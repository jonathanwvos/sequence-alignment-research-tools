# Measuring the distance between multiple sequence alignments

- Work ID: `w-4dfea2a0db47`
- Asset ID: `a-4dfea2a0db47d11c`
- Source PDF: `literature/academic-papers-processed/Measuring the distance between multiple sequence alignments - Blackburne, Whelan.pdf`
- SHA-256: `4dfea2a0db47d11cb9172d3a18a8bc36b24d9aa4db79af169feb00ccf7a411dd`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Blackburne and Whelan introduce four metrics for comparing multiple sequence alignments. The metrics use different amounts of gap information. (PDF p. 1).
- The study compares alignment methods on BAliBASE data and INDELible simulations. (PDF p. 1).
- The metrics reveal differences between inferred alignments even when their distances from a reference are similar. (PDF p. 7).

## Objectives

- Define valid alignment distances that can include gap positions and inferred indel locations on a phylogenetic tree. (PDF p. 1).
- Use these distances to study differences between alignment methods and changes in performance with evolutionary divergence. (PDF p. 2).

## Arguments

- The authors state that SP and TC scores violate symmetry and the triangle inequality. These scores therefore do not provide valid metric spaces for alignment comparison. (PDF p. 1).
- The authors argue that combined metrics can distinguish changes in residue pairing, gap position, and inferred indel history. (PDF p. 7).

## Analysis

- dSSP uses Jaccard distance over residue homology sets. The gap-aware metrics use normalized symmetric differences with constant set sizes, then average across observed characters. (PDF p. 3).
- The gap-aware distances lie between zero and one. They describe the chance that a sampled residue has a different alignment assignment against another sampled sequence. (PDF p. 3).
- The definitions enforce d_evol ≥ d_pos ≥ d_seq. dSSP is not part of this ordering. (PDF p. 5).
- For dSSP, a local change has a smaller effect when the alignment contains more residue pairings elsewhere. (PDF p. 3).

## Methods

- SSP ignores gaps. seq labels gaps by sequence, pos also labels their sequence position, and evol also labels the inferred tree edge of the indel. (PDF p. 2).
- For evol, each column receives a Dollo-parsimony history with at most one insertion and any number of deletions. (PDF p. 2).
- The procedure sorts sequence names and non-overlapping columns to give equivalent alignments a unique representation. (PDF p. 2).
- The study computes all pairwise alignment distances and displays mean distance matrices as heatmaps. evol uses RAxML reference trees for BAliBASE and generating trees for simulations. (PDF p. 3).

## Applications

- Sequence-wise distances can identify sequences whose placement differs strongly between alignments. (PDF p. 3).
- The authors propose comparing alternative alignments to study downstream inference, alignment uncertainty, and algorithm bias. (PDF p. 7).
- The authors provide the metrics in MetAl, a Haskell implementation. (PDF p. 1).

## Optimization

- Treating each gap position independently permits simple and efficient inference of indel locations on the tree. (PDF p. 2).
- Constant homology-set sizes for the gap-aware recodings permit fixed normalization of their symmetric differences. (PDF p. 3).

## Evaluation and testing

- The comparison uses ClustalW, Muscle, DIALIGN–TX, T–Coffee, ProbCons, two MAFFT modes, and Prank with +F. Other settings are defaults. (PDF p. 3).
- The BAliBASE sample contains 20 randomly selected alignments from each of RV12, RV30, and RV50. Full and homologous-region versions contain 4–142 sequences. (PDF p. 3).
- INDELible v1.03 simulations use balanced and unbalanced eight-leaf trees at six total tree lengths. Each setting has 20 replicates and a root sequence length of 1000. (PDF p. 3).
- Simulations use WAG substitutions, an indel rate of 0.1, and a power-law indel length distribution with parameter 1.7. Inferred alignments are compared with the known true alignments. (PDF p. 3).

## Results

- On simulations with tree length 1.4, Prank performs best under d_evol. MAFFT L–INS–i also performs well, while ClustalW performs worse than the other methods. (PDF p. 5).
- With increasing divergence, d_seq peaks near total tree length four, then levels off or decreases. d_evol continues to increase because it distinguishes gap positions and inferred events. (PDF p. 5).
- Sequence-wise errors are broadly similar on balanced trees. On unbalanced trees, sequences on longer terminal branches are harder to align. (PDF p. 5).
- On RV12, d_pos and d_evol are approximately equal. The authors infer that different gap placements rarely change the inferred indel history in this dataset. (PDF p. 7).

## Limitations and uncertainty

- The recoding assumes no evolutionary direction and cannot distinguish insertions from deletions. Independent treatment of gap positions is a biological simplification. (PDF p. 2).
- The comparison uses default aligner settings to demonstrate metric behavior. The authors do not present it as a definitive ranking of alignment quality. (PDF p. 3).
- The authors note that Prank's strong simulation performance may reflect similarity between its alignment model and the INDELible generating model. (PDF p. 5).
- d_seq can conceal errors in divergent, gap-rich alignments because it treats all gaps within a sequence as equivalent. (PDF p. 5).

## References

The reference entries need manual separation. The complete extracted reference section follows.

```text
Arnold,K. et al. (2006) The SWISS-MODEL workspace: a web-based environment for
protein structure homology modelling. Bioinformatics, 22, 195–201.
Cantarel,B. et al. (2006) Exploring the relationship between sequence similarity and
accurate phylogenetic trees. Mol. Biol. Evol., 23, 2090–2100.
Deza,M.M. and Deza,E. (2009) Encyclopedia of Distances. Springer, Berlin,
Heidelberg.
Dickson,R.J.et al. (2010) Identifying and seeing beyond multiple sequence alignment
errors using intra-molecular protein covariation. PLoS One, 5, e11082.
Do,C.B. et al. (2005) ProbCons: probabilistic consistency-based multiple sequence
alignment. Genome Res., 15, 330–340.
Eddy,S.R. (2009) A new generation of homology search tools based on probabilistic
inference. Genome Inform., 23, 205–211.
Edgar,R.C. and Batzoglou,S. (2006) Multiple sequence alignment. Curr. Opin. Struct.
Biol., 16, 368–373.
Edgar,R.C. (2004) MUSCLE: a multiple sequence alignment method with reduced time
and space complexity. BMC Bioinformatics, 5, 113.
Eisen,J.A. (1998) Phylogenomics: improving functional predictions for uncharacterized
genes by evolutionary analysis. Genome Res., 8, 163–167.
Felsenstein,J. (2003) Inferring Phylogenies. Sinauer Associates Inc., Sunderland,
Massachusetts.
Fletcher,W. and Yang,Z. (2009) INDELible: a flexible simulator of biological sequence
evolution. Mol. Biol. Evol., 26, 1879–1888.
Fletcher,W. and Yang,Z. (2010) The effect of insertions, deletions, and alignment errors
on the branch-site test of positive selection. Mol. Biol. Evol., 27, 2257–2267.
Golubchik,T. et al. (2007) Mind the gaps: evidence of bias in estimates of multiple
sequence alignments. Mol. Biol. Evol., 24, 2433–2442.
Hagopian,R. et al. (2010) SATCHMO-JS: a webserver for simultaneous protein multiple
sequence alignment and phylogenetic tree construction. Nucleic Acids Res., 38,
W29–W34.
Hall,B.G. (2005) Comparison of the accuracies of several phylogenetic methods using
protein and DNA sequences. Mol. Biol. Evol., 22, 792–802.
Huson,D.H. and Steel,M. (2004) Phylogenetic trees based on gene content.
Bioinformatics, 20, 2044–2049.
Katoh,K. and Toh,H. (2008) Recent developments in the MAFFT multiple sequence
alignment program. Brief. Bioinformatics, 9, 286–298.
Landan,G. and Graur,D. (2007) Heads or tails: a simple reliability check for multiple
sequence alignments. Mol. Biol. Evol., 24, 1380–1383.
Larkin,M.A. et al. (2007) Clustal W and Clustal X version 2.0. Bioinformatics, 23,
2947–2948.
501
Downloaded
from
https://academic.oup.com/bioinformatics/article/28/4/495/212883
by
University
of
Cape
Town
Libraries
user
on
13
March
2026
[16:40 10/2/2012 Bioinformatics-btr701.tex] Page: 502 495–502
B.P.Blackburne and S.Whelan
Lassmann,T. and Sonnhammer,E.L.L. (2002) Quality assessment of multiple alignment
programs. FEBS Lett., 529, 126–130.
Leach,A.R. and Gillet,V.J. (2003) An Introduction to Chemoinformatics. Dordrecht
Kluwer Academic Publishers, Dordrecht, Netherlands.
Lipkus,A. (1999) A proof of the triangle inequality for the Tanimoto distance. J. Math.
Chem., 26, 263–265.
Liu,K. et al. (2009) Rapid and accurate large-scale coestimation of sequence alignments
and phylogenetic trees. Science, 324, 1561–1564.
Löytynoja,A. and Goldman,N. (2008) Phylogeny-aware gap placement prevents
errors in sequence alignment and evolutionary analysis. Science, 320,
1632–1635.
Markova-Raina,P. and Petrov,D. (2011) High sensitivity to aligner and high rate of
false positives in the estimates of positive selection in the 12 drosophila genomes.
Genome Res., 21, 863–874.
Miklos,I. et al. (2008) How reliably can we predict the reliability of protein structure
predictions? BMC Bioinformatics, 9, 137.
Morrison,D.A. and Ellis,J.T. (1997) Effects of nucleotide sequence alignment on
phylogeny estimation: a case study of 18S rDNAs of apicomplexa. Mol. Biol. Evol.,
14, 428–441.
Notredame,C. (2000) T-Coffee: a novel method for fast and accurate multiple sequence
alignment. J. Mol. Biol., 302, 205–217.
Notredame,C. (2007) Recent evolutions of multiple sequence alignment algorithms.
PLoS Comput. Biol., 3, e123.
Ogden,T.H. and Rosenberg,M.S. (2006) Multiple sequence alignment accuracy and
phylogenetic inference. Syst. Biol., 55, 314–328.
Penn,O. et al. (2010) An alignment confidence score capturing robustness to guide tree
uncertainty. Mol. Biol. Evol., 27, 1759–1767.
Pollard,D.A. et al. (2006) Detecting the limits of regulatory element conservation and
divergence estimation using pairwise and multiple alignments. BMC Bioinformatics,
7, 376.
Redelings,B.D. and Suchard,M.A. (2005) Joint Bayesian estimation of alignment and
phylogeny. Syst. Biol., 54, 401–418.
Schneider,A. et al. (2009) Estimates of positive darwinian selection are inflated by
errors in sequencing, annotation, and alignment. Genome Biol. Evol., 1, 114–118.
Simmons,M.P. and Ochoterena,H. (2000) Gaps as characters in sequence-based
phylogenetic analyses. Syst. Biol., 49, 369–381.
Stamatakis,A. (2006) RAxML-VI-HPC: maximum likelihood-based phylogenetic
analyses with thousands of taxa and mixed models. Bioinformatics, 22, 2688–2690.
Subramanian,A.R. et al. (2008) DIALIGN-TX: greedy and progressive approaches for
segment-based multiple sequence alignment. Algorithms Mol. Biol., 3, 6.
Thompson,J.D. et al. (2005) Balibase 3.0: latest developments of the multiple sequence
alignment benchmark. Proteins, 61, 127–136.
Wang,L.-S. et al. (2011) The impact of multiple protein sequence alignment
on phylogenetic estimation. IEEE/ACM Trans. Comput. Biol. Bioinform., 8,
1108–1119.
Whelan,S. and Goldman,N. (2001) A general empirical model of protein evolution
derived from multiple protein families using a maximum-likelihood approach. Mol.
Biol. Evol., 18, 691–699.
Wise,M. (2010) No so hot - heads or tails is not able to reliably compare multiple
sequence alignments. Cladistics, 26, 438–443.
Wong,K.M. et al. (2008) Alignment uncertainty and genomic analysis. Science, 319,
473–476.
502
Downloaded
from
https://academic.oup.com/bioinformatics/article/28/4/495/212883
by
University
of
Cape
Town
Libraries
user
on
13
March
2026
```
