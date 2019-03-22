## Non chimeric contain data that go into taxonomic assignment

stats-dada2cephalo.qzv contains number of reads after denoinsing


**Non target include unnasigned as we expect fished to be at least fishes even if not in db**



after visualisation in view.qiime2.org we visualise it quickly and download the file as metadatacephalo.tsv before adding extra info.


## proportion


we downloaded the file taxa-bar-plotscephalo.qzv before downloading the csv file at the species level.
\
I summarised it simply uysing the SUM function to add 4 columns:

```
total_before_assigned	
hohio	
targetcephalopoda_sequences	
othernontarget
```

I saved the file as  prop_per_typecephalo.csv
I then put that data together with the metadata file using R. I also removed the low quality samples simply by removing all the samples that are not in the final dataset.




That was done using *merged_readstaxotypescephalo.R*

The final output is : cephalo_proportion_tables.txt

It will be good to add a column (usable reads) that only contains the sum of reads for taxonomic units that are used in the paper, but that depends a bit on Mel's final filtering of taxonomic units, so it is not reported here.





