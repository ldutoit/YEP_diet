# QIIME2pipe.md

### Summary

### import the data

I follow [info](https://docs.qiime2.org/2018.11/tutorials/importing/#manifest-file) and a phred score quality [here](https://www.drive5.com/usearch/manual/quality_score.html) to be able to create the write import command.

First I created a [manifest](metadata/manifestcephalo) file matching fastq to sample IDs. It should be noted than QIIME2 only accpets absolute paths for this. This also directly assign samples to fastq and the output file is therefore demultiplexed.

```
#module load Miniconda3
#source activate qiime2-2018.11 # version 2018.11
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path ~/repos/scripts/YEP_diet/metadata/manifestcephalo \
  --output-path paired-end-demuxcephalo.qza \
  --input-format PairedEndFastqManifestPhred33
```
We can visualise the output by creating a visualisation file qzv:


```
qiime demux summarize   --i-data paired-end-demuxcephalo.qza  --o-visualization paired-end-demuxcephalo.qzv
```


**Forward reads**
Total Sequences Sampled 10000
2%  6 nts
9%  6 nts
25% 178 nts
50% (Median)  178 nts
75% 178 nts
91% 178 nts
98% 178 nts

**Reverse Reads**
Total Sequences Sampled 10000
2%  6 nts
9%  6 nts
25% 180 nts
50% (Median)  181 nts
75% 181 nts
91% 181 nts
98% 181 nts

### Denoising


```
#!/bin/sh
qiime dada2 denoise-paired \
 --i-demultiplexed-seqs paired-end-demuxcephalo.qza \
 --o-representative-sequences rep-seqs-dada2cephalo.qza \
 --o-table table-dada2cephalo.qza \
 --p-n-threads 8 \
 --p-trunc-len-f 0 \
 --p-trunc-len-r 0 \
 --o-denoising-stats stats-dada2cephalo.qza 
```

Visualising the denoising :


```
qiime metadata tabulate \
  --m-input-file stats-dada2cephalo.qza \
  --o-visualization stats-dada2cephalo.qzv



qiime tools export --input-path rep-seqs-dada2cephalo.qza --output-path dna_sequences
```


### Feature classifier

I need to create my own feature classifier in order to assign taxonomy to the features. This process is detailed in [create_classifiercehalo.md](create_classifiercephalo.md)


Once I created my featureclassifier, I assign my features to features.

 This takes quite some temporary space. I therefore create a tmp folder and use it as the tmp folder for qiime to work on:

```
mkdir /home/ludovic.dutoit/projects/tmp
export TMPDIR="/home/ludovic.dutoit/projects/tmp"
```

and then  I can finally assign stuff!


```
qiime feature-classifier classify-sklearn \
  --i-classifier taxo_primerspec/classifierceph.qza \
  --i-reads  rep-seqs-dada2cephalo.qza \
  --o-classification taxonomy_cephalo.qza

qiime metadata tabulate \
  --m-input-file  taxonomy_cephalo.qza \
  --o-visualization taxonomy_cephalo.qzv



qiime taxa barplot \
  --i-table table-dada2cephalo.qza \
  --i-taxonomy taxonomy_cephalo.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadata.tsv \
  --o-visualization taxa-bar-plotscephalo.qzv
```


