#!/usr/bin/python3

# Part 1
# Function that takes 2 arg (protein seq and aa residue code) and returns perc that the aa makes up

def aa_perc(protein_seq, aa_residue_code):
    
    length = len(protein_seq)
    count = protein_seq.upper().count(aa_residue_code.upper())

    perc = (count / length) * 100

    return perc

# Assertion testing
assert round(aa_perc("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(aa_perc("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(aa_perc("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(aa_perc("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)


# Part 2
# Modify function so accepts a list of amino acid residues and count these within prot seq
# If no list is given, the function should return the percentage of hydrophobic amino acid residues

hydrophobic_aa = ["A", "I", "L", "M", "F", "W", "Y", "V"]

def aa_perc_2(protein_seq, aa_list = hydrophobic_aa):

    length = len(protein_seq)
    total_count = 0

    for aa in aa_list:
        count = protein_seq.upper().count(aa)                                                                     
        total_count += count

    perc = (total_count / length) * 100

    return perc

# Assertion testing
assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP")) == 65
