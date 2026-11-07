#!/usr/bin/python

dna_list = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT'] 

# seq 1 vs seq 2, 3, 4

seq_1 = dna_list[0]
seq_comp = dna_list[1:4]
i = 0

for seq in seq_comp:
    split_seq_1 = list(seq_1)
    split_seq_comp = list(seq_comp[i])

    for base in split_seq_1:
        idx = split_seq_1.index(base)

        if (split_seq_1[idx] == split_seq_comp[idx]):
            base_num = idx + 1
            seq_num = i + 2
            print(f"Base #{base_num} in seq 1 is the same as base #{base_num} in seq {seq_num}")

    i += 1


# seq 2 vs seq 3, 4
seq_2 = dna_list[1]
seq_comp = dna_list[2:4]
i = 0

for seq in seq_comp:
    split_seq_2 = list(seq_2)
    split_seq_comp = list(seq_comp[i])

    for base in split_seq_2:
        idx = split_seq_2.index(base)

        if (split_seq_2[idx] == split_seq_comp[idx]):
            base_num = idx + 1
            seq_num = i + 3
            print(f"Base #{base_num} in seq 2 is the same as base #{base_num} in seq {seq_num}")

    i += 1

# seq 3 vs seq 4
seq_3 = dna_list[2]
seq_comp = dna_list[3:4]
i = 0

for seq in seq_comp:
    split_seq_3 = list(seq_3)
    split_seq_comp = list(seq_comp[i])

    for base in split_seq_3:
        idx = split_seq_3.index(base)

        if (split_seq_3[idx] == split_seq_comp[idx]):
            base_num = idx + 1
            seq_num = i + 4
            print(f"Base #{base_num} in seq 3 is the same as base #{base_num} in seq {seq_num}")

    i += 1




