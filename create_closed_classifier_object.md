# create_classifier_closed.md


This summarises the steps I used to create the qiime database/

#collect fasta records

I create the classifier according to
https://docs.qiime2.org/2018.11/tutorials/feature-classifier/

```
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path round3.fasta \
  --output-path round3.qza

# I have a couple of duplicated taxonomy
less accession_round3.txt  | sort | uniq > accession_round3uniq.txt
qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \
  --input-path accession_round3uniq.txt \
  --output-path ref-taxonomy.qza
```



We then use them to create a set of raw reads to train the classifier on. We first clip the sequences using our primers.

The primers given by Bruce:


**cephalopods**
```
qiime feature-classifier extract-reads \
  --i-sequences round3.qza \
  --p-f-primer  GACGAGAAGACCCTAWTGAGCT \
    --p-r-primer  AAATTACGCTGTTATCCCT \
  --p-min-length 50 \
  --p-max-length 400 \
  --o-reads ref-seqsceph.qza
```

**chordates**
```
qiime feature-classifier extract-reads \
  --i-sequences round3.qza \
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


qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path dna-squences_combined_clipped.fasta \
  --output-path allrecordsncbi_clipped.qza
```


### Train classifier

```
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


