#!usr/bin/python

# Getting the exon positions from the exons.txt

with open("genomic_dna2.txt", "r") as genomic_file:
    genomic_dna2 = genomic_file.read()
    
with open("full_exon_file.txt", "w") as full_exon_file:
    with open("exons.txt", "r") as exon_file:
        for line in exon_file:
            exon_pos = line.split(",")
            full_exon_file.write(genomic_dna2[(int(exon_pos[0])-1) : (int(exon_pos[1]))])





