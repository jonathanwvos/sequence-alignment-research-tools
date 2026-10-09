# SparkBWA: Speeding Up the Alignment of high-throughput dna sequencing data

- Work ID: `w-623292acae69`
- Asset ID: `a-623292acae69ceec`
- Source PDF: `literature/academic-papers-processed/SparkBWA: Speeding Up the Alignment of high-throughput dna sequencing data.pdf`
- SHA-256: `623292acae69ceecc4cbe73c1b151933311814da302fa7f7cfdab7e22d87c23d`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- SparkBWA integrates BWA with Apache Spark to distribute DNA read mapping across a cluster. (PDF p. 2).
- Its two software layers require no changes to BWA source code. The authors claim compatibility with future and legacy BWA versions. (PDF p. 1).
- The evaluation measures performance, scalability, and memory consumption. It compares SparkBWA with other parallel BWA tools. (PDF p. 10).

## Objectives

- The authors aim to improve performance and scalability relative to BWA and other BWA tools. (PDF p. 2).
- The design aims to preserve BWA version compatibility and provide an API that hides implementation details. (PDF p. 2).

## Arguments

- The authors identify read mapping as a bottleneck as sequencing output increases. They propose distributed processing with Spark to reduce this cost. (PDF p. 2).
- The authors use JNI calls to BWA methods to address timeout problems associated with external BWA processes in Hadoop mappers. (PDF p. 5).

## Analysis

- The evaluation examines RDD creation and compares regular and hybrid execution modes. (PDF p. 10).
- For comparison with SEAL and pBWA, SparkBWA runs BWA-backtrack with BWA 0.5. BWA-MEM comparisons use BWA 0.7.12. (PDF p. 10).

## Methods

- SparkBWA supports BWA-MEM, BWA-backtrack, and BWA-SW. Its API selects the algorithm and single-end or paired-end input. (PDF p. 8).
- Each mapper needs the complete reference genome. Nodes can access it through NFS or store it at the same local path. (PDF p. 8).
- Each mapper writes a SAM file to HDFS. An optional reduce phase merges these files. (PDF p. 8).
- The API offers Join, Join with sortByKey, and SortHDFS approaches for paired-end RDD creation. (PDF p. 8).

## Applications

- SparkBWA maps sequencing reads to a large reference genome through the Scala Spark shell or the console. (PDF p. 8).

## Optimization

- Hybrid mode combines distributed map processes with BWA threads inside each mapper. (PDF p. 8).
- Users can set the partition count and thread count per mapper. By default, partitions follow the HDFS block size. (PDF p. 8).

## Evaluation and testing

- The benchmark uses three paired-end datasets from the 1000 Genomes Project. They contain 12 million, 24.1 million, and 98.8 million reads, with lengths of 51, 100, and 100 bp. (PDF p. 10).
- Tests use six nodes. Each node has 64 AMD Opteron cores and 256 GiB of memory. A 10GbE network connects the nodes. (PDF p. 10).
- The test environment uses Hadoop 2.7.1, Spark 1.5.2, and CentOS 6.7. Each YARN container receives about 11 GiB, allowing up to 22 concurrent containers per node. (PDF p. 10).
- Reported execution times are arithmetic means of twenty runs. BWA-MEM comparisons include BigBWA, Halvade, and threaded BWA. (PDF p. 10).

## Results

- The authors report that SparkBWA runs BWA-backtrack an average of 1.9 times faster than SEAL and 1.4 times faster than pBWA. (PDF p. 19).
- For BWA-MEM, the authors report an average speedup of 1.4 relative to BigBWA and Halvade. (PDF p. 20).

## Limitations and uncertainty

- Every mapper requires access to the complete reference genome. This adds a deployment requirement across cluster nodes. (PDF p. 8).
- The evaluated datasets use paired-end reads. Interpretation: these tests do not establish performance for single-end input. (PDF p. 10).
- The reported SparkBWA version supports only the Scala Spark shell. (PDF p. 8).

## References

