# Profile Hidden Markov Models

- Work ID: `b-753f18107c51`
- Asset ID: `a-d3f4a6cd267e6bbf`
- Source PDF: `literature/academic-papers-processed/Profile hidden Markov models.pdf`
- SHA-256: `d3f4a6cd267e6bbfac5d5bcca3371c44de7c13fbac9ddb237e66bc79c8ff05fd`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Profile HMMs convert multiple sequence alignments into probabilistic scoring models for remote homology searches. (PDF p. 1).
- The author describes model construction, scoring, training, domain libraries, and fold recognition. These methods are intended to complement pairwise sequence searches. (PDF p. 1).

## Objectives

- The author examines recent advances in profile HMM methods, with emphasis on alternative architectures, model libraries, and fold recognition. (PDF p. 1).
- The stated development goal is sensitive, statistically based sequence annotation that complements BLAST and FASTA. (PDF p. 7).

## Arguments

- The author argues that HMM theory gives profile scores a coherent probabilistic basis. Historical profile methods often used ad hoc scores. (PDF p. 1).
- Position independence during scoring does not prevent emission probabilities from encoding structural knowledge. It limits efficient treatment of long-distance residue correlations. (PDF p. 7).

## Analysis

- Forward and Viterbi require O(NM²) time for general HMMs. Sparse profile HMM transitions reduce this to O(NM) time. Standard space use is O(NM), where N is sequence length and M is state count. (PDF p. 2).
- Insertion transitions produce an affine-like gap score. The opening term is log tMI + log tIM, and the extension term is log tII. (PDF p. 3).
- The author attributes diminishing returns in domain-library coverage to unequal family sizes. Adding models for less populous families yields smaller gains in recognized sequences. (PDF p. 6).

## Methods

- Each consensus column has a match state for residue emissions, an insert state for additional residues, and a silent delete state. The architecture progresses from left to right. (PDF p. 3).
- Match scores usually use log odds: log(px/fx). Here, px is the state emission probability and fx is the background residue frequency. (PDF p. 3).
- Forward scores sequences, and Viterbi finds alignments. Building from an existing alignment converts emission and transition counts into probabilities. (PDF p. 2).
- Training from unaligned sequences uses methods such as Baum–Welch expectation maximization or gradient descent. This also requires inference of the hidden alignment. (PDF p. 2).

## Applications

- Pfam and PROSITE Profiles provide annotated domain models for protein sequence searches. The reported releases contain 1313 and 290 profiles, respectively. (PDF p. 6).
- A modified SAM implementation models secondary structure symbols. It aligns models trained on known structures to predicted secondary structures of new sequences. (PDF p. 6).

## Optimization

- The author reports memory-efficient Viterbi and Forward implementations with O(M) and O(M^1.5) space bounds. These incur a modest constant time penalty. (PDF p. 2).
- Most training methods optimize likelihood or posterior probability. Alternative objectives address biased sequence representation or discrimination between positive and negative examples. (PDF p. 3).
- The author recommends building from pre-aligned data when possible. Local training optimizers can become trapped in spurious optima. (PDF p. 3).

## Evaluation and testing

- CASP supplies sequences before their experimental structures become available. Fold predictions are assessed after structure determination. (PDF p. 7).
- The author describes CASP as an anecdotal benchmark. Method rankings are partly subjective, and expert interpretation varies between prediction groups. (PDF p. 7).
- An unpublished comparison measures the fraction of predicted C. elegans proteins recognized by successive Pfam releases. (PDF p. 6).

## Results

- Reported Pfam coverage of predicted C. elegans proteins rose from approximately 27% with 175 models to 35% with 527 models and 42% with 806 models. (PDF p. 6).
- Several successful CASP2 groups used HMM methods. Murzin and Bateman correctly predicted all six folds they attempted by combining profile HMMs, secondary structure prediction, and expert knowledge. (PDF p. 7).

## Limitations and uncertainty

- HMM training can encounter many local optima. General model architectures usually require manual design. (PDF p. 3).
- HMMs cannot efficiently represent long-distance residue correlations, such as complementary base pairs in RNA structural alignments. (PDF p. 7).
- The author states that library completeness cannot be estimated reliably because the total number of protein families is unknown. The available servers and databases were still changing rapidly. (PDF p. 6).

## References

The reference entries need manual separation. The complete extracted reference section follows.

