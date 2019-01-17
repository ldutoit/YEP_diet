#feature_taxo_summary.py

from Bio import SeqIO

outputfile = "output/summary_features_taxo.csv"

taxo_summary = {line.split()[0]:line.split()[1] for line in open("metadata/feature_taxonomy.csv")}
features_fasta =  {seq.id:  str(seq.seq) for seq in SeqIO.parse("metadata/features.fasta", "fasta")}

#feed in the original frequency table as a dictionary 
summary_features = {}
with open ("metadata/featuresummary.txt") as f:
	for line in f:
		if not line.startswith("Frequency"):
			feature, frequency,numberofsamples = line.split()
			summary_features[feature]=[frequency.replace(",",""),str(numberofsamples)]
  

#add taxonomy and output
output=open(outputfile,"w")
output.write("\t".join(["numberofsequenecesassigned","numberofsamples","sequence_length","sequence","featurecode"])+"\n")
for feature in summary_features.keys():
	summary_features[feature].append(taxo_summary[feature])
	summary_features[feature].append(str(len(features_fasta[feature])))
	summary_features[feature].append(features_fasta[feature])
	output.write(",".join(summary_features[feature]+[feature])+"\n")

output.close()
