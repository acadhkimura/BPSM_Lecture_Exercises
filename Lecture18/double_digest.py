#/bin/usr/python3

import re
# Fragment length when restriction enzyme recognition site is ANT*AAT
with open("long_dna.txt") as file:
    dna_seq = file.read()

bpsmi_cuts  = [m.start() + 3 for m in re.finditer(r"A[ACGT]TAAT", dna_seq)]
bpsmii_cuts = [m.start() + 4 for m in re.finditer(r"GC[AG][AT]TG", dna_seq)]

all_cuts = sorted(set(bpsmi_cuts + bpsmii_cuts))

boundaries = [0] + all_cuts + [len(dna_seq)]
fragments = [dna_seq[boundaries[i] : boundaries[i + 1]] for i in range(len(boundaries) - 1)]

for i, fragment in enumerate(fragments, start = 1):
    print(f"Fragment {i} (length{len(fragment)}): {fragment}")

