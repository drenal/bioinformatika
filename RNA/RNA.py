#!/usr/bin/env python3
"""
Rosaling RNA problem: http://rosalind.info/problems/rna/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))

from utils import read_in_file_as_string, dna_to_rna

dna = read_in_file_as_string(sys.argv[1])
rna = dna_to_rna(dna)
print(rna)
