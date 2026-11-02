#!usr/bin/python3

# Importing Modules
import os
import sys

# Plain genomic sequence:
with open("plain_genomic_seq.txt") as genomic_file:
    genomic_seq = genomic_file.read()

# Exon 1 from 1st to 63rd base
lc_exon_1 = genomic_seq[: 62]
with open("lc_exon_1.txt", "w") as lc_exon_1_file:
    lc_exon_1_write = lc_exon_1_file.write(lc_exon_1)    

# Exon 2 from 91st to end base
lc_exon_2 = genomic_seq[90: ] 
with open("lc_exon_2.txt", "w") as lc_exon_2_file:
    lc_exon_2_write = lc_exon_2_file.write(lc_exon_2)

# NCR from 64th to 90th base
lc_intron = genomic_seq[63:90]
with open("lc_intron.txt", "w") as lc_intron_file:
    lc_intron_write = lc_intron_file.write(lc_intron)


# AJ223353 DNA sequence:
# Coding sequence 29th to 409th
with open("AJ223353.fasta") as AJ223353_file:
    AJ223353_seq = AJ223353_file.read()

AJ_exon = AJ223353_seq[28:409]
with open ("AJ_exon.txt", "w") as AJ_exon_file:
    AJ_exon_write = AJ_exon_file.write(AJ_exon)

AJ_intron_1 = AJ223353_seq[:28]
with open ("AJ_intron_1.txt", "w") as AJ_intron_1_file:
    AJ_intron_1_write = AJ_intron_1_file.write(AJ_intron_1)

AJ_intron_2 = AJ223353_seq[409: ]
with open ("AJ_intron_2.txt", "w") as AJ_intron_2_file:
    AJ_intron_2_write = AJ_intron_2_file.write(AJ_intron_2)







                        

