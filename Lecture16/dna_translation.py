#!/bin/usr/python3
# Codon usage table for translation                                                                                    
gencode = {                                                                                                            
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',                                                                            
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',                                                                            
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',                                                                            
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                                                                            
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',                                                                            
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',                                                                            
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',                                                                            
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',                                                                            
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',                                                                            
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',                                                                            
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',                                                                            
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',                                                                            
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',                                                                            
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',                                                                            
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',                                                                            
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
           }

# Write a python programme that will take any DNA sequence and translate it into protein using the translation table

def dnaseq_to_protein(seq):
    protein = []
    dna_seq = list(seq.upper())

    for i in range(0, len(seq) - 3 + 1, 1):
        kmer = dna_seq[i : i + 3]

        if kmer in gencode.keys():
            prot = gencode.get(kmer)
            protein.append(prot)

    prot_seq = ''.join(protein)

    return prot_seq

dna_seq = input("Enter DNA sequenece to translate to its corresponding proteins: ")
dnaseq_to_protein(dna_seq)

# What happens if the DNA sequence contains undetermined bases (e.g. N)?

# Can you generate a translation in all three "forward" frames (transcription is on the top strand, starting at base 1, 2, and 3)?

def forward_translation(seq):
    dna_seq = list(seq.upper())
    strand_1 = dna_seq[0:9]
    strand_2 = dna_seq[1:10]
    strand_3 = dna_seq[2:11]

    translation_set = {}

    strands = [strand_1, strand_2, strand_3]
    indv_translation = []
    indv_protein = []
    final_protein = []

    for strand in strands:
        for i in range(0, 3, 1):
            kmer = dna_seq[i : i + 3]

            if kmer in gencode.keys():
                prot = gencode.get(kmer)
                indv_protein.append(prot)
                prot_seq = ''.join(protein)
                final_protein.append(prot_seq)
                indv_protein.clear()


        translation_set(strand) = final_protein[i]
        final_protein.clear()

# Can you generate a translation in all three "reverse" frames (transcription is on the bottom strand, starting at base end, end-1, and end-2)?

def reverse_translation(seq):
    dna_seq = list(seq.upper())
    strand_1 = dna_seq[0:9]
    strand_2 = dna_seq[1:10]
    strand_3 = dna_seq[2:11]

    translation_set = {}

    strands = [strand_1, strand_2, strand_3]
    reverse_strand = []
    reverse_strands = []
    indv_translation = []
    indv_protein = []
    final_protein = []

    for strand in strands:
        indv_base = list(strand)
        for base in indv_base:

            if base == "A":
                reverse_strand.append("T")
            elif base = "T":
                reverse_strand.append("A")
            elif base == "C":
                reverse_strand.append("G")
            elif base == "G":
                reverse_strand.append("C")

        reverse_str = ''.join(reverse_strand)
        reverse_strands.append(reverse_str)

        for rev_str in reverse_strands:
            forward_translation(rev_str)
