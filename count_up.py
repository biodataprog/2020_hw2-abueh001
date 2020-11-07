#!/usr/bin/env python3

# this is a python script template
# this next line will download the file using curl

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,csv,re,sys

# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence



if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
with gzip.open(gff,"rt") as fh:
    # now add code to process this
    gff = csv.reader(fh,delimiter="\t")
    numbergenes = 0
    totgenelength = 0
    genelength = 0
    for row in gff:
        if row[0].startswith("#"):
            continue
            
        if "gene" == row[2]:
            numbergenes += 1
            genelength = int(row[4])-int(row[3])
            totgenelength += genelength
   
        
        
    print("The number of genes is:",numbergenes)
    print("The total gene length is:",totgenelength,"bp")
      
with gzip.open(fasta,"rt") as fh: 
    pairs = aspairs(fh)
    seqs = dict(pairs)
    for a,b in seqs.items():
        seq_id = a
        seq = b
        bp = 0
        
    for line in seq:
        bp +=len(line)
        
print("The sequence length is:",bp,"bp")
print("The coding percentage of the genome is:","{0:.2%}".format(totgenelength/bp))
        
