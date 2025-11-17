#!/usr/bin/env python3
from Bio.Seq import Seq

gfa_file = "sub_mergedOG0000008.og.gfa"
out_fasta = "sub_mergedOG0000008.fasta"

segments = {}
paths = {}

# ---- First pass: read segment sequences ----
with open(gfa_file) as f:
    for line in f:
        if line.startswith("S"):
            fields = line.strip().split("\t")
            seg_id = fields[1]
            seq = fields[2]
            segments[seg_id] = seq

# ---- Second pass: process P lines ----
with open(gfa_file) as f, open(out_fasta, "w") as out:
    for line in f:
        if line.startswith("P"):
            fields = line.strip().split("\t")
            path_name = fields[1]     # sample name, e.g. "acu#1#A9:45603527-45621814"
            walk = fields[2].split(",")

            assembled = []

            for step in walk:
                if step == "*":  # skip wildcard
                    continue

                if step.endswith("+"):
                    seg = step[:-1]
                    seq = segments[seg]
                elif step.endswith("-"):
                    seg = step[:-1]
                    seq = str(Seq(segments[seg]).reverse_complement())
                else:
                    raise ValueError("Unexpected orientation in: " + step)

                assembled.append(seq)

            full_seq = "".join(assembled)

            # Write FASTA
            out.write(f">{path_name}\n")
            for i in range(0, len(full_seq), 80):
                out.write(full_seq[i:i+80] + "\n")

print("Done! FASTA written to", out_fasta)
