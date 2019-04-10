#!/usr/bin/env python 3

import Bio
from Bio import SeqIO


# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'


# open the FASTA file
fsa = open(fasta_file)


for fsa in SeqIO.parse("watermelon.fsa", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record)





