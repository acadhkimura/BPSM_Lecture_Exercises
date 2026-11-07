#!/bin/use/python3

# Reading genomic sequence of remote file
with open("AJ223353.fasta", "r") as remote_dna_file:
    remote_dna = remote_dna_file.read()

    # Setting parameters
    kmer_val = int(input("What is the kmer size? "))
    offset_val = int(input("What is the offset? "))
    n = int(input("Min number of times kmer must appear? "))

    # List for unique kmers and its respective counts
    uniq_kmer = []
    kmer_count = []


    for i in range(0, len(remote_dna) - kmer_val + 1, offset_val):

        # DNA segment
        kmer = remote_dna[i : i + kmer_val]

        # Check if kmer has appeared before
        if kmer not in uniq_kmer:
            uniq_kmer.append(kmer)
            kmer_count.append(1)

        else:
            i = uniq_kmer.index(kmer)
            kmer_count[i] += 1

    with open("AJ223353_master.txt", "w") as master_file:
        for kmer, count in zip(uniq_kmer, kmer_count):
            if count >= n:
                string = f"{kmer}: number of apperances = {count}\n"
                master_file.write(string)

