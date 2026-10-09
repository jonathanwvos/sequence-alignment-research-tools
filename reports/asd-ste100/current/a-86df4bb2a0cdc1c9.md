# The design and construction of reference pangenome graphs with minigraph

- Work ID: `b-7552d7a02975`
- Asset ID: `a-86df4bb2a0cdc1c9`
- Source PDF: `literature/academic-papers-processed/The design and construction of reference pangenome graphs with minigraph.pdf`
- SHA-256: `86df4bb2a0cdc1c9c0d7f87d3045b9036f070d89ce3e51626447f399853c49fb`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors develop minigraph for the incremental construction and alignment of reference pangenome graphs. (PDF p. 1).
- Minigraph identifies structural variations longer than 50 bp from assemblies and integrates them as alternative graph paths. (PDF p. 3).

## Objectives

- Construct comprehensive reference pangenome graphs from multiple assembled vertebrate genomes at chromosome scale. (PDF p. 1).

## Arguments

- Representing structural variants in a reference graph eliminates reference bias during read mapping and variant calling. (PDF p. 3).

## Analysis

- Graph size, insertion counts, and chaining densities are evaluated across primate and human haplotype collections. (PDF p. 16).

## Methods

- Sequence assemblies are mapped to an evolving bidirected graph using minimizer chaining and graph alignment. (PDF p. 16).
- Unaligned segments longer than 50 bp are iteratively inserted into the graph as bubble structures. (PDF p. 3).

## Applications

- Reference pangenome construction for human and primate genomics and structural variant genotyping. (PDF p. 3).

## Optimization

- Minimizer-based distance indexing allows rapid co-linear chaining across graph nodes. (PDF p. 16).

## Evaluation and testing

- Minigraph constructs human pangenome graphs from 20 haplotypes and primate graphs from four species. (PDF p. 3).

## Results

- Constructs chromosome-scale human pangenome graphs in hours, discovering thousands of non-reference structural variants. (PDF p. 3).

## Limitations and uncertainty

- Minigraph discards small variants under 50 bp and single nucleotide polymorphisms to maintain graph tractability. (PDF p. 3).

## References

