Grab pour 45 species and then the species identified to species level that are not in there...



allrecordsncbi.fasta is the base

I create the file list_species_closed.txt

It contains the species that we have from Bruce, in some other occurences the genus
and then all ther species that were not in Bruce but that were identified to species level in round 2

species = [species.strip() for species in open("list_species_closed.txt")]
fasta =

for sp in species"
 if len(sp.split()) = 2 # means it is a species 
  temp= {}
  temp = look for species iand append to new dict
  if nothing in temp:
  	fo to genus
   #fitlter temo
  # add temp to big dict
  else: it is one species
    	fo to genus
   	#fitlter temo
  	# add temp to big dict


 Add the extra data from Bruce

 >Mel10_LongChord16SF_bluecod
CCCCTTCAGAGAGGGCCAAATTAAGTGACCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGAAGCACTTATCCCCC
ACGTAGGCTGGGAAAACCTCCTATAAACAAGAGCTTCAGCTCTAATAATCAGAACCTCTGACTAAAAATGATCCGGCAAA
GCCGATCAACGGACCGAGTTACCCTAGGGATAACAGCGCAATC
 
>Mel7_LongChord16SF_Barracouta
ACCCTAAACAAAGGACTGAACTGAACAAACCATGCCCCTCTGTCTTAGGTTGGGGCGACCCCGAGGAAACAAAAAACCCA
CGAGTGGAATGGGAGCACTGACCTCCTACAACCAAGAGCTGCAGCTCTAACTAATAGAATTTCTAACCAATAATGATCCG
GCAAAGCCGATTAACGAACCAAGTTACCCTAGGGATAAAGCGCAATC
 
>Mel3_LongChord16SF_Pigfish
CCCCCAGACAAGGGGCCAAACCAAATGATCCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGCAACAAAAAACCCC
CACGTGGAATGGGACTATCCTCCTACAAACAAGAGCTGCAGCTCTAGTTCACAGAATTTCTGACCAATAAGATCCGGCAA
AGCCGATCAACGAACCGAGTTACCCTAGGGATAAAGCGCAATC
 
>Mel2_LongChord16SF_Seahorse
GCCCCCTAAAAGGCAACAAGCCAGTAACCTCATTTTAATATCTTTAGTTGGGGCGACCGCGGAGTAAAACAAAACCTCCG
TGAGGATTGAGGTAAAACCTTATACCTAAGAAAGTCATTTCTAAGCACCAAAATATTTGACCTAAAGATCCGGCAATAGC
CGATCAACGAACCTAGTTACCCCAGGGATAAAGCGCAATC

alternatively I use qiime vsearch that does the clustering