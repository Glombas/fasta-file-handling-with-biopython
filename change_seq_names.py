#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:31:30 2024

@author: glombik
"""
#add SeqIO, made to handle fasta sequences
from Bio import SeqIO
#add argparse to pass arguments when running the script (see below)
import argparse

#define a function to change the sequence names/headers
def adjust_fasta_names(input_file, output_file, list_of_names):    
#start with an empty dictionary for sequence names
    name_updates = {}

#open the file with list of names (tab separated), read it line by line and create an entry into the dictionary keeping the connection between the current (old) name and the new name
    with open(list_of_names) as file:
        for line in file:
            line = line.strip()
            read = line.split("\t")
            old_name = read[0].strip()
            updated_name = read[1].strip()
            name_updates[old_name] = updated_name

    #open the output file for writing            
    with open(output_file,'w') as adjusted:

    #open the input file with sequences, strip the name (header) and if there is a match to the dictionary, update the name with a new one.
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

# Call the function with provided arguments (see above)
adjust_fasta_names(args.input, args.output, args.names)
