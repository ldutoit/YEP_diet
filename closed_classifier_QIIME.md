```
qiime feature-classifier classify-sklearn \
  --i-classifier taxonomy_round2/classifier.qza \
  --i-reads  rep-seqs-dada2.qza \
  --o-classification taxonomy.qza

qiime metadata tabulate \
  --m-input-file taxonomy.qza \
  --o-visualization taxonomy.qzv



qiime taxa barplot \
  --i-table table-dada2.qza \
  --i-taxonomy taxonomy.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadata.tsv \
  --o-visualization taxa-bar-plotsround3.qzv
```

