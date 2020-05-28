```
qiime feature-table filter-features \
  --i-table table-dada2chordates.qza \
  --p-min-frequency 100 \
  --o-filtered-table sample-contingency-filtered-table.qza
```

This file contains all samples with features found in at least 100 reads.

In the downstream filtering, we remove all the samples with less than 2000 ray-finned fishes. But we are interested in keeping all-non target taxa so we cannot remove all samples wuth less than 2000 reads. We will do that manually later.

We create that barplot:

```
qiime taxa barplot \
  --i-table sample-contingency-filtered-table.qza \
  --i-taxonomy taxonomy_chordates.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadataextended.tsv \
  --o-visualization  taxa-bar-plotstargetnontargetchordates.qzv
```

We visualise it on https://view.qiime2.org/ that we download at level 5 (genus) . We can then summarise target and non-target. 
