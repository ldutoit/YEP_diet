#module load Python/2.7.14-gimkl-2017a


Here I tried to create a better database out of the species the yellow eyed penguin is known to eat (Mel shared document).

I tried to do my best to include all the species known by Mel (n=44). when species is not available, I take genus.

I also included all the species known at. the genus level from the first round of QIIME.


```
#python
#Grab pour 45 species and then the species identified to species level that are not in there...
from Bio import SeqIO
features_fasta =  {seq.id:  str(seq.seq) for seq in SeqIO.parse("taxonomy_round2/allrecordsncbi.fasta","fasta")} # all records from ncbi
list_species=[line.strip() for line in open("/home/ludovic.dutoit/repos/scripts/YEP_diet/metadata/list_species_closed.txt") if not "#" in line] # this file contains both species I want and things found at the first rounf of qiime

#taxo
taxo = [line.strip() for line in open("taxonomy_round2/allrecordsncbi_accession.txt")] # nmatching taxonomy for record

clean_fasta= {}
clean_taxo = []
missing = []
genus = []
species_level=[]
for sp in list_species:
  print sp
  # means it is a species 
  temp = [x for x in taxo if sp.strip() in x ]
  if len(temp)>1: species_level.append(sp.strip())
  if len(temp)==0:
    temp = [x for x in taxo if sp.strip().split()[0] in x.strip().split(";")[-1] ]
    print(temp)
    if len(temp)==0:
      missing.append(sp.strip())
    else:
      genus.append(sp.strip())
  if len(temp)>1:
    print len(temp)
    #for x in temp:
    #  print x.split()[0], features_fasta[x.split()[0]]
    temp2 = set(features_fasta[x.split()[0]] for x in temp)
  if len(temp)>0:
    #TEMP HAS THE RIGHT RECORDS, HERE I CHOOSE THE FIRST ONE RANDOMLY.. BUT I COULD SELECT ON LENGTH OR RELATEDNESS OF THE SPECIES TO OUR SPECIES OF INTEREST IF OUR SPECIES IS MISSING
    clean_fasta[temp[0].split()[0]]= features_fasta[temp[0].split()[0]]
    clean_taxo.append(temp[0])
```


#Put it in files

taxonomy_round3/accession_round3.txt
taxonomy_round3/round3.fasta
```
import os
os.mkdir("taxonomy_round3")
output=open("taxonomy_round3/accession_round3.txt","w")
output.write("\n".join([taxo for taxo in clean_taxo]))
output.close()


output=open("taxonomy_round3/round3.fasta","w")
output.write("\n".join([">"+key+"\n"+clean_fasta[key] for key in clean_fasta.keys()]))
output.close()

```


#how full is my db?

here are the species I have at the species level:
>>>[x for x in species_level if len(x.split())==2]
['Parapercis colias',
 'Pseudophycis bachus',
 'Sprattus antipodum',
 'Nototodarus sloani',
 'Thyrsites atun',
 'Seriolella brama',
 'Merluccius australis',
 'Macruronus novaezelandiae',
 'Nyctiphanes australis',
 'Pelotretis flavilatus',
 'Genypterus blacodes',
 'Macroctopus maorum',
 'Maurolicus muelleri',
 'Lotella rhacina',
 'Hippocampus abdominalis',
 'Anguilla australis',
 'Seriolella punctata',
 'Retropinna retropinna',
 'Peltorhamphus novaezeelandiae',
 'Sprattus muelleri',
 'Forsterygion lapillum',
 'Nemadactylus macropterus',
 'Gonorynchus gonorynchus',
 'Scorpaena cardinalis',
 'Helicolenus percoides',
 'Moroteuthis ingens',
 'Protomyctophum arcticum',
 'Trachipterus arcticus',
 'Parapercis allporti',
 'Pseudolabrus miles',
 'Notolabrus fucicola',
 'Allothunnus fallai',
 'Thyrsites atun',
 'Lipolagus ochotensis',
 'Pseudolabrus biserialis',
 'Mora moro',
 'Coelorinchus aspercephalus',
 'Maoricolpus roseus',
 'Kathetostoma canaster',
 'Hippocampus ramulosus',
 'Emmelichthys nitidus',
 'Antimora microlepis',
 'Lepidion lepidion',
 'Cheilodactylus nigripes',
 'Macroctopus maorum',
 'Erinaceus europaeus',
 'Medialuna californiensis',
 'Epirinus aquilus',
 'Cottunculus thomsonii',
 'Phascolosoma esculenta',
 'Argonauta nodosa',
 'Octopoteuthis megaptera']

here are the species for which we have relative at the genus level:
>>>genus
['Argentina elongata',
 'Grahamina nigripenne',
 'Cephalopoda squilid',
 'Sepioloidea pacifica',
 'Lissocampus filum',
 'Heterosquilla sp.']

known at genus level from round 1

>>>[x for x in species_level if len(x.split())==1]
['Sebastes',
 'Engraulis',
 'Cheilodactylus',
 'Hippocampus',
 'Xenopus',
 'Phacellophora',
 'Balanus',
 'Moroteuthopsis',
 'Anguilla',
 'Nototodarus',
 'Vanacampus',
 'Lepidion',
 'Lampanyctus',
 'Lepidotrigla',
 'Aglaophamus']

