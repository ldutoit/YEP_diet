# YEP_diet

## Description
Looking at prey detection from faecal samples of yellow eyed penguins. Sequenced 16S paired-end reads.

## Key Players
Mel Young (PhD student Zoology)
Bruce Robertson (PI)
Professor Yolanda van Heezik (PI)

## Objectives
Obtain presence absence for all YEP diet species.

## Physical location of the data
For now, the raw data is on the Robertson lab HCS storage  at otago uni:

/home/ludovic.dutoit/projectsmb://storage.hcs-p01.otago.ac.nz/sci-zoology-kakapogenome/Ludo/YEP_poo_16S_eDNAs/

The output files of qiime qzv and qza files are also there in processed_data (tocome)
Metadata info *tocome*

## Source files
the original data comes consists of 16S samples for 220 penguins. 1 is metagenomic data. The other 219 are 
## Analyses

### Quick and Dirty

I did a first quick and VERY dirty run through QIIME2 on 10 samples to see what is happening ( see [quickanddirtyqiime.md](quickanddirtyqiime.md))
That allowed me to detect:

S1 is the metagenomics sample ( not ampliconic).

There is plenty of fish.

The fastqc also shows large amount of nextera transposase left.




## Clean Run on different primer pairs

I start by cleaning the nextera transposase using [removenextera.sh](removenextera.sh). I also add a Quality threshold of a PHREDscore 25 using TrimGalore.

The idea is to separate the two primer pairs in two datasets.

This was done by separating the fastq file according to the first 6bp of both primers using [sort_by_primers.py](sort_by_primers.py). I also need to remove the primers drom the sequences, I do it using [removeprimers.md](removeprimers.md)

We then ran two independant analysis:

**[QIIME2pipeCHORDATES.md](QIIME2pipeCHORDATES.md)**

**[QIIME2pipeCEPHALO.md](QIIME2pipeCEPHALO.md)**

and then I summarise the info at the population level using [summary_features_taxonomy_primerpsec.md](summary_features_taxonomy_primerpsec.md)

this was by far the best approach. Probably also  because I removed the primers from the sequences.



## Downstream filtering

We filtered sequences a bit further before visualisation using [downstreamfiltering.md](downstreamfiltering.md)

!!FILL IN FINAL TABLES


## Proportion per types

[Proportionpertypes.md](Proportionpertypes.md) allows us to look at which proportion of the reads inputted are usable for chordates ( target species sequenced with enough data) vs which proportion of the data is Hohio, non-target species or target species with low taxonomic resolution / quality of sequence.

This is repeated in proportionpertypescephalo.md

!!FILMIN THE TWO FINAL TABLES