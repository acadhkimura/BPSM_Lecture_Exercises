#!/bin/bash    

#Show indexi counter (count the number of times the country  has appeared in the datafile in total) and country
cut -f7 example_people_data.tsv \t | sort | uniq -c | sort -r



