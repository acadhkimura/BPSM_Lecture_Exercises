# Downloading the latest eukaryotes.txt
import subprocess
subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell = True)

import pandas as pd 
df = pd.read_csv('eukaryotes.txt', sep = "\t", na_values = ['-'])

# How many fungal species have genomes bigger than 100Mb? What are their names?

fungi_100_df = df[
        (df['Size (Mb)'] > 100) & 
        (df['Group'] == 'Fungi')
]

print(f"Number of fungal species > 100 Mb: {len(fungi_100_df}")

print("\nNames:")
print(fungi_100_df['#Organism/Name'].tolist())

# 218 rows 


# How many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
kingdom_counts = df['Group'].value_counts()

# Fungi 16876
# Animals 14495
# Plants 4390
# Protists 1987
# Other 202


# Which Heliconius species genomes have been sequenced?
heliconius_df = df[df.iloc[;, 0].str.contains('Heliconius', case = False, na = False)]
print(heliconius_df.iloc[:, 0].unique())
# Length: 70


# Which sequencing centre has sequenced the most plant genomes? the most insect genomes?
plants_df = df[df['Group'] == 'Plants']
top_plants_df = plants_df['Center'].value_counts().head(1)
# USDA-ARS (314)

insects_df = df[)df['Group'] == 'animals') & (df['SubGroup'] == 'Insects')]
top_insects_df = insects_df['Center'].value_counts().head(1)
# WELCOME SANGER INSTITUTE (1637)


# Add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes? 
df['Proteins_per_Gene'] = df['Proteins'] / df['Genes']
# Prevent errors (remove na values)
valid_df = df.dropna(subset=['Genes', 'Proteins'])

protein_10_genomes = valid_df[valid_df['Proteins_per_Gene'] > 1.10]

print(f"Number of genomes with >10% more proteins than genes: {len(protein_10_genomes)}")
results_preview = protein_10_genomes[['Organism/Name', 'Group', 'Genes', 'Proteins', 'Proteins_per_Gene']]
print("\nPreview of matching genomes:")
print(results_preview.head(10))

# First 3
# Arabidopsis thaliana, Glycine max, Solanum lycopersicum
