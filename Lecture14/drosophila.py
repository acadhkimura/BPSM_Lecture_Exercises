#!/bin/usr/python3

# Opening and reading drosophila.csv file
with open("data.csv", "r") as drosophila_file:
    drosophila_data = drosophila_file.readlines()

    for data in drosophila_data:
        indv_data = list(data.split(","))
        name, seq, gene, expression = indv_data


        cleaned_gene = seq.upper()

        # AT content
        at_count = cleaned_gene.count("A") + cleaned_gene.count("T")
        at_cont = at_count / len(cleaned_gene) 
        if at_cont > 0.65:
            st = "high"
        elif at_cont > 0.45:
            st = "medium"
        else:
            st = "low"

        if (name == "Drosophila melanogaster" or name == "Drosophila simulans"):
            print(f"{name} genes: {gene}")
        elif (len(seq) > 90 and len(seq) < 110):
            print(f"Genes between 90 and 110 bases long: {gene}")
        elif (int(at_cont) > 0.5 and int(expression) > 200):
            print(f"AT content less than 0.5 and expression level over 200: {gene}")
        elif (name != "Drosophila melanogaster" and (gene.startswith("k") or gene.startswith("h"))):
            print(f"Genes starting with k or h except for Drosophila melanogaster: {gene}")

        print(f"{gene}: AT content: {st}")


            


    


