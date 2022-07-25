import json
import os
import sys

#open assembly data
#I found this method at https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data
#	after getting an error. I think it is because this is a jsonl, but not entirely sure. 

reports = []
for line in open("assembly_data_report.jsonl", "r"):
	reports.append(json.loads(line))

#to check type of reports
#print(type(reports))

#to check type of what's inside of reports
#print(type(reports[1]))

#checking length of reports
l = len(reports)
#print(l)

accession_list = []

organism_list = []

#reports is a list of dictionaries
for i in range(1,l):
	for k,v in reports[i].items():		#loop through reports
		typ = isinstance(v,dict)	#check if the report is a dict
		#print(typ)
		#if it is a dict, save the accession number and the organism name, if not, keep looping
		if typ:	
			for nk, nv in v.items():	#finding accesion name
				#print(nk,nv)	
				if nk == "assemblyAccession":
					accession_list.append(nv)	#append to accession list
				if nk == "biosample":			#organism names are in a nested dict with the key 'biosample'
					for key, value in nv.items(): 	#find the description dict within the biosample dict
						if key == "description":
							for o,on in value.items():#find the organism dict within the description dict within the biosample dict 
								if o == "organism":
									organism_list.append(on['organismName']) # save the organism name
				else:
					continue
		else:
			continue

#make the lists a dictionary	
acc_org = {accession_list[i]: organism_list[i] for i in range(len(accession_list))}

print(acc_org)

try:
	for k,v in acc_org.items():
		v = v.replace(" ", "_")		#replace spaces with underscores, change the if other naming scheme preferred
		if k[0:3] == "GCA":		#batch downloads from ncbi will download the genbank and refseq genomes for the same organism
			os.rename(k,v+"_gb")			#the conditionals distinguish the two, as GCF is usually for refseq and GCA is for genbank
		if k[0:3] == "GCF":			 
			os.rename(k,v+"_ref")
except BaseException as err:
    print("Unexpected {err=}, {type(err)=}")
    raise


