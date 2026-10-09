# Improving spliced alignment by modeling splice sites with deep learning

- Work ID: `b-5bea1ac879a5`
- Asset ID: `a-9a08bbfab6af59a8`
- Source PDF: `literature/academic-papers-processed/Improving spliced alignment by modeling splice sites with deep learning.pdf`
- SHA-256: `9a08bbfab6af59a80c2825125b8afce5de8187a07e1e1748fe461fbf6fef584b`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- Minisplice uses a small one-dimensional convolutional neural network to score candidate splice sites. (PDF p. 1).
- Modified minimap2 and miniprot use precomputed splice scores during residue alignment. (PDF p. 3).
- The authors report improved junction accuracy for noisy RNA reads and proteins with distant homology. (PDF p. 1).

## Objectives

- The authors aim to build a splice model that is more capable than a position weight matrix and remains easy to deploy. (PDF p. 3).
- They seek a small, fast model that works across multiple species. (PDF p. 6).

## Arguments

- Splice signals help distinguish alignments with similar residue scores. The authors state that this matters particularly for divergent sequences. (PDF p. 2).
- Position weight matrices cannot capture dependencies between positions or regulatory motifs without fixed positions. (PDF p. 2).
- The authors argue that very large models can impose unnecessary computation when the task is limited to splice-site prediction. (PDF p. 2).

## Analysis

- The transformed score compares the empirical probability of a candidate site with a null model that gives all GT or AG sites equal probability. (PDF p. 5).
- The authors infer from internal activations that the model uses longer-range exon composition as well as nearby splice signals. (PDF p. 14).
- The authors estimate that a 1% false-positive rate would produce 3.75 million false donor predictions in a mammalian genome. Splice predictions therefore require additional evidence. (PDF p. 14).

## Methods

- The workflow trains a model, calibrates its outputs with gene annotations, predicts genome-wide GT and AG scores, and supplies those scores to an aligner. (PDF p. 3).
- Calibration divides raw scores into 50 bins by default. Each bin uses annotated and unannotated site counts to estimate an empirical probability. (PDF p. 5).
- The score uses twice the base-2 logarithm of the probability ratio to match the BLOSUM scale used by miniprot. (PDF p. 5).
- Minimap2 incorporates donor and acceptor scores in its spliced dynamic programming recurrence. Miniprot uses the same score functions in a more complex recurrence. (PDF p. 5).

## Applications

- The tools support mRNA-to-genome and protein-to-genome alignment for gene annotation. (PDF p. 3).
- Aligner input is a tab-delimited splice-score file. The aligners can accept scores from other prediction methods. (PDF p. 5).

## Optimization

- The reported model has 7026 parameters. (PDF p. 1).
- Genome-wide score precomputation separates splice prediction from alignment. A model trained across species reduces the need for repeated training. (PDF p. 3).
- Minisplice is implemented in C and requires only zlib as an external dependency. (PDF p. 5).

## Evaluation and testing

- Model evaluation uses ROC curves and a scaled restricted area under the curve. The selected region has sensitivity above 50% and a false-positive rate below 10%. (PDF p. 6).
- The final model is trained on six insect genomes from five orders and seven vertebrate genomes. (PDF p. 6).
- Alignment evaluation includes human long-read RNA sequencing and cross-species protein datasets. (PDF p. 1).
- Figure 9 stratifies junction accuracy by alignment identity for zebrafish proteins aligned to human and for human HG002 direct-RNA reads. (PDF p. 14).

## Results

- The authors report that the model captures conserved splice signals across phyla and reveals GC-rich introns in mammals and birds. (PDF p. 1).
- The authors report substantial junction-accuracy gains, particularly for noisy long RNA reads and distant protein homologs. The supplied abstract gives no numerical gain. (PDF p. 1).

## Limitations and uncertainty

- The model is intended for simple deployment. The authors do not aim to match the best splice predictors, which have far more parameters. (PDF p. 3).
- No plant model was trained. (PDF p. 6).
- Preference for well-scored GT–AG sites can cause errors at introns with other splice signals. (PDF p. 14).
- Scores come from the reference genome and do not account for sample mutations that alter splice signals. (PDF p. 14).

## References