1. Schneider VA, Graves-Lindsay T, Howe K, Bouk N, Chen H-C, Kitts PA, Murphy TD, Pruitt KD, Thibaud-Nissen F, Albracht D, Fulton RS, Kremitzki M, Magrini V, Markovic C, McGrath S, Steinberg KM, Auger K, Chow W, Collins J, Harden G, Hubbard T, Pelan S, Simpson JT, Threadgold G, Torrance J, Wood JM, Clarke L, Koren S, Boitano M, Peluso P, Li H, Chin C-S, Phillippy AM, Durbin R, Wilson RK, Flicek P, Eichler EE, Church DM. Evaluation of GRCh38 and de novo haploid genome assemblies demonstrates the enduring quality of the reference assembly. Genome Res. 2017;27(5):849–64. https://doi.org/10.1101/gr.213611.116. (PDF p. 17)
2. Huddleston J, Chaisson MJP, Steinberg KM, Warren W, Hoekzema K, Gordon D, Graves-Lindsay TA, Munson KM, Kronenberg ZN, Vives L, Peluso P, Boitano M, Chin C-S, Korlach J, Wilson RK, Eichler EE. Discovery and genotyping of structural variation from long-read haploid genome sequence data. Genome Res. 2017;27(5):677–85. https://doi. org/10.1101/gr.214007.116. (PDF p. 17)
3. Eichler EE, Flint J, Gibson G, Kong A, Leal SM, Moore JH, Nadeau JH. Missing heritability and strategies for finding the underlying causes of complex disease. Nat Rev Genet. 2010;11(6):446–50. https://doi.org/10.1038/nrg2809. (PDF p. 17)
4. Li H, Bloom JM, Farjoun Y, Fleharty M, Gauthier L, Neale B, MacArthur D. A synthetic-diploid benchmark for accurate variant-calling evaluation. Nat Methods. 2018;15(8):595–7. https://doi.org/10.1038/s41592-018-0054-7. (PDF p. 17)
5. Wenger AM, Peluso P, Rowell WJ, Chang P-C, Hall RJ, Concepcion GT, Ebler J, Fungtammasan A, Kolesnikov A, Olson ND, et al. Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome. Nat Biotechnol. 2019;37(10):1155–62. https://doi.org/10.1038/s41587-019-0217-9. (PDF p. 17)
6. Audano PA, Sulovari A, Graves-Lindsay TA, Cantsilieris S, Sorensen M, Welch AE, Dougherty ML, Nelson BJ, Shah A, Dutcher SK, Warren WC, Magrini V, McGrath SD, Li YI, Wilson RK, Eichler EE. Characterizing the major structural variant alleles of the human genome. Cell. 2019;176(3):663–67519. https://doi.org/10.1016/j.cell.2018.12.019. (PDF p. 17)
7. Computational Pan-Genomics Consortium. Computational pan-genomics: status, promises and challenges. Brief Bioinform. 2016;19(1):118–35. https://doi.org/10.1093/bib/bbw089. (PDF p. 17)
8. Mäkinen V, Navarro G, Sirén J, Välimäki N. Storage and retrieval of highly repetitive sequence collections. J Comput Biol. 2010;17(3):281–308. https://doi.org/10.1089/cmb.2009.0169. (PDF p. 17)
9. Liu B, Zhu D, Wang Y. deBWT: parallel construction of Burrows–Wheeler Transform for large collection of genomes with de bruijn-branch encoding. Bioinformatics. 2016;32(12):174–82. https://doi.org/10.1093/bioinformatics/btw266. (PDF p. 17)
10. Boucher C, Gagie T, Kuhnle A, Langmead B, Manzini G, Mun T. Prefix-free parsing for building big BWTs. Algoritm Mol Biol. 2019;14(1):13. https://doi.org/10.1186/s13015-019-0148-5. (PDF p. 17)
11. Na JC, Kim H, Park H, Lecroq T, Léonard M, Mouchard L, Park K. FM-index of alignment: a compressed index for similar strings. Theor Comput Sci. 2016;638:159–70. https://doi.org/10.1016/j.tcs.2015.08.008. (PDF p. 17)
12. Vernikos G, Medini D, Riley DR, Tettelin H. Ten years of pan-genome analyses. Curr Opin Microbiol. 2015;23:148–54. https://doi.org/10.1016/j.mib.2014.11.016. (PDF p. 17)
13. Marcus S, Lee H, Schatz MC. SplitMEM: a graphical algorithm for pan-genome analysis with suffix skips. Bioinformatics. 2014;30(24):3476–83. https://doi.org/10.1093/bioinformatics/btu756. (PDF p. 17)
14. Baier U, Beller T, Ohlebusch E. Graphical pan-genome analysis with compressed suffix trees and the Burrows–Wheeler transform. Bioinformatics. 2015;32(4):497–504. https://doi.org/10.1093/bioinformatics/btv603. (PDF p. 17)
15. Beller T, Ohlebusch E. A representation of a compressed de Bruijn graph for pan-genome analysis that enables search. Algoritm Mol Biol. 2016;11:20. https://doi.org/10.1186/s13015-016-0083-7. (PDF p. 17)
16. Chikhi R, Limasset A, Jackman S, Simpson JT, Medvedev P. On the representation of de Bruijn graphs. J Comput Biol. 2015;22(5):336–52. https://doi.org/10.1089/cmb.2014.0160. (PDF p. 17)
17. Minkin I, Pham S, Medvedev P. TwoPaCo: an efficient algorithm to build the compacted de Bruijn graph from many complete genomes. Bioinformatics. 2017;33(24):4024–32. https://doi.org/10.1093/bioinformatics/btw609. (PDF p. 17)
18. Chikhi R, Limasset A, Medvedev P. Compacting de Bruijn graphs from sequencing data quickly and in low memory. Bioinformatics. 2016;32(12):201–8. https://doi.org/10.1093/bioinformatics/btw279. (PDF p. 17)
19. Almodaresi F, Pandey P, Patro R. Rainbowfish: a succinct colored de Bruijn graph representation. In: Schwartz R, Reinert K, editors. 17th International Workshop on Algorithms in Bioinformatics (WABI 2017), Leibniz International Li et al. Genome Biology (2020) 21:265 Page 18 of 19 Proceedings in Informatics (LIPIcs), vol. 88. Dagstuhl, Germany: Schloss Dagstuhl–Leibniz-Zentrum fuer Informatik; 2017. p. 18–11815. https://doi.org/10.4230/LIPIcs.WABI.2017.18. (PDF p. 17)
20. Iqbal Z, Caccamo M, Turner I, Flicek P, McVean G. De novo assembly and genotyping of variants using colored de Bruijn graphs. Nat Genet. 2012;44(2):226–32. https://doi.org/10.1038/ng.1028. (PDF p. 18)
21. Muggli MD, Alipanahi B, Boucher C. Building large updatable colored de Bruijn graphs via merging. Bioinformatics. 2019;35(14):51–60. https://doi.org/10.1093/bioinformatics/btz350. (PDF p. 18)
22. Holley G, Melsted P. Bifrost – highly parallel construction and indexing of colored and compacted de Bruijn graphs. Genome Biol. 2020;21:249. (PDF p. 18)
23. Liu B, Guo H, Brudno M, Wang Y. deBGA: read alignment with de Bruijn graph-based seed and extension. Bioinformatics. 2016;32(21):3224–32. https://doi.org/10.1093/bioinformatics/btw371. (PDF p. 18)
24. Almodaresi F, Sarkar H, Srivastava A, Patro R. A space and time-efficient index for the compacted colored de Bruijn graph. Bioinformatics. 2018;34(13):169–77. https://doi.org/10.1093/bioinformatics/bty292. (PDF p. 18)
25. Sirén J, Garrison E, Novak AM, Paten B, Durbin R. Haplotype-aware graph indexes. Bioinformatics. 2019;36:400–7. https://doi.org/10.1093/bioinformatics/btz575. (PDF p. 18)
26. Dilthey A, Cox C, Iqbal Z, Nelson MR, McVean G. Improved genome inference in the MHC using a population reference graph. Nat Genet. 2015;47(6):682–8. https://doi.org/10.1038/ng.3257. (PDF p. 18)
27. Dilthey AT, Mentzer AJ, Carapito R, Cutland C, Cereb N, Madhi SA, Rhie A, Koren S, Bahram S, McVean G, et al. HLA*LA–HLA typing from linearly projected graph alignments. Bioinformatics. 2019;35(21):4394–6. https://doi.org/ 10.1093/bioinformatics/btz235. (PDF p. 18)
28. Danecek P, Auton A, Abecasis G, Albers CA, Banks E, DePristo MA, Handsaker RE, Lunter G, Marth GT, Sherry ST, McVean G, Durbin R, 1000 Genomes Project Analysis Group. The variant call format and vcftools. Bioinformatics. 2011;27(15):2156–8. https://doi.org/10.1093/bioinformatics/btr330. (PDF p. 18)
29. Eggertsson HP, Jonsson H, Kristmundsdottir S, Hjartarson E, Kehr B, Masson G, Zink F, Hjorleifsson KE, Jonasdottir A, Jonasdottir A, Jonsdottir I, Gudbjartsson DF, Melsted P, Stefansson K, Halldorsson BV. Graphtyper enables population-scale genotyping using pangenome graphs. Nat Genet. 2017;49(11):1654–60. https://doi.org/10.1038/ ng.3964. (PDF p. 18)
30. Rakocevic G, Semenyuk V, Lee W-P, Spencer J, Browning J, Johnson IJ, Arsenijevic V, Nadj J, Ghose K, Suciu MC, et al. Fast and accurate genomic analyses using genome graphs. Nat Genet. 2019;51(2):354–62. https://doi.org/10. 1038/s41588-018-0316-4. (PDF p. 18)
31. Sibbesen JA, Maretty L, Danish Pan-Genome Consortium, Krogh A. Accurate genotyping across variant classes and lengths using variant graphs. Nat Genet. 2018;50(7):1054–9. https://doi.org/10.1038/s41588-018-0145-5. (PDF p. 18)
32. Biederstedt E, Oliver JC, Hansen NF, Jajoo A, Dunn N, Olson A, Busby B, Dilthey AT. NovoGraph: human genome graph construction from multiple long-read de novo assemblies. F1000Res. 2018;7:1391. https://doi.org/10.12688/ f1000research.15895.2. (PDF p. 18)
33. Eggertsson HP, Kristmundsdottir S, Beyter D, Jonsson H, Skuladottir A, Hardarson MT, Gudbjartsson DF, Stefansson K, Halldorsson BV, Melsted P. Graphtyper2 enables population-scale genotyping of structural variation using pangenome graphs. Nat Commun. 2019;10(1):5402. https://doi.org/10.1038/s41467-019-13341-9. (PDF p. 18)
34. Li H. Minigraph: a sequence-to-graph mapper and pangenome graph generator. 2020. https://doi.org/10.5281/ zenodo.4016798. Accessed 12 Mar 2020. (PDF p. 18)
35. Li H. Minimap and miniasm: fast mapping and de novo assembly for noisy long sequences. Bioinformatics. 2016;32(14):2103–10. https://doi.org/10.1093/bioinformatics/btw152. (PDF p. 18)
36. Pevzner PA, Tang H, Waterman MS. An Eulerian path approach to DNA fragment assembly. Proc Natl Acad Sci U S A. 2001;98(17):9748–53. https://doi.org/10.1073/pnas.171285098. (PDF p. 18)
37. Gnerre S, Maccallum I, Przybylski D, Ribeiro FJ, Burton JN, Walker BJ, Sharpe T, Hall G, Shea TP, Sykes S, Berlin AM, Aird D, Costello M, Daza R, Williams L, Nicol R, Gnirke A, Nusbaum C, Lander ES, Jaffe DB. High-quality draft assemblies of mammalian genomes from massively parallel sequence data. Proc Natl Acad Sci U S A. 2011;108(4): 1513–8. https://doi.org/10.1073/pnas.1017351108. (PDF p. 18)
38. Rautiainen M, Marschall T. GraphAligner: rapid and versatile sequence-to-graph alignment. Genome Biol. 2020;21: 253. (PDF p. 18)
39. Garrison E, Sirén J, Novak AM, Hickey G, Eizenga JM, Dawson ET, Jones W, Garg S, Markello C, Lin MF, Paten B, Durbin R. Variation graph toolkit improves read mapping by representing genetic variation in the reference. Nat Biotechnol. 2018;36(9):875–9. https://doi.org/10.1038/nbt.4227. (PDF p. 18)
40. Li H. Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics. 2018;34(18):3094–100. https://doi.org/ 10.1093/bioinformatics/bty191. (PDF p. 18)
41. Ono Y, Asai K, Hamada M. PBSIM: PacBio reads simulator–toward accurate genome assembly. Bioinformatics. 2013;29(1):119–21. https://doi.org/10.1093/bioinformatics/bts649. (PDF p. 18)
42. Lee C, Grasso C, Sharlow MF. Multiple sequence alignment using partial order graphs. Bioinformatics. 2002;18(3): 452–64. https://doi.org/10.1093/bioinformatics/18.3.452. (PDF p. 18)
43. Robinson JT, Thorvaldsdóttir H, Winckler W, Guttman M, Lander ES, Getz G, Mesirov JP. Integrative genomics viewer. Nat Biotechnol. 2011;29(1):24–6. https://doi.org/10.1038/nbt.1754. (PDF p. 18)
44. Garg S, Fungtammasan A, Carroll A, Chou M, Schmitt A, Zhou X, Mac S, Peluso P, Hatas E, Ghurye J, Maguire J, Mahmoud M, Cheng H, Heller D, Zook JM, Moemke T, Marschall T, Sedlazeck FJ, Aach J, Chin C-S, Church GM, Li H. Efficient chromosome-scale haplotype-resolved assembly of human genomes. bioRxiv. 2019. https://doi.org/ 10.1101/810341. (PDF p. 18)
45. Mathews LM, Chi SY, Greenberg N, Ovchinnikov I, Swergold GD. Large differences between LINE-1 amplification rates in the human and chimpanzee lineages. Am J Hum Genet. 2003;72(3):739–48. https://doi.org/10.1086/368275. (PDF p. 18)
46. Amemiya HM, Kundaje A, Boyle AP. The ENCODE blacklist: identification of problematic regions of the genome. Sci Rep. 2019;9(1):9354. https://doi.org/10.1038/s41598-019-45839-z. (PDF p. 18)
47. Depristo MA, Banks E, Poplin R, Garimella KV, Maguire JR, Hartl C, Philippakis AA, Del Angel G, Rivas MA, Hanna M, McKenna A, Fennell TJ, Kernytsky AM, Sivachenko AY, Cibulskis K, Gabriel SB, Altshuler D, Daly MJ. A framework for variation discovery and genotyping using next-generation dna sequencing data. Nat Genet. 2011;43(5):491–8. https://doi.org/10.1038/ng.806. Li et al. Genome Biology (2020) 21:265 Page 19 of 19 (PDF p. 18)
48. Llamas B, Narzisi G, Schneider V, Audano P, Biederstedt E, Blauvelt L, Bradbury P, Chang X, Chin C, Fungtammasan A, Clarke W, Cleary A, Ebler J, Eizenga J, Sibbesen J, Markello C, Garrison E, Garg S, Hickey G, Lazo G, Lin M, Mahmoud M, Marschall T, Minkin I, Monlong J, Musunuri R, Sagayaradj S, Novak A, Rautiainen M, Regier A, Sedlazeck F, Siren J, Souilmi Y, Wagner J, Wrightsman T, Yokoyama T, Zeng Q, Zook J, Paten B, Busby B. A strategy for building and using a human reference pangenome [version 1; peer review: 1 approved, 1 approved with reservations]. F1000Research. 2019;8:1751. https://doi.org/10.12688/f1000research.19630.1. (PDF p. 19)
49. Jain C, Misra S, Zhang H, Dilthey AT, Aluru S. Accelerating sequence alignment to graphs. In: 2019 IEEE International Parallel and Distributed Processing Symposium, IPDPS 2019, May 20-24, 2019. Rio de Janeiro, Brazil: IEEE; 2019. p. 451–61. (PDF p. 19)
50. Antipov D, Korobeynikov A, McLean JS, Pevzner PA. hybridspades: an algorithm for hybrid assembly of short and long reads. Bioinformatics. 2016;32(7):1009–15. (PDF p. 19)
51. Rautiainen M, Mäkinen V, Marschall T. Bit-parallel sequence-to-graph alignment. Bioinformatics. 2019;35(19): 3599–607. (PDF p. 19)
52. Jain C, Zhang H, Gao Y, Aluru S. On the complexity of sequence-to-graph alignment. J Comput Biol. 2020;27(4): 640–54. (PDF p. 19)
53. Pritt J, Chen N-C, Langmead B. Forge: prioritizing variants for graph genomes. Genome Biol. 2018;19(1):220. https://doi.org/10.1186/s13059-018-1595-x. (PDF p. 19)
54. Hickey G, Heller D, Monlong J, Sibbesen JA, Sirén J, Eizenga J, Dawson ET, Garrison E, Novak AM, Paten B. Genotyping structural variants in pangenome graphs using the vg toolkit. Genome Biol. 2020;21(1):35. https://doi. org/10.1186/s13059-020-1941-7. (PDF p. 19)
55. Chen S, Krusche P, Dolzhenko E, Sherman RM, Petrovski R, Schlesinger F, Kirsche M, Bentley DR, Schatz MC, Sedlazeck FJ, et al. Paragraph: a graph-based structural variant genotyper for short-read sequence data. Genome Biol. 2019;20(1):291. https://doi.org/10.1186/s13059-019-1909-7. (PDF p. 19)
56. Abouelhoda MI, Ohlebusch E. A local chaining algorithm and its applications in comparative genomics. In: Benson G, Page RDM, editors. Proceedings Algorithms in Bioinformatics, Third International Workshop, WABI 2003, September 15-20, 2003. Budapest, Hungary: Springer; 2003. p. 1–16. https://doi.org/10.1007/978-3-540-39763-2_1. (PDF p. 19)
57. Otto C, Hoffmann S, Gorodkin J, Stadler PF. Fast local fragment chaining using sum-of-pair gap costs. Algoritm Mol Biol. 2011;6:4. https://doi.org/10.1186/1748-7188-6-4. (PDF p. 19)
58. Ruzzo WL, Tompa M. A linear time algorithm for finding all maximal scoring subsequences. In: Lengauer T, Schneider R, Bork P, Brutlag DL, Glasgow JI, Mewes H, Zimmer R, editors. Proceedings of the Seventh International Conference on Intelligent Systems for Molecular Biology, August 6-10, 1999. Heidelberg, Germany: AAAI; 1999. p. 234–41. (PDF p. 19)
59. Suzuki H, Kasahara M. Introducing difference recurrence relations for faster semi-global alignment of long sequences. BMC Bioinformatics. 2018;19:45. https://doi.org/10.1186/s12859-018-2014-8. (PDF p. 19)
60. Tarailo-Graovac M, Chen N. Using repeatmasker to identify repetitive elements in genomic sequences. Curr Protoc Bioinforma. 2009;Chapter 4:4–10. (PDF p. 19)
61. Morgulis A, Gertz EM, Schäffer AA, Agarwala R. A fast and symmetric dust implementation to mask low-complexity DNA sequences. J Comput Biol. 2006;13(5):1028–40. https://doi.org/10.1089/cmb.2006.13.1028. (PDF p. 19)
62. Seo J-S, Rhie A, Kim J, Lee S, Sohn M-H, Kim C-U, Hastie A, Cao H, Yun J-Y, Kim J, Kuk J, Park GH, Kim J, Ryu H, Kim J, Roh M, Baek J, Hunkapiller MW, Korlach J, Shin J-Y, Kim C. De novo assembly and phasing of a Korean human genome. Nature. 2016;538(7624):243–7. https://doi.org/10.1038/nature20098. (PDF p. 19)
63. Kronenberg ZN, Fiddes IT, Gordon D, Murali S, Cantsilieris S, Meyerson OS, Underwood JG, Nelson BJ, Chaisson MJP, Dougherty ML, Munson KM, Hastie AR, Diekhans M, Hormozdiari F, Lorusso N, Hoekzema K, Qiu R, Clark K, Raja A, Welch AE, Sorensen M, Baker C, Fulton RS, Armstrong J, Graves-Lindsay TA, Denli AM, Hoppe ER, Hsieh P, Hill CM, Pang AWC, Lee J, Lam ET, Dutcher SK, Gage FH, Warren WC, Shendure J, Haussler D, Schneider VA, Cao H, Ventura M, Wilson RK, Paten B, Pollen A, Eichler EE. High-resolution comparative analysis of great ape genomes. Science. 2018;360(6393):eaar6343. https://doi.org/10.1126/science.aar6343. (PDF p. 19)
64. Gordon D, Huddleston J, Chaisson MJP, Hill CM, Kronenberg ZN, Munson KM, Malig M, Raja A, Fiddes I, Hillier LW, Dunn C, Baker C, Armstrong J, Diekhans M, Paten B, Shendure J, Wilson RK, Haussler D, Chin C-S, Eichler EE. Long-read sequence assembly of the gorilla genome. Science. 2016;352(6281):0344. https://doi.org/10. 1126/science.aae0344. Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. (PDF p. 19)
