#bin/usr/python

import re

# re.serach("x", "y")
# x: pattern to look for
# y: the input str / arguement
# Returns Ture or None

# raw string: use if you eed ti ignore special characters when doing a search and also tell python interpreter to interpret backslashes as literal slashes

# Example

my_raw_string = r"Hello\nworld\t!"
print(my_raw_string)
# Would return Hello\nworld\t

# Can also search different possiblites i.e search for A or T at a particular base position
dna = "ATCGCGACGCA"
if re.search(r"G(A|T)CG", dna):
    print("Restriction site G-AorT-CG found.")
else:
    print("Resctriction site G-AorT-CG not found.")

# Looking for any GC-then any base-GC
if re.search(r"GC(A|T|G|C)GC", dna):
    print("Found what we were looking for...")

# Same thing but using []
if re.search(r"GC[GATC]GC", dna):
    print("Found what we were looking for...")

# Describing character group by listing the characters that are not allowed, e.g. amibguous bases in DNA sequences
# When using re, if the character group starts with ^ then it means any character except the ones in the "Negated character group"

# Searching to see if there are bases that are not G or A or T or C
if re.search(r"[^GATC]", dna):
    print("Ambiguous base found")
else:
    print("Sequence has no ambiguous bases in it")

# Non-special characters
# \ Escape special character or start a sequence
# . MAtch any character except newline
# ^ Match start of the string
# $ Match end of the string
# [] Enclose a set of matchable characters
# () Crate capture group, & indicate precedence

# If using []. after a "[", to enclose a set, the onyl special characters are:
# ] End the set, if not teh 1st char
# - A range, e.g. a-c matches a or b or c
# ^ If it is the 1st character, negate the entire set (i.e. "none of these")

# {m} Exactly m repetitions
# {m, n} From m (default 0) to n (default inifinity) repetitions
# * 0 or more, same as {, }
# + 1 or more, same as {1, }
# ? 0 or 1, same as {, 1}

# Looking for "T something A"
re.search(r"T.A", dna)

# ?: the thing preceding ? is optional
# Number of times something (a base) is repeated
# In the pattern GCA?Y the A is optional
# The pattern will match GCAY and GCY

# +: the thing preceding + can be repeated more than once
# GFA+Y, the A can be repeated
# GCAY, GCAAY. GCAAAY etc, but can not be GCY

# *: most felxible quantifier, the thing preceding it is optional, but can also be repeated
# GCA*Y will match GCY, GCAY. GCAAY. GCAAAY etc

# Can also specify the number of repetions (min, max)
# GCA{2, 4}Y allows 2 to 4 As, so will match GCAAY, GCAAAY, and GCAAAAY but not GCY, GCAY

# ^: Specifiy starting with position, different to when it is at the beginning of a square bracket (enclose set) e.g. not the same as [^GATC]
# $ means at the end, so c$ will match GATC, but not GACTA
# Starts with A
re.search(r"^A", "ATGC")
# Ends with A
re.search(r"A$", "GTCA")
# Starts with A or G
re.search(r"^[AG]", "ATGT")
# Starts with A or G and ends with C
re.search(r"^[AG]", "GATAC") and re.search(r"c$", "GATAC")

# Re match object
# Calling group() on math object will tell us which portion of our input string matched the pattern

# Extracting multiple groups
lots_of_animals = [
  'Homo sapiens',
  'Mus musculus',
  'Erinaceus europaeus',
  'Columba livia',
  'Sciurus vulgaris',
  'Gorilla'
    ]

for this_animal in lots_of_animals :
   new_match_obj = re.search('(.+) (.+)',this_animal)
   print(this_animal+': genus is ' + new_match_obj.group(1)+', species is ' + new_match_obj.group(2))
  
# Can get positions of the match with object.start() or object.end()

# Splitting a string with regex
re.split(r'Y', dna)
# Would split dna sequence in places that contains Y (the Y would not appear in the splitted strings)

# Multiple finds
# re.findall() to find multiple instances of found characters

# Finding and processing multiple matches
# re.finditer()
# What are the start and stop positions of all stretches of A or T at least 4 bases long?
AorT_runs = re.finditer(r'[AT]{4,}', dna)

# Lookahead assertions
# Allowing overlaps
stringlength=3
AorT_runs_v3 = re.finditer(r'(?=[AT]{3,3})', dna)
counter=0
for ATs in AorT_runs_v3:
    counter += 1
    run_start = ATs.start()
    run_end = run_start+stringlength
    print('A/T triplet (overlapping): ' +str(counter)+' extends from base ' \
    + str(run_start+1) \
    + ' to base ' +str(run_end)+' and has sequence ' +str(dna[run_start:run_end]))

print('The input sequence was ' + dna)
































