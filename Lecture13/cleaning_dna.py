#!usr/bin/python
  
# DNA sequences in input.txt
with open("input.txt", "r") as dna_file:
    dna_seq = dna_file.readlines()

    line_counter = 1

    # Reading each line of the file and removing the adapter sequence (first 14 base pairs) + saving them to new file
    for line in dna_seq:
        with open("dna_file_{counter}.txt".format(counter = line_counter), "w" ) as single_dna_file:
            single_dna_file.write(line[14: ])
            print("Length of DNA sequence {counter}:".format(counter = line_counter), len(line[14: ]))
            line_counter += 1

