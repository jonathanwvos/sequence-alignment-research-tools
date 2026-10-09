# Identification of Direct Residue Contacts in Protein–Protein Interaction by Message Passing

- Work ID: `b-d521b3df46c0`
- Asset ID: `a-3a8d6f1e3df6d88e`
- Source PDF: `literature/academic-papers-processed/Identification of direct residue contacts in protein–protein interaction by message passing.pdf`
- SHA-256: `3a8d6f1e3df6d88e20eed775705bdbddb0c99e380539e8a03a2d5d5fc72b0d03`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors combine covariance analysis with global statistical inference to distinguish direct residue couplings from indirect correlations. (PDF p. 1).
- They apply message passing to aligned sensor kinase and response regulator sequences, then rank residue pairs by direct information. (PDF p. 3).

## Objectives

- Identify direct residue contacts at protein interfaces from sequence correlations. (PDF p. 1).
- Test whether global inference improves contact prediction over mutual information alone for SK/RR and RR/RR interactions. (PDF p. 2).

## Arguments

- A high pairwise correlation can arise through intermediate residues or multiple weak coupling paths. The authors therefore argue that local correlation scores cannot isolate direct contacts. (PDF p. 2).
- The authors use a maximum-entropy model to match single-position and pair frequencies while avoiding unnecessary constraints. (PDF p. 3).

## Analysis

- The SK/RR alignment contains 2,546 paired sequences with 88 SK positions and 124 RR positions. Gaps form a twenty-first sequence state. (PDF p. 2).
- Mutual information is corrected by subtracting its mean under a finite-sample null model. A threshold above the exponential background selects 32 correlated pairs. (PDF p. 2).
- Direct information measures the correlation produced by one inferred coupling in a two-position model with the observed single-position frequencies. (PDF p. 6).

## Methods

- HMMER aligns complete domains from RefSeq release 19 to Pfam models. Only unique species are retained to reduce strain oversampling. (PDF p. 6).
- SK/RR partners are inferred from chromosomal adjacency. The RR homodimer set requires both a response regulator domain and an OmpR-C DNA-binding domain. (PDF p. 6).
- A pairwise maximum-entropy model represents direct couplings and local amino acid preferences. Marginal estimation and coupling updates repeat until model frequencies meet the specified precision. (PDF p. 3).
- Belief propagation estimates single-position marginals. Susceptibility propagation extends the calculation to pair marginals. (PDF p. 6).

## Applications

- The authors propose inferred contacts as constraints for tertiary structure prediction and for quaternary structure prediction when monomer structures are available. (PDF p. 5).
- They suggest that variable contact patterns could guide the design of synthetic response regulators with different interaction specificity. (PDF p. 5).

## Optimization

- Message passing reduces the stated marginal-estimation cost from O(21^(N−2)N²) for exact summation to O(21²N⁴). (PDF p. 3).
- Gradient descent updates each coupling using the difference between observed and model pair frequencies. (PDF p. 3).
- The SK/RR calculation uses 60 positions from the 140 highest mutual-information pairs. This reduces the computation to 1,770 position pairs. (PDF p. 3).

## Evaluation and testing

- RR contact predictions were checked against minimum atom distances in ArcA, PhoP, and MicA structures. Pairs beyond 6 Å were treated as false positives. (PDF p. 5).
- The authors compared direct-information rankings with mutual-information rankings to evaluate contact specificity. (PDF p. 5).
- Tests with 32, 40, and 50 positions gave similar qualitative results when all relevant network nodes were included. The supporting results were not shown. (PDF p. 6).

## Results

- The SK/RR analysis separated nine pairs with high mutual and direct information from 22 pairs with high mutual information but weak direct coupling. (PDF p. 3).
- The RR analysis found four dimer contacts at ranks 1, 3, 26, and 40. The first false positive occurred at rank 24. (PDF p. 5).
- Inference for about 60 positions required approximately four days on one 2.33 GHz Xeon CPU. The authors estimated more than one month for 100 positions. (PDF p. 6).

## Limitations and uncertainty

