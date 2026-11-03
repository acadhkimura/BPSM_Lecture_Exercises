# Calculating the A and T content

# DNA sequence:
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# Count the number of A nucleotides
a_count = dna_seq.count("A")
print("Total number of A nucleotides in the DNA sequence:", a_count)

# Count the number of T nucleotides
t_count = dna_seq.count("T")
print("Total number of T nucleotides in the DNA sequence:", t_count)

# Add count together and divide by the length of sequence
at_count = a_count + t_count
dna_seq_len = len(dna_seq)
at_proportion = at_count / dna_seq_len
print("Proportion of A and T content in DNA sequence:", at_proportion)


# ------------------
# Complementing DNA
# Compliment of DNA seq
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

comp_dna_seq = (
        dna_seq
        .replace("A", "t")
        .replace("T", "A")
        .replace("t", "T")
        .replace("C", "g")
        .replace("G", "C")
        .replace("g", "G")
)
print("The complement DNA sequence is:", comp_dna_seq)


# ------------------
# Restriction fragment lengths
# ExoRI restriction enzyme with cut motif at "G*AATTC"
# Recognition site
dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"

motif_index = dna_seq.find(motif)

seq_1 = dna_seq[: (motif_index + 1)]
seq_2 = dna_seq[(motif_index + 1) : ]

print("The size of the 1st fragment is:", len(seq_1), "and the length of 2nd fragment is:", len(seq_2))


# ------------------
# Splicing out introns

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = dna_seq[: 62]
exon_2 = dna_seq[90: ]

print("The coding sequence of the genomic DNA is:", exon_1 + exon_2)

coding_seq = exon_1 + exon_2
print("The percentage of DNA sequence being the coding region is:", (len(coding_seq) / len(dna_seq)) * 100)

intron = dna_seq[62 : 91]
print(exon_1.upper()+intron.lower()+exon_1.upper())
