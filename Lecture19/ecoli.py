#!/usr/bin/python3

import matplotlib.pyplot as plt

# Making charts for ecoli.txt showing AT content in a sliding 1000 base window

window = 1000

ecoli_50000 = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace("\n", "").upper()[0:50000]

at_content_50000 = []
positions_50000 = []

for start in range(len(ecoli_50000) - window + 1):
    win = ecoli_50000[start : start + window]
    at_fraction = (win.count("A") + win.count("T")) / window
    at_content_50000.append(at_fraction)
    positions_50000.append(start)

plt.figure(figsize = (20,10))
plt.plot(positions_50000, at_content_50000, label = "AT content")
plt.xlabel("Position on genome")
plt.ylabel("AT fraction")
plt.legend()
plt.savefig("Ecoli_50000_AT.png", transparent = True)

plt.show()


ecoli_100000 = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace("\n", "").upper()[0:100000]

at_content_100000 = []
positions_100000 = []

for start in range(len(ecoli_100000) - window + 1):
    win = ecoli_100000[start : start + window]
    at_fraction = (win.count("A") + win.count("T")) / window
    at_content_100000.append(at_fraction)
    positions_100000.append(start)

plt.figure(figsize = (20,10))
plt.plot(positions_100000, at_content_100000, label = "AT content")
plt.xlabel("Position on genome")
plt.ylabel("AT fraction")
plt.legend()
plt.savefig("Ecoli_100000_AT.png", transparent = True)

plt.show()


ecoli_whole = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace("\n", "").upper()

at_content_whole = []
positions_whole = []

for start in range(len(ecoli_whole) - window + 1):
    win = ecoli_whole[start : start + window]
    at_fraction = (win.count("A") + win.count("T")) / window
    at_content_whole.append(at_fraction)
    positions_whole.append(start)

plt.figure(figsize = (20,10))
plt.plot(positions_whole, at_content_whole, label = "AT content")
plt.xlabel("Position on genome")
plt.ylabel("AT fraction")
plt.legend()
plt.savefig("Ecoli_whole_AT.png", transparent = True)

plt.show()

