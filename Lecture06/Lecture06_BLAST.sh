#!/bin/bash

tail -n +6 blastoutput2.out > clean_blastoutput2.out 

# List the subject accession for all HSPs
cut -f2 clean_blastoutput2.out |
while IFS=$'\t' read -r acc
do
	if [ -z "${acc}" ];
	then
		continue
	else
		echo "${acc}"
	fi
done

# List the alignment length and percent ID for all HSPs
cut -f3,4 clean_blastoutput2.out |
while IFS=$'\t' read -r id align	
do
	if [[ -z "${id}" && -z "${align}" ]]
	then 
		continue
	else
		echo -e "${align}\t${id}"
	fi
done

# How to check if a certain item is a variable
# If a column is an integer:
# if [[ "$coln" =~ ^[0-9]+$ ]]

# Show the HSPs with more than 20 mismatches
while IFS=$'\t' read -r line
do
	IFS=$'\t' read -ra cols <<< "$line"
	col5="${cols[4]}"

	if [[ "$col5" =~ ^[0-9]+$ ]]; then
		if (( col5 > 20 )); then
			echo "$line"
		fi
	fi
done < clean_blastoutput2.out

# Show the HSPs shorter than 100 amino acids and with more than 20 mismatches
while IFS=$'\t' read -r line
do
	if [[ -z "$line" ]]; then
		continue
	fi
	
	# Split current line into array (just include target columns)
	IFS=$'\t' read -ra cols <<< "$line"
	  l4=        3      alignment
	col5="${cols[4]}" # mismatch

	if (( $col4 < 100 && $col5 > 20 ))
	then
		echo "$line"
	fi
done < clean_blastoutput2.out
	
# List the first 20 HSPs that have fewer than 20 mismatches 
line_counter=0

while IFS=$'\t' read -r line
do
        if [[ -z "$line" ]]; then
                continue
        fi

        # Split current line into array (just include target columns)
        IFS=$'\t' read -ra cols <<< "$line"
	col5="${cols[4]}" # mismatch

	if [ "${col5}" -lt 20 ]; then
		echo "$line"
		line_counter=$((line_counter + 1))

		# Print the first 20 lines thus when counter reaches 20, stop loop
		if (( line_counter == 20 )); then
			break
		fi
	fi
done < clean_blastoutput2.out


# How many HSPs are shorter than 100 amino acids? | 3
while IFS=$'\t' read -r line
do
        if [[ -z "$line" ]]; then
                continue
        fi

        # Split current line into array (just include target columns)
        IFS=$'\t' read -ra cols <<< "$line"
        col7="${cols[6]}" # query start
        col8="${cols[7]}" # query end

       	if (( (col8 - col7) < 100))
        then
                echo "$line"
        fi
done < clean_blastoutput2.out | wc -l

# List the top ten highest (best) HSPs
# Sort by E-value, bitscore, % ID
sort -k11,11n -k12,12nr -k3,3nr clean_blastoutput2.out | head -n10

# List the start positions of all matches where the HSP Subject accession includes the letters string "AEI"
cut -f2,7 clean_blastoutput2.out |
while IFS=$'\t' read -r acc start
do
	if [[ "$acc" == *AEI* ]]; then
		echo -e "${start}"
	fi
done

# Alternatively, cut -f2,7 clean_blastoutput2.out | grep "AEI" | cut -f2

# How many subject sequences have more than one HSP
cut -f2 clean_blastoutput2.out | sort | uniq -c | awk "$1 > 1" | wc -l

# What percentage of each HSP is made up of mismatches?
grep -v "#"clean_blastoutput2.out | \
  awk '{
HSP_mm_pc = ($5/$4) * 100 ; 
print HSP_mm_pc;  
       }' |  more

# Allocate HSPs into a small number of different groups based on their scrores 



