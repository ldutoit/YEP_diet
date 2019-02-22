#create_classifier_primers_spec.md

This file creates two classifiers, those are primers specific.

The starting point is the database clipped for the reference primers

#Create folder
mkdir 
cd taxo_primerspec/
 
##get files in
cp ../taxonomy_round2/ref-seqschor/dna-sequences.fasta ref-seqschor.fa
cp ../taxonomy_round2/ref-seqsceph/dna-sequences.fasta ref-seqsceph.fa
cp ../taxonomy_round2/ref-taxonomy.qza .
#add mel sequences

echo ">MEL00002.1
CCCCTTCAGAGAGGGCCAAATTAAGTGACCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGAAGCACTTATCCCCCACGTAGGCTGGGAAAACCTCCTATAAACAAGAGCTTCAGCTCTAATAATCAGAACCTCTGACTAAAAATGATCCGGCAAAGCCGATCAACGGACCGAGTTACCCTAGGGATAACAGCGCAATC
>MEL00003.1
ACCCTAAACAAAGGACTGAACTGAACAAACCATGCCCCTCTGTCTTAGGTTGGGGCGACCCCGAGGAAACAAAAAACCCACGAGTGGAATGGGAGCACTGACCTCCTACAACCAAGAGCTGCAGCTCTAACTAATAGAATTTCTAACCAATAATGATCCGGCAAAGCCGATTAACGAACCAAGTTACCCTAGGGATAAAGCGCAATC
>MEL00004.1
CCCCCAGACAAGGGGCCAAACCAAATGATCCCTGCCCTAATGTCTTTGGTTGGGGCGACCGCGGGGCAACAAAAAACCCCCACGTGGAATGGGACTATCCTCCTACAAACAAGAGCTGCAGCTCTAGTTCACAGAATTTCTGACCAATAAGATCCGGCAAAGCCGATCAACGAACCGAGTTACCCTAGGGATAAAGCGCAATC
>MEL00001.1
GCCCCCTAAAAGGCAACAAGCCAGTAACCTCATTTTAATATCTTTAGTTGGGGCGACCGCGGAGTAAAACAAAACCTCCGTGAGGATTGAGGTAAAACCTTATACCTAAGAAAGTCATTTCTAAGCACCAAAATATTTGACCTAAAGATCCGGCAATAGCCGATCAACGAACCTAGTTACCCCAGGGATAAAGCGCAATC" > melseq.fa


cat melseq.fa ref-seqsceph.fa  > ref-seqscephwithmel.fa
cat melseq.fa ref-seqschor.fa  > ref-seqschorwithmel.fa



## IMPORT and train

### Chordates

```
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path ref-seqschorwithmel.fa \
  --output-path allrecordsncbi_clippedchor.qza

qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads allrecordsncbi_clippedchor.qza \
  --i-reference-taxonomy  ref-taxonomy.qza \
  --o-classifier classifierchor.qza
```
### Cephalo

```
qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path ref-seqscephwithmel.fa \
  --output-path allrecordsncbi_clippedceph.qza

qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads allrecordsncbi_clippedceph.qza \
  --i-reference-taxonomy  ref-taxonomy.qza \
  --o-classifier classifierceph.qza
```
NOTES :Look into fixing sequences of Mel (i.e. length), are they actually in?