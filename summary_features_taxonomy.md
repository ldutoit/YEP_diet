#summary_features_taxonomy.md
I want a summary of the most common features associated with their taxonomy to know how well common features were assigned to genus/species.

First, I extract the appropriate data_table.

```
qiime feature-table summarize   --i-table table-dada2.qza   --o-visualization table-dada2.qzv
```

Going into [https://view.qiime2.org/](https://view.qiime2.org/) I can extract the **feature detail** tab of the newly created table-dada2.qzv to see what are the common features (frequency/ number of species found in). I saved that table as [featuresummary.txt]

I then use [https://view.qiime2.org/](https://view.qiime2.org/) to extract a table matching taxonomy assignment and feature name. I do this with **taxonomy.qzv** and then use the *download metadata tsv file* tab at [metadata/feature_taxonomy.csv]


Finally, I extracted the associated dna sequences qiime tools export --input-path  rep-seqs-dada2.qza --output-path test

and then downloaded the file *dna-sequences.fasta* into the output-;ath (i.e. test) as [metadata/features.fasta](metadata/features.fasta)

I then combined those 3 files as one using [feature_taxo_summary.py]