# Deep reinforcement learning-based pairwise DNA sequence alignment method compatible with embedded edge devices

- Work ID: `b-41eab4a6366b`
- Asset ID: `a-bd6f7a22157b2edd`
- Source PDF: `literature/academic-papers-processed/Deep reinforcement learning-based pairwise DNA sequence alignment method compatible with embedded edge devices.pdf`
- SHA-256: `bd6f7a22157b2edd1e86ea8bdddacb03191c719f04a88c343c1d9b49030dcd87`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- EdgeAlign uses a dueling deep Q-network to align DNA sequences through a fixed sliding window. (PDF p. 2).
- The authors use AutoKeras to reduce model size and demonstrate inference on Jetson Nano and FPGA hardware. (PDF p. 8).

## Objectives

- The authors aim to support pairwise DNA alignment on low-cost edge devices with limited computing resources. (PDF p. 1).

## Arguments

- A fixed window bounds the resources needed for each alignment decision, even when input sequences are long. (PDF p. 3).
- The authors argue that sequential alignment can accumulate errors from reduced numerical precision. (PDF p. 6).

## Analysis

- Larger windows reduced mean benchmark error but increased resource use and inference time. (PDF p. 6).
- The benchmark error is zero when EdgeAlign meets or exceeds the BLAST score. Otherwise, it is the score deficit divided by the BLAST score. This metric measures score shortfall, not residue correspondence. (PDF p. 6).

## Methods

- The network processes image representations of nucleotide windows. Shared convolutional features feed state-value and action-advantage outputs. (PDF p. 2).
- The agent chooses forward, insertion, or deletion. Each action advances one or both sequence indices. Alignment stops when either sequence ends. (PDF p. 3).
- Training pairs contain synthetic mutations. The generator uses JC69 for substitutions and a Zipfian distribution for insertion and deletion lengths. Training uses Keras-RL. (PDF p. 5).

## Applications

- The demonstrated task is pairwise alignment of influenza sequences from the NCBI Virus Data Hub on embedded hardware. (PDF p. 6).
- The authors propose edge alignment as a component of portable genomic analysis that reduces dependence on cloud connectivity. (PDF p. 1).

## Optimization

- A trained DQN labels stored window states with predicted actions. AutoKeras searches for a smaller network that reproduces these actions. (PDF p. 6).
- The reduced model represents each nucleotide with a 2 × 2 pixel block. For a window of 50, parameter count fell from about 1.36 million to 98,000. (PDF p. 6).
- The FPGA implementation uses a row-stationary convolution accelerator to increase parallel execution and data reuse. Modified TensorFlow Lite kernels invoke the accelerator. (PDF p. 8).

## Evaluation and testing

- The benchmark uses 40 randomly selected influenza sequences and five window sizes. EdgeAlign scores are compared with scores from the NCBI online BLAST tool. (PDF p. 6).
- Tests measure mean score error and inference time per action. Reduced models use window sizes of 50 and 70. (PDF p. 6).
- Deployment tests include Jetson Nano, an STM32F746NG microcontroller, and an Arty A7-100T FPGA platform. (PDF p. 8).

## Results

- The reduced model with a window of 50 required 2.32 ms per action on Jetson Nano. (PDF p. 8).
- At 100 MHz, FPGA inference fell from 2.05 seconds to about one second per action with convolution acceleration. Floating-point computation preserved the reported mean error. (PDF p. 8).
- The 8-bit microcontroller model found about 70% fewer matches than the pretrained DQN. (PDF p. 8).

## Limitations and uncertainty

- The tested microcontroller configuration did not provide acceptable alignment accuracy. The authors concluded that their deployment needed floating-point precision. (PDF p. 8).
- Fixed window resources do not give fixed total execution time. Longer sequences require more alignment decisions. (PDF p. 8).
- The comparison with an earlier RL method uses different scoring metrics and hardware timing conditions. I interpret this as a limit on direct performance comparison. (PDF p. 8).

## References

