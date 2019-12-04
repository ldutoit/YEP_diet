# YEP_diet

## Description
Looking at prey detection from faecal samples of yellow eyed penguins. Sequenced 16S paired-end reads.

## Key Players
Mel Young (PhD student Zoology)
Bruce Robertson (PI)
Professor Yolanda van Heezik (PI)

## Objectives
Obtain presence absence for all yellow-eyed penguin diet species.

## Physical location of the data
For now, the raw data is on the Robertson lab HCS storage  at otago uni:

/home/ludovic.dutoit/projectsmb://storage.hcs-p01.otago.ac.nz/sci-zoology-kakapogenome/Ludo/YEP_poo_16S_eDNAs/

The processed and archive data is stored on : ...


## Output files

Those files are in the output folder and are to be archived with the manuscript:


[cephalo_proportion_tables.txt](output/cephalo_proportion_tables.txt) contains the broad classification of sequences into target and non target species for cephalopods sequences.

[chordates_proportion_tables.txt](output/chordates_proportion_tables.txt) contains the broad classification of sequences into target and non target species for chordates sequences.
[final_table_cephalo.csv](output/final_table_cephalo.csv) Contains the taxonomically assigned cephalo dataset
[final_table_chordates.csv](output/final_table_chordates.csv) Contains the taxonomically assigned chordates dataset
[taxonomy_cephalo.qzv](output/taxonomy_cephalo.qzv) match unique sequences to taxonomy with confidence score
[taxonomy_chordates.qzv](output/taxonomy_chordates.qzv) match unique sequences to taxonomy with confidence score
[sampled_alpha_chordates.png](output/sampled_alpha_chordates.png) figure S2 for alpha rarefaction
[observed_otus.csv](output/observed_otus.csv) raw data for alpha rarefaction plot

## Source files
the original data consists of 16S samples for 220 penguins. 1 is metagenomic data. The other 219 are 16S amplicon sequenced with 2 pairs of primers, one to amplify a cephalopod 16S fragment and one to amplify a fish 16S fragment.

## Analyses

### Quick and Dirty

I did a first quick and VERY dirty run through QIIME2 on 10 samples to explore what was happening ( see [quickanddirtyqiime.md](quickanddirtyqiime.md))
That allowed me to detect:

S1 is the metagenomics sample (not ampliconic).

There is plenty of fish.

The fastqc also shows large amount of nextera transposase left:

```
mkdir fastqc
fastqc source_files/OG3968_fastq/*.fastq -o fastqc
```

## Clean Run on different primer pairs

The general idea is to separate the two primer pairs in two datasets.

I start by cleaning the nextera transposase using [removenextera.sh](removenextera.sh). I also add a Quality threshold of a PHRED score 25 using TrimGalore.


This was done by separating the fastq file according to the first 6bp of both primers using [sort_by_primers.py](sort_by_primers.py). I also need to remove the primers in the sequences, I do it using [removeprimers.md](removeprimers.md)

We then ran two independant analysis:

**[QIIME2pipeCHORDATES.md](QIIME2pipeCHORDATES.md)**

**[QIIME2pipeCEPHALO.md](QIIME2pipeCEPHALO.md)**

I then summarised the info at the population level using [summary_features_taxonomy_primerpsec.md](summary_features_taxonomy_primerpsec.md) this allows to identify common sequences ( occurence or abundance) that are missing taxonomic assignment and to work on them by improving the database.



## Downstream filtering

We filtered sequences a bit further before visualisation using [downstreamfiltering.md](downstreamfiltering.md)

[output/final_table_cephalo.csv](output/final_table_cephalo.csv)
[output/final_table_chordates.csv](output/final_table_chordates.csv)

## Proportion per types

[Proportionpertypeschordates.md](Proportionpertypeschordates.md) allows us to look at which proportion of the reads inputted are usable for chordates ( target species sequenced with enough data) vs which proportion of the data is Hohio, non-target species or target species with low taxonomic resolution / quality of sequence.

This is repeated in [proportionpertypescephalo.md](proportionpertypescephalo.md)

We outputted:

[output/cephalo_proportion_tables.txt](output/cephalo_proportion_tables.txt)
[output/chordates_proportion_tables.txt]([output/chordates_proportion_tables.txt])


## completeness of database
*This has not been edited after adding opalfishes, so the opalfish have been updates*
We compared the list of records to the species presnece in our databases using [specieslist_vs_database_primer_spec.py](specieslist_vs_database_primer_spec.py) and a bit of manual editing to produce the file: [metadata/database_completedness.csv](metadata/database_completedness.csv). 


## Alpha rarefaction

It is done within downstreamfiltering.md using a downloaded alpha rarefaction qzv file into the script evaluatealphararechordates.R


