# M2Align: parallel multiple sequence alignment with a multi-objective metaheuristic

- Work ID: `w-debfcabc2c73`
- Asset ID: `a-debfcabc2c739800`
- Source PDF: `literature/academic-papers-processed/M2Align: parallel multiple sequence alignment with a multi-objective metaheuristic - Zambrano-Vega et al.pdf`
- SHA-256: `debfcabc2c7398005a2fa100ff13f177a00d90060d4e91c1792ee5ad25178cb0`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- M2Align reimplements MO-SAStrE in Java using NSGA-II. It optimizes STRIKE, totally conserved columns, and non-gap percentage together. (PDF p. 3).
- It stores gap information and evaluates candidate alignments in parallel. Tests on BAliBASE show reduced runtime with up to 20 cores. (PDF p. 2).

## Objectives

- The authors aim to reduce the cost of multi-objective multiple sequence alignment through multicore execution. (PDF p. 2).
- The default optimization maximizes STRIKE, the percentage of totally conserved columns, and the percentage of non-gaps. (PDF p. 3).

## Arguments

- The authors argue that multiple alignment scores capture different properties. A multi-objective search can return alternative trade-off solutions in one run. (PDF p. 3).
- Serial profiling of BAliBASE instance BB20001 identifies solution evaluation as the main runtime cost. This motivates parallel evaluation. (PDF p. 5).

## Analysis

- NSGA-II ranks combined parent and offspring populations by dominance. Crowding distance selects among solutions of equal rank to preserve diversity. (PDF p. 3).
- Parallel efficiency decreases because evaluation alternates with sequential work. Synchronous evaluation also leaves cores idle when candidate alignments have different evaluation times. (PDF p. 7).

## Methods

- The initial population uses alignments from ClustalW, MUSCLE, Kalign, Mafft, RetAlign, TCOFFEE, ProbCons, and FSA. (PDF p. 3).
- Single-point crossover combines compatible parts of two parent alignments. Closed-gap shifting moves gap groups, and columns containing only gaps are removed. (PDF p. 5).
- Each generation creates and evaluates offspring, merges them with parents, and selects the next population. The output approximates the Pareto front. (PDF p. 3).
- The Java implementation uses jMetal's NSGA-II and a multithreaded population evaluator. (PDF p. 5).

## Applications

- M2Align provides multiple sequence alignment with alternative objective scores. SOP and weighted SOP can replace STRIKE when PDB structures are unavailable. (PDF p. 3).
- A generic MSA problem template allows users to configure objectives from the implemented scores. (PDF p. 5).

## Optimization

- The alignment encoding stores gap groups instead of integer matrices. The authors report lower memory requirements and more efficient crossover and mutation. (PDF p. 3).
- Independent candidate evaluations run in parallel before population merging and ranking. The authors state that this parallel scheme preserves NSGA-II behavior. (PDF p. 5).

## Evaluation and testing

- The benchmark contained 218 BAliBASE v3.0 datasets in six groups: RV11, RV12, RV20, RV30, RV40, and RV50. (PDF p. 5).
- Runs used 100 candidates and 50,000 evaluations. Mutation probability was 0.80 and crossover probability was 0.20. (PDF p. 6).
- Tests used 1, 4, 10, and 20 cores on two ten-core Intel Xeon E5-2650 v3 processors at 2.3 GHz. Performance measures were speedup and efficiency. (PDF p. 6).
- Accuracy comparisons used the three optimized objectives and BAliBASE SP and TC scores. The reference scoring included unreliable regions. (PDF p. 6).

## Results

- For RV11, runtime decreased from 9.05 hours on one core to 0.99 hours on 20 cores. Table 2 reports 9.12-fold speedup and 46% efficiency. (PDF p. 6).
- For BB30009, sequential M2Align took 0.55 minutes, compared with 294.24 minutes for MO-SAStrE under matched test conditions. (PDF p. 6).
- Across BAliBASE, M2Align obtained STRIKE 2.44, TCC 2.45%, SP 0.81, and TC 0.46. These exceeded the reported comparator scores, excluding reference values. (PDF p. 6).
- M2Align obtained 58.13% non-gaps, below the 58.51% reported for MO-SAStrE. (PDF p. 6).

## Limitations and uncertainty

- The authors could not run the original MO-SAStrE code on all BAliBASE datasets. They used previously published scores, and no MO-SAStrE TC score was available. (PDF p. 6).
- M2Align and MO-SAStrE differ in implementation components and incompletely specified variation operators. The authors state that their search behavior is therefore not identical. (PDF p. 7).
- Gap count strongly affects performance. Pilot tests found medium-scale problems difficult to solve within reasonable time on the tested multicore system. (PDF p. 7).
- The authors identify medium and large alignments as unresolved challenges. They propose local search, asynchronous NSGA-II, and stronger computing systems as possible improvements. (PDF p. 7).

## References

