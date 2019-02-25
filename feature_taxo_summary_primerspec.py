#feature_taxo_summary.py
from Bio import SeqIO

global_outputfile = "output/summary_features_taxo_primerspec_global.csv"
chordates_outputfile = "output/summary_features_taxo_primerspec_chordates.csv"
cephalo_outputfile = "output/summary_features_taxo_primerspec_cephalo.csv"


###CHORDATES
taxo_summary = {line.split("\t")[0]:line.split("\t")[1] for line in open("metadata/feature_taxonomy_chordates.csv")}
features_fasta =  {seq.id:  str(seq.seq) for seq in SeqIO.parse("metadata/featureschordates.fasta", "fasta")}

#feed in the original frequency table as a dictionary 
summary_features = {}
with open ("metadata/featuresummarychordates.txt") as f:
	for line in f:
		if not line.startswith("Frequency"):
			feature, frequency,numberofsamples = line.split()
			summary_features[feature]=[frequency.replace(",",""),str(numberofsamples)]
  

#add taxonomy and output
output=open(chordates_outputfile,"w")
output.write(",".join(["numberofsequenecesassigned","numberofsamples","taxonomy","sequence_length","sequence","featurecode"])+"\n")
for feature in summary_features.keys():
	summary_features[feature].append(taxo_summary[feature])
	summary_features[feature].append(str(len(features_fasta[feature])))
	summary_features[feature].append(features_fasta[feature])
	output.write(",".join(summary_features[feature]+[feature])+"\n")

output.close()

###CEPHALO
taxo_summary = {line.split("\t")[0]:line.split("\t")[1] for line in open("metadata/feature_taxonomy_cephalo.csv")}
features_fasta =  {seq.id:  str(seq.seq) for seq in SeqIO.parse("metadata/featurescephalo.fasta", "fasta")}

#feed in the original frequency table as a dictionary 
summary_features = {}
with open ("metadata/featuresummarycephalo.txt") as f:
	for line in f:
		if not line.startswith("Frequency"):
			feature, frequency,numberofsamples = line.split()
			summary_features[feature]=[frequency.replace(",",""),str(numberofsamples)]
  

#add taxonomy and output
output=open(cephalo_outputfile,"w")
output.write(",".join(["numberofsequenecesassigned","numberofsamples","taxonomy","sequence_length","sequence","featurecode"])+"\n")
for feature in summary_features.keys():
	summary_features[feature].append(taxo_summary[feature])
	summary_features[feature].append(str(len(features_fasta[feature])))
	summary_features[feature].append(features_fasta[feature])
	output.write(",".join(summary_features[feature]+[feature])+"\n")

output.close()