1. Mattick, J. S. et al. The impact of genomics on the future of medicine and health. Med. J. Aust. 201, 17–20 (2014). (PDF p. 9)
2. Jain, M., Olsen, H. E., Paten, B. & Akeson, M. The Oxford Nanopore MinION: Delivery of nanopore sequencing to the genomics community. Genome Biol. 17, 1–11 (2016). (PDF p. 9)
3. Needleman, S. B. & Wunsch, C. D. A general method applicable to the search for similarities in the amino acid sequence of two proteins. J. Mol. Biol. 48, 443–453 (1970). (PDF p. 9)
4. Larkin, M. A. et al. Clustal W and Clustal X version 2.0. Bioinformatics 23, 2947–2948 (2007). (PDF p. 9)
5. Edgar, R. C. MUSCLE: Multiple sequence alignment with high accuracy and high throughput. Nucleic Acids Res. 32, 1792–1797 (2004). (PDF p. 9)
6. Katoh, K. & Standley, D. M. MAFFT multiple sequence alignment software version 7: Improvements in performance and usability. Mol. Biol. Evol. 30, 772–780 (2013). (PDF p. 9)
7. Sievers, F. et al. Fast, scalable generation of high-quality protein multiple sequence alignments using Clustal Omega. Mol. Syst. Biol. 7, 539 (2011). (PDF p. 9)
8. Chao, K.-M., Pearson, W. R. & Miller, W. Aligning two sequences within a specified diagonal band. Bioinformatics 8, 481–487 (1992). (PDF p. 9)
9. Camacho, C. et al. BLAST+: Architecture and applications. BMC Bioinform. 10, 1–9 (2009). (PDF p. 9)
10. Marçais, G. et al. MUMmer4: A fast and versatile genome alignment system. PLoS Comput. Biol. 14, e1005944 (2018). (PDF p. 9)
11. NCBI, B. L. A. S. T. Basic local alignment search tool—NCBI. https://​blast.​ncbi.​nlm.​nih.​gov/​Blast.​cgi. (PDF p. 9)
12. McGinnis, S. & Madden, T. L. BLAST: At the core of a powerful and diverse set of sequence analysis tools. Nucleic Acids Res. 32, W20–W25 (2004). (PDF p. 9)
13. Morgulis, A., Gertz, E. M., Schäffer, A. A. & Agarwala, R. A fast and symmetric DUST implementation to mask low-complexity DNA sequences. J. Comput. Biol. 13, 1028–1040 (2006). (PDF p. 9)
14. Mircea, I.-G., Bocicor, I. & Czibula, G. A reinforcement learning based approach to multiple sequence alignment. In International Workshop Soft Computing Applications 54–70 (Springer, 2016). (PDF p. 9)
15. Jafari, R., Javidi, M. M. & Kuchaki Rafsanjani, M. Using deep reinforcement learning approach for solving the multiple sequence alignment problem. SN Appl. Sci. 1, 1–12 (2019). (PDF p. 9)
16. Song, Y.-J., Ji, D. J., Seo, H., Han, G. B. & Cho, D.-H. Pairwise heuristic sequence alignment algorithm based on deep reinforcement learning. IEEE Open J. Eng. Med. Biol. 2, 36–43 (2021). (PDF p. 9)
17. Ramakrishnan, R. K., Singh, J. & Blanchette, M. RLALIGN: A reinforcement learning approach for multiple sequence alignment. In 2018 IEEE 18th International Conference on Bioinformatics and Bioengineering (BIBE) 61–66 (IEEE, 2018). (PDF p. 9)
18. Joeres, R. Multiple sequence alignment using deep reinforcement learning. SKILL 2021 (2021). (PDF p. 9)
19. David, R. et al. TensorFlow Lite Micro: Embedded machine learning for TinyML systems. Proc. Mach. Learn. Syst. 3, 800–811 (2021). (PDF p. 9)
20. He, X., Zhao, K. & Chu, X. AutoML: A survey of the state-of-the-art. Knowl. Based Syst. 212, 106622 (2021). (PDF p. 9)
21. Lall, A. EdgeAlign. https://​github.​com/​aryan​lall11/​EdgeA​lign (2022). (PDF p. 9)
22. Li, Y. Deep reinforcement learning: An overview. arXiv preprint arXiv:​1701.​07274 (2017). (PDF p. 9)
23. Hornik, K. Approximation capabilities of multilayer feedforward networks. Neural Netw. 4, 251–257 (1991). (PDF p. 9)
24. Wang, Z. et al. Dueling network architectures for deep reinforcement learning. In International Conference on Machine Learning 1995–2003 (PMLR, 2016). (PDF p. 9)
25. Manual, A. N. B. C. L. A. U. Appendices—ncbi blast command line applications user manual. https://​www.​ncbi.​nlm.​nih.​gov/​books/​ NBK27​9684/. (PDF p. 9)
26. Jukes, T. H. et al. Evolution of protein molecules. Mamm. Protein Metab. 3, 21–132 (1969). (PDF p. 9)
27. Qian, B. & Goldstein, R. A. Distribution of indel lengths. Proteins Struct. Funct. Bioinform. 45, 102–104 (2001). (PDF p. 9)
28. Plappert, M. keras-rl. https://​github.​com/​keras-​rl/​keras-​rl (2016). (PDF p. 9)
29. Liang, T., Glossner, J., Wang, L., Shi, S. & Zhang, X. Pruning and quantization for deep neural network acceleration: A survey. Neurocomputing 461, 370–403 (2021). (PDF p. 9)
30. Deng, L., Li, G., Han, S., Shi, L. & Xie, Y. Model compression and hardware acceleration for neural networks: A comprehensive survey. Proc. IEEE 108, 485–532 (2020). (PDF p. 9)
31. Gou, J., Yu, B., Maybank, S. J. & Tao, D. Knowledge distillation: A survey. Int. J. Comput. Vis. 129, 1789–1819 (2021). (PDF p. 9)
32. Ren, P. et al. A comprehensive survey of neural architecture search: Challenges and solutions. ACM Comput. Surv. (CSUR) 54, 1–34 (2021). (PDF p. 9)
33. Jin, H., Song, Q. & Hu, X. Auto-Keras: An efficient neural architecture search system. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 1946–1956 (ACM, 2019). (PDF p. 9)
34. Hatcher, E. L. et al. Virus variation resource—Improved response to emergent viral outbreaks. Nucleic Acids Res. 45, D482–D490 (2017). (PDF p. 9)
35. Chen, Y.-H., Krishna, T., Emer, J. S. & Sze, V. Eyeriss: An energy-efficient reconfigurable accelerator for deep convolutional neural networks. IEEE J. Solid-State Circuits 52, 127–138 (2016). (PDF p. 9)
36. Lall, A. TFLite-Micro-Accelerator. https://​github.​com/​aryan​lall11/​TFLite-​Micro-​Accel​erator (2022). (PDF p. 9)
37. Lall, A. EdgeAlign Hardware Implementation. https://​github.​com/​aryan​lall11/​EdgeA​lign/​blob/​master/​DDP_​Report_​17D07​0053.​ pdf (2022). 10 Vol:.(1234567890) Scientific Reports | (2023) 13:2773 | https://doi.org/10.1038/s41598-023-29277-6 www.nature.com/scientificreports/ Acknowledgements The authors thank Dr. Anirvan Chatterjee at HaystackAnalytics Pvt. Ltd. and Prof. Kiran Kondabagil at IIT Bombay for insightful discussions on sequence alignment, and the Wadhwani Electronics Lab (WEL) at IIT Bombay for providing hardware and computational resources to support this work. Activities at WEL are sup- ported through a grant from the Wadhwani Foundation [grant DO/2015-WEL001]. Author contributions A.L. and S.T. conceived the experiments, A.L. conducted the experiments. Both authors analysed the results and prepared the manuscript. Competing interests The authors declare no competing interests. Additional information Correspondence and requests for materials should be addressed to A.L. or S.T. Reprints and permissions information is available at www.nature.com/reprints. Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/. © The Author(s) 2023 (PDF p. 9)
