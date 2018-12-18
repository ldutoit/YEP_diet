# quickanddirtyqiime.md


### Summary

### import the data, try on 10 samples

I follow [info](https://docs.qiime2.org/2018.11/tutorials/importing/#manifest-file) and a phred score quality [here](https://www.drive5.com/usearch/manual/quality_score.html) to be able to create the write import command.

First I created a [manifest](metadata/manifest10) file matching fastq to sample IDs. It should be noted than QIIME2 only accpets absolute paths for this. This also directly assign samples to fastq and the output file is therefore demultiplexed.

```
# module load QIIME2
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path ~/repos/scripts/YEP_diet/metadata/manifest10 \
  --output-path paired-end-demux10samples.qza \
  --source-format PairedEndFastqManifestPhred33
```
We can visualise the output by creating a visualisation file qzv:


```
qiime demux summarize   --i-data paired-end-demux.qza   --o-visualization demux.qzv
```

### Denoising

```
#!/bin/sh
# module load QIIME2
qiime dada2 denoise-paired \
  --i-demultiplexed-seqs paired-end-demux10samples.qza \
  --o-representative-sequences rep-seqs-dada2.qza \
  --o-table table-dada2.qza \
--p-trunc-len-f 190 \
--p-trunc-len-r 150 \
--p-n-threads 8 \
--verbose
```

### Taxonomy
```
qiime feature-table summarize \
  --i-table table-dada2.qza \
  --o-visualization table-dada2.qzv \

qiime feature-table tabulate-seqs \
  --i-data rep-seqs-dada2.qza \
  --o-visualization rep-seqs-dada2.qzv
 ```


Then I blast my features in rep-seqs-dada2.qzv to have an idea of what is in the sample.

I see plenty of fish, a bit of Staph. aureus and ecoli that I will remove before the clean run. 