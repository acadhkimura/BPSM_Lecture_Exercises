#!bin/bash


# Get query_key and WebEnv
beast="Cosmoscarta"
db="nucleotide"

efetchstuff=$(wget -qO- "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=Cosmoscarta&usehistory=y" \
  | egrep "QueryKey|WebEnv")
echo ${efetchstuff}

# Use IFS to split the line into fields
IFS="/><"
echo ${efetchstuff}

echo ${efetchstuff} | awk '{print $(NF-5),$(NF-2)}'
QueryKey=$(echo ${efetchstuff} | awk '{print $(NF-5)}')
echo ${QueryKey}

WebEnv=$(echo ${efetchstuff} | awk '{print $(NF-2)}')
echo ${WebEnv}

unset IFS

wget -qO cosmoscarta_sequences.fasta \
 "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=${db}&query_key=${QueryKey}&WebEnv=${WebEnv}&rettype=fasta&retmode=text"

head -3 cosmoscarta_sequences.fasta

grep -c ">" cosmoscarta_sequences.fasta

grep -m3 ">" cosmoscarta_sequences.fasta


