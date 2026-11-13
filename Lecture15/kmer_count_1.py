#!/bin/usr/python3

DNA_seq = str(input("What is your DNa sequence: "))
kmer_val = int(input("What is the kmer size? "))
offset_val = int(input("What is the offset? "))
n = int(input("Min number of times kmer must appear? ")) 

def kmer_count(seq, kmer_val, offset_val, n):

    # List for unique kmers and its respective counts
    uniq_kmer = []
    kmer_count = []

    for i in range(0, len(seq) - kmer_val + 1, offset_val):

        # DNA segment
        kmer = seq[i : i + kmer_val]

        # Check if kmer has appeared before
        if kmer not in uniq_kmer:
            uniq_kmer.append(kmer)
            kmer_count.append(1)

        else:
            i = uniq_kmer.index(kmer)
            kmer_count[i] += 1

    with open("DNA_seq_kmer.txt", "w") as master_file:
        for kmer, count in zip(uniq_kmer, kmer_count):
            if count >= n:
                string = f"{kmer}: number of apperances = {count}\n"
                master_file.write(string)

kmer_count(DNA_seq, kmer_val, offset_val, n)
