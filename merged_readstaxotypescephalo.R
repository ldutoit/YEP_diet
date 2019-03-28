merged_readstaxotypescephalo






prop_per_type = read.table("prop_per_typecephalo.csv",h=T,sep=",")

final_table_with_excluded_samples =read.csv("final_table_cephalo.csv",h=T) # after replacing the first column by something else than index



colnames(prop_per_type)[1]<-"sample.id"
prop_per_type[,1]<-as.character(prop_per_type[,1])
final<-merge(prop_per_type,final_table_with_excluded_samples,by="sample.id")
colnames(final)


colnames(final)
#[1] "sample.id"
# [2] "total"
# [3] "Hohio"
# [4] "targetcephalopoda_sequences"
# [5] "othernontarget"
# [6] "Mollusca.Cephalopoda.Octopoda.Argonautidae.Argonauta.Argonauta_nodosa"
# [7] "Mollusca.Cephalopoda.Octopoda.Octopodidae.Enteroctopus.Enteroctopus_megalocyathus"
# [8] "Mollusca.Cephalopoda.Octopoda.Octopodidae.Octopus.__"
# [9] "Mollusca.Cephalopoda.Teuthida.Octopoteuthidae.__.__"
#[10] "Mollusca.Cephalopoda.Teuthida.Ommastrephidae.Nototodarus.__"
#[11] "Mollusca.Cephalopoda.Teuthida.Onychoteuthidae.Moroteuthopsis.Moroteuthopsis.aff..ingens.HEB.2018"
#[12] "Mollusca.Cephalopoda.Teuthida.__.__.__"
#[13] "Date"
#[14] "Samplequality"
#[15] "Breedingregion"
#[16] "Breedinglocation"
#[17] "Nestnumber"
#[18] "IndividualID"
#[19] "Ageclass"
#[20] "Statusof_bird1617"
#[21] "Time"
#[22] "Sex"
#Removing a few un9nteresting columns
final<-final[,-c(6:12)]
dim(final)

write.table(final,"cephalo_proportion_tables.txt",quote=F,row.names=F,sep="\t")

