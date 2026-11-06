#!/bin/usr/python3

import os

# Make appropriate directories
for i in range(1, 10):
    start = i * 100
    end = start + 99
    dir_name = f"DNA_size_{start}~{end}"
    if os.path.exists(dir_name):
        continue
    else:
        os.mkdir(dir_name)


# Ask for input dna file
dna_file = input("Input the dna file you want to bin by size: ")

# Reading dna sequence and convert to upper case
with open(dna_file, "r") as file:
    dna_seq = file.readlines()

for seq in dna_seq:
    cleaned_dna_seq = seq.upper()
    count = len(cleaned_dna_seq)

    # Caluculate size of sequnce to allocate to appropriate folder
    start = (count // 100) * 100
    end = start + 99

    target_dir = f"DNA_size_{start}~{end}"
    target_file = f"{start}~{end}"

    name = os.path.splitext(os.path.basename(dna_file))[0]
    out_filename = f"{name}_{target_file}.txt"
    out_path = os.path.join(target_dir, out_filename)

    with open(out_path, "a") as indv_file:
        indv_file.write(cleaned_dna_seq + "\n")
