# Methods for Assessing the Statistical Significance of Molecular Sequence Features by Using General Scoring Schemes

- Work ID: `b-1ceaa8511f4f`
- Asset ID: `a-97abef53a55bb7d3`
- Source PDF: `literature/academic-papers-processed/Methods for assessing the statistical significance of molecular sequence features by using general scoring schemes.pdf`
- SHA-256: `97abef53a55bb7d3e4b85f4ee185a0a87a9545cc367aa109504ea5e21b3d4ef2`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors derive statistical formulas for high segment scores under general scoring schemes. They also describe the composition of high-scoring segments. (PDF p. 1).
- The alignment results apply to segment comparisons without gaps. Examples include protein charge regions, hydrophobic regions, and protein subalignments. (PDF p. 3).

## Objectives

- Estimate whether a high segment score or a count of high-scoring segments can arise by chance. (PDF p. 1).
- Use segment composition to guide the choice of scores for biologically relevant features. (PDF p. 1).

## Arguments

- The authors argue that graded scores can represent residue properties and mismatch differences that simpler pattern models cannot represent. (PDF p. 1).
- The authors argue that suitable target frequencies should match the composition of the regions being sought. This supports log-likelihood ratio scores. (PDF p. 3).

## Analysis

- For independent letters, the model requires a negative expected score and some probability of a positive score. The maximal segment score grows on the order of ln(n)/λ*. (PDF p. 2).
- For a sequence of length n, the maximal-score tail is approximated by 1 − exp[−K*n exp(−λ*S)]. Counts of sufficiently separated segments above S have an approximate Poisson distribution with mean K*n exp(−λ*S). (PDF p. 2).
- For two independent sequences, the alignment formula replaces n with mn. The stated approximation requires similar letter distributions and sequence lengths that grow at roughly equal rates. (PDF p. 3).
- In sufficiently high-scoring random segments, the frequency of letter i approaches p_i exp(λ*s_i) as sequence length increases. (PDF p. 3).

## Methods

- Assign additive scores to letters. Select the segment with the greatest total score, so its length follows from the data rather than a fixed window. (PDF p. 2).
- Calculate λ* as the unique positive solution of Σ p_i exp(λ*s_i) = 1. For pairwise alignment, use pair probabilities and pair scores in this equation. (PDF p. 3).
- Estimate background probabilities from the observed protein composition. Calculate λ* and K*, then derive a score threshold for a selected significance level. (PDF p. 5).

## Applications

- The examples use scores for mixed charge, acidic charge, basic charge, hydrophobicity, and cysteine concentration. (PDF p. 4).
- PAM-250 scores assess cytochrome P450 similarity, internal similarity in the cystic fibrosis protein, and similarity to the bacterial transport protein chlD. (PDF p. 4).

## Optimization

- The authors propose scores proportional to log(q_i/p_i), where q_i represents the desired segment composition and p_i represents the background composition. (PDF p. 3).
- For protein comparison matrices, the authors recommend better estimates of background and target pair frequencies as a route to improved scores. (PDF p. 3).
- The series used to calculate K* converges geometrically. The authors state that only a small number of terms is needed for a useful estimate. (PDF p. 5).

## Evaluation and testing

- The evaluation uses representative protein examples and model-based probabilities. A broader application study is deferred to another publication. (PDF p. 4).
- The sodium ion channel example tests both its maximal basic-charge score and the occurrence of three separate high-scoring segments with a Poisson model. (PDF p. 4).

## Results

- The c-jun mixed-charge segment at residues 246–285 has score 29 and P < 0.0002. (PDF p. 4).
- The cystic fibrosis protein internal alignment joins residues 497–586 and 1295–1384. Its score is 120, with P < 0.00001. (PDF p. 4).
- The cystic fibrosis protein alignment to chlD spans 48 residues and has score 99, with P < 0.0001. (PDF p. 4).
- The thrombomodulin cysteine segment has score 12 and P approximately 0.91. The authors conclude that it is not unusual relative to the protein's high cysteine frequency. (PDF p. 4).

