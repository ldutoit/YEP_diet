import fasta_tools as ft # fasta tools can be downloaded 
dict_fastachor = ft.parse_fasta_to_dict("taxo_primerspec/ref-seqschorwithextra.fa",output_format="string")
dict_fastaceph = ft.parse_fasta_to_dict("taxo_primerspec/ref-seqscephwithmel.fa",output_format="string")
dict_fasta = dict_fastachor.update(dict_fastaceph)
species_list= [x.strip() for x in open("/home/ludovic.dutoit/repos/scripts/YEP_diet/metadata/specieslistcurated.txt")]
all_records = {" ".join(x.split()[0:]):x.split()[0] for x in open("taxonomy_round2/allrecordsncbi_accession.txt")}

#fishes first
for spname in  species_list:
	spname=spname.split("(")[1].split(")")[0]
	if  "sp." in spname: spname = spname.split(" ")[0]
	print spname
	listmatching = [all_records[x] for x in all_records.keys() if spname in x] #fint which record have that taxonomy
	#print(listmatching)
	records = [x for x in dict_fastachor.keys() if x in listmatching]  #check that the record is in the database
	if not len(records)>0:
		spname = spname.split(" ")[0]
		listmatching = [all_records[x] for x in all_records.keys() if spname in x] #fint which record have that taxonomy
		#print(listmatching)
		records = [x for x in dict_fastachor.keys() if x in listmatching]  #check that the record is in the database
		print "NO", spname,"genus matching:",len(records)>0,len(listmatching)
	else:
		print spname, "OK"

#cephalopods next so I dont validate a fish that is clipped in the cephalo but tnot the chordates database
	spname=spname.split("(")[1].split(")")[0]
	if  "sp." in spname: spname = spname.split(" ")[0]
	print spname
	listmatching = [all_records[x] for x in all_records.keys() if spname in x] #fint which record have that taxonomy
	#print(listmatching)
	records = [x for x in dict_fastaceph.keys() if x in listmatching]  #check that the record is in the database
	if not len(records)>0:
		spname = spname.split(" ")[0]
		listmatching = [all_records[x] for x in all_records.keys() if spname in x] #fint which record have that taxonomy
		#print(listmatching)
		records = [x for x in dict_fastaceph.keys() if x in listmatching]  #check that the record is in the database
		print "NO", spname,"genus matching:",len(records)>0,len(listmatching)
	else:
		print spname, "OK"

#cephalopods first

for spname in  species_list:
	print spname