import os

#load bbmap
manifest_input = "/home/ludovic.dutoit/repos/scripts/YEP_diet/metadata/manifest"
manifest_merged  = open("/home/ludovic.dutoit/repos/scripts/YEP_diet/metadata/manifest_merged_reads","w")
output_folder = "/home/ludovic.dutoit/projects/edna_yep/clean_nextera_merged/"
#Read the manifest line by line#
with open(manifest_input) as f:
	for line in f:
		if not line.startswith("sample"):
			if "val_1" in line:
				forward = line.split(",")[1]
				backward=forward.replace("_val_1","_val_2").replace("R1","R2")
				command = "bbmerge.sh in1="+forward+" in2="+backward+" out="+output_folder+"/"+os.path.basename(forward).split(".")[0]+"_merged.fq outu1="+output_folder+"/"+os.path.basename(forward).split(".")[0]+"_unmergedforward.fq  outu2="+output_folder+"/"+os.path.basename(forward).split(".")[0]+"_unmergedreverse.fq"
				os.system(command)
				manifest_merged.write(line.replace(forward,output_folder+"/"+os.path.basename(forward).split(".")[0]+"_merged.fq"))
		else:
			manifest_merged.write(line)


manifest_merged.close()
			#merge
#look at proportion

#sample-id,absolute-filepath,direction
#sample-1,$PWD/some/filepath/sample1_R1.fastq,forward#
#
#

#then launch the whole thing



