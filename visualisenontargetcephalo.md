For the paper to be able to demonstrate what else is in the cephalopod


```
qiime taxa barplot \
  --i-table  table-dada2cephalo.qza \
  --i-taxonomy taxonomy_cephalo.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadataextended.tsv \
  --o-visualization taxa-bar-plotsallcephalo.qzv
```
