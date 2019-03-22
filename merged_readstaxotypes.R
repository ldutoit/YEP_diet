#merged_readstaxotypes.R



metadata= read.table("metadatachordates.tsv",h=T)
prop_per_type = read.table("prop_per_type.csv",h=T,sep=",")

final_table_with_excluded_samples =read.csv("final_table_chordates.csv",h=T) # after replacing the first column by something else than index



metadata[,1]==prop_per_type[,1]
#

#  [1] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
# [16] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
# [31] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
# [46] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
# [61] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
# [76] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
# [91] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[106] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[121] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[136] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[151] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[166] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[181] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[196] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#[211] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE


final_prop_table =cbind(metadata, prop_per_type)


final_prop_table_right_samples = final_prop_table[which(final_prop_table[,1]%in%final_table_with_excluded_samples[,1]),]
colnames(final_prop_table_right_samples)
# [1] "sample.id"                    "input"
# [3] "filtered"                     "denoised"
# [5] "merged"                       "non.chimeric"
# [7] "index"                        "total_before_assigned"
# [9] "ohio"                         "target_Actinopteri_sequences"
#[11] "Other_non_target"


#Removing a few un9nteresting columns
final_prop_table_right_samples<-final_prop_table_right_samples[,c(1,8,9,10,11)]
colnames(final_prop_table_right_samples)



write.table(final_prop_table_right_samples,"chordates_proportion_tables.txt",quote=F,row.names=F,sep="\t")