1. Abbasi,M. et al. (2015). Local search for multiobjective multiple sequence alignment. In: Ortu~ no, F. and Rojas, I. (eds.), Bioinformatics and Biomedical Engineering, Volume 9044 of Lecture Notes in Computer Science. Springer International Publishing, Cham, pp. 175–182. Bacon,D.J., and Anderson,W.F. (1986) Multiple sequence alignment. J. Mol. Biol., 191, 153–161. Capella-Gutiérrez,S. et al. (2009) trimal: a tool for automated alignment trim- ming in large-scale phylogenetic analyses. Bioinformatics, 25, 1972. da Silva,F. et al. (2010) Alineaga a genetic algorithm with local search opti- mization for multiple sequence alignment. Appl. Intell., 32, 164–172. da Silva,F.J.M. et al. (2011) Parallel Niche Pareto AlineaGA–lineaGA Niche Pamultiobjective approach on multiple sequence alignment. J. Integr.Bioinformatics, 8, 174. Dayhoff,M. et al. (1978) A model of evolutionary change in proteins. In: Dayhoff, M.O. (ed.) Atlas of Protein Sequence and Structure, Vol. 5, National Biomedical Research Foundation, Washington, DC, pp. 345–352. Deb,K. et al. (2002) A fast and elitist multiobjective genetic algorithm: NSGA- II. IEEE Trans. Evol. Comput., 6, 182–197. Do,C. et al. (2005) Probcons: Probabilistic consistency-based multiple se- quence alignment. Genome Res., 15, 330–340. Durillo,J.J. et al. (2008). A Study of Master-Slave Approaches to Parallelize (PDF p. 7)
2. NSGA-II. In: IEEE Int. Symp. on Parallel and Distributed Processing, 2008 - IPDPS 2008, pp. 1p.e. Miami, FL, USA. Edgar,R. (2004) Muscle: multiple sequence alignment with high accuracy and high throughput. Nucleic Acids Res., 32, 1792–1797. Handl,J. et al. (2007) Multiobjective optimization in bioinformatics and com- putational biology. IEEE/ACM Transactions on Computational Biology and Bioinformatics/IEEE, ACM, Vol. 4, pp. 279–292. Henikoff,S., and Henikoff,J. (1992) Amino acid substitution matrices from protein blocks. Proc. Natl. Acad. Sci. USA, 89, 10915–10919. Katoh,K. et al. (2002) Mafft: a novel method for rapid multiple sequence alignment based on fast fourier transform. Nucleic Acids Res., 30, 3059–3066. Kaya,M. et al. (2014) Multiple sequence alignment with affine gap by using multi-objective genetic algorithm. Comput. Methods Prog. Biomed., 114, 38–49. Kemena,C. et al. (2011) Strike: evaluation of protein msas using a single 3d structure. Bioinformatics, 27, 3385–3391. Lassmann,T., and Sonnhammer,E.L. (2005) Kalign align mer,"http://www. ncbi.nlm.nih.gov/pubmed/2203920gorithm. BMC Bioinformatics, 6, 9. (PDF p. 7)
3. C.Zambrano-Vega et al. Downloaded from https://academic.oup.com/bioinformatics/article/33/19/3011/3852082 by Cape Town University user on 20 July 2026 Nebro,A. et al. (2015). Redesigning the jmetal multi-objective optimization framework. In: Proceedings of the Companion Publication of the 2015 Annual Conference on Genetic and Evolutionary Computation, GECCO Companion ’omp pp. 1093sniong New York, NY, USA. ACM. Notredame,C. et al. (2000) T-coffee: a novel method for fast and accurate multiple sequence alignment. J. Mol. Biol., 302, 205– 217. Nov ak,A.S.A. et al. (2010) Reticular alignment: A progressive corner-cutting method for multiple sequence alignment. BMC Bioinformatics, 11, 1–19. Ortu~ no,F. et al. (2013) Optimizing multiple sequence alignments using a gen- etic algorithm based on three objectives: structural information, non-gaps percentage and totally conserved columns. Bioinformatics (Oxford, England), 29, 2112–2121. Poirot,O. et al. (2004) 3dcoffee@igs: a web server for combining sequences and structures into a multiple sequence alignment. Nucleic Acids Res., 32(Suppl 2), W37. Rani,R.R., and Ramyachitra,D. (2016) Multiple sequence alignment using multi- objective based bacterial foraging optimization algorithm. Biosystems, 150, 177– 189. Roberts,R.B.A. et al. (2009) Fast statistical alignment. PLoS Comput. Biol., 5, e1000392. Rubio-Largo,A. et al. (2015). A hybrid multiobjective memetic metaheuristic for multiple sequence alignment. Evolutionary Computation, IEEE Transactions on, (99), pp. 1p. , Rubio-Largo,A. et al. (2016) Hybrid multiobjective artificial bee colony for multiple sequence alignment. Appl. Soft Comput., 41, 157– 168. Seeluangsawat,P., and Chongstitvatana,P. (2005). A multiple objective evolu- tionary algorithm for multiple sequence alignment. In Proceedings of the 7th Annual Conference on Genetic and Evolutionary Computation, GECCO ’ECC pp. 477esedi New York, NY, USA. ACM. Soto,W., and Becerra,D. (2014). A multi-objective evolutionary algorithm for improving multiple sequence alignments. In: Campos S. (ed.) Advances in Bioinformatics and Computational Biology, Volume 8826 of Lecture Notes in Computer Science. Springer International Publishing, Cham, pp. 73–82. Thompson,J.et al. (1994) Clustal w: improving the sensitivity of progres- sive multiple sequence alignment through sequence weighting, position- specific gap penalties and weight matrix choice. Nucleic Acids Res., 22, 4673–4680. Thompson,J. et al. (2005) Balibase 3.0: latest developments of the multiple se- quence alignment benchmark. Proteins, 61, 127–136. Wang,L. and Jiang,T. (1994) On the complexity of multiple sequence align- ment. J. Comput. Biol., 337–348. pages Zhu,H. et al. (2016) A novel approach to multiple sequence alignment using multiobjective evolutionary algorithm based on decomposition. IEEE J. Biomed. Health Inform., 20, 717–727. M2Align 3017 Downloaded from https://academic.oup.com/bioinformatics/article/33/19/3011/3852082 by Cape Town University user on 20 July 2026 (PDF p. 7)
