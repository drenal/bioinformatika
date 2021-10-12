#!/usr/bin/env python3
"""
Rosaling DNA reverse complementer problem: http://rosalind.info/problems/revc/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))

from utils import read_in_file_as_string, revc

dna = read_in_file_as_string(sys.argv[1])
revc = revc(dna)
print(revc)