## Limitations and uncertainty

- The alignment theorem excludes gaps. Outside its sequence-length and composition restrictions, the authors state that it gives conservative significance estimates. (PDF p. 3).
- The random protein model is a reference standard. The authors caution against treating its results as direct biological evidence. (PDF p. 3).
- The composition theorem for general multiple-sequence comparisons is a conjecture. The authors assume it when discussing protein comparison scores. (PDF p. 3).
- The appendix gives asymptotic bounds and states that lengths of at least 150 suffice in practice. Using the upper bound K+ gives a conservative significance estimate. (PDF p. 5).

## References

1. Doolittle, R. F. (1981) Science 214, 149-159. (PDF p. 5)
2. Karlin, S., Ghandour, G., Ost, F., Tavard, S. & Kom, L. J. (1983) Proc. Natl. Acad. Sci. USA 80, 5660-5664. (PDF p. 5)
3. Fitch, W. M. (1983) J. Mol. Biol. 163, 171-176. (PDF p. 5)
4. Altschul, S. F. & Erickson, B. W. (1985) Mol. Biol. Evol. 2, 526-538. (PDF p. 5)
5. Karlin, S., Ost, F. & Blaisdell, B. E. (1989) in Mathematical Methods for DNA Sequences, ed. Waterman, M. S. (CRC, Boca Raton, FL), pp. 133-157. (PDF p. 5)
6. Karlin, S. & Ost, F. (1985) Proceedings ofBerkeley Conference in Honor ofJ. Neyman and J. Kiefer, eds. LeCam, L. M. & Olshen, R. A. (Wadsworth, Monterey, CA), Vol. 1. (PDF p. 5)
7. Arratia, R. & Waterman, M. S. (1985) Adv. Math. 55, 13-23. (PDF p. 5)
8. Arratia, R. & Waterman, M. S. (1986) Ann. Prob. 13, 1236- 1249. (PDF p. 5)
9. Gordon, L., Schilling, M. F. & Waterman, M. S. (1986) Prob. Theor. Relat. 72, 279-287. (PDF p. 5)
10. Arratia, R., Gordon, L. & Waterman, M. S. (1986) Ann. Stat. 14, 971-993. (PDF p. 5)
11. Foulser, D. & Karlin, S. (1987) Stochastic Proc. Appl. 24, 203-224. (PDF p. 5)
12. Karlin, S. & Ost, F. (1987) Adv. Appl. Prob. 19, 293-351. (PDF p. 5)
13. Karlin, S. & Ost, F. (1988) Ann. Prob. 16, 535-563. (PDF p. 5)
14. Arratia, R., Morris, P. & Waterman, M. S. (1988) J. Appl. Prob. 25, 106-119. (PDF p. 5)
15. Feng, D. F., Johnson, M. S. & Doolittle, R. F. (1985) J. Mol. Evol. 21, 112-125. (PDF p. 5)
16. Risler, J. L., Delorme, M. O., Delacroix, H. & Henaut, A. (1988) J. Mol. Biol. 204, 1019-1029. (PDF p. 5)
17. McLachlan, A. D. (1971) J. Mol. Biol. 61, 409-424. (PDF p. 5)
18. Dayhoff, M. O., Schwartz, R. M. & Orcutt, B. C. (1978) in Atlas ofProtein Sequence and Structure (Natl. Biomed. Res. Found., Washington), Vol. 5, pp. 345-352. (PDF p. 5)
19. Mahler, H. R. & Cordes, E. H. (1966) Biological Chemistry (Harper & Row, New York). (PDF p. 5)
20. Dickerson, R. E. & Geis, I. (1983) Hemoglobin: Structure, Function, Evolution and Pathology (Cummings, Menlo Park, CA). 21. von Heijne, G. (1987) Sequence Analysis in Molecular Biology (Academic, San Diego, CA). (PDF p. 5)
21. Bishop, M. J. & Rawlings, C. J. (1987) Nucleic Acid and Protein Sequence Analysis: A Practical Approach (IRL, Ox- ford). (PDF p. 5)
22. Dembo, A. & Karlin, S. (1990) Ann. Prob., in press. (PDF p. 5)
23. Karlin, S., Dembo, A. & Kawabata, T. (1990) Ann. Stat., in press. (PDF p. 5)
24. Needleman, S. B. & Wunsch, C. D. (1970) J. Mol. Biol. 48, 443-453. (PDF p. 5)
25. Smith, T. F. & Waterman, M. S. (1981) Adv. Appl. Math. 2, 482-489. (PDF p. 5)
26. Wilbur, W. J. & Lipman, D. J. (1983) Proc. Nat!. Acad. Sci. USA 80, 726-730. (PDF p. 5)
27. Sellers, P. H. (1984) Bull. Math. Biol. 46, 501-524. (PDF p. 5)
28. Karlin, S., Morris, M., Ghandour, G. & Leung, M.-Y. (1988) Proc. Nat!. Acad. Sci. USA 85, 841-845. (PDF p. 5)
29. Wilbur, W. J. (1985) Mol. Biol. Evol. 2, 434-447. (PDF p. 5)
30. Karlin, S., Blaisdell, B. E., Mocarski, E. S. & Brendel, V. (1989) J. Mol. Biol. 205, 165-177. (PDF p. 5)
31. Karlin, S., Blaisdell, B. E. & Brendel, V. (1990) Methods Enzymol. 183, 388-402. (PDF p. 5)
32. Karlin, S. (1990) in Proceedings of the Sixth Conversation in Biomolecular Stereodynamics, eds. Sarma, R. H. & Sarma, M. H. (Adenine, Guilderland, NY), Vol. 2, pp. 171-180. (PDF p. 5)
33. Rauscher, F. J., III, Cohen, D. R., Curran, T., Bos, T. J., Vogt, P. K., Bohmann, D., Tjian, R. & Franza, R. B., Jr. (1988) Science 240, 1010-1016. (PDF p. 5)
34. Vogt, P. K., Bos, T. J. & Doolittle, R. F. (1987) Proc. Nat!. Acad. Sci. USA 84, 3316-3319. (PDF p. 5)
35. Ryder, K., Leu, L. F. & Nathans, D. (1988) Proc. Nat!. Acad. Sci. USA 85, 1487-1491. (PDF p. 5)
36. Karlin, S. & Brendel, V. (1990) Oncogenes 5, 85-95. (PDF p. 5)
37. Mitchell, P. J. & Tjian, R. (1989) Science 245, 371-378. (PDF p. 5)
38. Pirrotta, V., Manet, E., Hardon, E., Bickel, S. E. & Benson, M. (1987) EMBO J. 6, 791-799. (PDF p. 5)
39. Brendel, V. & Karlin, S. (1989) Proc. Natl. Acad. Sci. USA 86, 5698-5702. (PDF p. 5)
40. Theissen, H., Etzerodt, M., Reuter, R., Schneider, C., Lottspeich, R., Argos, P., Luehrmann, R. & Philipson, L. (1986) EMBO J. 5, 3209-3217. (PDF p. 5)
41. Jackson, T. R., Blair, L. A. C., Marshall, J., Goedert, M. & Hanley, M. R. (1988) Nature (London) 335, 437-440. (PDF p. 5)
42. Riordan, J. R., Rommens, J. M., Keren, B., Alan, N., Roma- hel, R., Grzelczak, Z., Zielenski, J., Lok, S., Plavsic, N., Chou, J. L., Drumm, M. L., Iannuzzi, M. C., Collins, F. S. & Tsui, L. C. (1989) Science 241, 1066-1071. (PDF p. 5)
43. Gonzalez, F. J. (1989) Pharmacol. Rev. 40, 243-288. Proc. Natl. Acad. Sci. USA 87 (1990) Downloaded from https://www.pnas.org by 192.143.141.160 on September 26, 2026 from IP address 192.143.141.160. (PDF p. 5)
