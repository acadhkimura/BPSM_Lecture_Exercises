#!/use/bin/python3

# Reading genomic sequence of remote file
with open("AJ223353.fasta", "r") as remote_dna_file:
    remote_dna = remote_dna_file.read()

    # Setting parameters
    window = 30
    offset = 3
    index = 1

    with open("AJ223353_master.fasta", "w") as master_file:
        for i in range(0, len(remote_dna) - window + 1, offset):

            # DNA segment
            dna_window = remote_dna[i : i + window]

            # Calculating GC content
            gc_count = dna_window.count("G") + dna_window.count("C")
            gc_perc = (gc_count / window)  * 100

            print("DNA segment:", dna_window)
            print("GC content:", gc_perc)

            # Writing for fasta file

            header = f">AJ22353_segment_{index}\n"
            seq = f"{dna_window}\n"
            filename = f"AJ223353_{index}.fasta"

            with open(filename, "w") as indv_file:
                indv_file.write(header + seq)

            master_file.write(header + seq)

            index += 1

