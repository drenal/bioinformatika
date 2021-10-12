#!/usr/bin/env python3
"""
Rosalind GC content counter problem: http://rosalind.info/problems/gc/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))
from utils import read_fasta, count_letter_percentages

sequences = read_fasta(sys.argv[1])
gc_content = {}
for s in sequences:
    perc = count_letter_percentages(sequences[s])
    gc_content[s] = perc["G"] + perc["C"]

max_gc_seq = max(gc_content, key=gc_content.get)

print(max_gc_seq)
print("{:.6f}".format(gc_content[max_gc_seq]*100))