1. Albaradei S, Magana-Mora A, Thafar M, Uludag M, Bajic VB, et al. Splice2Deep: an ensemble of deep convolutional neural networks for improved splice site prediction in genomic DNA. Gene. 2020;763S:100035. (PDF p. 15)
2. Amit M, Donyo M, Hollander D, Goren A, Kim E, et al. Diﬀerential gc content between exons and introns establishes distinct strategies of splice-site recognition. Cell Rep. 2012;1:543–56. (PDF p. 15)
3. Berakdar F, Wu TD, Zhu T, Samadi M, Vats P. DeepSAP: improved RNA-Seq alignment by integrating transcriptome guidance with transformer-based splice junction scoring. bioRxiv, 2025. p. 2025.04.23.650072. (PDF p. 15)
4. Bernardi G, Olofsson B, Filipski J, Zerial M, Salinas J, Cuny G, et al. The mosaic genome of warm-blooded vertebrates. Science. 1985;228:953–8. (PDF p. 15)
5. Birney E, Clamp M, Durbin R. GeneWise and Genomewise. Genome Res. 2004;14:988–95. (PDF p. 15)
6. Brendel V, Kleﬀe J. Prediction of locally optimal splice sites in plant pre-mRNA with applications to gene identiﬁcation in arabidopsis thaliana genomic DNA. Nucleic Acids Res. 1998;26:4748–57. (PDF p. 15)
7. Brendel V, Xing L, Zhu W. Gene structure prediction from consensus spliced alignment of multiple ESTs matching the same genomic locus. Bioinformatics. 2004;20:1157–69. (PDF p. 15)
8. Brixi G, Durrant MG, Ku J, Poli M, Brockman G, et al. Genome modeling and design across all domains of life with evo 2. bioRxiv, 2025. p. 2025.02.18.638918. (PDF p. 15)
9. Burge C, Karlin S. Prediction of complete gene structures in human genomic dna. J Mol Biol. 1997;268:78–94. (PDF p. 15)
10. Capitanchik C, Wilkins OG, Wagner N, Gagneur J, Ule J. From computational models of the splicing code to regulatory mechanisms and therapeutic implications. Nat Rev Genet. 2025;26:171–90. (PDF p. 15)
11. Chao K-H, Mao A, Salzberg SL, Pertea M. Splam: a deep-learning-based splice site predictor that improves spliced alignments. Genome Biol. 2024;25:243. (PDF p. 15)
12. Chen K, Zhou Y, Ding M, Wang Y, Ren Z, Yang Y. Self-supervised learning on millions of primary RNA sequences from 72 vertebrates improves sequence-based RNA splicing prediction. Brief Bioinform. 2024;25:bbae163. (PDF p. 15)
13. Choquet K, Patop IL, Churchman LS. The regulation and function of post-transcriptional RNA splicing. Nat Rev Genet. 2025;26:378–94. (PDF p. 15)
14. Dalla-Torre H, Gonzalez L, Mendoza-Revilla J, Lopez Carranza N, Grzywaczewski AH, et al. Nucleotide transformer: building and evaluating robust foundation models for human genomics. Nat Methods. 2025;22:287–97. (PDF p. 15)
15. Du X, Yao Y, Diao Y, Zhu H, Zhang Y, Li S. DeepSS: exploring splice site motif through convolutional neural network directly from DNA sequence. IEEE Access. 2018;6:32958–78. (PDF p. 15)
16. Gabriel L, Becker F, Hoﬀ KJ, Stanke M. Tiberius: end-to-end deep learning with an hmm for gene prediction. Bioinfor- matics. 2024;40:btae685. (PDF p. 15)
17. GotohO.Directmappingandalignmentofproteinsequencesontogenomicsequence.Bioinformatics.2008;24:2438– 44. (PDF p. 15)
18. Gotoh O. Spaln3: improvement in speed and accuracy of genome mapping and spliced alignment of protein query sequences. Bioinformatics. 2024;40:btae517. (PDF p. 15)
19. Gremme G, Brendel V, Sparks ME, Kurtz S. Engineering a software tool for gene structure prediction in higher organisms. Inf Softw Technol. 2005;47(15):965–78. (PDF p. 15)
20. Henikoﬀ S, Henikoﬀ JG. Amino acid substitution matrices from protein blocks. Proc Natl Acad Sci USA. 1992;89:10915– 9. (PDF p. 15)
21. Holst F, Bolger A, Günther C, Maß J, Triesch S, et al. Helixer–de novo prediction of primary eukaryotic gene models combining deep learning and a hidden markov model. bioRxiv, 2023: p. 2023.02.06.527280. (PDF p. 15)
22. Irimia M, Roy SW. Evolutionary convergence on highly-conserved 3’ intron structures in intron-poor eukaryotes and insights into the ancestral eukaryotic genome. PLoS Genet. 2008;4:e1000148. (PDF p. 15)
23. Iwata H, Gotoh O. Comparative analysis of information contents relevant to recognition of introns in many species. BMC Genomics. 2011;12:45. (PDF p. 15)
24. Iwata H, Gotoh O. Benchmarking spliced alignment programs including spaln2, an extended version of Spaln that incorporates additional species-speciﬁc features. Nucleic Acids Res. 2012;40:e161. Yang et al. Algorithms for Molecular Biology(2026)21:1 Page 16 of 16 (PDF p. 15)
25. Jaganathan K, Kyriazopoulou Panagiotopoulou S, McRae JF, Darbandi SF, Knowles D, et al. Predicting splicing from primary sequence with deep learning. Cell. 2019;176:535-548.e24. (PDF p. 16)
26. Kapustin Y, Souvorov A, Tatusova T, Lipman D. Splign: algorithms for computing spliced alignments with identiﬁcation of paralogs. Biol Direct. 2008;3:20. (PDF p. 16)
27. Kent WJ. BLAT-the BLAST-like alignment tool. Genome Res. 2002;12:656–64. (PDF p. 16)
28. Keren H, Lev-Maor G, Ast G. Alternative splicing and evolution: diversiﬁcation, exon deﬁnition and function. Nat Rev Genet. 2010;11:345–55. (PDF p. 16)
29. Li H. Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics. 2018;34:3094–100. (PDF p. 16)
30. Li H. Identifying centromeric satellites with dna-brnn. Bioinformatics. 2019;35:4408–10. (PDF p. 16)
31. Li H. Protein-to-genome alignment with miniprot. Bioinformatics. 2023;39:014. (PDF p. 16)
32. McCue K, Burge CB. An interpretable model of pre-mRNA splicing for animal and plant genes. Sci Adv. 2024;10:eadn1547. (PDF p. 16)
33. Nguyen E, Poli M, Faizi M, Thomas A, Birch-Sykes C, et al. HyenaDNA: long-range genomic sequence modeling at single nucleotide resolution. arXiv:2306.15794. 2023 (PDF p. 16)
34. Reese MG, Eeckman FH, Kulp D, Haussler D. Improved splice site detection in genie. J Comput Biol. 1997;4:311–23. (PDF p. 16)
35. Sibley CR, Blazquez L, Ule J. Lessons from non-canonical splicing. Nat Rev Genet. 2016;17:407–21. (PDF p. 16)
36. Slater GSC, Birney E. Automated generation of heuristics for biological sequence comparison. BMC Bioinform. 2005;6:31. (PDF p. 16)
37. Staden R. Computer methods to locate signals in nucleic acid sequences. Nucleic Acids Res. 1984;12:505–19. (PDF p. 16)
38. Tan L, Xing D, Chang C-H, Li H, Xie XS. Three-dimensional genome structures of single diploid human cells. Science. 2018;361:924–8. (PDF p. 16)
39. Usuka J, Brendel V. Gene structure prediction by spliced alignment of genomic DNA with protein sequences: increased accuracy by diﬀerential splice site scoring. J Mol Biol. 2000;297:1075–85. (PDF p. 16)
40. Wang D, Yu J. Both size and GC-content of minimal introns are selected in human populations. PLoS ONE. 2011;6:e17945. (PDF p. 16)
41. Wu TD, Nacu S. Fast and SNP-tolerant detection of complex variants and splicing in short reads. Bioinformatics. 2010;26:873–81. (PDF p. 16)
42. Wu TD, Watanabe CK. GMAP: a genomic mapping and alignment program for mRNA and EST sequences. Bioinfor- matics. 2005;21:1859–75. (PDF p. 16)
43. Xia Y, Jin Z, Zhang C, Ouyang L, Dong Y, et al. TAGET: a toolkit for analyzing full-length transcripts from long-read sequencing. Nat Commun. 2023;14:5935. (PDF p. 16)
44. Xie WJ, Meng L, Liu S, Zhang L, Cai X, Gao YQ. Structural modeling of chromatin integrates genome features and reveals chromosome folding principle. Sci Rep. 2017;7:2818. (PDF p. 16)
45. Xu C, Bao S, Wang Y, Li W, Chen H, Shen Y, et al. Reference-informed prediction of alternative splicing and splicing- altering mutations from sequences. Genome Res. 2024;34:1052–65. (PDF p. 16)
46. Yeo G, Burge CB. Maximum entropy modeling of short sequence motifs with applications to rna splicing signals. J Comput Biol. 2004;11:377–94. (PDF p. 16)
47. You N, Liu C, Gu Y, Wang R, Jia H, et al. Splicetransformer predicts tissue-speciﬁc splicing linked to human diseases. Nat Commun. 2024;15:9129. (PDF p. 16)
48. Zabardast A, Tamer EG, Son YA, Yılmaz A. An automated framework for evaluation of deep learning models for splice site predictions. Sci Rep. 2023;13:10221. (PDF p. 16)
49. Zeng T, Li YI. Predicting RNA splicing from DNA sequence using Pangolin. Genome Biol. 2022;23:103. (PDF p. 16)
50. Zhang J, Kuo CCJ, Chen L. GC content around splice sites aﬀects splicing through pre-mRNA secondary structures. BMC Genomics. 2011;12:90. (PDF p. 16)
51. Zhang Y, Liu X, MacLeod J, Liu J. Discerning novel splice junctions derived from rna-seq alignment: a deep learning approach. BMC Genomics. 2018;19:971. (PDF p. 16)
52. Zheng Z, Yu X, Chen L, Lee Y-L, Xin C, et al. Clair3-RNA: a deep learning-based small variant caller for long-read RNA sequencing data. bioRxiv, 2025. p. 2024.11.17.624050. Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional aﬃliations. (PDF p. 16)
