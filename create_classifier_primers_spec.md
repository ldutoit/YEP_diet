#create_classifier_primers_spec.md

This file creates two classifiers, those are primers specific.

The starting point is the database clipped for the reference primers


# collect fasta records

I downloaded all the metazoan records for 16S as well as 
![output/pictures/ncbiextraction.png](output/pictures/ncbiextraction.png)

as well as all the mitochondrion sequences for a few key group of species: 
```
#GENBANK queries
mitochondrion[filter] Actinopterygii[Organism] 
mitochondrion[filter] Cnidaria[Organism] 
mitochondrion[filter] Echinodermata[Organism] 
mitochondrion[filter] cephalopoda[Organism] 
mitochondrion[filter] Porifera[Organism] 
mitochondrion[filter] Cnidaria[Organism] 
```
I concatenated both:

cat actinopterygii.fasta metazoa16S.fasta cephalopoda.fasta cnidaria.fasta cephalopoda.fasta porifera.fasta  > allrecordsncbi.fasta

### Create database format for qiime to import

I used the tool [entrez qiime] (https://github.com/bakerccm/entrez_qiime) (python2.7, accessed december 2018). I followed the pdf tutorial.


```
#get taxonomy

wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz
tar -zxvf taxdump.tar.gz
 
ftp ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz
gunzip nucl_gb.accession2taxid.gz
```

```
python2.7 entrez_qiime.py  --inputfasta allrecordsncbi.fasta  -o  allrecordsncbi_accession.txt
```

That way every record is matched to a taxonomy in qiime2 standard format.

### Create classifier


Ce create the classifier according to
https://docs.qiime2.org/2018.11/tutorials/feature-classifier/
```
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path allrecordsncbi.fasta \
  --output-path allrecordsncbi.qza


qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \
  --input-path allrecordsncbi_accession.txt \
  --output-path ref-taxonomy.qza
```



We then clip them according to primers:


```
16S_LONG_Cephal_F
TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGGACGAGAAGACCCTAWTGAGCT
16S_LONG_Cephal_R
GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGAAATTACGCTGTTATCCCT
16S_LONG_Chord_F
TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGCGAGAAGACCCTRTGGAGCT
16S_SHORT_Chord_R
GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGTATCCTNGGTCGCCCCAAC
```




**cephalopods**
```
qiime feature-classifier extract-reads \
  --i-sequences allrecordsncbi.qza \
  --p-f-primer  GACGAGAAGACCCTAWTGAGCT \
    --p-r-primer  AAATTACGCTGTTATCCCT \
  --p-min-length 50 \
  --p-max-length 400 \
  --o-reads ref-seqsceph.qza
```

**chordates**
```
qiime feature-classifier extract-reads \
  --i-sequences allrecordsncbi.qza \
  --p-f-primer CGAGAAGACCCTRTGGAGCT  \
  --p-r-primer  TATCCTNGGTCGCCCCAAC \
  --p-min-length 50 \
  --p-max-length 400 \
  --o-reads ref-seqschor.qza
```

for chordates, we want to be able to add a few local sequences of important species:

```
# we export the one we have so far from the qiime object
qiime tools export --input-path  ref-seqschor.qza  --output-path ref-seqschor
cp ref-seqschor/dna-sequences.fasta > ref-seqschor.fa
# add those seqs to
 echo ">Auchenoceros_punctatus
TTAGACTTAAAATAAATTGCACTCTCATATTACTTACCCAATTAAATTCAGCAAATAAATATTGAAATGTCTTTG
>Bluecodconsensus_sequence
TTAGACACGAAGACAGCTCACCCCCCTTCCCCCTTCAGAAAAGGGCCAAATTAAGTGACCCTGCCCTAATGTCTTTG
AGAACCTCTGACTAAAAATGATCCGGCAAAGCCGATCAACGGACCGAGTTACCCT
>Silverside_consensus_sequence
TTAGACAAAAGGTAGACCACGTTTAACCCCCCTCCCTAACAGGACTAAACACAGTGCTCCCCTAACCTATATGTCTTTG" > extraseq.fa
```

and those to beginning of allrecordsncbi_accession.txt:


```
cat extraseq.fa ref-seqschor.fa  > ref-seqschorwithextra.fa
```
and the taxonomy to beginning of allrecordsncbi_accession.txt (tab separated two columns):

```
Auchenoceros_punctatus  Chordata;Actinopteri;Gadiformes;Moridae;Auchenoceros;Auchenoceros punctatus
Bluecodconsensus_sequence Chordata;Actinopteri; Trachiniformes;Pinguipedidae;Parapercis;Parapercis colias
Silverside_consensus_sequence Chordata;Actinopteri;Argentiniformes;Argentinidae;Argentina;Argentina elongata
```


```
#reimport taxonomy

qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \
  --input-path allrecordsncbi_accession.txt \
  --output-path ref-taxonomy.qza

```
Cephalopods do not have extra sequences.

## IMPORT and train


### Chordates

```
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path ref-seqschorwithextra.fa \
  --output-path allrecordsncbi_clippedchor.qza

qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads allrecordsncbi_clippedchor.qza \
  --i-reference-taxonomy  ref-taxonomy.qza \
  --o-classifier classifierchor.qza
```
### Cephalo
Cephalopods do not have extra sequences.

```

qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads ref-seqsceph.qza \
  --i-reference-taxonomy  ref-taxonomy.qza \
  --o-classifier classifierceph.qza
```
