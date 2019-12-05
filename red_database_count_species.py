##This short code is just to show how broad our database is


dict_taxo={taxa.split()[0]:" ".join(taxa.split()[1:]) for taxa in open("allrecordsncbi_accession.txt")}

act_species = []
with open("ref-seqschorwithextra2.fa") as f:
	for line in f:
		if line.startswith(">"):
			code = line.strip().split(" ")[0][1:]
			if "Actinopteri" in dict_taxo[code]  and " "  in dict_taxo[code] and not "sp." in dict_taxo[code] and not "homeseqclus" in dict_taxo[code]:
				act_species.append(" ".join(dict_taxo[code].split(" ")[:3]))

print (len(set(act_species))) 
#9835 species 
##We need to the two species of opalfish that were avoided nbecause they were many different clusters exluded at line 1 and not "homeseqclus" in dict_taxo[code]

This after checking because we got 3 more genuses and 2 more 

act_genuses = [x.split(";")[-2] for x in act_species]
print (len(set(act_genuses))) 
#3190 	#3191 with opalfish



cephalo_species = []
with open("refseqceph/dna-sequences.fasta") as f:
	for line in f:
		if line.startswith(">"):
			code = line.strip().split(" ")[0][1:]
			if "Cephalopod" in dict_taxo[code]  and " "  in dict_taxo[code] and not "sp." in dict_taxo[code]:
				cephalo_species.append(" ".join(dict_taxo[code].split(" ")[:3]))

print (len(set(cephalo_species)))  # 385 species

cephalo_genuses = [x.split(";")[-2] for x in cephalo_species]
print (len(set(cephalo_genuses))) # 145


###ADDING GENERA ONLY
cephalo_genera = []
with open("refseqceph/dna-sequences.fasta") as f:
	for line in f:
		if line.startswith(">"):
			code = line.strip().split(" ")[0][1:]
			if "Cephalopod" in dict_taxo[code]  and not in dict_taxo[code] and dict_taxo[code].count(";")>=5: # Only genera nop species
				cephalo_genera.append(" ".join(dict_taxo[code].split(";")[-1]))


