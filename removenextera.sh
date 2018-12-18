#1/bin/sh
module load TrimGalore

mkdir clean_nextera





for read1  in $(ls source_files/OG3968ampli/*R1_001.fastq)
	do 
	read2=$(echo $read1| sed -s s/R1/R2/)
	base=$(basename $read1 )
	trim_galore --stringency 5 --dont_gzip --trim1 --length 30 -q 25 --paired --nextera  -o clean_nextera $read1 $read2
done
