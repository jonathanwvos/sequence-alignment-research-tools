# AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations

- Work ID: `w-16c1eb4df325`
- Asset ID: `a-16c1eb4df325aedf`
- Source PDF: `literature/academic-papers-processed/AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations.pdf`
- SHA-256: `16c1eb4df325aedff4585a2e8701de7c4f0961cbe2d3dc2fd0e36afa34ad0c78`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The study evaluates AlphaGenome for personal gene expression prediction using GTEx data. The author reports better prediction of expression direction than Enformer, with an odds ratio of 3.0. (PDF p. 2).
- AlphaGenome improved predictions for genes with nonlinear sequence-expression relationships. Its performance remained below that of classic models trained on personal data. (PDF p. 7).

## Objectives

- The author aims to compare AlphaGenome with Enformer, Elastic Net, and Random Forest for personal gene expression prediction. (PDF p. 3).
- The study examines nonlinear sequence-expression relationships and the marginal effects of variants on AlphaGenome predictions. (PDF p. 3).

## Arguments

- The author hypothesizes that improved architecture and expanded training data could improve personal expression prediction without individual-level training. (PDF p. 3).
- The author suggests that basepair resolution, longer sequence context, and multimodal training contribute to the observed improvement. This explanation is presented as a likely cause. (PDF p. 7).

## Analysis

- In the ABI3 case study, Random Forest and AlphaGenome agreed on the strongest variant effect but differed on other variants. The author interprets this as evidence that the models capture different nonlinear relationships. (PDF p. 6).

## Methods

- The benchmark used GTEx RNA-seq data from 953 individuals across 50 tissues. The normalized expression matrix contained 42,372 genes before sparsity filtering. (PDF p. 3).
- The nonlinear analysis compared Random Forest with Elastic Net and examined the top 300 nonlinear genes. The ABI3 case study assessed variant effects in a 20 kb region around the transcription start site. (PDF p. 6).

## Applications

Not stated in the extractable source pages.

## Optimization

Not stated in the extractable source pages.

## Evaluation and testing

- The study compared AlphaGenome with Enformer and with Elastic Net and Random Forest. It included a subset of genes with likely nonlinear sequence-expression relationships. (PDF p. 3).
- Figure 2 compares model predictions with observed expression and compares marginal mutation effects for ABI3. (PDF p. 6).

## Results

- The author reports that AlphaGenome improved expression-direction prediction over Enformer with an odds ratio of 3.0. Some negative prediction-observation correlations became positive. (PDF p. 2).
- Both Random Forest and AlphaGenome assigned the largest ABI3 effect to chr17:49,210,289 C>T. AlphaGenome responded minimally to chr17:49,213,451 A>G, which Random Forest considered important. (PDF p. 6).
- AlphaGenome identified two other mutations with normalized effects near 0.2 that Random Forest did not detect. (PDF p. 6).

## Limitations and uncertainty

- AlphaGenome remained less accurate than classic machine learning models trained directly on personal data. (PDF p. 7).
- At the time of the report, the author stated that inference-only API access and restrictions on downstream fine-tuning prevented training AlphaGenome on personal data. (PDF p. 7).

## References

