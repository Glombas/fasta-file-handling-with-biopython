# fasta-file-handling-with-biopython

This repository contains a few scripts that I use frequently to change sequence names/filter fasta files.

## More scripts to be added when needed. 

[change_seq_names.py](change_seq_names.py) - Change sequence names based on the list provided
  
  options: -i input_fasta -o output_fasta -n name_file

_Note: the name_file needs to be a tab delimited file with 1st column containing old names and 2nd column containing new names._

[extract_fasta_seqs.py](extract_fasta_seqs.py) - extract sequences from fasta file BASED on the list provided
  
  options: -i input_fasta -o output_fasta -n name_file

[extract_minus_fasta_seqs.py](extract_minus_fasta_seqs.py) - extract sequences from fasta file MINUS the ones on the list provided
  
  options: -i input_fasta -o output_fasta -n name_file

[paths_gfa_to_fasta.py](paths_gfa_to_fasta.py) - extract full paths (segment "P" in the .gfa) from a subgraph/graph for every sample included in the graph.
