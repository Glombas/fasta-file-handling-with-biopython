#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract sequences from a FASTA file EXCLUDING those listed in a names file.
"""

from Bio import SeqIO
import argparse

def extract_fasta_seqs_exclude(input_file, output_file, list_of_names):
    # Load names into a set for fast lookup
    with open(list_of_names) as file:
        names_set = {line.strip() for line in file if line.strip()}

    # Open input and output files
    with open(input_file) as fasta_in, open(output_file, 'w') as f_out:
        # Select sequences NOT in the list
        selected_records = (
            record
            for record in SeqIO.parse(fasta_in, 'fasta')
            if record.name not in names_set
        )

        count = SeqIO.write(selected_records, f_out, 'fasta')

    print(f"Extraction complete: {count} sequences written to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract sequences from a FASTA file excluding listed sequence names.'
    )
    parser.add_argument('-i', '--input', required=True, help='Path to the input FASTA file')
    parser.add_argument('-o', '--output', required=True, help='Path to save the output FASTA file')
    parser.add_argument('-n', '--names', required=True, help='Path to the list of sequence names to exclude')

    args = parser.parse_args()
    extract_fasta_seqs_exclude(args.input, args.output, args.names)
