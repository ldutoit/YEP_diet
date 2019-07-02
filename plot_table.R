#From table 2

adult_fresh_fish<-c(60.9, 3.4, 17.9+17.8)
adult_latrines_fish<-c(51.8,1,13+34.2) # brought back to 100 for pres
adult_fresh_cephalo<-c(0.4, 0, 99.6)
adult_latrines_cephalo<-c(2.5,0,97.5)


data<-cbind(adult_fresh_fish,adult_latrines_fish,adult_fresh_cephalo,adult_latrines_cephalo)

#Ugy way of captuyring the labels
pdf("figtable2nolegend.pdf")
barplot(data, col=colors()[rev(c(23,89,12))] , border="white", font.axis=2, beside=F, names=c("Adult - Fresh", "Adult -Latrines","Adult - Fresh", "Adult -Latrines"),  font.lab=2,xlab="",ylab  = "proportion of sequences",legend= c("Target identified", "Target unidentified","Non-target"),ylim=c(0,1000))
dev.off()
apply(data,2,sum)

pdf("figtable2nolegend.pdf")
barplot(data, col=colors()[rev(c(23,89,12))] , border="white", font.axis=2, beside=F, names=c("Adult - Fresh", "Adult -Latrines","Adult - Fresh", "Adult -Latrines"),  font.lab=2,xlab="",ylab  = "proportion of sequences",)
dev.off()
apply(data,2,sum)
