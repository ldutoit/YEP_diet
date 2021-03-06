# create_classifier.md


This summarises the steps I used to create the qiime database/

#collect fasta records

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

All these sequences won't necessarily contains our sequence of interest but the'll be clipped(i.e. filtered) using our primers later.


### Create database format for qiime to import

I used the tool [entrez qiime] (https://github.com/bakerccm/entrez_qiime) (python2.7, accessed december 2018). I followed the pdf tutorial.


```
#get taxonomy

wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz
tar -zxvf taxdump.tar.gz
 
ftp ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz
gunzip nucl_gb.accession2taxid.gz
```

allrecordsncbi.fasta
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



We then use them to create a set of raw reads to train the classifier on. We first clip the sequences using our primers.

The primers given by Bruce:

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

We need to remove the Nextera adapters:

```
Read 1
5’ TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG
Read 2
5’ GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG

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
**Combine them**

```
#Export
qiime tools export --input-path  ref-seqschor.qza  --output-path ref-seqschor
qiime tools export --input-path  ref-seqsceph.qza  --output-path ref-seqsceph
#combine them
cat ref-seqsceph/dna-sequences.fasta ref-seqschor/dna-sequences.fasta > dna-squences_combined_clipped.fasta

```

### Verify taxonomic breadth of classifier

I add them manually and create the file by adding those lines to  beginning of dna-squences_combined_clipped.fasta:



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


and those to beginning of allrecordsncbi_accession.txt:

```
MEL00001.1  Chordata;Actinopteri;Syngnathiformes;Syngnathidae;Hippocampus;Hippocampus abdominalis
MEL00002.1  Chordata;Actinopteri;Uranoscopiformes;Pinguipedidae;Parapercis;Parapercis colias
MEL00003.1 Chordata;Actinopteri;Scombriformes;Gempylidae;Thyrsites;Thyrsites atun
MEL00004.1  Chordata;Actinopteri;Labriformes;Labridae;Bodianus;Bodianus unimaculatus 
```


### Re import and Train classifier

```
qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \
  --input-path allrecordsncbi_accession.txt \
  --output-path ref-taxonomy.qza

qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path dna-squences_combined_clipped.fasta \
  --output-path allrecordsncbi_clipped.qza


qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads allrecordsncbi_clipped.qza \
  --i-reference-taxonomy  ref-taxonomy.qza \
  --o-classifier classifier.qza
```

Great! we now have a trained classifier.

I just output the clipped sequences as a fasta file so that I can see which species are still in there or not:

```
qiime tools export --input-path allrecordsncbi_clipped.qza  --output-path dna_sequences_clipped
```