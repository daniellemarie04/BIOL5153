#!/usr/bin/env python3

import argparse
import csv 
import Bio
from Bio import SeqIO

# create an ArgumentParser object ('parser') that will hold all the information necessary
# to parse the command line
parser = argparse.ArgumentParser(description = "generates a PBS job script for the AHPCC Trestles cluster")

# add positional (required) arguments
parser.add_argument( "watermelon_fasta", help = "watermelon_fasta")
parser.add_argument( "watermelon_gff", help = "watermelon_gff" )

# specify the input files
fasta_file = 'watermelon.fsa'

# open the FASTA file
fsa = open(fasta_file)

#read the files in, open files with csv
with open('watermelon.gff', 'r') as melon:
    #create a csv reader object
    csvreader = csv.reader(melon, delimiter=',')
    for line in csvreader:
            if not line:
                continue
            else:
            
                for line in melon:
                    print(line)


for fsa in SeqIO.parser("watermelon.fsa", "fasta"):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))

#sequence, source, features, begin, end, length, strand, phase,
attributes = line.split('\t')

fields = line.split('\t')
print(fields[3], fields[4]

#extract the DNA sequence from the genome for this feature 

substring = []

trimmed_dna = dna[0]

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

#print reverse complement of strands

def complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    bases = list(seq) 
    bases = [complement[base] for base in bases] 
    return ''.join(bases)
    def reverse_complement(s):
        return complement(s[::-1])

  print("reverse_complement")
