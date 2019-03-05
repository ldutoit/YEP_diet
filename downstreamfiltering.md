I still kept the dataset separated for the two different primers
#Step 1: Remove non-targeted taxa

I remove all data that is from non-targeted species.

```
 qiime taxa filter-table --p-include cephalopoda --i-table table-dada2cephalo.qza --i-taxonomy taxonomy_cephalo.qza --o-filtered-table table-dada2cephaloONLY.qza --p-mode contains


 qiime taxa filter-table --p-include Actinopteri --i-table table-dada2chordates.qza --i-taxonomy taxonomy_chordates.qza --o-filtered-table table-dada2chordatesONLY.qza --p-mode contains
```


#Step 2: filter low quality samples
Filter the samples that are okay based on amount of alpha rarefaction on the fish species. NOT SURE HOW

paired-end-demuxcephalo.qzv

```
Samples nreads
S174	70
S78	52
S39	40
S131	15
S145	8
S22	5
S36	4
S62	2
S42	0
S50	0
S210	0
```


demux_chordates.qzv


```
S85	393
S4	282
S81	260
S78	49
S209	16
```

###Replot with metadata


```
qiime taxa barplot \
  --i-table table-dada2cephaloONLY.qza \
  --i-taxonomy taxonomy_cephalo.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadataextended.tsv \
  --o-visualization taxa-bar-plotscephalo.qzv


qiime taxa barplot \
  --i-table table-dada2chordatesONLY.qza \
  --i-taxonomy taxonomy_chordates.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadataextended.tsv \
  --o-visualization taxa-bar-plotschordates.qzv
```

I then downloaded those two files as:

...
and 

...

