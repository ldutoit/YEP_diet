#summary_features_taxonomy.md
I want a summary of the most common features associated with their taxonomy to know how well common features were assigned to genus/species.

First, I extract the appropriate data_table

```
qiime feature-table summarize   --i-table table-dada2cephalo.qza   --o-visualization table-dada2cephalo.qzv

qiime feature-table summarize   --i-table table-dada2chordates.qza   --o-visualization table-dada2chordates.qzv
```



### For each primerpair indepdently

The command below are specifically to download the required data pon my cinoputer

Going into [https://view.qiime2.org/](https://view.qiime2.org/) I can extract the **feature detail** tab of the newly created table-dada2cephalo.qzv/table-dada2chordates.qzv to see what are the common features (frequency/ number of species found in). I saved that table as [metadata/featuresummarycephalo.txt](metadata/featuresummarycephalo.txt)/[metadata/featuresummarychordates.txt](metadata/featuresummarychordates.txt)

```
#locally
scp mahuika:/home/ludovic.dutoit/projects/edna_yep/table-dada2cephalo.qzv .
scp mahuika:/home/ludovic.dutoit/projects/edna_yep/table-dada2chordates.qzv .
#and then on qiime view before download 
```


I then use [https://view.qiime2.org/](https://view.qiime2.org/) to extract a table matching taxonomy assignment and feature name. I do this with **taxonomy_chordates.qzv/taxonomy_cephalo.qzv** and then use the *download metadata tsv file* tab at metadata/feature_taxonomy_chordates.csv metadata/feature_taxonomy_cephalo.csv

```
#locally
scp mahuika:/home/ludovic.dutoit/projects/edna_yep/taxonomy_cephalo.qzv .
and then on view.wiim2.org  before downloading as:

/Users/dutlu42p/repos/mahuika/YEP_diet/metadata/feature_taxonomy_cephalo.csv

scp mahuika:/home/ludovic.dutoit/projects/edna_yep/taxonomy_chordates.qzv
#and then on view.wiim2.org  before downloading as:

 /Users/dutlu42p/repos/mahuika/YEP_diet/metadata/feature_taxonomy_chordates.csv
```


Finally, I extracted the associated dna sequences 

```
#on cluster
qiime tools export --input-path  rep-seqs-dada2cephalo.qza --output-path test
cp test/dna-sequences.fasta  dna-sequencescephalo.fasta 
rm -r test

qiime tools export --input-path  rep-seqs-dada2chordates.qza --output-path test
cp test/dna-sequences.fasta  dna-sequenceschordates.fasta 
rm -r test
```
and then downloaded the file *dna-sequencescephalo.fasta/dna-sequenceschordates.fasta* [metadata/featurescephalo.fasta](metadata/featurescephalo.fasta)/[metadata/featureschordates.fasta](metadata/featureschordates.fasta)

```
#locally
scp mahuika:/home/ludovic.dutoit/projects/edna_yep/dna-sequencescephalo.fasta /Users/dutlu42p/repos/mahuika/YEP_diet/metadata/featurescephalo.fasta

scp mahuika:/home/ludovic.dutoit/projects/edna_yep/dna-sequenceschordates.fasta /Users/dutlu42p/repos/mahuika/YEP_diet/metadata/featureschordates.fasta
```

I then combined those 6 files locally as two using [feature_taxo_summary_primerspec.py](feature_taxo_summary_primerspec.py). 



```
output/summary_features_taxo_primerspec_chordates.csv
output/summary_features_taxo_primerspec_cephalo.csv
```

Those two files allow a closer look at how well the common sequences are assigned and lead work on the database. It allows to extract sequences etc.