```text
Altschul,S.F. (1991) Amino acid substitution matrices from an
information theoretic perspective. J. Mol. Biol., 219, 555–565.
Altschul,S.F. and Gish,W. (1996) Local alignment statistics. Methods
Enzymol., 266, 460–480.
Altschul,S.F.,Gish,W.,Miller,W.,Myers,E.W.andLipman,D.J.(1990)
Basic local alignment search tool. J. Mol. Biol., 215, 403–410.
Altschul,S.F., Madden,T.L., Schaffer,A.A., Zhang,J., Zhang,Z.,
Miller,W. and Lipman,D.J. (1997) Gapped BLAST and PSI-
BLAST: A new generation of protein database search programs.
Nucleic Acids Res., 25, 3389–3402.
Asai,K., Hayamizu,S. and Handa,K. (1993) Prediction of protein
secondary structure by the hidden Markov model. Comput. Applic.
Biosci., 9, 141–146.
Attwood,T.K., Beck,M.E., Flower,D.R., Scordis,P. and Selley,J.N.
(1998) The PRINTS protein fingerprint database in its fifth year.
Nucleic Acids Res., 26, 304–308.
Bairoch,A., Bucher,P. and Hofmann,K. (1997) The PROSITE data-
base, its status in 1997. Nucleic Acids Res., 25, 217–221.
Baldi,P. and Brunak,S. (1998) Bioinformatics: The Machine Learning
Approach. MIT Press, Boston.
Baldi,P. and Chauvin,Y. (1996) Hybrid modeling, HMM/NN architec-
tures and protein applications. Neural Comput., 8, 1541–1565.
Baldi,P., Chauvin,Y., Hunkapiller,T. and McClure,M.A. (1994)
Hidden Markov models of biological primary sequence informa-
tion. Proc. Natl Acad. Sci. USA, 91, 1059–1063.
Barrett,C., Hughey,R. and Karplus,K. (1997) Scoring hidden Markov
models. Comput. Applic. Biosci., 13, 191–199.
S.R.Eddy
762
Barton,G.J. (1990) Protein multiple sequence alignment and flexible
pattern matching. Methods Enzymol., 183, 403–427.
Birney,E. and Durbin,R. (1997) Dynamite: A flexible code generating
language for dynamic programming methods used in sequence
comparison. In Proceedings of the Fifth International Conference
on Intelligent Systems in Molecular Biology, 5, 56–64. AAAI Press,
Menlo Park.
Bork,P. and Gibson,T.J. (1996) Applying motif and profile searches.
Methods Enzymol., 266, 162–184.
Bowie,J.U., Luthy,R. and Eisenberg,D. (1991) A method to identify
protein sequences that fold into a known three-dimensional
structure. Science, 253, 164–170.
Bruno,W.J. (1996) Modeling residue usage in aligned protein se-
quences via maximum likelihood. Mol. Biol. Evol., 13, 1368–1374.
Bucher,P., Karplus,K., Moeri,N. and Hofmann,K. (1996) A flexible
motif search technique based on generalized profiles. Comput.
Chem., 20, 3–23.
Burge,C. and Karlin,S. (1997) Prediction of complete gene structures
in human genomic DNA. J. Mol. Biol., 268, 78–94.
Chothia,C. (1992) One thousand families for the molecular biologist.
Nature, 357, 543–544.
Churchill,G.A. (1989) Stochastic models for heterogeneous DNA
sequences. Bull. Math. Biol., 51, 79–94.
Corpet,F., Gouzy,J. and Kahn,D. (1998) The ProDom database of
protein domain families. Nucleic Acids Res., 26, 323–326.
Di Francesco,V., Garnier,J. and Munson,P.J. (1997a) Protein topology
recognition from secondary structure sequences: Application of the
hidden Markov models to the alpha class proteins. J. Mol. Biol., 267,
446–463.
Di Francesco,V., Geetha,V., Garnier,J. and Munson,P.J. (1997b) Fold
recognition using predicted secondary structure sequences and
hidden Markov models of protein folds. Proteins, 1(Suppl.),
123–128.
Durbin,R., Eddy,S.R., Krogh,A. and Mitchison,G.J. (1998) Biological
Sequence Analysis: Probabilistic Models of Proteins and Nucleic
Acids. Cambridge University Press, Cambridge, UK.
Eddy,S.R. (1996) Hidden Markov models. Curr. Opin. Struct. Biol., 6,
361–365.
Fabian,P., Murvai,J., Vlahovicek,K., Hegyi,H. and Pongor,S. (1997)
The SBASE protein domain library, release 5.0: A collection of
annotated protein sequence segments. Nucleic Acids Res., 25,
240–243.
Felsenstein,J. and Churchill,G. (1996) A hidden Markov model
approach to variation among sites in rate of evolution. Mol. Biol.
Evol., 13, 93–104.
Godzik,A., Kolinski,A. and Skolnick,J. (1992) Topology fingerprint
approach to the inverse protein folding problem. J. Mol. Biol., 227,
227–238.
Goldman,N., Thorne,J.L. and Jones,D.T. (1996) Using evolutionary
trees in protein secondary structure prediction and other compara-
tive sequence analyses. J. Mol. Biol., 263, 196–208.
Gribskov,M., McLachlan,A.D. and Eisenberg,D. (1987) Profile analy-
sis: Detection of distantly related proteins. Proc. Natl Acad. Sci.
USA, 84, 4355–4358.
Grundy,W.N., Bailey,T.L. and Elkan,C.P. (1996) ParaMEME: A
parallel implementation and a web interface for a DNA and protein
motif discovery tool. Comput. Applic. Biosci., 12, 303–310.
Grundy,W.N., Bailey,T.L., Elkan,C.P. and Baker,M.E. (1997) Meta-
MEME: Motif-based hidden Markov models of protein families.
Comput. Applic. Biosci., 13, 397–406.
Henderson,J., Salzberg,S. and Fasman,K. (1997) Finding genes in
human DNA with a hidden Markov model. J. Comput. Biol., 4,
127–141.
Henikoff,S. (1996) Scores for sequence searches and alignments.Curr.
Opin. Struct. Biol., 6, 353–360.
Henikoff,S. and Henikoff,J.G. (1992) Amino acid substitution ma-
trices from protein blocks. Proc. Natl Acad. Sci. USA, 89,
10915–10919.
Henikoff,S., Greene,E.A., Pietrokovski,S., Bork,P., Attwood,T.K. and
Hood,L. (1997) Gene families: The taxonomy of protein paralogs
and chimeras. Science, 278, 609–614.
Henikoff,S., Pietrokovski,S. and Henikoff,J.G. (1998) Superior per-
formance in protein homology detection with the Blocks database
servers. Nucleic Acids Res., 26, 309–312.
Hughey,R. (1996) Parallel hardware for sequence comparison and
alignment. Comput. Applic. Biosci., 12, 473–479.
Hughey,R. and Krogh,A. (1996) Hidden Markov models for sequence
analysis: Extension and analysis of the basic method. Comput.
Applic. Biosci., 12, 95–107.
Jaynes,E.T. (1998) Probability Theory: The Logic of Science.
Available from http://bayes.wustl.edu.
Jongeneel,V., Junier,T., Iseli,C., Hofmann,K. and Bucher,P. (1998)
INSECT and MOLLUSCS—supercomputing on the cheap. Avail-
able from http:// cmpteam4.unil.ch/biocomputing/mollusc/ IN-
SECT_and_MOLLUSCS.html.
Karchin,R. and Hughey,R. (1998) Weighting hidden Markov models
for maximum discrimination. Bioinformatics, in press.
Karplus,K., Sjolander,K., Barrett,C., Cline,M., Haussler,D.,
Hughey,R., Holm,L. and Sander,C. (1997) Predicting protein
structure using hidden Markov models. Proteins, 1(Suppl.),
134–139.
Krogh,A. (1997) Two methods for improving performance of an
HMM and their application for gene finding. In Proceedings of the
Fifth International Conference on Intelligent Systems in Molecular
Biology, 5, 179–186. AAAI Press, Menlo Park.
Krogh,A. (1998) An introduction to hidden Markov models for
biological sequences. In Salzberg,S., Searls,D. and Kasif,S. (eds),
Computational Methods in Molecular Biology. Elsevier, New York.
pp. 45–63.
Krogh,A., Brown,M., Mian,I.S., Sjolander,K. and Haussler,D. (1994a)
Hidden Markov models in computational biology: Applications to
protein modeling. J. Mol. Biol., 235, 1501–1531.
Krogh,A., Mian,I.S. and Haussler,D. (1994b) A hidden Markov model
that finds genes in E.coli DNA. Nucleic Acids Res., 22, 4768–4778.
Kruglyak,L., Daly,M.J., Reeve-Daly,M.P. and Lander,E.S. (1996)
Parametric and nonparametric linkage analysis: A unified multi-
point approach. Am. J. Hum. Genet., 58, 1347–1363.
Kulp,D., Haussler,D., Reese,M.G. and Eeckman,F.H. (1996) A
generalized hidden Markov model for the recognition of human
genes in DNA. In Proceedings of the Fourth International
Conference on Intelligent Systems in Molecular Biology, 4,
134–141. AAAI Press, Menlo Park.
Levitt,M. (1997) Competitive assessment of protein fold recognition
and alignment accuracy. Proteins, 1(Suppl.), 92–104.
Profile hidden Markov models
763
Lukashin,A.V. and Borodovsky,M. (1998) GeneMark.hmm: New
solutions for gene finding. Nucleic Acids Res., 26, 1107–1115.
Luthy,R., Bowie,J.U. and Eisenberg,D. (1992) Assessment of protein
models with three-dimensional profiles. Nature, 356, 83–85.
Mamitsuka,H. (1996) A learning method of hidden Markov models for
sequence discrimination. J. Comput. Biol., 3, 361–373.
Moult,J., Hubbard,T., Bryant,S.H., Fidelis,K. and Pedersen,J.T. (1997)
Critical assessment of methods of protein structure prediction
(CASP): Round II. Proteins, 1(Suppl.), 2–6.
Murzin,A.G. and Bateman,A. (1997) Distant homology recognition
using structural classification of proteins. Proteins, 1(Suppl.),
105–112.
Neuwald,A.F., Liu,J.S., Lipman,D.J. and Lawrence,C.E. (1997) Ex-
tracting protein alignment models from the sequence database.
Nucleic Acids Res., 25, 1665–1677.
Orengo,C., Jones,D.T.andThornton,J.M.(1994)Proteinsuperfamilies
and domain superfolds. Nature, 372, 631–634.
Pearson,W. and Lipman,D. (1988) Improved tools for biological
sequence comparison. Proc. Natl Acad. Sci. USA, 85, 2444–2448.
Rabiner,L.R. (1989) A tutorial on hidden Markov models and selected
applications in speech recognition. Proc. IEEE, 77, 257–286.
Rost,B. and Sander,C. (1993) Prediction of protein secondary structure
at better than 70% accuracy. J. Mol. Biol., 232, 584–599.
Slonim,D., Kruglyak,L., Stein,L. and Lander,E. (1997) Building
human genome maps with radiation hybrids. J. Comput. Biol., 4,
487–504.
Sjölander,K., Karplus,K., Brown,M., Hughey,R., Krogh,A., Mian,I.S.
and Haussler,D. (1996) Dirichlet mixtures: A method for improving
detection of weak but significant protein sequence homology.
Comput. Applic. Biosci., 12, 327–345.
Sonnhammer,E.L., Eddy,S.R. and Durbin,R. (1997) Pfam: A com-
prehensive database of protein families based on seed alignments.
Proteins, 28, 405–420.
Sonnhammer,E.L.L., Eddy,S.R., Birney,E., Bateman,A. and Durbin,R.
(1998) Pfam: Multiple sequence alignments and HMM-profiles of
protein domains. Nucleic Acids Res., 26, 320–322.
Stultz,C.M., White,J.V. and Smith,T.F. (1993) Structural analysis
based on state-space modeling. Protein Sci., 2, 305–314.
Sunyaev,S.R., Rodchenkov,I.V., Eisenhaber,F. and Kuznetsov,E.N.
(1998) Analysis of the position dependent amino acid probabilities
and its application to the search for remote homologues. In
RECOMB ’98, pp. 258–265.
Tarnas,C. and Hughey,R. (1998) Reduced space hidden Markov model
training. Bioinformatics, in press.
Taylor,W.R. (1986) Identification of protein sequence homology by
consensus template alignment. J. Mol. Biol., 188, 233–258.
Thorne,J.L., Goldman,N. and Jones,D.T. (1996) Combining protein
evolution and secondary structure. Mol. Biol. Evol., 13, 666–673.
Wheelan,S.J. and Boguski,M.S. (1998) Late-night thoughts on the
sequence annotation problem. Genome Res., 8, 168–169.
White,J.V., Stultz,C.M. and Smith,T.F. (1994) Protein classification by
stochastic modeling and optimal filtering of amino-acid sequences.
Math. Biosci., 119, 35–75.
Wu,C.H., Zhao,S. and Chen,H.L. (1996) A protein class database
organized with ProSite, protein groups and PIR, superfamilies. J.
Comput. Biol., 3, 547–561.
Yada,T., Ishikawa,M., Tanaka,H. and Asai,K. (1996) Extraction of
hidden Markov model representations of signal patterns in DNA
sequences. Pac. Symp. Biocomput., World Scientific, Singapore, pp.
686–696.
```
