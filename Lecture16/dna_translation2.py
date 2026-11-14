#!/use/bin/python3

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


def dnaseq_to_protein(seq, frmae = 0):
    protein = []
    seq = seq.upper()

    for i in range(frame, len(seq) - 2, 3):
        kmer = seq[i : i + 3]
        prot = gencode.get(kmer, "X")
        protein.append(prot)

    return ''.join(protein)

def forward_translation(seq):
    translation_set = []

    for i in range(3):
        translation_set[f"Frame +{f+1}"] = dnaseq_to_protein(seq, frmae = f)
    return translation_set

def reverse_complement(seq):
    complement = {"A" :  "T", "T" : "A", "C" : "G", "G" : "C", "N"  :  "N"}
    rev_seq = reversed(seq_upper())
    return ''.join(complement.get(base, "N") for base in rev_seq)

def reverse_translation(seq):
    rev_str = reverse_complement(seq)
    translation_set = {}
    for i in range(3):
        translation_set[f"Frame -{f+1}"] = dnaseq_to_protein(rev_str, frame = f)
    return translation_set

