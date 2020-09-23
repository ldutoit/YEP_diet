# QIIME2pipe.md

 
### Summary

### import the data

I follow [info](https://docs.qiime2.org/2018.11/tutorials/importing/#manifest-file) and a phred score quality [here](https://www.drive5.com/usearch/manual/quality_score.html) to be able to create the write import command.

First I created a [manifest](metadata/manifestchordates) file matching fastq to sample IDs. It should be noted than QIIME2 only accpets absolute paths for this. This also directly assign samples to fastq and the output file is therefore demultiplexed.

```
#module load Miniconda3
#source activate qiime2-2018.11 # version 2018.11
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path ~/repos/scripts/YEP_diet/metadata/manifestchordates \
  --output-path paired-end-demuxchordates.qza \
  --input-format PairedEndFastqManifestPhred33
```
We can visualise the output by creating a visualisation file qzv:

```
qiime demux summarize   --i-data paired-end-demuxchordates.qza   --o-visualization demuxchordates.qzv
```


**Total Sequences Sampled**|**10000**
Forward Reads
Total Sequences Sampled 10000
2%  68 nts
9%  68 nts
25% 77 nts
50% (Median)  79 nts
75% 79 nts
91% 79 nts
98% 180 nts
**Forward reads**


**Reverse reads**|**10000**

Total Sequences Sampled 10000
2%  66 nts
9%  68 nts
25% 77 nts
50% (Median)  79 nts
75% 79 nts
91% 79 nts
98% 181 n

### Denoising

```
#!/bin/sh
# source activate /scale_wlg_persistent/filesets/project/uoo00116/repos
qiime dada2 denoise-paired \
 --i-demultiplexed-seqs paired-end-demuxchordates.qza \
 --o-representative-sequences rep-seqs-dada2chordates.qza \
 --o-table table-dada2chordates.qza \
 --p-n-threads 8 \
 --p-trunc-len-f 0 \
 --p-trunc-len-r 0 \
 --o-denoising-stats stats-dada2chordates.qza 
```

Visualising the denoising :


```
  qiime metadata tabulate \
    --m-input-file stats-dada2chordates.qza \
    --o-visualization stats-dada2chordates.qzv


qiime tools export --input-path rep-seqs-dada2chordates.qza --output-path dna_sequences
```


### Feature classifier

I need to create my own feature classifier in order to assign taxonomy to the features. This process is detailed in [create_classifier_primers_spec.md](create_classifier_primers_spec.md)


Once I created my featureclassifier, I assign my features to features.

 This takes quite some temporary space. I therefore create a tmp folder and use it as the tmp folder for qiime to work on:

```
mkdir /home/ludovic.dutoit/projects/tmp
export TMPDIR="/home/ludovic.dutoit/projects/tmp"
```

and then  I can finally assign the taxonomy!


```
qiime feature-classifier classify-sklearn \
  --i-classifier taxo_primerspec/classifierchor.qza \
  --i-reads  rep-seqs-dada2chordates.qza \
  --o-classification taxonomy_chordates.qza

qiime metadata tabulate \
  --m-input-file taxonomy_chordates.qza \
  --o-visualization taxonomy_chordates.qzv



qiime taxa barplot \
  --i-table table-dada2chordates.qza \
  --i-taxonomy taxonomy_chordates.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadata.tsv \
  --o-visualization taxa-bar-plotschordates.qzv
```
This barplot can be visualised into qiime2. We then proceeded with the file [downstreamfiltering.md](downstreamfiltering.md) that filters only Fishes from this dataset as well as deal with a minimum number of sequences.
