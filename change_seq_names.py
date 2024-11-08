#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:31:30 2024

@author: glombik
"""
from Bio import SeqIO 
import argparse

def adjust_fasta_names(input_file, output_file, list_of_names):    
    name_updates = {}
    
    with open(list_of_names) as file:
        for line in file:
            line = line.strip()
            read = line.split("\t")
            old_name = read[0].strip()
            updated_name = read[1].strip()
            name_updates[old_name] = updated_name
            
    with open(output_file,'w') as adjusted:
        
        with open(input_file) as fasta_in:
            for record in SeqIO.parse(fasta_in,'fasta'):
                record_id = record.id.strip()
                if record_id in name_updates:
                    print("found match in {}.".format(record.name))
                    record.id = name_updates[record_id]
                    record.description = name_updates[record_id]
                SeqIO.write(record,adjusted,'fasta')
      
            

if __name__ == "__main__":
# Set up the argument parser
    parser = argparse.ArgumentParser(description='Adjust fasta file headers based on list in names file ')
    parser.add_argument('-i', '--input', required=True, help='Input fasta file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('-n', '--names', required=True, help='List of new names')

# Parse the arguments
args = parser.parse_args()

# Call the function with provided arguments
adjust_fasta_names(args.input, args.output, args.names)