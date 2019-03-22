addmeadatatofinaltable.R

metadata<-read.table("/Users/dutlu42p/repos/mahuika/YEP_diet/metadata/sample_metadataextended.tsv",h=T)
cephalo<-read.csv("cephalolevel6.csv",h=T)#after changing name of first column to
colnames(cephalo)[1]<-"sample.id"
final<-merge(cephalo,metadata,by="sample.id")


cephalo[,1]%in%final[,1]

write.table(final,"final_table_cephalo.csv",row.names=F,quote=F,sep=",")

