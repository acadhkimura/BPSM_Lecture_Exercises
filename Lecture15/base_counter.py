#!/bin/usr/python3

# Function that will take a DNA sequence along with an optional threhold and return True or False to indicate whether the DNA seq contains high proportion of undetermined bases (i.e. not A, T, G, or C)

def base_counter(seq, threshold = 50):

    length = len(seq)
    base_list = ["A", "T", "G", "C"]
    total_count = 0

    for base in base_list:
        count = seq.upper().count(base)
        total_count += count

    not_base = length - total_count
    perc = (not_base / length) * 100

    if perc > threshold:
        return True
    else:
        return False

# Assertion testing
assert base_counter("ATCGCGCGATATGCGCATA", 50) == False
assert base_counter("AJDJDSFNVSKSDKJFE", 80) == True
