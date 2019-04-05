#!/usr/bin/env python3


#read the files in, open files

fasta = "watermelon.fsa"
genome = open(fasta, "r")


filename = "watermelon.gff"
gff = open(filename, "r")


#reading line by line

for line in gff:
	line = gff.readline()

    #skip blanks
	if not line.strip():


    #remove line breaks
    line = line.rstrip('\n')
    
#split based on tabs
#sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')

fields = line.split('\t')
print(fields[3], fields[4])

#extract the DNA seqeuence from the genome for this feature (corresponds to the coordinates in GFF)
#substring = []

trimmed_dna = dna[0:]

#print the DNA sequence for this feature

output.write(trimmed_dna)
for dna in file:
print(dna)

#calculate GC content for this feat

my_dna = gff

length = (my_dna)
g_count = my_dna.count('G')
c_count = my_dna.count('C')
gc_content = (g_count + c_count) / length

print("GC content is " + str(gc_content))










