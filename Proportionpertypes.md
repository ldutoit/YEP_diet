## Non chimeric contain data that go into taxonomic assignment

stats-dada2chordates.qzv contains number of reads after denoinsing


**Non target include unnasigned as we expect fished to be at least fishes even if not in db**



after visualisation in view.qiime2.org we visualisa it quickly and download the file as metadatachordates.tsv before adding extra info.


## proportion


we downloaded the file taxa-bar-plotschordates.qzv before downloading the csv file at the species level.

I summarised it simply uysing the SUM function to add 4 columns:

```
total_before_assigned	
hohio	
targetActinopteri_sequences)	
other non target ( included unassigned at the embranchment level )
```

I saved the file as  prop_per_type.csv
I then put that data together with the metadata file using R. I also removed the low quality samples simply by removing all the samples that are not in:

"taxa-bar-plotschordates100min2000.qzv" that I downloaded just for this purpoise as "final_table_chordates.csv"


That was done using *merged_readstaxotypes.R*

The final output is : chordates_proportion_tables.txt

It will be good to add a column (usable reads) that only contains the sum of reads for taxonomic units that are used in the paper, but that depends a bit on Mel's final filtering of taxonomic units, so it is not reported here.