1. Zaharia M, Chowdhury M, Franklin MJ, Shenker S, Stoica I. Spark: Cluster Computing with Working Sets. In: Proc. of the 2Nd USENIX Conference on Hot Topics in Cloud Computing (HotCloud); 2010. p. 10–10. (PDF p. 20)
2. Li H, Durbin R. Fast and Accurate Short Read Alignment with Burrows-Wheeler Transform. Bioinfor- matics. 2009; 25(14):1754–1760. doi: 10.1093/bioinformatics/btp324 PMID: 19451168 (PDF p. 20)
3. Dean J, Ghemawat S. MapReduce: Simplified Data Processing on Large Clusters. In: Proceedings of the 6th Conference on Symposium on Opearting Systems Design & Implementation—Volume 6. OSDI’04. Berkeley, CA, USA: USENIX Association; 2004. p. 10–10. (PDF p. 20)
4. Apache Hadoop home page;. http://hadoop.apache.org/. (PDF p. 20)
5. Shvachko K, Kuang H, Radia S, Chansler R. The Hadoop Distributed File System. In: Pro. of the IEEE 26th Symposium on Mass Storage Systems and Technologies (MSST); 2010. p. 1–10. (PDF p. 20)
6. Vavilapalli VK, Murthy AC, Douglas C, Agarwal S, Konar M, Evans R, et al. Apache Hadoop YARN: Yet Another Resource Negotiator. In: Proc. of the 4th Annual Symposium on Cloud Computing (SOCC); 2013. p. 5:1–5:16. (PDF p. 20)
7. Srirama SN, Jakovits P, Vainikko E. Adapting Scientific Computing Problems to Clouds Using MapRe- duce. Future Generation Computer Systems. 2012; 28(1):184–192. doi: 10.1016/j.future.2011.05.025 (PDF p. 20)
8. Islam M, Huang AK, Battisha M, Chiang M, Srinivasan S, Peters C, et al. Oozie: towards a scalable workflow management system for Hadoop. In: Proceedings of the 1st ACM SIGMOD Workshop on Scalable Workflow Execution Engines and Technologies. ACM; 2012. p. 4. (PDF p. 20)
9. Cascading home page;. http://www.cascading.org/. (PDF p. 20)
10. Zaharia M, Chowdhury M, Das T, Dave A, Ma J, McCauley M, et al. Resilient Distributed Datasets: A Fault-tolerant Abstraction for In-memory Cluster Computing. In: Proc. of the 9th USENIX Conference on Networked Systems Design and Implementation; 2012. p. 2–2. (PDF p. 20)
11. Apache Cassandra home page;. http://cassandra.apache.org/. (PDF p. 20)
12. Apache HBase home page;. http://hbase.apache.org/. (PDF p. 20)
13. Apache Parquet home page;. http://parquet.apache.org/. (PDF p. 20)
14. Hindman B, Konwinski A, Zaharia M, Ghodsi A, Joseph AD, Katz R, et al. Mesos: A Platform for Fine- grained Resource Sharing in the Data Center. In: Proc. of the 8th USENIX Conference on Networked Systems Design and Implementation; 2011. p. 295–308. SparkBWA: Speeding Up the Alignment of High-Throughput DNA Sequencing Data PLOS ONE | DOI:10.1371/journal.pone.0155461 May 16, 2016 20 / 21 (PDF p. 20)
15. Li H, Durbin R. Fast and AccurateLong-ReadAlignment with Burrows-Wheeler Transform. Bioinformat- ics. 2010; 26(5):589–595. doi: 10.1093/bioinformatics/btp698 PMID: 20080505 (PDF p. 21)
16. Li H. Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM. arXiv:13033997v2. 2013;. (PDF p. 21)
17. Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, et al. The Sequence Alignment/Map for- mat and SAMtools. Bioinformatics. 2009; 25(16):2078–2079. doi: 10.1093/bioinformatics/btp352 PMID: 19505943 (PDF p. 21)
18. Cock PJA, Fields CJ, Goto N, Heuer ML, Rice PM. The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants. Nucleic Acids Research. 2010; 38(6):1767– 1771. doi: 10.1093/nar/gkp1137 PMID: 20015970 (PDF p. 21)
19. Abuín JM, Pichel JC, Pena TF, Amigo J. BigBWA: Approaching the Burrows—Wheeler Aligner to Big Data Technologies. Bioinformatics. 2015; 31(24):4003–4005. (PDF p. 21)
20. Decap D, Reumers J, Herzeel C, Costanza P, Fostier J. Halvade: Scalable Sequence Analysis with MapReduce. Bioinformatics. 2015; 31(15):2482–2488. doi: 10.1093/bioinformatics/btv179 PMID: 25819078 (PDF p. 21)
21. Pireddu L, Leo S, Zanetti G. SEAL: A Distributed Short Read Mapping and Duplicate Removal Tool. Bioinformatics. 2011; 27(15):2159–2160. doi: 10.1093/bioinformatics/btr325 PMID: 21697132 (PDF p. 21)
22. Leo S, Zanetti G. Pydoop: a Python MapReduce and HDFS API for Hadoop. In: Proc. of 19th Sympo- syum on HPDC; 2010. p. 819–825. (PDF p. 21)
23. Peters D, Luo X, Qiu K, Liang P. Speeding Up Large-Scale Next Generation Sequencing Data Analysis with pBWA. Journal of Applied Bioinformatics & Computational Biology. 2012; 1(1):1–6. (PDF p. 21)
24. Klus P, Lam S, Lyberg D, Cheung MS, Pullan G, McFarlane I, et al. BarraCUDA—a fast short read sequence aligner using graphics processing units. BMC Research Notes. 2012; 5:27. doi: 10.1186/ 1756-0500-5-27 PMID: 22244497 (PDF p. 21)
25. Liu Y, Schmidt B, Maskell DL. CUSHAW: a CUDA compatible short read aligner to large genomes based on the Burrows-Wheeler transform. Bioinformatics. 2012; 28(14):1830–1837. doi: 10.1093/ bioinformatics/bts276 PMID: 22576173 (PDF p. 21)
26. Liu CM, Wong TKF, Wu E, Luo R, Yiu SM, Li Y, et al. SOAP3: Ultra-fast GPU-based parallel alignment tool for short reads. Bioinformatics. 2012; 28(6):878–879. doi: 10.1093/bioinformatics/bts061 PMID: 22285832 (PDF p. 21)
27. Luo R, Wong T, Zhu J, Liu CM, Zhu X, Wu E, et al. SOAP3-dp: Fast, Accurate and Sensitive GPU- Based Short Read Aligner. PLoS ONE. 2013; 8(5). doi: 10.1371/journal.pone.0065632 (PDF p. 21)
28. Cui Y, Liao X, Zhu X, Wang B, Peng S. mBWA: A Massively Parallel Sequence Reads Aligner. In: 8th Int. Conference on Practical Applications of Computational Biology & Bioinformatics. vol. 294 of Advances in Intelligent Systems and Computing; 2014. p. 113–120. (PDF p. 21)
29. You L, Congdon C. Building and Optimizing BWA ALN 0.5.10 for Intel Xeon Phi Coprocessors;. https:// github.com/intel-mic/bwa-aln-xeon-phi-0.5.10. (PDF p. 21)
30. Luo R, Cheung J, Wu E, Wang H, Chan SH, Law WC, et al. MICA: A fast short-read aligner that takes full advantage of Many Integrated Core Architecture (MIC). BMC Bioinformatics. 2015; 17:7. (PDF p. 21)
31. Arram J, Tsoi KH, Luk W, Jiang P. Hardware Acceleration of Genetic Sequence Alignment. Reconfigur- able Computing: Architectures, Tools and Applications Lecture Notes in Computer Science. 2013; 7806:13–24. (PDF p. 21)
32. Sogabe Y, Maruyama T. An acceleration method of short read mapping using FPGA. In: International Conference on Field-Programmable Technology (FPT); 2013. p. 350–353. (PDF p. 21)
33. Waidyasooriya H, Hariyama M. Hardware-Acceleration of Short-read Alignment Based on the Burrows- Wheeler Transform. IEEE Transactions on Parallel and Distributed Systems. 2015; PP(99):1–1. (PDF p. 21)
34. Zhao G, Ling C, Sun D. SparkSW: Scalable Distributed Computing System for Large-Scale Biological SequenceAlignment. In: 15th IEEE/ACM International Symposium on Cluster, Cloud and Grid Comput- ing (CCGrid); 2015. p. 845–852. (PDF p. 21)
35. Altshuler D et al. A map of human genome variation from population-scale sequencing. Nature. 2010; 467:1061–1073. doi: 10.1038/nature09534 PMID: 20981092 SparkBWA: Speeding Up the Alignment of High-Throughput DNA Sequencing Data PLOS ONE | DOI:10.1371/journal.pone.0155461 May 16, 2016 21 / 21 (PDF p. 21)
