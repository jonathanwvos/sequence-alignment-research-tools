# A Block-Sorting Lossless Data Compression Algorithm

- Work ID: `b-0dd8b513f1aa`
- Asset ID: `a-b957dfba7aeedcd6`
- Source PDF: `literature/academic-papers-processed/A Block-sorting Lossless Data Compression Algorithm.pdf`
- SHA-256: `b957dfba7aeedcd658811cd483830eb12233223c57612f7463dbb953338d8f3a`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The algorithm applies a reversible transformation to an input block. Sorting groups characters by context and makes redundancy easier for simple coders to use. (PDF p. 22).
- The tested implementation combines Algorithm C, a move-to-front coder, and a modified Huffman coder. (PDF p. 21).

## Objectives

- The authors aim to obtain compression comparable to good statistical models, with speed closer to Lempel–Ziv coders. (PDF p. 22).

## Arguments

- The authors argue that context-based sorting supports effective compression of both text and non-text inputs. (PDF p. 22).

## Analysis

- The transformation uses context from only one side of each character. (PDF p. 22).
- Compression improves as input blocks grow. The authors report only small gains above a few tens of millions of characters. (PDF p. 21).

## Methods

- For the Calgary tests, each input file forms one transformation block. A simple move-to-front coder processes the transformed output. (PDF p. 21).
- The modified Huffman coder processes the move-to-front output. It builds a new Huffman tree for each 16 kbyte input block. (PDF p. 21).

## Applications

- The authors present the method for general-purpose lossless compression of text and non-text data. (PDF p. 22).

## Optimization

- The implementation updates Huffman trees for separate 16 kbyte blocks instead of using one tree for the complete coder input. (PDF p. 21).
- Larger transformation blocks improve compression. Good compression requires blocks of several thousand characters. (PDF p. 22).

## Evaluation and testing

- The benchmark compresses 14 Calgary Compression Corpus files separately. Compression effectiveness is measured in output bits per input character. (PDF p. 21).
- CPU times were measured on a DECstation 5000/200 with a 25 MHz MIPS R3000 processor and a 64 kbyte cache. These times exclude I/O. (PDF p. 21).
- The block-size study uses Calgary book1 and the complete Hector corpus. Hector contains slightly more than 100 MBytes of modern English text. (PDF p. 21).
- Table 3 compares Alg-C/D with compress 4.2.3, gzip 1.2.4, and comp-2 with a fourth-order model. (PDF p. 22).

## Results

- Alg-C/D produces 856,233 bytes and a mean of 2.43 bits per character. Total CPU times are 51.1 seconds for compression and 9.4 seconds for decompression. (PDF p. 22).
- gzip produces 1,024,887 bytes and a mean of 2.71 bits per character. Its compression and decompression times are 42.6 and 4.9 seconds. (PDF p. 22).
- comp-2 produces 848,885 bytes and a mean of 2.47 bits per character. Its compression and decompression times are 603.2 and 614.1 seconds. (PDF p. 22).

## Limitations and uncertainty

- The authors expect the simple byte-wise move-to-front coder to prevent asymptotically optimal compression, even with unlimited block growth. (PDF p. 21).
- The reported mean bits per character is the mean of individual file values. It is not computed from the total compressed size. (PDF p. 21).

## References

1. J. Ziv and A. Lempel. A universal algorithm for sequential data compression. IEEE Transactions on Information Theory. Vol. IT-23, No. 3, May 1977, pp. 337–343. (PDF p. 23)
2. J. Ziv and A. Lempel. Compression of individual sequences via variable rate coding. IEEE Transactions on Information Theory. Vol. IT-24, No. 5, September 1978, pp. 530–535. (PDF p. 23)
3. T. Bell, I. H. Witten, and J.G. Cleary. Modeling for text compression. ACM Computing Surveys, Vol. 21, No. 4, December 1989, pp. 557–589. (PDF p. 23)
4. J.L. Bentley, D.D. Sleator, R.E. Tarjan, and V.K. Wei. A locally adaptive data compression algorithm. Communications of the ACM, Vol. 29, No. 4, April 1986, pp. 320–330. (PDF p. 23)
5. E.M. McCreight. A space economical suffix tree constructionalgorithm. Jour- nal of the ACM, Vol. 32, No. 2, April 1976, pp. 262–272. (PDF p. 23)
6. U. Manber and E. W. Myers, Suffix arrays: A new method for on-line string searches. SIAM Journal on Computing, Volume 22, No. 5, October 1993, pp. 935-948. (PDF p. 23)
7. I. H. Witten and T. Bell. The Calgary/Canterbury text compression cor- pus. Anonymous ftp from ftp.cpsc.ucalgary.ca: /pub/text.com- pression.corpus/text.compression.corpus.tar.Z (PDF p. 23)
8. L. Glassman, D. Grinberg, C. Hibbard, J. Meehan, L. Guarino Reid, and M-C. van Leunen. Hector: Connecting Words with Definitions. Proceedings of the 8th Annual Conference of the UW Centre for the New Oxford English Dictionary and Text Research, Waterloo, Canada, October, 1992. pp. 37– (PDF p. 23)
9. Also available as Research Report 92a, Digital Equipment Corporation Systems Research Center, 130 Lytton Ave, Palo Alto, CA. 94301. (PDF p. 23)
10. T.A. Welch. A technique for high performance data compression. IEEE Com- puter, Vol. 17, No. 6, June 1984, pp. 8–19. (PDF p. 23)
11. Peter Jannesen et al. Compress, Version 4.2.3. Posted to the Internet news- group comp.sources.reviewed, 28th August, 1992. Anonymous ftp from gatekeeper.dec.com: /pub/misc/ncompress-4.2.3 17 (PDF p. 23)
12. J. Gailly et al. Gzip,Version 1.2.4. Anonymous ftp from prep.ai.mit.edu: /pub/gnu/gzip-1.2.4.tar.gz (PDF p. 24)
13. Mark Nelson. Arithmetic coding and statistical modeling. Dr. Dobbs Journal. February, 1991. Anonymous ftp from wuarchive.wustl.edu: /mir- rors/msdos/ddjmag/ddj9102.zip 18 (PDF p. 24)
