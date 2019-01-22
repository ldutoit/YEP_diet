import fasta_tools as ft # fasta tools can be downloaded 
dict_fasta = ft.parse_fasta_to_dict("taxonomy_round2/dna-squences_combined_clipped.fasta",output_format="string")
all_records = {" ".join(x.split()[0:]):x.split()[0] for x in open("taxonomy_round2/allrecordsncbi_accession.txt")}


species_list= [x.strip() for x in open("/home/ludovic.dutoit/repos/scripts/YEP_diet/metadata/44splist97uncrurated.txt")]

for spname in  species_list:
	if  "sp." in spname: spname = spname.split(" ")[0]
	listmatching = [all_records[x] for x in all_records.keys() if spname in x] #fint which record have that taxonomy
	#print(listmatching)
	records = [x for x in dict_fasta.keys() if x in listmatching]  #check that the record is in the database
	if not len(records)>0:
		spname = spname.split(" ")[0]
		listmatching = [all_records[x] for x in all_records.keys() if spname in x] #fint which record have that taxonomy
		#print(listmatching)
		records = [x for x in dict_fasta.keys() if x in listmatching]  #check that the record is in the database
		print "NO", spname,"genus matching:",len(records)>0,len(listmatching)
	else:
		print spname, "OK"
