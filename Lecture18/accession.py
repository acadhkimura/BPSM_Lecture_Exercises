#use/bin/python
import re
           
accession_list = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

# Contain the number 5
for accession in accession_list:
    if re.search(r"5", accession):
        print("This accession number contains the no. 5:", accession)

# Contain the letter d or e
for accession in accession_list:
    if re.search(r"d|e", accession):
        print("This accession number contains the letter d or e:", accession)

# Contain the letters d and e in that order with a single letter between them
for accession in accession_list:
    if re.search(r"d.e", accession):
        print("This accession number contains the letter d and e in that order with a single letter between them:", accession)

# Contain both the letters d and e in any order
for accession in accession_list:
    if re.search(r"(d.*e|e.*d)", accession):
        print("This accession number contains the letter d and e in any order", accession)
        # .* means followed by 0 or more characters, then "e"

# Start with x or y
for accession in accession_list:
    if re.search(r"^[xy]", accession):
        print("This accession number starts with x or y:", accession)

# Start with x or y and end with e
for accession in accession_list:
    if re.search(r"^[xy]", accession) and re.search(r"e$", accession):
        print("This accession number starts with x or y and end with e*", accession)

# Contains any 3 numbers in any order
for accession in accession_list:
    if len(re.findall(r"\d", accession)) == 3:
        print("This accession number contains any 3 numbers in any order:", accession)

# Contains 3 different numbers in any order
for accession in accession_list:
    digits = re.findall(r"\d", accession)
    if len(set(digits)) == 3:
        print("This accession number contains 3 different numbers in any order", accession)

# Contain three or more numbers in a row
for accession in accession_list:
    if re.search(r"\d{3, }", accession):
        print("This accession number contain three or more numbers in a row:", accession)

# End with d followed by either a, r, or p
for accession in accession_list:
    if re.search(r"d[arp]$", accession):
        print("This accession number ends with d followed by either a, r, or p", accession)
