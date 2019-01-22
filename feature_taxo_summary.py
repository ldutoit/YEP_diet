#feature_taxo_summary.py

from Bio import SeqIO

outputfile = "output/summary_features_taxo.csv"

taxo_summary = {line.split("\t")[0]:line.split("\t")[1] for line in open("metadata/feature_taxonomy.csv")}
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
output.write(",".join(["numberofsequenecesassigned","numberofsamples","sequence_length","sequence","featurecode"])+"\n")
for feature in summary_features.keys():
	summary_features[feature].append(taxo_summary[feature])
	summary_features[feature].append(str(len(features_fasta[feature])))
	summary_features[feature].append(features_fasta[feature])
	output.write(",".join(summary_features[feature]+[feature])+"\n")

output.close()


#print list of genus and species

famgenandspe = set([taxon for taxon in taxo_summary.values() if taxon.count(";")>2])
for t in famgenandspe:
	print t


Arthropoda;Insecta;Thysanoptera;Thripidae;Scolothrips;Scolothrips takahashii
Chordata;Actinopteri;Myctophiformes;Myctophidae;Protomyctophum;Protomyctophum arcticum
Chordata;Actinopteri;Lampriformes;Trachipteridae;Trachipterus;Trachipterus arcticus
Chordata;Actinopteri;Perciformes;Sebastidae;Sebastes
Chordata;Actinopteri;Uranoscopiformes;Pinguipedidae;Parapercis;Parapercis allporti
Annelida;Clitellata;Haplotaxida;Enchytraeidae;Enchytraeus;Enchytraeus christenseni
Arthropoda;Insecta;Coleoptera;Scarabaeidae;Bohepilissus;Bohepilissus subtilis
Chordata;Actinopteri;Clupeiformes;Engraulidae;Engraulis;Engraulis environmental sample
Chordata;Actinopteri;Labriformes;Labridae;Pseudolabrus;Pseudolabrus miles
Chordata;Actinopteri;Labriformes;Labridae;Notolabrus;Notolabrus fucicola
Chordata;Actinopteri;Scombriformes;Scombridae;Allothunnus;Allothunnus fallai
Chordata;Actinopteri;Centrarchiformes;Cheilodactylidae;Cheilodactylus
Chordata;Actinopteri;Scombriformes;Gempylidae;Thyrsites;Thyrsites atun
Chordata;Actinopteri;Argentiniformes;Microstomatidae;Microstoma;Microstoma microstoma
Chordata;Aves;Passeriformes;Zosteropidae;Zosterops;Zosterops japonicus
Chordata;Actinopteri;Argentiniformes;Bathylagidae;Lipolagus;Lipolagus ochotensis
Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Hippocampus
Chordata;Mammalia;Rodentia;Muridae
Chordata;Amphibia;Anura;Pipidae;Xenopus;Xenopus laevis
Chordata;Mammalia;Diprotodontia;Phalangeridae;Trichosurus;Trichosurus vulpecula
Chordata;Actinopteri;Uranoscopiformes;Uranoscopidae;Kathetostoma;Kathetostoma canaster
Chordata;Actinopteri;Myctophiformes;Myctophidae
Chordata;Actinopteri;Gadiformes;Moridae;Pseudophycis;Pseudophycis barbata
Chordata;Actinopteri;Myctophiformes;Myctophidae;Lampanyctodes;Lampanyctodes hectoris
Chordata;Aves;Galliformes;Phasianidae;Gallus;Gallus gallus
Chordata;Actinopteri;Argentiniformes;Microstomatidae
Chordata;Actinopteri;Gadiformes;Moridae;Mora;Mora moro
Chordata;Actinopteri;Gadiformes;Macrouridae;Coelorinchus;Coelorinchus aspercephalus
Chordata;Aves;Galliformes;Phasianidae;Meleagris;Meleagris gallopavo
Arthropoda;Insecta;Coleoptera;Staphylinidae;Stenomalium;Stenomalium helmsi
Mollusca;Gastropoda;NA;Turritellidae;Maoricolpus;Maoricolpus roseus
Mollusca;Cephalopoda;Octopoda;Octopodidae;Octopus;Octopus magnificus
Chordata;Amphibia;Anura;Pipidae;Xenopus
Chordata;Actinopteri;Perciformes;Sebastidae;Sebastes;Sebastes sp. ADS-2008a
Chordata;Mammalia;Carnivora;Otariidae;Eumetopias;Eumetopias jubatus
Chordata;Mammalia;NA;Bovidae;Ovis;Ovis aries
Chordata;Actinopteri;Perciformes;Triglidae
Arthropoda;Hexanauplia;Sessilia;Balanidae;Balanus;Balanus sp. 4 MPL-2014
Chordata;Actinopteri;Ophidiiformes;Ophidiidae;Genypterus;Genypterus chilensis
Mollusca;Cephalopoda;Teuthida;Onychoteuthidae;Moroteuthopsis;Moroteuthopsis aff. ingens HEB-2018
Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Hippocampus;Hippocampus ramulosus
Chordata;Actinopteri;NA;Emmelichthyidae;Emmelichthys;Emmelichthys nitidus
Chordata;Actinopteri;Gadiformes;Moridae;Antimora;Antimora microlepis
Chordata;Actinopteri;Gadiformes;Moridae;Lepidion;Lepidion lepidion
Chordata;Actinopteri;Centrarchiformes;Cheilodactylidae;Cheilodactylus;Cheilodactylus nigripes
Mollusca;Cephalopoda;Octopoda;Octopodidae;Macroctopus;Macroctopus maorum
Chordata;Actinopteri;Anguilliformes;Anguillidae;Anguilla
Chordata;Mammalia;Insectivora;Erinaceidae;Erinaceus;Erinaceus europaeus
Mollusca;Cephalopoda;Teuthida;Ommastrephidae;Nototodarus;Nototodarus sp. GD-2007
Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Vanacampus
Chordata;Actinopteri;Gadiformes;Moridae;Lepidion
Chordata;Actinopteri;Centrarchiformes;Kyphosidae;Medialuna;Medialuna californiensis
Chordata;Actinopteri;Labriformes;Labridae;Pseudolabrus;Pseudolabrus biserialis
Chordata;Actinopteri;Syngnathiformes;Syngnathidae
Chordata;Aves;Sphenisciformes;Spheniscidae;Megadyptes;Megadyptes antipodes
Arthropoda;Insecta;Coleoptera;Scarabaeidae;Epirinus;Epirinus aquilus
Chordata;Actinopteri;NA;Emmelichthyidae
Chordata;Actinopteri;Gadiformes;Gadidae;Micromesistius;Micromesistius environmental sample
Chordata;Actinopteri;Myctophiformes;Myctophidae;Lampanyctus
Annelida;Polychaeta;Phascolosomatiformes;Phascolosomatidae;Phascolosoma;Phascolosoma esculenta
Chordata;Actinopteri;Perciformes;Psychrolutidae;Cottunculus;Cottunculus thomsonii
Chordata;Actinopteri;Perciformes;Triglidae;Lepidotrigla
Arthropoda;Hexanauplia;Calanoida;Calanidae;Calanus;Calanus pacificus
Chordata;Aves;Psittaciformes;Psittacidae;Cyanoramphus;Cyanoramphus novaezelandiae
Chordata;Mammalia;Carnivora;Felidae;Felis;Felis silvestris
Cnidaria;Scyphozoa;Semaeostomeae;Ulmaridae;Phacellophora;Phacellophora sp. NA
Chordata;Mammalia;Rodentia;Muridae;Rattus;Rattus rattus
Annelida;Polychaeta;Phyllodocida;Nephtyidae;Aglaophamus;Aglaophamus sp. MB4
Mollusca;Cephalopoda;Octopoda;Octopodidae
Mollusca;Cephalopoda;Octopoda;Argonautidae;Argonauta;Argonauta nodosa
Chordata;Aves;Passeriformes;Thraupidae
Chordata;Actinopteri;Labriformes;Labridae
Mollusca;Cephalopoda;Teuthida;Octopoteuthidae;NA;Octopoteuthidae environmental sample cf. Octopoteuthis megaptera
Chordata;Actinopteri;Perciformes;Cottidae;Cottus;Cottus environmental sample