>>>missing
['Auchenoceros punctatus',
 'Hemerocoetes monopterygius',
 'Hemerocoetes artus',
 'Kathestoma giganteum',
 'Parika scaber',
 'Grahamichtys radiata',
 'Stigmatophora macropterygia',
 'Tewara cranwellae',
 'Gnatophis habenatus',
 'Thaliacea sp.']


## Add home sequenced species
I got a few species from Mel:

```
>Mel10_LongChord16SF_bluecod_Parapercis_colias
CCCCTTCAGAGAGGGCCAAATTAAGTGACCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGAAGCACTTATCCCCCACGTAGGCTGGGAAAACCTCCTATAAACAAGAGCTTCAGCTCTAATAATCAGAACCTCTGACTAAAAATGATCCGGCAAAGCCGATCAACGGACCGAGTTACCCTAGGGATAACAGCGCAATC
 
>Mel7_LongChord16SF_Barracouta_Thyrsites_atun
ACCCTAAACAAAGGACTGAACTGAACAAACCATGCCCCTCTGTCTTAGGTTGGGGCGACCCCGAGGAAACAAAAAACCCACGAGTGGAATGGGAGCACTGACCTCCTACAACCAAGAGCTGCAGCTCTAACTAATAGAATTTCTAACCAATAATGATCCGGCAAAGCCGATTAACGAACCAAGTTACCCTAGGGATAAAGCGCAATC
 
>Mel3_LongChord16SF_Pigfish_red_Bodianus_unimaculatus
CCCCCAGACAAGGGGCCAAACCAAATGATCCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGCAACAAAAAACCCCCACGTGGAATGGGACTATCCTCCTACAAACAAGAGCTGCAGCTCTAGTTCACAGAATTTCTGACCAATAAGATCCGGCAAAGCCGATCAACGAACCGAGTTACCCTAGGGATAAAGCGCAATC
 
>Mel2_LongChord16SF_Seahorse_Hippocampus_abdominalis
GCCCCCTAAAAGGCAACAAGCCAGTAACCTCATTTTAATATCTTTAGTTGGGGCGACCGCGGAGTAAAACAAAACCTCCGTGAGGATTGAGGTAAAACCTTATACCTAAGAAAGTCATTTCTAAGCACCAAAATATTTGACCTAAAGATCCGGCAATAGCCGATCAACGAACCTAGTTACCCCAGGGATAAAGCGCAATC
```
I add them manually and create the file by adding those lines to round3.fasta:



```
>MEL00002.1
CCCCTTCAGAGAGGGCCAAATTAAGTGACCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGAAGCACTTATCCCCCACGTAGGCTGGGAAAACCTCCTATAAACAAGAGCTTCAGCTCTAATAATCAGAACCTCTGACTAAAAATGATCCGGCAAAGCCGATCAACGGACCGAGTTACCCTAGGGATAACAGCGCAATC
>MEL00003.1
ACCCTAAACAAAGGACTGAACTGAACAAACCATGCCCCTCTGTCTTAGGTTGGGGCGACCCCGAGGAAACAAAAAACCCACGAGTGGAATGGGAGCACTGACCTCCTACAACCAAGAGCTGCAGCTCTAACTAATAGAATTTCTAACCAATAATGATCCGGCAAAGCCGATTAACGAACCAAGTTACCCTAGGGATAAAGCGCAATC
>MEL00004.1
CCCCCAGACAAGGGGCCAAACCAAATGATCCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGCAACAAAAAACCCCCACGTGGAATGGGACTATCCTCCTACAAACAAGAGCTGCAGCTCTAGTTCACAGAATTTCTGACCAATAAGATCCGGCAAAGCCGATCAACGAACCGAGTTACCCTAGGGATAAAGCGCAATC
>MEL00001.1
GCCCCCTAAAAGGCAACAAGCCAGTAACCTCATTTTAATATCTTTAGTTGGGGCGACCGCGGAGTAAAACAAAACCTCCGTGAGGATTGAGGTAAAACCTTATACCTAAGAAAGTCATTTCTAAGCACCAAAATATTTGACCTAAAGATCCGGCAATAGCCGATCAACGAACCTAGTTACCCCAGGGATAAAGCGCAATC
```


and those to accession_round3.txt:

```
MEL00001.1  Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Hippocampus;Hippocampus abdominalis
MEL00002.1  Chordata;Actinopteri;Uranoscopiformes;Pinguipedidae;Parapercis;Parapercis colias
MEL00003.1 Chordata;Actinopteri;Scombriformes;Gempylidae;Thyrsites;Thyrsites atun
MEL00004.1  Chordata;Actinopteri;Labriformes;Labridae;Bodianus;Bodianus unimaculatus 
```

# I recreate the classifier

For now I left duplicates in and re-created the classifer and run the table using [create_closed_classifier_object.md](create_closed_classifier_object.md)


#running QIIME

[closed_classifier_QIIME.md](closed_classifier_QIIME.md)