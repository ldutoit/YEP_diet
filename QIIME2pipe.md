# QIIME2pipe.md

**in construction**

### Summary

### import the data

I follow [info](https://docs.qiime2.org/2018.11/tutorials/importing/#manifest-file) and a phred score quality [here](https://www.drive5.com/usearch/manual/quality_score.html) to be able to create the write import command.

First I created a [manifest](metadata/manifest) file matching fastq to sample IDs. It should be noted than QIIME2 only accpets absolute paths for this. This also directly assign samples to fastq and the output file is therefore demultiplexed.

```
#source activate /scale_wlg_persistent/filesets/project/uoo00116/repos # version 2018.11
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path ~/repos/scripts/YEP_diet/metadata/manifest \ 
  --output-path paired-end-demux.qza \
  --input-format PairedEndFastqManifestPhred33
```
We can visualise the output by creating a visualisation file qzv:


```
qiime demux summarize   --i-data paired-end-demux.qza   --o-visualization demux.qzv
```


**Forward reads**


**Total Sequences Sampled**|**10000**
:-----:|:-----:
2%|46 nts
9%|106 nts
25%|115 nts
50% (Median)|117 nts
75%|117 nts
91%|200 nts
98%|200 nts

**Forward reads**


**Reverse reads**|**10000**
:-----:|:-----:
2%|46 nts
9%|106 nts
25%|115 nts
50% (Median)|117 nts
75%|117 nts
91%|200 nts
98%|200 nts

### Denoising

```
#!/bin/sh
# source activate /scale_wlg_persistent/filesets/project/uoo00116/repos
qiime dada2 denoise-paired \
 --i-demultiplexed-seqs paired-end-demux.qza \
 --o-representative-sequences rep-seqs-dada2.qza \
 --o-table table-dada2.qza \
 --p-n-threads 8 \
 --p-trunc-len-f 0 \
 --p-trunc-len-r 0 \  
 --o-denoising-stats stats-dada2.qza 
```

Visualising the denoising :


```
qiime metadata tabulate \
  --m-input-file stats-dada2.qza \
  --o-visualization stats-dada2.qzv

qiime tools export --input-path rep-seqs-dada2.qza --output-path dna_sequences
```


### Feature classifier

I need to create my own feature classifier in order to assign taxonomy to the features. This process is detailed in [create_classifier.md](create_classifier.md)


Once I created my featureclassifier, I assign my features to features.

 This takes quite some temporary space. I therefore create a tmp folder and use it as the tmp folder for qiime to work on:

```
mkdir /home/ludovic.dutoit/projects/tmp
export TMPDIR="/home/ludovic.dutoit/projects/tmp"
```

and then  I can finally assign stuff!

```
qiime feature-classifier classify-sklearn \
  --i-classifier classifier.qza \
  --i-reads  rep-seqs-dada2.qza \
  --o-classification taxonomy.qza

qiime metadata tabulate \
  --m-input-file taxonomy.qza \
  --o-visualization taxonomy.qzv



qiime taxa barplot \
  --i-table table-dada2.qza \
  --i-taxonomy taxonomy.qza \
  --m-metadata-file ~/repos/scripts/YEP_diet/metadata/sample_metadata.tsv \
  --o-visualization taxa-bar-plots.qzv
```

Using [Qiime2 view](https://view.qiime2.org) and the file taxa-bar-plots.qzv I downloaded this at the genes and the species level in output/level5allmetazoan.txt and output/level6allmetazoan.txt

### Alpha rarefaction


I want to know wether each sample has enough depth of sequencing. I conduct alpha rarefaction analysis after struggling with the format of metadata.

```
qiime diversity alpha-rarefaction \
  --i-table table-dada2.qza \
  --p-max-depth 4000 \
  --m-metadata-file  ~/repos/scripts/YEP_diet/metadata/sample_metadatarare.tsv \ 
  --o-visualization alpha-rarefaction.qzv
 ```

 I download the csv output from qiime view on alpha-rarefaction.qzv in [output/observed_otus_alpha_rare.csv](output/observed_otus_alpha_rare.csv). I analysed it using [alpharare.R](alpharare.R) to generate plots per sample and a tata summary in [output/summaryalpharare](output/summaryalpharare)