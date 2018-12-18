# create_classifier.md


This summarises the steps I used to create the qiime database/

#collect fasta records

I downloaded all the metazoan records from genbank.

![output/pictures/ncbiextraction.png](output/pictures/ncbiextraction.png)


**In construction ( add silva and greengenes found)**



### Create database format for qiime to import

I used the tool [entrez qiime] (https://github.com/bakerccm/entrez_qiime) (python2.7, accessed december 2018). I followed the pdf tutorial.


```
#get taxonomy

wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz
tar -zxvf taxdump.tar.gz
 
ftp ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz
gunzip nucl_gb.accession2taxid.gz


python2.7 entrez_qiime.py  --inputfasta metazoa16S.fasta --outputfile metazoa16S.fasta -o  metazoa16S_accession.txt
```
That way every record is matched to a taxonomy in qiime2 standard format.

### Create classifier


Ce create the classifier according to
https://docs.qiime2.org/2018.11/tutorials/feature-classifier/
```
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path metazoa16S.fasta \
  --output-path metazoa16S.qza


qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \
  --input-path metazoa16S_accession.txt \
  --output-path ref-taxonomy.qza
```


Our primers can be extracted for chordates and cephalopods as per Table 1 and S1 of [Beagle et al. 2007](doi:10.1371/journal.pone.0000831).

We then use them to create a set of raw reads to train the classifier on.


**cephalopods**
```
#qiime feature-classifier extract-reads \
#  --i-sequences taxonomy/metazoa16S.qza \
#  --p-f-primer CGCCGAATCCCGTCGCMAGTAAAMGGCTTC \
#  --p-r-primer CCAAGCAACCCGACTCTCGGATCGAA \
#  --p-min-length 100 \
#  --p-max-length 400 \
#  --o-reads ref-seqsceph.qza
```

**chordates**
```
qiime feature-classifier extract-reads \
  --i-sequences taxonomy/metazoa16S.qza \
  --p-f-primer GACGAKAAGACCCTA  \
  --p-r-primer CGCTGTTATCCCTADRGTAACT \
  --p-min-length 100 \
  --p-max-length 400 \
  --o-reads ref-seqschor.qza
```

### Train classifier

```
qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads ref-seqschor.qza \
  --i-reference-taxonomy  taxonomy/ref-taxonomy.qza \
  --o-classifier classifier.qza
```

Great! we now have a trained classifier.