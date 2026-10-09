#!/usr/bin/env python3
"""Build evidence-backed capability classifications for the processed PDF collection.

This is a reproducible screening classifier. It detects controlled vocabulary terms
from the title, abstract/lead, and non-reference body text. It does not replace a
variant-level manual specification review.
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import subprocess
import tempfile
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from itertools import islice
from pathlib import Path
from urllib.parse import quote

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
PDF_DIR = ROOT / "literature" / "academic-papers-processed"
CLASS_DIR = OUT.parent / "classification"
REPORT_DIR = OUT.parent / "reports" / "asd-ste100"
RENAME_LOG = ROOT / "literature" / "academic-papers-processed-renames.csv"
CATALOG_ASSETS = {asset["sha256"]: asset for asset in json.loads((OUT.parent / "catalog" / "index.json").read_text())["assets"]}

# The user explicitly excluded textbooks and edited protocol handbooks from this
# paper-level classification pass. Keep the list exact and auditable.
SKIP_FILES = set()


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def filename_title(stem: str) -> str:
    stem = re.sub(r"\s+\((?:copy \d+|annotated|\d{4}[^)]*)\)$", "", stem, flags=re.I)
    parts = stem.rsplit(" - ", 1)
    if len(parts) == 2 and len(parts[1].split()) <= 12:
        return parts[0]
    return stem


def filename_authors(stem: str):
    cleaned = re.sub(
        r"\s+\((?:copy \d+|annotated|accepted manuscript|nsf archival manuscript|\d{4}[^)]*)\)$",
        "",
        stem,
        flags=re.I,
    )
    parts = cleaned.rsplit(" - ", 1)
    if len(parts) == 2 and len(parts[1].split()) <= 12:
        return parts[1]
    return None


def load_dimensions():
    with (CLASS_DIR / "dimensions.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_key = {row["dimension"]: row for row in rows}
    groups = []
    seen = set()
    for row in rows:
        if row["group"] not in seen:
            seen.add(row["group"])
            groups.append(row["group"])
    return rows, by_key, groups


DIMENSIONS, DIM_BY_KEY, GROUPS = load_dimensions()


def P(*patterns: str):
    return [re.compile(pattern, re.I) for pattern in patterns]


# Patterns are deliberately specific. A term must appear in the title/abstract/lead,
# or repeatedly in the non-reference body, before it is emitted as a supported value.
RULES: dict[str, dict[str, list[re.Pattern]]] = {
    "task.role": {
        "alignment": P(r"\b(sequence|structur(?:e|al)|profile|multiple) align(?:ment|er|ing)\b", r"\blongest common subsequence\b"),
        "distance_estimation": P(r"\b(distance|dissimilarity) (?:estimat|comput)", r"\bedit distance\b", r"\bphylogenetic distance\b"),
        "homology_search": P(r"\bhomolog(?:y|ous) (?:search|detect|retriev)", r"\bremote homology\b"),
        "read_mapping": P(r"\bread map(?:ping|per)\b", r"\bmap(?:ping|s) (?:reads|sequences) (?:to|against)\b", r"\bshort-read align"),
        "assembly": P(r"\bgenome assembl", r"\bde novo assembl", r"\bassembly graph\b"),
        "variant_calling": P(r"\bvariant call", r"\bgenotyp(?:e|ing)\b"),
        "clustering": P(r"\bcluster(?:ing|s) (?:protein|sequence|genome|read)", r"\bsequence clustering\b"),
        "classification": P(r"\b(?:sequence|protein|taxonomic) classification\b"),
        "structured_prediction": P(r"\bstructured prediction\b", r"\bsequence labeling\b"),
        "motif_search": P(r"\bmotif (?:search|discover|find|recognition)\b", r"\bpattern recognition\b"),
        "gene_finding": P(r"\bgene (?:finding|prediction)\b"),
        "phylogeny": P(r"\bphylogen(?:y|etic)\b", r"\bevolutionary tree\b"),
        "data_storage_coding": P(r"\bdna (?:data )?storage\b", r"\bconstrained cod(?:e|ing)\b.*\bdna\b"),
        "error_correction": P(r"\berror correct(?:ion|ing)\b", r"\bdeletion[-, ]+insertion[-, ]+correcting code"),
    },
    "task.arity": {
        "single_sequence": P(r"\blongest increasing subsequence\b", r"\ba single sequence\b"),
        "sequence_sequence": P(r"\bpairwise (?:sequence )?align", r"\btwo (?:strings|sequences)\b", r"\bstring[- ]to[- ]string\b"),
        "sequence_profile": P(r"\bsequence[- ]to[- ]profile\b", r"\bsequence (?:against|and) (?:a )?profile\b"),
        "profile_profile": P(r"\bprofile[- ]profile\b", r"\bprofile to profile\b"),
        "multiple_sequences": P(r"\bmultiple[- ](?:protein[- ])?sequence alignment\b", r"\bmultiple alignment\b", r"\bmsa\b"),
        "sequence_graph": P(r"\bsequence[- ]to[- ]graph\b", r"\bsequence (?:alignment )?(?:to|against) (?:a )?(?:variation |pangenome |directed )?graph\b", r"\bgraph alignment\b"),
        "graph_graph": P(r"\bgraph[- ]to[- ]graph\b", r"\bgraph alignment between\b"),
        "sequence_database": P(r"\bsequence database search\b", r"\bsearch(?:ing)? (?:a|the|large) (?:protein |sequence |genomic )?database\b", r"\bdatabase search(?:ing)?\b"),
    },
    "entity.domain": {
        "abstract_symbols": P(r"\bstrings? over (?:an|a) alphabet\b", r"\babstract (?:sequence|symbol)", r"\bcombinatorial string"),
        "text": P(r"\btext search", r"\btext string", r"\btext processing\b"),
        "binary_data": P(r"\bbinary (?:string|sequence|code|data)\b", r"\bbit string\b"),
        "dna": P(r"\bdna\b", r"\bgenom(?:e|ic)\b", r"\bnucleotide sequence"),
        "rna": P(r"\brna\b", r"\btranscript(?:ome|omic)\b"),
        "protein": P(r"\bprotein\b", r"\bamino acid\b", r"\bproteom"),
        "codons": P(r"\bcodon(?:s| sequence)?\b", r"\bgenetic code\b"),
        "time_series": P(r"\btime series\b", r"\btemporal sequence\b"),
        "speech": P(r"\bspeech recognition\b", r"\baudio[- ]to[- ]score\b"),
        "music": P(r"\bmusic (?:sequence|alignment)\b", r"\baudio[- ]to[- ]score\b"),
        "events": P(r"\bevent sequence\b"),
        "structures": P(r"\bprotein structure\b", r"\bstructural alignment\b", r"\bmolecular surface\b"),
        "distributions": P(r"\bprobability distributions?\b", r"\boptimal transport\b"),
    },
    "entity.alphabet": {
        "binary": P(r"\bbinary alphabet\b", r"\balphabet \{0, ?1\}"),
        "fixed_finite": P(r"\bfixed (?:finite )?alphabet\b", r"\bfinite alphabet\b"),
        "variable_finite": P(r"\balphabet size\b", r"\bsize of the alphabet\b"),
        "ordered": P(r"\btotally ordered\b", r"\bordered (?:set|alphabet|sequence)\b"),
        "unbounded_discrete": P(r"\bunbounded alphabet\b", r"\binteger alphabet\b"),
        "continuous": P(r"\bcontinuous (?:feature|signal|space|sequence)\b"),
        "set_valued": P(r"\bindeterminate string\b", r"\bdegenerate (?:base|symbol|string)\b", r"\bset-valued\b"),
        "probabilistic": P(r"\bprobabilistic (?:symbol|sequence|alphabet)\b", r"\bprofile hmm\b"),
    },
    "entity.unit": {
        "character": P(r"\bcharacters?\b", r"\bsymbols? of (?:a|the) string\b"),
        "base": P(r"\b(?:dna|rna) bases?\b", r"\bnucleotides?\b"),
        "amino_acid": P(r"\bamino acids?\b", r"\bresidue(?:s| pairs)?\b"),
        "codon": P(r"\bcodons?\b"),
        "kmer": P(r"\bk[- ]?mers?\b", r"\bq[- ]grams?\b"),
        "run": P(r"\bruns? of (?:equal|identical)\b", r"\brun[- ]length encoded\b"),
        "word_token": P(r"\bword tokens?\b", r"\btokenized text\b"),
        "sample": P(r"\btime[- ]series samples?\b"),
        "event": P(r"\bevents?\b"),
        "vector": P(r"\bembedding vectors?\b", r"\bfeature vectors?\b"),
        "distribution": P(r"\bprobability distributions?\b"),
        "graph_node": P(r"\bgraph (?:nodes|vertices)\b", r"\bvertex labels?\b"),
    },
    "representation.symbol": {
        "character": P(r"\bcharacter representation\b", r"\bcharacters? from (?:an|the) alphabet\b"),
        "integer_id": P(r"\binteger encod(?:e|ing)\b", r"\bsymbol ids?\b"),
        "bit_packed": P(r"\bpacked (?:bits?|integers?)\b", r"\b2[- ]bit encod"),
        "bit_set": P(r"\bbit[- ]?sets?\b", r"\bbit masks?\b"),
        "one_hot": P(r"\bone[- ]hot\b"),
        "probability_vector": P(r"\bprobability vectors?\b", r"\bposition weight matrix\b"),
        "dense_vector": P(r"\bdense (?:embedding )?vectors?\b", r"\bcontinuous embeddings?\b"),
        "run_pair": P(r"\b(?:character|symbol)[-, ]+(?:run )?(?:length|count) pairs?\b", r"\brun-length representation\b"),
        "structured_object": P(r"\bstructured (?:token|object|representation)\b"),
    },
    "representation.sequence": {
        "array": P(r"\barray representation\b", r"\bsequence arrays?\b"),
        "string": P(r"\binput strings?\b", r"\bsequence strings?\b"),
        "run_list": P(r"\brun[- ]length encod(?:ed|ing)\b", r"\blist of runs\b"),
        "sparse_matrix": P(r"\bsparse matrices?\b"),
        "dense_matrix": P(r"\bdense matrices?\b", r"\bsubstitution matrix\b"),
        "tensor": P(r"\btensor representation\b", r"\bsequence tensor\b"),
        "profile": P(r"\bsequence profiles?\b", r"\bposition[- ]specific scoring matrix\b", r"\bprofile hmm\b"),
        "graph": P(r"\b(?:variation|pangenome|sequence|assembly|partial order) graph\b"),
        "sketch": P(r"\bminhash\b", r"\bsequence sketch(?:es|ing)?\b"),
        "embedding_vector": P(r"\bsequence embeddings?\b", r"\bembedding vectors?\b"),
        "grammar": P(r"\bstraight[- ]line program\b", r"\bgrammar[- ]compressed\b"),
    },
    "representation.invariance": {
        "lossless": P(r"\blossless\b"),
        "homopolymer_collapse": P(r"\bhomopolymer[- ]compress", r"\bhpc minimizer"),
        "reverse_complement_canonical": P(r"\bcanonical (?:k[- ]?mer|minimizer)\b", r"\breverse[- ]complement canonical"),
        "case_fold": P(r"\bcase[- ]insensitive\b", r"\bcase fold"),
        "quantized": P(r"\bquantiz(?:e|ed|ation)\b", r"\bproduct quantization\b"),
        "order_discarded": P(r"\bignore(?:s|d)? (?:the )?order\b", r"\bbag of (?:k[- ]mers|words)\b"),
        "learned_lossy": P(r"\blearned (?:compressed )?representation\b", r"\blatent representation\b"),
    },
    "storage.scheme": {
        "uncompressed": P(r"\buncompressed string\b", r"\buncompressed sequence\b"),
        "rle": P(r"\brun[- ]length encod"),
        "bit_packing": P(r"\bbit[- ]pack", r"\bpacked (?:8|16|32|64)[- ]bit"),
        "delta": P(r"\bdelta encod"),
        "grammar_slp": P(r"\bstraight[- ]line program\b", r"\bgrammar[- ]compress"),
        "lz": P(r"\blempel[- ]ziv\b", r"\blz77\b", r"\blz78\b"),
        "bwt": P(r"\bburrows[- ]wheeler transform\b", r"\bbwt\b"),
        "entropy": P(r"\bentropy cod", r"\bhuffman cod"),
        "general_archive": P(r"\bgzip\b", r"\bgeneral[- ]purpose compression\b"),
        "succinct_graph": P(r"\bsuccinct (?:graph|representation)\b", r"\bcompressed graph index\b"),
    },
    "storage.compute_domain": {
        "uncompressed": P(r"\bon uncompressed (?:strings|sequences)\b"),
        "direct_compressed": P(r"\bdirectly on (?:the )?compressed\b", r"\bwithout decompress"),
        "decompress_then_compute": P(r"\bdecompress(?:ed|ion)? (?:before|then|prior)\b"),
        "compressed_seeds_only": P(r"\bcompressed (?:minimizers?|seeds?)\b", r"\bhomopolymer[- ]compressed minimizers?\b"),
        "mixed": P(r"\bhybrid compressed\b", r"\bpartially compressed\b"),
    },
    "storage.container": {
        "fasta": P(r"\bfasta(?:q)? format\b", r"\.fasta\b"),
        "fastq": P(r"\bfastq\b"),
        "gfa": P(r"\bgfa(?:2)? format\b", r"\.gfa\b"),
        "sam_bam_cram": P(r"\b(?:sam|bam|cram) format\b"),
        "vcf": P(r"\bvcf(?: format| file)?\b"),
        "stockholm": P(r"\bstockholm format\b"),
        "csv_json": P(r"\b(?:csv|json) format\b"),
        "binary_custom": P(r"\bcustom binary format\b"),
    },
    "preprocess.transform": {
        "none": P(r"\bwithout preprocessing\b", r"\bno preprocessing\b"),
        "tokenize": P(r"\btokeniz(?:e|ed|ation)\b"),
        "rle": P(r"\brun[- ]length encod"),
        "homopolymer_collapse": P(r"\bhomopolymer[- ]compress"),
        "reverse_complement": P(r"\breverse complements?\b"),
        "translation": P(r"\bsix[- ]frame translation\b", r"\btranslate(?:d|s)? (?:dna|nucleotide).*(?:protein|amino acid)\b"),
        "masking": P(r"\blow[- ]complexity mask", r"\bsequence masking\b"),
        "normalization": P(r"\bnormaliz(?:e|ed|ation) (?:the )?(?:score|embedding|input|vector)"),
        "embedding": P(r"\bcompute(?:s|d|ing)? (?:the )?embeddings?\b", r"\bembedding model\b"),
        "index_build": P(r"\bbuild(?:ing|s)? (?:an|the) index\b", r"\bindex construction\b"),
        "match_matrix": P(r"\bmatch matrices?\b", r"\bsimilarity matrices?\b"),
        "fft": P(r"\bfast fourier transform\b", r"\bfft\b"),
    },
    "preprocess.index": {
        "none": P(r"\bwithout (?:an )?index\b", r"\bindex[- ]free\b"),
        "hash_kmer": P(r"\bk[- ]?mer hash", r"\bhash table.*k[- ]?mer"),
        "minimizer": P(r"\bminimizers?\b"),
        "syncmer": P(r"\bsyncmers?\b"),
        "strobemer": P(r"\bstrobemers?\b"),
        "suffix_array": P(r"\bsuffix arrays?\b"),
        "suffix_tree": P(r"\bsuffix trees?\b"),
        "fm_index": P(r"\bfm[- ]index\b"),
        "automaton": P(r"\bsuffix automat", r"\bfinite automat"),
        "sketch": P(r"\bminhash sketch", r"\bsequence sketches?\b"),
        "ann": P(r"\bapproximate nearest neighbou?r\b", r"\bhnsw\b", r"\bvector index\b"),
        "lookup_blocks": P(r"\blookup tables?\b", r"\bprecomputed blocks?\b"),
    },
    "preprocess.reuse": {
        "per_input": P(r"\bpreprocess(?:ed|ing) each (?:input|sequence)\b"),
        "per_pair": P(r"\bfor each (?:sequence )?pair\b"),
        "per_database": P(r"\bindex(?:ed|ing) (?:the )?database\b", r"\bprecomputed database\b"),
        "per_batch": P(r"\bbatch preprocessing\b", r"\bfor each batch\b"),
        "offline_training": P(r"\bpre[- ]train(?:ed|ing)\b", r"\boffline train(?:ed|ing)\b"),
    },
    "entity_cmp.family": {
        "equality": P(r"\bsymbol equality\b", r"\bcharacters? (?:are )?equal\b", r"\bexact matches?\b"),
        "set_overlap": P(r"\bset intersection\b", r"\bambiguous (?:base|symbol).*(?:match|overlap)\b"),
        "ordering": P(r"\bincreasing subsequence\b", r"\btotal order\b"),
        "substitution_table": P(r"\bsubstitution matr", r"\bpam\d*\b", r"\bblosum\d*\b"),
        "position_specific": P(r"\bposition[- ]specific scoring matr", r"\bpssm\b", r"\bprofile score"),
        "dot_product": P(r"\bdot product\b", r"\binner product\b"),
        "cosine": P(r"\bcosine (?:similarity|distance)\b"),
        "lp_distance": P(r"\beuclidean distance\b", r"\bl[12] distance\b"),
        "kernel": P(r"\bkernel function\b", r"\bsequence kernel\b"),
        "learned": P(r"\blearned (?:similarity|score|scoring|substitution)\b", r"\bneural (?:similarity|scoring)\b"),
        "likelihood": P(r"\blog[- ]likelihood\b", r"\bemission probability\b"),
    },
    "entity_cmp.codomain": {
        "boolean": P(r"\bboolean (?:match|comparison|value)\b", r"\bbinary match (?:matrix|indicator)\b"),
        "integer": P(r"\binteger (?:score|cost|weight)\b"),
        "real": P(r"\breal[- ]valued (?:score|similarity|cost)\b", r"\bfloating[- ]point score\b"),
        "probability": P(r"\bmatch probabilit", r"\bposterior probabilit"),
        "vector": P(r"\breturns? (?:an )?embedding vector\b"),
        "set": P(r"\breturns? (?:a )?set of\b"),
    },
    "entity_cmp.context": {
        "context_free": P(r"\bcontext[- ]free (?:score|comparison)\b", r"\bconstant substitution score\b"),
        "position_dependent": P(r"\bposition[- ]specific\b", r"\bposition[- ]dependent score"),
        "neighborhood": P(r"\blocal context\b", r"\bneighbou?rhood (?:of|around) (?:the )?(?:residue|base|symbol)"),
        "whole_sequence": P(r"\bwhole[- ]sequence context\b", r"\bglobal context embeddings?\b"),
        "cross_sequence": P(r"\bcross[- ]attention\b", r"\bjointly encode(?:s|d)? (?:the )?two sequences\b"),
        "profile_conditioned": P(r"\bprofile[- ]conditioned\b", r"\bsequence[- ]profile score"),
    },
    "entity_cmp.property": {
        "symmetric": P(r"\bsymmetric (?:score|function|similarity|comparator)\b"),
        "asymmetric": P(r"\basymmetric (?:score|function|comparison)\b"),
        "reflexive": P(r"\breflexive\b"),
        "transitive": P(r"\btransitive\b"),
        "nonnegative": P(r"\bnon[- ]negative (?:score|cost|function)\b"),
        "identity_of_indiscernibles": P(r"\bidentity of indiscernibles\b"),
        "triangle_inequality": P(r"\btriangle inequality\b"),
    },
    "sequence_cmp.family": {
        "lcs_length": P(r"\blcs length\b", r"\blength of (?:a|the) longest common subsequence\b"),
        "lis_length": P(r"\blis length\b", r"\blength of (?:a|the) longest increasing subsequence\b"),
        "edit_distance": P(r"\bedit distance\b", r"\blevenshtein distance\b"),
        "alignment_score": P(r"\balignment score\b", r"\boptimal (?:global|local|pairwise) alignment\b"),
        "percent_identity": P(r"\bpercent(?:age)? identity\b", r"\bsequence identity\b"),
        "dtw": P(r"\bdynamic time warping\b", r"\bdtw\b"),
        "soft_dtw": P(r"\bsoft[- ]dtw\b"),
        "optimal_transport": P(r"\boptimal transport (?:distance|cost|alignment)\b", r"\bwasserstein distance\b"),
        "jaccard": P(r"\bjaccard (?:similarity|distance|index)\b"),
        "minhash_estimate": P(r"\bminhash\b"),
        "embedding_distance": P(r"\bembedding (?:similarity|distance)\b", r"\bcosine similarity.*embedding"),
        "likelihood": P(r"\bsequence likelihood\b", r"\balignment likelihood\b"),
        "phylogenetic_distance": P(r"\bphylogenetic distance\b", r"\bevolutionary distance\b"),
    },
    "sequence_cmp.property": {
        "symmetric": P(r"\bsymmetric distance\b", r"\bsymmetric similarity\b"),
        "asymmetric": P(r"\basymmetric distance\b", r"\basymmetric alignment\b"),
        "nonnegative": P(r"\bnon[- ]negative distance\b"),
        "zero_self": P(r"\bd\(x, ?x\) ?= ?0\b", r"\bzero self[- ]distance\b"),
        "identity_of_indiscernibles": P(r"\bidentity of indiscernibles\b"),
        "triangle_inequality": P(r"\btriangle inequality\b"),
        "metric": P(r"\bis a metric\b", r"\bmetric distance\b"),
        "pseudometric": P(r"\bpseudometric\b"),
        "divergence": P(r"\bdivergence between\b", r"\bsoft[- ]dtw divergence\b"),
        "similarity_only": P(r"\bsimilarity score\b", r"\bnot a metric\b"),
    },
    "objective.problem": {
        "lcs": P(r"\blongest common subsequences?\b", r"\blcs problem\b"),
        "longest_common_substring": P(r"\blongest common substring\b"),
        "lis": P(r"\blongest increasing subsequences?\b"),
        "edit_distance": P(r"\bedit distance\b", r"\bstring[- ]to[- ]string correction\b"),
        "weighted_alignment": P(r"\bweighted (?:sequence )?alignment\b", r"\baffine[- ]gap (?:alignment|cost)\b", r"\boptimal alignment score\b"),
        "dtw": P(r"\bdynamic time warping\b", r"\bdtw\b"),
        "optimal_transport": P(r"\boptimal transport\b", r"\bsinkhorn\b"),
        "viterbi": P(r"\bviterbi\b"),
        "partition_function": P(r"\bpartition function\b"),
        "sum_of_pairs": P(r"\bsum[- ]of[- ]pairs\b", r"\bsum of pairs score\b"),
        "tree_alignment": P(r"\btree alignment\b", r"\bphylogeny[- ]aware alignment\b"),
        "constrained_coding": P(r"\bconstrained cod(?:e|ing)\b", r"\bgc[- ]content constraint\b"),
        "retrieval": P(r"\binformation retrieval\b", r"\bnearest[- ]neighbou?r retrieval\b", r"\bprotein search\b"),
    },
    "objective.optimization": {
        "maximize": P(r"\bmaximiz(?:e|es|ing) (?:the )?(?:score|length|similarity|objective)\b", r"\bmaximum[- ]score alignment\b"),
        "minimize": P(r"\bminimiz(?:e|es|ing) (?:the )?(?:cost|distance|objective)\b", r"\bminimum edit\b"),
        "marginalize": P(r"\bsum over (?:all )?(?:alignments|paths)\b", r"\bmarginali[sz](?:e|ation)\b"),
        "count": P(r"\bcount(?:s|ing)? (?:the )?(?:number of )?(?:solutions|alignments|subsequences|paths)\b"),
        "enumerate": P(r"\benumerat(?:e|es|ing|ion) (?:all )?(?:solutions|alignments|subsequences|paths)\b"),
        "multiobjective": P(r"\bmulti[- ]objective\b", r"\bmultiple objectives\b"),
    },
    "objective.constraint": {
        "unrestricted": P(r"\bunrestricted (?:scoring|alignment|edit distance)\b"),
        "anchors": P(r"\banchor(?:ed|s)? alignment\b"),
        "band": P(r"\bbanded (?:dynamic programming|alignment)\b", r"\bwithin (?:a )?band\b"),
        "collinearity": P(r"\bcollinear(?:ity)? constraint\b", r"\bchain(?:ing)? anchors\b"),
        "splicing": P(r"\bspliced alignment\b", r"\bsplice sites?\b"),
        "frameshifts": P(r"\bframeshift(?:s| alignment)?\b"),
        "rearrangements": P(r"\brearrangement(?:s)?\b", r"\binversions? and translocations?\b"),
        "circular": P(r"\bcircular (?:sequence|alignment|genome)\b"),
        "motifs": P(r"\bmotif constraints?\b", r"\bpattern constraints?\b"),
        "haplotype_paths": P(r"\bhaplotype[- ](?:aware|constrained)\b", r"\bhaplotype paths?\b"),
        "length_bound": P(r"\bbounded (?:edit )?distance\b", r"\bwithin k edits\b", r"\blength[- ]bounded\b"),
    },
    "alignment.boundary": {
        "global": P(r"\bglobal (?:sequence |pairwise )?alignment\b", r"\bneedleman[- ]wunsch\b"),
        "local": P(r"\blocal (?:sequence |pairwise )?alignment\b", r"\bsmith[- ]waterman\b"),
        "semiglobal": P(r"\bsemi[- ]global alignment\b", r"\bsemiglobal alignment\b"),
        "overlap": P(r"\boverlap alignment\b"),
        "prefix": P(r"\bprefix alignment\b", r"\bprefix edit distance\b"),
        "infix": P(r"\binfix alignment\b"),
        "custom": P(r"\bcustom boundary conditions\b", r"\bfree[- ]end gaps?\b"),
    },
    "alignment.multiplicity": {
        "one_to_one": P(r"\bone[- ]to[- ]one alignment\b", r"\bpairwise alignment\b"),
        "one_to_many": P(r"\bone[- ]to[- ]many\b", r"\bone query against (?:a|the) database\b"),
        "many_to_many": P(r"\ball[- ](?:versus|vs)[- ]all\b", r"\bmany[- ]to[- ]many\b"),
        "unaligned_allowed": P(r"\bunaligned residues?\b", r"\bpartial alignment\b"),
    },
    "alignment.strategy": {
        "direct_pairwise": P(r"\bdirect pairwise alignment\b", r"\bpairwise dynamic programming\b"),
        "progressive": P(r"\bprogressive (?:multiple |profile |structural )?alignment\b"),
        "guide_tree": P(r"\bguide tree\b"),
        "iterative_refinement": P(r"\biterative refinement\b", r"\brefine(?:s|ment) (?:the )?alignment\b"),
        "consistency": P(r"\bconsistency[- ]based\b", r"\bprobabilistic consistency\b"),
        "center_star": P(r"\bcenter[- ]star\b", r"\bstar alignment\b"),
        "joint_optimization": P(r"\bjoint(?:ly)? optimi[sz](?:e|ation).*(?:alignment|phylogen)\b"),
        "template_based": P(r"\btemplate[- ]based alignment\b", r"\btemplate modeling\b"),
    },
    "scoring.substitution": {
        "unit": P(r"\bunit (?:edit|substitution) cost\b"),
        "match_mismatch": P(r"\bmatch[- ]mismatch (?:score|scoring)\b", r"\bmatch score.*mismatch (?:score|penalty)\b"),
        "arbitrary_table": P(r"\barbitrary scoring matr", r"\bgeneral substitution matr"),
        "pam": P(r"\bpam(?:30|70|120|250)?\b"),
        "blosum": P(r"\bblosum(?:45|50|62|80|90)?\b"),
        "pssm": P(r"\bposition[- ]specific scoring matr", r"\bpssm\b"),
        "contextual": P(r"\bcontext[- ]dependent (?:substitution|score)\b"),
        "learned": P(r"\blearned (?:substitution|residue|match) score\b", r"\bneural scoring function\b"),
        "quality_aware": P(r"\bbase[- ]quality[- ]aware\b", r"\bquality scores?.*(?:alignment|substitution)\b"),
    },
    "scoring.gap": {
        "none": P(r"\bungapped alignment\b", r"\bno gaps?\b"),
        "unit": P(r"\bunit (?:gap|insertion|deletion) cost\b"),
        "linear": P(r"\blinear gap (?:cost|penalty)\b"),
        "affine": P(r"\baffine[- ]gap\b", r"\bgap[- ]open.*gap[- ]extension\b"),
        "two_piece_affine": P(r"\btwo[- ]piece affine\b", r"\bdual affine\b"),
        "convex": P(r"\bconvex gap (?:cost|penalty)\b"),
        "concave": P(r"\bconcave gap (?:cost|penalty)\b"),
        "arbitrary": P(r"\barbitrary gap (?:cost|function)\b"),
        "learned": P(r"\blearned gap (?:cost|penalty|score)\b"),
        "splice_specific": P(r"\bintron (?:penalty|score)\b", r"\bsplice[- ]site scoring\b"),
    },
    "scoring.operation": {
        "match": P(r"\bmatch(?:ing)? (?:operation|score|characters|symbols)\b"),
        "substitution": P(r"\bsubstitution(?:s| operation| cost| score)\b"),
        "insertion": P(r"\binsertion(?:s| operation| cost| penalty)\b"),
        "deletion": P(r"\bdeletion(?:s| operation| cost| penalty)\b"),
        "transposition": P(r"\btransposition(?:s)?\b"),
        "duplication": P(r"\bduplication(?:s)?\b"),
        "reversal": P(r"\breversal(?:s)?\b"),
        "splice": P(r"\bsplice junctions?\b", r"\bintron operation\b"),
        "frameshift": P(r"\bframeshift(?:s)?\b"),
    },
    "scoring.scale": {
        "nonnegative_cost": P(r"\bnon[- ]negative (?:edit )?costs?\b"),
        "signed_reward": P(r"\bpositive match.*negative mismatch\b", r"\breward.*penalty\b"),
        "log_odds": P(r"\blog[- ]odds (?:score|matrix)\b"),
        "probability": P(r"\bprobabilistic score\b", r"\bposterior probabilit"),
        "normalized": P(r"\bnormalized (?:alignment )?score\b"),
        "unnormalized": P(r"\bunnormalized (?:score|similarity)\b"),
    },
    "solver.family": {
        "dynamic_programming": P(r"\bdynamic programming\b", r"\bdp recurrence\b"),
        "lis_reduction": P(r"\breduc(?:e|tion) to (?:the )?(?:longest increasing subsequence|lis)\b"),
        "binary_search": P(r"\bbinary search\b"),
        "four_russians": P(r"\bfour russians\b", r"\bmethod of four russians\b"),
        "bit_parallel": P(r"\bbit[- ]parallel\b", r"\bbit[- ]vector algorithm\b"),
        "wavefront_alignment": P(r"\bwavefront alignment algorithm\b", r"\bwfa\b"),
        "a_star": P(r"\ba\* (?:search|algorithm|alignment)\b", r"\ba-star\b"),
        "dijkstra": P(r"\bdijkstra(?:'s)?\b"),
        "flow": P(r"\bmin(?:imum)?[- ]cost flow\b", r"\bnetwork flow\b"),
        "optimal_transport": P(r"\boptimal transport\b"),
        "sinkhorn": P(r"\bsinkhorn\b"),
        "fft": P(r"\bfast fourier transform\b", r"\bfft[- ]based\b"),
        "automaton": P(r"\bsuffix automat", r"\bfinite[- ]state automat"),
        "branch_and_bound": P(r"\bbranch[- ]and[- ]bound\b"),
        "ilp": P(r"\binteger linear program", r"\bmixed[- ]integer program"),
        "sat": P(r"\bsat solver\b", r"\bboolean satisfiability\b"),
        "maximum_clique": P(r"\bmaximum clique\b"),
        "greedy": P(r"\bgreedy algorithm\b", r"\bgreedy extension\b"),
        "metaheuristic": P(r"\bmetaheuristic\b", r"\bgenetic algorithm\b", r"\bant colony\b"),
        "neural_inference": P(r"\bneural network\b", r"\bdeep learning (?:model|method|approach)\b"),
    },
    "dp.state": {
        "grid": P(r"\bdp (?:matrix|table|grid)\b", r"\bdynamic programming matrix\b"),
        "multidimensional_grid": P(r"\bmultidimensional dynamic programming\b", r"\bthree[- ]dimensional dp\b"),
        "sparse_matches": P(r"\bsparse dynamic programming\b", r"\bmatching pairs?\b"),
        "score_frontier": P(r"\bwavefronts? of score\b", r"\bscore[- ]indexed wavefront\b"),
        "graph_product": P(r"\bproduct graph\b", r"\bsequence[- ]graph dp\b"),
        "profile_states": P(r"\bprofile hmm states?\b", r"\bmatch, insertion,? and deletion states\b"),
        "intervals": P(r"\binterval dynamic programming\b"),
        "subsets": P(r"\bsubset dynamic programming\b"),
    },
    "dp.algebra": {
        "min_plus": P(r"\bmin[- ]plus\b", r"\bmin(?:imum)?.*\+.*(?:insertion|deletion|substitution)\b"),
        "max_plus": P(r"\bmax[- ]plus\b", r"\bmax(?:imum)?.*\+.*(?:match|score)\b"),
        "sum_product": P(r"\bsum[- ]product\b", r"\bforward[- ]backward algorithm\b"),
        "logsumexp": P(r"\blog[- ]sum[- ]exp\b"),
        "smoothed_max": P(r"\bsmooth(?:ed|ing) (?:the )?max\b"),
        "smoothed_min": P(r"\bsmooth(?:ed|ing) (?:the )?min\b", r"\bsoft[- ]min\b"),
        "boolean": P(r"\bboolean semiring\b", r"\bboolean dynamic programming\b"),
        "counting": P(r"\bcounting dynamic programming\b", r"\bnumber of optimal (?:paths|solutions)\b"),
        "pareto": P(r"\bpareto (?:front|optimal)\b"),
    },
    "dp.layout": {
        "full_table": P(r"\bfull (?:dp )?(?:matrix|table)\b", r"\bstor(?:e|ing) the entire (?:matrix|table)\b"),
        "rolling_rows": P(r"\brolling rows?\b", r"\btwo (?:dp )?rows?\b"),
        "rolling_columns": P(r"\brolling columns?\b", r"\btwo (?:dp )?columns?\b"),
        "checkpoint": P(r"\bcheckpoint(?:ing|s)?\b"),
        "divide_conquer": P(r"\bdivide[- ]and[- ]conquer\b", r"\bhirschberg(?:'s)? algorithm\b"),
        "bit_vector": P(r"\bbit[- ]vectors?\b", r"\bbit[- ]parallel\b"),
        "blocked": P(r"\bblocked dynamic programming\b", r"\btil(?:e|ed|ing) (?:the )?(?:dp )?matrix\b"),
        "tabulated": P(r"\bprecomputed tables?\b", r"\bblock tabulation\b"),
        "frontier": P(r"\bwavefront\b", r"\bfrontier states?\b"),
        "sparse": P(r"\bsparse dynamic programming\b", r"\bsparse (?:dp )?matrix\b"),
        "tensor": P(r"\bdifferentiable (?:dp|dynamic programming)\b", r"\bdp tensor\b"),
    },
    "dp.schedule": {
        "row_major": P(r"\brow[- ](?:by[- ])?row\b", r"\brow[- ]major\b"),
        "column_major": P(r"\bcolumn[- ](?:by[- ])?column\b", r"\bcolumn[- ]major\b"),
        "antidiagonal": P(r"\banti[- ]diagonal\b", r"\bminor diagonal wavefront\b"),
        "score_order": P(r"\bincreasing score order\b", r"\bscore[- ]ordered wavefront\b"),
        "topological": P(r"\btopological order\b", r"\btopological sort\b"),
        "best_first": P(r"\bbest[- ]first search\b"),
        "recursive": P(r"\brecursive (?:dynamic programming|decomposition|algorithm)\b"),
        "blocked": P(r"\bblock[- ]wise\b", r"\btiled wavefront\b"),
    },
    "dp.differentiation": {
        "none": P(r"\bnon[- ]differentiable dynamic programming\b"),
        "score_gradient": P(r"\bgradient of (?:the )?(?:alignment )?(?:score|loss)\b", r"\bdifferentiable (?:alignment|dynamic programming)\b"),
        "soft_solution": P(r"\bsoft alignment\b", r"\brelax(?:ed|ation of) (?:the )?(?:alignment|solution)\b"),
        "hard_solution_surrogate": P(r"\bstraight[- ]through estimator\b", r"\bsurrogate gradient\b"),
        "implicit_gradient": P(r"\bimplicit differentiation\b"),
        "train_only": P(r"\bduring training only\b", r"\bdifferentiable training objective\b"),
        "inference_time": P(r"\bat inference time.*differentiable\b"),
    },
    "trace.method": {
        "none": P(r"\bscore[- ]only\b", r"\bwithout traceback\b", r"\bdoes not (?:compute|provide) (?:an )?alignment\b"),
        "parent_pointers": P(r"\btraceback pointers?\b", r"\bparent pointers?\b"),
        "recompute": P(r"\brecomput(?:e|es|ing) (?:the )?(?:dp|score|rows|matrix)\b"),
        "divide_conquer": P(r"\bdivide[- ]and[- ]conquer traceback\b", r"\bhirschberg(?:'s)? (?:traceback|algorithm)\b"),
        "checkpoint": P(r"\bcheckpoint(?:ed|ing) traceback\b"),
        "backward_dp": P(r"\bbackward dynamic programming\b", r"\bbackward pass.*traceback\b"),
        "graph_search": P(r"\btraceback (?:as|using) (?:a )?graph search\b", r"\bsearch(?:ing)? the traceback graph\b"),
        "enumeration": P(r"\benumerat(?:e|ing) (?:all )?(?:optimal )?(?:paths|alignments|subsequences)\b"),
        "sample_posterior": P(r"\bsampl(?:e|ing) (?:from )?(?:the )?(?:alignment )?posterior\b"),
    },
    "trace.tie_policy": {
        "arbitrary_one": P(r"\bany one (?:optimal )?(?:alignment|solution|subsequence)\b", r"\barbitrary optimal (?:alignment|path)\b"),
        "deterministic_one": P(r"\btie[- ]breaking (?:rule|policy)\b", r"\bdeterministic traceback\b"),
        "all_distinct_strings": P(r"\ball distinct (?:longest common )?subsequences\b"),
        "all_position_alignments": P(r"\ball optimal alignments\b"),
        "all_graph_paths": P(r"\ball (?:optimal )?graph paths\b"),
        "top_k": P(r"\btop[- ]k (?:alignments|paths|solutions)\b"),
        "sampled": P(r"\bsampled alignments\b", r"\bsampling (?:optimal )?paths\b"),
        "capped": P(r"\bmaximum number of (?:alignments|paths|solutions)\b", r"\boutput cap\b"),
    },
    "graph.role": {
        "input_reference": P(r"\b(?:variation|pangenome|sequence) graph (?:reference|input)\b", r"\balign(?:ing|ment) (?:a )?sequence to (?:a )?graph\b"),
        "implicit_edit_state": P(r"\bedit graph\b", r"\balignment graph.*grid\b"),
        "explicit_match_intermediate": P(r"\bmatch graph\b", r"\bcompatibility graph\b"),
        "alignment_output": P(r"\bpartial order alignment graph\b", r"\balignment graph (?:output|represent)\b"),
        "guide_tree": P(r"\bguide tree\b"),
        "probabilistic_model": P(r"\bhidden markov model\b", r"\bprofile hmm\b"),
        "search_index": P(r"\bgraph index\b", r"\bindex graph\b"),
    },
    "graph.topology": {
        "path": P(r"\blinear path graph\b", r"\bgraph is a path\b"),
        "tree": P(r"\bguide tree\b", r"\bphylogenetic tree\b"),
        "dag": P(r"\bdirected acyclic graph\b", r"\bdag\b"),
        "directed_cyclic": P(r"\bdirected cyclic graph\b", r"\bgraphs? with cycles\b"),
        "bidirected": P(r"\bbidirected graph\b"),
        "undirected": P(r"\bundirected graph\b"),
        "hypergraph": P(r"\bhypergraph\b"),
    },
    "graph.label": {
        "base": P(r"\bvertices? labeled with (?:dna )?(?:bases|nucleotides)\b"),
        "string": P(r"\bvertices? labeled (?:by|with) strings?\b", r"\bstring[- ]labeled graph\b"),
        "profile": P(r"\bprofile graph\b", r"\bnodes? (?:store|contain) profiles?\b"),
        "coordinate": P(r"\bcoordinate graph\b", r"\bnode coordinates?\b"),
        "score": P(r"\bweighted graph\b", r"\bedge weights?\b"),
        "unlabelled": P(r"\bunlabelled graph\b", r"\bunlabeled graph\b"),
    },
    "graph.path_semantics": {
        "arbitrary_walk": P(r"\barbitrary walks?\b", r"\bwalks? through (?:the )?graph\b"),
        "simple_path": P(r"\bsimple paths?\b"),
        "haplotype_restricted": P(r"\bhaplotype[- ]restricted\b", r"\bhaplotype paths?\b"),
        "dag_path": P(r"\bpaths? in (?:a|the) dag\b"),
        "bounded_unrolling": P(r"\bunroll(?:ed|ing) (?:the )?cycles?\b", r"\bbounded walks?\b"),
        "orientation_aware": P(r"\borientation[- ]aware\b", r"\breverse orientation\b"),
    },
    "graph.construct": {
        "sequence_to_path": P(r"\bsequences? (?:are )?represented as paths?\b", r"\bsequence[- ]to[- ]path\b"),
        "progressive_poa": P(r"\bprogressive partial[- ]order alignment\b", r"\bpartial order alignment\b"),
        "de_bruijn": P(r"\bde bruijn graph\b"),
        "overlap_graph": P(r"\boverlap graph\b"),
        "variation_graph": P(r"\bvariation graph\b"),
        "match_to_graph": P(r"\bmatch(?:es|ing)? (?:to|into) (?:a|the) graph\b", r"\bmatch graph construction\b"),
        "edit_graph": P(r"\bedit graph\b"),
        "assembly": P(r"\bassembly graph\b"),
        "graph_update": P(r"\bupdate(?:s|d|ing) (?:the )?(?:alignment |reference )?graph\b", r"\binsert(?:s|ing) (?:a )?sequence into (?:the )?graph\b"),
    },
    "graph.traversal": {
        "topological": P(r"\btopological (?:order|sort|traversal)\b"),
        "bfs": P(r"\bbreadth[- ]first search\b", r"\bbfs\b"),
        "dfs": P(r"\bdepth[- ]first search\b", r"\bdfs\b"),
        "dijkstra": P(r"\bdijkstra(?:'s)?\b"),
        "a_star": P(r"\ba\* (?:search|algorithm)\b", r"\ba-star search\b"),
        "best_first": P(r"\bbest[- ]first search\b"),
        "wavefront": P(r"\bwavefront (?:search|traversal|algorithm)\b"),
        "dynamic_programming": P(r"\bdynamic programming (?:over|on) (?:the )?graph\b"),
        "branch_and_bound": P(r"\bbranch[- ]and[- ]bound\b"),
    },
    "graph.traversal_purpose": {
        "construction": P(r"\btravers(?:e|al|ing).*(?:construct|build) (?:the )?graph\b"),
        "scoring": P(r"\bgraph traversal.*(?:score|alignment)\b"),
        "search": P(r"\bgraph search\b", r"\bsearch(?:ing)? (?:the )?graph\b"),
        "reconstruction": P(r"\btraceback (?:graph|path)\b", r"\breconstruct(?:ing)? (?:the )?(?:path|alignment)\b"),
        "enumeration": P(r"\benumerat(?:e|ing) (?:all )?(?:graph )?paths\b"),
        "reachability": P(r"\breachability\b", r"\breachable (?:node|vertex|state)\b"),
    },
    "heuristic.kind": {
        "none": P(r"\bwithout heuristics?\b", r"\bno heuristic\b"),
        "seeding": P(r"\bseed[- ]and[- ]extend\b", r"\bseed(?:ing|s) (?:strategy|scheme|matches)\b"),
        "chaining": P(r"\bseed chaining\b", r"\bchain(?:ing)? (?:the )?(?:seeds|anchors)\b"),
        "banding": P(r"\bbanded (?:dynamic programming|alignment)\b", r"\bfixed band\b"),
        "adaptive_band": P(r"\badaptive band\b", r"\bdynamic band\b"),
        "x_drop": P(r"\bx[- ]drop\b"),
        "z_drop": P(r"\bz[- ]drop\b"),
        "beam": P(r"\bbeam search\b"),
        "greedy": P(r"\bgreedy (?:extension|search|algorithm)\b"),
        "learned": P(r"\blearned heuristic\b", r"\bneural heuristic\b"),
        "progressive": P(r"\bprogressive alignment\b"),
        "randomized": P(r"\brandomized algorithm\b", r"\brandom sampling\b"),
        "admissible_bound": P(r"\badmissible heuristic\b", r"\blower bound heuristic\b"),
        "safe_pruning": P(r"\bsafe pruning\b", r"\bprun(?:e|ing).*(?:without|preserv).*(?:optimal|exact)\b"),
        "genetic": P(r"\bgenetic algorithm\b"),
        "ant_colony": P(r"\bant colony\b"),
    },
    "heuristic.safeguard": {
        "none": P(r"\bno (?:correctness )?safeguard\b"),
        "admissibility_proof": P(r"\bheuristic is admissible\b", r"\bprove(?:s|d)? admissib"),
        "bound_certificate": P(r"\boptimality certificate\b", r"\bbound certificate\b"),
        "band_doubling": P(r"\bband[- ]doubling\b", r"\bdouble(?:s|d) (?:the )?band\b"),
        "exact_fallback": P(r"\bfallback to (?:an )?exact\b", r"\bexact fallback\b"),
        "exhaustive_completion": P(r"\bexhaustive completion\b", r"\buntil (?:the )?search is exhausted\b"),
        "error_bound": P(r"\bapproximation (?:factor|guarantee|bound)\b", r"\berror bound\b"),
    },
    "guarantee.kind": {
        "exact": P(r"\bexact (?:algorithm|alignment|edit distance|solution|computation)\b", r"\boptimal (?:alignment|solution).*(?:guarantee|algorithm)\b"),
        "exact_restricted": P(r"\bexact (?:within|for) (?:the )?(?:band|restricted|bounded)\b", r"\boptimal under (?:the )?(?:constraint|restriction)\b"),
        "bounded_approximation": P(r"\bconstant[- ]factor approximation\b", r"\bapproximation (?:factor|ratio|scheme)\b"),
        "probabilistic": P(r"\bwith (?:high )?probability\b", r"\bprobabilistic guarantee\b"),
        "heuristic": P(r"\bheuristic (?:algorithm|method|approach)\b", r"\bwithout guarantee(?:ing)? optimality\b"),
        "numerical_approximation": P(r"\bnumerical approximation\b", r"\bconvergence tolerance\b"),
        "empirical_only": P(r"\bempirically (?:demonstrate|evaluate|validate)\b", r"\bno theoretical guarantee\b"),
    },
    "guarantee.evidence": {
        "proof": P(r"\bwe prove\b", r"\bproof of (?:correctness|optimality|theorem)\b"),
        "stated_theorem": P(r"\btheorem \d+\b", r"\bthe following theorem\b"),
        "empirical_validation": P(r"\bexperimental results\b", r"\bbenchmark(?:s|ing) (?:show|demonstrate|against)\b"),
        "author_claim": P(r"\bwe claim\b", r"\bthe authors? claim\b"),
        "independent_replication": P(r"\bindependent(?:ly)? reproduc(?:e|ed|tion)\b", r"\bindependent replication\b"),
    },
    "embedding.level": {
        "entity": P(r"\bsymbol embeddings?\b", r"\bamino[- ]acid embeddings?\b"),
        "contextual_entity": P(r"\bcontextual(?:ized)? residue embeddings?\b", r"\bper[- ]residue embeddings?\b"),
        "sequence": P(r"\bsequence[- ]level embeddings?\b", r"\bprotein sequence embeddings?\b"),
        "profile": P(r"\bprofile embeddings?\b"),
        "graph": P(r"\bgraph embeddings?\b", r"\bnode embeddings?\b"),
        "structure": P(r"\bstructure embeddings?\b", r"\bprotein structural embeddings?\b"),
    },
    "embedding.source": {
        "handcrafted": P(r"\bhand[- ]crafted features?\b", r"\bmanually designed features?\b"),
        "physicochemical": P(r"\bphysicochemical (?:properties|features|embedding)\b"),
        "spectral": P(r"\bspectral embeddings?\b", r"\beigenvector embeddings?\b"),
        "geometric": P(r"\bgeometric embeddings?\b", r"\bstructure[- ]aware geometric representation\b"),
        "trained_task": P(r"\btask[- ]specific embeddings?\b", r"\btrained embeddings?\b"),
        "protein_language_model": P(r"\bprotein language model\b", r"\besm[- ]?\d* embeddings?\b", r"\bprot(?:t5|bert)\b"),
        "general_language_model": P(r"\blarge language model\b", r"\btext encoder\b"),
        "random_projection": P(r"\brandom projections?\b"),
    },
    "embedding.use": {
        "entity_score": P(r"\bembedding[- ]based (?:residue|symbol) score\b"),
        "sequence_score": P(r"\bembedding (?:similarity|distance)\b"),
        "seeding": P(r"\bembedding[- ]based seeds?\b", r"\bembeddings?.*(?:seed|candidate) generation\b"),
        "retrieval": P(r"\bembedding[- ]based retrieval\b", r"\bvector database\b"),
        "clustering": P(r"\bcluster(?:ing)? (?:the )?embeddings?\b"),
        "prediction": P(r"\bembeddings? for (?:downstream )?prediction\b"),
        "alignment_training": P(r"\balignment (?:loss|supervision)\b", r"\btrain(?:ed|ing).*alignment\b"),
    },
    "learning.regime": {
        "none": P(r"\bno (?:machine )?learning\b", r"\btraining[- ]free\b"),
        "supervised": P(r"\bsupervised (?:learning|training)\b"),
        "self_supervised": P(r"\bself[- ]supervised\b", r"\bmasked language model(?:ing)?\b"),
        "unsupervised": P(r"\bunsupervised (?:learning|training)\b"),
        "contrastive": P(r"\bcontrastive (?:learning|training|loss)\b"),
        "reinforcement": P(r"\breinforcement learning\b"),
        "fine_tuned": P(r"\bfine[- ]tun(?:e|ed|ing)\b"),
        "frozen_pretrained": P(r"\bfrozen (?:pre[- ]?trained )?(?:model|encoder|embeddings)\b"),
    },
    "learning.component": {
        "embedding": P(r"\blearn(?:ed|ing) (?:the )?embeddings?\b"),
        "substitution": P(r"\blearn(?:ed|ing) (?:a )?(?:substitution|residue similarity|match) score\b"),
        "gap": P(r"\blearn(?:ed|ing) (?:the )?gap (?:cost|penalty|score)\b"),
        "heuristic": P(r"\blearned heuristic\b"),
        "alignment": P(r"\blearn(?:ed|ing) (?:the )?alignment\b", r"\bend[- ]to[- ]end.*alignment\b"),
        "objective": P(r"\blearn(?:ed|ing) (?:the )?(?:loss|objective)\b"),
        "graph": P(r"\blearn(?:ed|ing) (?:the )?graph\b"),
        "classifier": P(r"\btrain(?:ed|ing) (?:a )?classifier\b", r"\bclassification head\b"),
    },
    "learning.alignment_form": {
        "hard": P(r"\bhard alignment\b"),
        "soft": P(r"\bsoft alignment\b"),
        "latent": P(r"\blatent alignment\b"),
        "supervised": P(r"\balignment supervision\b", r"\bsupervised alignments?\b"),
        "surrogate": P(r"\balignment surrogate\b", r"\bsurrogate loss.*alignment\b"),
    },
    "parallel.level": {
        "bit_parallel": P(r"\bbit[- ]parallel\b"),
        "simd": P(r"\bsimd\b", r"\bvector instructions?\b"),
        "entity_pairs": P(r"\bindependent (?:cell|residue|symbol) comparisons?\b"),
        "dp_antidiagonals": P(r"\banti[- ]diagonal parallel", r"\bwavefront parallelism.*dp (?:matrix|table)\b"),
        "dp_tiles": P(r"\bparallel (?:dp )?tiles?\b", r"\btiled dynamic programming\b"),
        "frontiers": P(r"\bparallel wavefronts?\b", r"\bfrontier parallelism\b"),
        "graph_partitions": P(r"\bgraph partition(?:ing)?\b.*\bparallel\b", r"\bparallel graph partitions?\b"),
        "sequence_pairs": P(r"\bparallel (?:pairwise )?alignments?\b", r"\bsequence[- ]level parallel"),
        "database_shards": P(r"\bshard(?:ed|ing) (?:the )?database\b", r"\bdistributed database search\b"),
        "training_batches": P(r"\btraining batches?\b", r"\bdata[- ]parallel training\b"),
    },
    "parallel.backend": {
        "cpu_scalar": P(r"\bsingle[- ]threaded cpu\b", r"\bscalar cpu\b"),
        "cpu_simd": P(r"\b(?:avx|sse|simd)\b", r"\bcpu vector instructions?\b"),
        "cpu_threads": P(r"\bmultithread(?:ed|ing)\b", r"\bopenmp\b", r"\bmultiple cpu threads\b"),
        "gpu": P(r"\bgpu\b", r"\bcuda\b"),
        "multi_gpu": P(r"\bmulti[- ]gpu\b", r"\bmultiple gpus\b"),
        "distributed": P(r"\bdistributed (?:memory|computing|system|algorithm)\b", r"\bmpi\b"),
        "fpga": P(r"\bfpga\b"),
        "asic": P(r"\bapplication[- ]specific integrated circuit\b", r"\b(?:custom )?asic\b"),
        "processing_in_memory": P(r"\bprocessing[- ]in[- ]memory\b", r"\bpim architecture\b"),
    },
    "parallel.communication": {
        "none": P(r"\bno communication\b", r"\bcommunication[- ]free\b"),
        "barriers": P(r"\bsynchronization barriers?\b", r"\bbarrier synchronization\b"),
        "atomics": P(r"\batomic operations?\b"),
        "warp_shuffle": P(r"\bwarp shuffle\b", r"__shfl_"),
        "host_device": P(r"\bhost[- ]to[- ]device\b", r"\bcpu[- ]gpu transfer\b"),
        "device_device": P(r"\bdevice[- ]to[- ]device\b", r"\bgpu[- ]gpu communication\b"),
        "network": P(r"\bnetwork communication\b", r"\bmessage passing\b"),
    },
    "numeric.type": {
        "arbitrary_integer": P(r"\barbitrary[- ]precision integers?\b", r"\bbig integers?\b"),
        "fixed_integer": P(r"\b(?:8|16|32|64)[- ]bit integers?\b", r"\bfixed[- ]width integer\b"),
        "float16": P(r"\b(?:float16|fp16|half precision)\b"),
        "bfloat16": P(r"\bbfloat16\b"),
        "float32": P(r"\b(?:float32|fp32|single precision)\b"),
        "float64": P(r"\b(?:float64|fp64|double precision)\b"),
        "fixed_point": P(r"\bfixed[- ]point arithmetic\b"),
        "boolean": P(r"\bboolean (?:matrix|vector|arithmetic)\b"),
    },
    "numeric.policy": {
        "exact_range": P(r"\bexact integer arithmetic\b", r"\bwithin (?:the )?representable range\b"),
        "saturating": P(r"\bsaturat(?:e|ed|ing) arithmetic\b"),
        "overflow_detected": P(r"\boverflow detection\b", r"\bdetect(?:s|ed) overflow\b"),
        "precision_fallback": P(r"\bfallback to (?:higher|full) precision\b"),
        "rounding": P(r"\brounding error\b", r"\bround(?:ed|ing) to\b"),
        "tolerance": P(r"\bnumerical tolerance\b", r"\bconvergence tolerance\b"),
        "deterministic": P(r"\bdeterministic (?:output|algorithm|tie[- ]break)\b"),
        "nondeterministic": P(r"\bnondeterministic\b", r"\bnon[- ]deterministic\b"),
    },
    "resource.model": {
        "comparison": P(r"\bcomparison model\b", r"\bnumber of comparisons\b"),
        "word_ram": P(r"\bword[- ]ram\b", r"\bword size w\b"),
        "bit_complexity": P(r"\bbit complexity\b", r"\bbit operations\b"),
        "external_memory": P(r"\bexternal[- ]memory model\b", r"\bi/o complexity\b"),
        "parallel_work_span": P(r"\bwork[- ]span model\b", r"\bparallel time.*work\b"),
        "gpu_device": P(r"\bgpu memory\b", r"\bdevice memory\b"),
    },
    "resource.parameter": {
        "raw_lengths": P(r"\bstrings? of lengths? [mn]\b", r"\bsequence lengths?\b"),
        "run_counts": P(r"\bnumber of runs\b", r"\bcompressed lengths?\b"),
        "alphabet_size": P(r"\balphabet size\b", r"\|sigma\|"),
        "match_count": P(r"\bnumber of match(?:es|ing pairs)\b", r"\bmatching pairs? r\b"),
        "optimal_score": P(r"\boptimal (?:alignment )?(?:score|cost) [skd]\b", r"\bparameteri[sz]ed by (?:the )?(?:optimal )?(?:score|distance)\b"),
        "edit_bound": P(r"\bat most k (?:edits|differences)\b", r"\bedit distance k\b"),
        "word_bits": P(r"\bword size\b", r"\bw[- ]bit words?\b"),
        "embedding_dim": P(r"\bembedding dimension\b", r"\bd[- ]dimensional embeddings?\b"),
        "nodes": P(r"\b\|v\|\b", r"\bnumber of (?:graph )?(?:nodes|vertices)\b"),
        "edges": P(r"\b\|e\|\b", r"\bnumber of (?:graph )?edges\b"),
        "sequence_count": P(r"\bnumber of sequences\b", r"\bn sequences?\b.*\bmultiple alignment\b"),
        "output_size": P(r"\boutput[- ]sensitive\b", r"\boutput size\b"),
        "batch_size": P(r"\bbatch size\b", r"\bnumber of alignments per batch\b"),
    },
    "output.kind": {
        "score": P(r"\breturns? (?:the )?(?:optimal )?(?:alignment )?score\b", r"\bscore[- ]only\b"),
        "length": P(r"\bcomput(?:e|es|ing) (?:the )?length of (?:a|the) (?:longest|lcs|lis)\b"),
        "one_subsequence": P(r"\bcomput(?:e|es|ing) (?:a|one) longest common subsequence\b", r"\breconstruct(?:s|ing) (?:an?|one) lcs\b"),
        "one_alignment": P(r"\breconstruct(?:s|ing) (?:an?|one) (?:optimal )?alignment\b", r"\breturns? (?:an?|one) alignment\b"),
        "all_distinct_subsequences": P(r"\ball distinct (?:longest common )?subsequences\b"),
        "all_position_alignments": P(r"\ball optimal alignments\b"),
        "graph_path": P(r"\breturns? (?:the |a )?graph path\b", r"\balignment path in (?:the )?graph\b"),
        "graph_walk": P(r"\breturns? (?:the |a )?graph walk\b"),
        "alignment_graph": P(r"\bpartial order alignment graph\b", r"\balignment graph output\b"),
        "cigar": P(r"\bcigar (?:string|output|format)\b"),
        "endpoints": P(r"\balignment endpoints?\b", r"\bstart and end positions?\b"),
        "ranking": P(r"\branked (?:list|results|hits)\b", r"\btop[- ]k retrieval\b"),
        "soft_matrix": P(r"\bsoft alignment matrix\b", r"\balignment probability matrix\b"),
        "posterior": P(r"\bposterior (?:alignment|probabilities|distribution)\b"),
        "gradient": P(r"\bgradient(?:s)? (?:with respect to|of)\b"),
        "count": P(r"\bnumber of (?:optimal )?(?:alignments|subsequences|solutions|paths)\b"),
        "embedding": P(r"\boutputs? (?:an )?embedding\b", r"\bsequence embeddings? (?:are|is) produced\b"),
    },
    "output.completeness": {
        "score_only": P(r"\bscore[- ]only\b", r"\bcomputes? (?:only )?(?:the )?(?:distance|length|score),? not (?:the )?(?:alignment|subsequence)\b"),
        "one_optimum": P(r"\bone (?:optimal )?(?:alignment|solution|subsequence)\b", r"\ban optimal alignment\b"),
        "all_optima": P(r"\ball (?:distinct )?optimal (?:alignments|solutions|subsequences|paths)\b"),
        "top_k": P(r"\btop[- ]k\b"),
        "sampled": P(r"\bsampled (?:alignments|solutions|paths)\b"),
        "bounded": P(r"\bbounded number of (?:alignments|solutions|paths)\b"),
        "capped": P(r"\boutput cap\b", r"\bmaximum of \d+ (?:alignments|hits|solutions)\b"),
        "approximate": P(r"\bapproximate (?:alignment|distance|solution|score)\b"),
    },
    "evaluation.target": {
        "score_correctness": P(r"\bscore (?:correctness|agreement)\b", r"\bcorrect (?:edit distance|alignment score)\b"),
        "witness_validity": P(r"\balignment validity\b", r"\bvalidate(?:d|s)? (?:the )?(?:alignment|subsequence)\b"),
        "enumeration_completeness": P(r"\benumeration completeness\b", r"\ball solutions (?:were|are) recovered\b"),
        "alignment_accuracy": P(r"\balignment accuracy\b", r"\breference alignments?\b"),
        "homology_accuracy": P(r"\bhomology detection (?:accuracy|sensitivity)\b"),
        "mapping_accuracy": P(r"\bmapping accuracy\b", r"\bcorrectly mapped reads?\b"),
        "retrieval_accuracy": P(r"\bretrieval (?:accuracy|performance)\b", r"\bprecision at k\b"),
        "downstream_task": P(r"\bdownstream tasks?\b", r"\bfunctional prediction\b"),
        "runtime": P(r"\brun[- ]?time (?:performance|evaluation|comparison)\b", r"\bexecution time\b"),
        "memory": P(r"\bmemory (?:usage|consumption|footprint)\b", r"\bpeak memory\b"),
        "energy": P(r"\benergy consumption\b", r"\bpower efficiency\b"),
    },
    "evaluation.measure": {
        "exact_agreement": P(r"\bexact agreement\b", r"\bidentical (?:scores|outputs)\b"),
        "precision": P(r"\bprecision(?:@k)?\b"),
        "recall": P(r"\brecall(?:@k)?\b", r"\bsensitivity\b"),
        "f1": P(r"\bf1[- ]score\b", r"\bf[- ]measure\b"),
        "auroc": P(r"\bauroc\b", r"\barea under (?:the )?roc\b"),
        "auprc": P(r"\bauprc\b", r"\barea under (?:the )?precision[- ]recall\b"),
        "sp_score": P(r"\bsp score\b", r"\bsum[- ]of[- ]pairs score\b"),
        "tc_score": P(r"\btc score\b", r"\btotal[- ]column score\b"),
        "rmsd": P(r"\brmsd\b", r"\broot[- ]mean[- ]square deviation\b"),
        "percent_identity": P(r"\bpercent(?:age)? identity\b"),
        "edit_error_rate": P(r"\bedit error rate\b", r"\bbase error rate\b"),
        "wall_time": P(r"\bwall[- ]clock time\b", r"\bwall time\b"),
        "throughput": P(r"\bthroughput\b", r"\bsequences per second\b"),
        "gcups": P(r"\bgcups\b", r"\bbillion cell updates per second\b"),
        "rss": P(r"\bresident set size\b", r"\bpeak rss\b"),
        "vram": P(r"\bvram\b", r"\bgpu memory usage\b"),
        "output_bytes": P(r"\boutput (?:size|bytes)\b"),
        "energy": P(r"\bjoules?\b", r"\benergy consumption\b"),
    },
    "artifact.kind": {
        "paper": P(r"\babstract\b", r"\bintroduction\b"),
        "source_code": P(r"\bsource code (?:is|are) available\b", r"\bgithub\.com/\b", r"\bopen[- ]source (?:software|implementation|code)\b"),
        "binary": P(r"\bprecompiled binar", r"\bexecutable (?:is|are) available\b"),
        "container": P(r"\bdocker (?:image|container)\b", r"\bsingularity container\b"),
        "dataset": P(r"\bdata (?:are|is) available\b", r"\bdataset (?:is|are) available\b"),
        "benchmark_manifest": P(r"\bbenchmark (?:suite|manifest|scripts?) (?:is|are) available\b"),
        "weights": P(r"\bpre[- ]trained weights\b", r"\bmodel weights (?:are|is) available\b"),
        "proof": P(r"\bproof of (?:theorem|correctness|optimality)\b"),
        "erratum": P(r"\berratum\b", r"\bcorrection to\b"),
    },
    "artifact.availability": {
        "local": P(r"\babstract\b", r"\bintroduction\b"),
        "public": P(r"\bpublicly available\b", r"\bfreely available\b", r"\bopen[- ]source\b"),
        "subscription": P(r"\bsubscription access\b"),
        "request_only": P(r"\bavailable upon request\b"),
        "unavailable": P(r"\bnot (?:publicly )?available\b", r"\bcode is unavailable\b"),
    },
}


def validate_rules():
    for dimension, values in RULES.items():
        if dimension not in DIM_BY_KEY:
            raise ValueError(f"Unknown dimension in rules: {dimension}")
        allowed = set(DIM_BY_KEY[dimension]["allowed_values"].split("|"))
        unknown = set(values) - allowed
        if unknown:
            raise ValueError(f"Unknown values for {dimension}: {sorted(unknown)}")


validate_rules()


def extract_pdf(path: Path) -> tuple[str, str | None]:
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True,
            text=True,
            errors="replace",
            timeout=240,
        )
        if result.returncode != 0:
            return result.stdout, compact(result.stderr)[:500]
        return result.stdout, None
    except subprocess.TimeoutExpired:
        return "", "pdftotext timed out after 240 seconds"


def pdf_pages(path: Path) -> int | None:
    result = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, errors="replace")
    match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.M)
    return int(match.group(1)) if match else None


def remove_references(text: str) -> str:
    positions = []
    for match in re.finditer(r"(?im)^\s*(?:\d+[. ]+)?(?:references|bibliography|literature cited)\s*$", text):
        if match.start() > len(text) * 0.35:
            positions.append(match.start())
    return text[: min(positions)] if positions else text


def abstract_from(text: str) -> str:
    lead = text[:50000]
    match = re.search(
        r"(?is)(?:^|\n)\s*abstract\s*[.:]?\s*(.{120,8000}?)(?=\n\s*(?:keywords?|index terms?|\d+\.?\s+introduction|introduction)\b)",
        lead,
    )
    if match:
        return compact(match.group(1))
    return compact(lead[:7000])


def report_catalogue():
    reports = []
    for path in REPORT_DIR.glob("*.md"):
        content = path.read_text(errors="replace")
        title_match = re.search(r"^# (.+)$", content, re.M)
        if not title_match:
            continue
        summary_match = re.search(r"(?s)^## Executive summary\s+(.+?)(?=\n## )", content, re.M)
        reports.append(
            {
                "path": path,
                "title": title_match.group(1).strip(),
                "summary": compact(summary_match.group(1)) if summary_match else "",
            }
        )
    return reports


REPORTS = report_catalogue()


def match_report(title: str):
    if not REPORTS:
        return None
    ranked = sorted(
        ((SequenceMatcher(None, norm(title), norm(item["title"])).ratio(), item) for item in REPORTS),
        reverse=True,
        key=lambda item: item[0],
    )
    score, item = ranked[0]
    return {**item, "score": score} if score >= 0.88 else None


def metadata_log():
    if not RENAME_LOG.exists():
        return {}
    with RENAME_LOG.open(newline="") as handle:
        return {row["new_filename"]: row for row in csv.DictReader(handle)}


META = metadata_log()


def evidence_excerpt(text: str, match: re.Match, limit: int = 310) -> str:
    start = max(0, match.start() - limit // 2)
    end = min(len(text), match.end() + limit // 2)
    excerpt = compact(text[start:end])
    if start:
        excerpt = "…" + excerpt
    if end < len(text):
        excerpt += "…"
    return excerpt


def assess(patterns, title: str, abstract: str, lead: str, body: str):
    areas = [
        ("title", title, 10),
        ("abstract", abstract, 6),
        ("lead", lead, 3),
    ]
    best = None
    score = 0
    for area, text, weight in areas:
        for pattern in patterns:
            match = pattern.search(text)
            if match:
                score += weight
                candidate = (weight, area, evidence_excerpt(text, match), pattern.pattern)
                if best is None or candidate[0] > best[0]:
                    best = candidate
                break
    # Title/abstract/lead evidence already clears the relevance threshold. Body
    # scans are reserved for otherwise undetected facets.
    if score < 4:
        body_count = 0
        for pattern in patterns:
            matches = list(islice(pattern.finditer(body), 5))
            body_count += len(matches)
            if matches and best is None:
                best = (1, "body", evidence_excerpt(body, matches[0]), pattern.pattern)
        score += min(body_count, 5)
    if score < 4 or best is None:
        return None
    basis = "explicit" if best[1] in {"title", "abstract", "lead"} else "inferred"
    confidence = "high" if score >= 9 else "medium" if score >= 6 else "screening"
    return {
        "basis": basis,
        "confidence": confidence,
        "source_area": best[1],
        "evidence": best[2],
        "score": score,
    }


def add_inference(claims, dimension, value, evidence, reason):
    existing = next((c for c in claims if c["dimension"] == dimension), None)
    if existing is not None:
        if value not in existing["values"]:
            existing["values"].append(value)
            existing["values"].sort()
            existing["notes"] = f"{existing['notes']}; {reason}"
        return
    claims.append(
        {
            "group": DIM_BY_KEY[dimension]["group"],
            "dimension": dimension,
            "definition": DIM_BY_KEY[dimension]["definition"],
            "values": [value],
            "basis": "inferred",
            "confidence": "screening",
            "source_area": "cross-facet inference",
            "evidence": evidence,
            "notes": reason,
        }
    )


CURATED_OVERRIDES = {
    "A Linear Space Algorithm for Computing Maximal Common Subsequences - Hirschberg.pdf": {
        "task.role": (["alignment"], "The problem of finding a longest common subsequence of two strings"),
        "task.arity": (["sequence_sequence"], "Given strings A and B, find a string C that is a common subsequence"),
        "entity.domain": (["abstract_symbols"], "Given strings A and B over alphabet Z"),
        "entity.unit": (["character"], "if A(i) = B(j) then L(i,j) receives the diagonal value plus one"),
        "representation.sequence": (["string"], "The problem of finding a longest common subsequence of two strings"),
        "entity_cmp.family": (["equality"], "if A(i) = B(j) then L(i,j) receives the diagonal value plus one"),
        "sequence_cmp.family": (["lcs_length"], "L(i,j) is the maximum length possible of any common subsequence"),
        "objective.problem": (["lcs"], "find a string C that is a common subsequence of A and B and p is maximized"),
        "objective.optimization": (["maximize"], "find a string C that is a common subsequence of A and B and p is maximized"),
        "solver.family": (["dynamic_programming"], "L(i,j) is computed from the diagonal, upper, and left states"),
        "dp.state": (["grid"], "the element L(i,j) corresponds to the maximum common-subsequence length for two prefixes"),
        "dp.algebra": (["max_plus"], "otherwise L(i,j) is the maximum of L(i,j-1) and L(i-1,j)"),
        "dp.layout": (["rolling_rows", "divide_conquer"], "two rows recover prefix scores; the problem is then split recursively"),
        "dp.schedule": (["row_major", "recursive"], "derive each row from the preceding row and recursively solve the two subproblems"),
        "trace.method": (["divide_conquer"], "apply the theorem recursively to divide a problem until a trivial subproblem"),
        "guarantee.kind": (["exact"], "Algorithm C produces a common subsequence of maximum length"),
        "guarantee.evidence": (["proof"], "Proof of Correctness of Algorithm C"),
        "resource.parameter": (["raw_lengths"], "The algorithm requires quadratic time and linear space in the string lengths"),
        "output.kind": (["one_subsequence"], "Algorithm C produces as output a common subsequence C of maximum length"),
        "output.completeness": (["one_optimum"], "Algorithm C produces a common subsequence C of maximum length"),
    },
    "An Improved Algorithm for Matching Biological Sequences - Gotoh.pdf": {
        "task.role": (["alignment", "distance_estimation"], "an improved algorithm for matching biological sequences"),
        "task.arity": (["sequence_sequence"], "Let the two sequences be A and B"),
        "entity.domain": (["protein", "rna"], "aligning biological sequences, including protein and nucleic acid sequences"),
        "entity.unit": (["amino_acid", "base"], "a weight is given to an aligned pair of residues"),
        "entity_cmp.family": (["substitution_table"], "a weight d(ai,bj) is given to an aligned pair of residues"),
        "sequence_cmp.family": (["alignment_score"], "the distance matrix D is generated by induction"),
        "objective.problem": (["weighted_alignment"], "the recurrence chooses the smallest substitution or gap-extension cost"),
        "objective.optimization": (["minimize"], "each induction step chooses the smallest of three numbers"),
        "alignment.boundary": (["global", "local"], "alternative initialization is given for searching for the most locally similar subsequence"),
        "scoring.substitution": (["arbitrary_table"], "a weight d(ai,bj) is given to an aligned pair of residues"),
        "scoring.gap": (["affine"], "the gap weight has the form wk = uk + v"),
        "scoring.operation": (["substitution", "insertion", "deletion"], "the recurrence considers an aligned residue pair and insertion or deletion gaps"),
        "solver.family": (["dynamic_programming"], "the distance matrix D is generated by induction"),
        "dp.state": (["grid"], "the recurrence defines Dm,n together with auxiliary states Pm,n and Qm,n"),
        "dp.algebra": (["min_plus"], "each induction step chooses the smallest of three numbers"),
        "dp.layout": (["rolling_rows"], "two one-dimensional arrays and one variable are sufficient for temporary values"),
        "dp.schedule": (["row_major"], "the induction is completed in MN steps"),
        "trace.method": (["parent_pointers"], "optimal alignments are available by backtracking guided by the direction matrix"),
        "guarantee.kind": (["exact_restricted"], "the improvement applies when the gap weight has the stated affine form"),
        "guarantee.evidence": (["author_claim"], "the induction is completed in MN steps"),
        "resource.parameter": (["raw_lengths"], "M and N are the lengths of the sequences under comparison"),
        "output.kind": (["score", "one_alignment"], "optimal alignments are available by backtracking guided by the direction matrix"),
        "output.completeness": (["one_optimum"], "the traceback follows an optimal path through the direction matrix"),
    },
}


def apply_curated_overrides(filename: str, claims):
    overrides = CURATED_OVERRIDES.get(filename)
    if not overrides:
        return
    existing = {claim["dimension"]: claim for claim in claims}
    for dimension, (values, evidence) in overrides.items():
        claim = {
            "group": DIM_BY_KEY[dimension]["group"],
            "dimension": dimension,
            "definition": DIM_BY_KEY[dimension]["definition"],
            "values": values,
            "basis": "explicit",
            "confidence": "high",
            "source_area": "curated PDF review",
            "evidence": evidence,
            "notes": "Curated correction from the paper's algorithm, recurrence, or complexity analysis.",
        }
        if dimension in existing:
            claims[claims.index(existing[dimension])] = claim
        else:
            claims.append(claim)


def classify(path: Path):
    raw, extraction_error = extract_pdf(path)
    content = compact(raw)
    nonrefs = compact(remove_references(raw))[:600000]
    abstract = abstract_from(raw)
    lead = compact(raw[:30000])
    row = META.get(path.name, {})
    title = row.get("title") or filename_title(path.stem)
    authors = row.get("authors") or filename_authors(path.stem)
    claims = []
    for dimension, values in RULES.items():
        hits = []
        for value, patterns in values.items():
            found = assess(patterns, title, abstract, lead, nonrefs)
            if found:
                hits.append((value, found))
        if not hits:
            continue
        hits.sort(key=lambda item: item[1]["score"], reverse=True)
        # Cap broad dimensions to keep screening output readable. Equal-score ties remain.
        cap = 6 if dimension in {"artifact.kind", "evaluation.measure", "scoring.operation"} else 4
        cutoff = hits[min(cap, len(hits)) - 1][1]["score"] if len(hits) > cap else -1
        selected = [item for i, item in enumerate(hits) if i < cap or item[1]["score"] == cutoff]
        values_out = [item[0] for item in selected]
        primary = selected[0][1]
        notes = "; ".join(
            f"{value}: {result['source_area']} ({result['confidence']})" for value, result in selected
        )
        claims.append(
            {
                "group": DIM_BY_KEY[dimension]["group"],
                "dimension": dimension,
                "definition": DIM_BY_KEY[dimension]["definition"],
                "values": values_out,
                "basis": primary["basis"],
                "confidence": primary["confidence"],
                "source_area": primary["source_area"],
                "evidence": primary["evidence"],
                "notes": notes,
            }
        )

    apply_curated_overrides(path.name, claims)
    by_dim = {c["dimension"]: c for c in claims}
    objectives = set(by_dim.get("objective.problem", {}).get("values", []))
    if "lcs" in objectives:
        evidence = by_dim["objective.problem"]["evidence"]
        add_inference(claims, "task.arity", "sequence_sequence", evidence, "Ordinary LCS is a pairwise sequence objective unless the paper explicitly specifies multiple sequences.")
        add_inference(claims, "entity_cmp.family", "equality", evidence, "The default LCS relation compares symbol equality; verify any paper-specific comparator before implementation.")
        add_inference(claims, "sequence_cmp.family", "lcs_length", evidence, "LCS supplies a sequence-level length/score even when the paper also reconstructs a witness.")
        add_inference(claims, "objective.optimization", "maximize", evidence, "LCS maximizes common-subsequence length.")
    if "lis" in objectives:
        evidence = by_dim["objective.problem"]["evidence"]
        add_inference(claims, "task.arity", "single_sequence", evidence, "LIS is a single-sequence ordered-subsequence problem.")
        add_inference(claims, "entity_cmp.family", "ordering", evidence, "LIS relies on an ordering relation.")
        add_inference(claims, "sequence_cmp.family", "lis_length", evidence, "The objective induces an LIS length when the output is scalar.")
        add_inference(claims, "objective.optimization", "maximize", evidence, "LIS maximizes increasing-subsequence length.")
    if "edit_distance" in objectives:
        evidence = by_dim["objective.problem"]["evidence"]
        add_inference(claims, "task.arity", "sequence_sequence", evidence, "Ordinary edit distance compares two sequences.")
        add_inference(claims, "sequence_cmp.family", "edit_distance", evidence, "The paper's objective is an edit-distance sequence comparator.")
        add_inference(claims, "objective.optimization", "minimize", evidence, "Edit distance minimizes edit cost.")
    if any(c["dimension"] == "alignment.strategy" and "progressive" in c["values"] for c in claims):
        evidence = next(c["evidence"] for c in claims if c["dimension"] == "alignment.strategy")
        add_inference(claims, "heuristic.kind", "progressive", evidence, "Progressive assembly fixes an order of alignment and is classified as a heuristic strategy at pipeline level.")
    # Every local PDF has a paper artifact and local availability, even when extraction is sparse.
    add_inference(claims, "artifact.kind", "paper", path.name, "The classified source is a local PDF research paper.")
    add_inference(claims, "artifact.availability", "local", path.name, "The PDF exists in academic-papers-processed.")

    claims.sort(key=lambda c: (GROUPS.index(c["group"]), list(DIM_BY_KEY).index(c["dimension"])))
    summary = compact(abstract[:700])
    if len(summary) > 720:
        summary = summary[:717].rsplit(" ", 1)[0] + "…"
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    duplicate_id = sha[:16]
    asset = CATALOG_ASSETS.get(sha)
    if asset is None:
        raise ValueError(f"PDF missing from shared catalog: {path.name}")
    warnings = []
    if extraction_error:
        warnings.append(extraction_error)
    if len(content) < 1000:
        warnings.append("Sparse extractable text; classification relies heavily on title and requires manual review.")
    if len(claims) <= 3:
        warnings.append("Few controlled facets were detected; inspect this paper manually before treating absent facets as not applicable.")
    href = "../academic-papers-processed/" + quote(path.name)
    return {
        "id": asset["asset_id"],
        "work_id": asset["work_id"],
        "title": title,
        "authors": authors,
        "filename": path.name,
        "pdf_href": href,
        "pages": pdf_pages(path),
        "bytes": path.stat().st_size,
        "sha256": sha,
        "duplicate_id": duplicate_id,
        "text_characters": len(content),
        "summary": summary,
        "matching_report": asset["report_path"],
        "matching_report_score": 1.0 if (REPORT_DIR / "current" / f"{asset['asset_id']}.md").exists() else None,
        "claims": claims,
        "warnings": warnings,
    }


def write_json(papers, skipped):
    payload = {
        "schema_version": "collection-screening-1.0",
        "generated": __import__("datetime").date.today().isoformat(),
        "source_directory": str(PDF_DIR.relative_to(ROOT)),
        "taxonomy": "docs/Literature Review/Research Tools/classification/dimensions.csv",
        "skipped_files": skipped,
        "method": "Rule-based full-text screening with title/abstract/lead weighting, non-reference repetition checks, and evidence snippets.",
        "papers": papers,
    }
    (OUT / "papers.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return payload


def write_matrix(papers):
    fields = ["paper_id", "title", "authors", "filename", "pages", "sha256", "duplicate_id", "warning_count"] + [row["dimension"] for row in DIMENSIONS]
    with (OUT / "classification-matrix.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for paper in papers:
            row = {
                "paper_id": paper["id"],
                "title": paper["title"],
                "authors": paper["authors"] or "",
                "filename": paper["filename"],
                "pages": paper["pages"] or "",
                "sha256": paper["sha256"],
                "duplicate_id": paper["duplicate_id"],
                "warning_count": len(paper["warnings"]),
            }
            for claim in paper["claims"]:
                row[claim["dimension"]] = "|".join(claim["values"])
            writer.writerow(row)


def write_summary(papers, skipped):
    group_counts = Counter()
    dim_counts = Counter()
    value_counts = Counter()
    dup = defaultdict(list)
    for paper in papers:
        dup[paper["sha256"]].append(paper["filename"])
        for group in {claim["group"] for claim in paper["claims"]}:
            group_counts[group] += 1
        for claim in paper["claims"]:
            dim_counts[claim["dimension"]] += 1
            for value in claim["values"]:
                value_counts[(claim["dimension"], value)] += 1
    duplicate_groups = [items for items in dup.values() if len(items) > 1]
    lines = [
        "# Processed-paper classification summary",
        "",
        "Generated 24 September 2026 from the research-paper PDFs in `literature/academic-papers-processed`.",
        "",
        f"- PDFs classified: **{len(papers)}**",
        f"- Textbooks/protocol handbooks skipped at the user's direction: **{len(skipped)}**",
        f"- Taxonomy fields available: **{len(DIMENSIONS)}** across **{len(GROUPS)}** groups",
        f"- Papers with at least one screening warning: **{sum(bool(p['warnings']) for p in papers)}**",
        f"- Byte-identical duplicate groups: **{len(duplicate_groups)}**",
        "",
        "The counts below mean that an index was detected as relevant to a paper. They do not mean that undetected fields are unsupported or inapplicable.",
        "",
        "## Coverage by index group",
        "",
        "| Index group | Papers with a detected facet |",
        "|---|---:|",
    ]
    for group in GROUPS:
        lines.append(f"| {group} | {group_counts[group]} |")
    lines += ["", "## Most frequent controlled values", "", "| Dimension | Value | Papers |", "|---|---|---:|"]
    for (dimension, value), count in value_counts.most_common(60):
        lines.append(f"| `{dimension}` | `{value}` | {count} |")
    if duplicate_groups:
        lines += ["", "## Byte-identical PDF groups", ""]
        for items in duplicate_groups:
            lines.append("- " + "; ".join(f"`{item}`" for item in items))
    if skipped:
        lines += ["", "## Skipped textbooks and protocol handbooks", ""]
        for item in skipped:
            lines.append(f"- `{item}`")
    lines += [
        "",
        "## Interpretation limits",
        "",
        "This is an evidence-preserving screening index. It uses controlled lexical rules over extractable PDF text, removes reference sections where possible, and requires title/abstract/lead evidence or repeated body evidence. It can still classify a comparison target mentioned in an introduction, miss formulas or image-only text, or merge capabilities from several variants described by one paper. Review the evidence excerpt and source PDF before using a claim in an implementation or benchmark contract.",
        "",
        "A blank matrix cell means **unverified by this screening pass**, not unsupported. Survey papers naturally receive broad classifications. Duplicate PDFs remain separate tabs because the requested unit was every file; identical SHA-256 groups are identified above.",
        "",
    ]
    (OUT / "SUMMARY.md").write_text("\n".join(lines))


def write_html(payload):
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    group_data = json.dumps(GROUPS, ensure_ascii=False)
    dimension_data = json.dumps(DIMENSIONS, ensure_ascii=False)
    template = (OUT / "viewer-template.html").read_text()
    rendered = template.replace("__PAPER_DATA__", data).replace("__GROUP_DATA__", group_data).replace("__DIMENSION_DATA__", dimension_data)
    (OUT / "index.html").write_text(rendered)


def validate_outputs(papers, skipped):
    assert len(papers) + len(skipped) == len(
        [path for path in PDF_DIR.iterdir() if path.is_file() and path.suffix.lower() == ".pdf"]
    )
    assert len({paper["filename"] for paper in papers}) == len(papers)
    allowed = {row["dimension"]: set(row["allowed_values"].split("|")) for row in DIMENSIONS}
    for paper in papers:
        assert (PDF_DIR / paper["filename"]).is_file()
        assert hashlib.sha256((PDF_DIR / paper["filename"]).read_bytes()).hexdigest() == paper["sha256"]
        dimensions = [claim["dimension"] for claim in paper["claims"]]
        assert len(dimensions) == len(set(dimensions)), paper["filename"]
        for claim in paper["claims"]:
            assert set(claim["values"]) <= allowed[claim["dimension"]]
            assert claim["evidence"]
    html_text = (OUT / "index.html").read_text()
    assert "__PAPER_DATA__" not in html_text
    assert "role=\"tabpanel\"" in html_text
    assert all(paper["pdf_href"] in html_text for paper in papers)


def main():
    all_pdfs = sorted(
        (path for path in PDF_DIR.iterdir() if path.is_file() and path.suffix.lower() == ".pdf"),
        key=lambda path: path.name.casefold(),
    )
    skipped = [path.name for path in all_pdfs if path.name in SKIP_FILES]
    pdfs = [path for path in all_pdfs if path.name not in SKIP_FILES]
    unknown_skips = SKIP_FILES - set(skipped)
    if unknown_skips:
        raise FileNotFoundError(f"Configured skipped files not found: {sorted(unknown_skips)}")
    papers = []
    for index, path in enumerate(pdfs, 1):
        print(f"[{index:03d}/{len(pdfs):03d}] {path.name}", flush=True)
        papers.append(classify(path))
    payload = write_json(papers, skipped)
    write_matrix(papers)
    write_summary(papers, skipped)
    write_html(payload)
    validate_outputs(papers, skipped)
    print(f"Validated {len(papers)} paper records, {sum(len(p['claims']) for p in papers)} dimension claims.")


if __name__ == "__main__":
    main()
