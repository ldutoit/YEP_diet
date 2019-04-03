# to get the complete numbers



	data<-read.table("observed_otus.csv",h=T,sep=",")
	head(data)
	dir.create(output_dir)
	# there are 10 iterations for 10 different depths, I create a  x axis for my plot
	x<- gsub("depth.","",colnames(data)[2:101],perl=T)
	x<- gsub("_iter.[0-9]+","",x,perl=T)
	x<-as.numeric(x)

	data<-data[,2:101]
	data<-data[complete.cases(data),]


	newdata<-data
	for (row in 1:dim(data)[1]){
		data[row,]/data[row,100]
		newdata[row,]=data[row,]/max(data[row,])
	}


	defmean_no<-function(x){return (mean(as.numeric(as.character(x)),na.rm=T))}
	averagedata<-apply(newdata,2,defmean_no)

	stdev_no_na<-function(x){return (sd(as.numeric(as.character(x)),na.rm=T))}
	stderr<-apply(newdata,2,stdev_no_na)/sqrt(dim(newdata)[1])
#Figure SX: Alpha rarefaction curves for ray-finned fishes. 175 samples with more than 3000 ray-finned fishes reads were randomly sampled for different number of sequences. The y-axis represents the average percentage of the total number of independent type of sequences (i.e. QIIME 2 features) within each sample detected at each depth. The error bars represent the .

	pdf("sampled_alpha_chordates.pdf")
	plot(x[seq(1,100,by=10)],averagedata[seq(1,100,by=10)],pch=19,cex.axis=1.5,ylim=c(0,1.1),type="b",xlab="sampled depth",ylab = "% of total features detected",cex.lab=1.5)
	arrows(x[seq(1,100,by=10)],averagedata[seq(1,100,by=10)]-1.974*stderr[seq(1,100,by=10)],x[seq(1,100,by=10)],averagedata[seq(1,100,by=10)]+1.974*stderr[seq(1,100,by=10)],length=0.05,angle=90,code=3)
	dev.off()
# for markdown file
	png("/home/ludovic.dutoit/repos/scripts/YEP_diet/output/sampled_alpha_chordates.png")
	plot(x[seq(1,100,by=10)],averagedata[seq(1,100,by=10)],pch=19,cex.axis=1.5,ylim=c(0,1.1),type="b",xlab="sampled depth",ylab = "% of total features detected",cex.lab=1.5)
	arrows(x[seq(1,100,by=10)],averagedata[seq(1,100,by=10)]-1.974*stderr[seq(1,100,by=10)],x[seq(1,100,by=10)],averagedata[seq(1,100,by=10)]+1.974*stderr[seq(1,100,by=10)],length=0.05,angle=90,code=3)
	dev.off()