- The dataset was too small to estimate correlations involving more than two residues with sufficient precision. (PDF p. 3).
- The computational cost prevented simultaneous analysis of all 212 alignment positions. (PDF p. 3).
- Message passing is semiheuristic for graphs with loops. Its exactness applies to tree-like coupling graphs. (PDF p. 6).
- Sequence couplings alone cannot distinguish contacts within a monomer from contacts between monomers. The authors use known monomer structures for this distinction. (PDF p. 5).

## References

1. Cusick ME, Klitgord N, Vidal M, Hill DE (2005) Interactome: Gateway into systems biology. Hum Mol Genet 14(Spec No 2):R171–R181. (PDF p. 6)
2. Kortemme T, Baker D (2004) Computational design of protein-protein interactions. Curr Opin Chem Biol 8:91–97. (PDF p. 6)
3. Wells JA, McClendon CL (2007) Reaching for high-hanging fruit in drug discovery at protein-protein interfaces. Nature 450:1001–1009. (PDF p. 6)
4. Liolios K, Mavromatis K, Tavernarakis N, Kyrpides NC (2008) The Genomes On Line Database (GOLD) in 2007: Status of genomic and metagenomic projects and their associ- ated metadata. Nucleic Acids Res 36:D475–D479. (PDF p. 6)
5. Suel GM, Lockless SW, Wall MA, Ranganathan R (2003) Evolutionarily conserved networks of residues mediate allosteric communication in proteins. Nat Struct Biol 10:59–69. (PDF p. 6)
6. Lockless SW, Ranganathan R (1999) Evolutionarily conserved pathways of energetic con- nectivity in protein families. Science 286:295–299. (PDF p. 6)
7. Altschuh D, Lesk AM, Bloomer AC, Klug A (1987) Correlation of co-ordinated amino acid substitutions with function in viruses related to tobacco mosaic virus. J Mol Biol 193:693–707. (PDF p. 6)
8. Atchley WR, Wollenberg KR, Fitch WM, Terhalle W, Dress AW (2000) Correlations among amino acid sites in bHLH protein domains: An information theoretic analysis. Mol Biol Evol 17:164–178. (PDF p. 6)
9. Göbel U, Sander C, Schneider R, Valencia A (1994) Correlated mutations and residue contacts in proteins. Proteins Struct Funct Genet 18:309–317. (PDF p. 6)
10. Kass I, Horovitz A (2002) Mapping pathways of allosteric communication in GroEL by analysis of correlated mutations. Proteins Struct Funct Genet 48:611–617. (PDF p. 6)
11. White RA, Szurmant H, Hoch JA, Hwa T (2007) Features of protein-protein interactions in two-component signaling deduced from genomic libraries. Methods Enzymol 422:75–101. (PDF p. 6)
12. BurgerL,vanNimwegenE(2008)Accuratepredictionofprotein-proteininteractionsfrom sequence alignments using a Bayesian method. Mol Syst Biol 4:165. (PDF p. 6)
13. Thattai M, Burak Y, Shraiman BI (2007) The origins of specificity in polyketide synthase protein interactions. PLoS Comput Biol 3:1827–1835. (PDF p. 6)
14. Kortemme T, et al. (2004) Computational redesign of protein-protein interaction speci- ficity. Nat Struct Mol Biol 11:371–379. (PDF p. 6)
15. Fodor AA, Aldrich RW (2004) Influence of conservation on calculations of amino acid covariance in multiple sequence alignments. Proteins Struct Funct Bioinf 56:211–221. (PDF p. 6)
16. Mezard,M.,Parisi,G.Virasoro,M.A(1987)SpinGlassTheoryandBeyond(WorldScientific, Singapore). (PDF p. 6)
17. KschischangFR,FreyBJ,LoeligerH-A(2001)Factorgraphsandthesum-productalgorithm. IEEE Trans Inf Theory 47:498–519. (PDF p. 6)
18. Yedidia JS, Freeman WT, Weiss Y (2001) Generalized belief propagation. News Physiol Sci 13:689–695. (PDF p. 6)
19. Mezard M, Parisi G, Zecchina R (2002) Analytic and algorithmic solution of random satisfiability problems. Science 297:812–815. (PDF p. 6)
20. Hartmann AK, Weigt M (2005) Phase Transitions in Combinatorial Optimization Problems (Wiley-VCH, Weinheim). (PDF p. 6)
21. Mezard M, Montanari A (2008) Information, Physics and Computation (Oxford Univ Press, Oxford). (PDF p. 6)
22. UlrichLE,ZhulinIB(2007)MiST:Amicrobialsignaltransductiondatabase.NucleicAcidsRes 35:D386–D390. (PDF p. 6)
23. Mascher T, Helmann JD, Unden G (2006) Stimulus perception in bacterial signal- transducing histidine kinases. Microbiol Mol Biol Rev 70:910–938. (PDF p. 6)
24. Galperin MY (2006) Structural classification of bacterial response regulators: Diversity of output domains and domain combinations. J Bacteriol 188:4169–4182. (PDF p. 6)
25. Ninfa AJ, Magasanik B (1986) Covalent modification of the glnG product, NRI, by the glnL product, NRII, regulates the transcription of the glnALG operon in Escherichia coli. Proc Natl Acad Sci USA 83:5909–5913. (PDF p. 6)
26. Laub MT, Goulian M (2007) Specificity in two-component signal transduction pathways. Annu Rev Genet 41:121–145. (PDF p. 6)
27. Toro-Roman A, Mack TR, Stock AM (2005) Structural analysis and solution studies of the activatedregulatorydomainoftheresponseregulatorArcA:Asymmetricdimermediated by the ␣4-␤5-␣5 Face. J Mol Biol 349:11–26. (PDF p. 6)
28. Marina A, Waldburger CD, Hendrickson WA (2005) Structure of the entire cytoplasmic portion of a sensor histidine-kinase protein. EMBO J 24:4247–4259. (PDF p. 6)
29. ZapfJ,SenU,Madhusudan,HochJA,VarugheseKI(2000)Atransientinteractionbetween two phosphorelay proteins trapped in a crystal lattice reveals the mechanism of molecular recognition and phosphotransfer in signal transduction. Structure 8:851–862. (PDF p. 6)
30. Bialek W, Ranganathan, R (2007) Rediscovering the power of pairwise interactions, arXiv:0712.4397v1 [q-bio.QM]. (PDF p. 6)
31. Mezard, M. Mora, T (2008) Constraint satisfaction and neural networks: A statistical- physics perspective, arXiv:0803.3061v1 [q-bio.NC]. (PDF p. 6)
32. Mukhopadhyay D, Sen U, Zapf J, Varughese KI (2004) Metals in the sporulation phos- phorelay: Manganese binding by the response regulator Spo0F. Acta Crystallogr D Biol Crystallogr 60:638–645. (PDF p. 6)
33. Szurmant H, et al. (2008) Co-evolving motions at protein-protein interfaces of two- component signaling systems identified by covariance analysis. Biochemistry 47:7782– 7784. (PDF p. 6)
34. Fiedler U, Weiss V (1995) A common switch in activation of the response regulators NtrC and PhoB: Phosphorylation induces dimerization of the receiver modules. EMBO J 14:3696–3705. (PDF p. 6)
35. Bachhawat P, Stock AM (2007) Crystal structures of the receiver domain of the response regulatorPhoPfromEscherichiacoliintheabsenceandpresenceofthephosphorylanalog beryllofluoride. J Bacteriol 189:5987–5995. (PDF p. 6)
36. Bent CJ, Isaacs NW, Mitchell TJ, Riboldi-Tunnicliffe A (2004) Crystal structure of the response regulator 02 receiver domain, the essential YycF two-component system of Streptococcus pneumoniae in both complexed and native states. J Bacteriol 186:2872– 2879. (PDF p. 6)
37. Schmeisser C, Steele H, Streit WR (2007) Metagenomics, biotechnology with non- culturable microbes. Appl Microbiol Biotechnol 75:955–962. (PDF p. 6)
38. PruittKD,MaglottDR(2001)RefSeqandLocusLink:NCBIgene-centeredresources.Nucleic Acids Res 29:137–140. (PDF p. 6)
39. Eddy SR (1998) Profile hidden Markov models. Bioinformatics 14:755–763. (PDF p. 6)
40. Finn RD, et al. (2008) The Pfam protein families database. Nucleic Acids Res 36:D281–D288. 72 兩 www.pnas.org兾cgi兾doi兾10.1073兾pnas.0805923106 Weigt et al. Downloaded from https://www.pnas.org by 192.143.141.160 on September 26, 2026 from IP address 192.143.141.160. (PDF p. 6)