1. Cookson, W., Liang, L., Abecasis, G., Moffatt, M. & Lathrop, M. Mapping complex disease traits with global gene expression. Nature Reviews Genetics 10, 184–194 (2009). (PDF p. 7)
2. Mackay, T. F. C., Stone, E. A. & Ayroles, J. F. The genetics of quantitative traits: challenges and prospects 10, 565–577. URL https://www.nature.com/articles/ nrg2612. Number: 8 Publisher: Nature Publishing Group. (PDF p. 7)
3. Gamazon, E. R. et al. A gene-based association method for mapping traits using reference transcriptome data 47, 1091–1098. URL https://www.nature.com/ articles/ng.3367. Publisher: Nature Publishing Group. (PDF p. 7)
4. Zhang, Z., Bae, Y. E., Bradley, J. R., Wu, L. & Wu, C. SUMMIT: An integrative approach for better transcriptomic data imputation improves causal gene iden- tification 13, 6336. URL https://www.nature.com/articles/s41467-022-34016-y. Publisher: Nature Publishing Group. (PDF p. 7)
5. Gusev, A. et al. Integrative approaches for large-scale transcriptome-wide asso- ciation studies 48, 245–252. URL https://www.nature.com/articles/ng.3506. Publisher: Nature Publishing Group. (PDF p. 7)
6. Stephan, J., Stegle, O. & Beyer, A. A random forest approach to capture genetic effects in the presence of population structure 6, 7432. URL https://www.nature. com/articles/ncomms8432. Publisher: Nature Publishing Group. (PDF p. 7)
7. Zhou, J. & Troyanskaya, O. G. Predicting effects of noncoding variants with deep learning–based sequence model. Nature methods 12, 931–934 (2015). 6 (PDF p. 7)
8. Agarwal, V. & Shendure, J. Predicting mRNA abundance directly from genomic sequence using deep convolutional neural networks 31, 107663. URL https:// www.sciencedirect.com/science/article/pii/S2211124720306161. (PDF p. 8)
9. Kelley, D. R. et al. Sequential regulatory activity prediction across chromosomes with convolutional neural networks 28, 739–750. (PDF p. 8)
10. Zhou, J. et al. Deep learning sequence-based ab initio prediction of variant effects on expression and disease risk. Nature genetics 50, 1171–1179 (2018). (PDF p. 8)
11. Avsec, . et al. Effective gene expression prediction from sequence by integrating long-range interactions 18, 1196–1203. URL https://www.nature.com/articles/ s41592-021-01252-x. Number: 10 Publisher: Nature Publishing Group. (PDF p. 8)
12. Linder, J., Srivastava, D., Yuan, H., Agarwal, V. & Kelley, D. R. Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation 57, 949–961. URL https://www.nature.com/articles/s41588-024-02053-6. Publisher: Nature Publishing Group. (PDF p. 8)
13. Avsec, . et al. AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model. URL https://www.biorxiv.org/content/10.1101/ 2025.06.25.661532v1. Pages: 2025.06.25.661532 Section: New Results. (PDF p. 8)
14. Huang, C. et al. Personal transcriptome variation is poorly explained by current genomic deep learning models 55, 2056–2059. URL https://www.nature.com/ articles/s41588-023-01574-w. Number: 12 Publisher: Nature Publishing Group. (PDF p. 8)
15. Sasse, A. et al. Benchmarking of deep neural networks for predicting personal gene expression from DNA sequence highlights shortcomings 55, 2060–2064. URL https://www.nature.com/articles/s41588-023-01524-6. Number: 12 Publisher: Nature Publishing Group. (PDF p. 8)
16. Drusinsky, S., Whalen, S. & Pollard, K. S. Deep-learning prediction of gene expression from personal genomes. URL https://www.biorxiv.org/content/10. 1101/2024.07.27.605449v1. Pages: 2024.07.27.605449 Section: New Results. (PDF p. 8)
17. Rastogi, R., Reddy, A. J., Chung, R. & Ioannidis, N. M. Fine-tuning sequence-to-expression models on personal genome and transcriptome data. URL https://www.biorxiv.org/content/10.1101/2024.09.23.614632v1. Pages: 2024.09.23.614632 Section: New Results. (PDF p. 8)
18. Lonsdale, J. et al. The genotype-tissue expression (GTEx) project 45, 580–585. URL https://www.nature.com/articles/ng.2653. Number: 6 Publisher: Nature Publishing Group. (PDF p. 8)
19. Kaplan, J. et al. Scaling laws for neural language models. URL http://arxiv.org/ abs/2001.08361. 2001.08361 [cs]. 7 (PDF p. 8)
20. OpenAI et al. GPT-4 technical report. URL http://arxiv.org/abs/2303.08774. 2303.08774 [cs]. [21] xAI. Grok 4 | xAI. URL https://x.ai/news/grok-4. (PDF p. 9)
21. Shendure, J. et al. Dna sequencing at 40: past, present and future. Nature 550, 345–353 (2017). (PDF p. 9)
22. DeepMind. AlphaGenome API additional terms of service. URL https:// deepmind.google.com/science/alphagenome/terms. Methods Data Preprocessing For RNA-seq data, normalized expression values (V10) were downloaded from the GTEx website, with no additional processing applied. For each gene, a tissue was excluded if more than 50% of expression values were missing. For personal genomes, phased whole-genome sequencing data (V9) were used. In non-deep learning mod- els, genetic variants from the two haplotypes were treated as separate features and concatenated. Both SNVs and indels were included, and variants with a minor allele frequency below 1% were filtered out. For AlphaGenome and Enformer, both haplo- type sequences were used as input, and the resulting outputs were averaged to produce final predictions. Use AlphaGenome and Enformer for Personal Expression Prediction For AlphaGenome, a 1 Mb window centered on the transcriptional start site (TSS) of each gene was used as input. The model outputs predictions over the same window at single-basepair resolution. For each gene, predicted expression values from the TSS to the transcriptional end site (TES) were averaged to represent that gene’s expression level. AlphaGenome’s half-window size of 500 Kb is sufficient to span the full gene body (TSS to TES) for the vast majority of genes; only 422 genes–approximately 0.7% of all GTEx genes–exceed 500 Kb in length. Enformer, by contrast, requires training to predict GTEx tissue-level expression. The same train-validation-test split as used in the Borzoi [12] model was adopted, where each GTEx gene was assigned to a set based on the genomic region closest to its TSS. A 196,608 bp window centered on the TSS was extracted from the reference genome and used as input to the pretrained Enformer to obtain an embedding. As with AlphaGenome, predicted values from TSS to TES were averaged to represent gene-level expression. The target values were defined as the average expression across all GTEx individuals for each tissue. The position-averaged embedding vectors were then used to train a Ridge regres- sor to predict tissue-specific expression levels. The regularization strength was selected from 30 evenly spaced values in log space between 1 and 5. The optimal model was 8 chosen based on R2 performance on the validation set. For personal-level expression prediction, individual genome sequences were fed into Enformer to generate embed- dings, which were then input into the trained Ridge regressor to produce tissue-specific expression predictions. Choosing 300 Genes that Span Different R2 Values The R2 values from 10-fold cross-validation using Elastic Net were used as a reference to assess gene predictability. Genes were grouped into 10 bins based on their R2 values across tissues: (−∞,0], (0,0.01], (0.01,0.02], (0.02,0.05], (0.05,0.1], (0.1,0.2], (0.2,0.3], (0.3,0.4], (0.4,0.5], and (0.5,1]. From each bin, 30 genes were randomly selected, resulting in a set of 300 genes that span a wide range of predictability levels. In silico mutagenesis In silico mutagenesis (ISM) was performed to estimate the marginal effect of individual genetic mutations on AlphaGenome’s output. Each mutation was introduced into a reference sequence spanning 1 Mb centered on the TSS, and the resulting predicted expression was compared to the prediction from the unmodified reference sequence. The difference between these two predictions was taken as the mutation’s effect. For Random Forest, the reference expression was obtained using a feature vector of all zeros. Each mutation was then individually activated (set to one) to com- pute the corresponding alternative expression. To enable direct comparison between AlphaGenome and Random Forest, the marginal effects for all mutations were rescaled to the [0, 1] range. Acknowledgements This work was supported in part through the Minerva computational and data resources and staff expertise provided by Scientific Computing and Data at the Icahn School of Medicine at Mount Sinai and supported by the Clinical and Translational Science Awards (CTSA) grant UL1TR004419 from the National Center for Advancing Translational Sciences. Competing Interests None declared. 9 (PDF p. 9)
