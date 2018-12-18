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

/home/ludovic.dutoit/projectsmb://storage.hcs-p01.otago.ac.nz/sci-zoology-kakapogenome/Ludo/YEP_poo_16S_eDNAs/Danioreriohypoxia/source_files/

Metadata info *tocome*

## Source files
the original data comes consists of 16S samples for 220 penguins.
## Analyses

### Quick and Dirty

I did a first quick and VERY dirty run through QIIME2 on 10 samples to see what is happening ( see [quickanddirtyqiime.md](quickanddirtyqiime.md))
That allowed me to detect:

S1 is the metagenomics sample ( not ampliconic).

There is plenty of fish.

The fastqc also shows large amount of nextera transposase left.


### Clean run



I start by cleaning the nextera transposase using [removenextera.sh](removenextera.sh). I also add a Quality threshold of a PHREDscore 25 using TrimGalore.

Analyses done in QIIME2 explaineed in [QIIME2pipe.md](QIIME2pipe.md)
