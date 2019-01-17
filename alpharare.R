
output_dir<-"/Users/dutlu42p/repos/mahuika/YEP_diet/output/summaryalpharare"
data<-read.table("/Users/dutlu42p/repos/mahuika/YEP_diet/output/observed_otus_alpha_rare.csv",h=T,sep=",")
head(data)
dir.create(output_dir)
# there are 10 iterations for 10 different depths, I create a  x axis for my plot
x<- gsub("depth.","",colnames(data)[2:101],perl=T)
x<- gsub("_iter.[0-9]+","",x,perl=T)
x

datasummary<-c()
for (i in 1:dim(data)[1]){
  y=c()
  for (j in 0:9){
    y[j+1]<-mean(as.numeric(data[i,(2+j*10):(2+j*10+9)]))
    print(c("Check:",data[i,(2+j*10):(2+j*10+9)]))
  }
  png(paste(output_dir,"/",data[i,1],".png",sep=""))
  plot(sort(as.numeric(levels(as.factor(x)))),  y,pch=19,main=data[i,1],xlab="depth",ylab="mean_taxfeature_number_10_iter")
  dev.off()
  datasummary<-rbind(datasummary,c(as.character(data[i,1]),y))
}

colnames(datasummary)<-c("sample_id",sort(as.numeric(levels(as.factor(x)))))
write.table(datasummary,paste(output_dir,"/alphadatasummary.txt",sep=""),sep="\t",row.names=F,col.names=F,quote=F)
