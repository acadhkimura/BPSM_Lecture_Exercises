#!/bin/bash    

#Show index counter (count the number of times the country has appeared in the datafile in total) and country
cut -f7 example_people_data.tsv | sort | uniq -c | sort -r

# Alt, show line number and the respective country
cut -f7 example_people_data.tsv | nl       


# Show index counter, name, city, and the country, but without the header and blank lines
tail -n +2 example_people_data.tsv | cut -f1,3,7 |
while IFS=$'\t' read -r name city country     
do
        # If the line is empty, skip                                            
        if [ -z "${country}" ];
        then
                continue
        else
                echo -e "${name}\t${city}\t${country}"
        fi           
done | nl


# Put people into separate files: different file for each country  
tail -n +2 example_people_data.tsv | head -n -5 > clean_example_people_data.tsv 
cut -f1,7 clean_example_people_data.tsv |
while IFS=$'\t' read -r name country
do
	# If the country file already exists, append name to existing file, if not. create new file for the country
	echo -e "${name}" >> "${country}.txt"
done


# Work out how many people were born in October and where are they from, outputting the list of people 
# Create a new tsv file with just name, month, and country column
cut -f1,5,7 clean_example_people_data.tsv > october.tsv

# Count the number of people born in october (counter)
october_count=0

# While loop 
while IFS=$'\t' read -r name month country
do 
	if [ "${month}" == "October" ];
	then
		# Lists the person's name and country and increment the counter by 1
		echo -e "${name}\t${country}"
		october_count=$((octotber_count + 1))
	fi
done < october.tsv
echo "Total number of people born in October: $october_count"


# Work out how many people were born in October and where are they from, outputting as multiple lists 
# Keep track of the countries that has already been comes across
declare -A country_list

# Additionally keep track the total number of people born in October within each country
declare -A country_count

# While loop
while IFS=$'\t' read -r name month country
do
	if [ "${month}" == "October" ];
	then
		country_count[$country]=$((country_count[$country] + 1))
		
		# If the country has not appeared yet, add to country list
		if [ -z "${country_list[$country]}" ];
		then
			country_list[$country]="${name}"
		else
			country_list[$country]="${country_list[$country]}, ${name}"
		fi
	fi
done < october.tsv

for country in "${!country_list[@]}"
do
	echo "Country: $country"
	echo "List of people: ${country_list[$country]}"
	echo "Total number of people: ${country_count[$country]}"
done












