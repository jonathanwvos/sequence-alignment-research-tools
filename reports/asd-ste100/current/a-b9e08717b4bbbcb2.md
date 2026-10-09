# A Model of Evolutionary Change in Proteins

- Work ID: `b-7f8c14f7df90`
- Asset ID: `a-b9e08717b4bbbcb2`
- Source PDF: `literature/academic-papers-processed/A model of evolutionary change in proteins.pdf`
- SHA-256: `b9e08717b4bbbcb21a608f80838ef1fe1e431908e174580c49b74c980e3a67ea`
- ASD-STE100 Issue 9 review: **Pending manual review**

## Executive summary

- The authors derive amino acid replacement matrices from 1,572 accepted point mutations in 71 groups of closely related proteins. (PDF p. 1).
- The model combines exchange counts and relative mutabilities to estimate replacement probabilities at specified evolutionary distances. (PDF p. 3).
- The authors use a 250-PAM log odds matrix to score distant protein relationships. (PDF p. 8).

## Objectives

- Estimate both amino acid replacement frequencies and the tendency of each amino acid to remain unchanged. (PDF p. 1).
- Use mutation-based scores to distinguish distant protein relationships from random matches. (PDF p. 8).

## Arguments

- The authors argue that comparisons with inferred ancestors avoid false direct exchanges that can arise from comparisons between observed sequences. (PDF p. 2).
- The authors argue that identity counts and scores based only on the genetic code omit useful evidence from specific matching and differing residue pairs. (PDF p. 8).
- The authors attribute exchange patterns mainly to natural selection and secondarily to genetic code constraints. (PDF p. 7).

## Analysis

- Of 190 possible amino acid exchanges, 35 were not observed. Asp–Glu exchanges were most frequent, with 83 observations. (PDF p. 2).
- About 20% of exchanges involved amino acids whose codons differed at more than one nucleotide. The authors suggest that selection restricts changes at some sites and permits repeated changes at others. (PDF p. 2).
- Asn, Ser, Asp, and Glu had the highest average relative mutabilities. Trp and Cys had the lowest. (PDF p. 3).
- The log odds matrix shows groups of chemically similar residues that tend to replace one another. Some exchange patterns extend across these groups. (PDF p. 7).

## Methods

- Collect exchanges from phylogenetic trees and some related sequence pairs. Enter each exchange in both directions under a symmetric exchange assumption. (PDF p. 1).
- Use sequences that differ by less than 15% within each tree to reduce repeated substitutions at one site. Distribute changes at ambiguous ancestral positions among observed alternatives. (PDF p. 2).
- Calculate relative mutability as total changes divided by total exposure to mutation. Sum exposure across branches using local residue frequencies and branch mutation counts per 100 links. (PDF p. 3).
- Compare replacement probabilities with chance residue frequencies to obtain relatedness odds. Add log odds across positions to represent the product of position-specific odds. (PDF p. 7).

## Applications

- Convert observed sequence differences to estimated PAM distances for evolutionary tree calculations. (PDF p. 7).
- Use the 250-PAM log odds matrix as a scoring matrix for distant protein relationships. (PDF p. 8).

## Optimization

- Use sums of logarithms instead of products of position-specific odds. The authors describe this calculation as more convenient. (PDF p. 7).

## Evaluation and testing

- The mutation data cover 34 superfamilies organized into 71 evolutionary trees. (PDF p. 2).
- The authors state that chapter 23 compares the 250-PAM scoring matrix with other matrices. The supplied excerpts do not include that comparison. (PDF p. 8).

## Results

- The authors report that the expanded data produce more accurate replacement matrices and a more sensitive scoring matrix than their earlier version. (PDF p. 1).
- The distance table maps 50% observed difference to 80 PAMs and 80% observed difference to 246 PAMs. (PDF p. 7).
- Predicted differences at a given PAM distance differ by up to 2.5% from those reported in Volume 5. (PDF p. 7).
- The authors report that the 250-PAM log odds matrix is effective for detecting distant relationships. The supplied page gives no numerical detection results. (PDF p. 8).

## Limitations and uncertainty

- The symmetric exchange assumption prevents the model from detecting changes in amino acid frequencies over evolutionary distance. (PDF p. 1).
- Some inferred ancestral residues are ambiguous. Their exchange counts therefore require statistical allocation among alternatives. (PDF p. 2).
- The data contain no observations for 35 possible exchanges. The authors associate these gaps mainly with rare, less mutable residues and exchanges that require multiple nucleotide changes. (PDF p. 2).

## References

1. 1, Dayhoff, M.O., Eck, R.V., and Park, C.M., in Atlas of Protein Sequence and Structure 1972, Vol.5, ed. Dayhoff, M.O., pp.89-99, Nat. Biomed. Res. Found., Washington, D.C., 1972 (PDF p. 8)
2. Schwartz, R.M., and Dayhoff, M.O., in Evolution of Protein Molecules, ed. Matsubara, H., and Yamanaka, T., pp.1-16, Japan Sci. Soc. Press, Tokyo, 1978 (PDF p. 8)
3. Schwartz, R.M., and Dayhoff, M.O., in Origin of Life, ed. Noda, H., pp.457-469, Center for Academic Pub. Japan/Japan Sci. Soc. Press, Tokyo, 1978 (PDF p. 8)
4. Dayhoff, M.O., and Eck, R.V., Atlas of Protein Sequence and Structure 1967-68, pp.33-45, Nat. Biomed. Res. Found., Silver Spring, Md., 1968 (PDF p. 8)
