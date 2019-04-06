#!/usr/bin/env python3

# create an ArgumentParser object ('parser') that will hold all the information necessary
# to parse the command line
parser = argparse.ArgumentParser(description = "generates a PBS job script for the AHPCC Trestles cluster")

# add positional (required) arguments
parser.add_argument( "watermelon_fasta", help = "watermelon_fasta" )
parser.add_argument( "watermelon_gff", help = "watermelon_gff" )

#infile_name = "/Desktop/watermenlon_files"
#job_name = "
#queue = "available"
#walltime =00:30:00 
#ppn = 1

print("#PBS -N " + args.job_name)
print("#PBS -q " + args.queue)
print("#PBS -j oe")
print("#PBS -m abe")
print("#PBS -M dmaynard@uark.edu")
print("#PBS -o " + args.job_name + ".$PBS_JOBID") 
print("#PBS -l nodes=1:ppn=" + str(args.ppn))
print("#PBS -l walltime=" + str(args.walltime) + ":00:00" )

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










