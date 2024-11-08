#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:31:30 2024

@author: glombik
"""
from Bio import SeqIO 
import argparse

def extract_fasta_seqs(input_file, output_file, list_of_contigs):    
    with open(list_of_contigs) as file:
        lines1 = [line.strip() for line in file]
    with open(output_file,'w') as f:
        
        with open(input_file) as fasta_in:
            for record in SeqIO.parse(fasta_in,'fasta'):
                if record.name in lines1:
                        f.write(str(record.format('fasta')))
                        print("{} added to output.".format(record.name))

            

if __name__ == "__main__":
# Set up the argument parser
    parser = argparse.ArgumentParser(description='Split a tab-delimited file into multiple files based on the first column.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input fasta file')
    parser.add_argument('-o', '--output', required=True, help='Directory/file to save the output files')
    parser.add_argument('-n', '--names', required=True, help='Path to the list of names')

# Parse the arguments
args = parser.parse_args()

# Call the function with provided arguments
extract_fasta_seqs(args.input, args.output, args.names)
