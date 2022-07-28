# Pre-Orthofinder-Code
For renaming directories containing genomic data after an ncbi batch data packet download from their assembly accesssion to their organism name

Recently, I had to download some data packets through the ncbi gui, and found that the data was all contained in a folder that had the assembly accession number. This python script uses the assembly_data_report.jsonl file that comes with it to rename all of the data packet directories from their assembly accession to their organism ID. 

Be warned: I only tested it on my data, and I recommend making a copy of your data packets as backup because you can't undo the directory change.
