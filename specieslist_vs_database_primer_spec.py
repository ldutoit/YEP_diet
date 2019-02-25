import fasta_tools as ft # fasta tools can be downloaded 
dict_fastachor = ft.parse_fasta_to_dict("taxo_primerspec/ref-seqschorwithmel.fa",output_format="string")
dict_fastaceph = ft.parse_fasta_to_dict("taxo_primerspec/ref-seqscephwithmel.fa",output_format="string")
dict_fasta = dict_fastachor.join(dict_fastaceph)
species_list= [x.strip() for x in open("/home/ludovic.dutoit/repos/scripts/YEP_diet/metadata/44splist97uncrurated.txt")]


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


for spname in  species_list:
	print spname