famgenandspe = set([taxon for taxon in taxo_summary.values() if taxon.count(";")>3])
for t in famgenandspe:
	print t


Arthropoda;Insecta;Thysanoptera;Thripidae;Scolothrips;Scolothrips takahashii
Chordata;Actinopteri;Myctophiformes;Myctophidae;Protomyctophum;Protomyctophum arcticum
Chordata;Actinopteri;Lampriformes;Trachipteridae;Trachipterus;Trachipterus arcticus
Chordata;Actinopteri;Perciformes;Sebastidae;Sebastes
Chordata;Actinopteri;Uranoscopiformes;Pinguipedidae;Parapercis;Parapercis allporti
Annelida;Clitellata;Haplotaxida;Enchytraeidae;Enchytraeus;Enchytraeus christenseni
Arthropoda;Insecta;Coleoptera;Scarabaeidae;Bohepilissus;Bohepilissus subtilis
Chordata;Actinopteri;Clupeiformes;Engraulidae;Engraulis;Engraulis environmental sample
Chordata;Actinopteri;Labriformes;Labridae;Pseudolabrus;Pseudolabrus miles
Chordata;Actinopteri;Labriformes;Labridae;Notolabrus;Notolabrus fucicola
Chordata;Actinopteri;Scombriformes;Scombridae;Allothunnus;Allothunnus fallai
Chordata;Actinopteri;Centrarchiformes;Cheilodactylidae;Cheilodactylus
Chordata;Actinopteri;Scombriformes;Gempylidae;Thyrsites;Thyrsites atun
Chordata;Actinopteri;Argentiniformes;Microstomatidae;Microstoma;Microstoma microstoma
Chordata;Aves;Passeriformes;Zosteropidae;Zosterops;Zosterops japonicus
Chordata;Actinopteri;Argentiniformes;Bathylagidae;Lipolagus;Lipolagus ochotensis
Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Hippocampus
Chordata;Actinopteri;Labriformes;Labridae;Pseudolabrus;Pseudolabrus biserialis
Chordata;Amphibia;Anura;Pipidae;Xenopus;Xenopus laevis
Chordata;Mammalia;Diprotodontia;Phalangeridae;Trichosurus;Trichosurus vulpecula
Chordata;Mammalia;Carnivora;Otariidae;Eumetopias;Eumetopias jubatus
Chordata;Actinopteri;Gadiformes;Moridae;Pseudophycis;Pseudophycis barbata
Chordata;Actinopteri;Myctophiformes;Myctophidae;Lampanyctodes;Lampanyctodes hectoris
Chordata;Aves;Galliformes;Phasianidae;Gallus;Gallus gallus
Chordata;Actinopteri;Gadiformes;Moridae;Mora;Mora moro
Chordata;Actinopteri;Gadiformes;Macrouridae;Coelorinchus;Coelorinchus aspercephalus
Chordata;Aves;Galliformes;Phasianidae;Meleagris;Meleagris gallopavo
Arthropoda;Insecta;Coleoptera;Staphylinidae;Stenomalium;Stenomalium helmsi
Mollusca;Gastropoda;NA;Turritellidae;Maoricolpus;Maoricolpus roseus
Mollusca;Cephalopoda;Octopoda;Octopodidae;Octopus;Octopus magnificus
Chordata;Amphibia;Anura;Pipidae;Xenopus
Chordata;Actinopteri;Perciformes;Sebastidae;Sebastes;Sebastes sp. ADS-2008a
Chordata;Actinopteri;Uranoscopiformes;Uranoscopidae;Kathetostoma;Kathetostoma canaster
Chordata;Mammalia;NA;Bovidae;Ovis;Ovis aries
Cnidaria;Scyphozoa;Semaeostomeae;Ulmaridae;Phacellophora;Phacellophora sp. NA
Arthropoda;Hexanauplia;Sessilia;Balanidae;Balanus;Balanus sp. 4 MPL-2014
Chordata;Actinopteri;Ophidiiformes;Ophidiidae;Genypterus;Genypterus chilensis
Mollusca;Cephalopoda;Teuthida;Onychoteuthidae;Moroteuthopsis;Moroteuthopsis aff. ingens HEB-2018
Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Hippocampus;Hippocampus ramulosus
Chordata;Actinopteri;NA;Emmelichthyidae;Emmelichthys;Emmelichthys nitidus
Chordata;Actinopteri;Gadiformes;Moridae;Antimora;Antimora microlepis
Chordata;Actinopteri;Gadiformes;Moridae;Lepidion;Lepidion lepidion
Chordata;Actinopteri;Centrarchiformes;Cheilodactylidae;Cheilodactylus;Cheilodactylus nigripes
Mollusca;Cephalopoda;Octopoda;Octopodidae;Macroctopus;Macroctopus maorum
Chordata;Actinopteri;Anguilliformes;Anguillidae;Anguilla
Chordata;Mammalia;Insectivora;Erinaceidae;Erinaceus;Erinaceus europaeus
Mollusca;Cephalopoda;Teuthida;Ommastrephidae;Nototodarus;Nototodarus sp. GD-2007
Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Vanacampus
Chordata;Actinopteri;Gadiformes;Moridae;Lepidion
Chordata;Actinopteri;Centrarchiformes;Kyphosidae;Medialuna;Medialuna californiensis
Chordata;Aves;Sphenisciformes;Spheniscidae;Megadyptes;Megadyptes antipodes
Arthropoda;Insecta;Coleoptera;Scarabaeidae;Epirinus;Epirinus aquilus
Chordata;Actinopteri;Gadiformes;Gadidae;Micromesistius;Micromesistius environmental sample
Chordata;Actinopteri;Myctophiformes;Myctophidae;Lampanyctus
Chordata;Actinopteri;Perciformes;Psychrolutidae;Cottunculus;Cottunculus thomsonii
Chordata;Actinopteri;Perciformes;Triglidae;Lepidotrigla
Arthropoda;Hexanauplia;Calanoida;Calanidae;Calanus;Calanus pacificus
Chordata;Aves;Psittaciformes;Psittacidae;Cyanoramphus;Cyanoramphus novaezelandiae
Chordata;Mammalia;Carnivora;Felidae;Felis;Felis silvestris
Chordata;Mammalia;Rodentia;Muridae;Rattus;Rattus rattus
Annelida;Polychaeta;Phyllodocida;Nephtyidae;Aglaophamus;Aglaophamus sp. MB4
Annelida;Polychaeta;Phascolosomatiformes;Phascolosomatidae;Phascolosoma;Phascolosoma esculenta
Mollusca;Cephalopoda;Octopoda;Argonautidae;Argonauta;Argonauta nodosa
Mollusca;Cephalopoda;Teuthida;Octopoteuthidae;NA;Octopoteuthidae environmental sample cf. Octopoteuthis megaptera
Chordata;Actinopteri;Perciformes;Cottidae;Cottus;Cottus environmental sample
for t in spe:
	print t