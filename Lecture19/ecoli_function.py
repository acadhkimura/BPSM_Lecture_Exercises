#!/usr/bin/python3

import matplotlib.pyplot as plt

ecoli_seq_path = "/localdisk/data/BPSM/Lecture19/ecoli.txt"

def default_seq(path = ecoli_seq_path):
    with open(path, "r") as file:
        return file.read().replace("\n", "").upper()

def base_content(seq = None, window = 1000, content_type = "AT", start = 0, end = 50000, output = None):
    if seq is None:
        seq = default_seq()

    content = content_type.upper()
    if mode not in ("AT", "GC"):
        raise ValueError("Content type must be either "AT" or "GC"")

    region = seq[start : end]
    if len(region < window:
           raise ValueError("Selected sequence region is shorter than window size")

    bases = ("A", "T") if content == "AT" else ("G", "C")
    fractions = []
    positions = []

    for offset in range(len(region) - window + 1):
        win = region(offset : offset + window]
        count = win.count(bases[0] + win.count(bases[1])
        fractions.append(count / window)
        positions.append(start + offset)

    end_label = end if end is not None else len(seq)
    if output is None:
        output = f"ecoli_{content}_{start}_{end_label}_w{window}.png"

    plt.figure(figsize=(20, 10))
    plt.plot(
        positions,
        fractions,
        linewidth=0.8 if len(positions) > 100000 else 1.5,
        label=f"{mode} content ({window} bp window)",
    )
    plt.title(f"{mode} Content Across E. coli ({start:,} to {end_label:,} bp)")
    plt.xlabel("Genome position (bp)")
    plt.ylabel(f"{mode} fraction")
    plt.legend()

    plt.savefig(output, transparent=True)
    plt.show()

    
