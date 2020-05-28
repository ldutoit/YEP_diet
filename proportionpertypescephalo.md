We create this file with downstream filtering:

```
qiime feature-table filter-features \
  --i-table table-dada2cephalomin2000.qza \
  --p-min-frequency 50 \
  --o-filtered-table sample-contingency-filtered-table.qza
  ```
  
It stills include non target

We summarise it as a barplot using

```
qiime taxa barplot \
--i-table  sample-contingency-filtered-table.qza \
--i-taxonomy taxonomy_cephalo.qza \
--m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadataextended.tsv \
--o-visualization taxa-bar-plotstargetnontargetcephalo.qzv
```

We then inputted this taxa into https://view.qiime2.org/ at level 5 and summarised info into [output/cephalo_proportion_tables.txt](output/cephalo_proportion_tables.txt)
