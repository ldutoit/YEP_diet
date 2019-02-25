# Remove primers 

cephalo primers
forward: forward GACGAGAAGACCCTAWTGAGCT
referse: AAATTACGCTGTTATCCCT


chordates
forward: CGAGAAGACCCTRTGGAGCT
referse: TATCCTNGGTCGCCCCAAC

this is done according to the [cutadapt recipe](
https://cutadapt.readthedocs.io/en/stable/recipes.html#trimming-amplicon-primers-from-both-ends-of-paired-end-reads)

The basic command associated to the construction of the library is:
```
cutadapt -a FWDPRIMER...RCREVPRIMER -A REVPRIMER...RCFWDPRIMER --discard-untrimmed -o out.1.fastq.gz -p out.2.fastq.gz in.1.fastq.gz in.2.fastq.gz
```

##CHORDATES


```
output=clean_nexterachordatestrimmed/ 
mkdir -p $output
for file in $(ls clean_nexterachordates/*val_1.fq);
do
echo $file
base=$(basename $file 'R1_001_val_1.fq')
cutadapt -a CGAGAAGACCCTRTGGAGCT...GTTGGGGCGACCNAGGATA -A TATCCTNGGTCGCCCCAAC...AGCTCCAYAGGGTCTTCTCG --discard-untrimmed -o $output$base'R1_001_val_1.fq'  -p  $output$base'R2_001_val_2.fq' clean_nexterachordates/$base'R1_001_val_1.fq' clean_nexterachordates/$base'R2_001_val_2.fq' 
done
```
###CEPHALO

```
output=clean_nexteracephalotrimmed/ 
mkdir -p $output
for file in $(ls clean_nexteracephalo/*val_1.fq);
do
echo $file
base=$(basename $file 'R1_001_val_1.fq')
cutadapt -a GACGAGAAGACCCTAWTGAGCT...AGGGATAACAGCGTAATTT -A AAATTACGCTGTTATCCCT...AGCTCAWTAGGGTCTTCTCGTC --discard-untrimmed -o $output$base'R1_001_val_1.fq'  -p  $output$base'R2_001_val_2.fq' clean_nexteracephalo/$base'R1_001_val_1.fq' clean_nexteracephalo/$base'R2_001_val_2.fq' 
done
```