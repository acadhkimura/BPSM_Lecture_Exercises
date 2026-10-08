#!/bin/bash    

#Show index counter (count the number of times the country  has appeared in the datafile in total) and country
cut -f7 example_people_data.tsv | sort | uniq -c | sort -r

# Alt, show line number and the respective country
cut -f7 example_people_data.tsv | nl       


# Show index counter, name, city, and the country, but without the header and blank lines
tail -n +2 example_people_data.tsv | cut -f1,3,7 |
while IFS=$'\t' read -r name city country     
do
        # The line country="${country}" was redundant, so it can be removed
        if [ -z "${country}" ]
        then
                continue
        else
                echo -e "${name}\t${city}\t${country}"
        fi           
done | nl
