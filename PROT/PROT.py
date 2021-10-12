#!/usr/bin/env python3
"""
Rosalind problem PROT: http://rosalind.info/problems/prot/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))

from utils import rna_to_prot, read_in_file_as_string

rna = read_in_file_as_string(sys.argv[1])
aa = rna_to_prot(rna)
print(aa)
