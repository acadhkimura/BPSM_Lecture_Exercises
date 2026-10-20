rm singleline_NCBIseqs.fasta
count=0
while read lin
do
	[ -z "${line}# ] && continue
	if test ${line:0:1} == ">"
	then
		count=$(( ${count}+1 }}
		if test ${count} == 1
		then
			printf ${line}"\n"	
		else
			printf "\n"${line}
		fi
	else
		printf ${line} >> singleline_NCBIseqs.fasta
	fi
done < mock_NCBI.fasta

